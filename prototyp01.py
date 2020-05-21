import os
import time

from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.VideoClip import ImageClip
from os import walk

files = []
videos = []
images = []



def chose1():
   print("make sure all files are in the same folder as this script you are using! ")
   time.sleep(2)

   for (dirpath, dirnames, filenames) in walk(os.getcwd()):
       files.extend(filenames)
       break

   for i in files:
       if (i[-3:]) == "jpg":
           images.append(ImageClip(i).resize([640, 1136]).set_duration(3))
       if (i[-3:]) == "mp4":
           videos.append(VideoFileClip(i))

   final_clip = concatenate_videoclips(videos + images, method="compose")
   final_clip.write_videofile("Output.mp4")

   print("FINISHED! Enjoy Output.mp4")

def chose2():
    print("This takes some time..")
    time.sleep(2)
    for (dirpath, dirnames, filenames) in walk(os.getcwd()):
        files.extend(filenames)
        break

    for i in files:
        if (i[-3:]) == "jpg":
            images.append(ImageClip(i).resize([640, 1136]).set_duration(3))
        if (i[-3:]) == "mp4":
            videos.append(VideoFileClip(i))

    final_clip = concatenate_videoclips(videos + images, method="compose")
    final_clip.write_videofile("input.mp4")

    time.sleep(2)

    stream = os.popen(
        r'ffmpeg -i input.mp4 -lavfi "[0:v]scale=1920*2:1080*2,boxblur=luma_radius=min(h\,w)/20:luma_power=1:chroma_radius=min(cw\,ch)/20:chroma_power=1[bg];[0:v]scale=-1:1080[ov];[bg][ov]overlay=(W-w)/2:(H-h)/2,crop=w=1920:h=1080" Output.mp4')
    output = stream.read()

    os.rename(os.getcwd()+r"\input.mp4",os.getcwd()+r"\withBlackBorders.mp4")
    print("\nFinished! Enjoy Output.mp4")


def chose3():
    print("Make sure your videos name is 'input.mp4' !")
    time.sleep(2)

    stream = os.popen(
        r'ffmpeg -i input.mp4 -lavfi "[0:v]scale=1920*2:1080*2,boxblur=luma_radius=min(h\,w)/20:luma_power=1:chroma_radius=min(cw\,ch)/20:chroma_power=1[bg];[0:v]scale=-1:1080[ov];[bg][ov]overlay=(W-w)/2:(H-h)/2,crop=w=1920:h=1080" Output.mp4')
    output = stream.read()

    os.rename(os.getcwd()+r"\input.mp4",os.getcwd()+r"\withBlackBorders.mp4")
    print("\nFinished! Enjoy Output.mp4")

### INITIALIZE ###
while True:

    chose = str(input("Select number of function\n1 concatinate videos and|or images\n2 concatinate videos and|or images and convert to Horizontal"
                  "\n3 convert to Horizontal\n"))
    if chose == "1" or chose == "2" or chose == "3":
        break

if chose =="1":
    chose1()
if chose =="2":
    chose2()
if chose == "3":
    chose3()


