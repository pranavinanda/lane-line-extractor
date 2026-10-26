
import cv2
import numpy as np
def load_image(path):
    image = cv2.imread(path)

    if image is None:
        print("Could not open or load:", path)

    return image

def filter_colors(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    #white
    lower_white = np.array([0, 0, 150])
    upper_white = np.array([179, 80, 255])

    #yellow
    lower_yellow = np.array([15, 70, 100])
    upper_yellow = np.array([40, 255, 255])

    white_mask = cv2.inRange(hsv, lower_white, upper_white)
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    cv2.imshow("white only", white_mask)
    cv2.imshow("yellow only", yellow_mask)

    combined_mask = cv2.bitwise_or(white_mask, yellow_mask)

    filtered = cv2.bitwise_and(image, image, mask=combined_mask)

    return combined_mask, filtered


def convert_to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_blur(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

def detect_edges(image):
    return cv2.Canny(image, 50, 150)

def create_roi_mask(edges):
    height, width = edges.shape

    roi_mask = np.zeros_like(edges)

    points = np.array([[
        (0, height - 1),
        (0, int(0.85 * height)),
        (int(0.25 * width), int(0.55 * height)),
        (int(0.75 * width), int(0.55 * height)),
        (width - 1, int(0.85 * height)),
        (width - 1, height - 1)
    ]], dtype=np.int32)

    cv2.fillPoly(roi_mask, points, 255)

    return roi_mask

def apply_roi(edges, roi_mask):
    return cv2.bitwise_and(edges, roi_mask)

def show_and_save(title, image, path):
    cv2.imwrite(path, image)

    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":

    names = [
        "image1.jpg",
        "image2.jpg",
        "image3.jpeg",
        "image4.jpg"
    ]

    for name in names:

        image_path = "images/" + name

        print("\nProcessing:", image_path)

        # 1. Load image
        image = load_image(image_path)

        if image is None:
            continue

        # Create output folder path
        image_name = name.split(".")[0]
        output_folder = "outputs/" + image_name

        # 2. Original image
        show_and_save(
            "1. Original Image",
            image,
            output_folder + "/1_original.jpg"
        )

        # 3. White mask and filtered image
        white_mask, filtered = filter_colors(image)

        show_and_save(
            "2. White Mask",
            white_mask,
            output_folder + "/2_white_mask.jpg"
        )

        # 4. Grayscale image
        gray = convert_to_gray(filtered)

        # 5. Gaussian blur
        blurred = apply_blur(gray)

        show_and_save(
            "3. Gaussian Blur",
            blurred,
            output_folder + "/3_blurred.jpg"
        )

        # 6. Canny edges
        edges = detect_edges(blurred)

        show_and_save(
            "4. Canny Edges",
            edges,
            output_folder + "/4_edges.jpg"
        )

        # 7. ROI mask
        roi_mask = create_roi_mask(edges)

        show_and_save(
            "5. ROI Mask",
            roi_mask,
            output_folder + "/5_roi_mask.jpg"
        )

        # 8. Final ROI-masked edges
        final_lanes = apply_roi(edges, roi_mask)

        show_and_save(
            "6. ROI Masked Edges",
            final_lanes,
            output_folder + "/6_final_lanes.jpg"
        )

    print("\nAll images processed!")
    print("Check the outputs folder.")



