
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
