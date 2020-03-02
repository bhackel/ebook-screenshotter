import pyscreenshot as ImageGrab
from PIL import Image
import os, time, sys
import keyboard


class Shooter:

    def __init__(self):
        self.screenshot_path = "./screenshots/"
        self.num_pages = 850
        self.X1 = 850
        self.Y1 = 137
        self.X2 = 2127
        self.Y2 = 1771

    def start_grab(self):
        time.sleep(5)
        old_im = None
        for i in range(self.num_pages):
            im = ImageGrab.grab(bbox=(self.X1,self.Y1,self.X2,self.Y2))
            if old_im == im:
                sys.exit()
            filename = "{}image{:03d}.png".format(self.screenshot_path, i)
            im.save(filename)
            keyboard.send('ctrl+page Down')
            time.sleep(2)
            old_im = im

    def single(self):
        time.sleep(3)
        im = ImageGrab.grab(bbox=(self.X1,self.Y1,self.X2,self.Y2))
        im.save(self.screenshot_path + "imagetest.png")

if __name__ == '__main__':
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
    s = Shooter()
    s.start_grab()