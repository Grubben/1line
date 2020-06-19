# 1line
### __The line-by-line Program__

1line is a shell program written in Python **completely FOSS**. It's main objective is to make simple note-taking faster and more convenient without forcing you to start up an application.

Currently, only works on Unix platforms

## Usage:
```
$ 1line

$ 1line list

$ 1line add social-studies
> exit

$ 1line biology
> the mitochondria is the powerhouse of the cell
> exit

$ 1line remove social-studies

$ 1line open

$ 1line open biology
```


## Installation:
First make sure you have python3. Then:

```
pip3 install pyinstaller
```
Go to the directory that contains "1line.py"
```
pyinstaller --onefile 1line.py
```
Your unix-executable file is in the "dist" folder

# For Unix-not MacOS:
(I believe this is the correct method but beware, for I'm not tech savy)
Move (or drag with the mouse) the file to '/bin' directory:
```
cd dist
mv 1line /bin
```

# For Windows:
In Progress

# For MacOS:
```
cd dist
mv 1line /usr/local/bin
```


Have fun with it, and contribute if you wish!

*1line is all you need*
