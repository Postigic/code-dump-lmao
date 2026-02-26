# media to ascii

Converts videos and images into ASCII art.

![image](./__project_image__/image.png)

> Bad Apple rendered in ASCII, a classic rite of passage

## Overview

Converts `.mp4`, `.mov`, `.jpg`, `.png`, or `.gif` files to coloured ASCII art. Original audio from source videos is merged with the output.

`.gif` support is patchwork. It suffices for converting but I cannot comment on the maintainability.

~~Processing time is agreeably awful, no guarantee I will optimise it though.~~

**25/2/2026:** Processing time improved by ~3x/4x

- 15m -> 5m
- 4m -> 1m
- ~400/700 frames take ~20/30s.

## Features

- Converts video frames and images into coloured ASCII
- Merges audio from source videos
- Outputs videos as `.mp4` and images matching original format (`.jpg` or `.png`)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Windows:

```bash
start.bat
```

Cross-platform:

```bash
python -u main.py
```
