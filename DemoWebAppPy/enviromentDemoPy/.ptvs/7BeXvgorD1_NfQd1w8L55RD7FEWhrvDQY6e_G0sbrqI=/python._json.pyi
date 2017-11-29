import builtins
__doc__ = 'json speedups\n'
__name__ = '_json'
__package__ = ''
__spec__
def encode_basestring(string):
    'encode_basestring(string) -> string\n\nReturn a JSON representation of a Python string'
    pass
def encode_basestring_ascii(string):
    'encode_basestring_ascii(string) -> string\n\nReturn an ASCII-only JSON representation of a Python string'
    pass
class make_encoder(builtins.object):
    '_iterencode(obj, _current_indent_level) -> iterable'
    def __call__(self, *args, **kwargs):
        'Call self as a function.'
        pass
    __class__ = Encoder
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    default = builtins.member_descriptor()
    encoder = builtins.member_descriptor()
    indent = builtins.member_descriptor()
    item_separator = builtins.member_descriptor()
    key_separator = builtins.member_descriptor()
    markers = builtins.member_descriptor()
    skipkeys = builtins.member_descriptor()
    sort_keys = builtins.member_descriptor()
class make_scanner(builtins.object):
    'JSON scanner object'
    def __call__(self, *args, **kwargs):
        'Call self as a function.'
        pass
    __class__ = Scanner
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    object_hook = builtins.member_descriptor()
    object_pairs_hook = builtins.member_descriptor()
    parse_constant = builtins.member_descriptor()
    parse_float = builtins.member_descriptor()
    parse_int = builtins.member_descriptor()
    strict = builtins.member_descriptor()
def scanstring(string, end, strict):
    'scanstring(string, end, strict=True) -> (string, end)\n\nScan the string s for a JSON string. End is the index of the\ncharacter in s after the quote that started the JSON string.\nUnescapes all valid JSON string escape sequences and raises ValueError\non attempt to decode an invalid string. If strict is False then literal\ncontrol characters are allowed in the string.\n\nReturns a tuple of the decoded string and the index of the character in s\nafter the end quote.'
    pass
