# Jocelyn Strmec
# CPTS 427 Project

# document paths
imagepath ="/unencrypted_files/image"
textdocpath ="/unencrypted_files/textdoc"
audiopath ="/unencrypted_files/audio"
videopath ="/unencrypted_files/video"
error =""

def checkByCase(letter):
    match letter:
        case 'a':
            return imagepath
        case 'b':
            return textdocpath
        case 'c':
            return audiopath
        case 'd':
            return videopath
        case 'e':
            return error



def main():
    print('Chose a file type to encrypt by letter: \n\ta) image\n\tb) text file\n\tc) audio file\n\td) video file')
    fileType = input()
    checkByCase(fileType.lower().strip())