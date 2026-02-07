package com.bank.crypto;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import javax.crypto.spec.IvParameterSpec;

public class LegacyEncryption {

    // PQC-SCAN TARGET: Legacy 3DES (Triple DES) - Vulnerable
    public byte[] encrypt3DES(byte[] data, byte[] key) throws Exception {
        SecretKeySpec keySpec = new SecretKeySpec(key, "DESede");
        Cipher cipher = Cipher.getInstance("DESede/ECB/PKCS5Padding"); // ECB mode is weak
        cipher.init(Cipher.ENCRYPT_MODE, keySpec);
        return cipher.doFinal(data);
    }

    // PQC-SCAN TARGET: AES-CBC with static IV - Vulnerable to padding oracle
    public byte[] encryptAESCBC(byte[] data, byte[] key) throws Exception {
        SecretKeySpec keySpec = new SecretKeySpec(key, "AES");
        // STATIC IV usage - Critical vulnerability
        byte[] iv = new byte[16]; // Zero IV
        IvParameterSpec ivSpec = new IvParameterSpec(iv);
        
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, keySpec, ivSpec);
        return cipher.doFinal(data);
    }
}
