import os
import sys
from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt

# initialize COCO API for instance annotations
# path to cocoapi directory
data_dir = "/root/project3/COCO2014"
instances_ann_file = os.path.join(
    data_dir, "annotations_DCC", "captions_split_set_zebra_val_test_novel2014.json"
)
coco = COCO(instances_ann_file)

# # initialize COCO API for caption annotations
# captions_ann_file = os.path.join(data_dir, "annotations", f"captions_{data_type}.json")
# coco_caps = COCO(captions_ann_file)

# get image ids
ids = list(coco.anns.keys())


# pick a random image and obtain the corresponding URL
ann_id = np.random.choice(ids)
img_id = coco.anns[ann_id]["image_id"]
img = coco.loadImgs(img_id)[0]
url = img["url"]

print(img)
# print URL and visualize corresponding image
print(url)
I = io.imread(url)
plt.axis("off")
plt.imshow(I)

# load and display captions
ann_ids = coco.getAnnIds(imgIds=img["id"])
anns = coco.loadAnns(ann_ids)
coco.showAnns(anns)