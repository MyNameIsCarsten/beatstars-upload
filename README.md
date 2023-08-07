# beatstars-upload
Python script for handling the beat upload to beatstars.com

# How it works
## Beat naming
My beats are all named in a specific way:
[0001] C-Minor 100BPM Beat-Name (Prod. by MyName)

The script will use this naming convention to grab the BPM, key and beat title.
The specific beat is identified by its number, here "0001".

## After execution
After you have run the script, you will need to manually choose an upload date and publish your upload.

# Set-Up
## Create .env-File for login credentials
In order for the script to work, you will need to create a file called ".env".
Open it with a normal text editor and copy this code:
```
DEVICE_USERNAME="username"
DEVICE_PASSWORD="password"
```
Now, insert you beatstars username and password.

## Beat path
In "main.py" define where the script should look for the beat:
```
# Define where to look for the beat
folder = "Female"
dir_path = f"D:\Dropbox\Beats\ProfessionalStuff\Beatstars\{folder}"
```

## Chromedriver location
In "main.py" define where the script should look for Chromedriver:
```
# Define path for Chromedriver
driver_path = 'D:\Programme\PyCharm_Projects\chromedriver.exe'
```

If Chromedriver is outdated or you don't have it yet, get it here:
https://chromedriver.chromium.org/downloads

## Video locations
First, define the location of the image for your video.
```
# Define path for Image
clip_path = r"D:\Dropbox\Youtube Uploads\next.png"
```

Second, define the location for saving the video
```
# Define path to save video in
vid_path = fr"C:\Users\Carsten\Downloads\{tags[0]} - {name}.mp4"
```
```
# Define path for saving shorts in
shorts_path = fr"D:\Dropbox\Youtube Uploads\Shorts\{tags[0]} - {name} - Short.mp4"
```
## Tag generator
I have created an excel file (not part of this project) that I use for creating the YouTube text and tags.
The "tag_generator.py" module inserts the beat title and 2 of the 3 artist names into this excel.
You can comment out this function in "main.py".
