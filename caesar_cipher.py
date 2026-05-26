def caesar_encrypt(plaintext: str, shift: int) -> str:
    ciphertext = []
    for char in plaintext:
        if char.isupper():
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            ciphertext.append(shifted_char)
        elif char.islower():
            shifted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            ciphertext.append(shifted_char)
        else:
            ciphertext.append(char)
    return "".join(ciphertext)

def caesar_decrypt(ciphertext: str, shift: int) -> str:
    plaintext = []
    for char in ciphertext:
        if char.isupper():
            shifted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            plaintext.append(shifted_char)
        elif char.islower():
            shifted_char = chr((ord(char) - 97 - shift) % 26 + 97)
            plaintext.append(shifted_char)
        else:
            plaintext.append(char)
    return "".join(plaintext)

def main():
    print("=== DecodeLabs - Caesar Cipher Tool ===")
    
    text = input("Enter the message: ")
    while True:
        try:
            shift_value = int(input("Enter shift value (1-25): "))
            if 1 <= shift_value <= 25:
                break
            print("Please enter a number between 1 and 25.")
        except ValueError:
            print("Invalid input! Please enter an integer.")
            
    encrypted_text = caesar_encrypt(text, shift_value)
    decrypted_text = caesar_decrypt(encrypted_text, shift_value)
    
    print("\n--- Results ---")
    print(f"Original Text:  {text}")
    print(f"Encrypted Text: {encrypted_text}")
    print(f"Decrypted Text: {decrypted_text}")
    
if __name__ == "__main__":
    main()