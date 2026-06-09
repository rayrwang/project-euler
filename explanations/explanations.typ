
#set text(font: "Inter")
#set document(
  title: [Project Euler Solutions],
)

#align(center)[
  #title()
  Claude Opus 4.8
]
#outline(depth: 1)

#pagebreak()
#link("https://projecteuler.net/problem=23")[= Problem 23: Non-Abundant Sums]

Solution: 4179871

Sum the positive integers that cannot be written as the sum of two abundant numbers (numbers whose proper divisors sum to more than themselves). Every integer greater than $28123$ can be so written, so that bound is the cap.

Sieve the proper-divisor sums for all $i <= 28123$ (walk each $i$ across its multiples, adding $i$ to each). The abundant numbers are those with divisor-sum exceeding themselves. Mark every $a + b$ for abundant $a <= b$, then add up the integers left unmarked.

#pagebreak()
#link("https://projecteuler.net/problem=32")[= Problem 32: Pandigital Products]

Solution: 45228

Sum the distinct products $c$ for which $a times b = c$ and the three numbers together use each digit $1$–$9$ exactly once. The digit counts can only split as $1 times 4 = 4$ or $2 times 3 = 4$, so the smaller factor is below $100$. Iterate $a$ and $b$, concatenate $a$, $b$ and $a b$, and keep the product whenever those nine characters are exactly ${1, dots, 9}$.

#pagebreak()
#link("https://projecteuler.net/problem=43")[= Problem 43: Sub-string Divisibility]

Solution: 16695334890

Sum the $0$-to-$9$ pandigital numbers whose sliding three-digit windows $d_2 d_3 d_4, d_3 d_4 d_5, dots, d_8 d_9 d_10$ are divisible by $2, 3, 5, 7, 11, 13, 17$ respectively. Instead of testing all $10!$ permutations, build from the right: start with the three-digit multiples of $17$ that have distinct digits, then repeatedly prepend a digit so each new leading window is divisible by the next prime down the list. Finally prepend the one unused digit and sum the results.

#pagebreak()
#link("https://projecteuler.net/problem=51")[= Problem 51: Prime Digit Replacements]

Solution: 121313

Find the smallest prime belonging to an eight-member family formed by replacing one fixed set of digit positions with each value $0$–$9$. Sieve the primes for constant-time tests and, for each prime, try the position masks. Only a mask replacing a number of positions divisible by $3$ can produce eight primes: otherwise, as the replacement digit runs $0$–$9$, the digit sum modulo $3$ cycles and culls too many candidates as multiples of $3$. Return the smallest member of the first eight-family found.

#pagebreak()
#link("https://projecteuler.net/problem=70")[= Problem 70: Totient Permutation]

Solution: 8319823

We want the $n$ with $1 < n < N$, where $N = 10^7$, that minimises the ratio $n / phi(n)$ subject to $phi(n)$ being a digit permutation of $n$.

== Computing every totient at once

Factorising each $n$ on its own is the slow part. Instead we compute $phi$ for every value below $N$ in a single sieve, using the product formula
$
phi(n) = n product_(p divides n) (1 - 1/p).
$
Start with $phi[i] = i$ for all $i$. Sweep $p = 2, 3, 4, dots$; whenever $phi[p]$ is still equal to $p$ its entry has never been modified, so $p$ must be prime. For each such $p$ we fold in the factor $(1 - 1/p)$ across all of its multiples:
$
phi[k] <- phi[k] - phi[k] / p, quad k = p, 2p, 3p, dots
$
After the sweep $phi[i]$ holds $phi(i)$ for every $i < N$. The cost is $O(N log log N)$, versus factorising $N$ numbers separately.

== Searching for the minimum ratio

Two observations keep the search cheap.

First, a digit permutation leaves the digit sum unchanged, and every integer is congruent to its digit sum modulo $9$. So a necessary condition for $phi(n)$ to be a permutation of $n$ is
$
n equiv phi(n) quad ("mod" 9),
$
which rejects roughly $8/9$ of all candidates before any further work. For the survivors we confirm a genuine permutation by tallying digits: increment a length-$10$ array once per digit of $n$, decrement it once per digit of $phi(n)$, and accept only if every entry is back to zero.

