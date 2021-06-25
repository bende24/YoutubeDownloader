from pytube import YouTube
from moviepy.editor import *
import sys
import os
import re

DOWNLOAD_PATH = "D:\\Music"

def remove_non_alphabetic_characters(text):
	regex = re.compile('[^a-zA-Z1-9 ]')
	#First parameter is the replacement, second parameter is your input string
	foo = regex.sub('', text)
	return " ".join(foo.split())

def download_audio(yt, title):
	yt.streams.filter().first().download(DOWNLOAD_PATH, title)

print('Type url (type q to quit)')
for line in sys.stdin:
	if 'q' == line.strip() or '' == line.strip():
		break

	yt = YouTube(line.strip())
	title = remove_non_alphabetic_characters(yt.title)

	mp4_file = DOWNLOAD_PATH + "\\" + title + ".mp4"
	mp3_file = DOWNLOAD_PATH + "\\" + title + ".mp3"

	print(title + ' is being downloaded')
	download_audio(yt, title)
	
	videoclip = VideoFileClip(mp4_file)
	audioclip = videoclip.audio
	audioclip.write_audiofile(mp3_file)

	audioclip.close()
	videoclip.close()
	os.remove(mp4_file)

	print(yt.title + ' has been downloaded')
	print('Type url (type q to quit)')

print('Exit')