#   App_Exceptions is a support file used to supply other application modules
#   with custom exception classes.


#   Error is used to enable custom exception types
#   https://www.programiz.com/python-programming/user-defined-exception
class Error(Exception):
    pass


#   InvalidModelSelection is used to indicate programmer error with regards to
#   model calls, i.e. the programmer has called for a button of type "k," when
#   only A, B, X and Y exist.
class InvalidModelSelection(Error):
    pass
