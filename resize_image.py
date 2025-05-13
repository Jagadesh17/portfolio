from PIL import Image
import os

def resize_image(input_path, output_path, size=(400, 400)):
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Convert to RGB if necessary
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Resize the image
            resized_img = img.resize(size, Image.Resampling.LANCZOS)
            
            # Save the resized image
            resized_img.save(output_path, 'JPEG', quality=95)
            print(f"Image successfully resized and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Use the specified image path
input_file = 'D:/Projects/portfolio-main/photo.jpg'  # Your photo path
output_file = 'images/profile.jpg'

# Resize the image
resize_image(input_file, output_file) 