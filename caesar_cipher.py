def caesar_cipher(text, shift):
    result = ""
    # Iterate through each character in the text
    for i in range(len(text)):
        # Get the character and its ASCII code
        char = text[i]
        ascii_code = ord(char)
        
        # Apply the shift to the ASCII code (keeping it within the range of A-Z or a-z)
        if char.isupper():
            shifted_code = (ascii_code - 65 + shift) % 26 + 65
        elif char.islower():
            shifted_code = (ascii_code - 97 + shift) % 26 + 97
        else:
            # If the character is not a letter, don't shift it
            shifted_code = ascii_code
        
        # Convert the shifted ASCII code back to a character and add it to the result
        result += chr(shifted_code)
    
    return result
