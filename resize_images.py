import sys
import os
from PIL import Image

def resize_images(folder_path, target_size):
    image_files = [f for f in os.listdir(folder_path) if f[-3:]=="jpg"]

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image = Image.open(image_path)

        resized_image = image.resize((target_size, target_size))

        bounding_box_file = os.path.splitext(image_file)[0] + ".txt"
        bounding_box_path = os.path.join(folder_path, bounding_box_file)

        with open(bounding_box_path, 'r') as file:
            lines = file.readlines()

        resized_bounding_box = []
        for line in lines:
            try:
                class_index, x, y, w, h = line.strip().split()
                x = float(x) * target_size / image.width
                y = float(y) * target_size / image.height
                w = float(w) * target_size / image.width
                h = float(h) * target_size / image.height
                resized_bounding_box.append(f'{class_index} {x} {y} {w} {h}\n')
            except:
                print(image_file)

        resized_image.save(image_path)

images_dir = sys.argv[1]
resize_images(os.path.join(images_dir, "train"), 640)
resize_images(os.path.join(images_dir, "val"), 640)
resize_images(os.path.join(images_dir, "test"), 640)
