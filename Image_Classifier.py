import tensorflow as tf
from tensorflow.keras import datasets,layers,models
import matplotlib.pyplot as plt 

(train_images,train_labels),(test_images,test_labels)=datasets.fashion_mnist.load_data()

train_images=train_images/255.0
test_images=test_images/255.0

train_images=train_images.reshape(-1,28,28,1)
test_images=test_images.reshape(-1,28,28,1)

class_names=['T-shirt/top','Trouser','Pullover','Dress','Coat',
             'Sandal','Shirt','Sneaker','Bag','Ankle boot']

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5, validation_data=(test_images, test_labels))

test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"\n  Test Accuracy: {test_acc:.2f}")

import numpy as np
prediction = model.predict(test_images)
print(f"Predicted label for first image: {class_names[np.argmax(prediction[0])]}")


