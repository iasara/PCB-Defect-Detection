from preprocess import difference
from threshold import make_mask
from detection import find_boxes

def run_pipeline(test, temp, min_area=100, pad=0):

    # Calculate the difference between images
    diff = difference(test, temp, blur="median", k=5)

    # Convert the difference into a binary mask
    mask = make_mask(diff, method="otsu")

    # Detect possible defect regions
    boxes = find_boxes(mask, min_area=min_area, pad=pad)

    return diff, mask, boxes
