import numpy as np
from pyscf.data import nist
from pyscf.hessian import thermo

# Preserve original implementation
if not hasattr(thermo, "_orig_rotation_const"):
    thermo._orig_rotation_const = thermo.rotation_const


def rotation_const_clip_inertia(mass, atom_coords, unit="GHz", eps=1e-12):
    """
    Stable rotational constants for (near-)linear molecules.

    Fix: clip principal moments of inertia eigenvalues to a small positive eps
    BEFORE converting to rotational constants. This prevents negative/zero
    eigenvalues from numerical noise (which cause NaNs), while preserving the
    huge-constant pattern used to classify LINEAR rotors upstream.
    """
    mass = np.asarray(mass, dtype=float)
    atom_coords = np.asarray(atom_coords, dtype=float)

    # ---- reproduce upstream inertia eigenvalues ----
    mass_center = np.einsum("z,zr->r", mass, atom_coords) / mass.sum()
    r = atom_coords - mass_center
    im = np.einsum("z,zr,zs->rs", mass, r, r)
    im = np.eye(3) * im.trace() - im
    e = np.sort(np.linalg.eigvalsh(im))  # principal moments of inertia

    # ---- key fix: clip inertia eigenvalues ----
    # eps is in the same units as 'im' (mass * bohr^2 in atomic units context).
    e = np.maximum(e, eps)

    # ---- convert inertia to rotational constants, same as upstream ----
    unit_im = nist.ATOMIC_MASS * (nist.BOHR_SI) ** 2
    unit_hz = nist.HBAR / (4 * np.pi * unit_im)

    with np.errstate(divide="ignore"):
        if unit.lower() == "ghz":
            rot = unit_hz / e * 1e-9
        elif unit.lower() == "wavenumber":
            rot = unit_hz / e / nist.LIGHT_SPEED_SI * 1e-2
        else:
            raise RuntimeError("Unsupported unit " + unit)

    return rot


thermo.rotation_const = rotation_const_clip_inertia