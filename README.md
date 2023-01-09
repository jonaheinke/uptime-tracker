# Uptime Tracker

[![license](https://img.shields.io/github/license/jonaheinke/uptime-tracker)](LICENSE)
[![open issues](https://img.shields.io/github/issues/jonaheinke/uptime-tracker)](https://github.com/jonaheinke/uptime-tracker/issues)
[![code size](https://img.shields.io/github/languages/code-size/jonaheinke/uptime-tracker)](#)
[![used libraries](https://img.shields.io/badge/used%20libraries-pyinstaller-013243)](#)

This program tracks the uptime of a server or PC and saves it to a local file.

Its path can be defined in the fourteenth line of the script. The date and time formats can be changed via lines fifteen and sixteen ([format codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)).

If you want to bundle this program into an executable, just run `build` in the root directory. It uses [PyInstaller](https://pyinstaller.org/en/stable/) to create a single executable file.

## Which libraries does it require?

None. Just Python's standard libraries.

If you want to bundle this program into an executable with the `build` command, it uses the [PyInstaller](https://pyinstaller.org/en/stable/) to achieve that.

## What's currently not supported?

- sub-minute tracking
- starting the program at midnight (two entries will appear in the output file)
- launching multiple instances of the program