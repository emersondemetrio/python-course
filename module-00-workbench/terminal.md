# The terminal

> **In one sentence:** the terminal is a window where you give the computer instructions by typing text commands instead of clicking.

## Why it matters

Programmers run their code from the terminal, install tools from the terminal, and use Git from the terminal. You do not need to become an expert, but you need to feel at home with a handful of commands. Ten commands cover almost everything in this course.

## Analogy

Think of your computer's folders as a building. Each folder is a room, and rooms can have doors to other rooms inside them.

When you use the file explorer, you walk around the building by clicking. In the terminal, you are standing in **one room at a time**, and you move by saying where you want to go: "go into the kitchen", "go back to the hallway", "what is in this room?". The terminal always knows which room you are standing in.

## The idea, step by step

### Opening the terminal

- **Windows:** press the Windows key, type `PowerShell`, press Enter.
- **macOS:** press Cmd + Space, type `Terminal`, press Enter.
- **Linux:** usually Ctrl + Alt + T.

Your editor (Cursor or VS Code) also has a terminal built in: menu **Terminal → New Terminal**. It works exactly the same way.

### The prompt

When the terminal opens, you see a line like this:

```powershell
PS C:\Users\ana>
```

On macOS or Linux it looks more like this:

```bash
ana@laptop:~$
```

This is the **prompt**. It means "I am ready, type a command". It also tells you where you are:

- `PS` means you are in **PowerShell**.
- `C:\Users\ana` is the **folder you are in right now**.
- On macOS and Linux, `~` is a short name for your **home folder** (like `/Users/ana` or `/home/ana`).

You type a command after the prompt and press **Enter** to run it.

### Paths

A **path** is the address of a file or folder. It lists every folder you pass through to get there.

```text
C:\Users\ana\Projects\hello.py        (Windows)
/Users/ana/Projects/hello.py          (macOS)
```

Read it like directions: start at `C:`, go into `Users`, then into `ana`, then into `Projects`, and there you find `hello.py`. Windows separates folders with `\` and macOS/Linux with `/`.

### `pwd`: where am I?

`pwd` stands for **print working directory**. "Directory" is another word for folder. The **working directory** is the folder you are standing in.

```powershell
PS C:\Users\ana> pwd

