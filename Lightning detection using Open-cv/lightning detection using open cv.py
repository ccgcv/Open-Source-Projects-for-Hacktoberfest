import sys
import cv2
import cv2.cv as cv
import numpy as np
from PIL import Image
import progress
import time

SCALE = 0.5
NOISE_CUTOFF = 5
BLUR_SIZE = 3

start = time.time()

def count_diff(img1, img2):
    small1 = cv2.resize(img1, (0,0), fx=SCALE, fy=SCALE)
    small2 = cv2.resize(img2, (0,0), fx=SCALE, fy=SCALE)
    #cv2.imshow('frame', small2)
    #cv2.waitKey(1)
    diff = cv2.absdiff(small1, small2)
    diff = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    frame_delta1 = cv2.threshold(diff, NOISE_CUTOFF, 255, 3)[1]
    frame_delta1_color = cv2.cvtColor(frame_delta1, cv2.COLOR_GRAY2RGB)
    delta_count1 = cv2.countNonZero(frame_delta1)

    return delta_count1

filename = sys.argv[1]
video = cv2.VideoCapture(filename)

nframes = (int)(video.get(cv.CV_CAP_PROP_FRAME_COUNT))
width = (int)(video.get(cv.CV_CAP_PROP_FRAME_WIDTH))
height = (int)(video.get(cv.CV_CAP_PROP_FRAME_HEIGHT))
fps= (int)(video.get(cv.CV_CAP_PROP_FPS))

frame_count = 0

print "[i] Frame size: ", width, height
print "[i] Total frames:", nframes
print "[i] Fps:", fps

fff = open(filename+".csv", 'w')

flag, frame0 = video.read()
treshold = int(sys.argv[2])
strikes = 0

p0 = progress.AnimatedProgressBar(end=nframes, width=80)
for f in xrange(nframes-1):
    p0 + 1
    p0.show_progress()

    flag, frame1 = video.read()
    diff1  = count_diff(frame0, frame1)
    name = filename+"_%06d.jpg" % f

    if diff1 > treshold:
        cv2.imwrite(name, frame1)
        strikes = strikes + 1

        #small = cv2.resize(frame1, (0,0), fx=SCALE, fy=SCALE)
        #cv2.imshow('frame', small)
        #cv2.waitKey(1)

    text = str(f)+', '+str(diff1)
    #print text
    fff.write(text  + '\n')
    fff.flush()
    frame0 = frame1

fff.close()
print
print '[i] Strikes: ', strikes
print '[i] elapsed time:', time.time() - start