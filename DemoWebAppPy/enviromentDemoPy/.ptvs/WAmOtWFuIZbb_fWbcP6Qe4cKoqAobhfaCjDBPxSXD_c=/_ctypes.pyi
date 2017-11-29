import builtins
import ctypes
ArgumentError = ctypes.ArgumentError()
class Array(_CData):
    'XXX to be provided'
    __class__ = Array
    def __delitem__(self, key):
        'Delete self[key].'
        pass
    def __getitem__(self, key):
        'Return self[key].'
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class CFuncPtr(_CData):
    'Function Pointer'
    def __bool__(self):
        'self != 0'
        pass
    def __call__(self, *args, **kwargs):
        'Call self as a function.'
        pass
    __class__ = PyCFuncPtr
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    argtypes = builtins.getset_descriptor()
    errcheck = builtins.getset_descriptor()
    restype = builtins.getset_descriptor()
class COMError(builtins.Exception):
    'Raised when a COM method call failed.'
    __class__ = COMError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
def CopyComPointer(src, dst):
    'CopyComPointer(src, dst) -> HRESULT value\n'
    pass
FUNCFLAG_CDECL = 1
FUNCFLAG_HRESULT = 2
FUNCFLAG_PYTHONAPI = 4
FUNCFLAG_STDCALL = 0
FUNCFLAG_USE_ERRNO = 8
FUNCFLAG_USE_LASTERROR = 16
def FormatError(integer):
    'FormatError([integer]) -> string\n\nConvert a win32 error code into a string. If the error code is not\ngiven, the return value of a call to GetLastError() is used.\n'
    pass
def FreeLibrary(handle):
    'FreeLibrary(handle) -> void\n\nFree the handle of an executable previously loaded by LoadLibrary.\n'
    pass
def LoadLibrary(name):
    'LoadLibrary(name) -> handle\n\nLoad an executable (usually a DLL), and return a handle to it.\nThe handle may be used to locate exported functions in this\nmodule.\n'
    pass
def POINTER():
    pass
def PyObj_FromPtr():
    pass
def Py_DECREF():
    pass
def Py_INCREF():
    pass
RTLD_GLOBAL = 0
RTLD_LOCAL = 0
class Structure(_CData):
    'Structure base class'
    __class__ = Structure
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class Union(_CData):
    'Union base class'
    __class__ = Union
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class _Pointer(_CData):
    'XXX to be provided'
    def __bool__(self):
        'self != 0'
        pass
    __class__ = _Pointer
    def __delitem__(self, key):
        'Delete self[key].'
        pass
    def __getitem__(self, key):
        'Return self[key].'
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    contents = builtins.getset_descriptor()
class _SimpleCData(_CData):
    'XXX to be provided'
    def __bool__(self):
        'self != 0'
        pass
    __class__ = _SimpleCData
    def __ctypes_from_outparam__(self):
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    value = builtins.getset_descriptor()
__doc__ = 'Create and manipulate C compatible data types in Python.'
__file__ = 'c:\\users\\office-user\\source\\repos\\demowebapppy\\demowebapppy\\enviromentdemopy\\scripts\\_ctypes.pyd'
__name__ = '_ctypes'
__package__ = ''
__spec__
__version__ = '1.1.0'
_cast_addr = 1475512016
def _check_HRESULT():
    pass
_memmove_addr = 140706112258864
_memset_addr = 140706112259968
_pointer_type_cache = {}
_string_at_addr = 1475511728
def _unpickle():
    pass
_wstring_at_addr = 1475512336
def addressof():
    'addressof(C instance) -> integer\nReturn the address of the C instance internal buffer'
    pass
def alignment():
    'alignment(C type) -> integer\nalignment(C instance) -> integer\nReturn the alignment requirements of a C instance'
    pass
def buffer_info():
    'Return buffer interface information'
    pass
def byref():
    'byref(C instance[, offset=0]) -> byref-object\nReturn a pointer lookalike to a C instance, only usable\nas function argument'
    pass
def call_cdeclfunction():
    pass
def call_function():
    pass
def get_errno():
    pass
def get_last_error():
    pass
def pointer():
    pass
def resize():
    'Resize the memory buffer of a ctypes instance'
    pass
def set_errno():
    pass
def set_last_error():
    pass
def sizeof():
    'sizeof(C type) -> integer\nsizeof(C instance) -> integer\nReturn the size in bytes of a C instance'
    pass
