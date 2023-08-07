from moviepy.editor import *

def create_video(path:str, clip_path:str, vid_path:str, shorts_path:str):
    # Import the audio(Insert to location of your audio instead of audioClip.mp3)
    audio = AudioFileClip(path)

    # Import the Image and set its duration same as the audio (Insert the location of your photo instead of photo.jpg)
    clip = ImageClip(clip_path).set_duration(audio.duration)


    # Set the audio of the clip
    clip = clip.set_audio(audio)

    # Export the clip
    clip.write_videofile(vid_path, fps=30)

    # Create Short
    short = VideoFileClip(vid_path)

    short = short.subclip(0,60)

    short.write_videofile(shorts_path, fps=30)

    return