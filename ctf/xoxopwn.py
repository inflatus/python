# the nc brings up an evaluator
# finding out that it is a python evaluator
# uses the globals() builtin
# found a file within
# file was too long to open used __file__
# a^key=secret
# key = pythonwillhelpyouopenthedoor
# secret = 392a3d3c2b3a22125d58595733031c0c070a043a071a37081d300b1d1f0b09
# a^b=c is also a=b^c

secret = '392a3d3c2b3a22125d58595733031c0c070a043a071a37081d300b1d1f0b09'
secret = secret.decode('hex')
key = 'pythonwillhelpyouopenthedoor'
ret = ''
for i in xrange(len(secret)):
    ret += chr(ord(secret[i]) ^ ord(key[i % len(key)]))
print
ret
