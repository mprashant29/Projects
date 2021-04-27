import sys
from pytube import YouTube #imports youtube video
link=input("ENTER YOUR LINK:  ")

yt = YouTube(link) #accepts the input from user
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length,"Seconds")  #information about video
print("Description: ",yt.description)
print("Ratings: ",yt.rating)
#print(yt.streams) #prints all available streams
#print(yt.streams.filter(only_audio=True))
#print(yt.streams.filter(only_video=True))
#print(yt.streams.filter(progressive=True))

ys=yt.streams.get_highest_resolution()
print('VIDEO DOWNLOADED SUCESSFULLY')
ys.download()
print("DONE!!")

