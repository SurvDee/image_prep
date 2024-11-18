import cv2
import numpy as np
import os

def compute_and_save_indices(band_folders, output_folder):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Iterate through each folder for each band (e.g., 'cloud_Red', 'cloud_Green', etc.)
    image_names = set()
    
    # Collect all image names from the RED, GREEN, NIR folders
    for band_folder in band_folders:
        for image_file in os.listdir(band_folder):
            if image_file.endswith('_512px.png'):  # Only process the image files
                image_name = image_file.split('-')[0]  # Get the base name (e.g., split_0_bev_cld_00116)
                image_names.add(image_name)

    # Now process each image by gathering its bands (RED, GREEN, NIR)
    for image_name in image_names:
        band_images = {}

        # Load the corresponding band images for the current image_name (RED, GREEN, NIR)
        for band_folder in band_folders:
            for image_file in os.listdir(band_folder):
                if image_name in image_file and image_file.endswith('_512px.png'):  # Match the base name
                    # Determine the band name (RED, GREEN, NIR) from the folder or file name
                    if 'RED' in band_folder:
                        band_name = 'RED'
                    elif 'GREEN' in band_folder:
                        band_name = 'GREEN'
                    elif 'NIR' in band_folder:
                        band_name = 'NIR'
                    else:
                        continue
                    
                    # Full path to the band image
                    image_path = os.path.join(band_folder, image_file)
                    band_image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
                    
                    # Store the band image in the dictionary by its band name
                    band_images[band_name] = band_image

        # Once all the bands (RED, GREEN, NIR) are loaded for the image, compute the indices
        if 'RED' in band_images and 'GREEN' in band_images and 'NIR' in band_images:
            indices = {}

            red = band_images['RED']
            green = band_images['GREEN']
            nir = band_images['NIR']
            
            # Compute the indices

            # NDVI (using NIR and RED)
            ndvi = (nir.astype(float) - red) / (nir + red + 1e-5)
            indices['NDVI'] = ndvi

            # NDWI (using GREEN and NIR)
            ndwi = (green.astype(float) - nir) / (green + nir + 1e-5)
            indices['NDWI'] = ndwi

            # NDCI (using NIR and GREEN)
            ndci = (nir.astype(float) - green) / (nir + green + 1e-5)
            indices['NDCI'] = ndci

            # Brightness Index (using RED, GREEN, NIR)
            brightness_index = np.sqrt(np.square(red) + np.square(green) + np.square(nir))
            indices['Brightness_Index'] = brightness_index

            # Shadow Index (using RED, GREEN, NIR)
            shadow_index = (red + green + nir) / 3
            indices['Shadow_Index'] = shadow_index

            # Save each computed index as an image
            for index_name, index_data in indices.items():
                index_path = os.path.join(output_folder, index_name)
                os.makedirs(index_path, exist_ok=True)
                
                # Define the save path for each index
                save_path = os.path.join(index_path, f"{image_name}-{index_name}_512px.png")
                
                # Save as an 8-bit image (scaling the indices)
                cv2.imwrite(save_path, (index_data * 255).astype(np.uint8))
                print(f"Saved {index_name} for {image_name} at {save_path}")

# Define the paths to your band folders and output folder
band_folders = [
    'D:\\PG\\3rd_semester\\Data\\Project_Data\\work\\splitted_sorted\\images_cloud\\2_cir\\RED',
    'D:\\PG\\3rd_semester\\Data\\Project_Data\\work\\splitted_sorted\\images_cloud\\2_cir\\GREEN',
    'D:\\PG\\3rd_semester\\Data\\Project_Data\\work\\splitted_sorted\\images_cloud\\2_cir\\NIR'
]  # Add the correct paths to your band folders
output_folder = 'D:\\PG\\3rd_semester\\Data\\Project_Data\\work\\splitted_sorted\\images_cloud\\2_cir\\indices'  # Path to save indices

# Run the function to generate and save indices
compute_and_save_indices(band_folders, output_folder)
