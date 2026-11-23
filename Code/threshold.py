import cv2

THRESH = 50
BLOCK = 31
C = -25
KERNEL = 3

def make_mask(diff, method="otsu", thresh=THRESH,
              block=BLOCK, c=C, k=KERNEL, morph=True):

    # Convert the difference image into a binary mask
    if method == "fixed":
        _, mask = cv2.threshold(
            diff, thresh, 255, cv2.THRESH_BINARY
        )

    elif method == "otsu":
        _, mask = cv2.threshold(
            diff, 0, 255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

    elif method == "adaptive":
        mask = cv2.adaptiveThreshold(
            diff, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY, block, c
        )

    else:
        raise ValueError("method must be fixed, otsu or adaptive")

    # Remove small noise and refine detected regions
    if morph and k > 1:
        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT, (k, k)
        )

        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    return mask
