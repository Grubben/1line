# 1line
### __The line-by-line Program__

1line is a shell program written in Python **completely FOSS**. It's main objective is to make simple note-taking faster and more convenient without forcing you to start up an application.

Definitely works on Unix platforms; try your might on Windows

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


# Installation:
First make sure you have python3. Then:

```
pip3 install pyinstaller
```
Go to the directory that contains "1line.py"
```
pyinstaller --onefile 1line.py
```
Your file is in the "dist" folder (wether it's a unix-executable or an exe)

## For Unix-not MacOS:
(I believe this is the correct method but beware, for I'm not tech savy)
Move (or drag with the mouse) the file to '/bin' directory:
```
cd dist
mv 1line /bin
```

## For Windows:
Put the exe somewhere and make a PATH to it on the command prompt

(I'm not sure how so Good Luck!)

## For MacOS:
```
cd dist
mv 1line /usr/local/bin
```


Have fun with it, and contribute if you wish!

*1line is all you need*
