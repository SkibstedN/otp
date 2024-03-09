#!/usr/bin/python

from PIL import Image
import numpy as np

def xor_images(image_path1, image_path2, result_path):
    # Åbner de to billeder og konverterer dem til numpy arrays
    image1 = Image.open(image_path1).convert("L") # Konverterer til grayscale
    image2 = Image.open(image_path2).convert("L")
    
    image1_array = np.array(image1)
    image2_array = np.array(image2)
    
    # Tjekker at billederne har samme dimensioner
    if image1_array.shape != image2_array.shape:
        raise ValueError("Billederne skal være af samme størrelse.")
    
    # Udfører XOR operationen på billederne
    result_array = np.bitwise_xor(image1_array, image2_array)
    
    # Konverterer det resulterende array tilbage til et billede
    result_image = Image.fromarray(result_array)
    result_image.save(result_path)

# Erstat 'image_path1', 'image_path2', og 'result_path' med de faktiske stier

    
xor_images('ciphertext1.gif', 'ciphertext2.gif', 'result.gif')

