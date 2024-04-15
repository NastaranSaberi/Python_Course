import os
import imageio


file_list = sorted(os.listdir("Session8/images"))

IMAGES = []
for file_name in file_list:
    file_path = "Session8/images/" + file_name
    image = imageio.imread(file_path)
    IMAGES.append(image)
    

imageio.mimsave("Session8/my_output.gif", IMAGES)



