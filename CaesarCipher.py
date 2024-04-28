def encript_message():
    inputed_message = input("Message: ")
    #transform the message into ASCII 
    numbered_message = []
    for char in inputed_message:
        if char.isalpha():
            if char.islower():
                numbered_message.append(str(ord(char)))    
            elif char.isupper():
                numbered_message.append(str(ord(char)))
        else:
            numbered_message.append(char)  
    integer_list = [int(num) for num in numbered_message if num.isdigit()]

    # encrypt numbers into message in cipher form
    cipher_text = ""
    for num in numbered_message:
        if num.isdigit():
            if int(num) <= 70:
                cipher_text += chr(int(num) + 20) 
            elif 97 <= int(num) <= 102:
                cipher_text += chr(int(num) + 20) 
            elif int(num) > 70:
                cipher_text += chr(int(num) - 6)
        else:
            cipher_text += " "
    print(f"   Code: {cipher_text}")


def decript_message():
    inputed_code = input("   Code: ")
    #transform the message into ASCII 
    numbered_code = []
    for char in inputed_code:
        if char.isalpha():
            if char.islower():
                numbered_code.append(str(ord(char)))
            elif char.isupper():
                numbered_code.append(str(ord(char)))
        else: 
            numbered_code.append(char) 
    integer_list = [int(num) for num in numbered_code if num.isdigit()]

    #decrypt numbers into message in normal form
    normal_text = ""
    for num in numbered_code:
        if num.isdigit():
            if int(num) > 116:
                normal_text += chr(int(num) - 20) 
            elif 85 <= int(num) <= 90:
                normal_text += chr(int(num) - 20) 
            elif int(num) <= 116:
                normal_text += chr(int(num) + 6)
        else:
            normal_text += " "
    print(f"Message: {normal_text}")

encript_message()
print()

decript_message()