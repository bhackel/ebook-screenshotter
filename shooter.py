import pyscreenshot as ImageGrab
from PIL import Image
import os, time, sys
import keyboard


class Shooter:

    def __init__(self):
        self.screenshot_path = "./screenshots/"
        self.num_pages = 4
        self.X1 = 1852
        self.Y1 = 269
        self.X2 = 2558
        self.Y2 = 1320

        # 1616, 269, 2793, 1791
        # 1444, 269, 2966, 1446

        # Comment below and use single mode to include the boundaries in the image
        # to make sure the pixel locations are correct. Check in Photoshop/image editor
        self.X1 += 1
        self.Y1 += 1
        self.X2 -= 1
        self.Y2 -= 1

    def start_grab(self):
        time.sleep(5)
        old_im = None
        for i in range(self.num_pages):
            im = ImageGrab.grab(bbox=(self.X1,self.Y1,self.X2,self.Y2))
            if old_im == im:
                sys.exit()
            filename = "{}image{:03d}.png".format(self.screenshot_path, i+136)
            im.save(filename)
            print(f"captured {i} image, advancing...")

            # Change this keybind to the shortcut for "next page" in the book
            keyboard.send('right')

            # Increase sleep delay if the book takes a bit to load
            time.sleep(2)
           
            old_im = im
        print("Finished, run shots_to_pdf.py to convert to a pdf")

    def single(self):
        time.sleep(3)
        im = ImageGrab.grab(bbox=(self.X1,self.Y1,self.X2,self.Y2))
        im.save(self.screenshot_path + "imagetest.png")

if __name__ == '__main__':
    time.sleep(2)
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
    s = Shooter()
    
    # Switch between the two modes below for testing and full capture
    #s.single()
    s.start_grab()
