from pytube import YouTube
from sys import argv

link = input("Enter link:\t")
yt = YouTube(link)

print("Title\t", yt.title)
print("View\t", yt.views)
yd = yt.streams.get_highest_resolution()
yd.download("./videosDownloaded")