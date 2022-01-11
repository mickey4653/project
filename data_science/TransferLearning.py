# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:36:38 2020

@author: kevin
"""

from IPython.display import Image
Image(filename='./MLCourse/fighterjet.jpg')    

from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input,decode_predictions
import numpy as np

img_path='./MLCourse./fighterjet.jpg'
# the moduel requires to be 224*224
img=image.load_img(img_path,target_size=(224,224))
x=image.img_to_array(img)
x=np.expand_dims(x,axis=0)
x=preprocess_input(x)

#%%
model=ResNet50(weights='imagenet')
preds=model.predict(x)
print('Predicted:',decode_predictions(preds,top=3)[0])


def classify(img_path):
    img=image.load_img(img_path,target_size=(224,224))
    x=image.img_to_array(img)
    x=np.expand_dims(x,axis=0)
    x=preprocess_input(x)
    preds=model.predict(x)
    print('Predicted:',decode_predictions(preds,top=3)[0])
classify('./MLCourse/bunny.jpg')
classify("./MLCourse/firetruck.jpg")
classify('./MLCourse/breakfast.jpg')
