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
# track all images in each dataset category.
images={}
for label in labels:
    images[label] = os.listdir(os.path.join(dataset_path, default_subset, label))
    print(f"label: {label}, images: {len(images[label])}")
#shuffle the dataset
for label in labels:
    random.shuffle(images[label])
#specify percent of dataset for test/val
val_percentage = 0.1
test_percentage = 0.1
for label in labels:
    test_count = int(len(images[label]) * test_percentage)
    val_count = int(len(images[label]) * val_percentage)
    for i in range(test_count):
        filename = images[label].pop()
        source_path = os.path.join(dataset_path, default_subset, label, filename)
        destination_path = os.path.join(dataset_path, "test", label, filename)
        shutil.move(source_path, destination_path)
    for i in range(val_count):
        filename = images[label].pop()
        source_path = os.path.join(dataset_path, default_subset, label, filename)
        destination_path = os.path.join(dataset_path, "val", label, filename)
        shutil.move(source_path, destination_path)

