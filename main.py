# Jocelyn Strmec
# CPTS 427 Project

# imports
import numpy as np
from encryption_algs import encryption_alg2 as encrypt1
from encryption_algs import encryption_alg3 as encrypt2


images_dict ={0:'clouds.webp', 1:'mountains.jpeg',2:'poppy_field.webp',3:'sunset.jpeg',4:'walk_central_park.webp'}
files_dict ={0:'clouds.webp', 1:'mountains.jpeg',2:'poppy_field.webp',3:'sunset.jpeg',4:'walk_central_park.webp'}

def to_binary(data):
    """Convert `data` to binary format as string"""
    if isinstance(data, str):
        return ''.join([ format(ord(i), "08b") for i in data ])
    elif isinstance(data, bytes):
        return ''.join([ format(i, "08b") for i in data ])
    elif isinstance(data, np.ndarray):
        return [ format(i, "08b") for i in data ]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError("Type not supported.")

def main():
    print('Chose a file type to encrypt by inputting the corresponding letter: \n\ta)  image\n\tb)  text file\n')
    fileType = input()
    file_type = fileType.lower().strip()
    print('Input a single integer between 0-4.\n')
    file_num = input()
    print("Type in your secret message to encrypt: ")
    secret = input()

    if file_type =='a':
    encoded_image = encrypt2.encode(file_path, information_to_encrypt)
    decoded_data = encrypt2.decode(encoded_image)
    print(decoded_data)
    if file_type =='b':

    
    

# python encryption_algs/encryption_alg3.py -e mountains.jpeg -f data.csv -b 1
# python encryption_algs/encryption_alg3.py -e image.PNG -f data.csv -b 2
# python steganography_advanced.py -d image_encoded.PNG -f data_decoded.csv -b 3