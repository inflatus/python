#creating a sha256 hash from input
#need to expand on this to provide has choice 

import hashlib

input_hash = input('Select value to hash ')

encoded_hash = hashlib.sha256(input_hash.encode())

print (encoded_hash.hexdigest())

