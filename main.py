# %%
import os
import hashlib
import base58
from ecdsa import SigningKey, SECP256k1
import bech32

# %%
# 1. Generate a 256-bit private key
private_key_bytes = os.urandom(32)

private_key_int = int.from_bytes(private_key_bytes) # Convert to decimal number
print("Private Key (decimal):", private_key_int)

private_key_hex = private_key_bytes.hex()
print("Private Key (hex):", private_key_hex)

wif = base58.b58encode(b'\x80' + private_key_bytes + b'\x01' + hashlib.sha256(hashlib.sha256(b'\x80' + private_key_bytes + b'\x01').digest()).digest()[:4]).decode()
print("Private Key (WIF):", wif) # used for wallet import format

# %%
# 2. Generate public key using secp256k1
sk = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
vk = sk.verifying_key

# Format uncompressed public key (0x04 + X + Y)
public_key_bytes = b'\x04' + vk.to_string()
public_key_int = int.from_bytes(public_key_bytes)
print("Public Key (decimal):", public_key_int)
public_key_hex = public_key_bytes.hex()
print("Public Key (hex):", public_key_hex)

# %%
# 3. Create Bitcoin address (Legacy)
# Step 1: SHA-256 hash of the public key
sha256_hash = hashlib.sha256(public_key_bytes).digest()

# Step 2: RIPEMD-160 hash of the SHA-256 hash
ripemd160 = hashlib.new('ripemd160')
ripemd160.update(sha256_hash)
hashed_pubkey = ripemd160.digest()

# Step 3: Add version byte (0x00 for mainnet)
versioned_payload = b'\x00' + hashed_pubkey

# Step 4: Create checksum (double SHA-256)
checksum = hashlib.sha256(hashlib.sha256(versioned_payload).digest()).digest()[:4]

# Step 5: Combine and encode with Base58Check
full_payload = versioned_payload + checksum
address = base58.b58encode(full_payload).decode()

print("Bitcoin Address (Legacy):", address)

# %%
# BITCOIN ADDRESS GENERATION

# 1. Compress the public key (required for SegWit)
pubkey_bytes = vk.to_string()
x = pubkey_bytes[:32]
y = pubkey_bytes[32:]
prefix = b'\x03' if int.from_bytes(y, 'big') % 2 else b'\x02'
compressed_pubkey = prefix + x
print("Compressed Public Key (hex):", compressed_pubkey.hex())

# 2. Hash of the compressed public key (SHA-256 then RIPEMD-160)
sha256 = hashlib.sha256(compressed_pubkey).digest()
ripemd160 = hashlib.new('ripemd160', sha256).digest()

# 3. Create Bitcoin address (P2WPKH - witness version 0)
witness_version = 0
witness_program = bech32.convertbits(ripemd160, 8, 5, True)
segwit_address = bech32.bech32_encode("bc", [witness_version] + witness_program)

print("Bitcoin Address (SegWit ver):", segwit_address)

# %%



