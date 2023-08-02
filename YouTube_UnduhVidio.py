import pyfiglet
from pytube import YouTube

Banner = pyfiglet.figlet_format("code by n00bX8", font= "univers")
print(Banner)

url_yt = str(input('masukan url youtube: '))
my_video = YouTube(url_yt)
print(my_video.title)

my_video = my_video.streams.get_highest_resolution()
print("tunggu...")
my_video.download()
print("sukses !!!")
