"""Deployment code that loads the certs for live-endpoint context."""
import ssl

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain("certs/07_chain_fullchain.pem", "keys/10_leaf_private.pem")
ctx.minimum_version = ssl.TLSVersion.TLSv1_2
