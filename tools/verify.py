"""Verify python examples in the course Markdown files.

Rules (see STYLE.md):
- ```python block followed (optionally after 'Output:' / blank lines) by ```text block: run and compare output.
- '<!-- no-verify -->' right before the python fence: skip.
- '<!-- error -->' right before the python fence: must fail; last line of the text block must match last stderr line.
Also flags em dashes and <details> blocks missing the blank line after </summary>.
"""
import os, re, subprocess, sys, tempfile

FENCE = re.compile(r"^```(\w*)\s*$")

def blocks(lines):
    i, out = 0, []
    while i < len(lines):
        m = FENCE.match(lines[i].strip()) if lines[i].lstrip().startswith("```") else None
        if m and lines[i].strip() != "```":
            lang = m.group(1); start = i; body = []; i += 1
            while i < len(lines) and lines[i].strip() != "```":
                body.append(lines[i]); i += 1
            indent = len(lines[start]) - len(lines[start].lstrip())
            body = [l[indent:] if l[:indent].strip() == "" else l for l in body]
            out.append((start, i, lang, "\n".join(body)))
        i += 1
    return out

def run(code):
    with tempfile.TemporaryDirectory() as d:
        f = os.path.join(d, "t.py")
        open(f, "w", encoding="utf-8").write(code)
        r = subprocess.run([sys.executable, "-I", f], capture_output=True, text=True, cwd=d, timeout=20, stdin=subprocess.DEVNULL)
        return r.returncode, r.stdout, r.stderr

norm = lambda s: "\n".join(l.rstrip() for l in s.strip("\n").splitlines()).strip()

def check_file(path):
    probs, n = [], 0
    text = open(path, encoding="utf-8").read()
    if "—" in text:
        probs.append(f"{path}: contains em dash")
    lines = text.splitlines()
    for i, l in enumerate(lines):
        if l.strip().startswith("<summary>") and i + 1 < len(lines) and lines[i + 1].strip() != "":
            probs.append(f"{path}:{i+1}: missing blank line after </summary>")
    bs = blocks(lines)
    for k, (s, e, lang, body) in enumerate(bs):
        if lang != "python":
            continue
        prev = ""
        j = s - 1
        while j >= 0 and lines[j].strip() == "":
            j -= 1
        if j >= 0: prev = lines[j].strip()
        if prev == "<!-- no-verify -->":
            continue
        nxt = bs[k + 1] if k + 1 < len(bs) else None
        if not nxt or nxt[2] != "text":
            continue
        between = [l.strip() for l in lines[e + 1:nxt[0]]]
        ok_between = lambda b: (not b) or b.lower().rstrip(":").strip("*") in ("output", "error", "result", "it prints", "answer") \
            or b.startswith("<details") or re.fullmatch(r"<summary>.*</summary>", b) is not None
        if not all(ok_between(b) for b in between):
            continue
        n += 1
        rc, so, se = run(body)
        where = f"{path}:{s+1}"
        if prev == "<!-- error -->":
            last = norm(se).splitlines()[-1] if se.strip() else ""
            exp = norm(nxt[3]).splitlines()[-1] if nxt[3].strip() else ""
            if rc == 0:
                probs.append(f"{where}: marked as error but ran fine")
            elif last != exp:
                probs.append(f"{where}: error mismatch\n  expected: {exp}\n  got:      {last}")
        else:
            if rc != 0:
                probs.append(f"{where}: crashed\n{se.strip()[-300:]}")
            elif norm(so) != norm(nxt[3]):
                probs.append(f"{where}: output mismatch\n--- expected\n{norm(nxt[3])}\n--- got\n{norm(so)}")
    return probs, n

paths = []
for a in sys.argv[1:]:
    if os.path.isdir(a):
        for root, _, files in os.walk(a):
            paths += [os.path.join(root, f) for f in sorted(files) if f.endswith(".md")]
    else:
        paths.append(a)
allp, total = [], 0
for p in sorted(paths):
    pr, n = check_file(p); allp += pr; total += n
print(f"{len(paths)} files, {total} examples run.")
if allp:
    print(f"{len(allp)} problem(s):\n" + "\n\n".join(allp)); sys.exit(1)
print("OK")
