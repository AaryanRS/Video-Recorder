from moviepy.editor import *
import os

video = VideoFileClip("input.avi")

audio = AudioFileClip("audio.wav")

ComibneVideo = video.set_audio(audio)

ComibneVideo.write_videofile("Video.mp4")

os.remove("input.avi")
os.remove("audio.wav")