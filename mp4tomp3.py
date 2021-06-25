from moviepy.editor import *

file_name = "Using Science to Optimize Sleep Learning & Metabolism  Huberman Lab Podcast 3"
mp4_file = "D:\\Music\\"+file_name+".mp4"
mp3_file = "D:\\Music\\"+file_name+".mp3"

videoclip = VideoFileClip(mp4_file)
audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file)

audioclip.close()
videoclip.close()
