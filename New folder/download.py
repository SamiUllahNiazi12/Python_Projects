# from pytube import YouTube

# link = "https://www.youtube.com/watch?v=0t8Em88cTlI&list=LL&index=128"
# youtube_1 = YouTube(link)
 
# # print(youtube_1)
# # print(youtube_1.thumbnail_url)

# # videos = youtube_1.streams.filter(only_audio=True)
# # videos = youtube_1.streams.all()

# vid = list(enumerate(videos))
# for i in vid:
#     print(i)
# print()
# strm  = int(input("enter : "))
# videos[strm].download()
# print(" Succesfully ")


# ***Playlist***

from pytube import Playlist

py = Playlist("https://www.youtube.com/playlist?list=PLjVLYmrlmjGcsNaFScgdpEWE9Rv3qDiY4")

print(f'Downloading : {py.title}')

for video in py.videos:
    video.streams.first().download()