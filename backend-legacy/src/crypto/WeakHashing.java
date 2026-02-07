package com.bank.crypto;

import java.security.MessageDigest;

public class WeakHashing {

    // PQC-SCAN TARGET: MD5 - Broken collision resistance
    public byte[] hashMD5(String input) throws Exception {
        MessageDigest md = MessageDigest.getInstance("MD5");
        return md.digest(input.getBytes());
    }

    // PQC-SCAN TARGET: SHA-1 - Deprecated
    public byte[] hashSHA1(String input) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-1");
        return md.digest(input.getBytes());
    }
}
