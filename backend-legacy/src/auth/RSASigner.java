package com.bank.auth;

import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.Signature;

public class RSASigner {
    // PQC-SCAN TARGET: Klasické RSA je zranitelné Shorůvým algoritmem
    public KeyPair generateLegacyKey() throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
        kpg.initialize(2048); // Weak key size for quantum era
        return kpg.generateKeyPair();
    }

    public byte[] signData(byte[] data, KeyPair pair) throws Exception {
        Signature sign = Signature.getInstance("SHA256withRSA");
        sign.initSign(pair.getPrivate());
        sign.update(data);
        return sign.sign();
    }
}