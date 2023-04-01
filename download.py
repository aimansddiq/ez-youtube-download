import os
import sys
import yt_dlp

# Set the video URL and the directory where the video will be saved
save_dir = "/video/"
video_url = None

if len(sys.argv) > 1:
    video_url = sys.argv[1]

if video_url is None:
    video_url = input("Enter the video URL: ")

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Set options for downloading the video
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', # choose best video format available
    'outtmpl': save_dir + '%(title)s.%(ext)s', # specify the output filename and location
}

# Download the video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
