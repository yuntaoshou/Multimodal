import os
import tqdm
import glob
import numpy as np
import pandas as pd


def split_audio_from_video_16k(video_root, save_root):
    if not os.path.exists(save_root): os.makedirs(save_root)
    for video_path in tqdm.tqdm(glob.glob(video_root+'/*')):
        videoname = os.path.basename(video_path)[:-4]
        audio_path = os.path.join(save_root, videoname + '.wav')

        cmd = "%s -loglevel quiet -y -i %s -ar 16000 -ac 1 %s" %("/home/lkshpc/syt/multimodal/tools/ffmpeg-7.0.1-i686-static/ffmpeg", video_path, audio_path)
        os.system(cmd)

if __name__ == '__main__':
    split_audio_from_video_16k("./train_splits_video", "./train_splits_audio")
