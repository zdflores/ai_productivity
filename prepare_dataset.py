import os
import shutil
import random

dataset_path = './dataset'
labels_file_path = os.path.join(dataset_path, "labels.txt")
with open(labels_file_path) as f:
    labels = f.readlines()
labels = [label.strip() for label in labels]

labels = [label for label in labels if len(label) > 0]
labels = list(sorted(labels))
print(f"dataset labels: {labels}")