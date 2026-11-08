"""Check the course: run every Markdown example and every guide.py.

Markdown rules:
- A ```python block followed by a ```text block (optionally after "Output:" or a
  <details>/<summary> header) is run, and its output must match the text block.
- "<!-- no-verify -->" right before the python fence: skip it.
- "<!-- error -->" right before the python fence: it must fail, and the last line
  of the text block must match the last line of the error.

Also flags em dashes, <summary> lines without a blank line after them, and runs
each module's guide.py with "all" to make sure every item works.

Usage: uv run tools/verify.py [files or folders]   (default: the whole course)
"""

import os
import re
import subprocess
import sys
import tempfile

FENCE = re.compile(r"^```(\w*)\s*$")
ALLOWED_LABELS = ("output", "error", "result", "it prints", "answer")


def find_blocks(lines):
    """Return (start, end, language, body) for every fenced code block."""
    found, i = [], 0
    while i < len(lines):
        match = FENCE.match(lines[i].strip())
        if match and lines[i].strip() != "```":
            start, body = i, []
            i += 1
            while i < len(lines) and lines[i].strip() != "```":
                body.append(lines[i])
                i += 1
            indent = len(lines[start]) - len(lines[start].lstrip())
            body = [row[indent:] if row[:indent].strip() == "" else row for row in body]
            found.append((start, i, match.group(1), "\n".join(body)))
        i += 1
    return found


def run_python(args, cwd):
    result = subprocess.run(
        [sys.executable, "-I", *args],
        capture_output=True,
        text=True,
        cwd=cwd,
        timeout=60,
        stdin=subprocess.DEVNULL,
    )
    return result.returncode, result.stdout, result.stderr


def run_snippet(code):
    with tempfile.TemporaryDirectory() as folder:
        path = os.path.join(folder, "snippet.py")
        with open(path, "w", encoding="utf-8") as file:
            file.write(code)
        return run_python([path], folder)


def normalize(text):
    return "\n".join(row.rstrip() for row in text.strip("\n").splitlines()).strip()


def is_label(row):
    return (
        not row
        or row.lower().rstrip(":").strip("*") in ALLOWED_LABELS
        or row.startswith("<details")
        or re.fullmatch(r"<summary>.*</summary>", row) is not None
    )


def line_before(lines, index):
    j = index - 1
    while j >= 0 and lines[j].strip() == "":
        j -= 1
    return lines[j].strip() if j >= 0 else ""


def check_markdown(path):
    problems, count = [], 0
    with open(path, encoding="utf-8") as file:
        text = file.read()
    if "—" in text:
        problems.append(f"{path}: contains an em dash")
    lines = text.splitlines()
    for i, row in enumerate(lines):
        followed_by_text = i + 1 < len(lines) and lines[i + 1].strip() != ""
        if row.strip().startswith("<summary>") and followed_by_text:
            problems.append(f"{path}:{i + 1}: missing blank line after </summary>")
    blocks = find_blocks(lines)
    for k, (start, end, language, body) in enumerate(blocks):
        if language != "python":
            continue
        marker = line_before(lines, start)
        nxt = blocks[k + 1] if k + 1 < len(blocks) else None
        if marker == "<!-- no-verify -->" or not nxt or nxt[2] != "text":
            continue
        if not all(is_label(row.strip()) for row in lines[end + 1 : nxt[0]]):
            continue
        count += 1
        code, out, err = run_snippet(body)
        where = f"{path}:{start + 1}"
        expected = normalize(nxt[3])
        if marker == "<!-- error -->":
            last = normalize(err).splitlines()[-1] if err.strip() else ""
            wanted = expected.splitlines()[-1] if expected else ""
            if code == 0:
                problems.append(f"{where}: marked as error but ran fine")
            elif last != wanted:
                problems.append(
                    f"{where}: error mismatch\n  expected: {wanted}\n  got:      {last}"
                )
        elif code != 0:
            problems.append(f"{where}: crashed\n{err.strip()[-300:]}")
        elif normalize(out) != expected:
            problems.append(
                f"{where}: output mismatch\n--- expected\n{expected}\n--- got\n{normalize(out)}"
            )
    return problems, count


def check_guide(path):
    code, _, err = run_python([os.path.basename(path), "all"], os.path.dirname(path) or ".")
    return [f"{path}: 'all' failed\n{err.strip()[-400:]}"] if code != 0 else []


def collect(targets):
    markdown, guides = [], []
    for target in targets:
        if os.path.isdir(target):
            for root, dirs, files in os.walk(target):
                dirs[:] = sorted(d for d in dirs if not d.startswith("."))
                for name in sorted(files):
                    full = os.path.join(root, name)
                    if name.endswith(".md"):
                        markdown.append(full)
                    elif name == "guide.py":
                        guides.append(full)
        elif target.endswith("guide.py"):
            guides.append(target)
        else:
            markdown.append(target)
    return markdown, guides


def main(targets):
    markdown, guides = collect(targets or ["."])
    problems, total = [], 0
    for path in markdown:
        found, count = check_markdown(path)
        problems += found
        total += count
    for path in guides:
        problems += check_guide(path)
    print(f"{len(markdown)} Markdown files, {total} examples run, {len(guides)} guides run.")
    if problems:
        print(f"{len(problems)} problem(s):\n\n" + "\n\n".join(problems))
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main(sys.argv[1:])