Second, the ratios are compared exactly, without floating point. The best ratio so far is kept as a fraction $n_"best" \/ d_"best"$, and a new candidate $n \/ phi(n)$ improves on it precisely when
$
n dot d_"best" < n_"best" dot phi(n),
$
a comparison of two integer products.

The search itself assumes nothing about the form of the answer, but the winner turns out to be $8319823 = 2339 times 3557$, a product of two primes straddling $sqrt(N) approx 3162$. That is exactly where $n / phi(n) = product_(p divides n) p \/ (p-1)$ is smallest: few prime factors, each as large as possible, while still leaving room for $phi(n)$ to be a permutation of $n$.

#pagebreak()
#link("https://projecteuler.net/problem=72")[= Problem 72: Counting Fractions]

Solution: 303963552391

We count the reduced proper fractions $n \/ d$ with $1 <= n < d$, $gcd(n, d) = 1$, and $d <= N$ for $N = 10^6$.

Fix a denominator $d$. The valid numerators are exactly the integers in $[1, d)$ that are coprime to $d$, and the count of those is by definition Euler's totient $phi(d)$. Summing over every denominator gives
$
sum_(d=2)^(N) phi(d).
$
(The denominator $d = 1$ contributes nothing, since $n < d$ leaves no numerator.)

So the whole problem reduces to one totient sieve: build $phi(d)$ for all $d <= N$ with the same $O(N log log N)$ sieve used in Problem 70, then add up the entries from $2$ to $N$.

#pagebreak()
#link("https://projecteuler.net/problem=87")[= Problem 87: Prime Power Triples]

Solution: 1097343

Count the numbers below $5 times 10^7$ expressible as $p^2 + q^3 + r^4$ for primes $p, q, r$. The roots are small ($r <= 84$, $q <= 368$, $p <= 7071$), so sieve the primes once and mark every reachable sum in a boolean array, breaking each loop as soon as the partial sum passes the limit. The answer is the number of distinct marked sums.

#pagebreak()
#link("https://projecteuler.net/problem=95")[= Problem 95: Amicable Chains]

Solution: 14316

Find the smallest member of the longest amicable chain whose every element stays at or below $10^6$ (a chain is $n -> s(n) -> s(s(n)) -> dots -> n$, where $s$ sums proper divisors).

Sieve $s(i)$ for all $i <= 10^6$, then from each start follow the sequence. A walk that drops below the start (its true minimum was already handled) or climbs above $10^6$ is discarded; one that returns to the start is a chain. A generous length cap stops the walk from spinning forever inside a foreign cycle whose minimum exceeds the start. Track the longest.

#pagebreak()
#link("https://projecteuler.net/problem=108")[= Problem 108: Diophantine Reciprocals I]

Solution: 180180

We want the least $n$ for which $1\/x + 1\/y = 1\/n$ (positive integers) has more than $1000$ distinct solutions.

== Counting solutions

