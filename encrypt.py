import sys

def vigenere_cipher(text, key, encrypt=True):
    result = []
    key_length = len(key)
    key_shifts = [ord(k) - ord('A') for k in key]  # Convert key letters to shift values
    for i, char in enumerate(text):
        shift = key_shifts[i % key_length]
        if not encrypt:
            shift = -shift  # Reverse shift for decryption
        new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        result.append(new_char)
    return ''.join(result)

password = sys.stdin.readline().strip()
command = sys.stdin.readline().strip()
string = sys.stdin.readline().strip()

if command == 'encrypt':
    print(vigenere_cipher(string, password))
    sys.stdout.flush()
elif command == 'decrypt':
    print(vigenere_cipher(string, password, encrypt=False))
    sys.stdout.flush()



