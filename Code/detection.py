import cv2

def find_boxes(binary, min_area=100, pad=0):
    # Find contours in the binary image
    contours, _ = cv2.findContours(
        binary.copy(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    boxes = []
    height, width = binary.shape[:2]

    for contour in contours:
        # Ignore small regions
        area = cv2.contourArea(contour)

        if area >= min_area:
            # Get bounding box coordinates
            x, y, w, h = cv2.boundingRect(contour)

            # Add padding without exceeding image boundaries
            x1 = max(0, x - pad)
            y1 = max(0, y - pad)
            x2 = min(width, x + w + pad)
            y2 = min(height, y + h + pad)

            boxes.append((x1, y1, x2, y2))

    return boxes
