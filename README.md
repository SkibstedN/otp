# otp

We’ll be using a Python implementation of the One-Time-Pad (OTP) cipher for encrypting/decrypting images. Thus, the plaintext, the ciphertext and the key are all images (they will be called plain-image, cipher-image and just key, respectively), which need to be of the same size (in number of pixels) for the cipher to work.
Since OTP needs the key to be random, the keys that we’ll be using have been obtained from a Random Bitmap Generator.

## Running the script

The file images_xor.py is the Python script implementing the cipher, so it’s the one you need to use to encrypt and decrypt.
To run it, you need to first install the Pillow Python imaging library, which handles images.

