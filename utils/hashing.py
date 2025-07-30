import hashlib
import zlib

def hash_text(text):
    hashes = {}
    try:
        hashes['md5'] = hashlib.md5(text.encode()).hexdigest()
        hashes['sha1'] = hashlib.sha1(text.encode()).hexdigest()
        hashes['sha256'] = hashlib.sha256(text.encode()).hexdigest()
        hashes['sha384'] = hashlib.sha384(text.encode()).hexdigest()
        hashes['sha512'] = hashlib.sha512(text.encode()).hexdigest()
        hashes['adler32'] = format(zlib.adler32(text.encode()), '08x')
        hashes['crc32'] = format(zlib.crc32(text.encode()), '08x')
    except Exception as e:
        print("Hash error:", e)
    return hashes