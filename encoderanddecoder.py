# ENCODER AND DECODER.
# What this does is encodes and decodes messages/texts i.e creates secret messages or reveals secret texts
# Im pretty sure this code should be pretty easy to understand but I understand some people are beginners and even if you're good at programming this might seem a little hard to understand so do not worry. I have commented out complex things.

'''
Key Concepts:

Input/Output: The code prompts the user to choose between encoding or decoding, and then to enter the message.
Data Types: It uses the int data type for user input and the bytearray data type for message manipulation.
Conditional Statements: The if-else statements determine the encoding or decoding process based on the user's choice.
String Manipulation: The code uses string slicing and reversal to modify the message.


Encoding/Decoding Logic:

If the user chooses to encode, the code:
Reverses the first and last characters of the message if it's longer than 3 characters.
Otherwise, it simply reverses the entire message.
If the user chooses to decode, the code:
Reverses the first and last characters of the message if it's longer than 3 characters.
Otherwise, it simply reverses the entire message.
Note: This is a very basic encryption method and should not be used for sensitive data. For more secure encryption, consider using cryptographic libraries like pycryptodome.
'''

a = int(input("Do you want to encode or decode a message (1 for encode/2 for decode): ")) # typecasting for all the beginners out there, used int so that code doesnt throw an error whenever the user types a number.

if a == 1: # if the choice is 1 i.e choice for encode
    encode_input = input("Enter the message that you want to encode: ")
    byte_encoderarray = bytearray(encode_input, "utf-8") # bytearray is an in-built python function which makes it easier to string slice, choose the encoding utf-8 and in the place of encode_input u can write the string that u wanna slice
    if len(encode_input) >= 3:
        byte_encoderarray[0], byte_encoderarray[-1] = byte_encoderarray[-1], byte_encoderarray[0] #-1 = last character, [0] = first, so these characters will replace each other
        encoded_message = byte_encoderarray.decode() # once we use the .decode it slices the strings to the lengths that we provided above in the 11th line
        print(f"Your encoded message is: {encoded_message}") 
    else:
        encode_input = encode_input[::-1] # reverse the word, ::-1 reverses the whole world 
        print(f"Your decoded message is {encode_input}")
elif a == 2:
    decode_input = input("Enter the message that you want to decode: ")
    byte_decoderarray = bytearray(decode_input, "utf-8") # again the message that you wanna string slice and ofc encoding utf-8 or whatever if ur advanced
    if len(decode_input) >= 3:
        byte_decoderarray[-1], byte_decoderarray[0] = byte_decoderarray[0], byte_decoderarray[-1] # now the last character
        decoded_message = byte_decoderarray.decode()
        print(f"Your decoded message is {decoded_message} ")
    else:
        decode_input = decode_input[::-1]
        print(f"Your decoded message is {decode_input}")

# Project creation date: 4/10/2024
