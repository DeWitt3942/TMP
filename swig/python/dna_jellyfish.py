# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""Jellyfish binding"""



import os
if os.path.basename(__file__) == "__init__.pyc" or os.path.basename(__file__) == "__init__.py":
  import dna_jellyfish._dna_jellyfish
else:
  import _dna_jellyfish

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class MerDNA(_object):
    """Class representing a mer. All the mers have the same length, which must be set BEFORE instantiating any mers with jellyfish::MerDNA::k(int)"""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MerDNA, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MerDNA, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        Class representing a mer. All the mers have the same length, which must be set BEFORE instantiating any mers with jellyfish::MerDNA::k(int)
        Class representing a mer. All the mers have the same length, which must be set BEFORE instantiating any mers with jellyfish::MerDNA::k(int)
        Class representing a mer. All the mers have the same length, which must be set BEFORE instantiating any mers with jellyfish::MerDNA::k(int)
        """
        this = _dna_jellyfish.new_MerDNA(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def k(*args):
        """
        Get the length of the k-mers
        Set the length of the k-mers
        """
        return _dna_jellyfish.MerDNA_k(*args)

    k = staticmethod(k)

    def polyA(self):
        """Change the mer to a homopolymer of A"""
        return _dna_jellyfish.MerDNA_polyA(self)


    def polyC(self):
        """Change the mer to a homopolymer of C"""
        return _dna_jellyfish.MerDNA_polyC(self)


    def polyG(self):
        """Change the mer to a homopolymer of G"""
        return _dna_jellyfish.MerDNA_polyG(self)


    def polyT(self):
        """Change the mer to a homopolymer of T"""
        return _dna_jellyfish.MerDNA_polyT(self)


    def randomize(self):
        """Change the mer to a random one"""
        return _dna_jellyfish.MerDNA_randomize(self)


    def is_homopolymer(self):
        """Check if the mer is a homopolymer"""
        return _dna_jellyfish.MerDNA_is_homopolymer(self)


    def shift_left(self, arg2):
        """Shift a base to the left and the leftmost base is return . "ACGT", shift_left('A') becomes "CGTA" and 'A' is returned"""
        return _dna_jellyfish.MerDNA_shift_left(self, arg2)


    def shift_right(self, arg2):
        """Shift a base to the right and the rightmost base is return . "ACGT", shift_right('A') becomes "AACG" and 'T' is returned"""
        return _dna_jellyfish.MerDNA_shift_right(self, arg2)


    def canonicalize(self):
        """Change the mer to its canonical representation"""
        return _dna_jellyfish.MerDNA_canonicalize(self)


    def reverse_complement(self):
        """Change the mer to its reverse complement"""
        return _dna_jellyfish.MerDNA_reverse_complement(self)


    def get_canonical(self):
        """Return canonical representation of the mer"""
        return _dna_jellyfish.MerDNA_get_canonical(self)


    def get_reverse_complement(self):
        """Return the reverse complement of the mer"""
        return _dna_jellyfish.MerDNA_get_reverse_complement(self)


    def __eq__(self, arg2):
        """Equality between mers"""
        return _dna_jellyfish.MerDNA___eq__(self, arg2)


    def __lt__(self, arg2):
        """Lexicographic less-than"""
        return _dna_jellyfish.MerDNA___lt__(self, arg2)


    def __gt__(self, arg2):
        """Lexicographic greater-than"""
        return _dna_jellyfish.MerDNA___gt__(self, arg2)


    def dup(self):
        """Duplicate the mer"""
        return _dna_jellyfish.MerDNA_dup(self)


    def __str__(self):
        """Return string representation of the mer"""
        return _dna_jellyfish.MerDNA___str__(self)


    def set(self, s):
        """Set the mer from a string"""
        return _dna_jellyfish.MerDNA_set(self, s)


    def __getitem__(self, i):
        """Get base i (0 <= i < k)"""
        return _dna_jellyfish.MerDNA___getitem__(self, i)


    def __setitem__(self, i, b):
        """Set base i (0 <= i < k)"""
        return _dna_jellyfish.MerDNA___setitem__(self, i, b)


    def __lshift__(self, b):
        """Shift a base to the left and return the mer"""
        return _dna_jellyfish.MerDNA___lshift__(self, b)


    def __rshift__(self, b):
        """Shift a base to the right and return the mer"""
        return _dna_jellyfish.MerDNA___rshift__(self, b)

    __swig_destroy__ = _dna_jellyfish.delete_MerDNA
    __del__ = lambda self: None
MerDNA_swigregister = _dna_jellyfish.MerDNA_swigregister
MerDNA_swigregister(MerDNA)

def MerDNA_k(*args):
    """
    Get the length of the k-mers
    Set the length of the k-mers
    """
    return _dna_jellyfish.MerDNA_k(*args)

class QueryMerFile(_object):
    """Give random access to a Jellyfish database. Given a mer, it returns the count associated with that mer"""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, QueryMerFile, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, QueryMerFile, name)
    __repr__ = _swig_repr

    def __init__(self, path):
        """Open the jellyfish database"""
        this = _dna_jellyfish.new_QueryMerFile(path)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __getitem__(self, m):
        """Get the count for the mer m"""
        return _dna_jellyfish.QueryMerFile___getitem__(self, m)

    __swig_destroy__ = _dna_jellyfish.delete_QueryMerFile
    __del__ = lambda self: None
QueryMerFile_swigregister = _dna_jellyfish.QueryMerFile_swigregister
QueryMerFile_swigregister(QueryMerFile)

class ReadMerFile(_object):
    """Read a Jellyfish database sequentially"""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ReadMerFile, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ReadMerFile, name)
    __repr__ = _swig_repr

    def __init__(self, path):
        """Open the jellyfish database"""
        this = _dna_jellyfish.new_ReadMerFile(path)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def next_mer(self):
        """Move to the next mer in the file. Returns false if no mers left, true otherwise"""
        return _dna_jellyfish.ReadMerFile_next_mer(self)


    def mer(self):
        """Returns current mer"""
        return _dna_jellyfish.ReadMerFile_mer(self)


    def count(self):
        """Returns the count of the current mer"""
        return _dna_jellyfish.ReadMerFile_count(self)


    def __iter__(self):
        """Iterate through all the mers in the file, passing two values: a mer and its count"""
        return _dna_jellyfish.ReadMerFile___iter__(self)


    def __next__(self):
        """Iterate through all the mers in the file, passing two values: a mer and its count"""
        return _dna_jellyfish.ReadMerFile___next__(self)


    def next(self):
        """Iterate through all the mers in the file, passing two values: a mer and its count"""
        return _dna_jellyfish.ReadMerFile_next(self)

    __swig_destroy__ = _dna_jellyfish.delete_ReadMerFile
    __del__ = lambda self: None
ReadMerFile_swigregister = _dna_jellyfish.ReadMerFile_swigregister
ReadMerFile_swigregister(ReadMerFile)

class HashCounter(_object):
    """Read a Jellyfish database sequentially"""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, HashCounter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, HashCounter, name)
    __repr__ = _swig_repr

    def __init__(self, size, val_len, nb_threads=1):
        """
        Read a Jellyfish database sequentially
        Read a Jellyfish database sequentially
        """
        this = _dna_jellyfish.new_HashCounter(size, val_len, nb_threads)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def size(self):
        """Read a Jellyfish database sequentially"""
        return _dna_jellyfish.HashCounter_size(self)


    def val_len(self):
        """Read a Jellyfish database sequentially"""
        return _dna_jellyfish.HashCounter_val_len(self)


    def add(self, m, x):
        """Read a Jellyfish database sequentially"""
        return _dna_jellyfish.HashCounter_add(self, m, x)


    def update_add(self, arg2, arg3):
        """Read a Jellyfish database sequentially"""
        return _dna_jellyfish.HashCounter_update_add(self, arg2, arg3)


    def get(self, m):
        """Read a Jellyfish database sequentially"""
        return _dna_jellyfish.HashCounter_get(self, m)


    def __getitem__(self, m):
        """Read a Jellyfish database sequentially"""
        return _dna_jellyfish.HashCounter___getitem__(self, m)

    __swig_destroy__ = _dna_jellyfish.delete_HashCounter
    __del__ = lambda self: None
HashCounter_swigregister = _dna_jellyfish.HashCounter_swigregister
HashCounter_swigregister(HashCounter)

class HashSet(_object):
    """Read a Jellyfish database sequentially"""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, HashSet, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, HashSet, name)
    __repr__ = _swig_repr

    def __init__(self, size, nb_threads=1):
        """
        Read a Jellyfish database sequentially
        Read a Jellyfish database sequentially
        """
        this = _dna_jellyfish.new_HashSet(size, nb_threads)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def size(self):
        """Read a Jellyfish database sequentially"""
        return _dna_jellyfish.HashSet_size(self)


    def add(self, m):
        """Read a Jellyfish database sequentially"""
        return _dna_jellyfish.HashSet_add(self, m)


    def get(self, m):
        """Read a Jellyfish database sequentially"""
        return _dna_jellyfish.HashSet_get(self, m)


    def __getitem__(self, m):
        """Read a Jellyfish database sequentially"""
        return _dna_jellyfish.HashSet___getitem__(self, m)

    __swig_destroy__ = _dna_jellyfish.delete_HashSet
    __del__ = lambda self: None
HashSet_swigregister = _dna_jellyfish.HashSet_swigregister
HashSet_swigregister(HashSet)


def string_mers(str):
    """Get an iterator to the mers in the string"""
    return _dna_jellyfish.string_mers(str)

def string_canonicals(str):
    """Get an iterator to the canonical mers in the string"""
    return _dna_jellyfish.string_canonicals(str)
class StringMers(_object):
    """Extract k-mers from a sequence string"""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringMers, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringMers, name)
    __repr__ = _swig_repr

    def __init__(self, str, len, canonical):
        """Create a k-mers parser from a string. Pass true as a second argument to get canonical mers"""
        this = _dna_jellyfish.new_StringMers(str, len, canonical)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def next_mer(self):
        """Get the next mer. Return false if reached the end of the string."""
        return _dna_jellyfish.StringMers_next_mer(self)


    def mer(self):
        """Return the current mer (or its canonical representation)"""
        return _dna_jellyfish.StringMers_mer(self)


    def __iter__(self):
        """Return the current mer (or its canonical representation)"""
        return _dna_jellyfish.StringMers___iter__(self)


    def __next__(self):
        """Return the current mer (or its canonical representation)"""
        return _dna_jellyfish.StringMers___next__(self)


    def next(self):
        """Return the current mer (or its canonical representation)"""
        return _dna_jellyfish.StringMers_next(self)

    __swig_destroy__ = _dna_jellyfish.delete_StringMers
    __del__ = lambda self: None
StringMers_swigregister = _dna_jellyfish.StringMers_swigregister
StringMers_swigregister(StringMers)

# This file is compatible with both classic and new-style classes.


