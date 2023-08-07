# beatstars-upload
Python script for handling the beat upload to beatstars.com

# How it works
## Beat naming
My beats are all named in a specific way:
[0001] C-Minor 100BPM Beat-Name (Prod. by MyName)

The script will use this naming convention to grab the BPM, key and beat title.
The specific beat is identified by its number, here "0001".

You can define the folder where the script looks for via the "file_path.py" module.

# Set-Up
## Create .env-File for login credentials
In order for the script to work, you will need to create a file called ".env".
Open it with a normal text editor and copy thie code:
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