from PIL import Image
import glob,os

import numpy as np

import tensorflow as tf
from 
from keras.models import Sequential
from keras.layers import Activation,Dropout,Flatten,Dense
from keras.utils  import np_utils

from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent

class illProcess:
    resize_settings = (128,128)
    img_dir = os.path.join(BASE_DIR,"img")
    rawdata_dir = os.path.join(img_dir,"rawdata")
    savedata_dir = os.path.join(img_dir,"savedata")

    X_train = []
    y_train = []

    def __init__(self, raw_folder="", save_folder="") -> None:
        if raw_folder != "" or save_folder != "":
            self.rawdata_dir = os.path.join(self.img_dir,raw_folder)
            self.savedata_dir = os.path.join(self.img_dir,save_folder)

    def showpath(self):
        print(self.rawdata_dir,self.savedata_dir)

    def savemosaic(self):
        pathes = glob.glob(self.rawdata_dir+"/*.png")
        #files = main.openfolder(selfrawdata_dir)
        files = [os.path.basename(f) for f in pathes]
        
        for file in files:
            img = Image.open(os.path.join(self.rawdata_dir,file))
            img = img.resize(self.resize_settings)
            img.save(os.path.join(self.savedata_dir,file))
        print("mozaic end")

    def convertnp(self):
        files = glob.glob(self.savedata_dir + "/*.png")
        for i,file in enumerate(files):
            image = Image.open(file)
            image = image.convert("RGB")
            image = image.resize(self.resize_settings)
            data  = np.asarray(image)

            X_train = []
            X_train.append(data)
            self.X_train = np.array(X_train)

            return self.X_train





if __name__ == "__main__":
    ip = illProcess("rawdata","savedata")
    ip.showpath()
    ip.savemosaic()

    #X_train = ip.convertnp()

    #print(type(X_train))

