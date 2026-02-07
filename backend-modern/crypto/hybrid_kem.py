import oqs
from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

class HybridKEM:
    """
    PQC-SCAN TARGET: Hybrid Key Exchange (X25519 + Kyber768)
    This class demonstrates a transition strategy where classical and quantum-resistant
    algorithms are combined.
    """

    def __init__(self):
        self.kem_alg = "Kyber768"
        self.kem = oqs.KeyEncapsulation(self.kem_alg)

    def generate_keypair(self):
        # 1. Classical Key Generation (X25519)
        classical_private = x25519.X25519PrivateKey.generate()
        classical_public = classical_private.public_key()
        
        # 2. Post-Quantum Key Generation (Kyber768)
        pqc_public_key = self.kem.generate_keypair()
        
        return {
            "classical": (classical_private, classical_public),
            "pqc": (self.kem.export_secret_key(), pqc_public_key)
        }

    def encapsulate(self, peer_classical_public, peer_pqc_public):
        # 1. Classical Shared Secret
        ephemeral_private = x25519.X25519PrivateKey.generate()
        classical_shared = ephemeral_private.exchange(peer_classical_public)
        
        # 2. PQC Shared Secret
        ciphertext, pqc_shared = self.kem.encap_secret(peer_pqc_public)
        
        # 3. Hybrid Combination (Concatenation + KDF)
        combined_secret = classical_shared + pqc_shared
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'hybrid-key-exchange'
        ).derive(combined_secret)
        
        return ciphertext, ephemeral_private.public_key(), derived_key
