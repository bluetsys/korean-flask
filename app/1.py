import ecdsa
import hashlib
import base58

# These are the 3 private keys in base58check encoding.
privkey_b58_1 = "L5Mssn1ANiFXuWrYpSohHfbvZzuUNZ7Px8x4vCLCFthihhEVwowM"
privkey_b58_2 = "L3jg9jj7SBfoU5qiLunjuES1f6aoSjvQMYBXHqR4b7HBv92dnHsq"
privkey_b58_3 = "KwmT38RYZe55mM1TjY8dy41VpzerunJMoLt4Z97tF33rxHUsejLT"

# Remove the \x80 version prefix and x\01 compression suffix.
privkey_bin_1 = base58.b58decode_check(privkey_b58_1.encode())[1:-1]
privkey_bin_2 = base58.b58decode_check(privkey_b58_2.encode())[1:-1]
privkey_bin_3 = base58.b58decode_check(privkey_b58_3.encode())[1:-1]

# Create signing keys using the SECP256k1 curve in ECDSA.
sk_bin_1 = ecdsa.SigningKey.from_string(privkey_bin_1, ecdsa.SECP256k1)
sk_bin_2 = ecdsa.SigningKey.from_string(privkey_bin_2, ecdsa.SECP256k1)
sk_bin_3 = ecdsa.SigningKey.from_string(privkey_bin_3, ecdsa.SECP256k1)

# Derive verifying keys from the signing keys.
vk_bin_1 = sk_bin_1.verifying_key.to_string()
vk_bin_2 = sk_bin_2.verifying_key.to_string()
vk_bin_3 = sk_bin_3.verifying_key.to_string()

# Determine if the Y value is even. This is required for compression.
vk_iseven_1 = int(vk_bin_1.hex(), base=16) % 2 == 0
vk_iseven_2 = int(vk_bin_2.hex(), base=16) % 2 == 0
vk_iseven_3 = int(vk_bin_3.hex(), base=16) % 2 == 0

# Determine the prefix for the X value based on whether the Y value is even.
vk_prefix_1 = b"\x02" if vk_iseven_1 else b"\x03"
vk_prefix_2 = b"\x02" if vk_iseven_2 else b"\x03"
vk_prefix_3 = b"\x02" if vk_iseven_3 else b"\x03"

# Extract the X value from the verifying key. X is the first 32 bytes.
vk_xval_1 = vk_bin_1[:32]
vk_xval_2 = vk_bin_2[:32]
vk_xval_3 = vk_bin_3[:32]

# Get the SHA256 hash of the X value with the even/odd prefix.
vk_sha256_1 = hashlib.sha256(vk_prefix_1 + vk_xval_1).digest()
vk_sha256_2 = hashlib.sha256(vk_prefix_2 + vk_xval_2).digest()
vk_sha256_3 = hashlib.sha256(vk_prefix_3 + vk_xval_3).digest()

# Get the RIPEMD-160 hash of the SHA256 hash, then add the address prefix.
ripemd160_1 = hashlib.new("ripemd160")
ripemd160_1.update(vk_sha256_1)
address_1 = b"\x00" + ripemd160_1.digest()

ripemd160_2 = hashlib.new("ripemd160")
ripemd160_2.update(vk_sha256_2)
address_2 = b"\x00" + ripemd160_2.digest()

ripemd160_3 = hashlib.new("ripemd160")
ripemd160_3.update(vk_sha256_3)
address_3 = b"\x00" + ripemd160_3.digest()

# Get the base58check encoding for each address.
address_b58_1 = base58.b58encode_check(address_1)
address_b58_2 = base58.b58encode_check(address_2)
address_b58_3 = base58.b58encode_check(address_3)

# Show the addresses.
for x in [address_b58_1, address_b58_2, address_b58_3]:
    print(x.decode())

# 1FbFJHvT3xE2i5TDqtyCUuCiAjVJMV9XPt
# 1PSds68vNzCeYvJNB6axnN8VnrLSnJC6S1
# 1GPqjz4qQxz7ZWnvSN5Gc2H5hkhd5va95i