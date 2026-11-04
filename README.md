# qx-cert-lab
Certificate artifacts for Qryptive certificate-module testing.
Formats: PEM, DER, PKCS#7 (.p7b), PKCS#12 (.p12), JKS. Edges: weak keys, SHA-1/MD5 signatures,
expired / not-yet-valid / 7-day / 100-year, wildcard, multi-SAN, chain, code-signing/client/S-MIME EKU,
cert+key in one file, rotation pair. Push these to Qryptive AND to AWS ACM to compare inventories.
ALL TEST ONLY.
