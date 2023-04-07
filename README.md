# YouTube Audio Downloader

This project will create a YouTube Audio Downloader using the pytube library and Python 3. The goal of this project is to create easy to use application that allows users to quickly and easily download audio from YouTube videos.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Authors](#authors)

## Getting Started

To get started create a virtual environment. Clone the project.

Install the basic dependency, FFMPEG.

To install it on Windows first, install the [Chocolatey Package Manger](https://chocolatey.org/how-chocolatey-works). Install instructions are [here](https://chocolatey.org/install).

After installing chocolatey, download the package from an administrative instance of Powershell.

Update the Batchfile to include path to your virtual environment python interpreter and run.py;

```diff
@echo off
-"C:\Users\Ashish Singh\Documents\GitHub\YouTube-audio-downloader\Scripts\python.exe" "C:\Users\Ashish Singh\Documents\GitHub\YouTube-audio-downloader\run.py"
+"path-to-venv-folder\Scripts\python.exe" "path-to-project-folder\run.py"
pause
```

In variables.py update line 27 to save files to your Downloads folder;

```diff
- 'outtmpl': "C:\Users\Ashish Singh\Downloads\%(title)s.%(ext)s",
+ 'outtmpl': "path-to-Downloads-folder\%(title)s.%(ext)s",              

```

Run the batch file to get downloading.

### Prerequisites

- youtube-dl - version 2021.12.17
- regex - version 2022.10.31
- plyer - 2.1.0

### Installation

The requirements for this project are listed above.
To install these libraries to your local environment run the following installation commands in you terminal;

- ```pip3 install regex```
- ```pip3 install youtube-dl```

## Usage

Once the project is set up, run the batch file and past the YouTube video URL. that's it, wait for the download to finish. Done.

## Project Status

Project is: _completed_

## Authors

Initial work - [Ashish Singh](https://www.github.com/45H15H)
