from pytube import YouTube
import itertools
import threading
import time
import sys
#definition for making load animation
done = False
def animation():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        else:
            sys.stdout.write('\rloading ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\rdone!     ')
#body
Link =input('Enter url link \n')
print("Please Wait.. it will take some time")
#starting download from here
ads = YouTube(Link)
print(ads.streams)
itag = input('which stream do you wanna download? "type itag number" \n')
ys = ads.streams.get_by_itag(itag)
Location = input('Please enter the exact location you want to save \n')
t = threading.Thread(target=animation)
print(ads.streams.filter(progressive=True))
t.start()
print('please wait file is now downloading ...')
ys.download(link)
print('video downloaded succesfuly')
print('you can text me on telegram for financial support @Amir_mous')
#long process here
time.sleep(10)
done = True