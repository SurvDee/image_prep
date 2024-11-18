import os
import cv2

def split_image(image_path, output_folder, patch_size=512):
    """
    Splits an image into smaller patches of the specified size.

    Args:
        image_path (str): Path to the input image.
        output_folder (str): Path to the folder where patches will be saved.
        patch_size (int): Size of the patches (default is 512).
    """
    os.makedirs(output_folder, exist_ok=True)
    image = cv2.imread(image_path)
    img_height, img_width, _ = image.shape

    # Loop to extract patches
    patch_id = 0
    for y in range(0, img_height, patch_size):
        for x in range(0, img_width, patch_size):
            # Crop patch
            patch = image[y:y+patch_size, x:x+patch_size]

            # Skip incomplete patches
            if patch.shape[0] != patch_size or patch.shape[1] != patch_size:
                continue

            # Save patch
            base_name = os.path.basename(image_path).split('.')[0]
            patch_filename = f"{base_name}_patch_{patch_id:04d}.png"
            patch_path = os.path.join(output_folder, patch_filename)
            cv2.imwrite(patch_path, patch)
            patch_id += 1

            print(f"Saved patch: {patch_path}")

def process_folder(input_folder, output_folder, patch_size=512):
    """
    Splits all images in the input folder into smaller patches.

    Args:
        input_folder (str): Path to the input folder with images.
        output_folder (str): Path to the folder where patches will be saved.
        patch_size (int): Size of each patch (default is 512).
    """
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all image files in the folder
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tif', '.tiff')):
            image_path = os.path.join(input_folder, file_name)
            split_image(image_path, output_folder, patch_size)

# Define paths
input_folder = "D:\\PG\\3rd_semester\\Data\\Project_Data\\work\\images"  # Replace with your actual input folder
output_folder = "D:\\PG\\3rd_semester\\Data\\Project_Data\\work\\patches"  # Replace with your desired output folder

# Run the script
process_folder(input_folder, output_folder, patch_size=512)
