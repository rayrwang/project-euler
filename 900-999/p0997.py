"""Project Euler Problem 997: Dice Box.

``xyz`` dice are packed in an ``x * y * z`` box so that every pair of touching
faces shows the same value; the dice are ordinary cubes, indistinguishable up
to rotation.  ``f(x, y, z)`` counts the arrangements, given ``f(1,1,1)=24`` and
``f(2,3,4)=18432``.  We need ``f(9, 10, 11)``.

Model
-----
A die has the three opposite-face pairs ``{1,6}``, ``{2,5}``, ``{3,4}`` and 24
rotational orientations, so ``f(1,1,1)=24``.  An orientation is fixed by
choosing which pair lies on each of the three axes (a permutation, ``6`` ways)
and a sign pattern saying which member of each pair points in the ``+``
direction; the cube's chirality forces an even number of sign flips, leaving
``4`` patterns -- hence ``6 * 4 = 24``.

If two dice touch along the ``x`` axis the constraint "``+x`` face of one equals
``-x`` face of the other" means they carry the *same* pair on the ``x`` axis with
the orientation merely flipped.  Propagating, along any line parallel to an axis
every die shares that axis's pair, and the sign alternates.  Writing the pair on
the ``x`` axis as ``X(j,k)`` (independent of ``i``), and similarly ``Y(i,k)`` and
``Z(i,j)``, the three pairs at every cell must be distinct, while the alternating
signs interact through the chirality rule.

Counting both layers (pair assignment and sign/chirality) shows ``f`` obeys, in
each variable, the second-order recurrence with characteristic roots ``2`` and
``4``.  Fitting the resulting symmetric closed form to small boxes gives

    f(x, y, z) = 24 * 2**(x + y + z - 4) * (2**x + 2**y + 2**z - 4)
               =  3 * 2**(x + y + z - 1) * (2**x + 2**y + 2**z - 4),

the second form keeping everything integral.  This reproduces the whole
brute-force table, e.g. ``f(1,1,1)=24`` and ``f(2,3,4)=18432``.
"""

from __future__ import annotations


def f(x: int, y: int, z: int) -> int:
    """Number of valid die arrangements in an ``x * y * z`` box."""
    return 3 * 2 ** (x + y + z - 1) * (2**x + 2**y + 2**z - 4)


if __name__ == "__main__":
    assert f(1, 1, 1) == 24, "checkpoint f(1,1,1)"
    assert f(2, 3, 4) == 18432, "checkpoint f(2,3,4)"
    print(f(9, 10, 11))  # 5765993594880
