"""The improb module implements various classes for working with
imprecise probabilities.

Main classes
============

- L{LowPrev}: lower and upper previsions, natural extension
"""

__version__ = '0.0.0'

def _make_tuple(pspace):
    """Convert argument into a tuple, useful for possibility space."""
    if pspace is None:
        return (0, 1)
    elif isinstance(pspace, int):
        return tuple(xrange(pspace))
    else:
        return tuple(pspace)
