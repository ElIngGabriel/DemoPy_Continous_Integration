import builtins
class HASH(builtins.object):
    'A hash represents the object used to calculate a checksum of a\nstring of information.\n\nMethods:\n\nupdate() -- updates the current digest with an additional string\ndigest() -- return the current digest value\nhexdigest() -- return the current digest as a string of hexadecimal digits\ncopy() -- return a copy of the current hash object\n\nAttributes:\n\nname -- the hash algorithm being used by this object\ndigest_size -- number of bytes in this hashes output\n'
    __class__ = HASH
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    block_size = builtins.getset_descriptor()
    def copy(self):
        'Return a copy of the hash object.'
        pass
    def digest(self):
        'Return the digest value as a string of binary data.'
        pass
    digest_size = builtins.getset_descriptor()
    def hexdigest(self):
        'Return the digest value as a string of hexadecimal digits.'
        pass
    name = builtins.member_descriptor()
    def update(self):
        "Update this hash object's state with the provided string."
        pass
__doc__
__file__ = 'c:\\repos\\github\\demopy_continous_integration\\demowebapppy\\enviromentdemopy\\scripts\\_hashlib.pyd'
__name__ = '_hashlib'
__package__ = ''
__spec__
def new():
    'Return a new hash object using the named algorithm.\nAn optional string argument may be provided and will be\nautomatically hashed.\n\nThe MD5 and SHA1 algorithms are always supported.\n'
    pass
def openssl_md5():
    'Returns a md5 hash object; optionally initialized with a string'
    pass
openssl_md_meth_names = builtins.frozenset()
def openssl_sha1():
    'Returns a sha1 hash object; optionally initialized with a string'
    pass
def openssl_sha224():
    'Returns a sha224 hash object; optionally initialized with a string'
    pass
def openssl_sha256():
    'Returns a sha256 hash object; optionally initialized with a string'
    pass
def openssl_sha384():
    'Returns a sha384 hash object; optionally initialized with a string'
    pass
def openssl_sha512():
    'Returns a sha512 hash object; optionally initialized with a string'
    pass
def pbkdf2_hmac(hash_name, password, salt, iterations, dklen):
    'pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None) -> key\n\nPassword based key derivation function 2 (PKCS #5 v2.0) with HMAC as\npseudorandom function.'
    pass
