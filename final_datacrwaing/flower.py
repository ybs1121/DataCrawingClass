
import os, glob, numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import matplotlib.pyplot as plt
from tensorflow.python.keras.callbacks import ReduceLROnPlateau
from keras_preprocessing.image import ImageDataGenerator
# train_datagen = ImageDataGenerator(
#     width_shift_range=0.1,
#     height_shift_range=0.1,
#     zoom_range=0.2,
#     rotation_range = 30,
#     shear_range=0.2,
#     fill_mode = 'nearest'
# )

train_datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')




X_train, X_test, y_train, y_test = np.load(r"경로\flower.npy",allow_pickle=True)
print(X_train.shape)
print(X_train.shape[0])


categories = ["데이지", "동백", "라일락", "붓꽃", "수국","수선화","핑크뮬리","프리지아"]
nb_classes = len(categories)

#일반화
X_train = X_train.astype(float) / 255
X_test = X_test.astype(float) / 255

model = Sequential()
model.add(Conv2D(32, (3, 3), padding="same", input_shape=X_train.shape[1:], activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), padding="same", activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, (3, 3), padding="same", activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))


model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model_dir = './model'

print("학습")
print(len(X_train))

if not os.path.exists(model_dir):
    os.mkdir(model_dir)

earlystop = EarlyStopping(patience=10)

learning_rate_reduction = ReduceLROnPlateau(monitor='val_loss',
                                            patience=5,
                                            verbose=1,
                                            factor=0.5,
                                            min_lr=0.00001)

callbacks = [earlystop,learning_rate_reduction]

# model_path = model_dir + '/multi_img_classification.model'
#checkpoint = ModelCheckpoint(filepath=model_path, monitor='val_loss', verbose=1, save_best_only=True)

#early_stopping = EarlyStopping(monitor='val_loss', patience=10)

history = model.fit(
     train_datagen.flow(X_train, y_train, batch_size=15) , epochs=100, validation_data=(X_test,y_test),callbacks=callbacks)

model.save_weights(r"경로\flower_weights.h5")
model.save(r"C:경로\flower.h5")
model.save("./flower.h5")


y_vloss = history.history['val_loss']
y_loss = history.history['loss']
val_accuracy = history.history['val_accuracy']
accuracy = history.history['accuracy']

x_len = np.arange(len(y_loss))

plt.plot(x_len, y_vloss, marker='.', c='red', label='val_set_loss')
plt.plot(x_len, y_loss, marker='.', c='blue', label='train_set_loss')


plt.legend()
plt.xlabel('epochs')
plt.ylabel('loss')
plt.grid()
plt.show()

plt.plot(x_len, val_accuracy, marker='.', c='red', label='val_accuracy')
plt.plot(x_len, accuracy, marker='.', c='blue', label='accuracy')


plt.legend()
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.grid()
plt.show()


