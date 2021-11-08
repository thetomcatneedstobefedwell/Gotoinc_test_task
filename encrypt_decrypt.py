def encrypt(text, n):
    if text:
        i = 0
        while i < n:
            
            start_string = ''
            end_string = ''
            list_of_char = split(text)
            
            for index, val in enumerate(list_of_char):
                if index % 2 == 0:
                    end_string += val
                else:
                    start_string += val
            
            text = start_string + end_string
            i += 1
    return text
    
def split(text):
    char_list = []
    for char in text:
        char_list.append(char)
    return char_list
        
result = encrypt(None, 2)
# print(result)



def decrypt(encrypted_text, n):
    if encrypted_text:
        i = 0
        while i < n:
            length = len(encrypted_text)
            list_of_char = split(encrypted_text)
            end_list = []
            
            j = 0
            while j < int(length/2):
                end_list.append(list_of_char[int(length/2) + j])
                end_list.append(list_of_char[j])
                j += 1
            encrypted_text = ''.join(end_list)
            i += 1
    return encrypted_text
    
result = decrypt(None, 2)
print(result)
