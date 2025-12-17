"""
Patch for PySCF rotational constants (thermo.rotation_const).

This module applies a small numerical fix affecting rotational constants
for (near-)linear molecules. The issue is discussed in the PySCF GitHub
issue tracker (e.g. https://github.com/pyscf/pyscf/issues/2401).

The purpose of this patch is purely practical: it ensures that the
rotational constants returned by PySCF's finite-difference Hessian
machinery are non-negative and consistently ordered, avoiding occasional
sign flips caused by numerical noise.

This patch is safe to treat as a black box. Importing this module once
(e.g., `import patch`) is sufficient to activate the fix for the rest of
the Python session.
"""

import numpy as np
from pyscf.hessian import thermo

# Preserve the original implementation so the wrapper can call it.
if not hasattr(thermo, "_orig_rotation_const"):
    thermo._orig_rotation_const = thermo.rotation_const


def rotation_const_abs(mass, coords, unit="GHz"):
    """Return non-negative, sorted rotational constants.

    Parameters
    ----------
    mass : ndarray
        Atomic masses.
    coords : ndarray
        Cartesian coordinates of the atoms.
    unit : str, optional
        Unit for the rotational constants (default: "GHz").

    Notes
    -----
    This wrapper calls the original `thermo.rotation_const` implementation
    and then removes numerical sign noise by taking absolute values and
    sorting the constants in ascending order.
    """
    # Use PySCF's original routine
    rot = thermo._orig_rotation_const(mass, coords, unit=unit)

    # Remove occasional negative signs due to numerical noise
    rot = np.abs(rot)

    # Sort for consistency; this aids interpretation and debugging
    rot = np.sort(rot)

    return rot


# Replace PySCF's function with the patched version
thermo.rotation_const = rotation_const_abs