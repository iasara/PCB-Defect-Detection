"""
Role 2 - Preprocessing & Subtraction
ARTI 403 - Group 2 - Automated PCB Defect Detection

Interface (agreed between roles):
    difference(test, temp, blur, k) -> diff image

    test  : defective image (BGR or grayscale, numpy array)
    temp  : defect-free template image (same size as test)
    blur  : "none" | "gaussian" | "median"
    k     : filter size (odd number, e.g. 3, 5, 7). Ignored when blur="none".

Returns a single-channel uint8 image where bright pixels show
where the test image differs from the template (possible defects).
"""

import cv2

# Settings that Role 6 can change in experiments
BLUR_OPTIONS = ("none", "gaussian", "median")
DEFAULT_BLUR = "gaussian"
DEFAULT_K = 5


def to_gray(img):
    """Convert to grayscale if the image has 3 channels."""
    if img.ndim == 3:
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


def denoise(gray, blur=DEFAULT_BLUR, k=DEFAULT_K):
    """Apply the chosen noise-removal filter to a grayscale image."""
    blur = blur.lower()
    if blur not in BLUR_OPTIONS:
        raise ValueError(f"blur must be one of {BLUR_OPTIONS}, got '{blur}'")
    if blur == "none":
        return gray
    if k < 1 or k % 2 == 0:
        raise ValueError(f"k must be a positive odd number, got {k}")
    if blur == "gaussian":
        return cv2.GaussianBlur(gray, (k, k), 0)
    return cv2.medianBlur(gray, k)  # median


def difference(test, temp, blur=DEFAULT_BLUR, k=DEFAULT_K):
    """Grayscale -> denoise -> absolute difference."""
    if test.shape[:2] != temp.shape[:2]:
        raise ValueError(f"image sizes differ: {test.shape[:2]} vs {temp.shape[:2]}")
    test_g = denoise(to_gray(test), blur, k)
    temp_g = denoise(to_gray(temp), blur, k)
    return cv2.absdiff(test_g, temp_g)


if __name__ == "__main__":
    # Quick standalone test (does not need Role 1's code):
    #   python preprocess.py path/to/xxx_test.jpg path/to/xxx_temp.jpg
    import sys

    if len(sys.argv) != 3:
        print("usage: python preprocess.py <test.jpg> <temp.jpg>")
        sys.exit(1)
    test_img = cv2.imread(sys.argv[1])
    temp_img = cv2.imread(sys.argv[2])
    for b in BLUR_OPTIONS:
        d = difference(test_img, temp_img, b, DEFAULT_K)
        out = f"diff_{b}.png"
        cv2.imwrite(out, d)
        print(f"{b:9s} -> {out}  (non-zero pixels: {(d > 0).sum()})")
