from file_path import mp3_path
from regex import get_bpm_key
from beatstars import beatstars
from beat_video import create_video
from tag_generator import tag_generator

# Define 3 tags for beatstars
tags = ["Sexyy Red", "Sukihana", "Glorilla"]

# Define which beat number should be selected
number = 3331

# Define where to look for the beat
folder = "Female"

# Get beat meta data
bpm, key, name = get_bpm_key(mp3_path(number, folder))

# Name fix
try:
    key = key.split("/")[1].strip()
except:
    pass

# Upload beat
beatstars(number, bpm, name, key, tags, folder)

# Create video
create_video(mp3_path(number, folder), tags[0], name)

# Update Tag Generator
tag_generator(name, tags[0],tags[1])

'''
Note:
If Chromedriver outdated:
https://chromedriver.chromium.org/downloads
Save under: D:\Programme\PyCharm_Projects
'''
