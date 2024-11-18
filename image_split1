import cv2
import os

def split_images_in_folder(input_folder, patch_size=512):
    # Args:
        # input_folder (str): Path to the folder containing input images.
        # patch_size (int, optional): Size of the patches (in pixels). Defaults to 120.

    # List all files in the input folder
    for image_file in os.listdir(input_folder):
        # Check if the file is a JPEG image
        if image_file.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(input_folder, image_file)

            # Load the image
            image = cv2.imread(image_path)

            # Check if image loading was successful
            if image is None:
                print(f"Error: Could not load image from {image_path}. Please check the path and ensure it's a valid image.")
                continue

            # Create an output folder for the current image
            image_name = os.path.splitext(image_file)[0]
            output_folder = os.path.join(input_folder, image_name)  # Create a folder with the image name
            os.makedirs(output_folder, exist_ok=True)

            h, w, _ = image.shape
            patch_count = 0

            # Loop through the image and extract patches
            for i in range(0, h, patch_size):
                for j in range(0, w, patch_size):
                    # Ensure we do not go out of bounds
                    patch = image[i:i + patch_size, j:j + patch_size]
                    if patch.shape[0] == patch_size and patch.shape[1] == patch_size:
                        patch_filename = f'split_{patch_count}_{image_name}_{patch_size}px.png'
                        cv2.imwrite(os.path.join(output_folder, patch_filename), patch)
                        patch_count += 1

            print(f'Split {patch_count} patches from {image_file} and saved to {output_folder}')

# Example usage
input_folder = '/content/drive/MyDrive/Thesis_project/RGB'  # Change this to your input folder path
split_images_in_folder(input_folder)
