from preprocess import difference
from threshold import make_mask
from detection import find_boxes

def run_pipeline(test, temp, min_area=100, pad=0,
                 blur="median", k=5, method="otsu",
                 morph=True, thresh=50, kernel_size=3):

    # Calculate image differences
    diff = difference(test, temp, blur=blur, k=k)

    # Generate the binary mask
    mask = make_mask(
        diff, method=method, thresh=thresh,
        k=kernel_size, morph=morph
    )

    # Detect possible defect regions
    boxes = find_boxes(mask, min_area=min_area, pad=pad)

    return diff, mask, boxes
