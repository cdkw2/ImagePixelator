from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import filedialog

def generate_monochrome_pixel_art(pixel_size, scale):
    # Prompt the user to select an image file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    # Load the image
    original_image = Image.open(file_path)

    # Resize the image to a multiple of the pixel size
    width, height = original_image.size
    width = (width // pixel_size) * pixel_size
    height = (height // pixel_size) * pixel_size
    resized_image = original_image.resize((width, height))

    # Convert the resized image to black and white
    grayscale_image = resized_image.convert("L")

    # Create a new image to hold the pixel art
    scaled_size = (width // scale, height // scale)
    pixel_art = Image.new("RGB", scaled_size, color="white")

    # Draw each pixel of the pixel art by using the black and white value as the intensity
    draw = ImageDraw.Draw(pixel_art)
    for y in range(0, height, pixel_size):
        for x in range(0, width, pixel_size):
            box = (x // scale, y // scale, (x + pixel_size) // scale, (y + pixel_size) // scale)
            region = grayscale_image.crop((x, y, x + pixel_size, y + pixel_size))
            intensity = region.getpixel((0, 0))
            draw.rectangle(box, fill=(intensity, intensity, intensity))

    return pixel_art

pixel_art = generate_monochrome_pixel_art(pixel_size=20, scale=5)
pixel_art.save("output_image.png")
