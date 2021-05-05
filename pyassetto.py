import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, ReleaseKey, UpArrow, LeftArrow, RightArrow, DownArrow
import pyautogui

# define region of interest
def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked


def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(
        processed_img, threshold1=200, threshold2=300
    )  # tweakable

    vertices = np.array(
        [[10, 500], [10, 300], [300, 200], [500, 200], [800, 300], [800, 500]]
    )
    processed_img = roi(processed_img, [vertices])
    return processed_img


for i in list(range(4))[::-1]:
    print(i + 1)
    time.sleep(1)


def main():
    # Use PIL ImageGrab module to grab the printscreen frames
    while True:
        screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
        new_screen = process_img(screen)

        cv2.imshow("window", new_screen)
        # cv2.imshow("window", cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))

        # close screen grab with 'q'
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break


main()
