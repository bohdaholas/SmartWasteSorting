import sys
import os
import shutil
from sklearn.model_selection import train_test_split

input_dir = sys.argv[1]
output_dir = sys.argv[2]

classes = os.listdir(input_dir)
images = []
labels = []
for class_name in classes:
    print(class_name)
    class_dir = os.path.join(input_dir, class_name)
    for filename in os.listdir(class_dir):
        file_path = os.path.join(class_dir, filename)
        if filename[-3:] == "txt":
            labels.append(file_path)
            pre, _ = os.path.splitext(file_path)
            images.append(pre + ".jpg")

images.sort()
labels.sort()
train_images, val_images, train_labels, val_labels = train_test_split(images, labels, test_size = 0.2)
val_images, test_images, val_labels, test_labels = train_test_split(val_images, val_labels, test_size = 0.5)

def copy_files(files, folder):
    for filename in files:
        shutil.copy(filename, os.path.join(output_dir, folder))
       
copy_files(train_images + train_labels, 'train')
copy_files(val_images + val_labels, 'val')
copy_files(test_images + test_labels, 'test')
