import numpy as np
from PIL import ImageGrab
import cv2


def process_image(original_image):
    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.Canny(
        processed_image, threshold1=200, threshold2=300
    )  # tweakable
    return processed_image


# Use PIL ImageGrab module to grab the printscreen frames
while True:
    screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
    new_screen = process_image(screen)

    cv2.imshow("window", new_screen)
    # cv2.imshow("window", cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))

    # close screen grab with 'q'
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
