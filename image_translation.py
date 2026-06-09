from PIL import Image, ImageOps

image = Image.open("input_image.png.png")

translated_image = ImageOps.grayscale(image)

translated_image.save("output_image.jpg")

print("Image translation completed!")