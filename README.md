# OTP exercise

We'll be using a Python implementation of the [One-Time-Pad (OTP)](https://en.wikipedia.org/wiki/One-time_pad) cipher for encrypting/decrypting images. Thus, the plaintext, the ciphertext and the key are all images (they will be called *plain-image*, *cipher-image* and just *key*, respectively), which need to be of the same size (in number of pixels) for the cipher to work.
Since OTP needs the key to be random, the keys that we’ll be using have been obtained from a [Random Bitmap Generator](https://www.random.org/bitmaps).

## Running the script

The file *images_xor.py* is the Python script implementing the cipher, so it's the one you need to use to encrypt and decrypt.
To run it, you need to first install the [Pillow](https://pillow.readthedocs.io/en/stable/index.html) Python imaging library, which handles images.

The *images_xor.py* script can be run as follows

    python3 images_xor.py -p <plain> -k <key> -c <result>

where 
  
    <plain>   is the name of the file containing the plain-image if we’re encrypting (or the cipher-image, if we’re decrypting)
    <key>     is the name of the file containing the key to encrypt/decrypt
    <result>  is the name of the file where the resulting XORed image will be stored

    
**Both \<plain\> and \<key\> need to be B/W bitmap images of the same size (in number of pixels)**. You're encouraged to have a look at the source code and try to understand how it works. You can play and get familiar with the program by encrypting and decrypting images of your own, just remember that the key needs to be of the same size as the image you want to encrypt, and that the same key needs to be used for encryption and decryption (recall OTP is symmetric encryption). The folder *example* also provides some images to play with.

## What you're asked to do

1. Decrypting a ciphertext knowing the key
Under the folder *decrypting_otp* you will find a cipher-image and a key. Using the *images_xor.py* script, decrypt the cipher-image and recover the corresponding plain-image.

2. Breaking OTP when the key has been reused
Under the folder *breaking_otp* you will find two cipher-images. We don’t know anything about the corresponding plaintexts, only that they are images and that the same key has been used for both encryptions.

    - a. Can you get any information about the two plaintexts? Beware that we don’t aim at entirely recovering them (which is possible but a bit more complicated (*)). We just want to find out how they look like.

    - b. Find out and explain, in a more formal way (maybe using some mathematical expressions), why it’s a bad idea to reuse the key in OTP. You will need to use the XOR properties seen in class.

3. OTP alternatives
OTP, by definition, works XORing the plaintext with the key to encrypt, and XORing the ciphertext with the same key to decrypt. Modify the *images_xor.py* script to use the binary operators AND, and then also OR, instead of XOR. What do you observe in both cases and why?

(*) You’re of course welcome to try, as a bonus exercise.





