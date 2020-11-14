# import the necessary packages
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import glob
import cv2
import os
import datasets_ellipse
import models_ellipse

def load_attributes(inputPath):
	# initialize the list of column names in the CSV file and then
	# load it using Pandas
	cols = ["angle"]
	df = pd.read_csv(inputPath, header=None, names=cols)

	# return the data frame
	return df


def load_images(df, inputPath):
	# initialize our images array (i.e., the house images themselves)
    images = []
    
    for i in df.index.values:
        basePath = os.path.sep.join([inputPath,"{}.png".format(i)])
        image = cv2.imread(basePath)
        image = cv2.resize(image, (64, 64))
        images.append(image)
    
    return np.array(images)  


#%%

# =============================================================================
# ## code for displaying an image
# pt="/home/dev/Desktop/9th Semester/ML/Project/Ellipse/11.png"
# 
# im = cv2.imread(pt)
# cv2.imshow('img',im)
# cv2.waitKey(0)   # press any key to close the image
# cv2.destroyAllWindows()
# =============================================================================

# def load_images(df, inputPath):
# 	# initialize our images array (i.e., the house images themselves)
#     images = []
    
#     for i in df.index.values:
#         basePath = os.path.sep.join([inputPath,"{}.png".format(i+1)])
#         image = cv2.imread(basePath)
#         images.append(image)
    
#     return np.array(images) 

#%%
# pt="/home/dev/Desktop/9th Semester/ML/Project/Ellipse/11.png"
# im = cv2.imread(pt)

# ot="/home/dev/Desktop/9th Semester/ML/Project/keras-regression-cnns/Houses-dataset-master/Houses Dataset/1_bathroom.jpg"
# om =cv2.imread(ot)

#%%
# loc="/home/dev/Desktop/9th Semester/ML/Project/Ellipse"
# # construct the path to the input .txt file that contains information
# # and then load the dataset
# print("[INFO] loading attributes...")
# inputPath = os.path.sep.join([loc, "labels.txt"]) ##change
# df = datasets_ellipse.load_attributes(inputPath)

# aa = load_images(df,loc)