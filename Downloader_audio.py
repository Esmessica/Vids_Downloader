from pytube import YouTube
import os
on = True
while on:
    link = input("Enter link:\t")
    yt = YouTube(link)

    print("Title\t", yt.title)
    print("View\t", yt.views)
    yd = yt.streams.filter(only_audio=True).first()
    out_file = yd.download("./audios")

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print('Got it :)')
    ask = input("Do you want another audio? y/n\t")
    if ask == "n":
        on = False
    elif ask == "y":
        on = True
    else:
        raise Exception("Wrong commmand")
        on = True