import oqs

class PQCSignatures:
    """
    PQC-SCAN TARGET: Advanced PQC Signatures
    Demonstrates usage of Falcon (minimal latency) and SPHINCS+ (stateless hash-based).
    """

    def sign_with_falcon(self, message):
        # Falcon-512: Good for latency-sensitive applications
        with oqs.Signature("Falcon-512") as signer:
            public_key = signer.generate_keypair()
            signature = signer.sign(message)
            return signature, public_key

    def sign_with_sphincs(self, message):
        # SPHINCS+-SHA2-128f-simple: Conservative, stateless, larger signatures
        with oqs.Signature("SPHINCS+-SHA2-128f-simple") as signer:
            public_key = signer.generate_keypair()
            signature = signer.sign(message)
            return signature, public_key

    def verify_signature(self, algorithm, message, signature, public_key):
        with oqs.Signature(algorithm) as verifier:
            return verifier.verify(message, signature, public_key)
