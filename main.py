from moviepy.editor import VideoFileClip

video = VideoFileClip("D:\\Py-Projects\\Vdo to Audio Extractor\\Status.mp4")

audio = video.audio
audio.write_audiofile("Extractedsong.mp3")
