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

# collect all images in label categories and put them in either productive or unproductive

data_subsets=["test", "train", "val"]
default_subset = "train"
for subset in data_subsets:
    if subset == default_subset: continue
    subset_path = os.path.join(dataset_path, subset)
    for label in labels:
        source_subset_path = os.path.join(subset_path, label)
        destination_subset_path = os.path.join(dataset_path, default_subset, label)
        for filename in os.listdir(source_subset_path):
            source_path = os.path.join(source_subset_path, filename)
            destination_path = os.path.join(destination_subset_path, filename)
            shutil.move(source_path, destination_path)