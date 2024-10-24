import os
import pandas as pd
import cv2
import random
import numpy as np

root_directory = "/home/ilkham/Penugasan GamaForce/Gambar"

files = os.listdir(f"{root_directory}")

images = "images"
masks = "masks"

images_path = os.path.join(root_directory, images)
masks_path = os.path.join(root_directory, masks)

output_folder = "output_folder"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files_1 = [f for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]
files_2 = [f for f in os.listdir(masks_path) if os.path.isfile(os.path.join(masks_path, f))]

random.shuffle(files_1)
random.shuffle(files_2)

for i, (file_1_name, file_2_name) in enumerate(zip(files_1, files_2)):
    file_1_path = os.path.join(images_path, file_1_name)
    file_2_path = os.path.join(masks_path, file_2_name)

    try:
        df1 = pd.read_csv(file_1_path)
        df2 = pd.read_csv(file_2_path)

        merged_df = pd.concat([df1, df2], ignore_index=True)

        output_file_path = os.path.join(output_folder, f"merged_file_{i+1}.csv")
        merged_df.to_csv(output_file_path, index=False)
    except Exception as e:
        pass

image_files_1 = [f for f in os.listdir(images_path) if f.endswith(('.png'))]
image_files_2 = [f for f in os.listdir(masks_path) if f.endswith(('.png'))]

common_image_files = set(image_files_1).intersection(image_files_2)

combine = ["1", "2", "3", "4", "5", "6"]

a = 0
for i, image_name in enumerate(list(common_image_files)[:3]):
    image_1_path = os.path.join(images_path, image_name)
    image_2_path = os.path.join(masks_path, image_name)

    img1 = cv2.imread(image_1_path)
    img2 = cv2.imread(image_2_path)
    
    img1 = cv2.resize(img1, (300, 300))
    img2 = cv2.resize(img2, (300, 300))
    
    combine[i+a] = img1
    a += 1
    combine[i+a] = img2

white_image = np.ones((30, 960, 3), np.uint8) * 255
pisah = np.ones((300, 30, 3), np.uint8) * 255

row1 = np.hstack([combine[0], pisah, combine[2], pisah, combine[4]])
row2 = np.hstack([combine[1], pisah, combine[3], pisah, combine[5]])

combined_image = np.vstack([row1, white_image, row2])

cv2.imshow('Combined Image', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()