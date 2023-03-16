from pytube import YouTube
from sys import argv

# after typing in terminal python ytDownloader.py arg value 1 will use pasted link comign afterwards
# exmp - python ytDownloader.py https://www.youtube.com/watch?v=2p9RoNIP_1M

link = argv[1]

# assigning YT link value to yt
yt = YouTube(link)

#some extra info printing out title name
print("Title: ", yt.title)

#additional information of view count for current link
print("View: ", yt.views)

#selecting the highest possible quality for video to be downloaded
yd = yt.streams.get_highest_resolution()

#downloading in specifiec folder with path provided (in this example folder created within script location was used)
yd.download('./DownloadedVid')