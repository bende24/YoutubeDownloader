# Youtube-Mp3-Downloader
 
A simple command line based youtube mp3 downloader I've made for personal use.

## Requirements
The downloader uses pytube and moviepy python packages so you need to install them.

```
pip install pytube
pip install moviepy
```

Pytube: https://pypi.org/project/pytube/#Quickstart

Moviepy: https://pypi.org/project/moviepy/

## Download path
By default the audio will be downloaded to D:\\Music, if you want to change it you can do so by changing the 
```python
DOWNLOAD_PATH = "D:\\Music"
```
on the 7. line

## 404 Not Found error
This error happens when the pytube package is not up to date.
To fix this you have to upgrade the package.

```
pip install pytube --upgrade
```
