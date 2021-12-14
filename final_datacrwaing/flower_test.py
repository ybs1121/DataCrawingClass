import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from tensorflow.keras.models import load_model


im_rows = 64  # 이미지의 높이
im_cols = 64  # 이미지의 너비
im_color = 3  # 이미지의 색공간
in_shape = (im_rows, im_cols, im_color)
nb_classes = 8

LABELS = ["데이지", "동백", "라일락", "붓꽃", "수국", "수선화", "핑크뮬리", "프리지아"]
FLOWERS = ["순진, 인내, 평화, 희망", "누구보다 당신을 사랑합니다","아름다운 맹세", 
           "좋은 소식", "냉정, 진실된 꿈", "자기 사랑, 자존심, 고결, 신비", "고백",
           "천진난만, 당신의 앞날"]




model = load_model("flower.h5")


def check_photo(path):
    # 이미지 읽어 들이기
    img = Image.open(path)
    img = img.convert("RGB")  # 색공간 변환하기
    img = img.resize((im_cols, im_rows))  # 크기 변경하기
    plt.imshow(img)
    plt.show()
    # 데이터 변환하기
    x = np.asarray(img)
    x = x.reshape(-1, im_rows, im_cols, im_color)
    x = x / 255

    # 예측하기
    pre = model.predict([x])[0]
    idx = pre.argmax()
    per = int(pre[idx] * 100)
    return (idx, per)


def check_photo_str(path):
    idx, per = check_photo(path)
    # 응답하기
    print("이 사진은", LABELS[idx], "로(으로), 꽃말은", FLOWERS[idx], "입니다.")
    print("정답률은", per, "%입니다.")


if __name__ == '__main__':
    check_photo_str('flower1.jpg')

