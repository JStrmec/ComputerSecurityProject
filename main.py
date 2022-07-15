# Jocelyn Strmec
# CPTS 427 Project

# imports
import os
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

def initialfile_to_outputfile(initial_file):
    # sets file path for files
    path = "ComputerSecurityProject/unencrypted_files/"
    # split the filename and the image extension
    filename, ext = initial_file.split(".")
    output_image = os.path.join(path, f"{filename}_encoded.{ext}")
    return output_image

def main():
    print('Chose a file type to encrypt by inputting the corresponding letter: \n\ta)  image\n\tb)  text file\n')
    fileType = input()
    file_type = fileType.lower().strip()
    print('Input a single integer between 0-4.\n')
    file_num = input()
    print("Type in your secret message to encrypt: ")
    secret = input()
    
    if file_type =='a':
        output_file = initialfile_to_outputfile(images_dict[int(file_num.strip())])
        encoded_image = encrypt2.encode(output_file, secret)
        print("Would you like to decode the data?  y or n")
        affirmative = input()
        if affirmative.lower().strip() == 'y':
            decoded_data = encrypt2.decode(encoded_image)
            print("Secret message is:", decoded_data)
        else:
            print("Goodbye!")
    print(decoded_data)
    if file_type =='b':
        #output_file = initialfile_to_outputfile(files_dict[int(file_num.strip())])
        print("Goodbye.")
    
    

# python encryption_algs/encryption_alg3.py -e mountains.jpeg -f data.csv -b 1
# python encryption_algs/encryption_alg3.py -e image.PNG -f data.csv -b 2
# python steganography_advanced.py -d image_encoded.PNG -f data_decoded.csv -b 3