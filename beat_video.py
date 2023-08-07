from moviepy.editor import *

def create_video(path:str, artist:str, name:str):
    # Import the audio(Insert to location of your audio instead of audioClip.mp3)
    audio = AudioFileClip(path)

    # Import the Image and set its duration same as the audio (Insert the location of your photo instead of photo.jpg)
    clip = ImageClip(r"D:\Dropbox\Youtube Uploads\next.png").set_duration(audio.duration)

    # Set the audio of the clip
    clip = clip.set_audio(audio)

    # Export the clip
    clip.write_videofile(fr"C:\Users\Carsten\Downloads\{artist} - {name}.mp4", fps=30)

    # Create Short

    short = VideoFileClip(fr"C:\Users\Carsten\Downloads\{artist} - {name}.mp4")

    short = short.subclip(0,60)

    short.write_videofile(fr"D:\Dropbox\Youtube Uploads\Shorts\{artist} - {name} - Short.mp4", fps=30)

    return