#creating a sha256 hash from input
<<<<<<< HEAD
#need to expand on this to provide hash choice 
=======
#need to expand on this to provide has choice 
>>>>>>> cfc642f0e84860f835cffac04b2b32c2b8286c38

import hashlib

input_hash = input('Select value to hash ')

encoded_hash = hashlib.sha256(input_hash.encode())

print (encoded_hash.hexdigest())

