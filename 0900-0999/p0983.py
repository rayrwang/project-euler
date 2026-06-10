"""Project Euler 983.

Two circles of equal radius r with grid centers that pass through one common
grid point P automatically pass through a second one, Q = C1 + C2 - P, since
Q is integral and |Q - C1| = |C2 - P| = r. So under the no-tangency rule,
"harmonising" simply means sharing a grid point at distance r from both
centers, and r^2 = N must be an integer expressible as a sum of two squares.

Perfect consonant sets are "hypercube" configurations. Pick d pairwise
non-parallel lattice vectors v_1..v_d of norm N; let the centers be the odd
subset sums and the harmony points the even subset sums. Each harmonising
pair forms a rhombus with side r, every cherry P-C1-C2 closes into one, and
the count is 2^(d-1) circles and 2^(d-1) points. Exhaustive search over all
connected center sets at small N (e.g. every set up to size 6 at N = 5) finds
no other perfect sets, and the construction reproduces the given values
R(2) = 1 (d = 2 at N = 1) and R(4) = sqrt(5) (d = 3 at N = 5), which this
program asserts. n >= 500 needs d = 10 directions, hence at least 20 lattice
points on the circle, so N >= 325.

The difficulty is that having 20 lattice points is nowhere near sufficient:
writing V for all norm-N lattice vectors, a choice of generators only works if
every +-1-signed sum x over a support M of the chosen ten avoids
    x = 0                  (two centers collide),
    |x|^2 = 4N             (two circles tangent),
    |x|^2 = N, |M| odd     (a stray center-point incidence), and
    x in V - V, |M| even   (two far circles share a stray grid point,
                            spawning extra harmony points),
because any of these (with |M| < 10, realizable in both parities) breaks
|harmony points| = |circles|. Such relations are pervasive: every candidate
N < 6725 fails. A signed sum using all ten generators is realized only by
center pairs whose positive part has the right parity, so it kills just one
of the two orientations (centers on odd sums vs. centers on even sums); those
edge cases are settled by direct verification. That is exactly how the answer
configuration at N = 6725 = 5^2 * 269 survives: its single violating relation
has full support with odd positive part, so the even-sum orientation is a
flawless perfect set of 512 >= 500 circles.

Collisions are not always instantly fatal (merging identifies centers and
points in equal numbers), so subsets containing a vanishing signed sum are
enumerated separately: meet-in-the-middle finds every vanishing relation,
and all supersets of the minimal supports are checked directly, pruned only
by the tangency rule, which stays sound under merging. No merged
configuration ever stays perfect, and the first radius admitting a perfect
consonant set of at least 500 circles is r^2 = 6725.

Everything that reaches the final stage is verified against the definition:
distinct centers, no two centers at distance 2r, the grid points at distance
r from at least two centers counted exactly, and connectivity of the
harmonising graph.
"""

import numpy as np

ENC = 1 << 22
OFF = 1 << 21


def lattice_vecs(n):
    """All lattice vectors of squared length n."""
    out = set()
    a = 0
    while a * a <= n:
        b = int((n - a * a) ** 0.5)
        while b * b < n - a * a:
            b += 1
        if a * a + b * b == n:
            out |= {(a, b), (-a, b), (a, -b), (-a, -b)}
        a += 1
    return sorted(out)


def perfect_size(centers, n, V, O4):
    """Size of the perfect consonant set with these centers, else 0."""
    codes = np.unique((centers[:, 0] + OFF) * ENC + (centers[:, 1] + OFF))
    nc = len(codes)
    if nc < 2:
        return 0
    # harmony points: grid points at distance r from >= 2 distinct centers
    vc = np.array([dx * ENC + dy for dx, dy in V], dtype=np.int64)
    pcodes = (codes[:, None] + vc[None, :]).ravel()
    uniq, counts = np.unique(pcodes, return_counts=True)
    if int((counts >= 2).sum()) != nc:
        return 0
    # tangency: two centers separated by a norm-4n vector
    for dx, dy in O4:
        if np.intersect1d(codes + dx * ENC + dy, codes,
                          assume_unique=True).size:
            return 0
    # connectivity of the harmonising graph via shared points (union-find)
    parent = list(range(nc))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    owner = np.repeat(np.arange(nc), len(V))
    order = np.argsort(pcodes, kind="stable")
    pc_s, own_s = pcodes[order], owner[order]
    i = 0
    while i < len(pc_s):
        j = i + 1
        while j < len(pc_s) and pc_s[j] == pc_s[i]:
            j += 1
        for k in range(i + 1, j):
            parent[find(int(own_s[k]))] = find(int(own_s[i]))
        i = j
    return nc if len({find(i) for i in range(nc)}) == 1 else 0


