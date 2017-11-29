__doc__ = '_warnings provides basic warning filtering support.\nIt is a helper module to speed up interpreter start-up.'
__name__ = '_warnings'
__package__ = ''
__spec__
_defaultaction = 'default'
def _filters_mutated():
    pass
_onceregistry = {}
filters = [('ignore', None, <class 'DeprecationWarning'>, None, 0), ('ignore', None, <class 'PendingDeprecationWarning'>, None, 0), ('ignore', None, <class 'ImportWarning'>, None, 0), ('ignore', None, <class 'BytesWarning'>, None, 0), ('ignore', None, <class 'ResourceWarning'>, None, 0)]
def warn():
    'Issue a warning, or maybe ignore it or raise an exception.'
    pass
def warn_explicit():
    'Low-level inferface to warnings functionality.'
    pass
