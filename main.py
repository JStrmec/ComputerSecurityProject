# Jocelyn Strmec
# CPTS 427 Project

# imports
import numpy as np

# document paths
imagepath ="/unencrypted_files/image"
textdocpath ="/unencrypted_files/textdoc"
audiopath ="/unencrypted_files/audio"
videopath ="/unencrypted_files/video"
error =""

def check_by_case(letter):
    match letter:
        case 'a':
            return imagepath
        case 'b':
            return textdocpath
        case 'c':
            return audiopath
        case 'd':
            return videopath
    return error

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
    print('Chose a file type to encrypt by letter: \n\ta) image\n\tb) text file\n\tc) audio file\n\td) video file')
    fileType = input()
    unenecrypted_filepath = check_by_case(fileType.lower().strip())
    print("?")
    information_to_encrypt = input()
