#This script needs to be placed at the same hierarchy level of the taco_dataset_conversion.ipynb notebook.

import json, shutil
from pathlib import Path
from sklearn.model_selection import train_test_split

original_data_path = Path("./data")
with open(Path.joinpath(original_data_path,"annotations.json"), "r") as f:
    taco_data = json.loads(f.read())
annotations = taco_data["annotations"]
images = taco_data["images"]
number_annotations = len(annotations)
number_images = len(images)

bottle_ids_path = Path("./bottle_ids.json")
output_path = Path("./yolo_bottle_dataset")
Path.joinpath(output_path,"images/train").mkdir(parents=True,exist_ok=True)
Path.joinpath(output_path,"images/val").mkdir(parents=True,exist_ok=True)
Path.joinpath(output_path,"labels/train").mkdir(parents=True,exist_ok=True)
Path.joinpath(output_path,"labels/val").mkdir(parents=True,exist_ok=True)

with open(bottle_ids_path, "r") as f:
    target_categories = list(map(int, list(json.load(f).keys())))

image_ids = [image["id"] for image in images]
train_ids, test_ids = train_test_split(image_ids, test_size=0.2, random_state=42)

for annotation in annotations:
    if annotation["category_id"] not in target_categories:
        continue
    image = images[annotation["image_id"]]
    train_image = image["id"] in train_ids
    original_image_file_name = image["file_name"]
    image_file_name = original_image_file_name.replace('/',"_")
    image_width = image["width"]
    image_height = image["height"]

    src_image = Path.joinpath(original_data_path,original_image_file_name)
    if src_image.exists():
            
        # Convert Bounding Box
        # COCO: [x_min, y_min, width, height] -> YOLO: [x_center, y_center, width, height]
        dw, dh = 1./image_width, 1./image_height
        x = (annotation['bbox'][0] + annotation['bbox'][2]/2.0) * dw
        y = (annotation['bbox'][1] + annotation['bbox'][3]/2.0) * dh
        w = annotation['bbox'][2] * dw
        h = annotation['bbox'][3] * dh

        file_name_extension = "." + (image_file_name.split(".")[-1])

        if train_image:
            shutil.copy(src_image, output_path / "images/train" / image_file_name)
            with open(output_path / "labels/train" / image_file_name.replace(file_name_extension, '.txt'), 'a') as f_label:
                f_label.write(f"0 {x} {y} {w} {h}\n")
        else:
            shutil.copy(src_image, output_path / "images/val" / image_file_name)
            with open(output_path / "labels/val" / image_file_name.replace(file_name_extension, '.txt'), 'a') as f_label:
                f_label.write(f"0 {x} {y} {w} {h}\n")
print("Done!")