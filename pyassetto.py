import numpy as np
from PIL import ImageGrab
import cv2

# Use PIL ImageGrab module to grab the printscreen frames
while True:
    screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
    # printscreen_numpy = np.array(printscreen_pil.getdata(), dtype="uint8")

    cv2.imshow("window", cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))

    # close screen grab with 'q'
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
