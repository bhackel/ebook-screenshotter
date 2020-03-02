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


if __name__ == "__main__":
	To_PDF().convert()