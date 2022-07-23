def to_bin(data):
    """Convert `data` to binary format as string"""
    if isinstance(data, str):
        return ''.join([ format(ord(i), "08b") for i in data ])
    elif isinstance(data, bytes) or isinstance(data, np.ndarray):
        return [ format(i, "08b") for i in data ]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError("Type not supported.")

def encode(file_name, secret_data):
    secret_data += "====="
    # convert data to binary
    binary_secret_data = to_bin(secret_data)  
    # size of data to hide
    data_len = len(binary_secret_data)
        
    file1 = open(f"unencrypted_files/{file_name}.txt","r") 
    file2 = open(f"encrypted_files/{file_name}_encoded.txt","w+") 
    
    data_index = 0
    while True:     
        data = file1.readline()
        if(data_index<data_len-1):
            if(binary_secret_data[data_index]=='1'):  # replace the 'bit'
                data=data[0].lower() + data[1:]  # convert first letter to lowercase
        file2.write(data)
        data_index+=1
        if not data:
            break
    
def decode(file_name):
    crypto =''
    file2 = open(f"encrypted_files/{file_name}_encoded.txt","r") 
    while True:
        data = file2.readline()
        if not data:
            break
        # decodes lower and upper case letters of each line to secret message
        if(data[0].isupper()):
            crypto+='0'
        else:
            crypto+='1'
    # len of binary result 
    data_lencr = len(crypto)  
    #secret = ""
    all_bytes = [crypto[i: i+8] for i in range(0, data_lencr, 8) ]
    # convert from bits to characters
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "=====":
            break
    return decoded_data[:-5]