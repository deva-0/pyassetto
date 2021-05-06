import numpy as np
import cv2
import time
from grabscreen import grab_screen
from getkeys import key_check
from alexnet import alexnet
import os

WIDTH = 80
HEIGHT = 60
LR = 1e-3
EPOCHS = 8
MODEL_NAME = "pyassetto-highlands-{}-{}-{}-epochs.model".format(LR, "alexnetv2", EPOCHS)


def main():
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    # last_time = time.time()

    while True:
        screen = grab_screen(region=(0, 40, 800, 640))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen, (80, 60))

        # print("Frame took {} seconds".format(time.time() - last_time))
        # last_time = time.time()

        if len(training_data) % 500 == 0:
            print(len(training_data))
            np.save(file_name, training_data)


main()
