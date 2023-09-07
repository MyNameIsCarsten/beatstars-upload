from file_path import mp3_path
from regex import get_bpm_key
from beatstars import beatstars
from beat_video import create_video
from tag_generator import tag_generator

# Define 3 tags for beatstars
tags = ["Sexyy Red", "Sukihana", "Glorilla"]

# Define which beat number should be selected
number = 3341

# Define where to look for the beat
folder = "Female"
dir_path = f"D:\Dropbox\Beats\ProfessionalStuff\Beatstars\{folder}"

# Define path for Chromedriver
driver_path = 'D:\Programme\PyCharm_Projects\chromedriver.exe'

# Define path for Image
clip_path = r"D:\Dropbox\Youtube Uploads\next.png"

# Get beat meta data
bpm, key, name = get_bpm_key(mp3_path(number, folder, dir_path))

# Upload beat
beatstars(number, bpm, name, key, tags, folder, dir_path, driver_path)

# Define path to save video in
vid_path = fr"C:\Users\Carsten\Downloads\{tags[0]} - {name}.mp4"

# Define path for saving shorts in
shorts_path = fr"D:\Dropbox\Youtube Uploads\Shorts\{tags[0]} - {name} - Short.mp4"

# Create video
create_video(mp3_path(number, folder, dir_path), clip_path, vid_path, shorts_path)

# Update Tag Generator
tag_generator(name, tags[0],tags[1])
