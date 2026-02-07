from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

class ModernSymmetric:
    """
    PQC-SCAN TARGET: Modern Standard Symmetric Encryption
    This represents the 'Good' baseline that is NOT PQC but is currently secure.
    """

    def encrypt_aes_gcm(self, data, key):
        # AES-GCM is the current standard for authenticated encryption
        # It is generally considered quantum-safe (Grover's algorithm only halves key space)
        # providing keys are 256-bit.
        
        iv = os.urandom(12) # 96-bit nonce
        encryptor = Cipher(
            algorithms.AES(key),
            modes.GCM(iv),
        ).encryptor()

        ciphertext = encryptor.update(data) + encryptor.finalize()
        
        return {
            "ciphertext": ciphertext,
            "iv": iv,
            "tag": encryptor.tag
        }

    def decrypt_aes_gcm(self, ciphertext, key, iv, tag):
        decryptor = Cipher(
            algorithms.AES(key),
            modes.GCM(iv, tag),
        ).decryptor()

        return decryptor.update(ciphertext) + decryptor.finalize()
