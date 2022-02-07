import img2pdf
import os
from PIL import Image

class To_PDF:
    def convert(self):
        screenshot_path = "./screenshots/"
        image_files = os.listdir(screenshot_path)
        image_files.sort()

        with open("output.pdf", "wb") as f:
            f.write(img2pdf.convert([screenshot_path+i for i in image_files]))
    
    def convert_2(self):
        ###not working
        screenshot_path = "./screenshots/"
        image_files = os.listdir(screenshot_path)
        image_files.sort()

        with Image.open(screenshot_path+image_files[0]) as im1:
            im1.save("output2.pdf")

        for image_file in image_files[1:]:
            image = Image.open(screenshot_path+image_file)
            pdf = Image.open("output2.pdf")
            pdf.save("output2.pdf",save_all=True, append_images=[image])
            pdf.close()
            image.close()

    def remove_transparency(self, bg_colour=(255, 255, 255)):
        ## maybe working
        screenshot_path = "./screenshots/"
        image_files = os.listdir(screenshot_path)
        image_files.sort()

        for image_file in image_files:
            im = Image.open(screenshot_path+image_file)
            # Only process if image has transparency (http://stackoverflow.com/a/1963146)
            if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):

                # Need to convert to RGBA if LA format due to a bug in PIL (http://stackoverflow.com/a/1963146)
                alpha = im.convert('RGBA').split()[-1]

                # Create a new background image of our matt color.
                # Must be RGBA because paste requires both images have the same format
                # (http://stackoverflow.com/a/8720632  and  http://stackoverflow.com/a/9459208)
                bg = Image.new("RGBA", im.size, bg_colour + (255,))
                bg.paste(im, mask=alpha)
                bg.save(screenshot_path+image_file)
                print(f"converted {image_file}")

            else:
                print(f'failed to convert {image_file}')


if __name__ == "__main__":
    To_PDF().convert()