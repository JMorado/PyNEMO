"""a Python based regional NEMO model configuration toolbox."""

# Copyright 2023, NOC.

try:
    # NOTE: the `version.py` file must not be present in the git repository
    #   as it is generated by setuptools at install time
    from .version import __version__
except ImportError:  # pragma: no cover
    # Local copy or not installed with setuptools
    __version__ = "999"

__all__ = ["__version__"]
