"""MFCC feature extraction for an audio file."""

import librosa
import numpy as np
import pandas as pd

def extract_mfcc(file_path):
    mfcc_new = []
    # C:\Users\Farhan\Desktop\Semester 4\Big Data Theory\testing_audios\0_01_0.wav
    #file_path = input("Path:")
    x, sample_rate = librosa.load(path=file_path, res_type='kaiser_fast')  # ,res_type='kaiser_fast'
    mfccs = np.mean(librosa.feature.mfcc(y=x, sr=sample_rate, n_mfcc=50, lifter=100).T, axis=0)
    mfcc_new.append(mfccs)
    mfcc_new = pd.DataFrame(mfcc_new)
    return mfcc_new
