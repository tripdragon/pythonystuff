import subprocess

import os
from array import *


# Processes a folder of video files via ffmpeg in a batch
# Saves a bit of copy and paste really
# tested in python3

# Requires ffmpeg be installed and in your path
# You can tweak the flag settings as you need


# example of typical string
# ffmpeg -i  "/Users/Narfs/videos_in/star.mp4" -filter:v scale=300:-1 -vcodec libx264 -crf 28 "/Users/Narfs/videos_out/star.mp4"

parent_dir = './source_vids_copy'
target_dir = './target_vids_compressed'

for dirpath, dirs, files in os.walk(parent_dir):  
  for filename in files: 
    videopath = os.path.join(dirpath,filename) 
    if videopath.endswith('.mp4'):
        # now using f-strings
        fullcommand = f'ffmpeg -i "{videopath}" -filter:v scale=300:-1 -vcodec libx264 -crf 28 "{target_dir}/{filename}"'
        # fullcommand = "ffmpeg -i " + '\"' + videopath + '\"' + " " + "-filter:v scale=300:-1 -vcodec libx264 -crf 28 " + '\"' + target_dir + filename + '\"'
        
        print(fullcommand)
        subprocess.call(fullcommand, shell=True)
