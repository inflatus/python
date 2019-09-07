#creating a sha256 hash from input
#need to expand on this to provide hash choice

import hashlib

input_hash = input('Select value to hash ')

encoded_sha1 = hashlib.sha1(input_hash.encode())
encoded_sha224 = hashlib.sha224(input_hash.encode())
encoded_sha256 = hashlib.sha256(input_hash.encode())
encoded_sha384 = hashlib.sha384(input_hash.encode())
encoded_sha512 = hashlib.sha512(input_hash.encode())

print ('sha1 ',encoded_sha1.hexdigest())
print ('sha224 ',encoded_sha224.hexdigest())
print ('sha256 ',encoded_sha256.hexdigest())
print ('sha384 ',encoded_sha384.hexdigest())
print ('sha512 ',encoded_sha512.hexdigest())