Path
----
C:\Users\ana
```

On macOS and Linux:

```bash
$ pwd
/Users/ana
```

### `ls`: what is in here?

`ls` stands for **list**. It shows the files and folders in the current folder.

```powershell
PS C:\Users\ana> ls

    Directory: C:\Users\ana

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----          08/11/2026    10:12                Desktop
d----          08/11/2026    10:12                Documents
d----          08/11/2026    10:15                Projects
```

A `d` in the `Mode` column means it is a **directory** (a folder). On macOS and Linux the output is shorter, and folders often appear in a different color:

```bash
$ ls
Desktop    Documents    Projects
```

### `cd`: go somewhere

`cd` stands for **change directory**. You write `cd` followed by the name of the folder you want to enter.

```powershell
PS C:\Users\ana> cd Projects
PS C:\Users\ana\Projects>
```

Look at the prompt: it changed. You are now inside `Projects`.

A good habit: **run `ls` before `cd`**, so you see the exact names of the folders you can enter.

### `cd ..` and `cd .`: up one level, and "right here"

Two special names exist in every folder:

- `..` (two dots) means **the folder above this one**, the "parent" folder.
- `.` (one dot) means **this folder, right here**.

```powershell
PS C:\Users\ana\Projects> cd ..
PS C:\Users\ana>
```

`cd .` means "go to the folder I am already in", so nothing changes. It looks useless now, but `.` shows up a lot later, for example in `cursor .` ("open the editor here").

You can also go through several folders at once:

```powershell
PS C:\Users\ana> cd Projects\course
PS C:\Users\ana\Projects\course> cd ..\..
PS C:\Users\ana>
```

### Tab: let the terminal type for you

Type the first letters of a folder name and press **Tab**. The terminal completes the name for you.

```powershell
PS C:\Users\ana> cd Pr       ← press Tab here
PS C:\Users\ana> cd .\Projects\
```

This saves time and, more importantly, avoids typos. If nothing happens, there is no match, or there are several (for example `Pictures` and `Projects` both start with `P`). Type one more letter and press Tab again.

### Clearing the screen and seeing past commands

- **Ctrl + L** or the command `clear` cleans the screen. Nothing is deleted, the old text is just moved out of sight.
- `history` lists the commands you typed before.
- The **up arrow** brings back the previous command, so you do not need to type it again.

### `echo` and `cat`: show text

`echo` prints text in the terminal, a bit like `print()` in Python:

```powershell
PS C:\Users\ana> echo "Hello"
Hello
```

`cat` shows the content of a file. In PowerShell, `cat` works too (its official name is `Get-Content`):

```powershell
PS C:\Users\ana\Projects> cat groceries.txt
eggs
milk
coffee
```

### Running a Python file

To run a Python program, you type `python` followed by the name of the file. You must be in the folder where the file is.

```powershell
PS C:\Users\ana\Projects> python hello.py
Hello, world!
```

On macOS and Linux, the command is often `python3`:

```bash
$ python3 hello.py
Hello, world!
```

If you type only `python` (with no file name), Python opens an interactive mode instead of running your file. More about that in [python.md](python.md).

### PATH: how the terminal finds programs

When you type `python`, how does the terminal know where the Python program is? It looks in a list of folders called the **PATH**. If the folder where Python was installed is on that list, the command works. If not, you get an error like this:

```powershell
PS C:\Users\ana> python
python : The term 'python' is not recognized as the name of a cmdlet, function, script file, or operable program.
```

This does not mean Python is missing. It means the terminal does not know **where** it is. The fix is to add Python's folder to the PATH (on Windows, reinstalling Python with the box **"Add python.exe to PATH"** checked is the easiest way). After changing the PATH, close the terminal and open a new one.

## Common mistakes

### Running a file from the wrong folder

```powershell
PS C:\Users\ana> python hello.py
python: can't open file 'C:\\Users\\ana\\hello.py': [Errno 2] No such file or directory
```

**Why:** you are in `C:\Users\ana`, but the file is in `C:\Users\ana\Projects`. Python looks for the file in the folder you are standing in.

**Fix:** go to the right folder first, then run the file.

```powershell
PS C:\Users\ana> cd Projects
PS C:\Users\ana\Projects> python hello.py
Hello, world!
```

### Typing the folder name wrong

```powershell
PS C:\Users\ana> cd projetcs
cd : Cannot find path 'C:\Users\ana\projetcs' because it does not exist.
```

**Why:** a typo. The terminal does not guess what you meant.

**Fix:** run `ls` to see the exact name, and use **Tab** to complete it.

### Folder names with spaces

```powershell
PS C:\Users\ana> cd My Projects
Set-Location : A positional parameter cannot be found that accepts argument 'Projects'.
```

**Why:** the terminal uses spaces to separate the parts of a command. It thinks `My` is the folder and `Projects` is something extra.

**Fix:** put the name in quotes, `cd "My Projects"`. Better yet, never use spaces in folder names (see [software-engineering.md](software-engineering.md)).

### Typing `python` alone and getting stuck

```powershell
PS C:\Users\ana\Projects> python
Python 3.13.0 ...
>>>
```

**Why:** without a file name, Python opens its interactive mode (the `>>>` prompt). Your file did not run.

**Fix:** type `exit()` and press Enter to leave, then run `python hello.py`.

## Exercises

### Predict the output

#### Exercise 1: Where am I?

You open the terminal and see `PS C:\Users\ana>`. Then you run:

```powershell
cd Projects
cd course
cd ..
pwd
```

What does `pwd` show?

<details>
<summary>Show answer</summary>

```text
C:\Users\ana\Projects
```

You went into `Projects`, then into `course`, then `cd ..` took you back up one level, to `Projects`.

</details>

#### Exercise 2: Up, up, up

You are in `C:\Users\ana\Projects\course\week1`. You run `cd ..\..`. Where are you now?

<details>
<summary>Show answer</summary>

```text
C:\Users\ana\Projects
```

Each `..` goes up one level: from `week1` to `course`, then from `course` to `Projects`.

</details>

#### Exercise 3: The dot

You are in `C:\Users\ana\Projects`. You run `cd .` and then `pwd`. What does it show?

<details>
<summary>Show answer</summary>

```text
C:\Users\ana\Projects
```

`.` means "this folder". Going to the folder you are already in changes nothing.

</details>

### Fix the bug

#### Exercise 4: The file that does not exist

The file `hello.py` is in `C:\Users\ana\Projects`. You type this and get an error:

```powershell
PS C:\Users\ana> python hello.py
python: can't open file 'C:\\Users\\ana\\hello.py': [Errno 2] No such file or directory
```

What commands fix it?

<details>
<summary>Show answer</summary>

```powershell
cd Projects
python hello.py
```

Python looks for the file in the current folder. First go to the folder where the file is, then run it.

</details>

#### Exercise 5: Two words

You created a folder called `python course` and this fails:

```powershell
cd python course
```

Give two ways to fix it.

<details>
<summary>Show answer</summary>

1. Use quotes: `cd "python course"`
2. Better: rename the folder to `python-course` (no spaces) and run `cd python-course`.

The second option avoids the problem forever.

</details>

### Write it

#### Exercise 6: A full trip

Starting in your home folder, write the commands to:

1. Show where you are.
2. List what is in the folder.
3. Go into `Projects`.
4. Show the content of a file called `notes.txt`.
5. Go back to your home folder.

<details>
<summary>Show answer</summary>

```powershell
pwd
ls
cd Projects
cat notes.txt
cd ..
```

On macOS or Linux the commands are the same.

</details>

#### Exercise 7: Practice on your own computer

Open a terminal and, without looking at this page:

1. Find out which folder you are in.
2. Go into your `Documents` folder using Tab to complete the name.
3. Come back out.
4. Clear the screen.
5. Show the commands you just typed.

<details>
<summary>Show answer</summary>

```powershell
pwd
cd Doc        # press Tab, it becomes cd .\Documents\
cd ..
clear         # or Ctrl + L
history
```

If any step did not work, read the error message: it usually says exactly what is wrong (a typo, a folder that does not exist).

</details>

## Recap

- The terminal runs **text commands**. The prompt shows **which folder you are in**.
- `pwd` shows where you are, `ls` shows what is here, `cd folder` goes into a folder, `cd ..` goes up one level.
- **Tab** completes names. **Up arrow** repeats commands. **Ctrl + L** clears the screen.
- `python file.py` runs a file. You must be in the **same folder** as the file.
- If the terminal says `python` is "not recognized", the problem is the **PATH**, not Python itself.

**Next:** [python.md](python.md)
