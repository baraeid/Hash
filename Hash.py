import hashlib

H = hashlib.md5(b"bara") . hexdigest()
print(H)
print("Size MD5 = " , len(H))


H = hashlib.md5(b"Bara") . hexdigest()
print(H)
print("Size MD5 = " , len(H))


H = hashlib.md5(b"bara bassam fathi eid") . hexdigest()
print(H)
print("Size MD5 = " , len(H))



H = hashlib.sha1(b"bara") . hexdigest()
print(H)
print("Size sha1 = " , len(H))


H = hashlib.sha1(b"Bara") . hexdigest()
print(H)
print("Size sha1 = " , len(H))


H = hashlib.sha1(b"bara bassam fathi eid") . hexdigest()
print(H)
print("Size sha1 = " , len(H))


H = hashlib.sha224(b"bara") . hexdigest()
print(H)
print("Size sha224 = " , len(H))


H = hashlib.sha256(b"bara") . hexdigest()
print(H)
print("Size sha256 = " , len(H))


H = hashlib.sha384(b"bara") . hexdigest()
print(H)
print("Size sha384 = " , len(H))


H = hashlib.sha512(b"bara") . hexdigest()
print(H)
print("Size sha512 = " , len(H))

