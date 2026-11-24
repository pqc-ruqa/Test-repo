# Security Policy

## Scope

This repository contains only a test bed for CBOM (Cryptography Bill of Materials) detection: sample source code, sample configuration files and test data. It is not connected to any production system, service or deployment. Nothing in this repository runs anywhere.

Reports about the intentionally weak or outdated cryptography in the sample code (for example RSA, 3DES, MD5, AES-CBC with a static IV, old dependency versions) are not vulnerabilities. These samples are the purpose of the repository.

## Test keys in `pki/`

All key files under `pki/` are intentionally fake test data. They are not usable keys and are not used by any system. Reporting them, or secret scanning findings for them, is not a vulnerability report.

## Reporting a vulnerability

Please report security issues only through GitHub private vulnerability reporting:

https://github.com/pqc-ruqa/Test-repo/security/advisories/new

Do not open public issues, pull requests or discussions for security issues.

Useful reports describe a real problem in this repository itself, for example a real secret committed by mistake, or a workflow or configuration that could be abused. Please include the affected file, the commit, and the steps to reproduce.

There is no bug bounty and no guaranteed response time.

---

Česky: Bezpečnostní problémy hlaste jen přes GitHub private vulnerability reporting (odkaz výše), ne přes veřejné issues. Klíče v `pki/` jsou záměrně falešná testovací data.
