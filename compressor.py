
# get Pillow (fork of PIL) from
# pip before running -->
# pip install Pillow

# import required libraries
from pickletools import optimize
from PIL import Image
import os

# Set the path of the Origin file
downloadFolder = "/Users/Alba/Downloads/"
# Set the path of the Destiny file
picturesFolder = "/Users/Alba/Pictures/"

if __name__ == "__main__":

    # looping through all the files in downloadFolder
    for filename in os.listdir(downloadFolder):
        name, extension = os.path.splitext(downloadFolder + filename)

        # If the file format is JPG JPEG or PNG
        if extension in [".jpg", ".jpeg", ".png"]:

            # open the image
            picture = Image.open(downloadFolder + filename)
            
            # Save the picture with desired quality
            picture.save(picturesFolder + "compressed_"+filename, optimize=True, quality=60)
            os.remove(downloadFolder + filename)
            print("compressing", filename)

        

    print("Done")       
