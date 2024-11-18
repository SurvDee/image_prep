import cv2
import os

def split_rgb_channels(input_folder):
    # Define paths for the R, G, and B folders
    red_folder = os.path.join(input_folder, 'RED')
    green_folder = os.path.join(input_folder, 'GREEN')
    blue_folder = os.path.join(input_folder, 'BLUE')

    # Create folders if they don't already exist
    os.makedirs(red_folder, exist_ok=True)
    os.makedirs(green_folder, exist_ok=True)
    os.makedirs(blue_folder, exist_ok=True)

    # List all files in the input folder
    for image_file in os.listdir(input_folder):
        # Check if the file is an RGB image
        if image_file.lower().endswith('-rgb_512px.png'):
            image_path = os.path.join(input_folder, image_file)

            # Load the RGB image
            image = cv2.imread(image_path)
            if image is None:
                print(f"Error loading image: {image_path}")
                continue

            # Split the image into R, G, B channels
            blue_channel, green_channel, red_channel = cv2.split(image)

            # Extract the base name without the '-RGB_512px' part
            base_name = image_file.replace('-RGB_512px.png', '')

            # Save each channel as a separate image in its designated folder
            red_image_path = os.path.join(red_folder, f"{base_name}-RED_512px.png")
            green_image_path = os.path.join(green_folder, f"{base_name}-GREEN_512px.png")
            blue_image_path = os.path.join(blue_folder, f"{base_name}-BLUE_512px.png")

            cv2.imwrite(red_image_path, red_channel)
            cv2.imwrite(green_image_path, green_channel)
            cv2.imwrite(blue_image_path, blue_channel)

            print(f"Saved {red_image_path}, {green_image_path}, and {blue_image_path}")
        else:
            print(f"Skipping non-RGB file: {image_file}")

# Example usage
input_folder = 'D:\\PG\\3rd_semester\\Data\\Project_Data\\work\\splitted_sorted\\images_cloud\\1_rgb\\bev_cld_00116-RGB'  # Replace with your folder path
split_rgb_channels(input_folder)

