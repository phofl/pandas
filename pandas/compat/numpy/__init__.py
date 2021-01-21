""" support numpy compatibility across versions """

from distutils.version import LooseVersion

import numpy as np

# numpy versioning
_np_version = np.__version__
_nlv = LooseVersion(_np_version)
np_version_under1p17 = _nlv < LooseVersion("1.17")
np_version_under1p18 = _nlv < LooseVersion("1.18")
np_version_under1p19 = _nlv < LooseVersion("1.19")
np_version_under1p20 = _nlv < LooseVersion("1.20")
is_numpy_dev = ".dev" in str(_nlv)
_min_numpy_ver = "1.16.5"


if _nlv < _min_numpy_ver:
    raise ImportError(
        f"this version of pandas is incompatible with numpy < {_min_numpy_ver}\n"
        f"your numpy version is {_np_version}.\n"
        f"Please upgrade numpy to >= {_min_numpy_ver} to use this pandas version"
    )


__all__ = ["np", "_np_version"]
