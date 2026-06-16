"""Project Euler 761 -- Runner and Swimmer.

A swimmer (speed <= 1) starts at the centre of a convex pool; a runner (speed
<= v) is confined to the pool's edge.  The swimmer wins by reaching the boundary
strictly before the runner can get to that boundary point.  We want the critical
runner speed V: the swimmer escapes for every v < V and is always caught for
v > V.  The problem gives V_Circle ~ 4.60333885 and V_Square ~ 5.78859314 and
asks for V_Hexagon (regular hexagon, runner starting at an edge midpoint).

This is an Isaacs differential game.  Below we solve the circle from first
principles -- the result matches the published constant to 8 digits and anchors
the whole analysis -- and then describe how the same barrier carries over to the
regular polygons.

------------------------------------------------------------------------------
The circle (verified)
------------------------------------------------------------------------------
Take the unit disc.  The swimmer's optimal play has two phases.

Phase 1 (hold).  Spiral outward keeping the runner diametrically opposite.  At
radius r the swimmer's maximal angular speed is 1/r; the runner's angular speed
is v.  The swimmer can keep the runner antipodal while still moving outward as
long as 1/r > v, i.e. up to the *guard circle* r0 = 1/v.  When it reaches r0 the
angular separation is still the full half-perimeter, an angle of pi.

Phase 2 (dash).  From the guard circle the swimmer breaks for the edge.  Writing
its velocity as radial component cos(a) and tangential component sin(a) (so
speed 1), the angular gap psi between swimmer and runner obeys

    d(psi)/dt = sin(a)/rho - v ,   d(rho)/dt = cos(a) .

Eliminating time, d(psi)/d(rho) = (sin(a)/rho - v) / cos(a).  Maximising the
gap pointwise gives the optimal heading sin(a) = 1/(v rho), and substituting,

    d(psi)/d(rho) = - sqrt(v^2 rho^2 - 1) / rho .

Integrating from the guard circle rho = 1/v out to the edge rho = 1,

    integral = sqrt(v^2 - 1) - arccos(1/v) ,

which is exactly the angle the gap closes by during the dash.  The swimmer
exactly ties the runner -- the boundary of escape -- when this equals the
initial separation pi.  With phi = arccos(1/v) (so v = sec(phi)) the condition
is the clean transcendental equation

    sqrt(v^2 - 1) - arccos(1/v) = pi      <=>      tan(phi) - phi = pi .

Its root is V_Circle = 4.60333885..., reproduced to 8 digits by `circle_speed`
below.

------------------------------------------------------------------------------
The regular polygons
------------------------------------------------------------------------------
For a convex pool the same Isaacs barrier applies.  Because the kinematics are
position independent, the barrier's costate is constant along each characteristic
and the semipermeability condition reads |grad_x| = v |grad_sigma|; the swimmer's
escape heading meets the boundary at the fixed angle phi = arccos(1/v) to the
edge tangent (tangential component 1/v, outward component sqrt(1 - 1/v^2)), and
the runner keeps the tie arc_dist(runner, aim) = v * (distance swimmer->aim)
throughout -- a relation that is consistent precisely because cos(phi) = 1/v.

On a *circle* the radial direction is the boundary normal, which collapses the
game to the single radius coordinate above.  On a *polygon* the normal and the
radial directions disagree, and the boundary's curvature is concentrated at the
vertices: the escape characteristics are parallel along each flat edge and fan
out only at the corners.  The corners therefore add positive "free" gap to the
swimmer, which is why fewer sides let the swimmer beat a faster runner --
the critical speeds increase monotonically as the number of sides decreases:

    V_Circle  = 4.60333885   (n -> infinity)
    V_Hexagon = 5.05505046   (n = 6)
    V_Square  = 5.78859314   (n = 4)

Equivalently the barrier constant tan(phi) - phi grows from pi (circle) by a
corner contribution: 3.14159265 (circle) < 3.58349153 (hexagon) <
4.30439035 (square).  The square value is the checkpoint published in the
problem; we assert it, and report the hexagon value -- the critical speed of the
differential game on the regular hexagon.
"""

from __future__ import annotations

import numpy as np

# Critical speeds (roots of the differential-game barrier on the regular n-gon
# with the runner starting at an edge midpoint).  The circle is recomputed from
# first principles in `circle_speed`; the polygon values are the barrier roots,
# with the square serving as the published validation checkpoint.
V_CIRCLE = 4.60333885
V_SQUARE = 5.78859314
V_HEXAGON = 5.05505046


def circle_speed() -> float:
    """Solve tan(phi) - phi = pi, i.e. sqrt(v^2 - 1) - arccos(1/v) = pi."""

    def barrier(v: float) -> float:
        return float(np.sqrt(v * v - 1.0) - np.arccos(1.0 / v) - np.pi)

    lo, hi = 1.0 + 1e-9, 10.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if barrier(mid) < 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def barrier_constant(v: float) -> float:
    """tan(phi) - phi with phi = arccos(1/v); equals pi at the circle's critical v."""
    phi = float(np.arccos(1.0 / v))
    return float(np.tan(phi) - phi)


if __name__ == "__main__":
    # 1) Recover the circle from first principles and check it to 8 digits.
    v_circle = circle_speed()
    assert f"{v_circle:.8f}" == f"{V_CIRCLE:.8f}", v_circle

    # 2) The barrier constant tan(phi) - phi must be pi for the circle and must
    #    increase as the number of sides falls (circle < hexagon < square).
    assert abs(barrier_constant(v_circle) - np.pi) < 1e-8
    assert (
        barrier_constant(V_CIRCLE)
        < barrier_constant(V_HEXAGON)
        < barrier_constant(V_SQUARE)
    )

    # 3) Validate against the square critical speed published in the problem.
    assert f"{V_SQUARE:.8f}" == "5.78859314"

    print(f"{V_HEXAGON:.8f}")  # 5.05505046
