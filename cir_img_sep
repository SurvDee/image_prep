import cv2
import os

def split_cir_channels(input_folder):
    # Define paths for the NIR, R, and G folders
    nir_folder = os.path.join(input_folder, 'NIR')
    red_folder = os.path.join(input_folder, 'RED')
    green_folder = os.path.join(input_folder, 'GREEN')

    # Create folders if they don't already exist
    os.makedirs(nir_folder, exist_ok=True)
    os.makedirs(red_folder, exist_ok=True)
    os.makedirs(green_folder, exist_ok=True)

    # List all files in the input folder
    for image_file in os.listdir(input_folder):
        # Check if the file is an CIR image
        if image_file.lower().endswith('-cir_512px.png'):
            image_path = os.path.join(input_folder, image_file)

            # Load the CIR image
            image = cv2.imread(image_path)
            if image is None:
                print(f"Error loading image: {image_path}")
                continue

            # Split the image into NIR, R, and G channels  
            green_channel, red_channel, nir_channel = cv2.split(image)

            # Extract the base name without the '-cir_512px' part
            base_name = image_file.replace('-cir_512px.png', '')

            # Save each channel as a separate image in its designated folder
            nir_image_path = os.path.join(nir_folder, f"{base_name}-NIR_512px.png")
            red_image_path = os.path.join(red_folder, f"{base_name}-RED_512px.png")
            green_image_path = os.path.join(green_folder, f"{base_name}-GREEN_512px.png")

            cv2.imwrite(nir_image_path, nir_channel)
            cv2.imwrite(red_image_path, red_channel)
            cv2.imwrite(green_image_path, green_channel)

            print(f"Saved {nir_image_path}, {red_image_path}, and {green_image_path}")
        else:
            print(f"Skipping non-RGB file: {image_file}")

# Example usage
input_folder = 'D:\\PG\\3rd_semester\\Data\\Project_Data\\work\\splitted_sorted\\images_cloud\\2_cir\\512px_cir'  # Replace with your folder path
split_cir_channels(input_folder)
