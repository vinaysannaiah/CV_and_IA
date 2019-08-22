''' Read the first image from all the
sub folders and plot it in a single figure '''

import os
import matplotlib.pyplot as plt
from matplotlib import image as mat_image

# source folder path for all the images
src_path = '/home/vinay/All_codes/GitHub/CV_and_IA/computer_vision_edx/data/voc'

# setup a definite figure size
fig = plt.figure(figsize=(15, 15))

for root, folders, filenames in os.walk(src_path):
    # get all the folder details
    # get the count of folders
    image_num = 0
    # num folders for plotting purpose
    num_folders = len(folders)
    for folder in sorted(folders):
        # for every folder
        image_num += 1
        # list the images, sort and get the first image
        file_name = sorted(os.listdir(os.path.join(root, folder)))[0]
        # get the full path of the image
        file_path = os.path.join(root, folder, file_name)
        # read the image
        image = mat_image.imread(file_path)
        # plot the images add_subplot(rows, columns, number)
        a = fig.add_subplot(num_folders, 1, image_num)
        # show the image
        image_plot = plt.imshow(image)
        # set the title for every image in the sub-plot
        a.set_title(folder)
# enable plot view
plt.show()
