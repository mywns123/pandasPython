# 딜러닝을 구동하기 위한 케라스 함수 호출
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
# 필요 라이브러리
import numpy as np
import tensorflow as tf

# 난수 생성 패턴 고정 - 실행할 때마다 같은결과를 출력하기위해 설정하는 부분
np.random.seed(3)
tf.random.set_seed(3)

Data_set = np.loadtxt('./data/ThoraricSurgery.csv', delimiter=',')
print(Data_set)

X = Data_set[:, 0:17]
Y = Data_set[:, 17]
# 딥 러닝 구조를 결정합니다.
# Sequential()는 딥러닝 구조를 한층한층 쌓아올리게 함.
model = Sequential()
# Dense()는 각 층이 각가 어떤 특성을 가질지 옵션을 설정
model.add(Dense(30, input_dim=17, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# loss 신경망이 실행될대마다 오차값을 추적하는 함수
# optimizer 오차를 어떻게 줄여 나갈지 정하는 함수
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(X, Y, epochs=100, batch_size=10)






