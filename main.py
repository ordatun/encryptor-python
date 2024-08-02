from cryptography.fernet import Fernet
import string

class EncryptionEngine:
    def __init__(self, key=None):
        self.key = key or Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def encrypt_string(self, plain_text):
        if isinstance(plain_text, str):
            plain_text = plain_text.encode()
        encrypted_text = self.fernet.encrypt(plain_text)
        return encrypted_text

    def decrypt_string(self, encrypted_text):
        if isinstance(encrypted_text, str):
            encrypted_text = encrypted_text.encode()
        decrypted_text = self.fernet.decrypt(encrypted_text)
        return decrypted_text.decode()

    def caesar_encrypt(self, text, shift):
        shift = shift % 26
        alphabet = string.ascii_lowercase
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        table = str.maketrans(alphabet, shifted_alphabet)
        encrypted_text = text.translate(table)
        return encrypted_text

    def caesar_decrypt(self, text, shift):
        return self.caesar_encrypt(text, -shift)

    def encrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            file_data = file.read()
        encrypted_data = self.fernet.encrypt(file_data)
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)

    def decrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = self.fernet.decrypt(encrypted_data)
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)

if __name__ == "__main__":
    engine = EncryptionEngine()

    original_text = "Hello, World!"
    encrypted_text = engine.encrypt_string(original_text)
    decrypted_text = engine.decrypt_string(encrypted_text)

    print(f"Original: {original_text}")
    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")

    caesar_encrypted = engine.caesar_encrypt("hello", 3)
    caesar_decrypted = engine.caesar_decrypt(caesar_encrypted, 3)

    print(f"Caesar Encrypted: {caesar_encrypted}")
    print(f"Caesar Decrypted: {caesar_decrypted}")

    test_file_path = "test.txt"
    
    with open(test_file_path, "w") as f:
        f.write("This is a test file for encryption.")

    engine.encrypt_file(test_file_path)
    print(f"File {test_file_path} encrypted.")

    engine.decrypt_file(test_file_path)
    print(f"File {test_file_path} decrypted.")
