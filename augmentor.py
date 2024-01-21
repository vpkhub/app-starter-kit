import Augmentor
import os
import shutil

def augment_images(input_path, output_path, num_augmented_images):
    # Create an Augmentor Pipeline
    pipeline = Augmentor.Pipeline(input_path)

    # Define augmentation operations
    pipeline.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
    pipeline.flip_left_right(probability=0.5)
    pipeline.zoom_random(probability=0.5, percentage_area=0.8)
    pipeline.flip_top_bottom(probability=0.5)
    pipeline.random_distortion(probability=0.5, grid_width=4, grid_height=4, magnitude=8)
    pipeline.random_brightness(probability=0.7, min_factor=0.8, max_factor=1.2)
    pipeline.random_contrast(probability=0.7, min_factor=0.8, max_factor=1.2)

    # Execute the augmentation process
    pipeline.sample(num_augmented_images)

    # Get a list of the original image filenames
    original_images = [file for file in os.listdir(input_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Move augmented images to the output folder with the original image names
    for augmented_image in os.listdir(pipeline.augmentor_images_output):
        if augmented_image.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            original_image_name = original_images.pop(0)
            augmented_image_path = os.path.join(pipeline.augmentor_images_output, augmented_image)
            new_image_path = os.path.join(output_path, f"{os.path.splitext(original_image_name)[0]}_augmented_{augmented_image}")
            shutil.move(augmented_image_path, new_image_path)

if __name__ == "__main__":
    input_folder = "/path/to/your/images"
    output_folder = "/path/to/your/output"
    num_augmented_images = 5  # Adjust as needed

    augment_images(input_folder, output_folder, num_augmented_images)
