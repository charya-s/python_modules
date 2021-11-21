import torch
import numpy as np

alphabets = {
    "eng" : "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?.,'@#$%^&*()_-+=~`\/<>\":;[{}] ",
    "sin" : "සිංහල"
}

def create_dict(language):
    c2i_dict = {}
    i2c_dict = {}
    alphabet = alphabets[language]

    for i, c in enumerate(alphabet):
        c2i_dict[c] = i
        i2c_dict[i] = c
    
    return c2i_dict, i2c_dict
        

def encode_str(str, char_dict):
    encoded = []

    for c in str:
        oh_vector = np.zeros(len(char_dict))
        oh_vector[char_dict[c]] = 1
        encoded.append(oh_vector)

    encoded = np.array(encoded)
    encoded = torch.Tensor(encoded)
    return encoded


def decode_str(str_tensor, int_dict):
    decoded = ""

    for c in str_tensor:
        char = np.array(c)
        oh_index = 0
        for i in char:
            if i == 1:
                break
            oh_index += 1
        
        decoded = decoded + int_dict[oh_index]

    return decoded    

