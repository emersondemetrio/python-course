# Module 04: Files

Until now, everything your programs knew disappeared the moment they finished. You typed a name, the program greeted you, and then... gone. In this module your programs learn to **remember**: they will save text into files and read it back later, even after you close the terminal or turn off the computer.

## What you will learn

- The difference between a file **name** (a string) and the **file itself**
- How to open a file with `open` and `with`
- The three main modes: read (`"r"`), write (`"w"`) and append (`"a"`)
- How to read a whole file, or one line at a time
- How to write text and why you need `"\n"`
- What to do when the file does not exist yet

## Files in this module (read them in order)

1. [files.md](files.md): opening, reading and writing files
2. [project-notebook.md](project-notebook.md): a guided mini project, a "quick notes" program that saves your notes in a file

Estimated time: 2 to 3 study sessions of about 1 hour.

## Before you start

You should be comfortable with:

- variables and f-strings (module 01)
- lists and `for` loops (module 02)
- writing and calling functions with parameters and `return` (module 03)

If any of these feels shaky, revisit it first. Files use all of them.

## You are ready for the next module when you can...

- [ ] Explain, in your own words, why `name = "notes.txt"` does not open anything
- [ ] Open a file with `with open(...) as f:` without looking it up
- [ ] Say which mode to use to **add** a line without deleting what is already there
- [ ] Read a file and print each line numbered, starting from 1
- [ ] Explain why lines get "glued together" when you forget `"\n"`
- [ ] Finish the notes program from [project-notebook.md](project-notebook.md) and explain what `main()` does

**Next module:** [Module 05: Git and GitHub](../module-05-git-and-github/README.md)
