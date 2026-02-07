import oqs # Open Quantum Safe library

def generate_kyber_keypair():
    # PQC-SCAN TARGET: CRYSTALS-Kyber je PQC standard
    kem = oqs.KeyEncapsulation("Kyber512") 
    public_key = kem.generate_keypair()
    secret_key = kem.export_secret_key()
    return public_key, secret_key

def sign_dilithium(message):
    # PQC-SCAN TARGET: CRYSTALS-Dilithium pro podpisy
    sig = oqs.Signature("Dilithium2")
    public_key = sig.generate_keypair()
    signature = sig.sign(message)
    return signature