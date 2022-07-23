# Jocelyn Strmec
# CPTS 427 Project

# imports
from math import fabs
import os
import cv2

from datetime import datetime
from encryption_algs import encryption_alg2 as encrypt1
from encryption_algs import encryption_alg3 as encrypt2
from encryption_algs import encryption_alg4 as encrypt3

images_dict ={0:'unencrypted_files/clouds.webp', 1:'unencrypted_files/mountains.jpeg',2:'unencrypted_files/poppy_field.webp',3:'unencrypted_files/sunset.jpeg',4:'unencrypted_files/walk_central_park.webp'}
text_dict ={0:'text_file', 1:'text_file1',2:'text_file2',3:'text_file3',4:'text_file4'}
auto_secret_msg = "It's sandwich day. Every Thursday I give Pudge the Fish a peanut butter sandwich. But, today we were out of peanut butter. I asked my sister what to give him and she said a tuna sandwich. I can’t give Pudge tuna! Do you know what tuna is? It's a fish!"


def main():
    print("\n\nWould you like to encode your message in an ( a ) image or ( b ) a text file? \nSelect an option by inputting corresponding letter")
    message_type = input()
    print('Input a single integer between 0-4.')
    file_num = input()
    print("Type in your secret message to encrypt: ")
    secret = input()

    # Gets file name from dictionary using user input and parses it to variables for later use 
    output_file = images_dict[int(file_num.strip())]
    filename, ext = output_file.split(".")
    _, file= filename.split("/")

    if(message_type.lower() == "a"):
        # if else switches which algo is used based on current minute's eveness
        if(datetime.now().minute%2 == 0 and 1!=1.0):
            # encodes image
            encoded_image = encrypt2.encode(output_file, secret)
            # saves image
            cv2.imwrite(f"encrypted_files/{file}_encoded.{ext}", encoded_image)
            
            print("Would you like to decode the data?  y or n")
            affirmative = input()
            if affirmative.lower().strip() == 'y':
                # decodes image
                decoded_data = encrypt2.decode(f"encrypted_files/{file}_encoded.{ext}")   
                # prints message
                print("Secret message is:", decoded_data)
        else:
            # encodes image
            encoded_image = encrypt1.encode(output_file, secret)
            # saves image
            cv2.imwrite(f"encrypted_files/{file}_encoded.{ext}", encoded_image)

            print("Would you like to decode the data?  y or n")
            affirmative = input()
            if affirmative.lower().strip() == 'y':
                # decodes images
                decoded_data = encrypt1.decode(f"encrypted_files/{file}_encoded.{ext}")
                # prints message
                print("Secret message is:", decoded_data)
    else:
        file = text_dict[int(file_num.strip())]
        # encodes image
        encrypt3.encode(file, secret)

        print("Would you like to decode the data?  y or n")
        affirmative = input()
        if affirmative.lower().strip() == 'y':
            # decodes images
            decoded_data = encrypt3.decode(file)
            # prints message
            print("Secret message is:", decoded_data)

    print("Goodbye!")

main()   
    

# python encryption_algs/encryption_alg3.py -e mountains.jpeg -f data.csv -b 1
# python encryption_algs/encryption_alg3.py -e image.PNG -f data.csv -b 2
# python encryption_algs/encryption_alg3.py -d encrypted_files/mountains_encoded.jpeg -f data_decoded.csv -b 1