# Cheker

## How to use

Enter the command in the console
```sh
C:\Users\user\load_cheker> python main.py --help 
```
And you will be able to see the structure of the command

```sh
usage: main.py [-h] [--log [LOG]] path [path ...] process [process ...] interval [interval ...]

positional arguments:
  path         Path to process file
  process      Name of process
  interval     Query interval in seconds

optional arguments:
  -h, --help   show this help message and exit
  --log [LOG]  path to log
```

Using a script on the example of notepad

```sh
C:\Users\user\load_cheker> python main.py C:\Windows\system32 notepad.exe 1
```
