#!/usr/bin/env python

import argparse
import cv2
from os import *
from os.path import *


def get_new_path(file_path):
    file_name = basename(file_path)
    file_name_tokens = file_name.split('.')
    # Ignore extension.
    file_name = join(*file_name_tokens[:-1])
    file_dir = dirname(file_path)
    return join(file_dir, file_name)


def sample_video(video_path, sample_rate=1):
    video = cv2.VideoCapture(video_path)
    success, image = video.read()
    count = 0
    success = True
    new_path = get_new_path(video_path)

    if not exists(new_path):
        mkdir(new_path)

    while success:
        if count % sample_rate == 0:
            frame_name = "frame%d.jpg" % count
            frame_path = join(new_path, frame_name)
            print(frame_path)
            cv2.imwrite(frame_path, image)

        success, image = video.read()
        count += 1


def main():
    argparser = argparse.ArgumentParser(description="Video sampling tool")
    argparser.add_argument('video', help="Path to video file.")
    argparser.add_argument('--rate', '-r', metavar='sample-rate', default='1',
            type=int, help="Sample rate")

    args = argparser.parse_args()
    video_path = args.video

    sample_video(video_path, args.rate)


if __name__ == '__main__':
    main()

