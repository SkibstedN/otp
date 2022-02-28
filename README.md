# otp

We’ll be using a Python implementation of the [One-Time-Pad (OTP)](https://en.wikipedia.org/wiki/One-time_pad) cipher for encrypting/decrypting images. Thus, the plaintext, the ciphertext and the key are all images (they will be called plain-image, cipher-image and just key, respectively), which need to be of the same size (in number of pixels) for the cipher to work.
Since OTP needs the key to be random, the keys that we’ll be using have been obtained from a [Random Bitmap Generator](https://www.random.org/bitmaps).

## Running the script

The file *images_xor.py* is the Python script implementing the cipher, so it’s the one you need to use to encrypt and decrypt.
To run it, you need to first install the [Pillow](https://pillow.readthedocs.io/en/stable/index.html) Python imaging library, which handles images.

The images_xor.py script can be run as follows

  python3 images_xor.py -p <plain> -k <key> -c <result>

where 
  
  <plain>	is the name of the file containing the plain-image if we’re encrypting (or the cipher-image, if we’re decrypting)
  <key>		is the name of the file containing the key to encrypt/decrypt
  <result> 	is the name of the file where the resulting XORed image will be stored

    
Both <plain> and <key> need to be B/W bitmap images of the same size (in number of pixels). You’re encouraged to have a look at the source code and try to understand how it works. You can play and get familiar with the program by encrypting and decrypting images of your own, just remember that the key needs to be of the same size as the image you want to encrypt, and that the same key needs to be used for encryption and decryption (recall OTP is symmetric encryption). The folder *example* also provides some images to play with.





