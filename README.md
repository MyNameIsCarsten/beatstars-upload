# beatstars-upload
Python script for handling the beat upload to beatstars.com

# How it works
## Beat naming
My beats are all named in a specific way:
[0001] C-Minor 100BPM Beat-Name (Prod. by MyName)

The script will use this naming convention to grab the BPM, key and beat title.
The specific beat is identified by its number, here "0001".

You can define the folder where the script looks for via the "file_path.py" module.

## After execution
After you have run the script, you will need to manually choose a upload date and submit your upload.

# Set-Up
## Create .env-File for login credentials
In order for the script to work, you will need to create a file called ".env".
Open it with a normal text editor and copy this code:
```
DEVICE_USERNAME="username"
DEVICE_PASSWORD="password"
```
Now, insert you beatstars username and password.

## Chromedriver location
In "beatstars.py" in the function "beatstars()" you will need to define the location of your Chromedriver.
Mine is 'D:\Programme\PyCharm_Projects\chromedriver.exe'.

If Chromedriver is outdated or you don't have it yet, get it here:
https://chromedriver.chromium.org/downloads

## Video location
In "beat_video.py" you can define where the script should look for the image for your clip and where the short and full video should be stored.

## Tag generator
I have created an excel file (not part of this project) that I use for creating the YouTube text and tags.
The "tag_generator.py" module inserts the beat title and 2 of the 3 artist names into this excel.
You can comment out this function in "main.py".