def subset_sums_by_parity(gens):
    s = np.zeros((1, 2), dtype=np.int64)
    for g in gens:
        s = np.vstack([s, s + np.asarray(g, dtype=np.int64)])
    pop = np.array([bin(m).count("1") % 2 for m in range(len(s))], dtype=bool)
    return s[pop], s[~pop]


class CandidateSearch:
    """Decide whether radius^2 = n admits a perfect set of >= need circles."""

    def __init__(self, n, d, need):
        self.n, self.d, self.need = n, d, need
        self.V = lattice_vecs(n)
        self.O4 = lattice_vecs(4 * n)
        self.Va = np.array(self.V, dtype=np.int64)
        self.dirs = [v for v in self.V if v > (-v[0], -v[1])]
        dif = (self.Va[:, None, :] - self.Va[None, :, :]).reshape(-1, 2)
        self.vv = np.unique((dif[:, 0] + OFF) * ENC + (dif[:, 1] + OFF))
        self.checked = set()
        self.hit = False

    def ground_truth(self, sub):
        key = frozenset(sub)
        if self.hit or key in self.checked:
            return
        self.checked.add(key)
        for centers in subset_sums_by_parity(list(sub)):
            if perfect_size(centers, self.n, self.V, self.O4) >= self.need:
                self.hit = True
                return

    def violations(self, nex, ney, nesz, nox, noy, nosz, k):
        """Classify violations among newly created signed sums.

        Returns (proper, edge, collided): proper-support violation (< k,
        fatal for every completion in the collision-free space), full-support
        violation (== k, kills one orientation only), and whether a vanishing
        sum appeared (subset belongs to the merged space)."""
        n = self.n
        qe = nex * nex + ney * ney
        bad_e = qe == 4 * n
        big = nesz >= 4
        if np.any(big):
            invv = np.isin((nex[big] + OFF) * ENC + (ney[big] + OFF), self.vv)
            tmp = np.zeros(len(nex), dtype=bool)
            tmp[np.flatnonzero(big)[invv]] = True
            bad_e |= tmp
        qo = nox * nox + noy * noy
        bad_o = (qo == n) & (nosz >= 3)
        proper = bool(np.any(bad_e & (nesz < k)) or np.any(bad_o & (nosz < k)))
        edge = bool(np.any(bad_e & (nesz == k)) or np.any(bad_o & (nosz == k)))
        collided = bool(np.any(qe == 0))
        return proper, edge, collided

    @staticmethod
    def extend(ex, ey, esz, ox, oy, osz, vx, vy):
        one = np.array([1], dtype=np.int64)
        nox = np.concatenate([one * vx, ex + vx, ex - vx])
        noy = np.concatenate([one * vy, ey + vy, ey - vy])
        nosz = np.concatenate([one, esz + 1, esz + 1])
        nex = np.concatenate([ox + vx, ox - vx])
        ney = np.concatenate([oy + vy, oy - vy])
        nesz = np.concatenate([osz + 1, osz + 1])
        return nex, ney, nesz, nox, noy, nosz

    # -- pass 1: collision-free configurations, exactly d directions --------
    def dfs_clean(self, start, ex, ey, esz, ox, oy, osz, cur):
        if self.hit:
            return
        if len(cur) == self.d:
            self.ground_truth(cur)
            return
        for i in range(start, len(self.dirs)):
            vx, vy = self.dirs[i]
            nex, ney, nesz, nox, noy, nosz = self.extend(
                ex, ey, esz, ox, oy, osz, vx, vy)
            k = len(cur) + 1
            proper, edge, collided = self.violations(
                nex, ney, nesz, nox, noy, nosz, k)
            if proper or collided:
                continue  # collided subsets are covered by pass 2
            if edge:
                if k == self.d:
                    self.ground_truth(cur + [(vx, vy)])
                continue
            cur.append((vx, vy))
            self.dfs_clean(i + 1, np.concatenate([ex, nex]),
                           np.concatenate([ey, ney]),
                           np.concatenate([esz, nesz]),
                           np.concatenate([ox, nox]),
                           np.concatenate([oy, noy]),
                           np.concatenate([osz, nosz]), cur)
            cur.pop()
            if self.hit:
                return

    # -- pass 2: configurations containing a vanishing signed sum -----------
    def vanishing_supports(self):
        """Meet-in-the-middle: supports of all signed sums of distinct
        directions equal to zero."""
        nd = len(self.dirs)
        half = nd // 2

        def signed(dset):
            sums = np.zeros((1, 2), dtype=np.int64)
            code = np.zeros(1, dtype=np.int64)
            for k, (x, y) in enumerate(dset):
                v = np.array([x, y], dtype=np.int64)
                sums = np.vstack([sums, sums + v, sums - v])
                code = np.concatenate([code, code + 3 ** k,
                                       code + 2 * 3 ** k])
            return sums, code

        sL, cL = signed(self.dirs[:half])
        sR, cR = signed(self.dirs[half:])
        eL = (sL[:, 0] + OFF) * ENC + sL[:, 1]
        eR = (-sR[:, 0] + OFF) * ENC - sR[:, 1]
        oL, oR = np.argsort(eL), np.argsort(eR)
        supps = set()
        i = j = 0
        while i < len(oL) and j < len(oR):
            a, b = eL[oL[i]], eR[oR[j]]
            if a < b:
                i += 1
            elif a > b:
                j += 1
            else:
                i2, j2 = i, j
                while i2 < len(oL) and eL[oL[i2]] == a:
                    i2 += 1
                while j2 < len(oR) and eR[oR[j2]] == a:
                    j2 += 1
                for p in range(i, i2):
                    for q in range(j, j2):
                        ca, cb = int(cL[oL[p]]), int(cR[oR[q]])
                        if ca == 0 and cb == 0:
                            continue
                        m = 0
                        for k in range(half):
                            if (ca // 3 ** k) % 3:
                                m |= 1 << k
                        for k in range(nd - half):
                            if (cb // 3 ** k) % 3:
                                m |= 1 << (half + k)
                        supps.add(m)
                i, j = i2, j2
        minimal = []
        for m in sorted(supps, key=lambda x: bin(x).count("1")):
            if not any((b & m) == b for b in minimal):
                minimal.append(m)
        return minimal

    def dfs_merged(self, rest, start, ex, ey, esz, ox, oy, osz, cur, base):
        """Supersets of a vanishing support; only the tangency rule is sound
        once centers can merge, so everything else is verified directly."""
        if self.hit:
            return
        for i in range(start, len(rest)):
            vx, vy = rest[i]
            nex, ney, nesz, nox, noy, nosz = self.extend(
                ex, ey, esz, ox, oy, osz, vx, vy)
            k = len(base) + len(cur) + 1
            qe = nex * nex + ney * ney
            tang = qe == 4 * self.n
            if np.any(tang & (nesz < k)):
                continue
            sub = base + cur + [(vx, vy)]
            if np.any(tang & (nesz == k)):
                if k >= self.d:
                    self.ground_truth(sub)
                continue
            if k >= self.d:
                self.ground_truth(sub)
                if self.hit:
                    return
            cur.append((vx, vy))
            self.dfs_merged(rest, i + 1, np.concatenate([ex, nex]),
                            np.concatenate([ey, ney]),
                            np.concatenate([esz, nesz]),
                            np.concatenate([ox, nox]),
                            np.concatenate([oy, noy]),
                            np.concatenate([osz, nosz]), cur, base)
            cur.pop()
            if self.hit:
                return

    def run(self):
        z = np.zeros(0, dtype=np.int64)
        self.dfs_clean(0, z, z, z, z, z, z, [])
        if self.hit:
            return True
        for mask in self.vanishing_supports():
            base = [self.dirs[i] for i in range(len(self.dirs))
                    if (mask >> i) & 1]
            rest = [self.dirs[i] for i in range(len(self.dirs))
                    if not (mask >> i) & 1]
            ex, ey, esz, ox, oy, osz = z, z, z, z, z, z
            for vx, vy in base:
                nex, ney, nesz, nox, noy, nosz = self.extend(
                    ex, ey, esz, ox, oy, osz, vx, vy)
                ex, ey = np.concatenate([ex, nex]), np.concatenate([ey, ney])
                esz = np.concatenate([esz, nesz])
                ox, oy = np.concatenate([ox, nox]), np.concatenate([oy, noy])
                osz = np.concatenate([osz, nosz])
            qe = ex * ex + ey * ey
            tang = qe == 4 * self.n
            if np.any(tang & (esz < len(base))):
                continue
            if np.any(tang & (esz == len(base))):
                if len(base) >= self.d:
                    self.ground_truth(base)
            else:
                if len(base) >= self.d:
                    self.ground_truth(base)
                self.dfs_merged(rest, 0, ex, ey, esz, ox, oy, osz, [], base)
            if self.hit:
                return True
        return self.hit


def smallest_radius_squared(need):
    d = 1
    while 2 ** (d - 1) < need:
        d += 1
    n = 0
    while True:
        n += 1
        if len(lattice_vecs(n)) < 2 * d:
            continue
        if CandidateSearch(n, d, need).run():
            return n


assert smallest_radius_squared(2) == 1     # given: R(2) = 1
assert smallest_radius_squared(4) == 5     # given: R(4) = sqrt(5)
print(smallest_radius_squared(500))  # 6725