Clearing denominators turns $1\/x + 1\/y = 1\/n$ into $x y = n x + n y$, and adding $n^2$ to both sides factors it (Simon's favourite factoring trick):
$
(x - n)(y - n) = n^2.
$
Every factorisation $n^2 = u v$ with $u <= v$ gives a solution $x = n + u$, $y = n + v$, so the number of unordered solutions is
$
(d(n^2) + 1) / 2,
$
where $d$ counts divisors. The $+1$ then halving accounts for the single symmetric pair $u = v = n$. Requiring more than $1000$ solutions means
$
d(n^2) >= 2001.
$

== Finding the smallest such n

Write $n = product_i p_i^(a_i)$. Then $n^2 = product_i p_i^(2 a_i)$ and
$
d(n^2) = product_i (2 a_i + 1).
$
So we need the smallest integer whose exponents satisfy $product (2 a_i + 1) >= 2001$. For a fixed multiset of exponents the product $product p_i^(a_i)$ is smallest when the largest exponents sit on the smallest primes, so it suffices to search exponent tuples that are non-increasing across $2, 3, 5, 7, dots$

A short depth-first search does exactly this: at prime $p_i$ try each exponent $a$ (capped by the previous prime's exponent), divide the remaining divisor target by $(2 a + 1)$, and recurse. The search space is tiny and returns instantly. The minimum is
$
n = 180180 = 2^2 dot 3^2 dot 5 dot 7 dot 11 dot 13, quad d(n^2) = 5 dot 5 dot 3 dot 3 dot 3 dot 3 = 2025,
$
giving $(2025 + 1)\/2 = 1013$ solutions.

#pagebreak()
#link("https://projecteuler.net/problem=118")[= Problem 118: Pandigital Prime Sets]

Solution: 44680

We count the distinct sets of primes whose digits, taken together, are exactly $1, 2, dots, 9$ each used once (for example ${2, 5, 47, 89, 631}$).

== Two stages: count, then combine

Such a set is a partition of the nine digits into blocks, where each block's digits are arranged into a prime. Crucially, a set of primes determines its own partition (group the primes by which digits they use), so we may count

#h(1em) (set partitions of ${1, dots, 9}$) $times$ (a prime arrangement chosen per block)

without any risk of double counting, as long as each partition is enumerated once.

== Stage 1 — primes per digit subset

For every non-empty subset $S$ of the digits, let $f(S)$ be the number of permutations of $S$ that are prime. Two cheap rules cut the work sharply:
- if $abs(S) > 1$ and the digit sum of $S$ is divisible by $3$, then every arrangement is divisible by $3$, so $f(S) = 0$;
- a prime longer than one digit must end in $1, 3, 7$ or $9$, so only those arrangements are tested.

We store $f(S)$ for all $511$ subsets, indexing each subset by a $9$-bit mask.

== Stage 2 — combining blocks

Let $g(M)$ be the number of distinct prime sets using exactly the digits in mask $M$. Splitting off the block that contains the lowest set bit makes every partition unique:
$
g(M) = sum_(B subset.eq M, ell in B) f(B) dot g(M without B), quad g(0) = 1,
$
where $ell$ is the lowest set bit of $M$ and $B$ ranges over sub-masks containing it. Enumerating sub-masks costs $O(3^9)$ overall. The answer is $g$ of the full mask, $g(111111111_2) = 44680$.

#pagebreak()
#link("https://projecteuler.net/problem=125")[= Problem 125: Palindromic Sums]

Solution: 2906969179

Sum the palindromes below $10^8$ that can be written as a sum of two or more consecutive squares. Rather than test every number, generate the sums: for each starting base accumulate consecutive squares until the running total reaches $10^8$, recording each palindromic total in a set so that a number expressible in several ways is still counted once. Sum the set.

#pagebreak()
#link("https://projecteuler.net/problem=145")[= Problem 145: Reversible Numbers]

Solution: 608720

A number $n$ is _reversible_ if $n + "reverse"(n)$ has only odd decimal digits, with no leading zero in either $n$ or $"reverse"(n)$. We count reversible $n < 10^9$.

Instead of testing a billion numbers, count by digit length $d$. Write the digits of $n$ as $a_1 a_2 dots a_d$. When $n$ and $"reverse"(n)$ are added, column $j$ (counting from the right) always pairs the same two digits, $a_j + a_(d+1-j)$, so the column sums are symmetric. Let $S_j = a_j + a_(d+1-j)$, and let carries propagate right to left.

== Even length $d$

The units column gives $a_1 + a_d = S_1$; for that output digit to be odd, $S_1$ must be odd. The top column outputs $S_1 + c$ where $c$ is its incoming carry; since $S_1$ is already odd, $c$ must be even, i.e. $0$. Pushing this inward forces *every* column sum to be odd and below $10$, so there are no carries anywhere. Counting digit pairs $(x, y)$ with $x + y$ odd and $x + y < 10$:
- the outer pair needs $x, y >= 1$ (no leading zeros): $20$ choices;
- each of the remaining $d\/2 - 1$ pairs allows a zero: $30$ choices each.

So an even length contributes $20 dot 30^(d\/2 - 1)$.

== Odd length $d$

Now there is a middle column that adds a digit to itself, $2 a_m$, which is even. Its output can only be odd if a carry of $1$ arrives from the right. That single required carry cannot coexist with the carry-free pattern above unless the lengths line up: the consistency of the inward and outward carries closes only when $d equiv 3 space ("mod" 4)$. Those lengths contribute $100 dot 500^((d-3)\/4)$ (for $d = 3$ this is the $a_1 + a_d in {11, 13, 15, 17}$ outer pair, $20$ ways, times the $5$ middle digits $0..4$, giving $100$); lengths with $d equiv 1 space ("mod" 4)$ contribute nothing.

== Total

Summing over $d = 1, dots, 9$ (the digit lengths below $10^9$):
$
underbrace(20 + 600 + 18000 + 540000, "even") + underbrace(100 + 50000, d equiv 3) = 608720.
$
A direct brute-force count confirms each per-length value (for instance $120$ reversible numbers below $1000$).

#pagebreak()
#link("https://projecteuler.net/problem=173")[= Problem 173: Square Laminae]

Solution: 1572729

Count the square laminae (hollow square frames) that can be built with at most $10^6$ tiles. A frame of outer width $a$ and hole width $b$ (same parity, $b < a$) uses $a^2 - b^2$ tiles. For each $a$, start from the widest hole $b = a - 2$ and shrink it; the tile count rises monotonically, so stop the moment it exceeds $10^6$. The outer loop ends once even the thinnest frame, costing $4a - 4$ tiles, no longer fits.

#pagebreak()
#link("https://projecteuler.net/problem=179")[= Problem 179: Consecutive Positive Divisors]

Solution: 986262

We count integers $1 < n < 10^7$ for which $n$ and $n + 1$ have the same number of divisors.

Computing $d(n)$ by factorising each $n$ is wasteful. Instead sieve all divisor counts at once: for every $i$ from $1$ to $N$, walk its multiples $i, 2i, 3i, dots$ and add one to each, since $i$ divides every one of them. After the sweep $d[k]$ holds the divisor count of $k$. The work is the harmonic sum
$
sum_(i=1)^N N/i approx N ln N,
$
versus a per-number factorisation. A compact `int32` array keeps the strided increments cache-friendly.

Then a single linear scan counts the positions where $d[n] = d[n+1]$ for $2 <= n <= N - 1$, giving $986262$.

#pagebreak()
#link("https://projecteuler.net/problem=187")[= Problem 187: Semiprimes]

Solution: 17427258

We count the composite numbers $n < N$ (with $N = 10^8$) that are a product of exactly two primes, $n = p q$ with $p <= q$.

Writing each such $n$ with its smaller factor first makes the count a sum over $p$: for a fixed prime $p$, the partners are the primes $q$ with $p <= q$ and $p q < N$, i.e. $p <= q <= floor((N - 1) \/ p)$. Counting unordered pairs this way (insisting $q >= p$) visits each semiprime once. Only primes with $p^2 < N$, that is $p < sqrt(N) approx 10^4$, can be the smaller factor, so there are barely more than a thousand outer terms.

The largest partner occurs at $p = 2$, where $q$ can reach $(N-1)\/2$, so we sieve every prime up to $N\/2$ once. For each small prime $p$ a binary search in that sorted list returns the number of primes up to $floor((N-1)\/p)$; subtracting the primes below $p$ leaves the count of valid $q$. Summing gives $17427258$ (and $10$ below $30$, matching the example).

#pagebreak()
#link("https://projecteuler.net/problem=203")[= Problem 203: Squarefree Binomial Coefficients]

Solution: 34029210557338

Sum the distinct squarefree entries in the first $51$ rows of Pascal's triangle. The key fact is that every prime factor of $binom(n, k)$ with $n <= 50$ is at most $n$, so squarefreeness only needs testing against the primes up to $47$ — the large binomials themselves never have to be factored. Collect the distinct values from the left half of each row (using $binom(n, k) = binom(n, n - k)$) and add those divisible by no $p^2$.

#pagebreak()
#link("https://projecteuler.net/problem=315")[= Problem 315: Digital Root Clocks]

Solution: 13625242

Two seven-segment clocks each display a number, then repeatedly its digit sum down to a single digit, beginning and ending blank. Sam's clock clears and relights every segment at each step; Max's only toggles the segments that change. The answer is Sam's total segment transitions minus Max's, summed over the primes in $[10^7, 2 dot 10^7)$.

Sieve that prime range rather than testing each number for primality, and compute both transition counts per prime with integer digit arithmetic. For a step $a -> b$, Sam's cost is the total lit-segment count of $a$ plus that of $b$, while Max's cost is the sum over aligned digit positions of the population count of the segment-pattern XOR (a blank screen contributing the all-off pattern).

#pagebreak()
#link("https://projecteuler.net/problem=347")[= Problem 347: Largest Integer Divisible by Two Primes]

Solution: 11109800204052

For distinct primes $p, q$ let $M(p, q, N)$ be the largest integer $<= N$ whose only prime factors are $p$ and $q$ (so $M = p^a q^b$ with $a, b >= 1$), or $0$ if none exists. $S(N)$ sums all the distinct values; we need $S(10^7)$.

Each value $p^a q^b$ has a unique prime pair, so summing distinct values is the same as summing $M(p, q, N)$ over the pairs themselves. Iterating $n$ and factorising it is wasteful; instead iterate the pairs. A valid pair needs $p q <= N$, and since $p < q$ this forces $p < sqrt(N)$, so only a few hundred primes can be the smaller factor. Sieve the primes up to $N\/2$ (the largest a factor can be, paired with $2$), then loop $p$ over primes below $sqrt(N)$ and $q$ over larger primes while $p q <= N$.

For a fixed pair, $M$ is found by trying each power $p^a$ with $p^a q <= N$ and, for each, taking the largest power $q^b <= N \/ p^a$; the maximum product over all $a$ is $M(p, q, N)$. Summing gives $S(100) = 2262$ as a check and $S(10^7) = 11109800204052$.

#pagebreak()
#link("https://projecteuler.net/problem=348")[= Problem 348: Sum of a Square and a Cube]

Solution: 1004195061

We want the five smallest palindromes expressible as $a^2 + b^3$, with $a, b > 1$, in *exactly* four ways, and their sum.

The naive route, testing every integer for palindromicity, wastes almost all of its time: only about $10^5$ palindromes lie below $10^9$. So we generate palindromes directly and in increasing order. A palindrome is fixed by its first half: mirror a root $r$ of $h$ digits to get an even-length palindrome $r dot 10^h + "reverse"(r)$, or mirror $r$ minus its last digit for odd length. Iterating length upward, and root upward within each length, yields every palindrome in ascending order, so the first five that qualify are the smallest five.

For each palindrome $p$ we count the representations by trying every cube $b^3$ with $b >= 2$ and $b^3 + 4 <= p$ (the $+4$ leaves room for $a^2 >= 2^2$), and testing whether the remainder $p - b^3$ is a perfect square. Because the remainder is at least $4$, its root is automatically $>= 2$, so both parts exceed $1$ as required. Each palindrome costs $O(p^(1\/3))$ checks, and we keep only those with a count of exactly four.

The qualifying palindromes are $5229225$ (the example), $37088073$, $56200265$, $108909801$ and $796767697$, summing to $1004195061$.

#pagebreak()
#link("https://projecteuler.net/problem=357")[= Problem 357: Prime Generating Integers]

Solution: 1739023853137

Sum the integers $n <= 10^8$ for which $d + n\/d$ is prime for every divisor $d$ of $n$. Taking $d = 1$ forces $n + 1$ to be prime, so $n$ is even and the only candidates are $n = p - 1$ for primes $p$. Sieve the primes up to $10^8$ for constant-time primality tests, then for each candidate check the divisor pairs with $d <= sqrt(n)$ (the condition is symmetric in $d$ and $n\/d$), bailing out at the first failure — usually already at $d = 2$.

#pagebreak()
#link("https://projecteuler.net/problem=587")[= Problem 587: Concave Triangle]

Solution: 2240

Let the bottom-left of the rectangle be at $(0, 0)$ and the circles to have radius $1$.

The area of the L-section is $1 - pi/4$.

The diagonal line has slope $1/n$, and the intersection of the line with the first circle has coordinate:

$
x = (-sqrt(2) dot n^(3/2) + n^2 + n) / (n^2 + 1) \
y = x / n
$

The concave triangle can be split into a triangle and a curved section.

The area of the triangle is $"TriangleArea" = 1/2 x y$.

Let:
$
"CircleInt"(a, b) &= integral_a^b (sqrt(1-x^2)) dif x \
&= lr(1/2 (x sqrt(1-x^2) + sin^(-1)(x)) bar)_a^b
$

Then the area of the curved section is $"SectionArea" = (1-x) - "CircleInt"(0, 1-x)$.

And so the ratio is:
$
("TriangleArea" + "SectionArea") / (1-pi/4)
$

#pagebreak()
#link("https://projecteuler.net/problem=719")[= Problem 719: Number Splitting]

Solution: 128088830547982

An _S-number_ is a perfect square $n$ whose decimal digits can be cut into two or more contiguous blocks that add up to $sqrt(n)$ (for example $6724$, since $6 + 72 + 4 = 82 = sqrt(6724)$). We want $T(N) = sum_(n <= N, n "is an S-number") n$ for $N = 10^12$.

Rather than scan every $n$, iterate over the root $r$ from $2$ to $sqrt(N) = 10^6$ and test whether $r^2$ splits to $r$. The test is a pruned recursion. Splitting a number can only lower its value-sum (the maximum, one block, is the number itself), so for a target $t$ and remaining number $m$:
- if $m < t$ it is impossible;
- if $m = t$ the remaining number is itself the final block, success;
- otherwise peel off a trailing block $r = m mod 10^k$, and if $r < t$ recurse on the prefix $floor(m \/ 10^k)$ with target $t - r$.

The trailing-block extraction handles blocks with leading zeros automatically (so $9801 = 98 + 0 + 1$ is found). Because $r^2 != r$ for $r >= 2$, any successful split uses at least two blocks, as required. As a check, $T(10^4) = 41333$.

#pagebreak()
#link("https://projecteuler.net/problem=788")[= Problem 788: Dominating Numbers]

Solution: 471745499

A number is _dominating_ when one digit value occupies more than half of its places (for example $2022$, where three of four digits are $2$). Let $D(N)$ count dominating numbers below $10^N$; we need $D(2022) mod (10^9 + 7)$.

== Counting by length

Fix a digit length $d$. If a value $v$ fills more than half the $d$ places then no other value can also exceed half, so each dominating number has a *unique* dominant value. We may therefore sum over the count $k$ of that value with $k > d\/2$ and never double count.

For a fixed value $v$ appearing exactly $k$ times the placements split by whether $v$ is the leading digit, and there is a separate correction for the leading-zero rule when $v = 0$. Writing all of that out and summing over the ten possible values, the corrections cancel and leave a compact form:
$
A(d) = sum_(k > d\/2) binom(d, k) dot 9^(d - k + 1),
$
the number of dominating numbers with exactly $d$ digits. Then $D(N) = sum_(d=1)^(N) A(d)$. As a check, $D(4) = 603$ and $D(10) = 21893256$, matching the problem.

== Evaluating modulo $10^9 + 7$

The earlier approach evaluated $binom(d, k)$ and $9^(d-k+1)$ as exact integers; at $d approx 2000$ those are numbers with hundreds to thousands of digits, which is slow. Working modulo the prime $p = 10^9 + 7$ keeps every value small: precompute factorials and their modular inverses (via Fermat's little theorem) up to $N$, and the powers of $9$ up to $N + 1$. The double sum is then $O(N^2)$ cheap modular multiplications, giving $D(2022) equiv 471745499 space (mod p)$.

#pagebreak()
#link("https://projecteuler.net/problem=808")[= Problem 808: Reversible Prime Squares]

Solution: 3807504276997394

A reversible prime square is the square of a prime that is not a palindrome and whose digit reversal is also the square of a prime. Because squares grow with their root, iterating primes in increasing order yields these in increasing order too. Sieve primes up to about $3.2 dot 10^7$ (where the fiftieth occurs); for each prime $p$, reverse $p^2$, and if the reversal is a perfect square whose root is prime, count $p^2$. Stop at the fiftieth and sum.

#pagebreak()
#link("https://projecteuler.net/problem=932")[= Problem 932: $2025$]

Solution: 72673459417881349

Let $d$ be the number of digits in $b$. We have:
$
10^d a + b = (a+b)^2 \
b^2 + (2a - 1)b + a^2 - 10^d a = 0 \
b = (1 - 2a + sqrt(4 dot 10^d a - 4a + 1)) / 2
$

Similarly:
$
a = ((10^d - 2b) + sqrt(10^(2d) - 4 dot 10^d b + 4b)) / 2
$

Then search through the numbers up to half of the required length, where the corresponding other number is obtained using the formulas.
