# PQC-SCAN Test Bed Repository

This repository serves as a **Reference Test Bed** for validating the detection capabilities of the `pqc-scan` tool. It simulates a complex enterprise application containing a mix of legacy, modern, and Post-Quantum Cryptography (PQC) artifacts.

The goal is to test the scanner's ability to generate an accurate **CBOM (Cryptography Bill of Materials)** by identifying:
1.  **Vulnerable Legacy Algorithms** (e.g., RSA, 3DES, MD5)
2.  **Modern Standard Algorithms** (e.g., AES-GCM, ECC)
3.  **Post-Quantum Algorithms** (e.g., CRYSTALS-Kyber, Dilithium, Falcon, SPHINCS+)

## 🏗️ Repository Structure

```text
.
├── backend-legacy/         # Legacy Java application (Vulnerable)
│   └── src/
│       ├── auth/           # RSA Signing
│       └── crypto/         # 3DES, AES-CBC, MD5, SHA-1
├── backend-modern/         # Modern Python services (PQC & Hybrid)
│   ├── auth-service/       # Kyber & Dilithium (liboqs)
│   └── crypto/             # Hybrid KEM (X25519+Kyber), Falcon, SPHINCS+
├── frontend-app/           # JavaScript Frontend
│   └── src/services/       # RSA-OAEP & Simulated Kyber
├── infrastructure/         # Configuration files
│   └── nginx/              # SSL/TLS Config (Legacy & Hypothetical PQC suites)
└── pki/                    # Public Key Infrastructure Artifacts
    ├── RSA_keys/           # Traditional RSA keys
    ├── PQC_keys/           # Dilithium keys, Kyber public keys
    └── hybrid_certs/       # Experimental Hybrid Certificates
```

## 🧪 Ground Truth (Expected Results)

Use this table to verify the accuracy of the generated CBOM.

| File Path | Component / Function | Algorithm | Classification | Expected Status |
| :--- | :--- | :--- | :--- | :--- |
| **Backend Legacy** | | | | |
| `backend-legacy/src/auth/RSASigner.java` | `generateLegacyKey` | **RSA-2048** | Legacy | 🔴 **Vulnerable** (Shor's Algo) |
| `backend-legacy/src/crypto/LegacyEncryption.java` | `encrypt3DES` | **3DES (Triple DES)** | Legacy | 🔴 **Vulnerable** (Sweet32) |
| `backend-legacy/src/crypto/LegacyEncryption.java` | `encryptAESCBC` | **AES-CBC (Static IV)** | Modern (Misused) | 🟠 **Weakness** (Padding Oracle) |
| `backend-legacy/src/crypto/WeakHashing.java` | `hashMD5` | **MD5** | Legacy | 🔴 **Broken** (Collisions) |
| **Backend Modern** | | | | |
| `backend-modern/auth-service/quantum_auth.py` | `generate_kyber_keypair` | **CRYSTALS-Kyber** | PQC | 🟢 **Quantum-Safe** |
| `backend-modern/auth-service/quantum_auth.py` | `sign_dilithium` | **CRYSTALS-Dilithium** | PQC | 🟢 **Quantum-Safe** |
| `backend-modern/crypto/hybrid_kem.py` | `HybridKEM` | **X25519 + Kyber768** | Hybrid | 🟢 **Quantum-Safe** (Transition) |
| `backend-modern/crypto/pqc_signatures.py` | `sign_with_falcon` | **Falcon-512** | PQC | 🟢 **Quantum-Safe** |
| `backend-modern/crypto/pqc_signatures.py` | `sign_with_sphincs` | **SPHINCS+** | PQC | 🟢 **Quantum-Safe** |
| `backend-modern/crypto/modern_symmetric.py` | `encrypt_aes_gcm` | **AES-256-GCM** | Modern | 🟢 **Secure** (Pre-PQC Standard) |
| **Frontend** | | | | |
| `frontend-app/src/services/CryptoService.js` | `encryptLegacy` | **RSA-OAEP** | Legacy | 🔴 **Vulnerable** |
| `frontend-app/src/services/CryptoService.js` | `encapsulateKyber` | **Kyber-512 (Sim)** | PQC | 🟡 **Simulation/Mock** |
| **Infrastructure & PKI** | | | | |
| `infrastructure/nginx/nginx.conf` | `ssl_ciphers` | **ECDHE-RSA-...** | Legacy | 🔴 **Vulnerable** |
| `pki/PQC_keys/dilithium2_private.pem` | Key File | **Dilithium2** | PQC | 🟢 **Quantum-Safe** |
| `pki/PQC_keys/kyber768_public.bin` | Key File | **Kyber-768** | PQC | 🟢 **Quantum-Safe** |
| **Dependency Manifests (SCA)** | | | | |
| `backend-legacy/pom.xml` | Dependency | **Bouncy Castle 1.60** | Legacy | 🔴 **Vulnerable** (CVEs) |
| `backend-modern/requirements.txt` | Dependency | **liboqs-python** | PQC | 🟢 **Quantum-Safe** (Lib) |
| `frontend-app/package.json` | Dependency | **node-forge 0.10.0** | Legacy | 🔴 **Vulnerable** |

## 🛠️ Build & Setup (Simulation)

Since this is a heterogeneous test bed, you can simulate building the individual components:

**Backend Legacy (Java)**
```bash
cd backend-legacy
mvn clean install  # Simulates building the vulnerable Java app
```

**Backend Modern (Python)**
```bash
cd backend-modern
pip install -r requirements.txt # Installs PQC libraries
```

**Frontend (Node.js)**
```bash
cd frontend-app
npm install # Installs legacy crypto libraries
```

## 🚀 How to Use with PQC-Scan

1.  **Clone this repository** to your local environment.
2.  **Run `pqc-scan`** against the root directory:
    ```bash
    pqc-scan analyze --input ./ --output cbom.json
    ```
3.  **Compare `cbom.json`** against the **Ground Truth** table above.
4.  **Verify Detection**: Ensure all "Red" items are flagged as violations or warnings, and "Green" items are correctly identified as PQC.

## ⚠️ Disclaimer

This code is for **testing purposes only**. The cryptographic implementations (especially the PQC mocks) are **NOT secure** for production use. They are designed solely to trigger static analysis signatures.
