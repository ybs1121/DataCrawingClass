from PIL import Image
import os, glob, numpy as np

from keras_preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split

caltech_dir = r"경로"



categories = ["데이지", "동백", "라일락", "붓꽃", "수국","수선화","핑크뮬리","프리지아"]
nb_classes = len(categories)

image_w = 64
image_h = 64

pixels = image_h * image_w * 3

X = []
y = []



for idx, cat in enumerate(categories):

    # one-hot 돌리기.
    label = [0 for i in range(nb_classes)]
    label[idx] = 1

    image_dir = caltech_dir + "/" + cat
    files = glob.glob(image_dir + "/*.jpg")
    print(cat, " 파일 길이 : ", len(files))
    for i, f in enumerate(files):
        img = Image.open(f)
        img = img.convert("RGB")
        img = img.resize((image_w, image_h))
        data = np.asarray(img)

        X.append(data)
        y.append(label)

        if i % 700 == 0:
            print(cat, " : ", f)

X = np.array(X)
y = np.array(y)





X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)



xy = (X_train, X_test, y_train, y_test)

np.save(r"경로\flower.npy", xy)