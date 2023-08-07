import os

def mp3_path(number:int, folder:str):
    # Set new path
    dir_path = f"D:\Dropbox\Beats\ProfessionalStuff\Beatstars\{folder}"
    print(f"Looking for beat here: {dir_path}")

    # For loop to iterate through current path
    # filenames are split into: root, dirs (directory) and files
    number = "[" + str(number) + "]"
    for root, dirs, files in os.walk(dir_path):
        for file in files:

            # change the extension from '.mp3' to the one of your choice.
            # simple string method that will return true
            '''
            if file.endswith('.mp3'):
                print(root + '/' + str(file))'''

            # simple string method that will return true
            if number in file:
                path = (root + '/' + str(file))

    return path

def wav_path(number:int):
    # Set new path
    dir_path = "D:\Dropbox\Beats\ProfessionalStuff\Beatstars\\1! Wav Files"

    # For loop to iterate through current path
    # filenames are split into: root, dirs (directory) and files
    number = "[" + str(number) + "]"
    for root, dirs, files in os.walk(dir_path):
        for file in files:

            # change the extension from '.mp3' to the one of your choice.
            # simple string method that will return true
            '''
            if file.endswith('.wav'):
                print(root + '/' + str(file))'''

            # simple string method that will return true
            if number in file:
                path = (root + '/' + str(file))

    return path


