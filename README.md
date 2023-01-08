# Uptime Tracker

[![license](https://img.shields.io/github/license/jonaheinke/uptime-tracker)](LICENSE)
[![open issues](https://img.shields.io/github/issues/jonaheinke/uptime-tracker)](https://github.com/jonaheinke/uptime-tracker/issues)
[![code size](https://img.shields.io/github/languages/code-size/jonaheinke/uptime-tracker)](#)
[![used libraries](https://img.shields.io/badge/used%20libraries-pyinstaller-013243)](#)

This program tracks the uptime of a server or PC and saves it to a local file. Its path can be defined in the fourteenth line of the script.

If you want to bundle this program into an executable, just run `build` in the root directory. It uses [PyInstaller](https://pyinstaller.org/en/stable/) to create a single executable file.

## What's currently not supported?

It does not support sub minute tracking.

It does not support multi-day uptime tracking. It just shows the start date, start time and end time.