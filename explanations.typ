
#set text(font: "Inter")
#set document(
  title: [Project Euler Solutions],
)

#align(center)[
  #title()
  Claude Fable 5
]
#outline(depth: 1)

#pagebreak()
#link("https://projecteuler.net/problem=1")[= Problem 1: Multiples of 3 or 5]

Solution: 233168

Add the integers below $1000$ that are divisible by $3$ or by $5$, looping once and testing each.

#pagebreak()
#link("https://projecteuler.net/problem=2")[= Problem 2: Even Fibonacci Numbers]

Solution: 4613732

Generate Fibonacci numbers up to four million and sum the even ones.

#pagebreak()
#link("https://projecteuler.net/problem=3")[= Problem 3: Largest Prime Factor]

Solution: 6857

Factorise $600851475143$ by trial division and take the largest prime factor.

#pagebreak()
#link("https://projecteuler.net/problem=4")[= Problem 4: Largest Palindrome Product]

Solution: 906609

Check every product of two three-digit numbers and keep the largest that reads the same in reverse.

#pagebreak()
#link("https://projecteuler.net/problem=5")[= Problem 5: Smallest Multiple]

Solution: 232792560

Scan upward for the first number divisible by every integer from $2$ to $20$.

#pagebreak()
#link("https://projecteuler.net/problem=6")[= Problem 6: Sum Square Difference]

Solution: 25164150

Subtract the sum of the squares of $1$ to $100$ from the square of their sum, using $5050$ for the latter.

#pagebreak()
#link("https://projecteuler.net/problem=7")[= Problem 7: 10001st Prime]

Solution: 104743

Step through the odd numbers, testing primality, until the $10001$st prime is reached.

#pagebreak()
#link("https://projecteuler.net/problem=8")[= Problem 8: Largest Product in a Series]

Solution: 23514624000

Slide a window of thirteen digits across the given $1000$-digit number and take the largest product.

#pagebreak()
#link("https://projecteuler.net/problem=9")[= Problem 9: Special Pythagorean Triplet]

Solution: 31875000

Search for $a + b + c = 1000$ with $a^2 + b^2 = c^2$ and return the product $a b c$.

#pagebreak()
#link("https://projecteuler.net/problem=10")[= Problem 10: Summation of Primes]

Solution: 142913828922

Sum every prime below two million using a sieve.

#pagebreak()
#link("https://projecteuler.net/problem=11")[= Problem 11: Largest Product in a Grid]

Solution: 70600674

For each cell and each of the eight directions, multiply four adjacent entries and keep the maximum.

#pagebreak()
#link("https://projecteuler.net/problem=12")[= Problem 12: Highly Divisible Triangular Number]

Solution: 76576500

Generate triangular numbers until one has more than $500$ divisors.

#pagebreak()
#link("https://projecteuler.net/problem=13")[= Problem 13: Large Sum]

Solution: 5537376230

Add the fifty fifty-digit numbers and report the first ten digits.

#pagebreak()
#link("https://projecteuler.net/problem=14")[= Problem 14: Longest Collatz Sequence]

Solution: 837799

Compute the Collatz chain length for every start below one million and report the longest.

#pagebreak()
#link("https://projecteuler.net/problem=15")[= Problem 15: Lattice Paths]

Solution: 137846528820

The monotonic routes through a $20 times 20$ grid number $binom(40, 20)$.

#pagebreak()
#link("https://projecteuler.net/problem=16")[= Problem 16: Power Digit Sum]

Solution: 1366

Sum the decimal digits of $2^1000$.

#pagebreak()
#link("https://projecteuler.net/problem=17")[= Problem 17: Number Letter Counts]

Solution: 21124

Count the letters used to spell every number from $1$ to $1000$, using small per-range letter tables (with the British "and").

#pagebreak()
#link("https://projecteuler.net/problem=18")[= Problem 18: Maximum Path Sum I]

Solution: 1074

Work up the triangle from the bottom: each cell takes its value plus the larger of the two cells below, leaving the answer at the apex.

#pagebreak()
#link("https://projecteuler.net/problem=19")[= Problem 19: Counting Sundays]

Solution: 171

Walk a running day count month by month from $1901$ to $2000$, counting the months that begin on a Sunday.

#pagebreak()
#link("https://projecteuler.net/problem=20")[= Problem 20: Factorial Digit Sum]

Solution: 648

Sum the decimal digits of $100!$.

#pagebreak()
#link("https://projecteuler.net/problem=21")[= Problem 21: Amicable Numbers]

Solution: 31626

Sum the amicable numbers below $10000$, where $d(a)$ is the proper-divisor sum and $a != d(a) = b$ with $d(b) = a$.

#pagebreak()
#link("https://projecteuler.net/problem=22")[= Problem 22: Names Scores]

Solution: 871198282

Sort the names alphabetically, then sum each name's position times its alphabetical letter value.

#pagebreak()
#link("https://projecteuler.net/problem=23")[= Problem 23: Non-Abundant Sums]

Solution: 4179871

Sum the positive integers that cannot be written as the sum of two abundant numbers (numbers whose proper divisors sum to more than themselves). Every integer greater than $28123$ can be so written, so that bound is the cap.

Sieve the proper-divisor sums for all $i <= 28123$ (walk each $i$ across its multiples, adding $i$ to each). The abundant numbers are those with divisor-sum exceeding themselves. Mark every $a + b$ for abundant $a <= b$, then add up the integers left unmarked.

#pagebreak()
#link("https://projecteuler.net/problem=24")[= Problem 24: Lexicographic Permutations]

Solution: 2783915460

Generate the permutations of the digits $0$ to $9$ in lexicographic order and take the millionth.

#pagebreak()
#link("https://projecteuler.net/problem=25")[= Problem 25: 1000-digit Fibonacci Number]

Solution: 4782

Find the index of the first Fibonacci number with one thousand digits.

#pagebreak()
#link("https://projecteuler.net/problem=26")[= Problem 26: Reciprocal Cycles]

Solution: 983

For each denominator below $1000$, run long division while tracking remainders; the recurring cycle length is found by the first repeated remainder. Report the longest.

#pagebreak()
#link("https://projecteuler.net/problem=27")[= Problem 27: Quadratic Primes]

Solution: -59231

Search coefficients $a, b in (-1000, 1000)$ for the quadratic $n^2 + a n + b$ that produces the longest run of primes from $n = 0$, returning $a b$.

#pagebreak()
#link("https://projecteuler.net/problem=28")[= Problem 28: Number Spiral Diagonals]

Solution: 669171001

Sum the diagonals of a $1001 times 1001$ spiral using the closed form for each ring's four corners.

#pagebreak()
#link("https://projecteuler.net/problem=29")[= Problem 29: Distinct Powers]

Solution: 9183

Count the distinct values $a^b$ for $2 <= a, b <= 100$ with a set.

#pagebreak()
#link("https://projecteuler.net/problem=30")[= Problem 30: Digit Fifth Powers]

Solution: 443839

Sum the numbers equal to the sum of the fifth powers of their digits (the search bound is $6 dot 9^5$).

#pagebreak()
#link("https://projecteuler.net/problem=31")[= Problem 31: Coin Sums]

Solution: 73682

Count the ways to make two pounds from the coin denominations by recursing over the coin list.

#pagebreak()
#link("https://projecteuler.net/problem=32")[= Problem 32: Pandigital Products]

Solution: 45228

Sum the distinct products $c$ for which $a times b = c$ and the three numbers together use each digit $1$–$9$ exactly once. The digit counts can only split as $1 times 4 = 4$ or $2 times 3 = 4$, so the smaller factor is below $100$. Iterate $a$ and $b$, concatenate $a$, $b$ and $a b$, and keep the product whenever those nine characters are exactly ${1, dots, 9}$.

#pagebreak()
#link("https://projecteuler.net/problem=33")[= Problem 33: Digit Cancelling Fractions]

Solution: 100

Find the non-trivial two-digit fractions whose value is unchanged by cancelling a shared digit, and reduce the product of the four.

#pagebreak()
#link("https://projecteuler.net/problem=34")[= Problem 34: Digit Factorials]

Solution: 40730

Sum the numbers equal to the sum of the factorials of their digits.

#pagebreak()
#link("https://projecteuler.net/problem=35")[= Problem 35: Circular Primes]

Solution: 55

Count the primes below one million for which every digit rotation is also prime.

#pagebreak()
#link("https://projecteuler.net/problem=36")[= Problem 36: Double-base Palindromes]

Solution: 872187

Sum the numbers below one million that are palindromic in both base ten and base two.

#pagebreak()
#link("https://projecteuler.net/problem=37")[= Problem 37: Truncatable Primes]

Solution: 748317

Find the eleven primes that remain prime as digits are stripped from the left and from the right.

#pagebreak()
#link("https://projecteuler.net/problem=38")[= Problem 38: Pandigital Multiples]

Solution: 932718654

Search for the largest $1$ to $9$ pandigital formed by concatenating $n, 2n, dots$ for some integer.

#pagebreak()
#link("https://projecteuler.net/problem=39")[= Problem 39: Integer Right Triangles]

Solution: 840

For perimeters up to $1000$, count integer right-triangle solutions and report the perimeter with the most.

#pagebreak()
#link("https://projecteuler.net/problem=40")[= Problem 40: Champernowne's Constant]

Solution: 210

Concatenating the positive integers gives $0.123456789101112dots$; the task is the product of the digits at positions $1, 10, 100, dots, 10^6$. Building a string of a million digits is unnecessary. The $c$-digit numbers form a block of $9 dot 10^(c-1)$ numbers contributing $c dot 9 dot 10^(c-1)$ digits, so subtract whole blocks from the target position until it lands inside the $c$-digit block. The number holding it is then $10^(c-1) + floor((n - 1) \/ c)$ and the wanted digit is at offset $(n - 1) mod c$. The seven digits are $1, 1, 5, 3, 7, 2, 1$, whose product is $210$.

#pagebreak()
#link("https://projecteuler.net/problem=41")[= Problem 41: Pandigital Prime]

Solution: 7652413

Test the permutations using digits $1$ to $n$ for primality and keep the largest prime.

#pagebreak()
#link("https://projecteuler.net/problem=42")[= Problem 42: Coded Triangle Numbers]

Solution: 162

A word's letter value is triangular exactly when $1 + 8 v$ is a perfect square (for value $v$); count the words that qualify.

#pagebreak()
#link("https://projecteuler.net/problem=43")[= Problem 43: Sub-string Divisibility]

Solution: 16695334890

Sum the $0$-to-$9$ pandigital numbers whose sliding three-digit windows $d_2 d_3 d_4, d_3 d_4 d_5, dots, d_8 d_9 d_10$ are divisible by $2, 3, 5, 7, 11, 13, 17$ respectively. Instead of testing all $10!$ permutations, build from the right: start with the three-digit multiples of $17$ that have distinct digits, then repeatedly prepend a digit so each new leading window is divisible by the next prime down the list. Finally prepend the one unused digit and sum the results.

#pagebreak()
#link("https://projecteuler.net/problem=44")[= Problem 44: Pentagon Numbers]

Solution: 5482660

Search pairs of pentagonal numbers whose sum and difference are both pentagonal, minimising the difference, using the inverse formula to test pentagonality.

#pagebreak()
#link("https://projecteuler.net/problem=45")[= Problem 45: Triangular, Pentagonal, and Hexagonal]

Solution: 1533776805

Find the next number after $40755$ that is simultaneously triangular, pentagonal, and hexagonal. The triangular condition comes for free: $H_n = n(2n - 1) = (2n - 1)(2n)\/2 = T_(2n-1)$, so every hexagonal number is already triangular. It therefore suffices to walk the hexagonal numbers (starting just past $H_143 = 40755$) and test each for pentagonality, which holds when $1 + 24 H$ is a perfect square whose root, increased by one, is divisible by $6$. The first hit is $1533776805$.

#pagebreak()
#link("https://projecteuler.net/problem=46")[= Problem 46: Goldbach's Other Conjecture]

Solution: 5777

Find the smallest odd composite that cannot be written as a prime plus twice a square.

#pagebreak()
#link("https://projecteuler.net/problem=47")[= Problem 47: Distinct Primes Factors]

Solution: 134043

Find the first run of four consecutive integers each having exactly four distinct prime factors.

#pagebreak()
#link("https://projecteuler.net/problem=48")[= Problem 48: Self Powers]

Solution: 9110846700

Sum $1^1 + 2^2 + dots + 1000^1000$ and report the last ten digits.

#pagebreak()
#link("https://projecteuler.net/problem=49")[= Problem 49: Prime Permutations]

Solution: 296962999629

Find the arithmetic progression of three four-digit primes that are digit permutations of one another, other than the given $1487$ case.

#pagebreak()
#link("https://projecteuler.net/problem=50")[= Problem 50: Consecutive Prime Sum]

Solution: 997651

Track running sums of consecutive primes below one million and report the prime that is the longest such sum.

#pagebreak()
#link("https://projecteuler.net/problem=51")[= Problem 51: Prime Digit Replacements]

Solution: 121313

Find the smallest prime belonging to an eight-member family formed by replacing one fixed set of digit positions with each value $0$–$9$. Sieve the primes for constant-time tests and, for each prime, try the position masks. Only a mask replacing a number of positions divisible by $3$ can produce eight primes: otherwise, as the replacement digit runs $0$–$9$, the digit sum modulo $3$ cycles and culls too many candidates as multiples of $3$. Return the smallest member of the first eight-family found.

#pagebreak()
#link("https://projecteuler.net/problem=52")[= Problem 52: Permuted Multiples]

Solution: 142857

Find the smallest $x$ whose multiples $2x$ through $6x$ are all digit permutations of $x$.

#pagebreak()
#link("https://projecteuler.net/problem=53")[= Problem 53: Combinatoric Selections]

Solution: 4075

Count the binomial coefficients $binom(n, r)$ with $n <= 100$ that exceed one million.

#pagebreak()
#link("https://projecteuler.net/problem=54")[= Problem 54: Poker Hands]

Solution: 376

Given a thousand pairs of five-card hands, count how often the first player wins. Rather than encode poker's branching rules with nested comparisons and kicker logic, collapse each hand into one comparable key $("category", "tiebreak")$. The category is the usual ranking (straight flush down to high card), read off from whether the hand is a flush, a straight, and from the sorted pattern of rank multiplicities ($[4,1], [3,2], [3,1,1], dots$). The tiebreak is the list of card values ordered by frequency first and value second, so that quads, trips, and pairs float to the front; ordinary tuple comparison then resolves every kicker for free. Comparing the two keys with a single $>$ gives the winner, and the first player takes $376$ hands.

#pagebreak()
#link("https://projecteuler.net/problem=55")[= Problem 55: Lychrel Numbers]

Solution: 249

Count the numbers below $10000$ that fail to produce a palindrome within fifty reverse-and-add steps.

#pagebreak()
#link("https://projecteuler.net/problem=56")[= Problem 56: Powerful Digit Sum]

Solution: 972

Maximise the digit sum of $a^b$ over $a, b < 100$.

#pagebreak()
#link("https://projecteuler.net/problem=57")[= Problem 57: Square Root Convergents]

Solution: 153

Iterate the continued-fraction convergents of $sqrt(2)$ and count those whose numerator has more digits than the denominator.

#pagebreak()
#link("https://projecteuler.net/problem=58")[= Problem 58: Spiral Primes]

Solution: 26241

Grow the diagonals of a number spiral until the proportion of prime diagonal entries falls below ten percent.

#pagebreak()
#link("https://projecteuler.net/problem=59")[= Problem 59: XOR Decryption]

Solution: 129448

The ciphertext was XOR-encrypted with a repeating three-letter key; recover the key and sum the decrypted byte values. Brute-forcing all $26^3$ keys and judging which output "looks like English" is avoidable. Since the key has length three, the message is really three independent streams, each XOR-ed by a single byte. The most common character in English text is the space ($32$), so within each stream the most frequent ciphertext byte is an encrypted space, and the key byte is simply that value XOR $32$. Three frequency counts recover the key (it spells $"exp"$) with no searching; decrypting and summing gives $129448$.

#pagebreak()
#link("https://projecteuler.net/problem=60")[= Problem 60: Prime Pair Sets]

Solution: 26033

Find five primes for which concatenating any two (in either order) is also prime, minimising their sum. This is a minimum-weight $5$-clique search in the graph whose edges join compatible primes, which two ideas tame. First, a residue filter: concatenating $p$ and $q$ gives $p dot 10^k + q equiv p + q space (mod 3)$, so unless a prime equals $3$, every prime in the set must share one residue mod $3$; the search therefore runs separately within each residue class. Second, a sum bound: exploring each class in increasing order, a partial clique is abandoned as soon as adding the next (and hence every later) prime would reach the best sum found so far. The minimal set is ${13, 5197, 5701, 6733, 8389}$, summing to $26033$.

#pagebreak()
#link("https://projecteuler.net/problem=61")[= Problem 61: Cyclical Figurate Numbers]

Solution: 28684

Find the six four-digit numbers — one triangular, one square, one pentagonal, one hexagonal, one heptagonal, one octagonal — that form a cycle in which each number's last two digits are the next's first two, with the cycle closing back to the start. Generate the four-digit numbers of each type and index them by leading two digits, so the overlap constraint becomes an instant lookup. A depth-six search then assigns one number per type, at each step only following numbers whose first two digits match the previous number's last two; the constraint is tight enough that the tree barely branches. Anchoring on the octagonal numbers fixes the cycle's rotation. The unique ring is $1281, 8128, 2882, 8256, 5625, 2512$, summing to $28684$.

#pagebreak()
#link("https://projecteuler.net/problem=62")[= Problem 62: Cubic Permutations]

Solution: 127035954683

Group cubes by their sorted digits and find the smallest cube belonging to a group of exactly five digit-permutation cubes.

#pagebreak()
#link("https://projecteuler.net/problem=63")[= Problem 63: Powerful Digit Counts]

Solution: 49

Count the $n$-digit positive integers that are also $n$th powers.

#pagebreak()
#link("https://projecteuler.net/problem=64")[= Problem 64: Odd Period Square Roots]

Solution: 1322

Count the $n <= 10000$ whose continued fraction for $sqrt(n)$ has an odd period. No decimal expansion is needed: the continued fraction of a quadratic irrational is generated exactly by an integer recurrence. Starting from $a_0 = floor(sqrt(n))$, $m_0 = 0$, $d_0 = 1$, iterate
$
m_(k+1) = d_k a_k - m_k, quad d_(k+1) = (n - m_(k+1)^2) \/ d_k, quad a_(k+1) = floor((a_0 + m_(k+1)) \/ d_(k+1)).
$
The period always closes exactly when a term equals $2 a_0$, so counting the steps to that point gives the period length (perfect squares having none). Of the non-squares up to $10000$, $1322$ have an odd period.

#pagebreak()
#link("https://projecteuler.net/problem=65")[= Problem 65: Convergents of e]

Solution: 272

Build the hundredth convergent of the continued fraction for $e$ and sum the digits of its numerator.

#pagebreak()
#link("https://projecteuler.net/problem=66")[= Problem 66: Diophantine Equation]

Solution: 661

For each non-square $D <= 1000$, the equation $x^2 - D y^2 = 1$ (Pell's equation) has a smallest positive solution; find the $D$ whose minimal $x$ is largest. These minimal solutions can be astronomically large (for $D = 661$ the value of $x$ has $26$ digits), so no direct search works. Instead the fundamental solution sits among the convergents $h\/k$ of the continued fraction of $sqrt(D)$: running the same exact integer recurrence as Problem 64 while accumulating convergents via $h_i = a_i h_(i-1) + h_(i-2)$ and $k_i = a_i k_(i-1) + k_(i-2)$, the first convergent satisfying $h^2 - D k^2 = 1$ gives the minimal $x$. Scanning $D$ up to $1000$, the largest minimal solution occurs at $D = 661$.

#pagebreak()
#link("https://projecteuler.net/problem=67")[= Problem 67: Maximum Path Sum II]

Solution: 7273

The same bottom-up dynamic programming as Problem 18, applied to the hundred-row triangle read from file.

#pagebreak()
#link("https://projecteuler.net/problem=68")[= Problem 68: Magic 5-gon Ring]

Solution: 6531031914842725

Arrange $1$ to $10$ on a five-pointed ring (five outer nodes, five inner) so that every line — one outer node plus two adjacent inner nodes — has the same total, then read the lines off as a string starting from the lowest outer node. Find the maximum $16$-digit string. Two observations remove the search. A $16$- rather than $17$-digit string forces the two-digit $10$ onto an outer node (outer nodes appear once in the string, inner nodes twice). To maximise a string that begins at the smallest outer node, the outer ring must be the five largest values ${6,7,8,9,10}$ and the inner pentagon ${1,2,3,4,5}$; the common line total is then forced to $("sum outer") + 2("sum inner") = 70 = 5 dot 14$. Each outer value is therefore determined by the inner arrangement, $"outer"_j = 14 - "inner"_j - "inner"_(j+1)$, so it suffices to try the $120$ inner pentagons, keep those whose outers are exactly ${6,dots,10}$, and take the largest string: $6531031914842725$.

#pagebreak()
#link("https://projecteuler.net/problem=69")[= Problem 69: Totient Maximum]

Solution: 510510

Maximise $n\/phi(n)$ for $n <= 10^6$; the optimum is the primorial $510510$.

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
#link("https://projecteuler.net/problem=71")[= Problem 71: Ordered Fractions]

Solution: 428570

Scan denominators up to one million for the reduced fraction immediately below $3\/7$.

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
#link("https://projecteuler.net/problem=73")[= Problem 73: Counting Fractions in a Range]

Solution: 7295372

Count the reduced fractions strictly between $1\/3$ and $1\/2$ with denominator at most $12000$.

#pagebreak()
#link("https://projecteuler.net/problem=74")[= Problem 74: Digit Factorial Chains]

Solution: 402

Count the starting numbers below one million whose digit-factorial chain has exactly sixty non-repeating terms.

#pagebreak()
#link("https://projecteuler.net/problem=75")[= Problem 75: Singular Integer Right Triangles]

Solution: 161667

Count the wire lengths $L <= 1.5 dot 10^6$ that can be bent into exactly one integer-sided right triangle. Rather than search each length for triangles, generate the triangles. Euclid's formula gives every primitive Pythagorean triple from coprime $m > n > 0$ of opposite parity, with legs $m^2 - n^2$ and $2 m n$ and hypotenuse $m^2 + n^2$, hence perimeter $2 m (m + n)$. Every non-primitive triple is an integer multiple of a primitive one, so for each primitive perimeter $p$, increment a counter at $p, 2p, 3p, dots$ up to the limit. This is a sieve over triangles rather than a scan over lengths; the answer is the number of perimeters whose counter ends at exactly one, namely $161667$.

#pagebreak()
#link("https://projecteuler.net/problem=76")[= Problem 76: Counting Summations]

Solution: 190569291

Count the ways to write $100$ as a sum of two or more positive integers, via memoised recursion over the largest part.

#pagebreak()
#link("https://projecteuler.net/problem=77")[= Problem 77: Prime Summations]

Solution: 71

Find the first value expressible as a sum of primes in more than five thousand ways.

#pagebreak()
#link("https://projecteuler.net/problem=78")[= Problem 78: Coin Partitions]

Solution: 55374

Find the least $n$ for which $p(n)$, the number of partitions of $n$, is divisible by one million. Partition numbers grow super-polynomially, so neither enumerating partitions nor storing the full values is viable. Two ideas handle it. Euler's pentagonal number theorem gives a recurrence with only $O(sqrt(n))$ terms,
$
p(n) = sum_(k >= 1) (-1)^(k+1) (p(n - g_k) + p(n - g_k')),
$
where $g_k = k(3k-1)\/2$ and $g_k' = k(3k+1)\/2$ are the generalized pentagonal numbers (with $p(0) = 1$ and $p("negative") = 0$). And since only divisibility by $10^6$ matters, every value is kept modulo $10^6$, so the numbers never grow. Marching $n$ upward until a residue of zero appears gives $n = 55374$.

#pagebreak()
#link("https://projecteuler.net/problem=79")[= Problem 79: Passcode Derivation]

Solution: 73162890

From fifty three-digit login attempts, each revealing three characters of a secret passcode in order, reconstruct the shortest passcode consistent with all of them. Each attempt $a b c$ asserts that $a$ comes before $b$ and $b$ before $c$, so the attempts are precedence edges of a directed acyclic graph on the digits, and the passcode is a topological ordering of it. Building the graph and running a topological sort (repeatedly emitting a digit with no unmet predecessor) recovers the order. The digits turn out to be fully constrained into one sequence with no repeats, giving the passcode $73162890$.

#pagebreak()
#link("https://projecteuler.net/problem=80")[= Problem 80: Square Root Digital Expansion]

Solution: 40886

For each non-square up to $100$, compute one hundred digits of its square root with integer arithmetic and sum them.

#pagebreak()
#link("https://projecteuler.net/problem=81")[= Problem 81: Path Sum: Two Ways]

Solution: 427337

Find the minimum-sum path through an $80 times 80$ matrix from the top-left to the bottom-right, moving only right or down. The number of such paths is $binom(158, 79)$, far too many to enumerate. But to stand on any cell you must have arrived from the cell above it or the cell to its left, so the cheapest cost to reach a cell is its own value plus the smaller of those two predecessors' costs. Filling this table once, top-left to bottom-right, leaves the answer in the final corner: $427337$.

#pagebreak()
#link("https://projecteuler.net/problem=82")[= Problem 82: Path Sum: Three Ways]

Solution: 260324

Using the same $80 times 80$ matrix, find the minimum-sum path from any cell in the left column to any cell in the right column, now moving up, down, or right. The upward move breaks the single sweep of Problem 81, since a cell's cost can depend on one below it. The fix is to separate movement between columns from movement within a column: process columns left to right, and for each new column first record the cost of stepping right into each row, then relax vertical moves with two passes over the column — one downward, one upward — which resolves arriving at any row from any entry point. The minimum over the final column is $260324$.

#pagebreak()
#link("https://projecteuler.net/problem=83")[= Problem 83: Path Sum: Four Ways]

Solution: 425185

Using the same matrix once more, find the minimum-sum path from top-left to bottom-right, now moving freely in all four directions. With unrestricted movement there is no ordering of cells in which each depends only on earlier ones — the dependency graph has cycles — so the column sweeps of the previous problems no longer apply. This is a shortest-path problem: each cell is a node, and the cost of moving into a cell is its value. Dijkstra's algorithm with a priority queue repeatedly finalizes the cheapest-reachable unvisited cell (valid because all values are non-negative) and relaxes its neighbours, giving the minimum cost to the bottom-right corner as $425185$.

#pagebreak()
#link("https://projecteuler.net/problem=84")[= Problem 84: Monopoly Odds]

Solution: 101524

Playing Monopoly with four-sided dice, find the three squares most likely to be occupied and concatenate their two-digit indices. The board is a $40$-square loop with rules that perturb a plain random walk: landing on Go To Jail sends you to jail, three consecutive doubles sends you to jail, and the Community Chest and Chance squares draw from decks that may relocate the player (to Go, jail, specific squares, the next railway or utility, or back three). A Monte Carlo simulation rolls the dice many millions of times, applies every rule (tracking the consecutive-doubles count, and re-resolving the lone case where "go back three" from square $36$ lands on a Community Chest), and tallies each resulting square. The three most-visited are Jail ($10$), R2 ($15$), and E3 ($24$) -- well separated from the rest -- giving $101524$.

#pagebreak()
#link("https://projecteuler.net/problem=85")[= Problem 85: Counting Rectangles]

Solution: 2772

Search grid dimensions for the rectangle count nearest two million; a $w times h$ grid contains $sum (w - i)(h - j)$ sub-rectangles.

#pagebreak()
#link("https://projecteuler.net/problem=86")[= Problem 86: Cuboid Route]

Solution: 1818

A fly walks across the surface of an $a times b times c$ room between opposite corners; find the least maximum dimension $M$ for which the number of integer-sided cuboids (up to $M$) with an integer shortest route first exceeds one million. Unfolding the box turns the surface path into a straight line, and for $a <= b <= c$ the shortest unfolding has length $sqrt((a + b)^2 + c^2)$, so an integer route means $(a + b)^2 + c^2$ is a perfect square -- a Pythagorean condition. For each largest dimension $c$, range over the split $s = a + b$, test whether $s^2 + c^2$ is square, and add the number of pairs $(a, b)$ with $1 <= a <= b <= c$ summing to $s$ (a short closed count depending on whether $s <= c + 1$). Accumulating $c$ upward, the total passes one million at $M = 1818$ (and equals $2060$ at $M = 100$, as stated).

#pagebreak()
#link("https://projecteuler.net/problem=87")[= Problem 87: Prime Power Triples]

Solution: 1097343

Count the numbers below $5 times 10^7$ expressible as $p^2 + q^3 + r^4$ for primes $p, q, r$. The roots are small ($r <= 84$, $q <= 368$, $p <= 7071$), so sieve the primes once and mark every reachable sum in a boolean array, breaking each loop as soon as the partial sum passes the limit. The answer is the number of distinct marked sums.

#pagebreak()
#link("https://projecteuler.net/problem=88")[= Problem 88: Product-Sum Numbers]

Solution: 7587457

A product-sum number for set size $k$ is the smallest $N$ that is both the sum and the product of some $k$ natural numbers; sum the distinct minimal product-sum numbers for $2 <= k <= 12000$. Searching sets of up to twelve thousand numbers directly is hopeless, but two observations make it finite. Padding a factorization with $1$s leaves the product unchanged while raising the count and the sum, so a product $P$ formed from $t$ factors (each $>= 2$) summing to $S$ realizes $N = P$ for set size $k = t + (P - S)$. And the minimal value for any $k$ is at most $2k$ (take the factors ${2, k}$), so products beyond $2 dot 12000$ never need checking. A depth-first enumeration of all factorizations up to that bound assigns each its $k$, keeps the smallest $N$ per $k$, and the distinct minima sum to $7587457$ (and to $30$ for $k$ up to $6$, as stated).

#pagebreak()
#link("https://projecteuler.net/problem=89")[= Problem 89: Roman Numerals]

Solution: 743

Given a thousand Roman numerals written in valid but not necessarily minimal form, count the characters saved by rewriting each minimally. Rather than reason about Roman-numeral rules directly, pass through the integer value, which is unambiguous: parse each numeral (subtracting a symbol whenever a larger one follows it, adding it otherwise), then re-emit greedily from a value table that includes the six subtractive pairs ($"CM", "CD", "XC", "XL", "IX", "IV"$), taking the largest symbol that fits at each step. The saving is the length difference, and over all the numerals it totals $743$.

#pagebreak()
#link("https://projecteuler.net/problem=90")[= Problem 90: Cube Digit Pairs]

Solution: 1217

Two cubes each carry six of the ten digits; count the cube pairs that can display all nine two-digit squares ($01, 04, 09, 16, 25, 36, 49, 64, 81$) by placing the cubes side by side in either order. There are only $binom(10, 6) = 210$ possible cubes, so the search is small -- the real subtlety is that a $6$ can be turned upside down to serve as a $9$ and vice versa. Modelling that as a single capability (a cube "shows" $6$ or $9$ if it bears either), a pair is valid when, for every square $a b$, one cube shows $a$ while the other shows $b$ in some arrangement. Counting valid unordered pairs gives $1217$.

#pagebreak()
#link("https://projecteuler.net/problem=91")[= Problem 91: Right Triangles with Integer Coordinates]

Solution: 14234

Count the right triangles with one vertex at the origin and the other two at lattice points in a $50 times 50$ grid. The right angle may sit at any of the three vertices, and degenerate (collinear) triples must be excluded. No trigonometry or distances are needed: two edge vectors are perpendicular exactly when their dot product is zero, an exact integer test. So for each unordered pair of grid points $P, Q$ (origin excluded), discard the pair if $O, P, Q$ are collinear (cross product zero), then check the three vertices with three integer dot products. Sweeping every pair once counts each triangle exactly once, giving $14234$.

#pagebreak()
#link("https://projecteuler.net/problem=92")[= Problem 92: Square Digit Chains]

Solution: 8581146

Every chain under repeated squared-digit-sum ends at $1$ or $89$; count the starts below ten million that reach $89$.

#pagebreak()
#link("https://projecteuler.net/problem=93")[= Problem 93: Arithmetic Expressions]

Solution: 1258

Using four distinct digits with $+, -, times, div$ and parentheses, each digit once, find the set producing the longest unbroken run of target integers $1, 2, 3, dots, n$; report the digits in increasing order. Two ideas handle the explosion of expressions. All reachable values are generated by a single recursion: from a multiset of numbers, pick any ordered pair, replace it with each of $a+b$, $a-b$, $a times b$, $a div b$, and recurse on the smaller multiset -- which automatically covers every ordering and parenthesization. And the arithmetic is done with exact fractions, so division never introduces rounding error and a value counts as a target only when it is exactly a positive integer. Across the $binom(10,4) = 210$ digit sets, ${1, 2, 5, 8}$ yields the longest consecutive run (reaching $51$), so the answer is $1258$.

#pagebreak()
#link("https://projecteuler.net/problem=94")[= Problem 94: Almost Equilateral Triangles]

Solution: 518408346

Sum the perimeters of all almost-equilateral triangles -- sides $a, a, a plus.minus 1$ -- that also have integer area, with perimeter at most $10^9$. Searching side lengths up to a third of a billion is far too slow, but the integer-area condition is a Pell equation in disguise. Writing the third side as $b = a + e$ with $e = plus.minus 1$, an integer area needs $4a^2 - b^2 = k^2$; substituting $u = 3a - e$ turns this into $u^2 - 3 k^2 = 4$. The solutions of that Pell equation are produced by the recurrence $u' = 2u + 3k$, $k' = u + 2k$, each roughly $3.7$ times the last, so the rare valid triangles are generated directly rather than hunted. About fifteen steps reach the billion limit; their perimeters sum to $518408346$.

#pagebreak()
#link("https://projecteuler.net/problem=95")[= Problem 95: Amicable Chains]

Solution: 14316

Find the smallest member of the longest amicable chain whose every element stays at or below $10^6$ (a chain is $n -> s(n) -> s(s(n)) -> dots -> n$, where $s$ sums proper divisors).

Sieve $s(i)$ for all $i <= 10^6$, then from each start follow the sequence. A walk that drops below the start (its true minimum was already handled) or climbs above $10^6$ is discarded; one that returns to the start is a chain. A generous length cap stops the walk from spinning forever inside a foreign cycle whose minimum exceeds the start. Track the longest.

#pagebreak()
#link("https://projecteuler.net/problem=96")[= Problem 96: Su Doku]

Solution: 24702

Solve fifty Sudoku puzzles and sum the three-digit number in the top-left corner of each solution. A blind cell-by-cell guess faces up to $9$ choices per blank across dozens of blanks, an astronomical tree. Backtracking with a minimum-remaining-values heuristic tames it: always fill the empty cell with the fewest legal digits first, so forced cells are resolved immediately and branching happens only where unavoidable. Row, column, and box constraints are kept as bitmasks, making each cell's candidate set a couple of bitwise operations. The search then resolves each grid in milliseconds, and the corner numbers sum to $24702$.

#pagebreak()
#link("https://projecteuler.net/problem=97")[= Problem 97: Large Non-Mersenne Prime]

Solution: 8739992577

Report the last ten digits of $28433 dot 2^7830457 + 1$.

#pagebreak()
#link("https://projecteuler.net/problem=98")[= Problem 98: Anagramic Squares]

Solution: 18769

Among anagram word pairs, a bijective letter-to-digit substitution may turn both words into square numbers; find the largest such square. Searching all letter-to-digit assignments per word is wasteful. Instead, let the squares supply the mappings: group words by their sorted letters to find anagram pairs, and for each pair of a given length, scan the squares of that length. Aligning a square's digits with the first word reads off the implied letter-to-digit map (rejecting it unless it is a clean bijection); applying that same map to the anagram partner and checking whether the result is also a square (with no leading zero) confirms an anagramic pair. The largest square obtained this way is $18769$.

#pagebreak()
#link("https://projecteuler.net/problem=99")[= Problem 99: Largest Exponential]

Solution: 709

Compare the base-exponent pairs from file by exponent times $ln$ of base and report the line of the largest.

#pagebreak()
#link("https://projecteuler.net/problem=100")[= Problem 100: Arranged Probability]

Solution: 756872327473

A box of blue and red discs gives probability exactly $1\/2$ of drawing two blue discs without replacement; find the number of blue discs in the first arrangement with more than $10^12$ discs in total. The condition $2b(b-1) = n(n-1)$ is, after substituting $u = 2n - 1$ and $v = 2b - 1$, the negative Pell equation $u^2 - 2 v^2 = -1$. Its solutions are generated by $(u, v) -> (3u + 4v, 2u + 3v)$, each about $5.8$ times the last, producing the arrangements $3\/4, 15\/21, 85\/120, dots$ directly rather than by search. After about twenty steps the total passes a trillion, with $756872327473$ blue discs.

#pagebreak()
#link("https://projecteuler.net/problem=101")[= Problem 101: Optimum Polynomial]

Solution: 37076114526

A degree-ten polynomial generates a sequence; if only the first $k$ terms were known, one would fit the unique degree-$(k-1)$ polynomial through them and predict the next term. Sum these first incorrect predictions over all $k$ before the fit becomes exact. There is no need to solve for polynomial coefficients: Lagrange interpolation evaluates the fitted polynomial directly at a target point as a weighted combination of the known values, done in exact fractions. Since a fit through the first $k$ points reproduces the sequence exactly there, its first disagreement is always at term $k+1$; summing $"OP"(k, k+1)$ for $k = 1$ to $10$ gives $37076114526$.

#pagebreak()
#link("https://projecteuler.net/problem=102")[= Problem 102: Triangle Containment]

Solution: 228

Given a thousand triangles by their vertex coordinates, count how many contain the origin. The cross product gives the signed side of a directed edge, and the origin lies inside a triangle exactly when it is on the same side of all three edges traversed in order. So for each triangle, compute the three cross products of the origin against edges $A B$, $B C$, $C A$; if their signs are all the same the origin is enclosed, and if mixed it is outside. Three integer multiplications per triangle, with no floating point or special cases, give $228$ containing the origin.

#pagebreak()
#link("https://projecteuler.net/problem=103")[= Problem 103: Special Subset Sums: Optimum]

Solution: 20313839404245

A special sum set has all subset sums distinct *and* larger subsets always summing to more than smaller ones; find the minimum-sum special set of size seven, written as its concatenated elements. Two simplifications make the conditions cheap to test: "disjoint subsets have distinct sums" is equivalent to "all $2^n$ subset sums are distinct," and the size-monotonic rule reduces to checking that the smallest $k+1$ elements outweigh the largest $k$, for a few small $k$. The optimum is not searched from scratch but built: from an optimum set of size $n$ with median $m$, the set ${m} union {m + a_i}$ is a near-optimal size-$(n+1)$ candidate. Applied to the size-six optimum ${11,18,19,20,22,25}$ this yields ${20,31,38,39,40,42,45}$, and a small local search confirms nothing nearby is both smaller and special, giving $20313839404245$.

#pagebreak()
#link("https://projecteuler.net/problem=104")[= Problem 104: Pandigital Fibonacci Ends]

Solution: 329468

Find the Fibonacci index whose first nine and last nine digits are each $1$ to $9$ pandigital, keeping the tail modulo $10^9$ to stay fast.

#pagebreak()
#link("https://projecteuler.net/problem=105")[= Problem 105: Special Subset Sums: Testing]

Solution: 73702

From a file of around a hundred sets, identify which are special sum sets and sum the totals of those. This reuses the test from Problem 103: a set is special when all $2^n$ subset sums are distinct (equivalent to the disjoint-subset condition) and the $k+1$ smallest elements always outweigh the $k$ largest. Applying that check to each set and adding the totals of the special ones gives $73702$.

#pagebreak()
#link("https://projecteuler.net/problem=106")[= Problem 106: Special Subset Sums: Meta-testing]

Solution: 21384

For a set of $n$ elements whose size rule already holds, how many equal-size disjoint subset pairs actually need an equal-sum test? Unequal sizes are settled by the size rule, so only equal-size pairs $(B,C)$ matter, and even most of those are pre-decided: if $B$ sorted is element-wise smaller than $C$ sorted, then $B$ obviously sums less.

The count of such pre-decided (dominating) splits of $2k$ chosen elements is the Catalan number $C_k = binom(2k, k) \/ (k+1)$, because "one sorted sequence stays ahead of the other" is exactly the ballot condition Catalan numbers count. So for subset size $k$ the pairs needing a test number $binom(2k,k)\/2 - C_k$, and summing over the ways to pick the $2k$ elements gives

$ sum_(k=2)^(floor(n\/2)) binom(n, 2k) (binom(2k,k)\/2 - C_k) = 21384 $

for $n = 12$.

#pagebreak()
#link("https://projecteuler.net/problem=107")[= Problem 107: Minimal Network]

Solution: 259679

Given a 40-vertex weighted network as a symmetric adjacency matrix, find the greatest weight that can be removed while keeping every vertex connected. The cheapest connected subgraph is the minimum spanning tree, so the saving is the total of all edge weights minus the MST weight. Parsing the upper triangle into an edge list and running Kruskal's algorithm (sort edges ascending, add each edge whose endpoints lie in different components via union-find) gives an MST; subtracting it from the total yields $259679$.

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
#link("https://projecteuler.net/problem=109")[= Problem 109: Darts]

Solution: 38182

Count the ways to check out a score below 100, where a checkout uses at most three darts and the final dart must be a double. The board offers 62 distinct scoring segments (singles 1--20 and 25, doubles of those plus the bullseye 50, trebles 3--60), of which 21 are doubles. Fixing each possible finishing double, the zero, one, or two preceding darts form an unordered multiset; iterating the preceding darts with $i <= j$ to avoid double-counting permutations, and tallying every combination whose total stays under 100, gives $38182$.

#pagebreak()
#link("https://projecteuler.net/problem=110")[= Problem 110: Diophantine Reciprocals II]

Solution: 9350130049860600

Find the least $n$ for which $1\/x + 1\/y = 1\/n$ has more than four million solutions. The number of solutions equals $(d(n^2)+1)\/2$, where $d$ counts divisors, so the requirement is $d(n^2) > 7999999$. Writing $n = product p_i^(a_i)$ gives $d(n^2) = product (2 a_i + 1)$, a product of odd factors. Minimizing $n$ means assigning non-increasing exponents to the smallest primes; a depth-first search over exponent patterns (each prime's exponent capped by the previous one, pruning once $n$ exceeds the best found) locates the minimum, $9350130049860600$.

#pagebreak()
#link("https://projecteuler.net/problem=111")[= Problem 111: Primes with Runs]

Solution: 612407567715

Among 10-digit primes, for each digit $d$ find $M(d)$, the most times $d$ can repeat, then sum every 10-digit prime achieving that maximum; the answer is the total over all $d$. Rather than scan all primes, fix $d$ and try repetition counts from 10 downward: place $d$ in $m$ of the positions, fill the remaining $10 - m$ with non-$d$ digits (a small space, since $m$ is large), and primality-test each candidate. The first count $m$ that yields any primes is $M(d)$; their sum contributes to the running total of $612407567715$.

#pagebreak()
#link("https://projecteuler.net/problem=112")[= Problem 112: Bouncy Numbers]

Solution: 1587000

Count bouncy numbers (digits neither wholly non-decreasing nor non-increasing) until they make up ninety-nine percent of all numbers seen.

#pagebreak()
#link("https://projecteuler.net/problem=113")[= Problem 113: Non-Bouncy Numbers]

Solution: 51161058134250

Count the non-bouncy numbers below $10^100$ -- those whose digits are entirely non-decreasing or entirely non-increasing. No search is needed; each family is a stars-and-bars count. Non-decreasing numbers of up to $d$ digits (digits 1--9) number $binom(d+9, 9) - 1$, and non-increasing ones (digits 0--9, discarding the all-zero string at each length) number $binom(d+10, 10) - 1 - d$. Repdigits are counted in both, $9 d$ of them, so by inclusion--exclusion the total is $binom(d+9,9) + binom(d+10,10) - 10 d - 2$, which at $d = 100$ equals $51161058134250$.

#pagebreak()
#link("https://projecteuler.net/problem=114")[= Problem 114: Counting Block Combinations I]

Solution: 16475640049

A special case of Problem 115 with minimum block length three.

#pagebreak()
#link("https://projecteuler.net/problem=115")[= Problem 115: Counting Block Combinations II]

Solution: 168

Count the arrangements of red blocks of length at least $m$ separated by single gaps via memoised recursion, then find the row length where the count first passes one million.

#pagebreak()
#link("https://projecteuler.net/problem=116")[= Problem 116: Red, Green or Blue Tiles]

Solution: 20492570929

Count the ways to lay tiles of a single length ($2$, $3$ or $4$) on a row of fifty squares, summed over the three colours, excluding the empty arrangement.

#pagebreak()
#link("https://projecteuler.net/problem=117")[= Problem 117: Red, Green, and Blue Tiles]

Solution: 100808458960497

Count the ways to tile a row of 50 units using grey unit tiles together with red (length 2), green (length 3), and blue (length 4) tiles. Classifying tilings by the final tile gives the tetranacci recurrence $f(n) = f(n-1) + f(n-2) + f(n-3) + f(n-4)$ with $f(0) = 1$ and $f(n) = 0$ for $n < 0$. Rolling it forward to $n = 50$ yields $100808458960497$.

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
#link("https://projecteuler.net/problem=119")[= Problem 119: Digit Power Sum]

Solution: 248155780267521

Find the 30th number (at least two digits) that equals a power of its own digit sum, such as $512 = 8^3$ and $2401 = 7^4$. Searching the numbers directly is wasteful; instead generate candidates as $b^e$ for integer base $b >= 2$ and exponent $e >= 2$, keeping those where the digit sum of $b^e$ equals $b$. Since a value below $10^16$ has digit sum at most $144$, bases up to about $150$ suffice. Collecting the matches, sorting, and taking the 30th gives $248155780267521$.

#pagebreak()
#link("https://projecteuler.net/problem=120")[= Problem 120: Square Remainders]

Solution: 333082500

For each $a$ with $3 <= a <= 1000$, maximize the remainder $r$ of $(a-1)^n + (a+1)^n$ modulo $a^2$. Expanding both powers binomially, every term with $a^2$ or higher vanishes modulo $a^2$, leaving only the constant and linear terms. Even $n$ gives remainder $2$; odd $n$ gives $2 a n mod a^2 = a dot ((2n) mod a)$. The factor $(2n) mod a$ can reach $a-1$ when $a$ is odd (2 is invertible) but only $a-2$ when $a$ is even, so the maximum remainder is $a(a-1)$ or $a(a-2)$ accordingly. Summing over the range gives $333082500$.

#pagebreak()
#link("https://projecteuler.net/problem=121")[= Problem 121: Disc Game Prize Fund]

Solution: 2269

A bag starts with one red and one blue disc; each of 15 turns draws a disc (returned afterward) and then adds another red, so turn $i$ holds one blue among $i+1$ discs and $P(text("blue")) = 1\/(i+1)$. The player wins by drawing strictly more blue than red. Scaling turn $i$ by $i+1$ turns the chances into integer weights (blue 1, red $i$), so the coefficient of $x^k$ in $product_(i=1)^(15) (i + x)$ counts the weighted outcomes with exactly $k$ blue draws. Summing the coefficients for $k >= 8$ gives the winning weight; the win probability is that over $16!$, and the largest prize keeping the game profitable is $floor(16! \/ "wins") = 2269$.

#pagebreak()
#link("https://projecteuler.net/problem=122")[= Problem 122: Efficient Exponentiation]

Solution: 1582

For each $k$ up to 200, find the fewest multiplications needed to compute $x^k$, then sum these counts. Each multiplication forms a new power by adding two exponents already obtained, so a method for $x^k$ is exactly an addition chain ending at $k$, and the minimum is the shortest such chain. The shortest chain is found by iterative deepening: search for a chain of length 1, then 2, and so on, at each step extending by the sum of the current term with an earlier one, pruning whenever repeated doubling of the largest term still cannot reach $k$. Summing the minimal lengths over $k = 1$ to $200$ gives $1582$.

#pagebreak()
#link("https://projecteuler.net/problem=123")[= Problem 123: Prime Square Remainders]

Solution: 21035

Using $(p - 1)^n + (p + 1)^n mod p^2$, find the first prime index whose remainder exceeds $10^10$.

#pagebreak()
#link("https://projecteuler.net/problem=124")[= Problem 124: Ordered Radicals]

Solution: 21417

Sort $1$ to $100000$ by radical (the product of distinct prime factors), breaking ties by value, and read off the $10000$th.

#pagebreak()
#link("https://projecteuler.net/problem=125")[= Problem 125: Palindromic Sums]

Solution: 2906969179

Sum the palindromes below $10^8$ that can be written as a sum of two or more consecutive squares. Rather than test every number, generate the sums: for each starting base accumulate consecutive squares until the running total reaches $10^8$, recording each palindromic total in a set so that a number expressible in several ways is still counted once. Sum the set.

#pagebreak()
#link("https://projecteuler.net/problem=126")[= Problem 126: Cuboid Layers]

Solution: 18522

Cubes are wrapped in layers around an $a times b times c$ cuboid; the $n$-th layer uses $2(a b + b c + c a) + 4(n-1)(a + b + c) + 4(n-1)(n-2)$ cubes. The task is the least layer size produced by exactly 1000 distinct cuboids. Iterating cuboids with $a >= b >= c$ (so each is counted once) and all layers $n$, tallying every layer size up to a bound, then scanning for the smallest size with a count of 1000, yields $18522$.

#pagebreak()
#link("https://projecteuler.net/problem=127")[= Problem 127: abc-Hits]

Solution: 18407904

Summing $c$ over all abc-hits with $c < 120000$, where an abc-hit is a coprime triple $a + b = c$ ($a < b$) with $op("rad")(a b c) < c$ and $op("rad")$ the product of distinct primes. Since $a + b = c$ with $gcd(a,b)=1$ forces $a, b, c$ pairwise coprime, $op("rad")(a b c) = op("rad")(a) op("rad")(b) op("rad")(c)$. A radical sieve precomputes every $op("rad")$, and the values are sorted by radical so that, looping over $a$ and ascending $op("rad")(b)$, the inner loop breaks as soon as $op("rad")(a) op("rad")(b) >= 120000$ -- already too large to undercut any $c$. The surviving triples passing the coprimality and radical tests sum to $18407904$.

#pagebreak()
#link("https://projecteuler.net/problem=128")[= Problem 128: Hexagonal Tile Differences]

Solution: 14516824220

Hexagonal tiles spiral outward, and PD(n) counts how many of a tile's six neighbour-differences are prime; the 2000th tile with PD = 3 is sought. Brute-forcing the spiral on small rings shows PD = 3 can only occur at ring corners. The first tile of ring $n$, numbered $3n^2-3n+2$, has differences $6n-1$, $6n+1$, $12n+5$; the last tile, $3n^2+3n+1$ (for $n >= 2$), has $6n-1$, $6n+5$, $12n-7$. PD = 3 holds exactly when those three are all prime. Tile 1 is the first such tile and ring 1's last tile (7) is a non-qualifying special case. Enumerating corners in order until the 2000th gives $14516824220$.

#pagebreak()
#link("https://projecteuler.net/problem=129")[= Problem 129: Repunit Divisibility]

Solution: 1000023

For $n$ coprime to 10, let $A(n)$ be the length of the smallest repunit (a number of the form $111...1$) divisible by $n$; find the least $n$ with $A(n) > 10^6$. Since $A(n) <= n$ always, any such $n$ must itself exceed $10^6$, so the search starts at $1000001$. For each candidate coprime to 10, the repunit residue is grown one digit at a time via $x arrow.r (10 x + 1) mod n$, stopping early once the length passes $10^6$ without hitting zero. The first qualifying $n$ is $1000023$.

#pagebreak()
#link("https://projecteuler.net/problem=130")[= Problem 130: Composites with Prime Repunit Property]

Solution: 149253

With $A(n)$ the least repunit length divisible by $n$ (from Problem 129), every prime $p$ outside ${2,3,5}$ satisfies $A(p) | p-1$. The task is the sum of the first 25 composite $n$ (coprime to 10) for which $A(n)$ likewise divides $n-1$. Scanning odd non-multiples of 5, skipping primes, computing $A(n)$ by the residue recurrence $x arrow.r (10 x + 1) mod n$, and testing $(n-1) mod A(n) = 0$ collects them; the first 25, beginning with 91, sum to $149253$.

#pagebreak()
#link("https://projecteuler.net/problem=131")[= Problem 131: Prime Cube Partnership]

Solution: 173

Count the primes $p < 10^6$ for which some positive integer $n$ makes $n^3 + n^2 p$ a perfect cube. Writing this as $n^2(n+p)$ and trying $n = k^3$ turns it into $k^6 (k^3 + p)$, a cube precisely when $k^3 + p$ is the next cube $(k+1)^3$, i.e. $p = (k+1)^3 - k^3 = 3k^2 + 3k + 1$. These differences of consecutive cubes are the only $p$ that work, so the answer is the number of primes among them below $10^6$, which is $173$.

#pagebreak()
#link("https://projecteuler.net/problem=132")[= Problem 132: Large Repunit Factors]

Solution: 843296

Find the sum of the first 40 prime factors of the repunit $R(10^9)$, a number with a billion ones. Since $R(k) = (10^k - 1)\/9$, a prime $p$ outside ${2,3,5}$ divides $R(k)$ exactly when $10^k equiv 1 (mod p)$. This is checked instantly by modular exponentiation, never forming the giant number. Testing primes in increasing order and accumulating the first 40 that satisfy the congruence gives $843296$.

#pagebreak()
#link("https://projecteuler.net/problem=133")[= Problem 133: Repunit Nonfactors]

Solution: 453647705

Sum the primes below $10^5$ that never divide $R(10^n)$ for any $n$. A prime $p$ (not 2 or 5) divides some $R(10^n)$ iff its order $op("ord")_p(10)$ divides $10^n$ for some $n$, which happens exactly when that order has the form $2^a 5^b$. Equivalently, $p$ is a divisor iff $10^(10^n) equiv 1 (mod p)$ for some small $n$ (the exponents $a, b$ are bounded since the order is below $p$), testable directly. The primes failing this for all $n$ -- the nonfactors, with $p = 3$ a special case since $3 | 9$ -- sum to $453647705$.

#pagebreak()
#link("https://projecteuler.net/problem=134")[= Problem 134: Prime Pair Connection]

Solution: 18613426663617118

For each pair of consecutive primes $p_1 < p_2$ with $5 <= p_1 <= 10^6$, find the least $n$ whose final digits are $p_1$ and which is divisible by $p_2$, then sum these. Writing $n = p_1 + k dot 10^d$ where $d$ is the digit count of $p_1$, divisibility by $p_2$ requires $k equiv -p_1 (10^d)^(-1) (mod p_2)$. Since $10^d$ is coprime to $p_2$, its modular inverse exists, giving $k$ and hence $n$ directly for each pair. Summing over all pairs yields $18613426663617118$.

#pagebreak()
#link("https://projecteuler.net/problem=135")[= Problem 135: Same Differences]

Solution: 4989

Count the $n < 10^6$ for which $x^2 - y^2 - z^2 = n$ has exactly ten solutions in positive integers $x, y, z$ that are consecutive terms of an arithmetic progression. Since the AP gives $z = 2y - x$, the form simplifies to $y(4x - 5y)$. Setting $k = 4x - 5y$ makes $n = y k$ with $x = (5y+k)\/4$ and $z = (3y-k)\/4$, so a valid solution requires $k < 3y$ and $y + k equiv 0 (mod 4)$. Sweeping all such $(y, k)$ and tallying the resulting $n$ in a sieve, then counting indices whose tally is exactly ten, gives $4989$.

#pagebreak()
#link("https://projecteuler.net/problem=136")[= Problem 136: Singletons]

Solution: 2544559

Count the $n < 5 times 10^7$ for which $x^2 - y^2 - z^2 = n$ (with $x, y, z$ consecutive terms of an arithmetic progression) has exactly one solution. This is the Problem 135 reduction reused: solutions correspond to pairs $n = y k$ with $k < 3y$ and $y + k equiv 0 (mod 4)$. The same sweep tallies each $n$, saturating the count at two since only the cases none/one/many matter, and the number of $n$ with a tally of exactly one is $2544559$.

#pagebreak()
#link("https://projecteuler.net/problem=137")[= Problem 137: Fibonacci Golden Nuggets]

Solution: 1120149658760

The Fibonacci power series $A_F(x) = sum_(i>=1) F_i x^i$ equals $x\/(1 - x - x^2)$. Demanding $A_F(x) = n$ for a positive integer $n$ gives $n x^2 + (n+1) x - n = 0$, which has a rational root exactly when its discriminant $5n^2 + 2n + 1$ is a perfect square. The integers $n$ that arise (the golden nuggets) are precisely the products $F_(2k) dot F_(2k+1)$: $2, 15, 104, 714, ...$ The 15th is $F_30 dot F_31 = 1120149658760$.

#pagebreak()
#link("https://projecteuler.net/problem=138")[= Problem 138: Special Isosceles Triangles]

Solution: 1118049290473932

Consider isosceles triangles with base $b$ and equal legs $L$ whose height $h$ differs from the base by exactly one ($h = b plus.minus 1$). From $L^2 = (b\/2)^2 + h^2$ the condition rearranges to $(5b plus.minus 4)^2 - 20 L^2 = -4$, a Pell-type equation. Its solutions make the leg lengths satisfy the recurrence $L_n = 18 L_(n-1) - L_(n-2)$ with $L_1 = 17$ (the smallest triangle, base 16) and $L_2 = 305$. Summing the first twelve leg lengths gives $1118049290473932$.

#pagebreak()
#link("https://projecteuler.net/problem=139")[= Problem 139: Pythagorean Tiles]

Solution: 10057761

Count Pythagorean triples $a^2 + b^2 = c^2$ with perimeter below $10^8$ for which four copies of the triangle tile a $c times c$ square leaving a central hole of side $|b - a|$ that itself tiles the square, i.e. $(b - a) | c$. Generating primitives by Euclid's formula ($a = m^2-n^2$, $b = 2 m n$, $c = m^2+n^2$), the divisibility test is scale-invariant, so each qualifying primitive of perimeter $P$ contributes $floor((10^8-1)\/P)$ scaled copies. Summing over all primitives gives $10057761$.

#pagebreak()
#link("https://projecteuler.net/problem=140")[= Problem 140: Modified Fibonacci Golden Nuggets]

Solution: 5673835352990

For the modified Fibonacci sequence $1, 4, 5, 9, 14, ...$, the series $A_G(x) = sum G_k x^k$ equals $(x + 3x^2)\/(1 - x - x^2)$. Setting $A_G(x) = n$ gives $(n+3) x^2 + (n+1) x - n = 0$, rational exactly when the discriminant $5n^2 + 14n + 1$ is a perfect square. The resulting golden nuggets $2, 5, 21, 42, 152, 296, 1050, ...$ obey the recurrence $n_k = 7 n_(k-2) - n_(k-4) + 7$; summing the first thirty gives $5673835352990$.

#pagebreak()
#link("https://projecteuler.net/problem=141")[= Problem 141: Investigating Progressive Perfect Squares]

Solution: 878454337159

A number $n$ is progressive if dividing it by $d$ leaves quotient $q$ and remainder $r$ with $q, d, r$ forming a geometric progression. Sum the progressive perfect squares below $10^12$. Since $r < d$, the quotient $q$ is the geometric mean, so writing $r = a c^2$, $q = a c e$, $d = a e^2$ with $e > c$ coprime and core $a$ gives $n = q d + r = a^2 c e^3 + a c^2$. Sweeping these parameters within the bound and keeping the perfect squares (deduplicated) sums to $878454337159$.

#pagebreak()
#link("https://projecteuler.net/problem=142")[= Problem 142: Perfect Square Collections]

Solution: 1006193

Find the smallest $x + y + z$ (with $x > y > z > 0$) for which $x+y$, $x-y$, $x+z$, $x-z$, $y+z$, $y-z$ are all perfect squares. The pairs $x plus.minus y$ and $x plus.minus z$ being square means both $y$ and $z$ are values $v$ with $x plus.minus v$ square, i.e. $2x = c^2 + d^2$ and $v = (c^2 - d^2)\/2$. Collecting these candidate values for each $x$, then searching each $x$ for a pair $y > z$ whose sum and difference are also squares (scanning $x$ in increasing order and stopping once $x$ alone exceeds the best sum), yields $1006193$.

#pagebreak()
#link("https://projecteuler.net/problem=143")[= Problem 143: Investigating the Torricelli Point of a Triangle]

Solution: 30758397

The Torricelli point joins to the three vertices by segments $p, q, r$ meeting at 120 degrees, so each triangle side is $sqrt(p^2 + p q + q^2)$. Integer sides require every pair among $p, q, r$ to satisfy $p^2 + p q + q^2 = $ square -- a "120-pair", generated from Eisenstein triples $A = m^2 - n^2$, $B = 2 m n + n^2$ and their multiples. Building the graph whose edges are 120-pairs and summing the distinct $p + q + r <= 120000$ over all triangles (mutually paired triples) gives $30758397$.

#pagebreak()
#link("https://projecteuler.net/problem=144")[= Problem 144: Investigating Multiple Reflections of a Laser Beam]

Solution: 354

A laser bounces inside the elliptical mirror $4x^2 + y^2 = 100$, entering through a tiny gap at the top and reflecting until it escapes. The simulation tracks the contact point and travel direction: at each impact the inward normal is parallel to $(4x, y)$, so the reflected direction is $d - 2 (d dot n \/ n dot n) n$. Substituting the reflected ray into the ellipse equation and discarding the current root gives the next contact via $t = -(8 x r_x + 2 y r_y) \/ (4 r_x^2 + r_y^2)$. Counting contacts until the beam reaches the gap ($|x| <= 0.01$, $y > 0$) yields $354$.

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
#link("https://projecteuler.net/problem=146")[= Problem 146: Investigating a Prime Pattern]

Solution: 676333270

Find $n < 1.5 times 10^8$ for which $n^2 + 1, 3, 7, 9, 13, 27$ are consecutive primes. Parity and a residue check mod 5 force $n$ to be a multiple of 10, and small-prime divisibility of any $n^2 + "offset"$ prunes the vast majority of candidates in a fast modular sieve. Survivors are confirmed by full primality tests on the six values, plus checks that the intermediate offsets $5, 11, 15, 17, 19, 21, 23, 25$ give composites (so the six are genuinely consecutive). Summing the valid $n$ gives $676333270$.

#pagebreak()
#link("https://projecteuler.net/problem=147")[= Problem 147: Rectangles in Cross-Hatched Grids]

Solution: 846910284

Count all rectangles -- axis-aligned and diagonal -- fitting in every cross-hatched $m times n$ grid for $1 <= m <= 47$, $1 <= n <= 43$, and sum. Axis-aligned rectangles number $binom(m+1,2) binom(n+1,2)$. Diagonal ones use lines $c = x - y$ (slope $+1$) and $d = x + y$ (slope $-1$); a tilted rectangle is an axis box in $(c,d)$ space, valid when its corners stay in the grid. Writing $s = c_1+d_1$, $t = d_1-c_1$ (equal parity), the box of spans $d c, d d$ fits when $s in [0, 2m - d c - d d]$ and $t in [d c, 2n - d d]$; counting same-parity $(s,t)$ gives the diagonal total. The formula was checked against brute force (a 3 by 2 grid gives 37). Summing over all grids yields $846910284$.

#pagebreak()
#link("https://projecteuler.net/problem=148")[= Problem 148: Exploring Pascal's Triangle]

Solution: 2129970655314432

Count the entries in the first $10^9$ rows of Pascal's triangle not divisible by 7. By Kummer's theorem the number of such entries in row $n$ is the product of (base-7 digit $+ 1$) over the digits of $n$. Summing over a complete block of $7^j$ rows gives $28^j$ (since $1 + 2 + dots + 7 = 28$), so a base-7 digit DP over $10^9$ accumulates the total $2129970655314432$ with no triangle ever built.

#pagebreak()
#link("https://projecteuler.net/problem=149")[= Problem 149: Searching for a Maximum-Sum Subsequence]

Solution: 52852124

A $2000 times 2000$ grid is filled by a lagged Fibonacci generator. Find the greatest sum of any contiguous run along a row, column, or either diagonal. After generating the grid, Kadane's algorithm runs along every line in each of the four directions, tracking the best running sum, which is $52852124$.

#pagebreak()
#link("https://projecteuler.net/problem=150")[= Problem 150: Searching a Triangular Array for a Sub-Triangle with Minimum Sum]

Solution: -271248680

A 1000-row triangle is filled by a linear congruential generator. Find the minimum sum over all sub-triangles (an apex plus all cells beneath it). With per-row prefix sums, each apex $(i, j)$ is grown one row at a time, adding the segment $j dots j+d$ of row $i+d$ in constant time, giving an $O(n^3)$ sweep whose minimum is $-271248680$.

#pagebreak()
#link("https://projecteuler.net/problem=151")[= Problem 151: Paper Sheets of Standard Sizes]

Solution: 0.464399

Starting from one A1 sheet, a worker repeatedly draws a random sheet; a sheet larger than A5 is cut, adding one of each smaller size, while an A5 is used up. Find the expected number of draws where the envelope holds exactly one sheet, excluding the first and last. A memoised recursion over the count-state $f(s) = [|s| = 1] + sum p_k f(s')$ gives the expectation; subtracting the always-present first (the A1) and last (the lone A5) occurrences yields $0.464399$.

#pagebreak()
#link("https://projecteuler.net/problem=152")[= Problem 152: Writing 1/2 as a Sum of Inverse Squares]

Solution: 301

Count the ways to write $1\/2$ as a sum of distinct $1\/k^2$ with $2 <= k <= 80$. For each prime $p >= 11$ (so $p^2 > 80$), the chosen multiples of $p$ must combine $p$-integrally: the numerator of $sum 1\/(k\/p)^2$ over them must be divisible by $p^2$. Multiples lying in no such group are dropped, cutting 79 candidates to 42. With surviving denominators using only the primes up to 13 the common denominator stays within machine range, so a meet-in-the-middle over the 42 values counts the $301$ subsets hitting exactly half.

#pagebreak()
#link("https://projecteuler.net/problem=153")[= Problem 153: Investigating Gaussian Integer Divisors]

Solution: 17971254122360635

Sum, over $n <= 10^8$, of the real parts of every Gaussian-integer divisor $a + b i$ with $a > 0$. Writing each divisor as $g(a' + b' i)$ with $(a', b')$ primitive, the geometric sum over $g$ collapses via $sum_g g floor(K\/g) = sum_(m <= K) sigma(m) =: D(K)$, giving $T = sum_("primitive" (a', b')) a' dot D(N\/(a'^2 + b'^2))$. Each $D$ is evaluated in $O(sqrt(K))$ by hyperbola blocking while iterating primitive vectors, yielding $17971254122360635$.

#pagebreak()
#link("https://projecteuler.net/problem=154")[= Problem 154: Exploring Pascal's Triangle (Trinomials)]

Solution: 479742450

Count the trinomial coefficients $200000! \/ (i! j! k!)$ (with $i + j + k = 200000$) divisible by $10^12 = 2^12 dot 5^12$. By Legendre, $v_p$ of the coefficient is $v_p(n!) - v_p(i!) - v_p(j!) - v_p(k!)$, so divisibility needs $v_2 >= 12$ and $v_5 >= 12$. Precomputing $v_p(m!)$ cumulatively and sweeping $i <= j <= k$ (weighting each triple by its $1$, $3$, or $6$ permutations) counts $479742450$.

#pagebreak()
#link("https://projecteuler.net/problem=155")[= Problem 155: Counting Capacitor Circuits]

Solution: 3857447

Count the distinct capacitances obtainable from up to 18 identical capacitors. Let $S_k$ be the set of values built from exactly $k$ units; each value of $S_k$ comes from joining a network of $i$ units with one of $k - i$ units, in parallel ($a + b$) or in series ($a b \/ (a + b)$). Building $S_1, dots, S_18$ as sets of reduced fractions and taking the union gives $3857447$ distinct values.

#pagebreak()
#link("https://projecteuler.net/problem=156")[= Problem 156: Counting Digits]

Solution: 21295121502550

Let $f(n, d)$ count the occurrences of digit $d$ in writing $1, 2, dots, n$. For each $d$ we want every $n$ with $f(n, d) = n$, then sum them. The function $f$ is evaluated in $O(log n)$ by a place-value formula, and the roots of $g(n) = f(n, d) - n$ are found by recursive bisection: since each step changes $g$ by at most $L - 1$ upward and $1$ downward, an interval with $g("lo") > "len"$ holds no root and is pruned. Summing all roots over $d = 1, dots, 9$ gives $21295121502550$.

#pagebreak()
#link("https://projecteuler.net/problem=157")[= Problem 157: Solving the Diophantine Equation 1/a + 1/b = p/10^n]

Solution: 53490

Count the solutions of $1\/a + 1\/b = p\/10^n$ for $n = 1, dots, 9$. Writing $a = g x$, $b = g y$ with $gcd(x, y) = 1$ forces $x y divides 10^n$, and then $p = (10^n\/(x y))(x + y)\/g$, so each coprime pair $(x, y)$ contributes $d((10^n\/(x y))(x + y))$ solutions (one per valid $g$). Coprime divisors of $10^n$ just assign the whole power of 2 and the whole power of 5 to one side each, so a short enumeration sums to $53490$.

#pagebreak()
#link("https://projecteuler.net/problem=158")[= Problem 158: Exploring Strings with One Left-to-Right Ascent]

Solution: 409511334375

Count length-$n$ strings of distinct letters from a 26-letter alphabet having exactly one position where a letter exceeds its left neighbour. Choosing the $n$ letters fixes their relative order, so the arrangements with exactly one ascent number the Eulerian number $angle.l n, 1 angle.r = 2^n - n - 1$. Thus $p(n) = binom(26, n)(2^n - n - 1)$, and its maximum over $n$ is $409511334375$.

#pagebreak()
#link("https://projecteuler.net/problem=159")[= Problem 159: Digital Root Sums of Factorisations]

Solution: 14489159

For each $n$, $"mdrs"(n)$ is the largest sum of digital roots over all factorisations into integers $> 1$. Since every split $n = a b$ has $a, b < n$, processing $n$ in increasing order makes $"mdrs"(n) = max("dr"(n), max_(a divides n) "mdrs"(a) + "mdrs"(n\/a))$ a clean dynamic program, where $"dr"(n) = 1 + (n - 1) mod 9$. Summing over $2 <= n < 10^6$ gives $14489159$.

#pagebreak()
#link("https://projecteuler.net/problem=160")[= Problem 160: Factorial Trailing Digits]

Solution: 16576

Find the last five non-zero digits of $(10^12)!$. The trailing zeros number $z = v_5(n!)$, and we want $(n!\/10^z) mod 10^5$ via CRT on $2^5$ and $5^5$. Peeling multiples of 5 gives the recursion $P(n) = (product_(5 divides.not k <= n) k) dot P(floor(n\/5))$ for $n!\/5^(v_5)$ modulo $5^5$, each full period of residues multiplying to $-1$. Dividing out the matched twos (invertible mod $5^5$) and combining with $0$ mod $2^5$ (the surplus of twos exceeds 5) yields $16576$.

#pagebreak()
#link("https://projecteuler.net/problem=161")[= Problem 161: Triominoes]

Solution: 20574308184277971

Count the tilings of a $9 times 12$ grid by triominoes (the straight piece in 2 orientations and the L piece in 4). A broken-profile dynamic program scans the cells in row-major order, keeping a bitmask of the occupancy of the window of cells from the current position forward. At the first empty cell a piece must be placed to cover it; otherwise the cell is already filled and the window slides on. Carrying the masks across all 108 cells counts $20574308184277971$ tilings.

#pagebreak()
#link("https://projecteuler.net/problem=162")[= Problem 162: Hexadecimal Numbers]

Solution: 3D58725572C62302

Count hexadecimal numbers of at most 16 digits (no leading zero) containing at least one 0, one 1 and one A. By inclusion-exclusion over which of the three required digits are forbidden, each term counts strings over a reduced alphabet: if 0 is forbidden the first digit is unconstrained among the remaining symbols, otherwise it must avoid 0. Summing over lengths $1$ to $16$ and reporting in hexadecimal gives $"3D58725572C62302"$.

#pagebreak()
#link("https://projecteuler.net/problem=163")[= Problem 163: Cross-Hatched Triangles]

Solution: 343047

Count all triangles in a size-$n$ cross-hatched equilateral triangle. The figure has $9 n - 3$ lines in six direction families. Triangle counting is affine-invariant, so shearing to the right triangle $\{x >= 0, y >= 0, x + y <= n\}$ gives lines $x = k$, $y = k$, $x + y = k$, $x - y = c$, $2 x + y = c$, $x + 2 y = c$ with rational intersections. A triangle is any triple of pairwise non-parallel, non-concurrent lines whose three intersections lie in the region; integer cross-products test this. The model reproduces $T(1) = 16$, $T(2) = 104$, and gives $T(36) = 343047$.

#pagebreak()
#link("https://projecteuler.net/problem=164")[= Problem 164: Numbers for Which No Three Consecutive Digits Have a Sum Greater Than 9]

Solution: 378158756814587

Count 20-digit numbers (no leading zero) in which every three consecutive digits sum to at most 9. A digit DP carries the last two digits as state: from $(a, b)$ the next digit $c$ is allowed whenever $a + b + c <= 9$. Seeding with all valid leading pairs and advancing 18 times sums to $378158756814587$.

#pagebreak()
#link("https://projecteuler.net/problem=165")[= Problem 165: Intersections]

Solution: 2868868

A Blum Blum Shub generator produces 5000 segments; count the distinct true intersection points, where "true" means the unique common point of two segments lying strictly interior to both. Each pair is tested with integer cross products (parallel pairs skipped, endpoints excluded by strict inequalities), and the crossing point is stored as a reduced exact fraction $(X\/g, Y\/g, "den"\/g)$ so coincident crossings collapse. The set then holds $2868868$ distinct points.

#pagebreak()
#link("https://projecteuler.net/problem=166")[= Problem 166: Criss-Cross]

Solution: 7130034

Count $4 times 4$ grids of digits where every row, column and both diagonals share one sum $s$. Fixing rows 0 and 1, the column sums force row 3 from row 2, while the two diagonal conditions and the row-2 sum reduce row 2 to a single free cell: $c_1 - c_0$ and $c_2 - c_3$ are determined, and $c_0 + c_3$ is fixed, so the valid choices of $c_0$ are counted directly within the digit bounds. Summed over all $s$ and top rows: $7130034$.

#pagebreak()
#link("https://projecteuler.net/problem=167")[= Problem 167: Investigating Ulam Sequences]

Solution: 3916160068885

Sum the $10^11$-th term of the Ulam sequences $U(2, 2n+1)$ for $n = 2, dots, 10$. Each such sequence has exactly two even terms, $2$ and $e_2 = 2(v+1)$; afterwards every term is odd, and an odd $x$ belongs to the sequence exactly when one of $x - 2$, $x - e_2$ is already present, giving $O(1)$ generation. The sequence of gaps is eventually periodic, so a KMP failure function recovers the period $P$ and per-period increase, and the far term is reached arithmetically. The nine terms sum to $3916160068885$.

#pagebreak()
#link("https://projecteuler.net/problem=168")[= Problem 168: Number Rotations]

Solution: 59206

Sum the last five digits of every $n$ with $10 <= n < 10^100$ such that moving the last digit to the front yields a multiple of $n$. Writing $n = 10 a + d$, the rotation $d dot 10^(k-1) + a = m n$ gives $a = d(10^(k-1) - m)\/(10 m - 1)$. Looping over digit length $k$, multiplier $m$ and last digit $d$, every integer $a$ in the right range yields a solution; the running sum mod $10^5$ is $59206$.

#pagebreak()
#link("https://projecteuler.net/problem=169")[= Problem 169: Sums of Powers of Two]

Solution: 178653872807

Count the ways to write $n = 10^25$ as a sum of powers of 2 with each power used at most twice. The count obeys $h(2 m) = h(m) + h(m - 1)$ and $h(2 m + 1) = h(m)$, a recursion whose memoised evaluation touches only $O(log n)$ distinct arguments, giving $178653872807$.

#pagebreak()
#link("https://projecteuler.net/problem=170")[= Problem 170: Pandigital Concatenated Products]

Solution: 9857164023

Find the largest 0-to-9 pandigital concatenated product $P = "concat"(m a_1, dots, m a_k)$ whose inputs $"concat"(m, a_1, dots, a_k)$ are also 0-to-9 pandigital. Iterating pandigital $P$ from the top downward, each is split into product-parts in every way; for a split, any common factor $m$ of the parts yields candidate multipliers $a_i = "part"\/m$, and the first $P$ for which $"concat"(m, a_i)$ is pandigital is the answer, $9857164023$.

#pagebreak()
#link("https://projecteuler.net/problem=171")[= Problem 171: Squared Digit Sums That Are Squares]

Solution: 142989277

Sum every $0 < n < 10^20$ whose digits' squares sum to a perfect square, reporting the last nine digits. A digit DP over the 20 positions tracks the square-sum together with how many numbers reach it and their running total mod $10^9$; summing the totals over square-valued states gives $142989277$.

#pagebreak()
#link("https://projecteuler.net/problem=172")[= Problem 172: Investigating Numbers with Few Repeated Digits]

Solution: 227485267000992000

Count 18-digit numbers (no leading zero) in which no digit appears more than three times. Building strings digit by digit and interleaving each digit's copies, the number of length-18 strings with every digit capped at three is computed, and the strings beginning with zero (digit 0 capped at two over the remaining 17 places) are subtracted, leaving $227485267000992000$.

#pagebreak()
#link("https://projecteuler.net/problem=173")[= Problem 173: Square Laminae]

Solution: 1572729

Count the square laminae (hollow square frames) that can be built with at most $10^6$ tiles. A frame of outer width $a$ and hole width $b$ (same parity, $b < a$) uses $a^2 - b^2$ tiles. For each $a$, start from the widest hole $b = a - 2$ and shrink it; the tile count rises monotonically, so stop the moment it exceeds $10^6$. The outer loop ends once even the thinnest frame, costing $4a - 4$ tiles, no longer fits.

#pagebreak()
#link("https://projecteuler.net/problem=174")[= Problem 174: Counting the Number of Hollow Square Laminae]

Solution: 209566

A square lamina of $t$ tiles satisfies $t = a^2 - c^2$ with $a > c >= 1$ and $a equiv c thin (mod 2)$, equivalently $t = 4 d s$ with $1 <= d < s$. The number of laminae using exactly $t$ tiles is therefore the number of such factor pairs, computed by a pair-sieve. Counting how many $t <= 10^6$ admit between $1$ and $10$ laminae gives $209566$.

#pagebreak()
#link("https://projecteuler.net/problem=175")[= Problem 175: Fractions and Sum of Powers of Two]

Solution: 1,13717420,8

With $f(n)$ the hyperbinary count, the ratio $f(n)\/f(n-1)$ ranges over every positive rational, and the run lengths of $n$'s binary expansion (its shortened binary expansion) are exactly the continued-fraction quotients of that ratio. Taking the Euclidean quotients of $123456789\/987654321$, adjusting for parity, dropping zeros and reversing gives the shortened binary expansion $1,13717420,8$.

#pagebreak()
#link("https://projecteuler.net/problem=176")[= Problem 176: Rectangular Triangles That Share a Cathetus]

Solution: 96818198400000

A right triangle with integer leg $n$ comes from $n^2 = (c-b)(c+b)$, so the number of such triangles is $(tau(N^2) - 1)\/2$ where $N = n$ for odd $n$ and $N = n\/2$ for even $n$. Requiring exactly $47547$ triangles forces $tau(N^2) = 95095 = 5 dot 7 dot 11 dot 13 dot 19$. Writing this as a product of odd factors $2 e_i + 1$ and assigning the largest exponents to the smallest primes minimises $N$; the smallest $n$ is the even case $96818198400000$.

#pagebreak()
#link("https://projecteuler.net/problem=177")[= Problem 177: Integer Angled Quadrilaterals]

Solution: 129325

The diagonals of convex $A B C D$ meet at $P$, forming four triangles. With $phi = angle A P B$, the eight corner angles satisfy $a_1 + a_2 = c_1 + c_2 = 180 - phi$ and $b_1 + b_2 = d_1 + d_2 = phi$, together with the law-of-sines closure $(sin a_2 \/ sin a_1)(sin b_2 \/ sin b_1)(sin c_2 \/ sin c_1)(sin d_2 \/ sin d_1) = 1$. Iterating the integer angles $a_1, a_2, b_1, c_1$ and solving the closure for $d_1$ yields all labelled quadrilaterals; canonicalising each under the dihedral relabelling group (cyclic shifts by two and reversal) and counting distinct classes gives $129325$.

#pagebreak()
#link("https://projecteuler.net/problem=178")[= Problem 178: Step Numbers]

Solution: 126461847755

Count numbers below $10^40$ that are step numbers (consecutive digits differ by exactly one) and pandigital (use every digit). A digit DP carries the current last digit and the bit-set of digits seen; from each state the next digit is the last $plus.minus 1$, and states reaching the full mask of all ten digits are summed across lengths, yielding $126461847755$.

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
#link("https://projecteuler.net/problem=180")[= Problem 180: Rational Zeros of a Function of Three Variables]

Solution: 285196020571078987

After simplification $f_n (x, y, z) = (x + y + z)(x^n + y^n - z^n)$, so a rational zero needs $x^n + y^n = z^n$; by Fermat only $n in {-2, -1, 1, 2}$ qualify, giving $z in {x + y, sqrt(x^2 + y^2), x y \/ (x + y), x y \/ sqrt(x^2 + y^2)}$. Ranging $x, y$ over rationals $a\/b$ with $0 < a < b <= 35$ and keeping the golden triples whose $z$ is also such a rational, the distinct values of $x + y + z$ sum to $t = u\/v$ with $u + v = 285196020571078987$.

#pagebreak()
#link("https://projecteuler.net/problem=181")[= Problem 181: Grouping Objects of Two Colours]

Solution: 83735848679360680

Count the ways to split $60$ black and $40$ white objects into unordered groups. Each possible group type $(b, w) != (0, 0)$ is an item usable any number of times, so the answer is an unbounded two-dimensional knapsack: iterating each group type and accumulating $"dp"[i][j] "+"= "dp"[i-b][j-w]$ over the $61 times 41$ grid gives $83735848679360680$.

#pagebreak()
#link("https://projecteuler.net/problem=182")[= Problem 182: RSA Encryption]

Solution: 399788195976

For $p = 1009$, $q = 3643$ the number of unconcealed messages under exponent $e$ is $(1 + gcd(e - 1, p - 1))(1 + gcd(e - 1, q - 1))$. Scanning all valid $e$ coprime to $phi = (p-1)(q-1)$, the minimum value is $9$; summing every $e$ that attains it gives $399788195976$.

#pagebreak()
#link("https://projecteuler.net/problem=183")[= Problem 183: Maximum Product of Parts]

Solution: 48861552

Splitting $N$ into $k$ equal parts gives product $(N\/k)^k$, maximised near $k = N\/e$, so only the two integer neighbours need checking. The maximum is a terminating decimal exactly when the reduced denominator $k\/gcd(N, k)$ has only the prime factors $2$ and $5$; summing $-N$ for terminating cases and $+N$ otherwise over $N = 5, dots, 10000$ gives $48861552$.

#pagebreak()
#link("https://projecteuler.net/problem=184")[= Problem 184: Triangles Containing the Origin]

Solution: 1725323624056

Count triangles on lattice points inside a disk of radius $105$ that strictly contain the origin. A triangle fails this exactly when its three direction-angles fit in a closed half-plane: either the maximum angular gap exceeds $pi$ (the points lie in an open half-plane) or equals $pi$ (an antipodal pair places the origin on an edge). Counting both via integer cross-products and direction classes and subtracting from $binom(n, 3)$ leaves $1725323624056$.

#pagebreak()
#link("https://projecteuler.net/problem=185")[= Problem 185: Number Mind]

Solution: 4640261571849533

Twenty-two guesses each report how many of their sixteen digits sit in the correct position. Treating a candidate's total deviation from the required match counts as an energy, a steepest-descent local search with random restarts (changing the single digit that most reduces the deviation, restarting from a random sequence at each local minimum) drives the energy to zero, recovering the unique secret $4640261571849533$.

#pagebreak()
#link("https://projecteuler.net/problem=186")[= Problem 186: Connectedness of a Network]

Solution: 2325629

Calls are produced by the lagged-Fibonacci generator $S_k = (100003 - 200003 k + 300007 k^3) mod 10^6$ for $k <= 55$ and $S_k = (S_(k-24) + S_(k-55)) mod 10^6$ thereafter, paired into caller and called. Misdials (caller equal to called) are skipped and the rest fed to a union-find; the number of successful calls when the prime minister's component first reaches $99%$ of the million users is $2325629$.

#pagebreak()
#link("https://projecteuler.net/problem=187")[= Problem 187: Semiprimes]

Solution: 17427258

We count the composite numbers $n < N$ (with $N = 10^8$) that are a product of exactly two primes, $n = p q$ with $p <= q$.

Writing each such $n$ with its smaller factor first makes the count a sum over $p$: for a fixed prime $p$, the partners are the primes $q$ with $p <= q$ and $p q < N$, i.e. $p <= q <= floor((N - 1) \/ p)$. Counting unordered pairs this way (insisting $q >= p$) visits each semiprime once. Only primes with $p^2 < N$, that is $p < sqrt(N) approx 10^4$, can be the smaller factor, so there are barely more than a thousand outer terms.

The largest partner occurs at $p = 2$, where $q$ can reach $(N-1)\/2$, so we sieve every prime up to $N\/2$ once. For each small prime $p$ a binary search in that sorted list returns the number of primes up to $floor((N-1)\/p)$; subtracting the primes below $p$ leaves the count of valid $q$. Summing gives $17427258$ (and $10$ below $30$, matching the example).

#pagebreak()
#link("https://projecteuler.net/problem=188")[= Problem 188: Hyperexponentiation]

Solution: 95962097

Compute the tetration $1777 arrow.t arrow.t 1855$ modulo $10^8$ by repeated modular exponentiation from the top down.

#pagebreak()
#link("https://projecteuler.net/problem=189")[= Problem 189: Tri-Colouring a Triangular Grid]

Solution: 10834893628237824

Colour the $64$ triangles of an eight-row grid with three colours so that edge-sharing triangles differ. A transfer-matrix DP carries the colours of a row's upward triangles; building row $k+1$ as $U_0 D_0 U_1 dots U_k$, each downward $D_j$ must avoid its two neighbours and the triangle above, leaving $3 - |{U_j, U_(j+1), "above"_j}|$ choices. Summing the DP gives $10834893628237824$.

#pagebreak()
#link("https://projecteuler.net/problem=190")[= Problem 190: Maximising a Weighted Product]

Solution: 371048281

To maximise $x_1 x_2^2 dots x_m^m$ with $sum x_i = m$, weighted AM-GM gives $x_i = 2 i \/ (m+1)$. Evaluating the resulting product exactly as a rational and summing its floor over $m = 2, dots, 15$ yields $371048281$.

#pagebreak()
#link("https://projecteuler.net/problem=191")[= Problem 191: Prize Strings]

Solution: 1918080160

Count length-$30$ strings over ${O, A, L}$ with at most one $A$ and no three consecutive $L$. A DP over (position, absences used, trailing run of lates) tallies the valid strings to $1918080160$.

#pagebreak()
#link("https://projecteuler.net/problem=192")[= Problem 192: Best Approximations]

Solution: 57060635927998347

For each non-square $n <= 100000$, the best rational approximation to $sqrt(n)$ with denominator at most $10^12$ is either the largest continued-fraction convergent within the bound or the maximal semiconvergent built on it. Generating the convergents of $sqrt(n)$ and comparing the two candidates in high precision, the sum of the winning denominators is $57060635927998347$.

#pagebreak()
#link("https://projecteuler.net/problem=193")[= Problem 193: Squarefree Numbers]

Solution: 684465067343069

The squarefree count below $2^50$ is $sum_d mu(d) floor((2^50 - 1) \/ d^2)$. Building the Mobius function up to $2^25$ with a sieve that flips signs on prime multiples and zeros prime-square multiples, the weighted sum gives $684465067343069$.

#pagebreak()
#link("https://projecteuler.net/problem=194")[= Problem 194: Coloured Configurations]

Solution: 61190912

Units $A$ and $B$ are the same seven-vertex graph — four corners joined by vertical edges, a top edge, and a three-vertex middle chain hanging between the top and bottom corner pairs — except that $A$ also has the bottom edge. Units are glued along their vertical edges into a chain, and $N(a, b, c)$ counts the proper $c$-colourings over all arrangements of $a$ units $A$ and $b$ units $B$.

The chain structure factorises the count. Colour the leftmost vertical pair in $c(c - 1)$ ways; then each unit, read left to right, contributes an independent factor: the number of ways to colour its five new vertices given the colours of its left pair. By colour symmetry this factor depends only on the unit type and $c$ (the left pair is always properly coloured, since the vertical edge joins it), so
$
N(a, b, c) = binom(a + b, a) dot c(c - 1) dot e_A (c)^a dot e_B (c)^b,
$
where the binomial counts the distinct unit orderings ("up to translation" merely discards absolute position).

The extension counts $e_A$ and $e_B$ are degree-$5$ polynomials in $c$ (one factor per free vertex, by deletion–contraction), so brute-forcing them for $c = 2, dots, 8$ and Lagrange-interpolating gives their exact values at $c = 1984$. The formula reproduces all three given examples, and exact integer arithmetic followed by a final reduction modulo $10^8$ gives the last eight digits.

#pagebreak()
#link("https://projecteuler.net/problem=195")[= Problem 195: 60-Degree Triangle Inscribed Circles]

Solution: 75085391

Integer-sided triangles with exactly one $60$-degree angle (Eisenstein triples) split into two primitive families; since the inradius of a primitive triangle scales linearly with the triangle, each coprime parameter pair $(p, q)$ contributes $floor("bound" \/ (p q))$ scalings whose inradius stays within the limit. Summing both families reproduces $T(100) = 1234$, $T(1000) = 22767$, $T(10000) = 359912$ and gives $T(1053779) = 75085391$.

#pagebreak()
#link("https://projecteuler.net/problem=196")[= Problem 196: Prime Triplets]

Solution: 322303240771079935

In the triangle of integers each entry has up to eight neighbours. A prime belongs to a prime triplet iff it is a "centre" with at least two prime neighbours, or it neighbours such a centre. Segment-sieving the five rows around each target and applying a $3 times 3$ convolution over the prime mask to find centres and their neighbours, $S(5678027) + S(7208785) = 322303240771079935$.

#pagebreak()
#link("https://projecteuler.net/problem=197")[= Problem 197: Investigating the Behaviour of a Recursively Defined Sequence]

Solution: 1.710637717

With $f(x) = floor(2^(30.403243784 - x^2)) dot 10^(-9)$ and $u_(n+1) = f(u_n)$, the sequence settles into a 2-cycle, so $u_n + u_(n+1)$ stabilises. Iterating to convergence gives $u_n + u_(n+1) = 1.710637717$.

#pagebreak()
#link("https://projecteuler.net/problem=198")[= Problem 198: Ambiguous Numbers]

Solution: 52374425

An ambiguous number is the midpoint of a Farey-neighbour pair $a\/b < c\/d$ (with $b c - a d = 1$), so its reduced denominator is $2 b d$. Counting those in $(0, 1\/100)$ with $2 b d <= 10^8$ is a walk over the Stern-Brocot subdivision of $(0\/1, 1\/100)$, where node $(b, d)$ has children $(b, b+d)$ and $(b+d, d)$; each left spine is summed in closed form. Adding the $49$ straddling pairs $(0\/1, 1\/d)$ for $51 <= d <= 99$ gives $52374425$.

#pagebreak()
#link("https://projecteuler.net/problem=199")[= Problem 199: Iterative Circle Packing]

Solution: 0.00396087

An outer circle (curvature $-1$) holds three equal mutually tangent circles. Every gap bounded by three mutually tangent circles is filled by a Soddy circle of curvature $a + b + c + 2 sqrt(a b + b c + c a)$ (Descartes' theorem), each spawning three further gaps. Summing the areas (as $1 \/ "curvature"^2$) of all circles produced through ten iterations, the uncovered fraction is $0.00396087$.

#pagebreak()
#link("https://projecteuler.net/problem=200")[= Problem 200: Prime-Proof Squbes]

Solution: 229161792008

A sqube is $p^2 q^3$ for distinct primes $p, q$. Generating squbes up to $10^12$, keeping those whose decimal contains "200" and which are prime-proof (no single-digit change, tested by Miller-Rabin, yields a prime), the $200$th in increasing order is $229161792008$.

#pagebreak()
#link("https://projecteuler.net/problem=201")[= Problem 201: Subsets with a Unique Sum]

Solution: 115039000

From $\{1^2, dots, 100^2\}$ take all 50-element subsets and sum those totals achievable by exactly one subset. A DP over (subset size, running sum) counts realisations, capped at $2$ since only counts equal to $1$ contribute; summing those sums gives $115039000$.

#pagebreak()
#link("https://projecteuler.net/problem=202")[= Problem 202: Laserbeam]

Solution: 1209002624

Unfolding the mirror triangle into a triangular lattice turns reflection into a straight line. A beam reaching the image $(x,y)$ of $C$ is reflected $2(x+y)-3$ times, leaves early unless $gcd(x,y)=1$, and lands on a $C$-vertex iff $x equiv y space (mod 3)$. With $s = x+y = (n+3)\/2$ this counts $x in [1,s)$ coprime to $s$ with $x equiv -s space (mod 3)$; a Mobius sum over the squarefree divisors of $s = 6008819575$ gives $1209002624$ (matching the stated $2$ for $11$ bounces and $80840$ for $1000001$).

#pagebreak()
#link("https://projecteuler.net/problem=203")[= Problem 203: Squarefree Binomial Coefficients]

Solution: 34029210557338

Sum the distinct squarefree entries in the first $51$ rows of Pascal's triangle. The key fact is that every prime factor of $binom(n, k)$ with $n <= 50$ is at most $n$, so squarefreeness only needs testing against the primes up to $47$ — the large binomials themselves never have to be factored. Collect the distinct values from the left half of each row (using $binom(n, k) = binom(n, n - k)$) and add those divisible by no $p^2$.

#pagebreak()
#link("https://projecteuler.net/problem=204")[= Problem 204: Generalised Hamming Numbers]

Solution: 2944730

A type-100 Hamming number has every prime factor at most $100$. Recursively multiplying in the $25$ primes $<= 100$ and counting products $<= 10^9$ gives $2944730$.

#pagebreak()
#link("https://projecteuler.net/problem=205")[= Problem 205: Dice Game]

Solution: 0.5731441

Peter rolls nine 4-sided dice, Colin six 6-sided dice. Convolving each die distribution and summing $P("Peter" = p) dot P("Colin" < p)$ over all $p$ yields $P("Peter" > "Colin") = 0.5731441$.

#pagebreak()
#link("https://projecteuler.net/problem=206")[= Problem 206: Concealed Square]

Solution: 1389019170

The square reads $1\_2\_3\_4\_5\_6\_7\_8\_9\_0$. Ending in $0$ makes the root a multiple of $10$, and the hundreds digit $9$ forces $n equiv 30$ or $70 (mod 100)$; scanning that residue class over the valid root range finds $n = 1389019170$.

#pagebreak()
#link("https://projecteuler.net/problem=207")[= Problem 207: Integer Partition Equations]

Solution: 44043947822

Writing $x = 2^t$, every integer $x >= 2$ yields a partition with $k = x(x-1)$, perfect exactly when $x$ is a power of two. At threshold $k(x)$ the proportion is (powers of two $<= x$)$\/(x-1)$; the first $x$ where this drops below $1\/12345$ is $x = 209867$, giving $k = x(x-1) = 44043947822$.

#pagebreak()
#link("https://projecteuler.net/problem=208")[= Problem 208: Robot Walks]

Solution: 331951449665644800

The robot faces one of $5$ directions; each $72 degree$ arc has a displacement that is an integer combination of four irrational basis terms. It returns to the start exactly when all four integer coordinates vanish. A DP over (facing direction, four coordinates) for $70$ arcs counts $331951449665644800$ closed journeys (and reproduces the stated $70932$ for $25$ arcs).

#pagebreak()
#link("https://projecteuler.net/problem=209")[= Problem 209: Circular Logic]

Solution: 15964587728784

The map $tau(a_1, dots, a_6) = (a_2, dots, a_6, a_1 xor (a_2 and a_3))$ permutes the $64$ inputs into cycles. The constraint $f(x) and f(tau x) = 0$ is an independent-set condition on each cycle, counted by the Lucas number $L_n$; multiplying $L_n$ over all cycle lengths gives $15964587728784$.

#pagebreak()
#link("https://projecteuler.net/problem=210")[= Problem 210: Obtuse Angled Triangles]

Solution: 1598174770174689458

A point $B$ makes triangle $O B C$ obtuse (with $C=(r\/4, r\/4)$) in three disjoint ways: angle at $O$ gives the half-plane $x+y<0$, angle at $C$ gives $x+y > r\/2$, and angle at $B$ gives the open disk on diameter $O C$ (centre $(r\/8, r\/8)$, $R^2 = r^2\/32$). Intersecting each with the diamond $|x|+|y| <= r$ and removing the degenerate points on $x=y$ gives $N(10^9) = 1598174770174689458$ (verified against $N(4)=24$, $N(8)=100$).

#pagebreak()
#link("https://projecteuler.net/problem=211")[= Problem 211: Divisor Square Sum]

Solution: 1922364685

$sigma_2(n)$, the sum of the squares of the divisors of $n$, is built for all $n < 64 dot 10^6$ by a divisor sieve. Summing those $n$ for which $sigma_2(n)$ is a perfect square (e.g. $sigma_2(42) = 2500 = 50^2$) gives $1922364685$.

#pagebreak()
#link("https://projecteuler.net/problem=212")[= Problem 212: Combined Volume of Cuboids]

Solution: 328968937309

The $50000$ lagged-Fibonacci cuboids have integer coordinates in $[0, 10398]$. Sweeping $z$ over the distinct boundaries, each slab contributes (2D union area of the active boxes) $times$ (slab height); the area comes from an $x$-sweep with a Klee segment tree over $y$, which self-clears each slab. The union volume is $328968937309$ (matching the stated $723581599$ for the first $100$ cuboids).

#pagebreak()
#link("https://projecteuler.net/problem=213")[= Problem 213: Flea Circus]

Solution: 330.721154

Each flea performs an independent random walk on the $30 times 30$ grid, so a flea starting at $s$ is at cell $c$ after $50$ turns with probability $(T^50)_(s,c)$ for the walk matrix $T$. Raising $T$ to the 50th power by squaring, the expected number of empty squares is $sum_c product_s (1 - (T^50)_(s,c)) = 330.721154$.

#pagebreak()
#link("https://projecteuler.net/problem=214")[= Problem 214: Totient Chains]

Solution: 1677366278943

Sieving Euler's totient up to $4 dot 10^7$, the chain length satisfies $L(n) = L(phi(n)) + 1$ and is filled in ascending order (chains strictly decrease). Summing the primes $p$ (those with $phi(p) = p - 1$) whose chain length is $25$ gives $1677366278943$.

#pagebreak()
#link("https://projecteuler.net/problem=215")[= Problem 215: Crack-free Walls]

Solution: 806844323190414

Each row is a way to tile a width-$32$ strip with bricks of length $2$ and $3$, described by its set of internal crack positions. Two rows may be stacked iff their crack sets are disjoint; a DP over $10$ rows counts the crack-free walls as $806844323190414$ (the small case $W(9,3)=8$ checks out).

#pagebreak()
#link("https://projecteuler.net/problem=216")[= Problem 216: The Primality of 2n^2-1]

Solution: 5437849

$t(n) = 2n^2 - 1$ is composite exactly when some prime $p$ divides it, i.e. $n^2 equiv (p+1)\/2 space (mod p)$, which is solvable only when $2$ is a quadratic residue mod $p$ (so $p equiv plus.minus 1 space (mod 8)$). Using Tonelli--Shanks to find the roots and sieving $n equiv plus.minus r space (mod p)$, the survivors for $n <= 5 dot 10^7$ number $5437849$ (and $2202$ for $n <= 10^4$).

#pagebreak()
#link("https://projecteuler.net/problem=217")[= Problem 217: Balanced Numbers]

Solution: 6273134

A $k$-digit number is balanced when its first and last $floor(k\/2)$ digits have equal sums (an odd length leaves a free middle digit). A digit DP groups each half by digit sum $s$ and tracks both the count and the numeric-value sum of half-strings; combining the leading half (first digit $1..9$) with the trailing half over each shared $s$ gives $T(L)$. Summing $L = 1 dots 47$ and reducing mod $3^15$ yields $6273134$ (with $T(1)=45$, $T(2)=540$, $T(5)=334795890$).

#pagebreak()
#link("https://projecteuler.net/problem=218")[= Problem 218: Perfect Right-angled Triangles]

Solution: 0

A perfect triangle is a primitive triple with hypotenuse $c = d^2$, so $d^2 = m^2 + n^2$ is itself a primitive triple. Enumerating all of these for $d <= 10^8$ (i.e. $c <= 10^16$) via Euclid parameters gives $15915492$ perfect triangles, and every one has area divisible by $"lcm"(6,28)=84$. Hence the count of perfect-but-not-super-perfect triangles is $0$.

#pagebreak()
#link("https://projecteuler.net/problem=219")[= Problem 219: Skew-cost Coding]

Solution: 64564225042

An optimal prefix-free code is built greedily: repeatedly split the cheapest current leaf of weight $w$ into children of weight $w+1$ and $w+4$, which changes the total leaf-weight sum by $w+5$. Batching equal-weight leaves makes $"Cost"(10^9) = 64564225042$ instant (and $"Cost"(6)=35$).

#pagebreak()
#link("https://projecteuler.net/problem=220")[= Problem 220: Heighway Dragon]

Solution: 139776,963904

The dragon is the L-system $a arrow.r a R b F R$, $b arrow.r L F a L b$. Precomputing, for each symbol and depth, its F-step count and net (displacement, turn) lets whole blocks be skipped when they fit in the remaining budget. Walking $10^12$ steps into $D_50$ from a northward start reaches $(139776, 963904)$ (the $500$th step of $D_10$ is $(18,16)$).

#pagebreak()
#link("https://projecteuler.net/problem=221")[= Problem 221: Alexandrian Integers]

Solution: 1884161251122450

An Alexandrian integer satisfies $A = p q r$ with $1\/A = 1\/p + 1\/q + 1\/r$, which rearranges to $A = p(p+d)(p + (p^2+1)\/d)$ where $d$ ranges over divisors of $p^2+1$ (whose prime factors are only $2$ and primes $equiv 1 space (mod 4)$). The minimum $A$ for a given $p$ exceeds $4p^3$, so generating all $A <= 3 dot 10^15$ for $p <= 95000$ and sorting yields the $150000$th value $1884161251122450$ (the first six are $6, 42, 120, 156, 420, 630$).

#pagebreak()
#link("https://projecteuler.net/problem=222")[= Problem 222: Sphere Packing]

Solution: 1590933

We want the shortest pipe of internal radius $50$ mm that holds $21$ balls of radii $30, 31, dots, 50$ mm, in micrometres.

Every ball has radius more than half the pipe's, so each ball touches the wall and consecutive balls nestle on opposite sides of the axis; the problem reduces to ordering the balls. The centre of a ball of radius $r$ sits at distance $R - r$ from the axis, so for adjacent balls the centres are $r_i + r_j$ apart while their radial offsets differ by $(R - r_i) + (R - r_j)$, giving an axial gap of
$
sqrt((r_i + r_j)^2 - (2R - r_i - r_j)^2) = sqrt(4R(s - R)), quad s = r_i + r_j,
$
which depends only on the *sum* of the adjacent radii and is concave increasing in $s$. The total length is $r_"first" + r_"last"$ plus the sum of the gaps, and by concavity the sum of gaps is minimised by the valley arrangement — the smallest balls in the middle, radii growing outward alternately ($50, 48, dots, 30, dots, 49$): any deviation can be improved by an exchange. An exhaustive Held–Karp dynamic program over all $21!$ orderings (in $O(2^(21) dot 21^(2))$) confirms the valley order is optimal, at $approx 1590.933$ mm.

#pagebreak()
#link("https://projecteuler.net/problem=223")[= Problem 223: Almost Right-angled Triangles I]

Solution: 61614848

Count triangles with integer sides $a <= b <= c$, perimeter at most $25,000,000$, that are _barely acute_: $a^2 + b^2 = c^2 + 1$.

The three Barning matrices that generate the tree of Pythagorean triples preserve the quadratic form $a^2 + b^2 - c^2$, so they also act on the solutions of $a^2 + b^2 - c^2 = 1$, and the perimeter strictly grows under each. Every barely acute triple descends, by the inverse maps, to one of the roots $(1,1,1)$ or $(1,2,2)$.

Two details keep the count exact. First, normalise each node to $a <= b$ before generating children. Second, at a symmetric node ($a = b$) the first and third matrices produce mirror-image children whose subtrees coincide after normalisation, so the third child is skipped there. With those rules the forest enumerates each triangle exactly once — verified against a brute-force count up to perimeter $20,000$ — so the answer is simply the number of nodes with perimeter within the limit, traversed with an explicit stack.

#pagebreak()
#link("https://projecteuler.net/problem=224")[= Problem 224: Almost Right-angled Triangles II]

Solution: 4137330

Now the triangles are _barely obtuse_: $a^2 + b^2 = c^2 - 1$, with perimeter at most $75,000,000$.

The machinery of Problem 223 transfers unchanged, since the Barning matrices preserve $a^2 + b^2 - c^2 = -1$ as well; the only difference is the single root $(2, 2, 3)$. Normalising to $a <= b$ and skipping the mirror child at symmetric nodes again yields each triangle exactly once (verified by brute force up to perimeter $20,000$), and the node count of the pruned tree is the answer.

#pagebreak()
#link("https://projecteuler.net/problem=225")[= Problem 225: Tribonacci Non-divisors]

Solution: 2009

The tribonacci sequence taken mod $n$ is purely periodic, returning to $1,1,1$; $n$ divides some term iff a $0$ appears first. Scanning odd $n$ (the non-divisors begin $27, 81, 91, 103, dots$), the $124$th such number is $2009$.

#pagebreak()
#link("https://projecteuler.net/problem=226")[= Problem 226: A Scoop of Blancmange]

Solution: 0.11316017

The blancmange curve is $T(x) = sum_(n>=0) s(2^n x)\/2^n$. The area inside the circle $C$ (centre $(1\/4, 1\/2)$, radius $1\/4$) and under the curve is $integral_0^(1\/2) max(0, min(T(x), y_"high"(x)) - y_"low"(x)) d x$, where $y_"low","high" = 1\/2 minus.plus sqrt(1\/16 - (x - 1\/4)^2)$. Midpoint integration on a dyadic grid converges quickly (the curve is self-similar) to $0.11316017$.

#pagebreak()
#link("https://projecteuler.net/problem=227")[= Problem 227: The Chase]

Solution: 3780.618622

Track the gap between the two dice on the cycle of $100$ players. Each turn both dice move $-1\/0\/+1$ with probability $1\/6, 4\/6, 1\/6$, so the gap changes by $Delta in [-2, 2]$ with the convolved distribution. Gap $0$ is absorbing; solving the linear system for the expected absorption time from gap $50$ gives $3780.618622$.

#pagebreak()
#link("https://projecteuler.net/problem=228")[= Problem 228: Minkowski Sums]

Solution: 86226

The Minkowski sum of convex polygons has one edge per distinct edge direction. Each $S_n$ contributes directions ${90 degree + 360 degree k\/n}$, so the total number of sides is the count of distinct $k\/n space (mod 1)$ over all $n in [1864, 1909]$. Distinct reduced fractions with denominator $d$ number $phi(d)$, so the answer is $sum_(d in D) phi(d)$ over all divisors $d$ of numbers in the range, giving $86226$ (and $S_3 + S_4$ has $6$ sides).

#pagebreak()
#link("https://projecteuler.net/problem=229")[= Problem 229: Four Representations Using Squares]

Solution: 11325263

For each form $a^2 + k b^2$ with $k in {1,2,3,7}$, a sieve marks a distinct bit at every representable value up to $2 dot 10^9$. The integers carrying all four bits number $11325263$ (and $75373$ up to $10^7$).

#pagebreak()
#link("https://projecteuler.net/problem=230")[= Problem 230: Fibonacci Words]

Solution: 850481152593119296

Treating the two $100$-digit seeds $A$ (digits of $pi$) and $B$ as letters, digit position $p$ lies in block $q = (p-1) div 100$ at offset $(p-1) mod 100$. Whether block $q$ is $A$ or $B$ follows from a recursion on the Fibonacci block-counts ($F_n = F_(n-2) F_(n-1)$). Summing $10^n D((127+19n) dot 7^n)$ for $n = 0 dots 17$ gives $850481152593119296$.

#pagebreak()
#link("https://projecteuler.net/problem=231")[= Problem 231: Prime Factorisation of Binomial Coefficients]

Solution: 7526965179680

We need the sum of the terms in the prime factorisation of $binom(20\,000\,000, 15\,000\,000)$ — e.g. $binom(10, 3) = 120 = 2 dot 2 dot 2 dot 3 dot 5$ gives $14$.

By Legendre's formula the exponent of a prime $p$ in $n!$ is $sum_(i >= 1) floor(n \/ p^i)$, so its exponent $e_p$ in $binom(n, k) = n! \/ (k! (n-k)!)$ is the corresponding difference. Sieve the primes up to $n = 2 dot 10^7$ and accumulate $sum_p p dot e_p$; each prime costs only $O(log_p n)$ divisions.

#pagebreak()
#link("https://projecteuler.net/problem=232")[= Problem 232: The Race]

Solution: 0.83648556

Player 1 tosses one coin per turn and scores $1$ on heads; Player 2 chooses $T$, tosses $T$ coins, and scores $2^(T-1)$ if all are heads (probability $2^(-T)$). Player 1 starts; first to $100$ wins; Player 2 always picks the $T$ maximising her winning probability.

Index states by the points each player still needs: let $f(a, b)$ be Player 2's winning probability with Player 1 about to toss, and $g(a, b)$ with Player 2 about to toss. Then
$
f(a, b) = 1/2 A + 1/2 g(a, b), quad A = cases(g(a - 1, b) & "if" a > 1, 0 & "if" a = 1),
$
and for a choice of $T$ with $q = 2^(-T)$, $s = 2^(T-1)$,
$
g(a, b) = max_T [q W_T + (1 - q) f(a, b)], quad W_T = cases(1 & "if" s >= b, f(a, b - s) & "otherwise").
$
Player 1's tails and Player 2's failure both return to the *same* needs, so $f(a, b)$ and $g(a, b)$ depend on each other. Substituting the first equation into the second collapses each candidate $T$ to a closed form,
$
y_T = (q W_T + (1 - q) A \/ 2) / (1 - (1 - q) \/ 2),
$
and $g(a, b) = max_T y_T$. Filling states with $a$, then $b$, ascending makes $A$ and every $W_T$ already available; $T$ past the first $s >= b$ only lowers $q$, so each state checks at most $ceil(log_2 b) + 1$ choices. The answer is $f(100, 100)$, validated against the known values for games to $1$, $2$ and $4$ points.

#pagebreak()
#link("https://projecteuler.net/problem=233")[= Problem 233: Lattice Points on a Circle]

Solution: 271204031455541309

The circle through $(0, 0)$, $(N, 0)$, $(0, N)$, $(N, N)$ has centre $(N\/2, N\/2)$ and radius $N\/sqrt(2)$. The substitution $(u, v) = (2x - N, 2y - N)$ maps its lattice points bijectively onto the solutions of $u^2 + v^2 = 2N^2$ (the parity constraints come for free, since $u^2 + v^2 equiv 2N^2 (mod 8)$ forces matching parities), so the count is the sum-of-two-squares function $r_2 (2N^2) = 4 product_i (2b_i + 1)$, where the $b_i$ are the exponents of the primes $equiv 1 (mod 4)$ in $N$ — verified by direct counting for $n <= 3000$.

A count of $420$ requires $product (2b_i + 1) = 105 = 3 dot 5 dot 7$, so the exponent multiset is one of $(52)$, $(17, 1)$, $(10, 2)$, $(7, 3)$, $(3, 2, 1)$. The first two exceed $10^(11)$ even with the smallest primes $5$ and $13$. Hence $N = m k$ where the "core" $m$ carries exactly one of the three feasible signatures on distinct primes $equiv 1 (mod 4)$, and the cofactor $k$ has *no* prime factor $equiv 1 (mod 4)$.

The smallest core is $5^3 dot 13^2 dot 17 = 359125$, so cofactors never exceed $10^(11) \/ 359125 approx 2.8 dot 10^5$: sieve that range, zero out anything divisible by a prime $equiv 1 (mod 4)$, and take prefix sums $S(x)$ of the survivors. Enumerate the cores recursively (assigning each exponent of the pattern to a distinct admissible prime, pruning at the limit) and accumulate $m dot S(floor(10^(11) \/ m))$. Cross-checked against brute force at $10^6$ and $4 dot 10^6$.

#pagebreak()
#link("https://projecteuler.net/problem=234")[= Problem 234: Semidivisible Numbers]

Solution: 1259187438574927161

With $"lps"(n)$ the largest prime $<= sqrt(n)$ and $"ups"(n)$ the smallest prime $>= sqrt(n)$, an $n >= 4$ is semidivisible when exactly one of them divides $n$. Sum these up to $999,966,663,333$.

For consecutive primes $p < q$ and $p^2 < n < q^2$ we have $"lps"(n) = p$ and $"ups"(n) = q$; at $n = p^2$ both equal $p$, so prime squares are never semidivisible (this exclusion is what reproduces the stated sum $34825$ up to $1000$). Over each open interval the semidivisible sum is (multiples of $p$) plus (multiples of $q$) minus *twice* the multiples of $p q$ — the doubly divisible numbers must contribute nothing but were counted once in each term. Each piece is an arithmetic series, so a prime sieve to $approx 10^6$ and one pass over consecutive pairs (capping the last interval at the limit) finishes in milliseconds.

#pagebreak()
#link("https://projecteuler.net/problem=235")[= Problem 235: An Arithmetic Geometric Sequence]

Solution: 1.002322108633

Find $r$ with $s(5000) = sum_(k=1)^(5000) (900 - 3k) r^(k-1) = -600,000,000,000$.

At $r = 1$ the sum is $sum (900 - 3k) < 0$ but far above the target, and increasing $r$ weights the strongly negative tail (terms down to $-14100$) ever harder, so $s$ is strictly decreasing past $r = 1$ and the root is unique. Bisect on $[1, 1.1]$ with `Decimal` arithmetic at $30$ significant digits — $60$ halvings pin the root far beyond the $12$ decimal places requested.

#pagebreak()
#link("https://projecteuler.net/problem=236")[= Problem 236: Luxury Hampers]

Solution: 123/59

Suppliers A and B shipped five products in quantities $(5248, 640)$, $(1312, 1888)$, $(2624, 3776)$, $(5760, 3776)$, $(3936, 5664)$. Every per-product spoilage rate of B is $m$ times A's, yet A's overall rate is $m$ times B's. Find the largest possible $m = u\/v > 1$.

== Reduction

The supply ratios $b_i \/ a_i$ are $5\/41$, $59\/41$, $59\/41$, $59\/90$, $59\/41$: products $2$, $3$, $5$ share a ratio and pool. Per group, the spoilage counts satisfy $t \/ s = m dot b \/ a$; reducing that fraction to $p \/ q$ forces $s = q j$, $t = p j$ for a positive integer $j$, with $j <= min(a \/ q, b \/ p)$ (and $j >= 1$, since every rate must be positive for the ratios to equal $m$). The pooled group's three multipliers sum to a $K$ that ranges over the full interval $[3, K_max]$. The totals are $18880$ and $15744$, so the overall condition $sum s \/ 18880 = m dot sum t \/ 15744$ becomes
$
c_1 j_1 + c_2 K + c_4 j_4 = 0, quad c_g = 246 v q_g - 295 u p_g.
$

== Bounding the search

Substituting $t_i = m (b_i \/ a_i) s_i$ into the overall condition gives $sum s_i = m^2 (295\/246) sum (b_i \/ a_i) s_i$; since the smallest supply ratio is $5\/41$, this forces $m^2 < (246 dot 41) \/ (295 dot 5)$, i.e. $m < 2.615$ — equivalently $c_1 > 0$, while $c_2 < 0$ always. The constraint $t_1 <= 640$ reads $5u \/ gcd(5u, 41v) <= 640$, and coprimality of $u, v$ caps that gcd at $205$: either $u <= 640$, or $41 | u$ with $u <= 26240$. That leaves about $3$ million candidate fractions, and cheap per-product bound checks ($p_2 <= 1888$, $q_2 <= 1312$, ...) eliminate nearly all of them.

== Feasibility

For each survivor, existence of $(j_1, K, j_4)$ is a bounded linear Diophantine question: for each $j_1$ solve $c_4 j_4 equiv -c_1 j_1 (mod |c_2|)$ by modular inverse and step through the few admissible $j_4$, checking that $K$ lands in $[3, K_max]$. Exactly $35$ values of $m$ survive, the smallest being $1476\/1475$ — both matching the problem statement — and the largest is $123\/59$.

#pagebreak()
#link("https://projecteuler.net/problem=237")[= Problem 237: Tours on a 4 x n Playing Board]

Solution: 15836928

$T(n)$ counts the tours of a $4 times n$ board that start in the top-left corner, end in the bottom-left corner, move one square at a time, and visit every square once. We need $T(10^(12)) mod 10^8$.

A column-by-column transfer-matrix view guarantees $T$ obeys some fixed-order linear recurrence, so the recurrence can be recovered numerically: brute-force DFS gives $T(1), dots, T(11) = 1, 1, 4, 8, 23, 55, 144, 360, 921, 2329, 5924$ (matching $T(10) = 2329$ from the statement), and exact linear algebra on those terms yields the minimal order-$4$ relation
$
T(n) = 2T(n - 1) + 2T(n - 2) - 2T(n - 3) + T(n - 4),
$
which the three held-out brute-force terms confirm. Then $4 times 4$ matrix exponentiation modulo $10^8$ reaches $n = 10^(12)$ in $log n$ steps.

#pagebreak()
#link("https://projecteuler.net/problem=238")[= Problem 238: Infinite String Tour]

Solution: 9922545104535661

The Blum Blum Shub stream $s_(n+1) = s_n^2 mod 20300713$ returns to its seed after $2,534,198$ steps, so the concatenated digit string $w$ is *purely periodic*: one period has $L = 18,886,117$ digits with digit sum $D = 80,846,691$. Let $P$ be the digit prefix-sum function, $P(0) = 0$.

A substring starting at position $z$ with digit sum $k$ exists iff $k + P(z - 1) = P(e)$ for some $e >= z$. Appending whole periods adds exactly $D$ to a prefix sum while preserving the start, so existence depends only on the residue: $k$ is reachable from $z$ iff $(k + P(z - 1)) mod D in R$, where $R = {P(e) mod D : 1 <= e <= L}$. Consequently $p(k) = min{z : (k + P(z-1)) mod D in R}$ depends only on $k mod D$, and the offsets $P(z - 1) mod D$ themselves repeat with period $L$ in $z$.

Computationally: walk $z = 1, 2, dots$ and mark every still-unassigned residue in $(R - P(z-1)) mod D$ with the value $z$ (vectorised over the $approx 19$M elements of $R$); every residue is covered by $z = 89$. The statement's check value $sum_(k <= 1000) p(k) = 4742$ matches. The final sum over $k <= 2 dot 10^(15)$ is (full periods) $times sum_r p(r)$ plus a partial-period tail.

#pagebreak()
#link("https://projecteuler.net/problem=239")[= Problem 239: Twenty-two Foolish Primes]

Solution: 0.001887854841

One hundred numbered disks are shuffled into a row; we want the probability that exactly $22$ of the $25$ prime-numbered disks end up away from their natural positions — equivalently, exactly $3$ prime disks are fixed.

Choose the fixed primes in $binom(25, 3)$ ways. The other $97$ disks may permute freely except that none of the remaining $22$ prime disks may sit in its own position; by inclusion–exclusion over which of those primes are fixed anyway, that count is $sum_(j=0)^(22) (-1)^j binom(22, j) (97 - j)!$. Dividing by $100!$ and evaluating with exact rational arithmetic gives the probability to $12$ decimal places.

#pagebreak()
#link("https://projecteuler.net/problem=240")[= Problem 240: Top Dice]

Solution: 7448717393364181966

Count the ways twenty $12$-sided dice can land so that the top ten values sum to $70$ (the statement's small case: $1111$ ways for five $6$-sided dice with top three summing to $15$).

Classify each outcome by $m$, the tenth-largest value shown. If $j$ dice exceed $m$ (necessarily $j <= 9$, all of them in the top ten), the top set is completed by $10 - j$ dice showing exactly $m$, the $j$ high dice must sum to $70 - (10 - j) m$, and every other die shows at most $m$. Summing over $m$ and $j$:
- choose which dice are high, $binom(20, j)$, and count their ordered value assignments in $[m + 1, 12]$ with the required sum by a small DP;
- let $i >= 10 - j$ dice in total show $m$: choose them in $binom(20 - j, i)$ ways and give each remaining die any of the $m - 1$ smaller values.
The classification is exhaustive and disjoint (every outcome has a unique $(m, j, i)$), the small case reproduces $1111$, and the full sum is the answer.

#pagebreak()
#link("https://projecteuler.net/problem=241")[= Problem 241: Perfection Quotients]

Solution: 482316491800641154

We need every $n <= 10^(18)$ whose abundancy $sigma(n) \/ n$ equals $k + 1\/2$ — the _hemiperfect_ numbers.

Build $n$ from prime powers depth-first, tracking the remaining target $r$: if the part built so far has abundancy $a$, the still-missing coprime part $m$ must satisfy $sigma(m) \/ m = r = "target" \/ a$. Two facts drive the branching. If $r = p\/q$ in lowest terms with $q > 1$, then $q | m$ — in particular the largest prime factor of $q$ must divide $m$, so branch over its exponent. If $r$ is an integer ($>= 2$), branch over the smallest prime of $m$, pruning whenever even the product of $q \/ (q - 1)$ over all remaining primes fitting in the budget $10^(18) \/ n$ cannot reach $r$. Abundancy only grows as primes are added, so $r < 1$ prunes immediately, and $r = 1$ records a solution.

Running the search for targets $3\/2, 5\/2, dots, 13\/2$ (the abundancy of any $n <= 10^(18)$ stays below $13\/2$) finds all $22$ hemiperfect numbers in range, from $2$ up to $301183421949935616$, and their sum is the answer.

#pagebreak()
#link("https://projecteuler.net/problem=242")[= Problem 242: Odd Triplets]

Solution: 997104142249036713

$f(n, k)$ counts $k$-subsets of ${1, dots, n}$ with odd element sum; count the pairs with $n <= 10^(12)$ where $n$, $k$ and $f(n, k)$ are all odd.

Brute force over all odd $n <= 301$ reveals a clean Lucas-style law: $f(n, k)$ is odd exactly when $n = 4m + 1$, $k = 4j + 1$, and $j$ is a binary submask of $m$. Each valid $n$ therefore contributes $2^("popcount"(m))$ triplets, and the answer is $sum_(m = 0)^(M) 2^("popcount"(m))$ with $M = (10^(12) - 1) \/ 4$. That sum has a standard digit evaluation: scanning the bits of $M$ from the top, each set bit contributes $2^("ones so far") dot 3^("free bits below")$ (since $sum_(m < 2^t) 2^("popcount"(m)) = 3^t$), plus $2^("popcount"(M))$ for $m = M$ itself.

#pagebreak()
#link("https://projecteuler.net/problem=243")[= Problem 243: Resilience]

Solution: 892371480

A fraction $p\/d$ ($p < d$) is resilient when it cannot be cancelled, so the resilience of $d$ is $R(d) = phi(d) \/ (d - 1)$; find the smallest $d$ with $R(d) < 15499 \/ 94744$.

Since $phi(d) \/ d = product_(p | d) (1 - 1\/p)$ depends only on the set of prime divisors, resilience is driven down by packing in as many small distinct primes as possible — primorials. Multiply primes $2, 3, 5, dots$ until the primorial crosses the threshold; the crossing happens at the primorial through $p = 47$. A smaller witness may exist among multiples $m P_0$ of the *previous* primorial $P_0$ (for $m$ composed of primes already dividing $P_0$, $phi(m P_0) = m phi(P_0)$, so the ratio improves slightly as $d - 1$ grows): the smallest multiplier that works is $m = 4$, giving $4 P_0 = 892371480$, which beats the full primorial.

#pagebreak()
#link("https://projecteuler.net/problem=244")[= Problem 244: Sliders]

Solution: 96356848

A fifteen-puzzle variant with $7$ red and $8$ blue tiles: from the solid configuration (reds on the left, empty top-left) reach the chequerboard, where each move letter (L, R, U, D) names the direction *the tile* slides and a path's checksum folds the moves' ASCII codes by $c |-> (243c + m) mod 100000007$. Sum the checksums over all minimal-length paths.

Colour-equivalent states number only $binom(15, 7) dot 16 = 102960$, so breadth-first search from both endpoints is immediate; the shortest length is $32$. The subtlety is that each path's checksum is mod-reduced *during* the walk, so checksums of different paths wrap independently — but because the requested total is itself reported modulo $100000007$, a layered DP over the shortest-path DAG carrying (path count, checksum sum) with all arithmetic mod $p$ is exact:
$
"sum"_v = sum_(u -> v) ("sum"_u dot 243 + "count"_u dot m_(u v)).
$
The stated example (LULUR $-> 19761398$) validates the move semantics and the fold. It turns out a single shortest path exists, and its checksum is the answer.

#pagebreak()
#link("https://projecteuler.net/problem=245")[= Problem 245: Coresilience]

Solution: 288084712410001

Sum the composite $n <= 2 dot 10^(11)$ for which $C(n) = (n - phi(n)) \/ (n - 1)$ is a unit fraction — equivalently $(n - phi(n)) | (n - 1)$.

Such $n$ must be squarefree: $p^2 | n$ would put $p$ in both $n$ and $n - phi(n)$, and $n - phi(n) | n - 1$ would then force $p | 1$. Two disjoint cases remain.

*Semiprimes* $n = p q$. Writing $k = (n - 1) \/ (n - phi(n))$, the divisibility rearranges to $(p - k)(q - k) = k^2 - k + 1 =: M$. For each $k$, factor $M$ and test $p = k + d$, $q = k + e$ for every divisor pair $d e = M$. The smallest achievable $n$ is about $(k + sqrt(M))^2 >= (2k - 1)^2$, so $k$ runs to $(sqrt("limit") + 1) \/ 2 approx 223607$ — the balanced divisor pair, not $d = 1$, gives the minimum, an easy bound to get wrong. Since $x^2 - x + 1$ is odd and its prime factors are $3$ or $equiv 1 (mod 3)$, trial division needs only those primes.

*Three or more factors*: write $n = m q$ with $q$ the largest prime and $m$ composite squarefree. With $c = m - phi(m)$, the condition becomes $q (m - k c) = k phi(m) + 1$, determining $q$ for each $k$ with $m - k c > 0$ (at most about the smallest prime of $m$ values). Enumerate $m$ by DFS over ascending primes — $m p < "limit"$ is required for any valid $q > p$ — solve for $q$, check primality and verify the divisibility directly. Both cases validated against brute force to $2 dot 10^6$.

#pagebreak()
#link("https://projecteuler.net/problem=246")[= Problem 246: Tangents to an Ellipse]

Solution: 810834388

The locus of points equidistant from a circle $c$ (centre $M$, radius $r = 15000$) and an interior point $G$ satisfies $|P M| + |P G| = r$: an ellipse with foci $M(-2000, 1500)$ and $G(8000, 1500)$, so $a^2 = 7500^2 = 56250000$, $c = 5000$, and $b^2 = a^2 - c^2 = 31250000$, centred at $(3000, 1500)$. Count lattice points $P$ outside the ellipse whose two tangents to it meet at an angle greater than $45 degree$.

Centre the coordinates (the lattice shifts to the integer grid) and form the pair-of-tangents conic $S S_1 = T^2$. Its quadratic part simplifies dramatically: with $E = X^2 b^2 + Y^2 a^2 - a^2 b^2$ (positive exactly outside the ellipse) and $D = X^2 + Y^2 - (a^2 + b^2)$ (the director-circle expression),
$
A + B = D / (a^2 b^2), quad H^2 - A B = E / (a^4 b^4),
$
so the angle between the tangent *rays* exceeds $90 degree$ exactly when $D <= 0$, and otherwise equals the line angle $phi$ with $tan^2 phi = 4E \/ D^2$. The criterion is therefore the pure integer test: $E > 0$ and ($D <= 0$ or $4E > D^2$), with equality $4E = D^2$ meaning exactly $45 degree$ (excluded) and $E = 0$ the on-ellipse lattice points (no tangent pair, excluded). The test was verified against direct numeric tangent construction at thousands of random points.

On the region boundary $D^2 = 4E <= 4a^2 (X^2 + Y^2)$ gives $sqrt(X^2 + Y^2) <= a + sqrt(2a^2 + b^2) < 20000$, so a vectorised scan of one quadrant (reflecting in both axes, since only $X^2, Y^2$ appear) counts everything.

#pagebreak()
#link("https://projecteuler.net/problem=247")[= Problem 247: Squares Under a Hyperbola]

Solution: 782252

Squares are packed greedily under $y = 1\/x$ for $x >= 1$, each new square being the largest that fits. Every placed square sits in the corner $(x_0, y_0)$ of a region against the hyperbola, with side $s$ solving $(x_0 + s)(y_0 + s) = 1$, and its placement spawns two child regions: to its right (index "left" $+ 1$) and on top (index "below" $+ 1$). A max-heap on side length replays the greedy order exactly.

A square indexed $(3, 3)$ arises once per lattice path from $(0, 0)$ to $(3, 3)$, i.e. exactly $binom(6, 3) = 20$ times. Pop the heap, tracking how many $(3, 3)$ squares have appeared; the position $n$ at which the twentieth appears is the answer. Side lengths at this depth are separated by far more than double-precision error, so float ordering is exact.

#pagebreak()
#link("https://projecteuler.net/problem=248")[= Problem 248: Euler's Totient Function Equals 13!]

Solution: 23507044290

Since $phi(n) = product p^(e - 1)(p - 1)$ over the prime powers of $n$, every prime factor $p$ of a solution satisfies $(p - 1) | 13!$. Of the $1584$ divisors $d$ of $13! = 6227020800$, exactly $459$ give a prime $d + 1$ — the only primes that can appear. A DFS over strictly increasing candidate primes assigns exponents, dividing the remaining target by $(p - 1) p^(e - 1)$, and records $n$ whenever the target hits $1$. Each solution arises exactly once; sorting the $182752$ of them and taking the $150000$th gives the answer.

#pagebreak()
#link("https://projecteuler.net/problem=249")[= Problem 249: Prime Subset Sums]

Solution: 9275262564250418

Count subsets of the primes below $5000$ whose sum is prime, modulo $10^(16)$. A subset-sum DP does it directly: $"dp"[s]$ counts subsets summing to $s$, updated per prime as $"dp"[s + p] += "dp"[s]$ (one vectorised shifted-slice addition per prime; two reduced values fit in an unsigned $64$-bit word). Sums reach at most $1548136$, so a second sieve marks which sums are prime, and the answer is $sum "dp"[q]$ over prime $q$.

#pagebreak()
#link("https://projecteuler.net/problem=250")[= Problem 250: 250250]

Solution: 1425480602091519

Count non-empty subsets of ${1^1, 2^2, dots, 250250^250250}$ with sum divisible by $250$, modulo $10^(16)$. Only $i^i mod 250$ matters, so reduce each element and run a DP over the $250$ residues: an element of residue $r$ maps $"dp" -> "dp" + "shift"("dp", r)$ (include it or not). After all $250250$ elements, $"dp"[0] - 1$ (dropping the empty subset) is the answer.

#pagebreak()
#link("https://projecteuler.net/problem=251")[= Problem 251: Cardano Triplets]

Solution: 18946051

A triplet $(a, b, c)$ of positive integers is _Cardano_ when $root(3, a + b sqrt(c)) + root(3, a - b sqrt(c)) = 1$; count them with $a + b + c <= 110,000,000$.

Setting $u, v$ for the two cube roots: $u + v = 1$, $u^3 + v^3 = 2a$ and $u v = root(3, a^2 - b^2 c)$, so $u v = (1 - 2a)\/3$ and cubing gives $27 b^2 c = 27a^2 - (1 - 2a)^3 = (a + 1)^2 (8a - 1)$. Divisibility by $27$ forces $a = 3k + 2$, leaving
$
b^2 c = (k + 1)^2 (8k + 5) =: M.
$
So for each $k$ the task is to count divisors $b$ with $b^2 | M$ and $a + b + M\/b^2 <= N$ — verified for the example $(2, 1, 5)$ and against brute force to $N = 10^6$.

The square divisors come from the factorisations. $8k + 5$ is factorised for all $k$ at once by a blocked sieve over the arithmetic progression (a prime $p$ divides $8k + 5$ iff $k equiv -5/8 (mod p)$); after removing primes up to $17131$ the residual is $1$ or prime, since two larger primes would exceed $max(8k + 5) approx 2.93 dot 10^8 < 17137^2$. A smallest-prime-factor sieve handles $k + 1$, and the two factor lists merge with at most one shared prime because $gcd(k + 1, 8k + 5) | 3$. A DFS over the merged exponents enumerates $b$, pruning once $b$ exceeds the slack $N - a$, with $c$ accumulated through capped products so nothing overflows.

#pagebreak()
#link("https://projecteuler.net/problem=252")[= Problem 252: Convex Holes]

Solution: 104924.0

Find the largest-area convex polygon with vertices among $500$ pseudo-random points that contains none of the other points in its interior.

Every convex hole is counted exactly once via its lexicographically (by $(y, x)$) smallest vertex $b$: the other vertices lie lex-above $b$, so their angles around $b$ span less than $180 degree$ and the polygon decomposes into a fan of triangles $(b, v_t, v_(t+1))$ in angular order. The hole is empty iff every fan triangle contains no given point *strictly* inside (points on the boundary do not invalidate a hole — the data contains $66$ collinear triples, so the convention matters), and convexity amounts to a strict left turn at every $v_t$ (the interior angle at $b$ is automatically below $180 degree$).

Per base point: sort candidates by angle (ties by distance), precompute the strictly-empty pairs $E[i, j]$ by scanning the angular range between $i$ and $j$, then run
$
f[i, j] = "area"_2(b, q_i, q_j) + max_(k : E[k, i], "left turn at" i) f[k, i],
$
taking the global maximum over all pairs and bases. The whole procedure was validated against exhaustive subset search on the first $8$, $10$, $12$ and $14$ points before running all $500$.

#pagebreak()
#link("https://projecteuler.net/problem=253")[= Problem 253: Tidying Up A]

Solution: 11.492847

A $40$-piece caterpillar is assembled in uniformly random order; $M$ is the maximum number of contiguous segments ever present. Find $E[M]$ to six decimals.

Each placement creates a segment (no placed neighbour), extends one (one neighbour) or merges two (both neighbours). The key combinatorial fact: the number of placement orders realising a given create/extend/merge word factorises step by step — with $s$ segments present, a create can be made in $s + 1$ ways, an extend in $2s$ ways, and a merge in $s - 1$ ways. This was established empirically and then confirmed *exactly*: the products reproduce the per-word permutation counts for every operation word at $n = 4, 5, 6, 7$ under exhaustive enumeration (and in particular sum to $n!$).

With that, a DP over (current segments, maximum so far) carrying those multipliers counts all $40!$ orders by their maximum segment count; the exact rational expectation, evaluated with `Decimal`, rounds to $11.492847$.

#pagebreak()
#link("https://projecteuler.net/problem=254")[= Problem 254: Sums of Digit Factorials]

Solution: 8184523820510

With $f(n)$ the sum of factorials of $n$'s digits, $"sf"(n)$ the digit sum of $f(n)$, $g(i)$ the smallest $n$ with $"sf"(n) = i$ and $"sg"(i)$ the digit sum of $g(i)$, compute $sum_(i=1)^(150) "sg"(i)$.

$f(n)$ depends only on $n$'s digit multiset, and for a fixed value $F$ the minimal $n$ is canonical: digit $d in {1, dots, 8}$ appears $a_d <= d$ times with $sum a_d d! = F mod 9!$ (the factorial number system), plus $c = floor(F \/ 9!)$ nines, all written in ascending order — replacing $d + 1$ copies of $d!$ by one $(d + 1)!$ always shortens the number. This canonical construction was verified against brute force for every $i <= 40$.

So $g(i)$ is determined by the best $F$ with digit sum $i$, minimising first the total length $c + "len"("prefix")$. The minimal number $m_i$ with digit sum $i$ anchors the search at $c_0 = floor(m_i \/ 9!)$, and since prefixes have at most $1 + 2 + dots + 8 = 36$ digits, only windows $c in [c_0, c_0 + 36]$ can win. Within a window the $9!$ prefix values are scanned in precomputed (length, lexicographic) order, stopping at the first $p$ with $"digitsum"(c dot 9! + p) = i$ — the digit sum splits as a high part (with carry) plus a table lookup on the low six digits, and $F$ stays within $64$-bit range even at $i = 150$ ($c approx 1.9 dot 10^(11)$). Finally $"sg"(i) = 9c + sum "prefix digits"$, no astronomical $g(i)$ ever materialised.

#pagebreak()
#link("https://projecteuler.net/problem=255")[= Problem 255: Rounded Square Roots]

Solution: 4.4474011180

Heron's rounded square root starts from $x_0 = 7 dot 10^6$ (for $14$-digit $n$) and iterates $x' = floor((x + ceil(n\/x)) \/ 2)$ until $x' = x$; find the average number of iterations over all $n in [10^(13), 10^(14))$ to ten decimals.

The iteration count is piecewise constant in $n$: for fixed $x$, $ceil(n \/ x) = q$ holds on the whole interval $((q - 1)x, q x]$, and there the next estimate $x' = floor((x + q)\/2)$ is a single value. Recursively splitting the full range this way visits about $1.3 dot 10^7$ first-level intervals (one per value of $q$ at $x_0$) and only a couple of descendants each, since interval widths collapse to at most the current $x$. Summing $("interval size") times ("iteration count")$ at the leaves — with an explicit stack and exact integer arithmetic — gives the exact total, validated against direct per-$n$ simulation over all four-digit numbers ($x_0 = 70$, where the statement's example $"RS"(4321)$ takes $2$ iterations).

#pagebreak()
#link("https://projecteuler.net/problem=256")[= Problem 256: Tatami-Free Rooms]

Solution: 85765680

A room $a times b$ ($a <= b$, even size $s = a b$) is laid with $1 times 2$ tatami so that no point has four mat corners meeting; rooms admitting no such tiling are _tatami-free_, and $T(s)$ counts them per size. Find the smallest $s$ with $T(s) = 200$.

Tileability was first settled mechanically: a column-by-column DP whose state holds the protrusion mask and the vertical-pair mask of the previous column, with the four-corner rule enforced at every interior row boundary between adjacent columns. Running it for all widths $a <= 13$ over a wide range of $b$ reveals — and then confirms with zero mismatches for all $b <= 130$ — the clean characterisation (due to Ruskey and Williams): writing $b = k(a + 1) + r$,
$
"the room is tatami-free" <=> k >= 1 "and" 2 <= r <= a - 3 - 2k.
$
The rule reproduces the statement's data exactly: $T(70) = 1$ via $7 times 10$ alone, and $T(1320) = 5$ via precisely the five listed rooms.

Counting is then direct: for every width $a >= 7$ and band $k$, the free lengths form the run $k(a + 1) + 2, dots, k(a + 1) + (a - 3 - 2k)$, thinned to even $b$ when $a$ is odd. Each free room with $s <= 10^8$ increments a counter at index $s\/2$ (16-bit, since $T$ can exceed $255$ near $10^8$), and the first size with exactly $200$ is the answer.

#pagebreak()
#link("https://projecteuler.net/problem=257")[= Problem 257: Angular Bisectors]

Solution: 139012411

With bisector feet $F$ on $C A$ and $G$ on $A B$, the bisector ratios give $A F = b c \/ (a + c)$ and $A G = b c \/ (a + b)$, so $"area"(A B C) \/ "area"(A F G) = (a + b)(a + c) \/ (b c) =: R$. Count integer triangles $a <= b <= c$ with perimeter $<= 10^8$ and $R$ integral.

Since each factor $(1 + a\/b), (1 + a\/c) in (1, 2]$, an integral $R$ is $2$, $3$ or $4$. $R = 4$ forces the equilateral case ($floor(10^8\/3)$ triangles). For $k = R in {2, 3}$ the substitution $X = (k-1)b - a$, $Y = (k-1)c - a$ turns the condition into
$
X Y = k a^2,
$
where the triangle inequality $a + b > c$ is exactly $X > a$ and $b <= c$ is $X < sqrt(k) a$; for $k = 3$, integrality of $b, c$ further needs $X equiv Y equiv a (mod 2)$.

Enumerate by the divisor $X = d$: $d | k a^2$ holds precisely when $a$ is a multiple of $m(d) = product p^(ceil((e_p - v_p(k))\/2))$ over $p^(e_p) || d$, read off a smallest-prime-factor sieve. For each $d$, walk $a$ over multiples of $m(d)$ in $(d\/sqrt(k), d)$; the perimeter is increasing in $a$, so each walk stops early, and $d$ itself stops once the minimal perimeter $4.13 d$ (resp. $2.16 d$) exceeds the bound — getting these two constants right matters, and the whole enumeration was verified against full brute force for perimeters up to $12000$.

#pagebreak()
#link("https://projecteuler.net/problem=258")[= Problem 258: A Lagged Fibonacci Sequence]

Solution: 12747994

$g_k = g_(k - 2000) + g_(k - 1999)$ with $g_0 = dots = g_1999 = 1$; find $g_(10^(18)) mod 20092010$.

The characteristic polynomial is $x^2000 - x - 1$, so $x^k mod (x^2000 - x - 1)$ gives coefficients $c_i$ with $g_k = sum c_i g_i$ — and with all initial terms equal to $1$, the answer is simply the coefficient sum. Square-and-multiply over degree-$2000$ polynomials does the rest: schoolbook multiplication (reduced coefficients are below $2 dot 10^7$, so $2000$-term accumulations stay inside $64$ bits with periodic reduction), and the trinomial reduction $x^(2000 + j) = x^(j + 1) + x^j$. About $90$ polynomial multiplications cover $k = 10^(18)$; the implementation was checked against the direct recurrence for $k$ up to $5000$.

#pagebreak()
#link("https://projecteuler.net/problem=259")[= Problem 259: Reachable Numbers]

Solution: 20101196798

A positive integer is _reachable_ if an arithmetic expression using the digits $1$ to $9$ in order — with concatenation, $+$, $-$, $times$, $\/$ and arbitrary parentheses — evaluates to it. Sum the distinct reachable positive integers.

An interval DP over the digit string answers it exactly: $S[i][j]$ holds every rational reachable from digits $i$ through $j$, namely the plain concatenated number together with $x op y$ for every split point $k$ and every operation, with $x in S[i][k]$, $y in S[k+1][j]$. Values are exact normalised fractions; division only excludes zero denominators. The set sizes stay tame ($605600$ for digits $2$–$9$; $3244635$ for the full string), and the answer sums the positive integers among the $3.2$ million final values.

#pagebreak()
#link("https://projecteuler.net/problem=260")[= Problem 260: Stone Game]

Solution: 167542057

Three piles; a move removes $N > 0$ stones from one pile, from two piles ($N$ each), or from all three ($N$ each); last stone wins. Sum $x + y + z$ over all losing configurations $x <= y <= z <= 1000$ (the statement verifies $173895$ for the bound $100$).

Process sorted configurations in an order compatible with reachability (any move, after re-sorting, is component-wise $<=$). A position is losing iff no move reaches a losing position, and each move type fixes simple invariants:
- removing from one pile fixes the *other two piles* — line key ${p, q}$;
- removing from two piles fixes their *difference* and the untouched pile — key $(v - u, w)$;
- removing from all three fixes both *gaps* — key $(y - x, z - y)$.
The decisive observation is that losing positions form an antichain under moves: if one losing position could reach another, it would by definition be winning. Hence each line key is ever marked by at most one losing position, and at query time only the (earlier-processed, i.e. exactly reachable) positions have marked their keys — so three boolean tables of size $1001^2$ compute the game exactly. The $1.7 dot 10^8$ sorted triples scan in about a second, reproducing $173895$ at $n = 100$.

#pagebreak()
#link("https://projecteuler.net/problem=261")[= Problem 261: Pivotal Square Sums]

Solution: 238890850232021

$k$ is a _square-pivot_ if some $m > 0$, $n >= k$ satisfy $(k-m)^2 + dots + k^2 = (n+1)^2 + dots + (n+m)^2$; sum the distinct pivots $<= 10^(10)$.

Expanding both sides and completing squares yields a Pell-type form: with $X = 2k - m$ and $Y = 2n + m + 1$,
$
(m + 1) X^2 - m Y^2 = -m(m + 1),
$
whose solution set is permuted by the automorphism built from the unit $t^2 - 4m(m+1) s^2 = 1$, $(t, s) = (2m + 1, 2)$: $(X, Y) -> (t X + 2m Y, 2(m+1) X + t Y)$. The obvious seed $(X, Y) = (m, m + 1)$ (the degenerate pivot $k = m$, $n = 0$) generates the familiar solutions — for $m = 1$ the twin-Pythagorean pivots $4, 21, 120, dots$, for $m = 2$ the classic $10^2 + 11^2 + 12^2 = 13^2 + 14^2$ — but it is *not* the whole story: brute force at small bounds exposed $k = 820$ ($m = 8$, $n = 861$), which the inverse map traces back to a second fundamental class with seed $X = 0$, $Y = sqrt(m + 1)$, existing exactly when $m + 1$ is a perfect square. In general $m | X^2$ for any fundamental solution (since $m Y^2 = (m+1)(X^2 + m)$), so seeds are scanned over multiples of $product p^(ceil(e\/2))$ up to $m$. Orbits are expanded from $(X, Y)$ and $(-X, Y)$, keeping $n >= k$; the smallest non-trivial pivot per $m$ is $2m(m+1)$, bounding $m <= 70710$. Verified against brute force exactly to $k <= 3000$ and by total sum to $10^6$.

#pagebreak()
#link("https://projecteuler.net/problem=262")[= Problem 262: Mountain Range]

Solution: 2531.205

The exponent $|10^(-6)(x^2 + y^2) - 0.0015(x + y) + 0.7|$ vanishes on the circle centred $(750, 750)$ of radius $sqrt(425000) approx 652$, so the terrain is a closed mountain band around that circle, with crest height above $10900$ everywhere. Both $A(200, 200)$ and $B(1400, 1400)$ lie outside the band, so a constant-altitude flight must squeeze between the band and the square's edge.

The minimum feasible altitude is where the outer level set last touches a wall: a grid BFS over altitudes locates the pinch on the west edge, and exactly,
$
f_min = max_y h(0, y) = 10396.4621932 dots quad ("at" y approx 895.48),
$
with the south edge symmetric. At $f_min$ the shortest path is the taut string over the west/north side of the band: a straight segment from $A$ to a tangent point, an arc of the outer level curve through the pinch, and a straight segment to $B$. That outer curve is convex, so the geodesic is precisely the $A$-to-$B$ portion of the convex hull of ${A, B}$ together with the densely polygonised level curve — sampled on $1.2$ million rays from the band's centre with the radius bisected to machine precision — giving length $2531.20469 dots$

#pagebreak()
#link("https://projecteuler.net/problem=263")[= Problem 263: An Engineers' Dream Come True]

Solution: 2039506520

An _engineers' paradise_ $n$ requires $(n-9, n-3)$, $(n-3, n+3)$, $(n+3, n+9)$ to be three consecutive sexy prime pairs — so $n plus.minus 3$, $n plus.minus 9$ are primes with no other prime between them — and all of $n - 8, n - 4, n, n + 4, n + 8$ practical. Sum the first four.

The four primes force $n$ even, and mod $5$ they are $n+1, n+2, n+3, n+4$, so $5 | n$: hence $n equiv 0 (mod 10)$ and $n equiv.not 0 (mod 3)$. The numbers $n plus.minus 5$ are automatically composite, so consecutiveness reduces to $n plus.minus 1$ and $n plus.minus 7$ being composite. A segmented sieve to $1.5 dot 10^9$ scans $n = 10, 20, dots$ for the pattern ($59514$ survivors), and each survivor's five even neighbours are tested with Stewart's criterion for practicality ($2 | m$ and each successive prime $p <= sigma("so far") + 1$, checked against the known list of small practical numbers). The paradises are $219869980$, $312501820$, $360613700$ and $1146521020$.

#pagebreak()
#link("https://projecteuler.net/problem=264")[= Problem 264: Triangle Centres]

Solution: 2816417.1055

Count lattice triangles with circumcentre $O$ and orthocentre $H(5, 0)$, summing perimeters up to $10^5$ (the statement gives nine triangles with perimeter $<= 50$, summing to $291.0089$).

With the circumcentre at the origin, $H = A + B + C$, so the vertices lie on one circle $x^2 + y^2 = N$ with coordinate sum $(5, 0)$. Fixing $A = (a, b)$: $B + C = S = (5 - a, -b)$ and $B - C perp S$, so $B - C = j(-sigma_2, sigma_1)$ where $sigma = S\/g$ is primitive, $g = gcd(|5 - a|, |b|)$. Equal radii give $|S|^2 + |B - C|^2 = 4N$, i.e. $j^2 = (4N - g^2 q)\/q$ with $q = |sigma|^2$; and since $N = 25 - 10 g sigma_1 + g^2 q$, the divisibility $q | (4N - g^2 q)$ is exactly $q | (40 g sigma_1 - 100)$ — forcing $q <= 20|5 - 2 g sigma_1|$ and hence $|sigma| <= 40g + 3$. Enumerating pairs $(g, sigma)$ under that cap (plus $g|sigma| <= R + 5$) needs only $approx 10^8$ cheap steps, although the disk holds a billion lattice points. Each side has length $sqrt(3N + 10 a' - 25)$ ($a'$ the opposite vertex's abscissa), so all triangles are near-equilateral and the perimeter bound caps $R <= 10^5 \/ (3 sqrt(3)) + 2$. Valid $(g, sigma)$ yield $B, C = (S plus.minus D)\/2$ when parity permits; triangles, found once per vertex, are deduplicated by sorted vertex key. Verified exactly against direct triple search at perimeter bounds $50$ and $500$.

#pagebreak()
#link("https://projecteuler.net/problem=265")[= Problem 265: Binary Circles]

Solution: 209110240768

The circular arrangements of $2^N$ bits in which all $N$-bit clockwise windows differ are the binary de Bruijn sequences $B(2, N)$, and reading each from its unique run of $N$ zeros fixes the rotation. A depth-first search extends the string from $N$ zeros, tracking the used windows and finally checking the $N - 1$ wrap-around windows; summing the resulting $2^N$-bit values gives $S(3) = 52$ as stated and $S(5) = 209110240768$ across the $2^(2^4 - 5) = 2048$ sequences.

#pagebreak()
#link("https://projecteuler.net/problem=266")[= Problem 266: Pseudo Square Root]

Solution: 1096883702440585

$"PSR"(n)$ is the largest divisor of $n$ not exceeding $sqrt(n)$; find $"PSR"(p) mod 10^(16)$ for $p$ the product of the $42$ primes below $190$.

Since $p$ is squarefree, $"PSR"(p)$ is the largest subset product below $sqrt(p)$ — a knapsack on the logarithms with $2^(42)$ subsets. Meet in the middle: the primes split into halves of $21$, and all $2^(21)$ subset log-sums of each half are built by doubling. With the right half sorted, each left sum pairs with the largest right sum fitting under $log sqrt(p)$ by binary search. Floating point cannot certify the winner among near-ties, so every pairing within $10^(-6)$ of the float optimum (including the neighbour just above the searched boundary) is re-verified exactly with big integers ($d^2 <= p$), and the exact maximum is reduced mod $10^(16)$. Verified against direct subset enumeration for the primes below $30$, $50$ and $70$.

#pagebreak()
#link("https://projecteuler.net/problem=267")[= Problem 267: Billionaire]

Solution: 0.999992836187

Betting a fixed fraction $f$ of capital on each of $1000$ fair tosses (heads triples the stake), $h$ heads turn £$1$ into $(1 + 2f)^h (1 - f)^(1000 - h)$ — increasing in $h$, so reaching £$10^9$ is the tail event $h >= h_min (f)$, and the best strategy minimises $h_min$. For fixed $h$ the capital-maximising fraction solves $2h\/(1 + 2f) = (1000 - h)\/(1 - f)$, the Kelly fraction $f = (3h - 1000)\/2000$. Scanning $h$ finds the least value whose optimal fraction reaches the goal: $h^* = 432$ with $f = 0.148$. The answer is the exact binomial tail $sum_(k >= 432) binom(1000, k) \/ 2^(1000)$, evaluated with big integers and rounded to twelve decimals.

#pagebreak()
#link("https://projecteuler.net/problem=268")[= Problem 268: Counting Numbers with Four Prime Factors]

Solution: 785478606870985

Count integers below $10^(16)$ divisible by at least four distinct primes below $100$.

The weighted inclusion–exclusion
$
sum_(|S| >= 4) (-1)^(|S| - 4) binom(|S| - 1, 3) floor((N - 1) / (product S))
$
counts each integer with exactly $t >= 4$ qualifying primes once, because $sum_k (-1)^(k - 4) binom(k - 1, 3) binom(t, k) = 1$. A DFS over the $25$ primes visits only subsets whose product stays below $N$. The stated $23$ below $1000$ and a direct count below $10^5$ both check out.

#pagebreak()
#link("https://projecteuler.net/problem=269")[= Problem 269: Polynomials with at Least One Integer Root]

Solution: 1311109198529286

The digits of $n$ are the coefficients of $P_n$, so $P_n (x) > 0$ for positive $x$, and for $x <= -10$ the leading term dominates everything else: integer roots lie in ${0, -1, dots, -9}$. Inclusion–exclusion over nonempty root sets $T$ then counts, with sign $(-1)^(|T| + 1)$, the numbers vanishing at all of $-t$ for $t in T$, by a most-significant-first digit DP that carries every Horner partial value $s_t -> -t s_t + d$ simultaneously. The crucial prune: with $r$ digits still to come, the suffix contributes some value in $["lo"(t, r), "hi"(t, r)]$ (extreme alternating digit sums), so a state survives only if $s_t (-t)^r$ lies in $[-"hi", -"lo"]$ — large root sets die instantly and the whole computation takes a second. Leading zeros model shorter numbers; $n = 10^(16)$ ($P = x^(16)$, root $0$) joins separately. $Z(10^5) = 14696$ as stated.

#pagebreak()
#link("https://projecteuler.net/problem=270")[= Problem 270: Cutting Squares]

Solution: 82282080

Cuts are non-crossing straight chords between the $4N$ border lattice points of an $N times N$ square, applied until no further cut is legal; $C(N)$ counts the outcomes (rotations and reflections distinct).

Maximality makes every face a triangle with unit border edges, so $C(N)$ counts triangulations of the cyclic border-point sequence in which collinear triples (three points on one side) are forbidden — a zero-area triangle is not a piece, and a chord running along a side is not a cut. The Catalan-style interval DP $T(i, j) = sum_k T(i, k) T(k, j)$ over non-degenerate apexes $k$ (with $T(i, i+1) = 1$) runs in $O((4N)^3)$; collinear spans vanish automatically since all their apexes are degenerate. $C(1) = 2$ and $C(2) = 30$ reproduce the statement, and $C(30) mod 10^8 = 82282080$.

#pagebreak()
#link("https://projecteuler.net/problem=271")[= Problem 271: Modular Cubes, Part 1]

Solution: 4617456485273129588

$n = 13082761331670030$ is the product of the primes from $2$ through $43$, so by CRT the cube roots of unity mod $n$ are the independent combinations of cube roots mod each prime: one root when $p equiv.not 1 (mod 3)$, three for the six primes $7, 13, 19, 31, 37, 43$ — hence $3^6 = 729$ solutions. Each combination maps back through the CRT idempotents $e_p = (n\/p) dot ((n\/p)^(-1) mod p)$; the answer sums them all and removes $x = 1$. $S(91) = 363$ verifies the construction.

#pagebreak()
#link("https://projecteuler.net/problem=272")[= Problem 272: Modular Cubes, Part 2]

Solution: 8495585919506151122

$x^3 equiv 1 (mod p^e)$ has three solutions when $p equiv 1 (mod 3)$ (any $e$) or $p = 3, e >= 2$, and one otherwise; the root count is multiplicative, so $C(n) = 242$ means $243 = 3^5$ roots: exactly five contributors among the distinct primes $q equiv 1 (mod 3)$ dividing $n$, plus one for $9 | n$. Therefore either five good prime powers with $3$-part in ${1, 3}$, or four good prime powers with $3^e$, $e >= 2$ — and in both cases the leftover cofactor is _neutral_: every prime factor $equiv 2 (mod 3)$. With $G(x)$ the sum of neutral numbers up to $x$ (prefix sums of a sieve; the largest argument needed is $10^(11)\/(9 dot 7 dot 13 dot 19) approx 6 dot 10^6$), the answer is a sum over good-prime-power products $P$ of $P G(N\/P)$ (and variants with the $3$-part), enumerated by an explicit-stack DFS over the good primes with minimal-completion pruning. Verified against a direct contributor-counting sieve at $10^6$, $3 dot 10^6$ and $10^7$.

#pagebreak()
#link("https://projecteuler.net/problem=273")[= Problem 273: Sum of Squares]

Solution: 2032447591196869022

Each prime $p equiv 1 (mod 4)$ splits in $ZZ[i]$ as $pi overline(pi)$ with $pi = x + i y$, $x^2 + y^2 = p$. For squarefree $N$ a product of $k$ such primes, the representations $a^2 + b^2 = N$ with $0 <= a <= b$ correspond to the $2^(k - 1)$ conjugate-choice classes of $product (pi "or" overline(pi))$ up to units. A DFS over the $16$ primes below $150$ multiplies the canonical pair $(a, b)$ by $(x, y)$ both ways — $(|a x - b y|, a y + b x)$ and $(|a x + b y|, |b x - a y|)$ — merging the two when they coincide (the first prime), and adds $min(a, b)$ at every node, so all $3^(16)$-ish subset–class combinations are summed in one pass. Coordinates stay below $sqrt(product p) < 10^(13)$, comfortably $64$-bit. Verified against direct $a^2 + b^2$ enumeration over all subsets of the first two, three and four primes.

#pagebreak()
#link("https://projecteuler.net/problem=274")[= Problem 274: Divisibility Multipliers]

Solution: 1601912348822

Writing $n = 10q + r$, the map $f(n) = q + m r$ preserves divisibility by $p$ exactly when $f(n) equiv k n (mod p)$ for invertible $k$: comparing coefficients, $10k equiv 1$ and $m equiv k$, so the divisibility multiplier is $m = 10^(-1) mod p$ ($m = 34$ for $p = 113$ as stated). For $p$ coprime to $10$, $m = (k p + 1)\/10$ with the single digit $k$ satisfying $k p equiv -1 (mod 10)$: $k = 9, 3, 7, 1$ for $p equiv 1, 3, 7, 9$. Sieve the primes below $10^7$ and sum the closed form (sanity-checked by verifying $10 m equiv 1 (mod p)$ for every prime).

#pagebreak()
#link("https://projecteuler.net/problem=275")[= Problem 275: Balanced Sculptures]

Solution: 15030564

A balanced sculpture of order $n$ is a polyomino of $n$ blocks in $y >= 1$ plus the plinth at the origin; connectivity forces $(0, 1)$ to be a block, the blocks' torque $sum x$ must vanish, and mirror images are identified — so the answer is $(A + S)\/2$, with $A$ counting reflections as distinct and $S$ the mirror-symmetric ones. Connectivity also bounds the reach: a cell out at column $X$ needs a cell in every column $1..X$ (torque at least $X(X+1)\/2$), which the remaining cells can no longer cancel beyond $X = 8$ for $n = 18$.

$A$ comes from a broken-profile transfer-matrix DP over columns $x = -8..8$ and rows $1..18$: the state is the connectivity partition of the boundary profile plus the number of cells used — and, crucially, *not* the torque: each (profile, cells) entry stores a count vector over the feasible torque window $[max(-r R, -c R), min(-r x, 0)]$ ($r$ cells remaining), turning per-torque hashing into vector adds. States die when a boundary component vanishes prematurely (the polyomino would disconnect; the last component vanishing with all cells used and torque $0$ is tallied), or when the remaining cells cannot pay for a minimum spanning tree of the row gaps between boundary components — connected sets span whole row intervals, so each gap must eventually be filled. (A naive "sum of consecutive gaps" prune is wrong for interleaved components and silently lost three order-$10$ sculptures; the MST bound is exact-safe.) The cell $(0,1)$ is forced rather than tracked. $S$ runs the same DP on the half board $x >= 0$ with $x > 0$ cells counted twice, since a symmetric sculpture is connected iff its right half is.

Everything was validated against direct Redelmeier enumeration at orders $6$ ($A = 27$, $S = 9$) and $10$ ($A = 1825$, $S = 103$), and against the stated $360505$ at order $15$ ($A = 718474$, $S = 2536$). Order $18$: $A = 30044041$, $S = 17087$, with the seven-minute $A$ pass peaking around $1.1 dot 10^8$ window elements.

#pagebreak()
#link("https://projecteuler.net/problem=276")[= Problem 276: Primitive Triangles]

Solution: 5777137137739632912

Alcuin's sequence $T(p)$ counts integer triangles of perimeter $p$: $"round"(p^2\/48)$ for even $p$ and $"round"((p+3)^2\/48)$ for odd $p$. On each residue class $p = 12k + r$ it is an exact quadratic $3k^2 + A_r k + B_r$, so the cumulative $F(x) = sum_(p <= x) T(p)$ evaluates in $O(12)$ via Faulhaber sums. Every triangle is a unique integer multiple of a primitive one, giving $F(N) = sum_d P(floor(N\/d))$, and Möbius inversion yields
$
P(N) = sum_(d >= 1) mu(d) F(floor(N \/ d)),
$
evaluated over hyperbola blocks with Mertens prefix sums of a Möbius sieve to $10^7$. Verified against brute-force primitive-triangle counts at $N = 20, 50, 100$.

#pagebreak()
#link("https://projecteuler.net/problem=277")[= Problem 277: A Modified Collatz Sequence]

Solution: 1125977393124310

Each of the three maps divides by $3$ after a linear step, so the branch at step $i$ depends only on $a_1 mod 3^i$ — the $30$-letter prefix pins $a_1$ down to a single residue class mod $3^(30)$, and conversely every member of that class produces the same $30$ branches. The residue is lifted one base-$3$ digit at a time: among the lifts modulo $3^(k+1)$, exactly one representative reproduces the first $k + 1$ letters under direct simulation. The answer is the smallest member of the final class above $10^(15)$, re-verified by simulation; the worked example $231 -> $ "DdDddUUdDD" checks out.

#pagebreak()
#link("https://projecteuler.net/problem=278")[= Problem 278: Linear Combinations of Semiprimes]

Solution: 1228215747273908452

For distinct primes the Frobenius number of ${p q, p r, q r}$ is $f(p, q, r) = 2 p q r - p q - p r - q r$, verified by brute reachability for several triples. Summing over $p < q < r < 5000$: the $p q r$ terms total the elementary symmetric $e_3$, and each unordered pair ${u, v}$ occurs in $K - 2$ triples, so the pairwise terms total $e_2 (K - 2)$, with $e_2, e_3$ obtained from prime power sums by Newton's identities ($K = 669$ primes).

#pagebreak()
#link("https://projecteuler.net/problem=279")[= Problem 279: Triangles with Integral Sides and an Integral Angle]

Solution: 416577688

The law of cosines makes every angle of an integer triangle have rational cosine, and Niven's theorem says the only rational degree-angles with rational cosine are $60 degree$, $90 degree$ and $120 degree$. No triangle combines two of them (the angle sums fail or force irrational side ratios), so the three families partition the count, each as $sum_("primitive") floor(N \/ p)$:
- $90 degree$: $(m^2 - n^2, 2 m n, m^2 + n^2)$, coprime and opposite parity — each primitive once;
- $60 degree$: $(m^2 - n^2, 2 m n - n^2, m^2 - m n + n^2)$ over coprime $(m, n)$; the generators $(m, n)$ and $(m, m - n)$ give the same triangle, so restrict $2n <= m$ (the self-paired $(2, 1)$ yields the equilateral); the triple's gcd is $1$ or $3$ and is divided out;
- $120 degree$: $(m^2 - n^2, 2 m n + n^2, m^2 + m n + n^2)$ over coprime $(m, n)$; each primitive arises from exactly one generator of gcd $1$ and one of gcd $3$ — keep gcd $1$.
All parametrisations and uniqueness claims were verified exhaustively against brute-force primitive enumeration to perimeter $3000$, and the totals against full brute counts at $3000$ and $10000$.

#pagebreak()
#link("https://projecteuler.net/problem=280")[= Problem 280: Ant and Seeds]

Solution: 430.088247

Between pickup and drop events the ant is a plain random walk on the $25$ cells, so the chain decomposes into blocks indexed by (bottom-seed mask $B$, top-filled mask $T$, carrying $c$) with $|B| = 5 - |T| - c$. Events — stepping onto a seeded bottom cell while empty-handed, or an unfilled top cell while carrying — strictly increase the progress $("picked" + "dropped")$, so the blocks form a DAG. Solving in reverse topological order, each block is a $25$-variable linear system $E(p) = 1 + "mean"_q [E'(q) "or" E(q)]$ where event neighbours $q$ refer to the already-solved successor block, and the full-top empty-handed block absorbs at $0$. The answer is $E$ at the centre square in the initial block, $430.088247$.

#pagebreak()
#link("https://projecteuler.net/problem=281")[= Problem 281: Pizza Toppings]

Solution: 1485776387445623

Burnside over the cyclic group of the $m n$ slices: a rotation of order $d$ fixes a topping arrangement iff $d$ divides every colour count $n$, and then the fixed arrangements form the multinomial $(m n\/d; n\/d, dots, n\/d)$. Hence
$
f(m, n) = 1/(m n) sum_(d | n) phi.alt(d) ((m n\/d)!) / ((n\/d)!)^m,
$
which reproduces $f(2,1) = 1$, $f(3,1) = 2$, $f(3,2) = 16$. Since $f$ increases in $n$ and $f(m, 1) = (m - 1)!$, a double loop over $m >= 2$, $n >= 1$ with early exits collects every value at most $10^(15)$ ($m$ reaches $18$).

#pagebreak()
#link("https://projecteuler.net/problem=282")[= Problem 282: The Ackermann Function]

Solution: 1098988351

$A(m, n) = 2 arrow.t^(m-2) (n + 3) - 3$ for $m >= 2$ (checked against the recursion for small arguments), so $A(0,0), dots, A(3,3) = 1, 3, 7, 61$ exactly, $A(4,4) = 2 arrow.t arrow.t 7 - 3$, while $A(5,5)$ and $A(6,6)$ are both $2 arrow.t arrow.t h - 3$ for astronomically large heights $h$. Modulo $14^8$ the tetration $2 arrow.t arrow.t h$ is eventually constant in $h$, because the $phi.alt$-chain of the modulus collapses to $1$ within a few dozen levels; it is evaluated by the generalised Euler theorem $2^T equiv 2^(T mod phi.alt + phi.alt)$ (the exponents here always exceed $log_2 M$), exactly for heights up to $4$. Stability is verified by comparing heights $50$ and $60$.

#pagebreak()
#link("https://projecteuler.net/problem=283")[= Problem 283: Integer Sided Triangles with Integral Area/Perimeter Ratio]

Solution: 28038042525570324

The ratio equals $r\/2$ with $r$ the inradius, so ratio $k$ means $r = 2k$. With $x = s - a$, $y = s - b$, $z = s - c$, Heron's formula gives $x y z = r^2 (x + y + z)$; the half-integer branch dies on parity for even $r$, so $x <= y <= z$ are positive integers. Multiplying through by $x$ produces the key identity
$
(x y - r^2)(x z - r^2) = r^2 (x^2 + r^2),
$
so for each $k <= 1000$ and each $x <= sqrt(3) r$ the solutions correspond to divisor pairs $d_1 <= d_2$ of $N = r^2 (x^2 + r^2)$ with $x | d_1 + r^2$ (then $y = (d_1 + r^2)\/x$, $z = (d_2 + r^2)\/x$, $y >= x$). $N$ factors cheaply — $r <= 2000$ and $x^2 + r^2 <= 4 r^2 <= 1.6 dot 10^7$ sits inside a smallest-prime-factor sieve — and divisors are generated from the merged factorisation. Verified against direct $(x, y)$ scanning for $k <= 10$.

#pagebreak()
#link("https://projecteuler.net/problem=284")[= Problem 284: Steady Squares]

Solution: 5a411d7b

An $n$-digit steady square satisfies $x^2 equiv x (mod 14^n)$ — an idempotent mod $2^n 7^n$. Besides $0$ and $1$, CRT gives exactly two nontrivial idempotents, $e_1 equiv (1 mod 2^n, 0 mod 7^n)$ and $e_2 = 1 - e_1$, and they lift coherently: $e mod 14^n$ is just the $n$-digit truncation of $e mod 14^(10000)$. So both idempotents are computed once at full precision, their base-$14$ digit arrays read off, and for every $n$ whose leading digit (digit $n - 1$) is nonzero the prefix digit sum is added; $x = 1$ contributes $1$. The statement's check (total $582$ for $n <= 9$) is asserted, and the grand total is converted to base $14$.

#pagebreak()
#link("https://projecteuler.net/problem=285")[= Problem 285: Pythagorean Odds]

Solution: 157055.80999

With $x = k a + 1$, $y = k b + 1$ uniform over $[1, k+1]^2$, round $k$ scores iff $x^2 + y^2$ lands in the annulus $[(k - 1\/2)^2, (k + 1\/2)^2)$, so $P_k = (A(k + 1\/2) - A(k - 1\/2))\/k^2$ with $A(R)$ the area of ${x, y >= 1, x^2 + y^2 <= R^2}$ — the square's upper bounds never bind since $k + 1\/2 < k + 1$. From $integral sqrt(R^2 - x^2) d x = x sqrt(R^2 - x^2)\/2 + (R^2\/2) arcsin(x\/R)$, $A$ has a closed form between $x = 1$ and $sqrt(R^2 - 1)$ (zero for $R <= sqrt(2)$). The expectation $sum k P_k$ over $k <= 10^5$ was sanity-checked by Monte Carlo simulation of the first ten rounds.

#pagebreak()
#link("https://projecteuler.net/problem=286")[= Problem 286: Scoring Probabilities]

Solution: 52.6494571953

The total score is a Poisson binomial over $50$ independent shots with success probabilities $p_x = 1 - x\/q$; $P("exactly" 20)$ comes from the standard $50 times 21$ DP. As $q$ grows past $50$, every hit probability rises and the $20$-point probability falls monotonically through $0.02$ (it is $0.041$ at $q = 50^+$ and $0.0022$ at $q = 60$), so a bisection pins the unique root to ten decimals.

#pagebreak()
#link("https://projecteuler.net/problem=287")[= Problem 287: Quadtree Encoding]

Solution: 313135496

The minimal quadtree length satisfies: a uniform region costs $2$ bits, anything else costs $1$ plus its four quadrants. Against the disk $(x - 2^(23))^2 + (y - 2^(23))^2 <= 2^(46)$, a pixel box is all black iff its farthest corner lies inside, and all white iff its closest (coordinate-clamped) point lies strictly outside — two $O(1)$ tests, so the recursion only descends along the circle boundary, about $2 pi dot 2^(24)$ leaf-level cells. Verified against explicit pixel-array recursion for $N = 1$ through $7$.

#pagebreak()
#link("https://projecteuler.net/problem=288")[= Problem 288: An Enormous Factorial]

Solution: 605857431263981935

Legendre's formula gives the exponent of $p$ in $N!$ as $(N - s_p (N))\/(p - 1)$ with $s_p$ the base-$p$ digit sum — and $N(p, q) = sum T_n p^n$ has exactly the $T_n$ as its base-$p$ digits, since $0 <= T_n < p$. So $"NF"(p, q) mod p^k$ is $((N - sum T_n) mod (p - 1) p^k) \/ (p - 1)$, requiring only $N$ modulo $(p - 1) p^k$, accumulated alongside the quadratic generator. The given check $"NF"(3, 10^4) mod 3^(20) = 624955285$ is asserted.

#pagebreak()
#link("https://projecteuler.net/problem=289")[= Problem 289: Eulerian Cycles]

Solution: 6567944538

Each circle passes through the four corners of a unit square, so neighbouring circles cross at lattice points: a point on $k$ squares carries $2k$ arc-ends, and a non-crossing Eulerian cycle chooses at every lattice point a non-crossing perfect matching of those ends in their true cyclic order ($C_k$ options) such that the union of curves is a single component. The cyclic order — each circle's two tangent directions split by curvature — is computed numerically by sampling every quarter-arc near its endpoints, which the worked examples then validate. Two structural facts make the count tractable. First, for a single cycle the loop closure must be the very *last* connection in any processing order, since a curve closed early could never absorb later arcs — so the sweep forbids closures everywhere except the final vertex. Second, the cut between circle-rows is crossed only by the $2m$ side arcs (a row's top arcs peak below the next cut), so the sweep state is a non-crossing link pattern over at most $approx 14$ dangling strands — a few hundred states. Each lattice vertex consumes a contiguous frontier block (asserted) and emits strands at their geometric staircase positions; local matchings update the pattern by path-following. The construction reproduces $L(1,2) = 2$, $L(2,2) = 37$, $L(3,3) = 104290$ exactly, and $L(6,10) mod 10^(10) = 6567944538$.

#pagebreak()
#link("https://projecteuler.net/problem=290")[= Problem 290: Digital Signature]

Solution: 20444710234716473

A digit DP from the least significant end: appending digit $d$ to $n$ appends digit $(137 d + c) mod 10$ to $137 n$ with new carry $floor((137 d + c)\/10)$ — carries stay below $137$ — so the state is (carry, running digit-sum difference). After the $18$ digits the leftover carry flushes its own decimal digits into $137 n$; states with final difference zero are counted. Verified against brute force below $10^4$ and $10^5$.

#pagebreak()
#link("https://projecteuler.net/problem=291")[= Problem 291: Panaitopol Primes]

Solution: 4037526

Reducing $p = (x^4 - y^4)\/(x^3 + y^3) = (x - y)(x^2 + y^2)\/(x^2 - x y + y^2)$ with $x = g a$, $y = g b$, $gcd(a, b) = 1$: the denominator $a^2 - a b + b^2$ is coprime to both $a - b$ and $a^2 + b^2$, so it divides $g$, leaving $p = t (a - b)(a^2 + b^2)$. Primality forces $t = 1$, $a = b + 1$:
$
p = n^2 + (n + 1)^2 = 2 n^2 + 2 n + 1,
$
and conversely every such prime is attained (cross-checked against a direct $(x, y)$ search). Counting these primes below $5 dot 10^(15)$: the value is $((2n+1)^2 + 1)\/2$, so all its prime factors are $equiv 1 (mod 4)$ — sieving the $n$-array by the roots $2n + 1 equiv plus.minus sqrt(-1) (mod q)$ for *all* primes $q equiv 1 (mod 4)$ up to $sqrt(5 dot 10^(15)) < 7.1 dot 10^7$ removes every composite exactly, with no primality testing afterwards ($sqrt(-1) = r^((q-1)\/4)$ for a non-residue $r$). Verified against Miller–Rabin counting at $10^4$, $10^6$, $10^8$.

#pagebreak()
#link("https://projecteuler.net/problem=292")[= Problem 292: Pythagorean Polygons]

Solution: 3600060866

Up to translation, a convex polygon with no three collinear vertices is exactly a multiset of edge vectors with pairwise distinct directions summing to zero, and integer edge lengths make each vector $k(a, b)$ with $a^2 + b^2$ a perfect square. Splitting the angle-sorted edge cycle at $-90 degree$ (inclusive) and $+90 degree$ gives a right chain over directions ${d x > 0} union {(0, -1)}$ and a left chain over exactly their negations, so left chains are negated right chains and
$
P(n) = sum_(X, Y, p_1 + p_2 <= n) R(X, Y, p_1) R(X, Y, p_2) - 1 - \#(2"-gons"),
$
with $R$ counting right chains by displacement and perimeter via a take-at-most-one knapsack over each direction's length multiples (numpy shifted adds). The subtraction removes the empty-plus-empty term and degenerate two-edge "polygons". Verified against the given $P(4) = 1$, $P(30) = 3655$, $P(60) = 891045$.

#pagebreak()
#link("https://projecteuler.net/problem=293")[= Problem 293: Pseudo-Fortunate Numbers]

Solution: 2209

Admissible numbers below $10^9$ are products of the first $k$ primes ($2$ through at most $23$, the primorial of $29$ being too large) with all exponents at least one — $6656$ of them by DFS over exponents. For each, the pseudo-Fortunate number is the least $M > 1$ with $N + M$ prime, found by Miller–Rabin scanning (the statement's $"pf"(630) = 11$ is asserted); the $41$ distinct values sum to $2209$.

#pagebreak()
#link("https://projecteuler.net/problem=294")[= Problem 294: Sum of Digits, Experience \#23]

Solution: 789184709

Length-$n$ digit strings are governed by a linear recurrence over states (value mod $23$, digit sum capped at $23$); digit sum $23$ forces $k > 0$, so $S(n)$ is one entry of the $n$-th power of the transition. Since $n = 11^(12)$ is astronomical, the digit-sum axis is carried as a truncated generating polynomial: the transition is a $23 times 23$ matrix over $ZZ[y]\/(y^(24))$ (entry $r -> (10r + d) mod 23$ gains $y^d$), and exponentiation by squaring needs only $approx 80$ polynomial-matrix products. Verified against direct DP for the given $S(9) = 263626$ and $S(42) = 6377168878570056$.

#pagebreak()
#link("https://projecteuler.net/problem=295")[= Problem 295: Lenticular Holes]

Solution: 4884650818

Two circles with lattice centres meeting at two lattice points share a chord $P Q$ that must be a primitive vector (interior chord lattice points would lie inside the lens) with both coordinates odd (else the bisector carries no lattice centre). With $P = 0$, $Q = (a, b)$, the centres are $O_u = ((a - u b)\/2, (b + u a)\/2)$ for odd $u$, and $4 r^2 = c^2 (u^2 + 1)$, $c^2 = a^2 + b^2$ — reproducing both statement examples. Above the chord line the smaller-offset disk is contained in the larger, so the lens splits into an upper cap owned by the smaller-$u$ circle and a lower cap owned by the larger, and the two emptiness conditions decouple (the lower being the mirror of the upper). The key observation is that cap-emptiness is *linear* in $u$:
$
u <= U^* = min_(L(v) >= 1) (|v|^2 - S(v)) / L(v),
$
over lattice $v$, with $L = a v_y - b v_x$ and $S = a v_x + b v_y$. Completing the square, the level-$m$ minimiser has $S equiv (b\/a) m (mod c^2)$ nearest $c^2\/2$, giving an exact-fraction scan over ascending $m$ with a monotone stopping bound. With $U degree$ the largest odd integer $<= U^*$, the realisable radius pairs of a chord are exactly all odd $v_1 <= v_2$ with both $>= W = max(1, -U degree)$, so a $c^2$-class contributes $K(K+1)\/2$ pairs (only its largest $U^*$ over shapes matters). Pairs can coincide across classes (e.g. $4 r^2 = 20$ arises from $c^2 = 2$ and $c^2 = 10$); inclusion–exclusion over the cliques of shared values corrects this. Only chords with $c^2 < 2N$ can contribute — near-zero $U^*$ forces $(b\/a) mod c^2$ within $2N\/c$ of $0$ — enumerated with a $4 times$ margin and confirmed stable under much larger caps. Validated against direct geometric brute force at $L(10) = 30$, $L(20) = 122$, and the given $L(100) = 3442$.

#pagebreak()
#link("https://projecteuler.net/problem=296")[= Problem 296: Angular Bisector and Tangent]

Solution: 1137208419

With $a = B C$, $b = A C$, $c = A B$, the tangent-chord angle makes the line through $B$ meet $B C$ at angle $angle B A C$, and the sine rule in triangle $B C E$ collapses to $B E = a c\/(a + b)$ — verified by explicit coordinate construction of $E$ for several triangles. So $B E$ is integral iff $s' | c$ with $s' = (a + b)\/gcd(a, b)$. Writing $a = g a'$, $b = g b'$ coprime ($a' <= b'$, so $b' >= s'\/2$) and $c = k s'$, the triangle conditions $c >= b$ and $c < a + b$ become $g b' <= k s'$ and $k < g$, with perimeter $(g + k) s' <= N$. For fixed $(s', b')$ the number of valid $(g, k)$ is
$
sum_g [min(g - 1, T - g) - ceil(g b'\/s') + 1]^+, quad T = floor(N\/s'),
$
evaluated in $O(log)$ time by Euclidean floor sums, split at $g = (T+1)\/2$ with a binary search for where the second region empties. The count is non-increasing in $b'$, so the coprime $b'$ loop stops at the first zero. Verified against direct triple enumeration for $N = 100, 500, 2000$.

#pagebreak()
#link("https://projecteuler.net/problem=297")[= Problem 297: Zeckendorf Representation]

Solution: 2252639041804718029

With Fibonacci numbers $F = 1, 2, 3, 5, dots$ and $S(n) = sum_(0 < i < n) z(i)$: every number in $[F_k, F_k + j)$ is $F_k$ plus a smaller Zeckendorf tail (valid since $j <= F_(k-1)$), giving
$
S(n) = S(F_k) + (n - F_k) + S(n - F_k) quad "for" F_k < n <= F_(k+1),
$
and in particular the table recurrence $S(F_(k+1)) = S(F_k) + F_(k-1) + S(F_(k-1))$. Walking the Zeckendorf digits of $10^(17)$ then takes $O(log n)$. Verified against brute $z$-summation below $1000$ and the given $S(10^6) = 7894453$.

#pagebreak()
#link("https://projecteuler.net/problem=298")[= Problem 298: Selective Amnesia]

Solution: 1.76882294

Only the relationship between the two memories matters, never the actual numbers: Larry's memory is an LRU queue of abstract slots $1..5$ (1 = most recent) and Robin's a FIFO tuple whose symbols are Larry slots or canonically relabelled outside markers. A called number falls into four cases — a Larry element that is or isn't also in Robin's memory, a Robin-only element, or a fresh number (of which there are exactly $10 - 5 - |"Robin"| + "shared"$) — each specific element with probability $1\/10$. Canonicalisation leaves only $438$ reachable memory states; the score difference $D$ rides along as a distribution vector per state, shifted by $plus.minus 1$ on one-sided hits, and $EE|L - R|$ is read off after $50$ turns. Cross-checked by Monte Carlo simulation.

#pagebreak()
#link("https://projecteuler.net/problem=299")[= Problem 299: Three Similar Triangles]

Solution: 549936643

Brute-force shape comparison (sorted squared side lengths, gcd-normalised) over all configurations with $b + d < 100$ shows the $92$ solutions split into two disjoint families.

*Family 1* (covering every $b != d$): $P$ is the midpoint of $A C$, so $a = 2m$, and similarity reduces to $(b - a)(d - a) = 2m^2$ — verified exactly on the brute set. The unique coprime split of an ordered divisor pair of $2m^2$ is $e = 2 g alpha^2$, $f = g beta^2$ with $gcd(alpha, beta) = 1$, $beta$ odd and $m = g alpha beta$, so the perimeter constraint $b + d = 4m + e + f < N$ becomes $g(2 alpha^2 + 4 alpha beta + beta^2) < N$, two ordered pairs $(b, d)$ per triple.

*Family 2* ($b = d$): every brute row satisfies $(b - a)^2 = 2 p q$ with $q = a - p$, i.e. $b = a + 2t$ with $p + q = a$, $p q = 2 t^2$ (equivalently $a^2 - 8t^2$ a perfect square). The same coprime split ${p, q} = {2 g alpha^2, g beta^2}$ biject onto solutions, with $b + d = 2 g (2 alpha^2 + 2 alpha beta + beta^2) < N$.

Both counts are simple double loops over $(alpha, beta)$ with $g$ counted in closed form. The generated sets match brute force exactly below $100$ ($74 + 18 = 92$) and reproduce the given $320471$ at $10^5$.

#pagebreak()
#link("https://projecteuler.net/problem=300")[= Problem 300: Protein Folding]

Solution: 8.0540771484375

A protein is a string of H/P elements folded along a self-avoiding walk on the square lattice; an H-H contact is a pair of H elements occupying lattice-adjacent cells, and a string is folded to maximise contacts. We want the average optimal contact count over all $2^15$ strings of length $15$.

Consecutive H-H pairs are bonded and therefore always in contact, contributing a fixed baseline for each string; the optimisation only concerns the non-consecutive adjacent H-H pairs. So enumerate every folding shape once as the set of non-consecutive contact pairs (deduplicating identical pair-sets, and fixing the first step since contacts are rotation-invariant), then score each string as its baseline plus the maximum, over all shapes, of pairs whose two ends are both H. With shapes encoded as index pairs the scoring is pure bit-testing. The length-8 case reproduces the stated $850\/256 = 3.3203125$.

#pagebreak()
#link("https://projecteuler.net/problem=301")[= Problem 301: Nim]

Solution: 2178309

Count the $n <= 2^30$ with $n xor 2n xor 3n = 0$, the losing positions of this three-heap Nim.

#pagebreak()
#link("https://projecteuler.net/problem=303")[= Problem 303: Multiples with Small Digits]

Solution: 1111981904675169

For a positive integer $n$, $f(n)$ is the least positive multiple of $n$ whose decimal digits are all at most $2$ (drawn from ${0, 1, 2}$); we want $sum_(n=1)^(10000) f(n) \/ n$.

For a fixed $n$, find the smallest qualifying multiple by a breadth-first build of the number one digit at a time, working over the remainders modulo $n$. A state is a remainder $r$, and appending a digit $d in {0, 1, 2}$ sends $r |-> (10 r + d) mod n$. Starting from the leading digits $1$ and $2$ (no leading zero) and always trying digits in increasing order, the queue reaches candidates in order of increasing length and, within a length, increasing value; so the first time a remainder is seen it is via the smallest number reaching it, and the first time remainder $0$ is reached gives $f(n)$. Marking remainders visited keeps each search to at most $n$ states. Such a multiple always exists: a repunit $R_k$ is divisible by any $n$ coprime to $10$, and trailing zeros absorb the factors $2$ and $5$. Summing over $n <= 100$ gives $11363107$ as a check.

#pagebreak()
#link("https://projecteuler.net/problem=304")[= Problem 304: Primonacci]

Solution: 283988410192

With $a(1) = "next_prime"(10^14)$ and $a(n) = "next_prime"(a(n-1))$, the $a(n)$ are the consecutive primes just above $10^14$. Writing $f$ for the Fibonacci sequence and $b(n) = f(a(n))$, we need $sum_(n=1)^(100000) b(n)$ modulo $m = 1234567891011$.

Two ingredients suffice. The primes are collected by stepping through odd numbers above $10^14$ and applying a deterministic Miller–Rabin test; the gaps average $ln(10^14) approx 32$, so a hundred thousand primes need only a couple of million candidates. Each Fibonacci value is taken modulo $m$ by fast doubling,
$ F(2k) = F(k) (2 F(k+1) - F(k)), quad F(2k+1) = F(k)^2 + F(k+1)^2, $
processing the bits of the index from the most significant down. Since $m approx 1.2 dot 10^12$, a product of two residues can reach $1.5 dot 10^24$ and overflow $64$ bits, so the multiplications use an overflow-safe modular routine (correct for $m < 2^62$). Summing the residues gives the answer.

#pagebreak()
#link("https://projecteuler.net/problem=305")[= Problem 305: Reflexive Position]

Solution: 18174995535140

Let $S = 123456789101112dots$ be the concatenation of the positive integers, and $f(n)$ the start position of the $n$-th occurrence of the digit-string of $n$ in $S$. We need $sum_(k=1)^13 f(3^k)$, with positions running up to about $1.8 dot 10^13$.

The engine is a counter $C(P, m)$ giving the number of occurrences of a pattern $P$ (of length $L$) that *start* inside one of the numbers $1, dots, m$. Grouping by the digit-length $d$ of the starting number, an occurrence is either internal (the $L$ characters lie within a single number, counted by a digit-DP that pins $P$ across a fixed window) or it straddles a boundary (a suffix of the current number followed by the start of the next ones). For the straddling case, when the number has at least $L$ digits and the matched suffix is not all nines, incrementing leaves the upper digits fixed, so the condition collapses to a number that simultaneously starts with the pattern's tail and ends with its head — again a digit-DP; the few genuine carries and very short numbers are handled directly.

With $C$ in hand, $f(n)$ is a binary search for the number $m$ containing the $n$-th occurrence, after which the exact character offset within $m$ is read off and added to the precomputed length of $1 dots (m-1)$. The given $f(1) = 1$, $f(5) = 81$, $f(12) = 271$ and $f(7780) = 111111365$ confirm the construction.

#pagebreak()
#link("https://projecteuler.net/problem=306")[= Problem 306: Paper-strip Game]

Solution: 852938

Two players alternately paint two contiguous white squares of a length-$n$ strip black; whoever cannot move loses. We count the $n <= 10^6$ that are wins for the first player.

Painting two adjacent squares of a length-$k$ strip removes them and splits the rest into two independent strips whose lengths sum to $k - 2$, so the Sprague–Grundy value obeys
$ G(k) = "mex" {G(a) xor G(b) : a + b = k - 2, space a, b >= 0}, $
with $G(0) = G(1) = 0$. A single strip of length $n$ is a first-player win exactly when $G(n) != 0$. Computing the sequence is quadratic, but it is eventually periodic: the values settle into a cycle of period $34$ after a short preperiod (here the first $53$ terms). Generating a few thousand terms, detecting and verifying the period, then extending by $G(n) = G("pre" + (n - "pre") mod 34)$, lets the count reach $10^6$ at once. For $1 <= n <= 5$ the wins are $n = 2, 3, 4$, as stated.

#pagebreak()
#link("https://projecteuler.net/problem=307")[= Problem 307: Chip Defects]

Solution: 0.7311720251

With $k$ independent, uniformly placed defects spread over $n$ chips, $p(k, n)$ is the probability that some chip carries at least three defects; we need $p(20000, 1000000)$ to ten decimal places.

Work with the complement, where every chip holds $0$, $1$ or $2$ defects. If exactly $j$ chips hold a pair (using $2j$ of the labelled defects) and the other $k - 2j$ defects sit alone, the number of placements is $binom(n, j) binom(n - j, k - 2j) k! \/ 2^j$; dividing by $n^k$ makes it a probability $t_j$. The ratio of consecutive terms telescopes to
$ t_j / t_(j-1) = ((k - 2j + 2)(k - 2j + 1)) / (2 j (n + j - k)), $
starting from $t_0 = product_(i=0)^(k-1) (n - i) \/ n$ (all defects in distinct chips). Then $p = 1 - sum_(j=0)^(floor(k\/2)) t_j$. The terms span dozens of orders of magnitude (with $t_0 approx e^(-200)$), so the running sum is carried in extended precision; $p(3, 7) approx 0.0204081633$ confirms the recurrence.

#pagebreak()
#link("https://projecteuler.net/problem=309")[= Problem 309: Integer Ladders]

Solution: 210139

Two ladders of integer lengths lean across a street of integer width $w$, crossing at integer height $h$ above the road. For lengths $0 < x < y < 10^6$, how many triples $(x, y, h)$ admit an integer $w$?

Let the ladders meet the opposite walls at heights $X = sqrt(x^2 - w^2)$ and $Y = sqrt(y^2 - w^2)$. Similar triangles give the optic equation $1\/h = 1\/X + 1\/Y$, that is $h = (X Y) \/ (X + Y)$. Were $X$ or $Y$ irrational, $h$ could not be rational, so both wall heights are integers and $(w, X, x)$, $(w, Y, y)$ are Pythagorean triples. Writing the two heights as $X_1 < X_2$, the crossing height is an integer exactly when
$ (X_1 + X_2) divides X_1^2, quad "because" quad h = X_1 - X_1^2 / (X_1 + X_2). $

So enumerate every Pythagorean triple with hypotenuse below $10^6$. Each triple ${p, q, c}$ gives two configurations: width $p$ with wall height $q$, and width $q$ with wall height $p$. For a configuration of width $w$ and smaller height $X_1$, the admissible partners are $X_2 = D - X_1$ for each divisor $D$ of $X_1^2$ with $D > 2 X_1$ (forcing $X_2 > X_1$); such an $X_2$ counts when $w^2 + X_2^2$ is itself a perfect square below the limit. Each valid pair is reached once. There are $5$ triples below $200$ and $146$ below $1600$, matching the known checks.

#pagebreak()
#link("https://projecteuler.net/problem=310")[= Problem 310: Nim Square]

Solution: 2586528661783

Nim Square is three-heap normal-play Nim in which a move removes a positive square number of stones from one heap. For positions $(a, b, c)$ with $0 <= a <= b <= c <= 10^5$, how many are losing for the player to move?

A single heap of size $s$ has Grundy value
$ g(s) = "mex" {g(s - i^2) : i >= 1, space i^2 <= s}, $
found for all $s <= 10^5$ in one sweep — each heap needs only the $approx 316$ square subtractions, and the values stay small (at most $74$). As in ordinary Nim, a three-heap position is losing precisely when $g(a) xor g(b) xor g(c) = 0$.

A direct $O(N^3)$ scan is hopeless, so tally how many heap sizes carry each Grundy value and let $T$ be the number of *ordered* triples with vanishing XOR, read off from the pairwise XOR-distribution of those tallies (the value range is tiny). Convert ordered to sorted counts: an all-equal triple needs $g = 0$; a multiset ${p, p, q}$ has XOR $g(q)$, so it vanishes iff $g(q) = 0$ (with $p$ free); and the all-distinct multisets are what remains of $T$ after removing those degenerate orderings and dividing by $6$. Summing the three classes gives $1160$ for the bound $29$ and the stated answer at $10^5$.

#pagebreak()
#link("https://projecteuler.net/problem=311")[= Problem 311: Biclinic Integral Quadrilaterals]

Solution: 2466018557

A biclinic integral quadrilateral $A B C D$ is convex with $1 <= A B < B C < C D < A D$, integer $B D$, and $A O = C O <= B O = D O$ all integer, where $O$ is the midpoint of $B D$. With $a = A O = C O$ and $d = B O = D O$, the median (parallelogram) law gives $A B^2 + A D^2 = B C^2 + C D^2 = 2(a^2 + d^2)$, so the side-square sum equals $4(a^2 + d^2) <= N$.

Place $O$ at the origin with $B, D$ on the $x$-axis. A side pair $(p, q)$ for $A$ satisfies $p^2 + q^2 = 2(a^2 + d^2)$; the substitution $(p, q) = (u - w, u + w)$ converts each into a representation $u^2 + w^2 = a^2 + d^2$. So a quadrilateral is just three distinct representations of a common $V = a^2 + d^2 = x^2 + y^2$: the one with smallest $x - y$ supplies $(d, a)$ -- the always-present degenerate split, here excluded -- and the other two give the nested side pairs. Since every representation has a distinct $x - y$, the count for a given $V$ is exactly $binom(r(V), 3)$, where $r(V)$ counts representations with $x >= y >= 1$.

Thus $B(N) = sum_(V <= N\/4) binom(r(V), 3)$, evaluated by counting representations in memory-bounded blocks of $V$. The checks $B(10^4) = 49$ and $B(10^6) = 38239$ confirm it.

#pagebreak()
#link("https://projecteuler.net/problem=312")[= Problem 312: Cyclic Paths on Sierpiński Graphs]

Solution: 324681947

$C(n)$ counts the Hamiltonian cycles of the order-$n$ Sierpiński graph $S_n$; we need $C(C(C(10000))) mod 13^8$.

== The closed form

Counting cycles by pruned backtracking on the actual graphs gives $C(3) = 8$ (matching the problem) and $C(4) = 13824 = 8 dot 12^3$. Together with the given $C(5) = 71328803586048 = 8 dot 12^12$, the exponents $0, 3, 12$ fit
$
C(n) = 8 dot 12^((3^(n-2) - 3) \/ 2),
$
which the structure of the graph explains: the three outer corners of $S_n$ have degree $2$, forcing the cycle through them, and the cycle decomposes into three corner-to-corner Hamiltonian paths, one per order-$(n-1)$ sub-triangle, whose counts multiply and obey a tripling recursion. The formula is then confirmed at $n = 10000$ against *both* given residues, $C(10000) equiv 37652224 space (mod 10^8)$ and $equiv 617720485 space (mod 13^8)$ — five independent data points in all.

== The tower

$C(C(C(10000)))$ is a power tower, so the exponents are reduced with the generalised Euler lift: for *any* base $b$ and modulus $m$, $b^E equiv b^(E mod phi(m) + phi(m)) space (mod m)$ once $E >= log_2 m$ — a condition every exponent here satisfies astronomically. The quantity $t(x) = (3^(x-2) - 3) \/ 2$ is handled exactly by working modulo $2m$ before halving (the numerator is always even), and the value of the inner $C$'s feeds the next level's exponent through a short mutual recursion on shrinking moduli. The whole evaluation is a handful of modular exponentiations.

#pagebreak()
#link("https://projecteuler.net/problem=313")[= Problem 313: Sliding Game]

Solution: 2057774861813004

A red counter starts in the top-left corner of an $m times n$ grid and the blank space in the bottom-right; counters slide into the blank, and $S(m, n)$ is the minimum number of moves to bring the red counter to the bottom-right corner. We count the grids with $S(m, n) = p^2$ over primes $p < 10^6$.

Every counter except the red one is interchangeable, so a position of the puzzle is fully described by the pair (red square, blank square) — a state space of size $m n (m n - 1)$ rather than $(m n)!$. Breadth-first search over these states gives $S$ exactly for small grids, confirming $S(5, 4) = 25$ and revealing a clean structure for $m > n >= 2$:
$
S(m, n) = 6m + 2n - 13,
$
with the separate diagonal family $S(n, n) = 8n - 11$ (and the special case $S(2, 2) = 5$). The shape of the formula is intuitive: the blank must first travel to the red counter, and thereafter each unit of red progress along the long side costs $6$ moves (the blank circles around the red counter between pushes) while the final approach along the diagonal is cheaper.

Neither family can produce $p^2$ except through the first formula. For odd $p$, $p^2 equiv 1 space (mod 8)$ while $8n - 11 equiv 5 space (mod 8)$, so the diagonal never matches; and $6m + 2n - 13$ is odd, ruling out $p = 2$. For each odd prime set $t = (p^2 + 13) \/ 2$, so the equation $6m + 2n - 13 = p^2$ becomes $3m + n = t$. The constraints $n >= 2$ and $m > n$ pin $m$ to the interval $t\/4 < m <= (t - 2)\/3$, giving $floor((t - 2)\/3) - floor(t\/4)$ grids, doubled to count both orientations. Summing over a sieve of the primes below $10^6$ reproduces the stated $5482$ grids for $p < 100$ and yields the answer.

#pagebreak()
#link("https://projecteuler.net/problem=315")[= Problem 315: Digital Root Clocks]

Solution: 13625242

Two seven-segment clocks each display a number, then repeatedly its digit sum down to a single digit, beginning and ending blank. Sam's clock clears and relights every segment at each step; Max's only toggles the segments that change. The answer is Sam's total segment transitions minus Max's, summed over the primes in $[10^7, 2 dot 10^7)$.

Sieve that prime range rather than testing each number for primality, and compute both transition counts per prime with integer digit arithmetic. For a step $a -> b$, Sam's cost is the total lit-segment count of $a$ plus that of $b$, while Max's cost is the sum over aligned digit positions of the population count of the segment-pattern XOR (a blank screen contributing the all-off pattern).

#pagebreak()
#link("https://projecteuler.net/problem=316")[= Problem 316: Numbers in Decimal Expansions]

Solution: 542934735751917735

A stream of uniformly random decimal digits is read until the digit string of $n$ first appears; $g(n)$ is the expected (1-based) index of the *first* digit of that occurrence. We need $sum_(n=2)^(999999) g(floor(10^16 \/ n))$.

The heart of the problem is the classical fair-casino (Conway leading number) argument. Imagine that just before each stream position a fresh gambler bets $1$ that the pattern starts there, parlaying digit by digit at fair odds of $10 : 1$ per digit. The total amount wagered is always exactly the number of digits revealed, and the game is fair, so the expected number of digits read when the pattern completes equals the total stake still live at that moment. A gambler is still live exactly when the last $L$ digits — a suffix of the pattern — coincide with a prefix of the pattern, i.e. for every *border* of the pattern (a string that is both prefix and suffix, the full pattern included), and that gambler holds $10^L$. Hence the expected index of the pattern's final digit is $sum_b 10^(|b|)$ over all nonempty borders $b$, and the expected start index subtracts $d - 1$ for a $d$-digit pattern. The problem's example confirms it: $535$ has borders $535$ and $5$, so $g(535) = 10^3 + 10 - 2 = 1008$.

The borders of each pattern are read off the KMP failure function — the longest proper border, then its longest border, and so on. A million patterns of at most $16$ digits take well under two seconds, and the stated check value $sum_(n=2)^(999) g(floor(10^6 \/ n)) = 27280188$ verifies the whole pipeline.

#pagebreak()
#link("https://projecteuler.net/problem=317")[= Problem 317: Firecracker]

Solution: 1856532.8455

A firecracker bursts at height $h_0 = 100$; its fragments scatter in every direction at speed $v = 20$ and then fall under gravity $g = 9.81$. We want the volume of the region their paths sweep before landing.

Each fragment follows a parabolic arc, and over all launch directions the family of trajectories has as its envelope the _parabola of safety_,
$ Y(r) = h_0 + v^2/(2 g) - (g r^2)/(2 v^2), $
the greatest height reachable at horizontal distance $r$. The swept solid is everything between the ground and this envelope, revolved about the vertical axis. Writing $A = h_0 + v^2/(2 g)$ for the apex height and $B = g/(2 v^2)$, the envelope meets the ground at $r_max^2 = A\/B$, and the shell integral collapses:
$ V = integral_0^(r_max) 2 pi r (A - B r^2) dif r = (pi A^2)/(2 B) = (pi A^2 v^2)/g approx 1856532.8455. $

#pagebreak()
#link("https://projecteuler.net/problem=318")[= Problem 318: 2011 Nines]

Solution: 709313889

For $p < q$ with $p + q <= 2011$, consider numbers $sqrt(p) + sqrt(q)$ whose even powers have fractional parts approaching $1$; $N(p, q)$ is the least $n$ for which the fractional part of $(sqrt(p) + sqrt(q))^(2n)$ begins with $2011$ nines, and we sum $N$ over the qualifying pairs.

Let $e = (sqrt(p) + sqrt(q))^2$ and $d = (sqrt(q) - sqrt(p))^2 = p + q - 2 sqrt(p q)$. Expanding $d^n + e^n$, the odd powers of $sqrt(p q)$ cancel, so the sum is an integer and the fractional part of $e^n$ equals $1 - d^n$. It therefore approaches $1$ exactly when $d < 1$ — and if $p q$ is a perfect square, $d$ is a positive integer, so those degenerate pairs exclude themselves. The condition $d < 1$ also caps the search: $q - p - 1 < 2 sqrt(p)$, a band of width about $2 sqrt(p)$ above each $p$, around $42000$ pairs in all.

The fractional part $1 - d^n$ starts with at least $2011$ nines exactly when $d^n <= 10^(-2011)$, so $N(p, q) = ceil(2011 \/ (-log_10 d))$. The only delicacy is numerical: $d$ can sit near $1$, making $N$ in the millions, and an ordinary float could round the ceiling the wrong way. Evaluating with $80$-digit decimals and asserting that the quotient never falls within $10^(-30)$ of an integer makes the ceiling provably correct ($d$ is irrational, so exact boundary hits are impossible).

#pagebreak()
#link("https://projecteuler.net/problem=321")[= Problem 321: Swapping Counters]

Solution: 2470433131948040

With $n$ red and $n$ blue counters at opposite ends of a row of $2 n + 1$ squares (one empty square between them), $M(n)$ is the fewest slides and hops needed to swap the two colours. We want the sum of the first forty values of $n$ for which $M(n)$ is a triangular number.

First, $M(n) = n^2 + 2 n$: each of the $2 n$ counters must advance $n + 1$ squares, giving $2 n (n + 1)$ square-steps; a hop advances two squares and a slide one, and the $n^2$ red–blue meetings are exactly the hops, leaving $2 n$ slides, so $M(n) = 2 n (n + 1) - n^2 = n^2 + 2 n$ (indeed $M(3) = 15$). Requiring $n^2 + 2 n = k (k + 1) \/ 2$ and completing the square turns this into the Pell-like equation
$ m^2 - 8 u^2 = -7, quad u = n + 1, space m = 2 k + 1. $
Its positive solutions split into two classes, generated from the fundamentals $(m, u) = (1, 1)$ and $(5, 2)$ by the unit $3 + sqrt(8)$, that is $(m, u) |-> (3 m + 8 u, m + 3 u)$. Merging the resulting $u$-values in increasing order (dropping $u = 1$) gives $n = u - 1 = 1, 3, 10, 22, 63, dots$; the first five sum to $99$ and the first forty to the answer.

#pagebreak()
#link("https://projecteuler.net/problem=322")[= Problem 322: Binomial Coefficients Divisible by 10]

Solution: 999998760323313995

$T(m, n)$ counts the binomial coefficients $binom(i, n)$ divisible by $10$ for $n <= i < m$; we need $T(10^18, 10^12 - 10)$.

Divisibility by $10$ is divisibility by both $2$ and $5$, so by inclusion–exclusion
$
T(m, n) = (m - n) - A_2 - A_5 + A_(2,5),
$
where $A_p$ counts $i$ in $[n, m)$ with $binom(i, n)$ *not* divisible by $p$. By Kummer's theorem $binom(i, n)$ is coprime to a prime $p$ exactly when adding $n$ to $i - n$ in base $p$ produces no carry — equivalently (Lucas) every base-$p$ digit of $n$ is at most the corresponding digit of $i$. Each $A_p$ is then a base-$p$ digit DP counting $i < m$ whose digits dominate $n$'s (the domination already forces $i >= n$).

The joint term $A_(2,5)$ is the crux: it needs the base-$2$ and base-$5$ digit conditions simultaneously, and the two radices never align. Two observations make it cheap. First, the base-$2$ condition is just the binary supermask test $(i and n) = n$. Second, the base-$5$ condition depends only on $i mod 5^k$ (with $5^k > n$), so it is fixed by choosing the low $k$ base-$5$ digits of $i$ to dominate $n$'s. For $n = 10^12 - 10$ almost all of $n$'s base-$5$ digits equal $4$, forcing $i$'s digit there to be exactly $4$, so only a few thousand low residues survive; for each, a short sweep of the high part $h$ (with $i = h dot 5^k + r < m$) keeps those $i$ that are binary supermasks of $n$. The whole evaluation runs in about a second, and the given $T(10^9, 10^7 - 10) = 989697000$ confirms it.

#pagebreak()
#link("https://projecteuler.net/problem=323")[= Problem 323: Bitwise-OR Operations on Random Integers]

Solution: 6.3551758451

Each step ORs in a random $32$-bit integer; the expected number of steps is $sum i dot p(i)$, where $p(i)$ comes from differencing the closed-form chance that all bits are set by step $i$.

#pagebreak()
#link("https://projecteuler.net/problem=324")[= Problem 324: Building a Tower]

Solution: 96972774

$f(n)$ counts the fillings of a $3 times 3 times n$ tower with $2 times 1 times 1$ blocks; we need $f(10^10000) mod 100000007$.

A block is either flat within a layer (two in-plane orientations) or vertical, straddling two consecutive layers. The interface between layers is therefore described by the $9$-bit mask of cells protruding upward, giving a $512 times 512$ transfer matrix $T$: entry $T[s][s']$ counts the ways to complete one layer whose mask-$s$ cells arrive occupied from below while protruding mask $s'$ upward, enumerated by a first-free-cell recursion. Then $f(n) = (T^n)[0][0]$, which reproduces $f(2) = 229$ and $f(4) = 117805$ exactly (and $f$ vanishes at odd $n$, where the cell count is odd).

Raising a $512 times 512$ matrix to the $10^10000$ is hopeless, but $f(n) = e_0^T T^n e_0$ means the even subsequence $g(k) = f(2k)$ satisfies a linear recurrence of degree at most $512$. Berlekamp–Massey on $200$ generated terms (modulo the prime $q = 10^8 + 7$) finds the minimal recurrence has degree just $19$, and it provably reproduces every remaining generated term. Kitamasa evaluation — computing $x^(n\/2)$ modulo the degree-$19$ characteristic polynomial by binary exponentiation over the $approx 33000$-bit exponent — then gives $g$ at $k = 5 dot 10^9999$ in milliseconds. The three remaining given residues, $f(10)$, $f(10^3)$ and $f(10^6)$, all verify through the same pipeline.

#pagebreak()
#link("https://projecteuler.net/problem=325")[= Problem 325: Stone Game II]

Solution: 54672965

Two piles; a move removes a positive multiple of the smaller pile from the larger; emptying a pile wins. $S(N)$ sums $x + y$ over the losing configurations $0 < x < y <= N$, and we need $S(10^16) mod 7^10$.

This is the Euclid game, whose P-positions have the famous golden-ratio characterisation: $(x, y)$ with $x < y$ is losing exactly when $y < phi x$. The solution does not take this on faith — a memoised game-tree search verifies it for every pair up to $40$. The intuition: when $y < phi x$ the only legal move is $y -> y - x$, which lands at ratio above $phi$; when $y > phi x$ the mover can always choose the multiple landing inside the strip.

So $S(N)$ sums $x + y$ over $x < y <= min(floor(phi x), N)$. For $x$ below $x_1 = floor(N \/ phi) + 1$ the cap is $F(x) = floor(phi x)$ and the contribution involves the three Beatty power sums $sum F$, $sum x F$ and $sum F^2$; beyond $x_1$ the cap is $N$ and Faulhaber's formulas finish in closed form. The Beatty sums are computed by counting lattice points under $y = phi x$ and reflecting: each sum over $x <= n$ becomes the same triple of sums over $y <= m = floor(n \/ phi)$ — because $1\/phi = phi - 1$, the recursion calls itself at $m < 0.62 n$ and terminates in $O(log N)$ exact-integer steps (with $floor(n \/ phi)$ evaluated exactly through $floor(n sqrt(5)) = "isqrt"(5 n^2)$). Both check values, $S(10) = 211$ and $S(10^4) = 230312207313$, confirm the assembly.

#pagebreak()
#link("https://projecteuler.net/problem=326")[= Problem 326: Modulo Summations]

Solution: 1966666166408794329

With $a_1 = 1$ and $a_n = (sum_(k=1)^(n-1) k dot a_k) mod n$, define $f(N, M)$ as the number of pairs $1 <= p <= q <= N$ whose block sum $sum_(i=p)^q a_i$ is divisible by $M$. We want $f(10^12, 10^6)$.

Writing $P_t = sum_(i=1)^t a_i$, a block $(p, q)$ is divisible by $M$ exactly when $P_q equiv P_(p-1) (mod M)$, so $f(N, M) = sum_r binom(c_r, 2)$ over the residue counts $c_r$ among $P_0, dots, P_N$. The sequence $a$ has a clean closed form periodic in $n mod 6$: with $n = 6q + r$, $a_n = n\/2$ for $r in {0, 2}$, $a_n = 4q+1$ for $r = 1$, $a_n = q$ for $r in {3, 5}$, and $a_n = n - 1$ for $r = 4$ (each verified directly against the recurrence).

Because each $a_n$ is linear within its residue class, $P_t$ is piecewise quadratic and $P_t mod M$ turns out to be periodic with period exactly $6 M$. Counting residues over one period of $6 dot 10^6$ values and scaling by the number of whole periods in $[0, N]$ (plus the short tail) gives the answer instantly. The checks $f(10, 10) = 4$ and $f(10^4, 10^3) = 97158$ confirm it.

#pagebreak()
#link("https://projecteuler.net/problem=327")[= Problem 327: Rooms of Doom]


Solution: 34315549139516

A corridor of $R$ rooms is separated by $R + 1$ card-operated doors; each passage of a door consumes one card, at most $C$ cards may be carried, and each room has a box for stashing cards. $M(C, R)$ is the minimum number of cards drawn from the dispenser at the start; we need $sum M(C, 30)$ for $3 <= C <= 40$.

This has the structure of the classic jeep problem. Let $N(d)$ be the number of cards that must be on hand (carried or stashed at the current position) to pass $d$ more doors. If $d <= C$ the cards are simply carried: $N(d) = d$. Otherwise, the $N(d - 1)$ cards needed beyond the next door have to be ferried through it: a round trip costs two door passages and lands $C - 2$ cards on the far side (carry $C$, spend one entering, keep one for the trip back), while the final one-way trip costs one passage and lands $C - 1$. Choosing the trip count $k$ minimally with $(k - 1)(C - 2) + (C - 1) >= N(d - 1)$ gives the recurrence $N(d) = N(d - 1) + 2k - 1$, and $M(C, R) = N(R + 1)$ since the dispenser supplies exactly what is consumed.

The recurrence reproduces both stated values — $M(3, 6) = 123$, with its dramatic near-tripling per extra door once $C - 2 = 1$, and $M(4, 6) = 23$ — as well as the check sum $sum_(C=3)^(10) M(C, 10) = 10382$. The final sum runs instantly; the bulk of it comes from the small-$C$ terms, where ferrying is brutally expensive.

#pagebreak()
#link("https://projecteuler.net/problem=329")[= Problem 329: Prime Frog]

Solution: 199740353/29386561536000

A frog hops left or right with equal probability among squares $1$ to $500$ (bouncing back at the ends), croaking just before each hop: on a prime square it croaks P with probability $2\/3$ and N with $1\/3$, on a non-prime square the reverse. From a uniformly random start, we want the probability that its first fifteen croaks spell PPPPNNPPPNPPNPN, as a reduced fraction.

Keep the arithmetic exact with an integer weight per square. A croak contributes numerator $2$ when the square's prime-ness matches the target letter and $1$ otherwise, each over a factor of $3$; a hop contributes $1\/2$ to each neighbour, and a forced hop off an end has probability $1 = 2 dot 1\/2$, so it carries numerator $2$. Every length-$15$ path then shares the denominator $500 dot 3^15 dot 2^14$, and a single forward sweep over the croaks accumulates the path-weight numerators across all squares. Reducing numerator against denominator gives the fraction.

#pagebreak()
#link("https://projecteuler.net/problem=330")[= Problem 330: Euler's Number]

Solution: 15955822

The sequence $a(n) = sum_(i=1)^infinity a(n-i)\/i!$ (with $a(n) = 1$ for $n < 0$) takes the form $a(n) = (A(n) e + B(n)) \/ n!$ for integers $A, B$; we want $A(10^9) + B(10^9)$ modulo $77777777$.

Substituting the closed form and clearing $n!$ turns the defining series into binomial convolutions:
$
A(n) = sum_(i=1)^n binom(n, i) A(n - i) + n!, quad
B(n) = sum_(i=1)^n binom(n, i) B(n - i) - sum_(i=0)^n n! \/ i!,
$
where the subtracted tail $d(n) = sum_(i=0)^n n! \/ i!$ obeys $d(n) = n d(n-1) + 1$.

The modulus factors as $77777777 = 7 dot 11 dot 73 dot 101 dot 137$, all small primes. Reduced modulo a prime $p$, the binomial coefficients (via Lucas) and the factorials make $A(n) + B(n)$ periodic with period $p(p - 1)$, so each residue is read off at $n mod p(p-1)$ after computing a single period, and CRT recombines them. The given $a(10) = (328161643 e - 652694486)\/10!$ checks the recurrences.

#pagebreak()
#link("https://projecteuler.net/problem=332")[= Problem 332: Spherical Triangles]

Solution: 2717.751525

For each radius $r$ from $1$ to $50$, $A(r)$ is the area of the smallest non-degenerate spherical triangle whose vertices are integer points on the sphere of radius $r$; we sum these.

The area of a spherical triangle is its solid angle times $r^2$, and for unit vertex vectors $a, b, c$ the solid angle is $2 arctan(|a dot (b times c)| \/ (1 + a dot b + b dot c + c dot a))$. Three vertices are degenerate -- lying on one great circle -- exactly when they are coplanar with the centre, i.e. when the integer scalar triple product vanishes; testing this exactly (rather than with a floating-point area threshold) is essential, since the smallest triangles are extremely thin slivers that a tolerance would wrongly discard or admit. Enumerating all vertex triples on each sphere (vectorised with one vertex fixed) and taking the minimum reproduces $A(14) = 3.294040$.

#pagebreak()
#link("https://projecteuler.net/problem=333")[= Problem 333: Special Partitions]

Solution: 3053105

A partition of $n$ into parts $2^i 3^j$ is _valid_ when no part divides another; $P(n)$ counts the valid partitions. We want the sum of the primes $q < 10^6$ with $P(q) = 1$.

Since $2^i 3^j divides 2^k 3^l$ iff $i <= k$ and $j <= l$, a valid partition is an _antichain_ in the divisibility poset: its lattice points $(i, j)$ have strictly increasing $i$ as $j$ strictly decreases. Sweeping the powers of three from high to low, each column contributes at most one part, whose exponent $i$ must exceed every $i$ chosen so far. The DP state is (largest $i$ used, running sum); a prefix sum along the "largest $i$" axis injects all earlier states with a smaller $i$ in one pass, and counts are clamped at $2$ since only $P(q) = 1$ matters. As a check, $sum_(q < 100, P(q) = 1) q = 233$ and $P(11) = 2$, $P(17) = 1$.

#pagebreak()
#link("https://projecteuler.net/problem=334")[= Problem 334: Spilling the Beans]

Solution: 150320021261690835

A move takes two beans from a bowl and drops one into each neighbour; the game ends when every bowl holds $0$ or $1$ bean. Starting from $1500$ bowls holding $b_1, dots, b_1500$ (a pseudo-random sequence summing to about $1.5$ million beans), we count the moves.

This is the one-dimensional abelian sandpile, so the order of play is irrelevant and the halting configuration is unique. It conserves both the bean count $N$ and the first moment $sum i b_i$, and turns out to be a centred run of $1$s -- a block of length $N$, or length $N + 1$ with a single central gap when parity forces it -- placed to match the moment.

Letting $f_i$ be how often bowl $i$ fires, each firing is a discrete Laplacian step, so $"init" - "final" = -Delta f$ and $f_i = -1/2 sum_j |i - j| g_j$ with $g = "init" - "final"$. The total number of moves $sum_i f_i$ is then evaluated in linear time by two prefix-sum passes that split $|i - j|$ at $j <= i$ and $j > i$. The two-bowl case $(289, 145)$ reproduces the given $3419100$.

#pagebreak()
#link("https://projecteuler.net/problem=335")[= Problem 335: Gathering the Beans]

Solution: 5032316

Peter sets out $x$ bowls in a circle, each with one bean; a move empties a bowl and drops its beans one at a time clockwise, then repeats from wherever the last bean fell, until the all-ones state recurs. $M(x)$ counts the moves; we need $sum_(k=0)^(10^18) M(2^k + 1)$ modulo $7^9$.

Direct simulation gives $M(5) = 15$ and $M(100) = 10920$ and, for $x = 2^k + 1$, exposes a clean closed form. Tracking the total bean "travel" (the summed grab sizes) gives $2^k (2^k + 2)$ exactly; separating it from the move count leaves a remainder governed by a $(2, 3, 4)$-geometric recurrence, yielding
$
M(2^k + 1) = 4^k - 3^k + 2^(k+1).
$

The requested sum is therefore three geometric series $sum 4^k$, $sum 3^k$, $sum 2^(k+1)$, each evaluated modulo $7^9$ (every common ratio minus one is invertible there), giving the answer instantly.

#pagebreak()
#link("https://projecteuler.net/problem=336")[= Problem 336: Maximix Arrangements]

Solution: CAGBIHEFJDK

Carriages are reordered by turntable rotations, each reversing a suffix of the train. Simple Simon seats carriage A, then B, and so on: to place the next carriage found at index $j$, he reverses the suffix at $j$ to push it to the end, then the suffix at its target to drop it in -- two rotations (one if already at the end, none if already seated). The worst case ("maximix") takes $2n - 3$ rotations.

Generating permutations in lexicographic order and counting those that need the maximal $2n - 3$ rotations gives the 2011th maximix arrangement for eleven carriages directly. The construction is confirmed by the given facts: six carriages have exactly $24$ maximix arrangements with DFAECB tenth.

#pagebreak()
#link("https://projecteuler.net/problem=337")[= Problem 337: Totient Stairstep Sequences]

Solution: 85068035

We count integer sequences starting at $a_1 = 6$ with $phi(a_i) < phi(a_(i+1)) < a_i < a_(i+1)$ and last term at most $N = 2 dot 10^7$, modulo $10^8$.

Let $f(a)$ be the number of valid sequences ending at $a$. A predecessor $b$ of $a$ must satisfy $phi(a) < b < a$ and $phi(b) < phi(a)$, so
$
f(a) = [a = 6] + sum_(phi(b) < phi(a)) f(b) - sum_(b <= phi(a)) f(b).
$
The subtraction is exact: $b <= phi(a)$ forces $phi(b) < b <= phi(a)$, so those are exactly the terms counted by the first sum but with $b$ too small. Sweeping $a$ in increasing value (so every $f(b)$ with $b < a$ is already known) and keeping two Fenwick trees -- one indexed by $phi$-value, one by value -- evaluates both sums in $O(N log N)$; $S(N)$ is the running total of $f$. The checks $S(100) equiv 482073668$ and $S(10^4) equiv 73808307$ confirm it.

#pagebreak()
#link("https://projecteuler.net/problem=339")[= Problem 339: Peredur Fab Efrawg]

Solution: 19823.542204

Two flocks start with $n$ white and $n$ black sheep. A uniformly random sheep bleats and a sheep of the opposite colour crosses (white bleats grow the white flock, black bleats grow the black flock); afterwards Peredur may remove white sheep to maximise the expected final number of black sheep. We want $E(10000)$.

By the martingale optimality principle (Williams' Mabinogion sheep problem), the optimal move is to cut the white flock to one fewer than the black flock, keeping black a strict majority. So the value depends only on canonical states $(w, b)$ with $w <= b - 1$, with $w = 0$ terminal of value $b$. Every bleat preserves the total $w + b$ except when a white bleat forces a removal, which drops the total by one or two.

Processing totals in increasing order, the same-total transitions form a tridiagonal system in $w$ (solved by the Thomas algorithm) whose only external references are to already-finished smaller totals, so a short rolling buffer of recent totals gives an $O(n^2)$-time, $O(n)$-memory computation. Crucially the first move permits no removal, so $E(n)$ is one forced bleat from $(n, n)$ into this optimal value function; this reproduces the given $E(5) = 6.871346$.

#pagebreak()
#link("https://projecteuler.net/problem=340")[= Problem 340: Crazy Function]

Solution: 291504964

With $F(n) = n - c$ for $n > b$ and $F(n) = F(a + F(a + F(a + F(a + n))))$ otherwise, we need the last nine digits of $S(a, b, c) = sum_(n=0)^b F(n)$ for $a = 21^7$, $b = 7^21$, $c = 12^7$ (note $a > c$).

For $n in (b - a, b]$ we have $a + n > b$, so the innermost call gives $a + n - c$; since $a > c$ each successive argument also exceeds $b$, and the four levels unwind to $F(n) = n + 4a - 4c$. Inductively, for $n in (b - (k+1)a, b - k a]$,
$ F(n) = n + 4(k+1)a - (3k+4)c. $
Writing $m = floor(b\/a)$, the sum splits into the partial bottom block $[0, b - m a]$ (using $k = m$) plus the full blocks $k = 0, ..., m-1$, each contributing $P_k = a b - a(a-1)\/2 + (3k+4)a(a-c)$. Everything is evaluated with exact integers and reduced mod $10^9$ only at the end, sidestepping modular-division issues. The example $S(50, 2000, 40) = 5204240$ (with $F(0) = 3240$, $F(2000) = 2040$) matches a direct recursive evaluation over the whole range.

#pagebreak()
#link("https://projecteuler.net/problem=341")[= Problem 341: Golomb's Self-describing Sequence]

Solution: 56098610614277014

Golomb's sequence $G$ is the unique nondecreasing sequence of natural numbers in which $n$ occurs exactly $G(n)$ times; we want $sum_(1 <= n < 10^6) G(n^3)$, with arguments as large as $10^18$.

Read as runs, the value $c$ occupies positions $(A(c-1), A(c)]$ where $A(c) = sum_(j <= c) G(j)$, so $G(N)$ is the $c$ with $A(c-1) < N <= A(c)$. Building $G$ and the prefixes $A$ and $W(w) = sum_(j <= w) j dot G(j)$ up to a base bound of about $1.1 dot 10^7$ makes $A(c)$ an $O(log)$ evaluation for any $c <= A("base")$: writing $w = G(c)$ (itself a base lookup, since $c <= A("base")$), one has $A(c) = W(w-1) + w(c - A(w-1))$ with $w$ around $10^7$, comfortably inside the tables.

Since $A$ ranges from $W(w-1)$ to $W(w)$ across value $w$'s run, every cube query is resolved without an individual search: locate $w$ with $W(w-1) < N <= W(w)$ by one batched binary search over $W$, then $c = A(w-1) + ceil((N - W(w-1)) \/ w)$. The whole sum is fully vectorised and runs in a few seconds; the checks $G(10^3) = 86$, $G(10^6) = 6137$ and $sum G(n^3) = 153506976$ for $n < 10^3$ confirm it.

#pagebreak()
#link("https://projecteuler.net/problem=342")[= Problem 342: The Totient of a Square Is a Cube]


Solution: 5943040885644

We sum the $n$ with $1 < n < 10^10$ for which $phi(n^2)$ is a perfect cube.

For $n = product p^(a_p)$ we have $phi(n^2) = product p^(2 a_p - 1) (p - 1)$. The exponent of a prime $p$ in $phi(n^2)$ is therefore $2 a_p - 1$ plus whatever the factors $q - 1$ contribute for primes $q > p$ dividing $n$ (each $q - 1$ factors into primes smaller than $q$). The largest prime factor of $n$ receives no such help, so its own exponent must satisfy $2a - 1 equiv 0 space (mod 3)$, i.e. $a equiv 2 space (mod 3)$, so $a >= 2$ — which forces every prime factor of $n$ below $sqrt(10^10) = 10^5$.

This makes a depth-first search over primes in *decreasing* order natural. The state carries, for each smaller prime, the exponent modulo $3$ already contributed by the $(q - 1)$ factors of the primes chosen so far. A prime with nonzero pending exponent is _obligated_: the search may not skip past it, and its exponent in $n$ is pinned modulo $3$ (pending $1$ forces $a equiv 0$, so $a >= 3$; pending $2$ forces $a equiv 1$, so $a >= 1$; pending $0$ allows skipping or $a equiv 2$ with $a >= 2$). Whenever no obligation remains, the current product is a solution and is added to the running total — the problem's example $50 = 2 dot 5^2$ falls out this way, since using $5^2$ leaves $5 - 1 = 2^2$ pending and $2^1$ completes the cube $phi(2500) = 2^3 5^3$. The budget $n < 10^10$ prunes the tree to a size that runs in seconds, and a brute force over $n < 10^4$ (testing $n dot phi(n)$ for cubeness directly) validates the search.

#pagebreak()
#link("https://projecteuler.net/problem=343")[= Problem 343: Fractional Sequences]

Solution: 269533451410884183

Starting from $1\/k$, the map $x\/y -> (x+1)\/(y-1)$ (reduced) is iterated until the denominator is $1$, giving the integer $f(k)$. We want $sum_(k=1)^(2 dot 10^6) f(k^3)$.

The unreduced step keeps $x + y$ fixed; reducing divides $x + y$ by a common factor. Incrementing $x$ from $1$, the first reduction happens at $x$ equal to the smallest prime factor $p$ of the current sum $S$, which divides $S$ by $p$ and resets $x$ to $1$. So $S = k + 1$ is repeatedly divided by its smallest prime until it becomes prime, and the run ends there with $f(k) = S - 1$; the surviving prime is the *largest* prime factor of $k + 1$, hence $f(k) = "lpf"(k + 1) - 1$.

Because $k^3 + 1 = (k + 1)(k^2 - k + 1)$, $f(k^3) = max("lpf"(k+1), "lpf"(k^2 - k + 1)) - 1$. The first factor is read from a largest-prime-factor sieve; the second (up to $4 dot 10^12$) is reduced by sieving only the primes that can divide it. A prime $p$ divides $k^2 - k + 1$ exactly when $(2k - 1)^2 equiv -3 space (mod p)$, which has roots only for $p = 3$ and $p equiv 1 space (mod 3)$; those roots (via a modular square root of $-3$) give arithmetic progressions of $k$ to strip. After removing all primes up to $2 dot 10^6$ any residue above $1$ is itself the largest prime factor. The check $sum_(k=1)^(100) f(k^3) = 118937$ holds.

#pagebreak()
#link("https://projecteuler.net/problem=344")[= Problem 344: Silver Dollar Game]

Solution: 65579304332

$W(n, c)$ counts the winning configurations of the silver dollar game on $n$ squares with $c$ worthless coins and one silver dollar; we want $W(10^6, 100) mod 1000036000099$, where the modulus is the semiprime $1000003 dot 1000033$.

With $m = c + 1$ coins (here odd), a placement is described by the $m + 1$ non-negative gaps summing to $N = n - m$, and the silver dollar may be any of the $m$ coins, so there are $m binom(n, m)$ configurations. The game reduces to Nim on the alternating "active" gaps: a position is losing exactly when those gaps xor to zero. Splitting by where the dollar sits gives $L_0 = "Count"(N)$ (dollar on the second coin) and $L_1 = "Count"(N+1) - "Count"'(N+1)$ for the dollar further right, where $"Count"$ is the number of gap vectors of a given sum whose active entries xor to zero, and the primed term drops one active gap to remove a vanished leading gap. The answer is $m binom(n, m) - (L_0 + (m-2)L_1)$.

$"Count"$ is evaluated with a binary carry DP: per column an even number of active gaps hold a $1$, and scanning the bits of the target sum the only state is the carry. Everything runs directly modulo the semiprime (inverses exist since both primes exceed $m$). The exact values $W(10, 2) = 324$ and $W(100, 10) = 1514704946113500$ both check out.

#pagebreak()
#link("https://projecteuler.net/problem=345")[= Problem 345: Matrix Sum]

Solution: 13938

Choosing one entry from each row of a $15 times 15$ matrix so that no two chosen entries share a column, maximise the sum.

This is the assignment problem, solved by a bitmask dynamic program over the set of columns already used. Let $"dp"("mask")$ be the largest total achievable when the chosen columns form $"mask"$; since exactly one entry is taken per row, the number of set bits in $"mask"$ is the next row to fill. Extending each state by every still-unused column and keeping the maximum fills all $2^15$ states in $O(2^15 dot 15)$ steps, and the all-columns mask holds the Matrix Sum. The $5 times 5$ example evaluates to $3315$ as a check.

#pagebreak()
#link("https://projecteuler.net/problem=346")[= Problem 346: Strong Repunits]

Solution: 336108797689259276

Collect every number that is a repunit of length at least three in some base up to $sqrt(n)$, together with all values that are length-two repunits, and sum the distinct ones below $10^12$.

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
#link("https://projecteuler.net/problem=349")[= Problem 349: Langton's Ant]

Solution: 115384615384614952

Langton's ant walks a grid of black and white squares: on white it flips the square to black, turns clockwise and steps forward; on black it flips to white, turns counterclockwise and steps. Starting on an all-white grid, we want the number of black squares after $10^18$ moves.

Simulating $10^18$ steps is out of the question, but the ant's famous behaviour makes it unnecessary: after a chaotic transient of roughly $10000$ steps it locks into a "highway", a configuration that recurs every $104$ steps displaced diagonally, adding a constant number of black squares per period. The solution simulates a little past the transient ($11000$ steps), then continues to four checkpoints spaced $104$ steps apart and aligned so the target $10^18$ is a whole number of periods beyond the first. The black-square gains between consecutive checkpoints are measured and verified to be equal — the simulation confirms the periodicity instead of taking it on faith — and the count is extrapolated linearly: $12$ new black squares per $104$-step period.

#pagebreak()
#link("https://projecteuler.net/problem=350")[= Problem 350: Constraining the Least Greatest and the Greatest Least]

Solution: 84664213

$f(G, L, N)$ counts the ordered lists of $N$ natural numbers with $gcd >= G$ and $"lcm" <= L$; we need $f(10^6, 10^12, 10^18) mod 101^4$.

Factor out the gcd: a list with gcd exactly $g$ is $g$ times a list with gcd $1$, and its lcm constraint becomes $"lcm" <= floor(L \/ g)$. So $f = sum_(g >= G) C(floor(L \/ g))$ where $C(m)$ counts gcd-$1$ lists with lcm at most $m$. Because $g >= G = sqrt(L)$, only the values $m <= M = L \/ G = 10^6$ occur, and the number of $g$ producing each $m$ is a floor-division block count — so everything reduces to computing $C$ on $1..M$.

Counting instead by *exact* lcm makes the problem multiplicative. The number of lists with lcm exactly $l$ is $D(l) = product_(p^e || l) ((e + 1)^N - e^N)$: each entry's exponent of $p$ is at most $e$, minus the choices where no entry attains $e$. Splitting a list with lcm exactly $l$ by its gcd $d$ (which divides $l$) gives the divisor-sum identity $D(l) = sum_(d | l) c(l \/ d)$, where $c$ counts gcd-$1$ lists by exact lcm. Möbius inversion turns this into the sieve-friendly convolution $c = mu * D$, and $C$ is just the prefix sum of $c$.

The computation over $1..10^6$ is three array passes: $D$ from a smallest-prime-factor table (the per-prime factors $(e+1)^N - e^N$ are modular powers with the huge $N = 10^18$ reduced by fast exponentiation), the convolution $c = mu * D$ as one harmonic-series sweep of slice additions, and a cumulative sum. The four stated examples, including $f(10, 100, 1000) mod 101^4 = 3286053$, all check out.

#pagebreak()
#link("https://projecteuler.net/problem=351")[= Problem 351: Hexagonal Orchards]

Solution: 11762187201804552

In a hexagonal orchard of order $n$ (a triangular lattice of points inside a regular hexagon of side $n$), $H(n)$ counts the points hidden from the centre by a nearer point. We want $H(10^8)$.

A point is hidden exactly when it is not the closest lattice point along its ray, i.e. when its coordinates are not coprime. By the six-fold symmetry the lattice splits into six sectors, and at radial index $i$ the visible points in a sector are the $phi(i)$ with coprime coordinates, leaving $i - phi(i)$ hidden. Hence
$ H(n) = 6 sum_(i=1)^n (i - phi(i)) = 6 ((n (n + 1))/2 - Phi(n)), quad Phi(n) = sum_(i=1)^n phi(i). $
The totient summatory function $Phi$ is evaluated sublinearly from the identity $sum_(d=1)^n Phi(floor(n\/d)) = n(n+1)\/2$, giving
$ Phi(n) = (n (n + 1))/2 - sum_(d=2)^n Phi(floor(n\/d)), $
grouped over equal values of $floor(n\/d)$ and seeded by a sieve of $phi$ (hence $Phi$) for all arguments up to about $n^(2\/3)$. The checks $H(5) = 30$, $H(10) = 138$, $H(1000) = 1177848$ all hold.

#pagebreak()
#link("https://projecteuler.net/problem=353")[= Problem 353: Risky Moon]

Solution: 1.2759860331

Stations sit at the integer points on the sphere of radius $r$; a road runs along the great circle between two stations, and a road of arc length $d$ carries risk $(d \/ (pi r))^2 = (theta \/ pi)^2$ for central angle $theta$. We want the least-risk journey from the North Pole to the South Pole station, summed over $r = 2^n - 1$ for $n = 1, dots, 15$.

Since risk is the square of the normalised length, breaking a hop into shorter ones always lowers it (as the half-way example $0.5 < 1$ shows), so the optimal path threads many nearby stations. This is a shortest-path problem: build a graph linking each station to its nearest neighbours -- recovered with a grid bucketing of the integer coordinates, the central angle obtained from the chordal distance -- with edge weight $(theta \/ pi)^2$, and run Dijkstra from the North to the South Pole. Thirty-two neighbours per station already reproduces the dense-graph value $M(7) = 0.1784943998$ exactly.

#pagebreak()
#link("https://projecteuler.net/problem=354")[= Problem 354: Distances in a Bee's Honeycomb]

Solution: 58065134

In a honeycomb of unit hexagons the cell centres form a triangular lattice; a centre $a bold(v)_1 + b bold(v)_2$ lies at squared distance $L^2 = 3(a^2 + a b + b^2)$ from the queen cell. So $B(L)$, the number of cells at distance $L$, equals the number of integer representations of $m = L^2 \/ 3$ by the Loeschian form $a^2 + a b + b^2$. We count distances $L <= 5 dot 10^11$ with $B(L) = 450$, i.e. Loeschian $m <= (5 dot 10^11)^2 \/ 3$ with $r(m) = 450$.

The representation count is multiplicative: $r(m) = 6 product_(p equiv 1 (3)) (e_p + 1)$, and is $0$ unless every prime $equiv 2 (mod 3)$ occurs to an even power (the prime $3$ is neutral). So $r(m) = 450$ forces $product (e_p + 1) = 75$ over primes $equiv 1 (mod 3)$. The factorizations of $75$ into parts $>= 2$ give exactly four exponent patterns: ${74}$, ${2, 24}$, ${4, 14}$, ${2, 4, 4}$.

Write $m = K M$, where $K$ holds the $equiv 1 (mod 3)$ primes in one of those patterns and $M = 3^c t^2$ with $t$ built only from primes $equiv 2 (mod 3)$. Then the answer is $sum_K G(N \/ K)$ with $N = (5 dot 10^11)^2 \/ 3$ and $G(y) = sum_(c >= 0) T(floor(sqrt(y \/ 3^c)))$, where $T(z)$ counts integers $<= z$ all of whose prime factors are $equiv 2 (mod 3)$. The high exponents force the pattern primes to be small, so only a few million $K$ arise, and a single sieve for $T$ finishes the sum in seconds.

#pagebreak()
#link("https://projecteuler.net/problem=356")[= Problem 356: Largest Roots of Cubic Polynomials]

Solution: 28010159

Let $a_n$ be the largest real root of $x^3 - 2^n x^2 + n$; we need the last eight digits of $sum_(i=1)^(30) floor(a_i^987654321)$.

The classic conjugate-root trick applies. Writing $a, b, c$ for the three roots, the power sums $S_k = a^k + b^k + c^k$ are integers obeying the recurrence $S_k = 2^n S_(k-1) - n S_(k-3)$ (multiply $x^3 = 2^n x^2 - n$ by $x^(k-3)$ and sum over the roots), seeded by $S_0 = 3$, $S_1 = 2^n$ and $S_2 = 4^n$ from the elementary symmetric polynomials $e_1 = 2^n$, $e_2 = 0$.

The two conjugates are small: with $x_0 = sqrt(n \/ 2^n)$, the cubic is positive at $0$ and $x_0$ but negative at $-x_0$ and $1$, placing one root $b$ in $(x_0, 1)$ and the other $c$ in $(-x_0, 0)$. Hence $b > |c|$, so for an odd exponent $k$ the tail $b^k + c^k$ lies strictly in $(0, 1)$, and $a^k = S_k - (b^k + c^k)$ has $floor(a^k) = S_k - 1$ — verified numerically for small $n$ and $k$ against the actual roots.

Each $S_k mod 10^8$ comes from a $3 times 3$ matrix power in $O(log k)$ steps, and the answer is $sum_(n=1)^(30) (S_k - 1) mod 10^8$ with $k = 987654321$.

#pagebreak()
#link("https://projecteuler.net/problem=357")[= Problem 357: Prime Generating Integers]

Solution: 1739023853137

Sum the integers $n <= 10^8$ for which $d + n\/d$ is prime for every divisor $d$ of $n$. Taking $d = 1$ forces $n + 1$ to be prime, so $n$ is even and the only candidates are $n = p - 1$ for primes $p$. Sieve the primes up to $10^8$ for constant-time primality tests, then for each candidate check the divisor pairs with $d <= sqrt(n)$ (the condition is symmetric in $d$ and $n\/d$), bailing out at the first failure — usually already at $d = 2$.

#pagebreak()
#link("https://projecteuler.net/problem=358")[= Problem 358: Cyclic Numbers]

Solution: 3284144505

A cyclic number is $c = (10^(p-1) - 1) \/ p$ for a full-reptend prime $p$ (one for which $10$ is a primitive root, so $1\/p$ has period $p - 1$); $c$ is precisely the repeating block of $1\/p$ and so has $p - 1$ digits, with leading zeros kept. We seek the digit sum of the unique such number beginning $00000000137$ and ending $56789$.

Its digit sum is $9 (p - 1) \/ 2$: the digits pair off into nines (for $142857$ the sum is $27 = 9 dot 6 \/ 2$). The two end conditions pin $p$ down. The leading $00000000137$ means $floor(10^11 \/ p) = 137$, hence $10^11 \/ 138 < p <= 10^11 \/ 137$. The trailing $56789$ means $c equiv 56789 space (mod 10^5)$; since $c p = 10^(p-1) - 1 equiv -1 space (mod 10^5)$, this gives $56789 p equiv 99999 space (mod 10^5)$, fixing $p$ modulo $10^5$. Scanning that short arithmetic progression for the prime whose order of $10$ is $p - 1$ yields the unique $p$, and $9 (p - 1) \/ 2$ is the answer.

#pagebreak()
#link("https://projecteuler.net/problem=359")[= Problem 359: Hilbert's New Hotel]

Solution: 40632119

Person $n$ takes the lowest floor that is empty or whose last occupant $m$ has $m + n$ a perfect square; $P(f, r)$ is the person in room $r$ of floor $f$. We sum $P(f, r)$ over all $f r = 71328803586048 = 2^27 dot 3^12$ and report the last eight digits.

Simulation exposes the structure: along any floor the occupants satisfy $a_i + a_(i+1) = (i + b)^2$, where floor $1$ has $b = 1$ and floors $2k, 2k+1$ share $b = 2k$. The first occupants are $P(1,1) = 1$, $P(2k, 1) = 2 k^2$, $P(2k+1, 1) = 2 k (k + 1)$. Solving the alternating recurrence $a_(i+1) = (i + b)^2 - a_i$ with the identity $sum_(k=1)^n (-1)^(n-k) k^2 = n (n + 1) \/ 2$ gives the closed form
$ P(f, r) = (-1)^(r-1) (a_1 - (b (b + 1))/2) + ((b + r - 1)(b + r))/2, $
which reproduces $P(10, 20) = 440$, $P(25, 75) = 4863$ and $P(99, 100) = 19454$. Summing over the $364$ divisor pairs of $2^27 dot 3^12$ and reducing modulo $10^8$ gives the result.

#pagebreak()
#link("https://projecteuler.net/problem=362")[= Problem 362: Squarefree Factors]

Solution: 457895958010

$"Fsf"(k)$ is the number of ways to write $k$ as an unordered product of squarefree factors all greater than $1$, and $S(n) = sum_(k=2)^n "Fsf"(k)$; we need $S(10^10)$.

Summing $"Fsf"$ over all $k <= n$ counts every (value, factorization) pair, which is exactly the number of multisets of squarefree integers $> 1$ whose product is at most $n$. Counting those multisets with factors in nondecreasing order gives
$
F(N, "lo") = "multisets (incl. empty) of squarefree factors" >= "lo, product" <= N,
$
with $S(n) = F(n, 2) - 1$ after dropping the empty multiset. The key speedup: a factor $d > sqrt(N)$ can occur at most once (no second factor $>= d$ would fit), so all such $d$ contribute one multiset ${d}$ each and are counted in bulk by the squarefree-counting function $Q(b) = sum_k mu(k) floor(b \/ k^2)$; only factors $d <= sqrt(N)$ are recursed on. Memoizing on the $O(sqrt(N))$ distinct values of $floor(N \/ dots)$ keeps the recursion fast, and $"Fsf"(54) = 2$, $S(100) = 193$ confirm it.

#pagebreak()
#link("https://projecteuler.net/problem=364")[= Problem 364: Comfortable Distance]

Solution: 44855254

$N$ people fill $N$ seats in a row, each preferring a seat with no occupied neighbour, then one with a single occupied neighbour, then any seat. $T(N)$ counts the seating orders; we want $T(10^6) mod 100000007$.

Because the priority rules are exhausted in turn, all "rule 1" people (no occupied neighbour) sit first. Their seats form a maximal independent dominating set $S$ of size $k$; since its members are pairwise non-adjacent, none ever blocks another, so any of the $k!$ orders works. Writing the row as $[L] O [g_1] O dots O [g_(k-1)] O [R]$, maximality forces the end gaps $L, R in {0,1}$ and each interior gap $g_i in {1,2}$. With $e = L + R$ end gaps of size $1$ and $g_2$ interior gaps of size $2$, each size-$2$ gap yields one rule-2 seat (with $2$ choices of which seat fills first) and one rule-3 seat, while each size-$1$ interior gap is a lone rule-3 seat. The rule-2 phase then orders $e + g_2$ seats and the rule-3 phase orders $k - 1$ seats, giving the contribution
$
k! dot (k-1)! dot (e + g_2)! dot 2^(g_2).
$
The seat total fixes $g_2 = N - 2k + 1 - L - R$ and $binom(k-1, g_2)$ chooses which interior gaps are the size-$2$ ones, so summing over $k$ and the four $(L, R)$ cases is $O(N)$. The checks $T(10) = 61632$ and $T(1000) equiv 47255094$ confirm it.

#pagebreak()
#link("https://projecteuler.net/problem=365")[= Problem 365: A Huge Binomial Coefficient]

Solution: 162619462356610313

Let $M(n, k, m) = binom(n, k) mod m$. We want $sum M(10^18, 10^9, p q r)$ over prime triples $1000 < p < q < r < 5000$.

There are $501$ primes in that range. For each prime $p$, $binom(10^18, 10^9) mod p$ is computed by Lucas' theorem: writing both numbers in base $p$ (about five or six digits), the result is the product of $binom(n_i, k_i) space (mod p)$ over digits, each evaluated from factorial and inverse-factorial tables mod $p$. With those residues in hand, every triple's value mod $p q r$ follows from the Chinese Remainder Theorem on the squarefree modulus. Precomputing a table of $p_j^(-1) space (mod p_i)$ turns the inner CRT into a few multiplications, so the roughly $binom(501, 3) approx 2.1 dot 10^7$ triples are summed quickly.

#pagebreak()
#link("https://projecteuler.net/problem=366")[= Problem 366: Stone Game III]

Solution: 88351299

One pile of $n$ stones; the opener removes any positive number but not the whole pile, and thereafter each player removes at most twice what the opponent just took. $M(n)$ is the maximum the opener can take from a winning position (else $0$); we need $sum_(n <= 10^18) M(n) mod 10^8$.

This is Fibonacci Nim. A position $(n, k)$ — $n$ stones, may take $1..k$ — is a second-player win exactly when $k$ is below the smallest term of $n$'s Zeckendorf representation (confirmed here by a memoised game-tree search on small cases). A first move of $t$ leaves $(n - t, 2t)$, which the opener wants to be a loss, i.e. $2t < $ smallest Zeckendorf term of $n - t$. Writing $n = F_k + r$ with $F_k$ the largest Fibonacci number $<= n$ (so $0 <= r < F_(k-1)$), the maximal such $t$ satisfies the recursion
$
M(n) = cases(r & "if " 2r < F_k\, , M(r) & "otherwise") ,
$
with $M(n) = 0$ when $n$ is itself Fibonacci — reproducing the worked example $M(5) = 0$ and $M(2), M(7), M(20) = 2, 1, 4$.

For the sum to $10^18$, group numbers by their largest Fibonacci term: those with top term $F_k$ are $n = F_k + r$, $r in [0, F_(k-1) - 1]$, contributing $r$ while $2r < F_k$ (an arithmetic run summed in closed form) and $M(r)$ beyond — a tail of the same prefix sum at a far smaller argument. The arguments shrink geometrically, so the memoised prefix recursion is logarithmic in $N$. One arithmetic subtlety: $2$ is not invertible modulo $10^8$, so the triangular sums $t(t+1)\/2$ are reduced by halving the even factor *before* taking the modulus rather than multiplying by a modular inverse. The check value $sum_(n=1)^(100) M(n) = 728$ confirms the assembly.

#pagebreak()
#link("https://projecteuler.net/problem=367")[= Problem 367: Bozo Sort]

Solution: 48271207

This bozo-sort variant repeatedly picks $3$ of the $n$ positions uniformly and replaces their contents by a uniformly random one of the $6$ arrangements, until the sequence is sorted. We want the expected number of shuffles averaged over all $11!$ inputs, rounded to an integer.

The expected hitting time $E[pi]$ of the identity is unchanged by relabelling the values, so it depends only on the cycle type of $pi$ — and there are only $p(11) = 56$ cycle types. Taking one representative of each, enumerating the $binom(n,3)$ position triples and their $6$ rearrangements, and recording the resulting cycle type yields the transition probabilities between cycle types. This gives a $56 times 56$ linear system $E[c] = 1 + sum_(c') P(c -> c') E[c']$ with $E$ of the identity type equal to $0$. Solving it exactly over the rationals and averaging $E[c]$ weighted by each class size divided by $n!$ gives $approx 48271206.77$, i.e. $48271207$. The small cases $n = 4 -> 27.5$ and $n = 7 -> 6200.2$ confirm the model.

#pagebreak()
#link("https://projecteuler.net/problem=369")[= Problem 369: Badugi]

Solution: 862400558448

A Badugi is a $4$-card set with all distinct ranks and all distinct suits. $f(n)$ counts the $n$-card hands from a standard $52$-card deck that contain such a $4$-card subset; we want $sum_(n=4)^(13) f(n)$.

View a hand as a bipartite graph between the $4$ suits and the $13$ ranks, with an edge for every card held. A Badugi is exactly a matching of size $4$ (assign each suit a distinct rank), so a hand contains a Badugi iff this graph has a perfect matching on the suit side. Hence $f(n) = binom(52, n)$ minus the hands whose maximum matching is at most $3$.

The no-Badugi hands are counted by a DP over the $13$ ranks. Processing one rank at a time, we choose which of the $4$ suits it holds (a $4$-bit mask), and that rank may be matched to at most one suit. The state is the set of suit-subsets reachable as a matching — a $16$-bit mask over the $16$ subsets of suits — and a hand acquires a Badugi precisely when the full suit-set becomes reachable. Carrying the running card count gives every $f(n)$ at once; the construction reproduces the stated $f(5) = 514800$.

#pagebreak()
#link("https://projecteuler.net/problem=370")[= Problem 370: Geometric Triangles]

Solution: 41791929448408

A geometric triangle has integer sides $a <= b <= c$ in geometric progression, $b^2 = a c$; we count those with perimeter $<= 2.5 dot 10^13$.

Writing the common ratio in lowest terms $n\/m$ with $gcd(m, n) = 1$ and $m <= n$, the sides are a scaling $s dot (m^2, m n, n^2)$. The triangle inequality (only $a + b > c$ can fail) becomes $m^2 + m n > n^2$, i.e. $n < phi m$ with $phi$ the golden ratio, and the perimeter is $s (m^2 + m n + n^2)$. The count is therefore
$
sum_("primitive" (m,n)) floor(P \/ (m^2 + m n + n^2)).
$

Coprimality is handled by Möbius inversion: if $A(P) = sum_("all" (m,n)) floor(P \/ b)$ over all valid pairs (with $b = m^2 + m n + n^2$), then a pair $(g m', g n')$ contributes $floor(P \/ (g^2 b'))$, giving $A(P) = sum_g f(floor(P \/ g^2))$ where $f$ is the primitive-only sum; inverting, $f(P) = sum_g mu(g) A(floor(P \/ g^2))$. The unrestricted $A(P)$ is evaluated by iterating $m$ up to $sqrt(P\/3)$ and, for each, jumping through the constant blocks of $floor(P \/ b)$ in $n$ by solving the quadratic $b(n) <= P \/ q$ for each quotient $q$ — so the per-$m$ cost is the number of distinct quotients rather than the full $n$-range. The whole computation runs in well under a minute, and the given $861805$ triangles with perimeter $<= 10^6$ confirm it.

#pagebreak()
#link("https://projecteuler.net/problem=371")[= Problem 371: Licence Plates]

Solution: 40.66368097

Each plate shows a number $000$–$999$ uniformly at random, and Seth wins as soon as two numbers he has seen sum to $1000$. Only the number matters. Pairing $n$ with $1000 - n$: the value $0$ would need $1000$ (not a plate) so it never wins; $500$ pairs with itself, so two $500$s win; and $1$–$499$ pair with $501$–$999$, giving $499$ complementary pairs.

A win occurs the instant a drawn number's partner has already appeared. By symmetry the state is $(k, s)$, where $k$ is the number of the $499$ pairs that are "half seen" (exactly one side seen) and $s$ records whether a $500$ has appeared. On each draw (probability $1\/1000$ apiece): the dead $0$ changes nothing; a $500$ wins if $s = 1$ and otherwise sets $s = 1$; the unseen side of any half-seen pair wins (there are $k$ of these); an already-seen side changes nothing (another $k$); and with probability $2(499 - k)\/1000$ a fresh pair raises $k$ to $k+1$. Letting $E[k, s]$ be the expected remaining draws and solving these linear equations from $k = 499$ downward yields $E[0, 0] approx 40.66368097$.

#pagebreak()
#link("https://projecteuler.net/problem=374")[= Problem 374: Maximum Integer Partition Product]

Solution: 334420941

$f(n)$ is the largest product of a partition of $n$ into *distinct* parts and $m(n)$ the number of parts achieving it (so $f(10) = 30$, $m(10) = 3$ from $10 = 2 + 3 + 5$); we need $sum_(n <= 10^14) f(n) m(n) mod 982451653$.

The optimal partition is anchored on the consecutive block $\{2, 3, dots, k\}$ for the largest $k$ with $S_k = 2 + 3 + dots + k <= n$, and the surplus $r = n - S_k$ (which ranges over $0 dots k$) is absorbed minimally — keeping parts distinct and as large as possible. Brute-force search confirms the rule:
$
f(n) = cases(
  k! & r = 0,
  k! (k+1) \/ (k+1-r) quad & 1 <= r <= k-1 wide ("drop " k+1-r", add " k+1),
  k! (k+2) \/ 2 & r = k wide ("drop " 2", add " k+2)
),
$
and in every case $m(n) = k - 1$. So each $k$ governs the $k+1$ consecutive values $n = S_k, dots, S_k + k$ (with $S_k = k(k+1)\/2 - 1$).

Summing $f m$ over a full block collapses: the middle cases contribute $k!(k+1) sum_(j=2)^(k) 1\/j = k!(k+1)(H_k - 1)$ with $H_k$ the harmonic number. Maintaining $k!$ and $H_k$ modulo the prime incrementally, with all modular inverses precomputed in one linear pass, evaluates the whole sum in $O(sqrt(N))$ blocks. Only the final block is partial (summed term by term), $n = 1$ is the lone special case, and $k = 2$ accounts for $n = 2, 3, 4$. The given total $sum_(n=1)^(100) f m = 1683550844462$ confirms the construction.

#pagebreak()
#link("https://projecteuler.net/problem=375")[= Problem 375: Minimum of Subsequences]

Solution: 7435327983715286168

With the quadratic PRNG $S_(n+1) = S_n^2 mod 50515093$, $A(i, j)$ is the minimum of $S_i dots S_j$ and $M(N) = sum_(1 <= i <= j <= N) A(i, j)$; we want $M(2 dot 10^9)$.

This is the sum of minimums over every subarray. Sweeping left to right, keep a value-increasing stack of $("value", "span")$ blocks together with a running quantity $"cur"$ equal to the sum of minimums of all subarrays ending at the current position. Reading a new term $S$ pops every block whose value is $>= S$ (those subarrays now take minimum $S$), merges their spans, and adds $S times ("merged span")$ to $"cur"$; adding $"cur"$ to the total at each step accumulates the full double sum in a single $O(N)$ pass. The PRNG values are well spread, so the stack never exceeds a few dozen entries, and the final total fits in $64$ bits. The checks $M(10) = 432256955$ and $M(10000) = 3264567774119$ confirm it.

#pagebreak()
#link("https://projecteuler.net/problem=378")[= Problem 378: Triangle Triples]

Solution: 147534623725724718

With $T(n) = n(n+1)\/2$ the $n$-th triangular number and $d T(n)$ its number of divisors, $T r(n)$ counts triples $1 <= i < j < k <= n$ with $d T(i) > d T(j) > d T(k)$. We want the last $18$ digits of $T r(6 dot 10^7)$.

Since $gcd(n, n+1) = 1$, splitting off the factor of $2$ writes $T(n)$ as a product of two coprime parts, so $d T(n) = d(a) dot d(b)$ where $(a, b)$ is $(n\/2, n+1)$ for even $n$ and $(n, (n+1)\/2)$ for odd $n$. A linear sieve gives the divisor counts $d$ up to $n+1$, hence the whole array $d T(1 dots n)$.

Counting strictly decreasing triples is then a standard two-Fenwick-tree sweep: for each middle index $j$ the number of triples through it is (how many earlier values exceed $d T(j)$) times (how many later values are smaller), and a right-to-left pass followed by a left-to-right pass over the $d T$-values produces both factors in $O(n log)$. The running total is kept modulo $10^18$; the checks $T r(100) = 5772$ and $T r(1000) = 11174776$ confirm it.

#pagebreak()
#link("https://projecteuler.net/problem=379")[= Problem 379: Least Common Multiple Count]

Solution: 132314136838185

$f(n)$ counts couples $(x, y)$ with $x <= y$ and $"lcm"(x, y) = n$; $g$ is its summatory function, and we need $g(10^12)$.

For $n = product_i p_i^(a_i)$, a pair with $"lcm" = n$ chooses for each prime the exponents $(b_i, c_i)$ with $max(b_i, c_i) = a_i$, giving $2a_i + 1$ ordered possibilities per prime, so the number of *ordered* pairs is $d(n^2) = product_i (2a_i + 1)$. Exactly one of these is diagonal ($x = y = n$), hence
$
f(n) = (d(n^2) + 1) \/ 2, quad g(N) = 1/2 (D(N) + N), quad D(N) = sum_(n <= N) d(n^2).
$

The summatory $D(N)$ is found from the Dirichlet identity $d(n^2) = (1 * 1 * mu^2)(n)$ — equivalently $sum d(n^2) n^(-s) = zeta(s)^3 \/ zeta(2s)$. Writing the squarefree indicator as $mu^2(c) = sum_(d^2 | c) mu(d)$ peels off a Möbius factor:
$
D(N) = sum_(d <= sqrt(N)) mu(d) \, D_3(floor(N \/ d^2)),
$
where $D_3(m) = sum_(n <= m) d_3(n)$ is the three-divisor summatory, i.e. the number of ordered triples $(a, b, c)$ with $a b c <= m$. Computing $D_3$ by enumerating only sorted triples $a <= b <= c$ (with $a <= root(3, m)$, $b <= sqrt(m\/a)$) and weighting each by its $6\/3\/1$ orderings costs $O(m^(2\/3))$, and the outer $d$-sum is dominated by $d = 1$, so the whole evaluation runs in a couple of seconds. The given $g(10^6) = 37429395$ confirms the construction.

#pagebreak()
#link("https://projecteuler.net/problem=381")[= Problem 381: (prime-k) Factorial]

Solution: 139602943319822

For a prime $p$, $S(p) = (sum_(k=1)^5 (p-k)!) mod p$; we want $sum S(p)$ for $5 <= p < 10^8$.

By Wilson's theorem $(p-1)! equiv -1 space (mod p)$, and dividing successively by $p-1, p-2, ...$ (each $equiv -1, -2, ...$) gives $(p-k)! equiv (-1)^k\/(k-1)! space (mod p)$. Summing the five terms,
$ S(p) equiv -1 + 1 - 1/2 + 1/6 - 1/24 = -3/8 space (mod p). $
Solving $8x equiv -3 space (mod p)$ yields a closed form by residue: $S(p) = (3p-3)\/8$, $(p-3)\/8$, $(7p-3)\/8$, $(5p-3)\/8$ for $p equiv 1, 3, 5, 7 space (mod 8)$ respectively. A sieve to $10^8$ then sums these (checked against $sum S(p) = 480$ for $p < 100$).

#pagebreak()
#link("https://projecteuler.net/problem=382")[= Problem 382: Generating Polygons]

Solution: 697003956

The sticks satisfy $s_i = s_(i-1) + s_(i-3)$ (with $s_1, s_2, s_3 = 1, 2, 3$), and a subset of $U_n = {s_1, dots, s_n}$ forms a polygon exactly when it has at least three sticks and its longest stick is shorter than the sum of the others. We want the last $9$ digits of $f(10^18)$.

Counting the complementary failures by their maximum, $f(n) = (2^n - 1 - n - binom(n, 2)) - sum_(m=3)^n B(m)$, where $B(m)$ is the number of subsets $T subset.eq {s_1, dots, s_(m-1)}$ with $|T| >= 2$ and $"sum"(T) <= s_m$ (these are the size-$>=3$ subsets whose maximum $s_m$ violates the polygon inequality). A memoised "subsets within a budget" recursion computes $B(m)$ exactly for the first several $m$; from those values $B$ is found to obey a fixed order-$9$ linear recurrence (rooted in the characteristic polynomial $x^3 = x^2 + 1$ of the stick sequence), verified on dozens of terms.

Advancing the running total $sum B(m)$ to $n = 10^18$ is then a matrix exponentiation modulo $10^9$ on a state holding nine consecutive $B$ values plus their partial sum, while $2^n - 1 - n - binom(n,2)$ is taken directly mod $10^9$. The checks $f(5) = 7$, $f(10) = 501$ and $f(25) = 18635853$ confirm it.

#pagebreak()
#link("https://projecteuler.net/problem=383")[= Problem 383: Divisibility Comparison Between Factorials]

Solution: 22173624649806

Let $f_5(n)$ be the exponent of $5$ in $n$. $T_5(n)$ counts $i in [1, n]$ with $f_5((2i-1)!) < 2 f_5(i!)$; we want $T_5(10^18)$.

By Legendre, $f_5(m!) = (m - s_5(m)) \/ 4$ where $s_5$ is the base-$5$ digit sum. Using $s_5(2i-1) = s_5(2i) - 1 + 4 v_5(i)$ (with $v_5(i)$ the number of trailing base-$5$ zeros) and the identity $s_5(2i) - 2 s_5(i) = -4 C(i)$, where $C(i)$ is the number of carries when doubling $i$ in base $5$, the inequality collapses to the strikingly simple
$
v_5(i) > C(i).
$

Writing $i = 5^v dot j$ with $5 divides.not j$, the trailing zeros create no carries, so $C(i) = C(j)$ and the condition is $v > C(j)$. Therefore
$
T_5(n) = sum_(v >= 1) hash{ j : 5 divides.not j, j <= n\/5^v, C(j) <= v - 1 },
$
and each inner count is a base-$5$ digit DP over $j$ that tracks the doubling carries (the carry runs low-to-high, so the recursion fixes high digits and lets the lower part report the carry it pushes up). With only about $26$ values of $v$, the whole computation is instant, and $T_5(10^3) = 68$, $T_5(10^9) = 2408210$ confirm it.

#pagebreak()
#link("https://projecteuler.net/problem=386")[= Problem 386: Maximum Length of an Antichain]

Solution: 528755790

$S(n)$ is the set of divisors of $n$, and an antichain is a subset in which no element divides another. $N(n)$ is the largest antichain (e.g. $S(30)$ gives $\{2, 3, 5\}$, so $N(30) = 3$); we need $sum_(n <= 10^8) N(n)$.

Write $n = product_i p_i^(a_i)$. Its divisors, ordered by divisibility, form a product of chains: a divisor is fixed by its exponent vector $(e_1, dots, e_r)$ with $0 <= e_i <= a_i$, and one divides another iff its vector is componentwise $<=$. By the de Bruijn–Tengbergen–Kruyswijk theorem this poset is rank-symmetric and rank-unimodal, where a divisor's rank is the exponent sum $sum_i e_i$. The widest antichain is therefore the largest rank level, and the level sizes are exactly the coefficients of
$
product_i (1 + x + dots + x^(a_i)).
$
So $N(n)$ is the central (largest, by unimodality) coefficient of that product — depending only on the multiset of exponents, not the primes. Brute-forcing maximum antichains for $n < 2000$ matches this with no exceptions.

To sum over $n <= 10^8$, a smallest-prime-factor sieve factors each $n$ into its exponent multiset, and the central coefficient is computed by convolving the chain polynomials (a few-millisecond operation since $sum a_i <= 26$). The exponent multisets repeat heavily, so the inner work is tiny; the whole sieve-and-sweep runs in well under a minute. A cross-check, $sum_(n <= 10^6) N(n) = 4153927$, confirms the implementation.

#pagebreak()
#link("https://projecteuler.net/problem=387")[= Problem 387: Harshad Numbers]

Solution: 696067597313468

A Harshad number is divisible by its digit sum. A right truncatable Harshad (RTH) number remains a Harshad number under repeated removal of its last digit, and a strong Harshad number is one whose quotient by its digit sum is prime. We sum the primes below $10^14$ whose truncation (last digit removed) is a strong RTH number.

The truncation property means the RTH numbers form a tree rooted at the single digits $1$–$9$: every RTH number is a shorter RTH number with one digit appended, and there are only a few hundred thousand of them below $10^13$. Grow this tree level by level, keeping a child $10h + d$ exactly when it is divisible by its digit sum. Whenever a node $h$ is strong — $h$ divided by its digit sum is prime by a Miller–Rabin test — try all ten extensions $10h + d$ below $10^14$ and add the primes among them to the total. The stated check value, $90619$ for the primes below $10^4$, confirms the bookkeeping.

#pagebreak()
#link("https://projecteuler.net/problem=388")[= Problem 388: Distinct Lines]

Solution: 831907372805129931

$D(N)$ counts the distinct lines from the origin through the lattice points of $[0, N]^3$; the answer is the first nine and last nine digits of $D(10^10)$.

Every line meets the cube's lattice in the multiples of a unique *primitive* point — one with $gcd(a, b, c) = 1$ — and since all coordinates are nonnegative there is no sign ambiguity, so $D(N)$ is just the number of primitive nonzero points. Möbius inversion over the common divisor gives
$
D(N) = sum_(d >= 1) mu(d) ((floor(N \/ d) + 1)^3 - 1),
$
which collapses into $O(sqrt(N))$ floor-division blocks, each weighted by a difference of the Mertens function $M$.

The only real work is evaluating $M$ at the $approx 2 sqrt(N)$ block boundaries up to $10^10$. The standard two-tier method applies: sieve $mu$ up to $2 dot 10^7$ and take prefix sums, then for larger arguments use the identity $sum_(d >= 1) M(floor(x \/ d)) = 1$ rearranged to $M(x) = 1 - sum_(d >= 2) M(floor(x \/ d))$, itself evaluated blockwise. Because floors compose ($floor(floor(N\/a) \/ b) = floor(N \/ (a b))$), every argument that ever arises is of the form $floor(N \/ k)$, so computing those in increasing order makes each evaluation a single pass and the total cost $O(N^(2\/3))$. The given $D(10^6) = 831909254469114121$ checks the pipeline end to end.

#pagebreak()
#link("https://projecteuler.net/problem=389")[= Problem 389: Platonic Dice]

Solution: 2406376.3623

A d4 is rolled; its value many d6 are rolled and summed; that sum many d8; then d12; then d20. We need the variance of the final sum $I$ to four decimals.

This is the law of total variance, applied four times. For $S = X_1 + dots.c + X_N$ with the $X_i$ iid and independent of $N$,
$
EE[S] = EE[N] thin EE[X], wide "Var"(S) = EE[N] "Var"(X) + "Var"(N) thin EE[X]^2.
$
A fair $m$-sided die has mean $(m + 1)\/2$ and variance $(m^2 - 1)\/12$, so the chain $T -> C -> O -> D -> I$ is four applications of the compounding formula starting from the d4's $(5\/2, 5\/4)$. Exact rational arithmetic gives $"Var"(I) = 2464129395 \/ 1024$, and the compounding step is validated against a brute-force enumeration of the exact distribution of $C$ (sum of $T$ six-sided dice). Rounded to four decimals: $2406376.3623$.

#pagebreak()
#link("https://projecteuler.net/problem=390")[= Problem 390: Triangles with Non Rational Sides and Integral Area]

Solution: 2919133642971

$S(n)$ sums the integral areas at most $n$ over all triangles with sides $sqrt(1 + b^2)$, $sqrt(1 + c^2)$ and $sqrt(b^2 + c^2)$ for positive integers $b, c$; we need $S(10^10)$.

Placing the triangle with vertices at the origin and $(b, 1)$, the third vertex is forced onto the line $b x + y = 1$, and the area works out to $1/2 sqrt(b^2 + c^2 + b^2 c^2)$ — the example $b = 2$, $c = 8$ gives $sqrt(324) \/ 2 = 9$ as stated. Integral area $A$ thus means $b^2 + c^2 + b^2 c^2 = (2A)^2 = k^2$, and reducing modulo $4$ forces $b$ and $c$ both even (any other parity leaves the left side $equiv 1$ or $3$).

For fixed $a$, the equation $k^2 - (a^2 + 1) c^2 = a^2$ is a Pell-type equation whose unit is $(2a^2 + 1, 2a)$, so the solutions in $c$ form chains under $c -> (2a^2 + 1) c plus.minus 2 a k$. A Vieta-style descent — jumping the larger element of a pair downward strictly shrinks it, with the sign analysis showing the jump lands in $(0, c)$ when $c > 2a^2$ and below $2a$ otherwise — terminates every solution at $c = 0$, i.e. at a root pair $\{b, 2 b^2\}$. The search therefore walks the tree from those roots, branching on both jump signs of both coordinates and keeping children that exceed the current maximum (the rejected sign is the parent direction), bounded by $k <= 2n$. Only $1218$ triangles exist below $10^10$, found instantly, and the tree provably agrees with a quadratic brute force up to $10^5$.

#pagebreak()
#link("https://projecteuler.net/problem=393")[= Problem 393: Migrating Ants]


Solution: 112398351350823112

Each of the $n^2$ ants on an $n times n$ grid steps to an adjacent square, all destinations are distinct, and no two ants use the same edge; $f(10)$ counts the moves.

Distinct destinations make the move a permutation of the squares in which every square maps to a neighbour, and the shared-edge rule eliminates exactly the $2$-cycles, where two ants would swap across one edge. So $f(n)$ counts directed cycle covers of the grid graph in which each undirected edge carries at most one ant — and since the grid is bipartite with unequal colour classes when $n$ is odd, $f(3) = 0$ falls out as a sanity check.

The count comes from a broken-profile dynamic program over cells in row-major order. The frontier records one ternary state per column for the vertical edge dangling below the processed region — unused, pointing down, or pointing up — plus one state for the horizontal edge to the left of the next cell. Processing a cell combines its incoming up/left edge states with a choice of down/right states subject to the local conservation law: exactly one edge into the cell and one out (boundary edges forced unused). Each transition is a slice operation on an $(n + 1)$-dimensional array of side $3$; with Python-integer entries the count is exact with no overflow concern, and the verified values $f(2) = 2$ and $f(4) = 88$ confirm the bookkeeping before $f(10)$ is read off the all-unused state.

#pagebreak()
#link("https://projecteuler.net/problem=394")[= Problem 394: Eating Pie]

Solution: 3.2370342194

Jeff repeatedly slices the remaining pie with two cuts to uniformly random border points and keeps only the counterclockwise-most of the three resulting pieces, stopping once less than a fraction $F = 1\/x$ remains. We want the expected number of rounds $E(40)$.

If $U_1, U_2$ are uniform on $[0,1]$, the kept fraction multiplies by $r = 1 - max(U_1, U_2)$, whose density is $2(1 - r)$. Writing $g(p)$ for the expected number of remaining rounds when a fraction $p$ is left, $g(p) = 0$ for $p < F$ and otherwise $g(p) = 1 + integral_0^1 g(p r) dot 2(1 - r) dif r$. Rewriting the integral over $q = p r$ and differentiating twice converts this into the Euler equation
$
p^2 g''(p) + 4 p g'(p) = 2,
$
with $g(F) = 1$ and $g'(F) = 0$ at the threshold. Its general solution $g(p) = C_1 + C_2 p^(-3) + (2\/3) ln p$, evaluated at $p = 1$ after fixing the constants, gives the closed form
$
E(x) = 7/9 + 2/3 ln x + 2/(9 x^3),
$
which matches $E(1) = 1$, $E(2) approx 1.2676536759$ and $E(7.5) approx 2.1215732071$ exactly, so $E(40) approx 3.2370342194$.

#pagebreak()
#link("https://projecteuler.net/problem=397")[= Problem 397: Triangle on Parabola]

Solution: 141630459461893728

Three points sit on $y = x^2 \/ k$ at integer $x$-coordinates $a < b < c$; $F(K, X)$ counts quadruplets $(k, a, b, c)$ with $1 <= k <= K$, $-X <= a < b < c <= X$, whose triangle has at least one $45 degree$ angle. We want $F(10^6, 10^9)$.

The chord joining the points at $x = u$ and $x = v$ has slope $(u + v) \/ k$, so the tangent of the angle between two edges meeting at a vertex is a tidy rational expression, and demanding exactly $45 degree$ (the acute case, distinguishing it from $135 degree$) factors into a product equal to $-2 k^2$:
$
"C1 (at " a ")": (a + b - k)(a + c + k) = -2 k^2, quad
"C2 (at " c ")": (a + c - k)(b + c + k) = -2 k^2,
$
$
"C3 (at " b ")": (a + b + k)(b + c - k) = -2 k^2.
$
The answer is $|"C1" union "C2" union "C3"|$. For one condition, one pairwise vertex-sum equals a signed divisor of $2 k^2$ while the remaining vertex is free, contributing a clamped interval of valid values, summed over the divisors of $2 k^2$ (generated from a smallest-prime-factor sieve of $k$). Satisfying two conditions at once forces a right-isosceles triangle and is counted by requiring a second quantity to divide $2 k^2$; all three at once is impossible, since three $45 degree$ angles cannot sum to $180 degree$. The reflection $x -> -x$ gives $|"C1"| = |"C2"|$ and $|"C2" sect "C3"| = |"C1" sect "C3"|$, so $F = 2|"C1"| + |"C3"| - |"C1" sect "C2"| - 2|"C1" sect "C3"|$. The checks $F(1, 10) = 41$ and $F(10, 100) = 12492$ confirm it.

#pagebreak()
#link("https://projecteuler.net/problem=398")[= Problem 398: Cutting Rope]

Solution: 2010.59096

A length-$n$ rope is cut at $m - 1$ of its $n - 1$ integer interior points, giving $m$ segments; $E(n, m)$ is the expected length of the second-shortest segment, and we want $E(10^7, 100)$.

Each cut pattern is a composition of $n$ into $m$ positive parts, all $binom(n-1, m-1)$ of them equally likely, so $E = sum_(t >= 1) P("second-shortest" >= t)$. The second-shortest is at least $t$ exactly when at most one part is smaller than $t$, which gives
$
P(>= t) = (A(t) + m (binom(W, m-1) - binom(W-t+1, m-1))) / binom(n-1, m-1),
$
where $A(t) = binom(n-1-m(t-1), m-1)$ counts patterns with every part $>= t$, and the bracket counts patterns with exactly one part below $t$ ($m$ placements, the small part's value summed away by the hockey-stick identity), with $W = n-1-(m-1)(t-1)$.

Each ratio $binom(x, m-1) \/ binom(n-1, m-1)$ is evaluated as the product $product_(i=0)^(m-2) (x-i)\/(n-1-i)$; forming it as a product rather than via differences of log-gammas avoids catastrophic cancellation and keeps full double precision. Summing over $t$ (a few times $n\/m$ terms) gives $2010.59096$; the checks $E(3, 2) = 2$ and $E(8, 3) = 16\/7$ confirm the setup.

#pagebreak()
#link("https://projecteuler.net/problem=399")[= Problem 399: Squarefree Fibonacci Numbers]

Solution: 1508395636674243,6.5e27330467

We need the $10^8$-th squarefree Fibonacci number, reported as its last sixteen digits and a one-significant-figure scientific form.

Assuming Wall's conjecture (the first Fibonacci divisible by a prime $p$ is never divisible by $p^2$), $p^2 divides F_n$ exactly when $p dot alpha(p) divides n$, where $alpha(p)$ is the rank of apparition of $p$ (the least $m$ with $p divides F_m$, a divisor of $p - (5\/p)$). Hence $F_n$ fails to be squarefree precisely when $n$ is a multiple of some modulus $m_p = p dot alpha(p)$, and the squarefree Fibonacci indices are those struck out by none of these moduli. A prime contributes a modulus $<= N$ only if $alpha(p) <= N\/p$, so a direct scan of primes up to about $1.6 dot 10^6$ collects them all — any larger prime would need a tiny rank of apparition, i.e. it would divide $F_a$ for a small $a$, and checking those $F_a$ adds nothing new.

Sieving the moduli up to $N approx 1.4 dot 10^8$ and taking a running count places the $10^8$-th squarefree index at $n = 130775524$. Fast-doubling gives $F_n mod 10^16 = 1508395636674243$, and $log_10 F_n = n log_10 phi - (1\/2) log_10 5$ gives the magnitude $6.5 times 10^27330467$. The stated $200$-th value $F_260 approx 9.7 e 53$ confirms the method.

#pagebreak()
#link("https://projecteuler.net/problem=400")[= Problem 400: Fibonacci Tree Game]

Solution: 438505383468410633

On the Fibonacci tree $T(k)$ — a root with $T(k - 1)$ and $T(k - 2)$ as children — players alternately remove a node together with its subtree, and whoever is forced to take the global root loses. $f(k)$ counts the first player's winning first moves; we want the last $18$ digits of $f(10000)$.

== Grundy values collapse to a one-line recursion

For this subtree-removal game the Grundy value of a rooted tree is $1$ plus the xor of its children's values: removing the root reaches $0$, and a move inside one child replaces its value freely within its own game, so the mex telescopes. Hence $G(k) = 1 + (G(k - 1) plus.circle G(k - 2))$ with $G(0) = 0$, $G(1) = 1$ — verified against a direct game-tree solver on the actual trees up to $T(6)$ (whose first draft conflated "leaf" with "removed entirely" in the tree encoding, caught by exactly that check). The values stay remarkably small: $G(10000)$ fits in three bits.

== Counting moves, not just winners

Nobody takes the root voluntarily, so the position value is $G(k - 1) plus.circle G(k - 2)$ and a first move wins iff it zeroes the xor. Let $"cnt"(j, t)$ be the number of single-node removals inside $T(j)$ that leave it at Grundy value $t$. Internal moves always produce a value of at least $1$, so $"cnt"(j, 0) = 1$ (remove $T(j)$ whole), and otherwise the move lives in one of the two child subtrees:
$
"cnt"(j, t) = "cnt"(j - 1, (t - 1) plus.circle G(j - 2)) + "cnt"(j - 2, (t - 1) plus.circle G(j - 1)),
$
with $f(k) = "cnt"(k - 1, G(k - 2)) + "cnt"(k - 2, G(k - 1))$. The reachable $(j, t)$ states were probed empirically before committing — about $1.7 dot 10^7$ at $k = 10^4$, comfortable for a memoised iterative evaluation — and counts only ever add, so reducing modulo $10^18$ is exact for the last-$18$-digits answer. The recursion matches the brute-force game solver through $k = 5$ and reproduces both givens $f(5) = 1$ and $f(10) = 17$.

#pagebreak()
#link("https://projecteuler.net/problem=401")[= Problem 401: Sum of Squares of Divisors]

Solution: 281632621

Let $sigma_2(n)$ be the sum of the squares of the divisors of $n$ and $"SIGMA2"(n) = sum_(i=1)^n sigma_2(i)$; we need $"SIGMA2"(10^15) mod 10^9$.

Rather than factorise every $i$, count contributions by divisor. A fixed $k$ divides exactly $floor(n\/k)$ of the integers $1, ..., n$, so it contributes $k^2$ to each of them:
$
"SIGMA2"(n) = sum_(k=1)^n floor(n\/k) dot k^2.
$
The quotient $floor(n\/k)$ takes only $O(sqrt(n))$ distinct values, and the $k$ giving a fixed quotient $q$ form a contiguous block $[k_0, floor(n\/q)]$. Over such a block the contribution is $q sum_(k=k_0)^(k_1) k^2$, and the prefix sums of squares are $sum_(k=1)^m k^2 = m(m+1)(2m+1)\/6$. Walking the blocks brings the cost from $10^15$ down to about $2 sqrt(10^15) approx 6.3 dot 10^7$ steps.

The modulus $10^9$ is not prime, so the $\/6$ cannot be done with a modular inverse. Instead it is carried out exactly before reducing: among $m$ and $m+1$ one is even, and among $m$, $m+1$ and $2m+1$ one is a multiple of $3$, so dividing the appropriate factors removes the $6$ while everything is still an integer. The three reduced factors are then each taken $mod 10^9$ and multiplied with reductions in between, every intermediate product staying below $10^18$. As a check, $"SIGMA2"(6) = 113$.

#pagebreak()
#link("https://projecteuler.net/problem=402")[= Problem 402: Integer-valued Polynomials]

Solution: 356019862

$M(a, b, c)$ is the largest $m$ dividing $n^4 + a n^3 + b n^2 + c n$ for every integer $n$, and $S(N)$ sums it over $0 < a, b, c <= N$. We want the last nine digits of $sum S(F_k)$ for $2 <= k <= 1234567890123$.

== M lives modulo 24

By Newton's basis every value of the polynomial is an integer combination of $f(0), dots.h, f(4)$, so $M = gcd(f(1), f(2), f(3), f(4))$; it divides the fourth difference $4! = 24$, and depends on $(a, b, c)$ only modulo $24$ (brute-checked against gcds over many $n$, negatives included). Writing $N = 24 q + t$, each residue class is hit $q$ or $q + 1$ times, so $S(N) = E_0 q^3 + E_1(t) q^2 + E_2(t) q + E_3(t)$ with coefficients read off a $24^3$ table — instantly reproducing both givens $S(10) = 1972$ and $S(10^4) = 2024258331114$.

== Fibonacci power sums in exact arithmetic

$F_k mod 24$ has Pisano period exactly $24$, so $t$ is constant on each class $k equiv s (mod 24)$ and the task reduces to $sum F_k^e$ ($e <= 3$) over arithmetic progressions of $k$ up to $1.2 dot 10^12$. The map $(F_k, F_(k + 1)) -> (F_(k + 24), F_(k + 25))$ is linear, so its induced action on the ten monomials of degree $<= 3$, augmented with four running accumulators, is a $14 times 14$ matrix; powering it with exact Python integers modulo $24^3 dot 10^9$ leaves enough headroom to divide $sum (F_k - t)^j$ by $24^j$ *exactly* (the modulus $10^9$ alone has no inverse of $24$). The whole pipeline is validated against direct summation of $S(F_k)$ for $k <= 50$ before the full run, which finishes in under a second.

#pagebreak()
#link("https://projecteuler.net/problem=405")[= Problem 405: A Rectangular Tiling]

Solution: 237696125

A $2 : 1$ rectangle is repeatedly subdivided: each tile is replaced by two side strips (each a rotated $2 : 1$ rectangle, a quarter of the long side wide) and a central square cut into two stacked $2 : 1$ tiles. $f(n)$ counts the points of $T(n)$ where four tiles meet; we want $f(10^k)$ for $k = 10^18$, modulo $17^7$.

== Finding the closed form

Four tiles meet at a point exactly when the point is a corner of four tiles (with fewer corners the point lies in the interior of some tile's edge, giving a T-junction of at most three tiles). Simulating the subdivision directly — coordinates scaled by $4$ per step to stay integral, corners tallied in a hash map — gives
$
f(1), dots.h, f(10) = 0, 2, 16, 82, 368, 1554, 6384, 25874, 104176, 418066.
$
The differences $g(n) = f(n) - 4 f(n - 1)$ satisfy $g(n) = 2 g(n - 1) + 3 - (-1)^n$, and unwinding both linear recurrences yields
$
f(n) = (6 dot 4^n - 20 dot 2^n + 15 - (-1)^n) / 15,
$
which reproduces all ten simulated values, $f(4) = 82$, and the given $f(10^9) mod 17^7 = 126897180$.

== Evaluating at $n = 10^(10^18)$

Since $2$ and $4$ are coprime to $17^7$, exponents reduce modulo $phi(17^7) = 16 dot 17^6$: compute $e = 10^(10^18) mod 16 dot 17^6$ by modular exponentiation, then $4^n equiv 4^e$ and $2^n equiv 2^e$. The exponent $n$ is even, so $(-1)^n = 1$, and $15$ is invertible mod $17^7$. The whole computation is a handful of `pow` calls.

#pagebreak()
#link("https://projecteuler.net/problem=406")[= Problem 406: Guessing Game]

Solution: 36813.12757207

Guessing a hidden number in ${1, dots.h, n}$ costs $a$ per "too low" answer and $b$ per "too high"; $C(n, a, b)$ is the optimal worst-case cost. We want $sum_(k=1)^(30) C(10^12, sqrt(k), sqrt(F_k))$ to eight decimals.

== Strategies are weighted binary trees

A strategy is a binary tree in which *every* node resolves one number (a "yes" is free), and a number reached by $i$ "lower" and $j$ "higher" answers costs $i a + j b$. The numbers coverable within worst-case budget $T$ are therefore
$
N(T) = sum_(i a + j b <= T) binom(i + j, i),
$
and $C(n, a, b)$ is the smallest value of the form $i a + j b$ with $N >= n$ — the optimum is always attained at such a lattice value.

== Searching the candidate values

Per $k$, candidates $(i, j)$ are enumerated in an adaptive box (doubled if the optimum lands near the boundary), with binomials built incrementally in exact integers capped at $n + 1$. Sorting by floating value is safe here: distinct true values of $i sqrt(k) + j sqrt(F_k)$ differ by at least about $1 \/ (i_max sqrt(k) + j_max sqrt(F_k))$ — far above `float64` error — and exactly equal values occur only in the all-rational case $k = 1$, where floats are exact. Prefix sums of the capped weights plus a scan find the minimal qualifying value; the winning $(i, j)$ is then re-evaluated in $40$-digit decimals for the final sum. The Fibonacci growth makes the trees wildly lopsided by $k = 30$ ($b = sqrt(832040) approx 912$), which the box adaptation absorbs automatically.

All four given values reproduce — $C(5, 2, 3) = 5$, $C(20000, 5, 7) = 82$ and both irrational examples to every printed digit — alongside an interval DP on small instances, whose first draft charged phantom costs for empty branches ($g = 1$ or $g = m$) and was caught by exactly this cross-check.

#pagebreak()
#link("https://projecteuler.net/problem=407")[= Problem 407: Idempotents]

Solution: 39782849136421

For each $n$ let $M(n)$ be the largest $a < n$ with $a^2 equiv a space (mod n)$ — an _idempotent_ — and we want $sum_(n=1)^(10^7) M(n)$.

The congruence $a^2 equiv a$ means $n divides a(a-1)$. Since $a$ and $a-1$ are coprime, each prime power $p^e$ dividing $n$ must divide $a$ or $a-1$ entirely, i.e. $a equiv 0$ or $a equiv 1 space (mod p^e)$. By the Chinese remainder theorem an idempotent is exactly a choice of $0$ or $1$ on each of the $omega(n)$ prime-power factors, giving $2^(omega(n))$ of them.

So the work per $n$ is: factor $n$ into prime powers $q_1, ..., q_m$ with a smallest-prime-factor sieve; build the CRT basis $e_i$ (the value that is $1 space (mod q_i)$ and $0$ on the others, computed as $(n\/q_i) dot (n\/q_i)^(-1) mod q_i$); and take the maximum of the $2^m$ subset sums $sum_(i in S) e_i mod n$. The all-empty choice gives $0$ and the all-ones choice gives $1$, so prime powers correctly yield $M = 1$; the largest subset sum below $n$ is $M(n)$. As checks, $M(6) = 4$, $sum_(n<=20) M = 75$ and $sum_(n<=100) M = 2549$. The $2^(omega(n))$ subsets sum to roughly $10^8$ across the whole range, so the sieve-and-enumerate runs in a few seconds.

#pagebreak()
#link("https://projecteuler.net/problem=408")[= Problem 408: Admissible Paths Through a Grid]

Solution: 299742733

A lattice point is _inadmissible_ when $x$, $y$ *and* $x + y$ are all positive perfect squares; $P(n)$ counts north/east paths from $(0, 0)$ to $(n, n)$ avoiding such points. We want $P(10^7) mod 10^9 + 7$.

== Few bad points, not many

The third condition is the whole problem. Requiring only $x = a^2$, $y = b^2$ would give about $10^7$ bad points and sink the standard technique; adding $a^2 + b^2 = c^2$ makes the bad points exactly the Pythagorean leg pairs with legs at most $sqrt(10^7) approx 3162$ — and there are only $7850$ of them, found by a direct double loop with a perfect-square test.

== First-bad-point inclusion–exclusion

With the bad points sorted lexicographically, let $f_i$ be the number of paths from the origin to bad point $i$ that avoid all earlier bad points:
$
f_i = binom(x_i + y_i, x_i) - sum_(j: x_j <= x_i, y_j <= y_i) f_j binom(Delta x + Delta y, Delta x),
$
and then $P(n) = binom(2n, n) - sum_i f_i binom((n - x_i) + (n - y_i), n - x_i)$. With $K = 7850$ the $O(K^2)$ double loop is about $6 dot 10^7$ binomial products over factorial tables up to $2n$. The given values $P(5) = 252$, $P(16) = 596994440$ and $P(1000) equiv 341920854$ all reproduce, alongside a full dynamic-programming brute force over the grid for $n <= 60$.

#pagebreak()
#link("https://projecteuler.net/problem=409")[= Problem 409: Nim Extreme]

Solution: 253223948

A position is $n$ distinct pile sizes drawn from ${1, ..., 2^n - 1}$ — equivalently the nonzero vectors of $FF_2^n$ — and it is winning unless its nim-sum (XOR) is zero. The worked value $W(2) = 6$ counts the three two-element subsets of ${1, 2, 3}$ in both orders each, so positions are *ordered* tuples. Writing $M = 2^n - 1$, the total ordered count is the falling factorial $P(M, n) = M (M-1) dots.c (M - n + 1)$, and
$
W(n) = P(M, n) - n! dot Z(n),
$
where $Z(n)$ is the number of $n$-element *subsets* of the nonzero vectors with XOR zero.

To count $Z(n)$, average the zero-sum indicator over the characters $chi_w (v) = (-1)^(w dot v)$ of $FF_2^n$. For a fixed $w$ the generating polynomial $product_(v != 0) (1 + x chi_w (v))$ splits by how many nonzero $v$ lie on each side of the hyperplane $w dot v = 0$: the trivial character $w = 0$ gives $(1+x)^(M)$, and each of the $M$ nonzero characters gives $(1+x)^(2^(n-1)-1) (1-x)^(2^(n-1))$. Hence
$
Z(n) = 1/2^n [binom(M, n) + M dot c_n], quad c_n = [x^n] (1+x)^(2^(n-1)-1) (1-x)^(2^(n-1)).
$
Combining and using $n! binom(M, n) = P(M, n)$,
$
W(n) = P(M, n) - 2^(-n) [P(M, n) + M dot n! dot c_n] space (mod 10^9 + 7).
$
The exponents $2^(n-1)$ are astronomically large, but only the single coefficient $c_n = sum_(j=0)^n binom(a, j) binom(b, n-j) (-1)^(n-j)$ is needed (with $a equiv 2^(n-1) - 1$, $b equiv 2^(n-1)$ reduced $mod p$, the binomials evaluated as falling factorials). Precomputing inverses $1..n$, building $binom(b, dot)$ forward and $binom(a, dot)$ incrementally turns the whole thing into a handful of $O(n)$ passes. It reproduces $W(1..3) = 1, 6, 168$, $W(5) = 19764360$ and $W(100) equiv 384777056$.

#pagebreak()
#link("https://projecteuler.net/problem=411")[= Problem 411: Uphill Paths]

Solution: 9936352

For each $n$ there are stations at $(2^i mod n, 3^i mod n)$ for $0 <= i <= 2n$ (coincident stations count once), and $S(n)$ is the most stations a path from $(0, 0)$ to $(n, n)$ with non-decreasing coordinates can visit. We want $sum_(k=1)^(30) S(k^5)$.

== Generating the stations

Listing all $2n + 1$ indices is wasteful: the pair sequence is eventually periodic. $2^i mod n$ has pre-period equal to the exponent of $2$ in $n$ — at most $20$ when $n = k^5$, $k <= 30$ — and similarly for $3$, so from index $25$ onward the sequence is purely cyclic with period at most $lambda(n) <= n$. Generate pairs until the index-$25$ pair recurs; that window contains every distinct station, at most $n + 25$ of them instead of $2n + 1$.

== Longest uphill chain

Encode each station as the single key $x n + y$, sort, and drop duplicates: the stations are now ordered by $x$, with ties broken by ascending $y$. A monotone path is then exactly a non-decreasing subsequence of the $y$ values, so $S(n)$ is the longest such subsequence, found by patience sorting with an upper-bound binary search in $O(m log m)$. The given values $S(22) = 5$, $S(123) = 14$ and $S(10000) = 48$ all reproduce; the full sum (largest case $n = 30^5 approx 2.4 dot 10^7$) takes under half a minute.

#pagebreak()
#link("https://projecteuler.net/problem=412")[= Problem 412: Gnomon Numbering]

Solution: 38788800

$L(m, n)$ is an $m times m$ grid with the top-right $n times n$ corner removed, and $"LC"(m, n)$ counts numberings of its cells by $1, 2, dots.h$ in which every cell is smaller than the cell below it and the cell to its left. We want $"LC"(10000, 5000) mod 76543217$.

== Reduction to a standard Young tableau

Rotate the gnomon by $180 degree$ and replace each entry $c$ by $N + 1 - c$ (where $N = m^2 - n^2$ is the cell count). The two constraints become "smaller than the cell to the right" and "smaller than the cell below", and the rotated region is left-justified with weakly decreasing row lengths — a genuine Young diagram $lambda$ with $m - n$ rows of length $m$ followed by $n$ rows of length $m - n$. So $"LC"(m, n)$ is the number of standard Young tableaux of $lambda$, given by the hook length formula
$
"LC"(m, n) = N! / (product_("cells" (i, j)) h(i, j)),
$
with $h(i, j)$ the usual arm + leg + 1 hook (column heights here take just two values, $m$ and $m - n$).

== Modulo $76543217$

The modulus is prime, and crucially $N = 75 dot 10^6$ and every hook (at most $2m - 1$) are *smaller* than it, so neither $N!$ nor the hook product vanishes mod $p$. Compute both with a $75$-million-step loop and finish with one Fermat inverse. The exact hook formula reproduces $"LC"(3, 0) = 42$, $"LC"(5, 3) = 250250$ and $"LC"(6, 3) = 406029023400$, and the modular version gives $"LC"(10, 5) equiv 61251715$, all matching the problem.

#pagebreak()
#link("https://projecteuler.net/problem=413")[= Problem 413: One-child Numbers]

Solution: 3079418648040719

A $d$-digit number (no leading zero) is _one-child_ if exactly one of its contiguous substrings — read by value, so leading zeros are fine and a lone $0$ divides everything — is divisible by $d$. $F(N)$ counts one-child numbers below $N$; we want $F(10^19)$, summed over lengths $d = 1, dots.h, 19$.

== The residue multiset is the whole state

Scan the digits left to right and follow the residues mod $d$ of every substring ending at the current position: appending digit $c$ sends each residue $r$ to $10 r + c$ and starts a fresh single-digit substring $c$. Children accrue exactly when classes land on residue $0$. Two suffixes sharing a residue stay together forever, so only the *multiset* of residues matters — and any class of size two or more that lands on $0$ produces two children at once, which is fatal. Counts therefore cap at $2$, and the state is $d$ trits plus a child flag ($0$ or $1$; two or more dies). Correctness of the cap: capped classes only ever merge upward, and "at least two" is all the kill rule needs.

== Reachable states stay small

The worry is $3^d$ states, but the reachable set is tiny: probing showed peaks of about $1.3 dot 10^5$ states at $d = 17$ and $5.3 dot 10^5$ at $d = 19$. The DP keeps a table of state rows with multiplicities and advances a whole digit layer at once with vectorised column scatters, then merges duplicates by sorting packed rows — about ten seconds for all nineteen lengths combined. Counts brush $2.3 dot 10^15$ at $d = 18$ but stay well inside $64$ bits.

Checks: exact brute-force enumeration agrees for $d = 2, 3, 4$, and the given $F(10^3) = 389$ and $F(10^7) = 277674$ reproduce as the partial sums over lengths.

#pagebreak()
#link("https://projecteuler.net/problem=414")[= Problem 414: Kaprekar Constant]

Solution: 552506775824935461

For bases $b = 6t + 3 eq.not 9$ the five-digit Kaprekar routine (sort digits descending minus ascending, repeat) converges to a constant $C_b$; $s_b (i)$ counts the iterations from $i$ (zero for $C_b$ and repdigits) and $S(b) = sum_(0 < i < b^5) s_b (i)$. We want the last $18$ digits of $sum_(k = 2)^(300) S(6k + 3)$, bases up to $1803$ with $b^5 approx 1.9 dot 10^16$ — far too many $i$ to visit.

== Collapsing to two digit statistics

Sort $i$'s digits ascending as $d_1 <= dots.h <= d_5$. The subtraction telescopes:
$
D = (d_5 - d_1)(b^4 - 1) + (d_4 - d_2)(b^3 - b),
$
so one step depends only on $(x, y) = (d_5 - d_1, d_4 - d_2)$ — about $b^2 \/ 2$ states instead of $b^5$ numbers. Define $F(x, y) = s_b (D(x, y))$; then $F(x, y) = 0$ when $D(x, y) = C_b$ and $1 + F$ of $D$'s own statistics otherwise, filled over the grid by path-following with memoisation (an off-by-one lurks here: a chain ending at an already-known state needs that value *plus one*). Every non-repdigit $i eq.not C_b$ has $s_b (i) = 1 + F(x, y)$, and $C_b$ — whose digits follow the pattern $(4t + 2, 2t, 6t + 2, 4t + 1, 2t + 1)$, verified as the routine's fixed point — corrects the total by exactly $1$.

== Counting each class

$N(x, y)$, the number of $i < b^5$ with statistics $(x, y)$, factors over the gaps $u_1, dots.h, u_4$ between consecutive sorted digits: $u_2 + u_3 = y$, $u_1 + u_4 = x - y$, $b - x$ translations of the minimum digit, and for each of the $16$ patterns of which gaps vanish, a fixed orderings count $120 \/ product ("run"!)$. That makes $N(x, y)$ an $O(1)$ evaluation and $S(b)$ an $O(b^2)$ computation. Step counts reach $620$ at $b = 1803$, so the per-class product $N dot (1 + F)$ can brush the int64 limit; an overflow-safe multiply handles the rare large classes. Checks: the class counts match a full enumeration at $b = 15$, and both given values $S(15) = 5274369$ (also brute-forced end to end) and $S(111) = 400668930299$ reproduce.

#pagebreak()
#link("https://projecteuler.net/problem=415")[= Problem 415: Titanic Sets]

Solution: 55859742

A set of lattice points is _titanic_ if some line passes through exactly two of its points; $T(N)$ counts titanic subsets of the $(N + 1)^2$ grid, and we want $T(10^11) mod 10^8$.

== Sylvester–Gallai does the heavy lifting

By the Sylvester–Gallai theorem every finite non-collinear point set has an ordinary line, so the *non*-titanic sets are exactly: the empty set, single points, and collinear sets of size at least $3$ (gaps allowed — the problem's own ${(0,0), (1,1), (2,2), (4,4)}$ example). With $g(k) = 2^k - 1 - k - binom(k, 2)$,
$
T(N) = 2^P - 1 - P - sum_("lines" L) g(k_L), quad P = (N + 1)^2.
$

== Counting lines by direction

Axis-parallel lines give $2(N + 1) g(N + 1)$. For a primitive slanted direction $(a, b)$ the window count $A_m = (N + 1 - (m - 1)a)(N + 1 - (m - 1)b)$ counts each line with $k$ points $k - m + 1$ times — *not* once, the prototype's first failure (it surfaced as exactly one phantom $5$-point line at $N = 4$). Lines with at least $m$ points are therefore $A_m - A_(m+1)$, and a second Abel summation leaves the clean weight $sum_L g = sum_m A_m (2^(m - 2) - 1)$. Substituting $s = m - 1$, Möbius-inverting the primitivity, and grouping by $t = s d$:
$
"Slant" = 2 sum_(t <= N) F(t)^2 h(t), quad h = mu * w, quad w(s) = 2^(s - 1) - 1,
$
with $F(t) = K(N + 1) - t K(K + 1)\/2$, $K = floor(N\/t)$, linear in $t$ on constant-$K$ blocks.

== Sublinear machinery mod $10^8$

Expanding $F^2$ per block needs the weighted prefix sums $H_j (x) = sum_(t <= x) t^j h(t)$ for $j = 0, 1, 2$, which unfold as $sum_d mu(d) d^j G_j (x \/ d)$ with closed-form $G_j$ (geometric-derivative sums of $s^j 2^(s-1)$). Three ingredients keep everything fast and exact mod the *composite* $10^8 = 2^8 5^8$: weighted Mertens sums $M_j (y) = sum_(d <= y) mu(d) d^j$ via the identity $sum_k k^j M_j (y\/k) = 1$, computed sublinearly over the quotients of $N$; powers of $2$ by CRT ($0$ mod $2^8$, exponent reduced mod $phi(5^8)$); and all divisions by $2$ and $6$ cancelled exactly before reducing. Every argument arising anywhere is a quotient of $N$, so $G_j$ is precomputed at the $approx 6 dot 10^5$ distinct quotients once and the $H_j$ evaluations at every block boundary are pure table lookups — about $5 dot 10^8$ block iterations in total.

The exact prototype was validated against full subset enumeration at $N = 1, 2$ and the actual line histograms before any optimisation, and the production code reproduces all five given values, including $T(111) equiv 13500401$ and $T(10^5) equiv 63259062$ which exercise the entire sublinear pipeline.

#pagebreak()
#link("https://projecteuler.net/problem=416")[= Problem 416: A Frog's Trip]

Solution: 898082747

A frog makes $m$ round trips along a row of $n$ squares, jumping $1$–$3$ ahead on each leg; $F(m, n)$ counts the travels leaving at most one square unvisited. We want $F(10, 10^12) mod 10^9$.

== Twenty independent paths

Reversing each homeward leg turns the $m$ round trips into $2m$ independent left-to-right jump paths from square $1$ to square $n$; the only coupling is the joint condition that their landing sites cover all squares except possibly one. Processing squares left to right, each path is either grounded on the current square or overflying one or two more, so the joint state is just the multiset count $(n_0, n_1, n_2)$ — paths are interchangeable for counting — plus a flag for the single allowed miss (a square where $n_0 = 0$). For $2m = 20$ that is $binom(22, 2) times 2 = 462$ states.

== One trinomial step, then matrix power

In each step the $n_0$ grounded paths redistribute into the three overfly classes with trinomial multiplicities and everyone advances one square. $F(m, n)$ is the entry of the step matrix to the power $n - 1$ from all-grounded to all-grounded (both endpoints are always visited). Squaring the $462 times 462$ matrix forty times handles $n = 10^12$ in a few seconds of numba. All five given values reproduce — the four exact small ones also against a direct enumeration over tuples of paths — plus an extra brute-force point at $F(2, 6)$.

#pagebreak()
#link("https://projecteuler.net/problem=417")[= Problem 417: Reciprocal Cycles II]

Solution: 446572970925740

$L(n)$ is the length of the recurring cycle of $1\/n$ ($0$ when $n$ has no prime factors besides $2$ and $5$); we want $sum_(n=3)^(10^8) L(n)$.

The cycle length is the multiplicative order of $10$ modulo $n$ with all factors of $2$ and $5$ stripped — equivalently, the lcm of $"ord"_(p^k)(10)$ over the prime powers $p^k || n$ with $p eq.not 2, 5$. Three ingredients make this linear-ish over $10^8$:

+ *Prime orders.* For each prime $p$, $"ord"_p (10)$ divides $p - 1$: factor $p - 1$ with a smallest-prime-factor sieve, and for each prime factor $q$ keep dividing the exponent by $q$ while $10$ to the reduced power is still $1 mod p$.
+ *Prime-power lifting.* $"ord"_(p^(k+1))(10)$ equals $"ord"_(p^k)(10)$, times $p$ exactly when $10^("ord") eq.not 1 mod p^(k+1)$ — one modular exponentiation per level, and only $p < 10^4$ have higher powers in range.
+ *The lcm sieve.* For each prime power $q = p^k$, fold its order into $L[m]$ by lcm for every $m$ exactly divisible by $q$ (multiples of $q$ whose cofactor is not divisible by $p$). The total work is $sum_q 10^8 \/ q approx 3 dot 10^8$ gcd operations.

Numbers of the form $2^a 5^b$ retain the initial placeholder $1$ and are corrected at the end (there are only a few hundred). The stated check $sum_(n=3)^(10^6) L(n) = 55535191115$ reproduces, as do the cycle lengths of $1\/3, dots.h, 1\/10$ from the problem table.

#pagebreak()
#link("https://projecteuler.net/problem=418")[= Problem 418: Factorisation Triples]

Solution: 1177163565297340320

$f(n) = a + b + c$ for the divisor triple $a <= b <= c$, $a b c = n$, minimising $c \/ a$; we want $f(43!)$.

== Half a billion divisors, log-uniformly dense

$43!$ has about $5.2 dot 10^8$ divisors spread log-uniformly over $122$ nats, roughly $8500$ per $0.1%$ multiplicative window — so the optimal triple is balanced extremely close to $n^(1\/3)$. The divisors inside a $plus.minus 2%$ window of the cube root come from a meet-in-the-middle split of the fourteen primes into halves of about $2 dot 10^4$ divisors each: one half sorted, the other scanned with binary searches for the complementary range, yielding the window list directly.

== Scan down, prune hard

Candidate $a$ walks downward from the cube root. For fixed $a$, the ratio $c \/ a = n \/ (a^2 b)$ decreases in $b$, so the best partner is the *largest* window divisor $b <= sqrt(n \/ a)$ with $b >= a$ and $a b | n$ — the first divisibility hit wins and the inner scan stops. The outer scan stops by the unconditional bound $c \/ a >= sqrt(n \/ a^3)$, which only grows as $a$ shrinks; once it passes the best ratio found (compared exactly by cross-multiplied big integers) no smaller $a$ can win, and the code asserts the stop came from the bound rather than window exhaustion. The same code reproduces the given $f(20!) = 4034872$, and a plain brute force confirms $f(165) = 19$ and $f(100100) = 142$. The full run takes a fraction of a second.

#pagebreak()
#link("https://projecteuler.net/problem=419")[= Problem 419: Look and Say Sequence]

Solution: 998567458,1046245404,43363922

Count the ones, twos and threes in the $10^12$-th term of the look-and-say sequence, modulo $2^30$.

== Conway's elements, rediscovered programmatically

Conway's cosmological theorem says every look-and-say string eventually decomposes into a fixed set of $92$ "elements" that evolve independently forever. Rather than transcribing his table, the solution rediscovers it: a candidate split point (only between differing digits) is accepted when the two halves, evolved separately for fifteen steps, concatenate to the evolution of the whole at every step. Starting from "$1$" and closing the set of irreducible chunks under one-step decay yields the elements plus a handful of early transients — which are harmless, since they too get rows in the decay matrix and simply feed the persistent ones.

== Then it's linear algebra

With the decay matrix $D$ in hand, the composition vector of term $n$ is $v_1 D^(n - 1)$, and the digit counts are inner products with each element's literal digit tallies. The matrix is on the order of a hundred square, so powering to $10^12$ modulo $2^30$ is immediate. The decisive validation: the matrix-based counts are compared against *direct string simulation* for a spread of $n$ up to $48$ (where the term already has $10^5$ digits), including the given $A(40), B(40), C(40) = 31254, 20259, 11625$ — any false split would break those equalities.

#pagebreak()
#link("https://projecteuler.net/problem=420")[= Problem 420: $2 times 2$ Positive Integer Matrix]

Solution: 145159332

$F(N)$ counts $2 times 2$ positive integer matrices with trace below $N$ that are squares of positive integer matrices in *two* different ways; we want $F(10^7)$.

== Parametrising double squares

Suppose $M = A^2 = B^2$ with traces $t = "tr" A$, $t' = "tr" B$. Equal traces force $A = B$ (Cayley–Hamilton gives $t A - t B = (det A - det B) I$, which for $t = t'$ makes $A - B$ scalar and then zero), so $t eq.not t'$. Write $g = gcd(t, t')$, $t = g T$, $t' = g T'$ with $gcd(T, T') = 1$. Matching the entries of $A^2$ and $B^2$ — off-diagonals $b t = b' t'$, $c t = c' t'$ and the diagonal difference $(a - e) t = (a' - e') t'$ — forces $b = T' b_0$, $c = T' c_0$, $a - e = T' delta$ (and symmetrically with $T$ for $B$), and equating the traces of the two expressions for $M$ collapses, after cancelling $T^2 - T'^2$, to
$
g^2 - delta^2 = 4 b_0 c_0, quad "tr" M = (g^2 (T^2 + T'^2)) / 2.
$
Conversely each tuple $(T > T', g, delta, b_0, c_0)$ — with $delta equiv g space (mod 2)$, both $T, T'$ odd when $g$ is odd (integrality of the diagonal entries), and $|delta| <= (g T' - 2) \/ T$ (positivity of $B$'s diagonal; $A$'s follows) — produces exactly one $M$, and a $2 times 2$ matrix has at most two positive roots, so there is no double counting. Hence
$
F(N) = sum_(T, T', g, delta) d((g^2 - delta^2) / 4),
$
the divisor counts coming from the factorisations $4 b_0 c_0 = g^2 - delta^2$. The triple loop over $(T', T, g)$ with the inner $delta$ scan costs $O(N)$ overall with a divisor-count sieve up to $N \/ 10$. Both $F(50) = 7$ (also confirmed by brute-force squaring of small matrices) and $F(1000) = 1019$ reproduce.

#pagebreak()
#link("https://projecteuler.net/problem=421")[= Problem 421: Prime Factors of $n^15 + 1$]

Solution: 2304215802083466198

$s(n, m)$ sums the distinct primes $p <= m$ dividing $n^15 + 1$; we want $sum_(n <= 10^11) s(n, 10^8)$.

Swap the two sums: each prime $p <= 10^8$ contributes $p$ once for every $n <= 10^11$ with $n^15 equiv -1 space (mod p)$, so it suffices to know, for each prime, the residues solving that congruence.

Because $15$ is odd, $x = -1$ is always a solution. The full solution set is then $-1$ times the group $mu$ of $15$th roots of unity mod $p$, which is cyclic of order $g = gcd(15, p - 1) in {1, 3, 5, 15}$ (in the cyclic multiplicative group, $x^15 = 1$ has exactly $g$ solutions). For $g = 1$ (primes with $p eq.not 1$ mod $3$ and mod $5$, about $3\/8$ of them) the only root is $n equiv -1$. Otherwise take $z = 2, 3, dots.h$ and let $w = z^((p-1)\/g)$; once some $w$ has order exactly $g$ (checked by $w^(g\/3) eq.not 1$ and $w^(g\/5) eq.not 1$ for the prime divisors of $g$), its powers enumerate all of $mu$.

Each root $r in [1, p - 1]$ accounts for $floor((N - r)\/p) + 1$ values of $n <= N$. Summing $p$ times that count over the roots of every prime up to $10^8$ (sieved) gives the answer; the total stays below $2^63$. The method is verified against a direct trial-division computation of $sum_(n <= 100) s(n, 10^4)$ and the problem's $s(10, 1000) = 483$.

#pagebreak()
#link("https://projecteuler.net/problem=422")[= Problem 422: Sequence of Points on a Hyperbola]

Solution: 92060460

On $H: 12x^2 + 7x y - 12y^2 = 625$, starting from $P_1 = (13, 61\/4)$ and $P_2 = (-43\/6, -4)$, each $P_i$ is the second intersection of $H$ with the line through $P_(i-1)$ parallel to $P_(i-2) X$, where $X = (7, 1)$. Find $P_n$ for $n = 11^14$, reported as $(a + b + c + d) mod (10^9 + 7)$ over the reduced coordinates.

== The hyperbola factors

$12x^2 + 7x y - 12y^2 = (3x + 4y)(4x - 3y)$, so substituting $u = 3x + 4y = 25t$ gives $v = 4x - 3y = 25\/t$ and $x = 3t + 4\/t$, $y = 4t - 3\/t$. A chord between parameters $t_1, t_2$ has slope proportional to $-1\/(t_1 t_2)$: *chords are parallel exactly when their parameter products agree*. Since $t_X = 1$, the construction is simply $t_i t_(i-1) = t_(i-2)$, i.e. $t_i = t_(i-2) \/ t_(i-1)$ — and with $t_1 = 4$, $t_2 = -3\/2$, the exponents obey $c_i = c_(i-2) - c_(i-1)$, giving $t_n = 4^(plus.minus F_(n-2)) (-3\/2)^(minus.plus F_(n-1))$ with signed Fibonacci numbers (all three given points reproduce exactly).

== Closed-form reduction

For odd $n$, $t = s dot 2^alpha \/ 3^m$ with $alpha = F_(n-2) + F_n$, $m = F_(n-1)$, $s = (-1)^m$, and both coordinates reduce in closed form: $x = s(2^(2alpha - 2) + 3^(2m - 1)) \/ (2^(alpha - 2) 3^(m - 1))$ and $y = s(2^(2alpha + 2) - 3^(2m + 1)) \/ (2^alpha 3^m)$, already in lowest terms by residue inspection. Everything mod $p$ needs only the Fibonacci numbers mod $p - 1$ (Fermat) and mod $2$ (the sign). The modular path is validated against exact `Fraction` arithmetic for every odd $n$ up to $29$, including the given $n = 7$ answer $806236837$.

#pagebreak()
#link("https://projecteuler.net/problem=423")[= Problem 423: Consecutive Die Throws]

Solution: 653972374

Throw a die $n$ times and let $c$ count consecutive equal pairs; $C(n)$ counts the outcomes with $c <= pi(n)$ (the prime-counting function), and we want $S(5 dot 10^7) = sum_(n <= 5 dot 10^7) C(n)$ mod $10^9 + 7$.

== Counting outcomes by $c$

The first throw is free ($6$ ways); each of the remaining $n - 1$ transitions either repeats the previous value ($1$ way) or changes it ($5$ ways). Choosing which $c$ transitions repeat gives exactly $6 binom(n - 1, c) 5^(n - 1 - c)$ outcomes, so with $k = n - 1$ and $m = pi(n)$,
$
C(n) = 6 T_k (m), quad T_k (m) = sum_(c = 0)^(m) binom(k, c) 5^(k - c).
$
This reproduces all four given values $C(3) = 216$, $C(4) = 1290$, $C(11) = 361912500$, $C(24) = 4727547363281250000$.

== Sliding the tail sum

Summing $5 dot 10^7$ binomial tails naively is quadratic, but the tail slides in $O(1)$. Pascal's rule gives $T_(k+1)(m) = 5 T_k (m) + T_k (m - 1) = 6 T_k (m) - binom(k, m) 5^(k - m)$, used at every step; and whenever $n$ is prime, $pi$ ticks up and $T_k (m + 1) = T_k (m) + binom(k, m + 1) 5^(k - m - 1)$. The single tracked binomial coefficient and power of $5$ update with one multiplication each using precomputed modular inverses of $1, dots.h, L$, making the whole sum linear. The check $S(50) equiv 832833871$ matches the problem, and the incremental sum agrees with the exact big-integer formula for all $n <= 40$.

#pagebreak()
#link("https://projecteuler.net/problem=424")[= Problem 424: Kakuro]

Solution: 1059760019628

Two hundred cryptic kakuro puzzles ($5 times 5$ and $6 times 6$) have their clue sums encrypted by a per-puzzle bijection between the letters A–J and the digits $0$–$9$; each puzzle's answer is the ten-digit string of the letters' values in alphabetical order (a missing tenth letter takes the leftover digit), and we want the total.

== Letters first, grid second

The solver searches letter assignments depth-first, most-frequently-used letters first, with cheap but sharp pruning: a run of length $L$ sums to between $L(L+1)\/2$ and $L(19-L)\/2$, so a single-letter clue pins that letter to a narrow digit range, the tens letter of a two-letter clue must be $1$–$4$ (and nonzero), and letters that appear as prefilled cells cannot be $0$.

== Subset-table propagation

Each complete assignment fixes every clue value, and the grid is then solved by constraint propagation: for every run, the precomputed bitmasks of distinct digit subsets of the right size and sum are filtered against the current cell candidates, their union prunes each cell, and placed digits are removed from run-mates, iterated to a fixpoint with a tiny backtracking search on top. Infeasible letter assignments die in propagation almost immediately, so all $200$ puzzles solve in about six seconds. The example puzzle's answer $8426039571$ and the given first-ten total $64414157580$ both reproduce.

#pagebreak()
#link("https://projecteuler.net/problem=425")[= Problem 425: Prime Connection]

Solution: 46479497324

Two primes are _connected_ if they have the same number of digits and differ in exactly one position, or if one is obtained from the other by prepending a single digit. A prime $P$ is a _2's relative_ if there is a chain of connected primes from $2$ to $P$ in which no prime exceeds $P$, and $F(N)$ sums the primes $p <= N$ that are _not_ relatives.

The "no prime exceeds $P$" rule is the whole trick: a prime's relative-status depends only on smaller primes. So sieve to $N$, process the primes in increasing order, and maintain a union--find structure. When prime $p$ is reached, join it to every already-seen (hence smaller) prime it connects to: for the same-length case, vary each of its digits and check whether the resulting smaller number is prime; for the prepend case, strip $p$'s leading digit and, if the remaining tail is a prime with no leading zero, join the two. Looking only "downward" to smaller primes both enforces the chain constraint automatically and avoids handling each connection twice. After the joins, $p$ is a relative exactly when it shares a component with $2$; otherwise its value is added to the running total. This reproduces $F(10^3) = 431$ and $F(10^4) = 78728$.

#pagebreak()
#link("https://projecteuler.net/problem=426")[= Problem 426: Box-Ball System]

Solution: 31591886008

A box-ball configuration is given by alternating run lengths (occupied first); each turn moves every ball once, leftmost-unmoved ball to the nearest empty box on its right. The system eventually settles into _solitons_ — blocks of balls whose lengths never change again, ordered ascending. From the run lengths $(t_0, dots.h, t_(10^7))$ of the given pseudo-random sequence, we want the sum of squares of the final state.

== Conserved quantities instead of simulation

Simulating $approx 1.6 dot 10^8$ balls to separation is hopeless, but the soliton content is conserved from the start. By the classical Takahashi–Satsuma invariants, the number of solitons of size $>= k$ equals $E_k$, the number of "ball, empty" boundaries after $k - 1$ rounds of *10-elimination*: simultaneously delete one ball and one empty box at every such boundary. The answer telescopes without ever storing the multiset:
$
sum_("solitons" s) s^2 = sum_(k >= 1) (E_k - E_(k+1)) k^2 = sum_(k >= 1) E_k (2k - 1).
$

== Elimination on run lengths

On the run-length encoding, a node is a ball run followed by an empty run (the right-infinite emptiness is a huge sentinel). One round decrements both runs of every node by one and compacts: a vanished empty run merges adjacent ball runs, a vanished ball run folds its empty run into the previous one, and leading empties fall off. A round costs $O("nodes")$ and $E_k$ is the node count, so the total work is $sum_k E_k$ — exactly the number of balls. The whole computation runs in a couple of seconds.

Both given examples reproduce — $(2, 2, 2, 1, 2) arrow.r [1, 2, 3]$ and $(t_0, dots.h, t_10) arrow.r [1, 3, 10, 24, 51, 75]$ — and the elimination multiset matches a direct turn-by-turn simulation on 31 terms. The simulation itself held a lesson: free solitons keep their run lengths *between* collisions, so "unchanged for one turn" is not final; the state is final once the run sequence is also non-decreasing, since the faster (larger) solitons are then in front for good.

#pagebreak()
#link("https://projecteuler.net/problem=427")[= Problem 427: n-sequences]

Solution: 97138867

An $n$-sequence has $n$ elements from ${1, dots.h, n}$; $L(S)$ is its longest run of equal consecutive values, and $f(n) = sum L(S)$ over all $n^n$ sequences. We want $f(7500000) mod 10^9 + 9$.

== Layer-cake over run thresholds

$f(n) = sum_(k=1)^(n) \#{L >= k} = n dot n^n - sum_(m=1)^(n-1) N_m$, where $N_m$ counts sequences with every run of length at most $m$. Decomposing a sequence into $j$ maximal runs gives $n(n-1)^(j-1)$ colour choices times the compositions of $n$ into $j$ parts of size at most $m$, so per length the generating function is rational:
$
N_m = n dot [x^n] (x - x^(m+1)) / (1 - n x + (n - 1) x^(m+1)).
$
Expanding the denominator's geometric series,
$
[x^t] = sum_(i >= 0) (-1)^i (n - 1)^i binom(t - i m, i) thin n^(t - i(m+1)),
$
about $t \/ (m + 1)$ terms per coefficient — so summing $N_m$ over all $m$ costs $O(n log n) approx 2.4 dot 10^8$ constant-time terms with precomputed factorial, inverse-factorial, and power tables ($n^e$ and $(n-1)^i$ as full arrays). A hand check at $n = 2$ gives $f(2) = 2 dot 2^2 - N_1 = 8 - 2 = 6$, matching direct enumeration; the code brute-forces $n = 3, 5$ and reproduces the given $f(3) = 45$, $f(7) = 1403689$ and $f(11) = 481496895121$.

#pagebreak()
#link("https://projecteuler.net/problem=428")[= Problem 428: Necklace of Circles]

Solution: 747215561862

With $W, X, Y, Z$ collinear at gaps $a, b, c$, circles $C_("in")$ (diameter $b$) and $C_("out")$ (diameter $a + b + c$), the triplet is a *necklace* if $k >= 3$ pairwise non-overlapping circles can ring between them, each tangent to both and to its neighbours. Count integer triplets with $b <= 10^9$.

== Steiner's porism and Niven's theorem

Such a ring is a Steiner chain, and by Steiner's porism its existence depends only on the inversive distance of the two circles, $I = ((2a + b)(2c + b) + b^2) \/ (2b(a + b + c))$; a single-wrap $k$-chain needs $I = (1 + sin^2(pi \/ k)) \/ (1 - sin^2(pi \/ k))$. But $I$ is rational, and by Niven's theorem $sin^2(pi \/ k)$ is rational only for $k in {3, 4, 6}$, so $I in {7, 3, 5\/3}$ — the given examples $(5,5,5) -> 5\/3$, $(4,3,21) -> 3$ and the non-example $(2,2,5) -> 19\/9$ all check.

== Three Diophantine families

Clearing denominators, each $I$ value factors: $k = 4$ gives $(a - b)(c - b) = 2b^2$, $k = 3$ gives $(a - 3b)(c - 3b) = 12b^2$, and $k = 6$ gives $(3a - b)(3c - b) = 4b^2$ with both factors $equiv -b (mod 3)$; size comparisons kill the negative branches, so the counts are $tau(2b^2)$, $tau(12b^2)$, and a character-corrected divisor count $(tau(4b^2) - chi(b) F(4b^2)) \/ 2$ (or $(2gamma - 1) tau$ of the non-$3$ part when $3^gamma || b$), where $F$ collapses to the divisor count of the $(p equiv 1)$-part of $b^2$. All three are determined by $b$'s prime exponents, so a segmented sieve factoring every $b <= 10^9$ accumulates the total in about ninety seconds. $T(1) = 9$ and $T(20) = 732$ are confirmed against an independent solve-for-$c$ brute force, and $T(3000) = 438106$ matches the given.

#pagebreak()
#link("https://projecteuler.net/problem=429")[= Problem 429: Sum of Squares of Unitary Divisors]

Solution: 98792821

A unitary divisor $d$ of $n$ satisfies $gcd(d, n\/d) = 1$, so it takes either all or none of each prime power in $n$. The sum of squares of unitary divisors $S$ is therefore multiplicative with $S(p^a) = 1 + p^(2a)$ (the $1$ from $d = 1$, the $p^(2a)$ from $d = p^a$). We need $S(10^8 !) mod (10^9 + 9)$.

For $N!$ the exponent of a prime $p$ is given by Legendre's formula $e_p = sum_(i >= 1) floor(N\/p^i)$, so
$
S(N !) = product_(p <= N) (1 + p^(2 e_p)).
$
Sieve the primes up to $10^8$; for each, accumulate $e_p$ by the floor-sum, compute $p^(2 e_p) mod (10^9 + 9)$ by fast exponentiation, and fold $(1 + p^(2 e_p))$ into the running product. The check $S(4!) = (1 + 2^6)(1 + 3^2) = 650$ confirms the formula.

#pagebreak()
#link("https://projecteuler.net/problem=430")[= Problem 430: Range Flips]

Solution: 5000624921.38

$N$ two-sided disks start white; each of $M$ turns picks $A, B$ uniformly in $[1, N]$ and flips every disk between them. $E(N, M)$ is the expected number of white disks afterwards; we want $E(10^10, 4000)$ to two decimals.

== Per-disk analysis

Disk $i$ escapes a flip exactly when both endpoints land strictly on the same side of it, so it is flipped with probability $q_i = 1 - ((i - 1)^2 + (N - i)^2) \/ N^2$. Turns are independent, and a disk is white iff its flip count is even; the standard parity identity gives $P("white") = (1 + r_i^M) \/ 2$ with $r_i = 1 - 2 q_i$, hence
$
E(N, M) = N / 2 + 1 / 2 sum_(i = 1)^(N) r_i^M.
$
This reproduces $E(3, 1) = 10\/9$, $E(3, 2) = 5\/3$, $E(10, 4) approx 5.157$ and $E(100, 10) approx 51.893$ exactly from the problem.

== Truncating the sum

Summing $10^10$ terms is unnecessary: $r_i$ falls monotonically from $approx 1 - 4 i \/ N$ at the edges to about $0$ in the middle (symmetric in $i arrow.l.r N + 1 - i$), so $r_i^M approx e^(- 4 M i \/ N)$ dies after roughly $N \/ (4 M) dot ln(1\/epsilon)$ indices. Cutting off once $r^M < 10^(-18)$ keeps about $2.6 dot 10^7$ terms per end (counted once and used for both by symmetry) with total truncation error below $10^(-7)$ — far inside the two-decimal target. The truncated evaluator matches the full sum at $N = 10^6$ to $10^(-6)$.

#pagebreak()
#link("https://projecteuler.net/problem=431")[= Problem 431: Square Space Silo]

Solution: 23.386029052

Grain dropped at horizontal distance $x$ from the centre of a cylindrical silo (radius $6$, angle of repose $alpha = 40 degree$) forms a cone of repose with apex at the drop point $P$; the wasted space $V(x)$ is the volume between the silo top and the grain surface. We want $sum x$ over all $x$ for which $V(x)$ is a perfect square, to $9$ decimals.

== A one-dimensional integral

The surface lies $tan(alpha) dot |q - P|$ below the top at each point $q$ of the disk, so $V(x) = tan(alpha) integral.double |q - P| dif A$. Switching to polar coordinates centred at $P$, the radial integral of $s dot s$ is immediate and
$
V(x) = tan(alpha) / 3 integral_0^(2 pi) L(theta)^3 dif theta, quad L(theta) = -x cos theta + sqrt(R^2 - x^2 sin^2 theta),
$
$L$ being the distance from $P$ to the wall in direction $theta$. The integrand is smooth and periodic, so the midpoint rule converges spectrally — $2^14$ samples are far past machine precision. The model is validated by all three given numbers for the $alpha = 30 degree$, $R = 3$ silo: $V(0) = 32.648388556$, and solving $V(x) = 36$ and $49$ returns $1.114785284$ and $2.511167869$.

== Picking out the squares

$V$ increases monotonically in $x$ (the mean distance to the disk grows as the apex moves off-centre), from $V(0) approx 379.6$ to $V(R) approx 644.4$. The perfect squares in range are $20^2, dots.h, 25^2$, each giving one $x$ by bisection; their sum rounds to $23.386029052$.

#pagebreak()
#link("https://projecteuler.net/problem=432")[= Problem 432: Totient Sum]

Solution: 754862080

Here $S(n, m) = sum_(i=1)^m phi(n i)$ with $n = 510510 = 2 dot 3 dot 5 dot 7 dot 11 dot 13 dot 17$, and we want the last nine digits of $S(510510, 10^11)$. Writing $T(n, m) = sum_(i=1)^m phi(n i)$, peel off the smallest prime factor $p$ of the (squarefree) $n$. Since $phi(p k) = (p-1) phi(k)$ when $p divides.not k$ and $p phi(k)$ when $p | k$,
$
T(n, m) = (p - 1) T(n\/p, m) + T(n, floor(m\/p)).
$
The first term handles the $i$ not divisible by $p$; the second collects the $i = p j$ (where $phi(n i) = phi(n j) dot p\/(p-1) dot (p-1)$ telescopes back into $T(n, floor(m\/p))$). Peeling primes one at a time always removes the smallest, so only the eight "suffix" products of the seven primes ever appear, and the recursion bottoms out at $T(1, m) = Phi(m) = sum_(i <= m) phi(i)$.

The summatory totient $Phi$ is evaluated over the _quotient lattice_ of $m$: sieve $phi$ and its prefix sums up to $L approx m^(2\/3)$, and for each large value $v = floor(m\/i)$ use
$
Phi(v) = v(v+1)\/2 - sum_(d >= 2) Phi(floor(v\/d)),
$
with divisor-block grouping so each call is $O(sqrt(v))$ and every $floor(v\/d)$ is again a lattice point (either sieved or a previously computed larger index). Memoizing $T$ on $("prime index", m')$ and reducing mod $10^9$ throughout (taking the even factor of $v(v+1)$ before halving, since $10^9$ has no inverse of $2$) gives the answer in a few seconds. It reproduces the given $S(510510, 10^6) = 45480596821125120$.

#pagebreak()
#link("https://projecteuler.net/problem=433")[= Problem 433: Steps in Euclid's Algorithm]

Solution: 326624372659664

$E(x, y)$ counts the steps of Euclid's algorithm — $(x, y) arrow.r (y, x mod y)$ until the second entry is $0$ — and $S(N) = sum_(1 <= x, y <= N) E(x, y)$. We want $S(5 dot 10^6)$, about $2.5 dot 10^13$ pairs averaging $13$ steps each, so anything per-pair is hopeless.

== From depths to descendant counts

Steps are gcd-invariant, so everything reduces to coprime pairs; for $y > x$ the chain of $(y, x)$ climbs the *reverse Euclid tree* rooted at the terminal $(1, 0)$, where the children of $(b, c)$ are its predecessors $(c + k b, b)$. Then $E(y, x)$ is the depth of $(y, x)$, and a depth sum is a descendant count: $sum E = sum_("nodes" (b, c)) \#{"descendants with first coordinate" <= N}$.

A descendant reached by quotients $(k_1, dots.h, k_j)$ has first coordinate $u b + v c$ where $(u, v)$ is the leading continuant pair — and crucially each coprime $u > v >= 1$ arises from exactly *two* quotient sequences (the two continued-fraction representations), while $(1, 0)$ and $(1, 1)$ arise once. (Missing this multiplicity was the first prototype's failure.) Summing over nodes turns $S$ into counts of quadruples $u b + v c <= N$ with both pairs coprime and ordered.

== Collapsing the Möbius layers

Möbius inversion removes both coprimalities, and composing with the outer gcd-scaling sum gives $1 * mu * mu = mu$ — a single Möbius layer:
$
S(N) = 2 N^2 - N - floor(N \/ 2) + 4 sum_(m) mu(m) thin W(floor(N \/ m)),
$
where $W(M) = \#{u > v >= 1, b > c >= 1 : u b + v c <= M}$ has *no* arithmetic conditions left. The swap $(u, v, b, c) arrow.r (v, u, c, b)$ pairs the order regions, so $W$ follows by inclusion–exclusion from $W_0 = sum_(x + y <= M) d(x) d(y)$ (a divisor-sieve convolution), the cheap diagonal counts, and the mixed count $X = \#{u > v, c > b}$. Substituting $u = v + p$, $c = b + q$ turns $X$ into lattice points under a line for every $(v, b)$ with $2 v b$ small — each an $O(log)$ Euclidean `floor_sum`, with $(v, b)$ symmetry halving the work. Evaluating $W$ at the $O(sqrt(N))$ distinct quotients against Mertens prefix sums finishes in seconds.

Every identity was validated against brute force at small sizes before assembly — which caught both the continuant multiplicity and an off-by-one in the $X$ loop bound — and the final routine reproduces all three given values $S(1) = 1$, $S(10) = 221$, $S(100) = 39826$, plus a direct $4 dot 10^6$-pair brute force at $N = 2000$.

#pagebreak()
#link("https://projecteuler.net/problem=434")[= Problem 434: Rigid Graphs]

Solution: 863253606

$R(m, n)$ counts the ways to add diagonal braces to the cells of an $m times n$ grid graph (one optional brace per cell, orientation irrelevant) so that the embedding is rigid; $S(N) = sum_(i, j <= N) R(i, j)$, and we want $S(100) mod 1000000033$.

== Rigidity is bipartite connectivity

By the classical Bolker–Crapo theorem, a braced grid is rigid exactly when its _brace graph_ — one vertex per row, one per column, and an edge for every braced cell — is connected. Since each of the $m n$ cells is braced independently, $R(m, n)$ is the number of connected spanning subgraphs of $K_(m, n)$.

== Counting connected spanning subgraphs

Extract the connected component of a fixed row vertex: if it contains $i$ rows and $j$ columns, the remaining $(m - i)(n - j)$ potential edges are unconstrained, so
$
2^(m n) = sum_(i, j) C(i, j) binom(m - 1, i - 1) binom(n, j) thin 2^((m - i)(n - j)),
$
which solves for $C(m, n) = R(m, n)$ row by row ($C(1, 0) = 1$ is the isolated vertex; $C(i, 0) = 0$ for $i >= 2$). Over the whole $100 times 100$ table the four nested indices cost only $(Sigma m)(Sigma n) approx 2.6 dot 10^7$ operations, with binomials from a Pascal triangle mod the (conveniently irrelevant whether prime) modulus.

Checks: a union–find brute force over all $2^(m n)$ edge subsets confirms $R(2, 3) = 19$ from the problem, $R(1, 1) = 1$, and the full $S(3)$; the given $S(5) = 25021721$ also reproduces.

#pagebreak()
#link("https://projecteuler.net/problem=435")[= Problem 435: Polynomials of Fibonacci Numbers]

Solution: 252541322550

The polynomial $F_n (x) = sum_(i=0)^n f_i x^i$ uses the Fibonacci numbers as coefficients, and we want $sum_(x=0)^100 F_n (x)$ for $n = 10^15$, modulo $15!$. Because the Fibonacci generating function is $sum_(i >= 0) f_i x^i = x \/ (1 - x - x^2)$, multiplying the partial sum by $1 - x - x^2$ telescopes (every interior coefficient $f_k - f_(k-1) - f_(k-2)$ vanishes), leaving only boundary terms:
$
F_n (x) = (f_(n+1) x^(n+1) + f_n x^(n+2) - x) / (x^2 + x - 1).
$
The denominator $D = x^2 + x - 1$ is nonzero for every integer $x$, but it need not be invertible modulo the composite $15!$. The fix exploits that $F_n (x)$ is a genuine integer, so the numerator equals $D dot F_n (x)$ exactly: computing it modulo $m D$ yields $D dot (F_n (x) space (mod m))$, and an ordinary integer division by $D$ recovers $F_n (x) space (mod m)$. Each Fibonacci pair $f_n, f_(n+1)$ comes from fast doubling and each power from fast exponentiation, all mod $m D$. The closed form reproduces $F_7(11) = 268357683$.

#pagebreak()
#link("https://projecteuler.net/problem=436")[= Problem 436: Unfair Wagers]

Solution: 0.5276662759

Louise adds uniform draws until the total exceeds $1$, recording her last draw $x$; Julie continues until the total exceeds $2$, recording her last draw $y$. Find $P(y > x)$.

== Renewal structure

The density that a partial sum of independent $U(0,1)$ draws sits at level $s < 1$ before crossing is the renewal density $e^s$, plus a unit atom at $s = 0$ (no draws yet). Player 1 therefore crosses level $1$ with last draw $x$ and overshoot $t = S - 1$ having joint density $e^(1 + t - x)$ on $0 < t < x < 1$ (the pre-crossing sum was $1 + t - x$, necessarily positive, so the atom never contributes — a single draw cannot exceed $1$).

Player 2 then faces a fresh crossing of the gap $c = 1 - t in (0, 1)$. Given $c$, her last draw $y$ has density $bb(1)_(y > c) + e^c - e^(max(0, c - y))$: the indicator is the atom (her first draw already clears the gap, possible now that $c < 1$), and the exponential terms integrate the renewal density over pre-sums $u > c - y$.

== Exact integration

$P(y > x)$ is a double integral of elementary exponentials over the triangle $0 < t < x < 1$, split by the relative position of $x$ and $c = 1 - t$. Sympy evaluates it in closed form; the result, $approx 0.5276662759$, is confirmed against a $4 dot 10^5$-trial Monte Carlo simulation of the literal game before printing. Louise is right to object: the second player wins more often than not.

#pagebreak()
#link("https://projecteuler.net/problem=437")[= Problem 437: Fibonacci Primitive Roots]

Solution: 74204709657207

A Fibonacci primitive root $g$ of $p$ satisfies $g^(n+2) equiv g^(n+1) + g^n$, i.e. $g^2 equiv g + 1$, while also being a primitive root. So $g$ must be a root of $x^2 - x - 1$ in $FF_p$, which requires $5$ to be a quadratic residue: either $p = 5$ or $p equiv plus.minus 1 space (mod 5)$. For such $p$ the two roots are $(1 plus.minus sqrt(5)) \/ 2$, and $p$ qualifies exactly when at least one of them is a primitive root.

There is no simple congruence test for this (the density is of Artin type), so each candidate prime is checked directly: take $sqrt(5)$ via Tonelli--Shanks (a single power when $p equiv 3 space (mod 4)$), form the two roots, factor $p - 1$ by trial division against the primes up to $10^4$ (the leftover cofactor, if any, is prime since $p - 1 < 10^8$), and test primitivity through $g^((p-1)\/q) != 1$ for every prime $q | p-1$. Sieving the primes below $10^8$ and running this in compiled code reproduces the stated $323$ primes below $10^4$ summing to $1480491$, and finishes the full range in a few seconds.

#pagebreak()
#link("https://projecteuler.net/problem=438")[= Problem 438: Integer Part of Polynomial Equation's Solutions]

Solution: 2046409616809

Count monic integer polynomials $x^7 + a_1 x^6 + dots.h + a_7$ whose seven roots are all real with sorted floors exactly $1, dots.h, 7$ (root $i$ in $[i, i + 1)$), and sum $S(t) = sum |a_i|$ over them.

== Values, not coefficients

The root boxes force the sign pattern $b_k := (-1)^(8 - k) f(k) >= 0$ at $k = 1, dots.h, 7$ and $f(8) >= 1$, and the seventh finite difference of a monic septic pins the weighted sum $sum_(k = 1)^8 binom(7, k - 1) b_k = 5040$. Each $b_k$ is further capped by $product_i sup |k - r|$ over the boxes, every pair by the joint per-box suprema $b_k b_l <= product_i sup |k - r| |l - r|$, midpoint evaluations obey $|f(k + 1/2)| <= product_i sup|dot|$, and exterior points give *two-sided* windows such as $f(0) in [-40319, -5040]$ — all linear in the value vector, all prunable by interval arithmetic at every search level.

== Integrality is a finite-difference statement

The decisive filter: $f$ has integer coefficients *iff* $j! divides Delta^j f(1)$ for every $j$ (Newton's basis $f = sum_j (Delta^j f(1) \/ j!) (x - 1)^((j))$). Pairwise congruences $f(k) equiv f(l) mod (k - l)$ are strictly weaker — $12 binom(x - 1, 4)$ passes all of them with non-integer coefficients. Better still, when a search level extends a contiguous run of chosen points at an endpoint, the $Delta^j$ condition pins the new value modulo $j!$ with unit coefficient, so the DFS *steps* by $2, 6, 24, 120$ at successive levels and the final value modulo $720$, instead of enumerating and rejecting. The last two values $(b_1, b_8)$ resolve analytically: their sum is the budget remainder (forcing $R equiv 0 mod 7$ for free), and the constraint rows become linear in $b_1$, intersecting to a few candidates per leaf.

== Exact validity in integer arithmetic

Survivors number in the tens of millions, so per-candidate symbolic root finding is impossible — and unnecessary. With every $b_k >= 1$ the strict sign alternation at eight consecutive integers already certifies seven real roots, one strictly inside each interval. When some $f(k) = 0$, the root at $k$ is divided out synthetically (exact integers); the quotient must be nonzero at every integer (a repeated integer root has no box to live in) and its signs must flip exactly across the intervals still owed a root. Both validity and $S(t)$ (via Newton-difference coefficients) run inside the search in $O(n^2)$ integer operations per leaf.

The full pipeline reproduces the given $n = 4$ data ($12$ tuples, $sum S = 2087$), matches an independent sympy-validated brute force over Vieta coefficient boxes at $n = 3$, and at $n = 7$ finds exactly $24883200$ tuples — precisely the Vandermonde volume $product_(i < j) (j - i)$, which also equals $12$ at $n = 4$ — in about $40$ seconds.

#pagebreak()
#link("https://projecteuler.net/problem=439")[= Problem 439: Sum of Sums of Divisors]

Solution: 968697378

$S(N) = sum_(i, j <= N) sigma(i j)$ with $sigma$ the divisor sum; we want $S(10^11) mod 10^9$.

== Decoupling the product

$sigma$ is multiplicative but $sigma(i j)$ couples $i$ and $j$ through their common factors; the exact correction is
$
sigma(i j) = sum_(d | gcd(i, j)) mu(d) thin d thin sigma(i \/ d) thin sigma(j \/ d),
$
verified directly over a grid of pairs before anything else. Summing over $i, j$ then separates completely:
$
S(N) = sum_(d <= N) mu(d) thin d thin T(floor(N \/ d))^2, quad T(M) = sum_(m <= M) sigma(m) = sum_k k floor(M \/ k).
$

== Everything on the quotients

Both ingredients live on the $O(sqrt(N))$ distinct quotients of $N$: $T$ by hyperbola blocks in $O(sqrt(M))$ per value, and the weighted Mertens prefix $M_1(y) = sum_(d <= y) mu(d) d$ by the sublinear recurrence $sum_k k thin M_1(floor(y \/ k)) = 1$ over a $3 dot 10^7$ sieved base — the same machinery built for Problem 415. The modulus $10^9 = 2^9 5^9$ is composite, but only divisions by $2$ ever arise (triangular range sums), each cancelled exactly before reduction. The whole computation runs in about twenty seconds.

Checks: the identity itself, brute force at $N = 3$ (the given $59$) and $N = 50$, plus both given values $S(10^3) = 563576517282$ and $S(10^5) equiv 215766508$, the latter two exercising the full sublinear pipeline.

#pagebreak()
#link("https://projecteuler.net/problem=440")[= Problem 440: GCD and Tiling]

Solution: 970746056

$T(n)$ counts tilings of a $1 times n$ board by dominoes and unit squares bearing one of ten digits, and $S(L) = sum_(a, b, c <= L) gcd(T(c^a), T(c^b))$; we want $S(2000) mod 987898789$.

== A strong divisibility sequence in disguise

The tiling recurrence is $T(n) = 10 T(n-1) + T(n-2)$, so $T(n) = U_(n+1)$ for the Lucas sequence $U(P = 10, Q = -1)$ — and Lucas $U$ with coprime parameters satisfies $gcd(U_m, U_n) = U_(gcd(m, n))$. Hence $gcd(T(c^a), T(c^b)) = U_(gcd(c^a + 1, c^b + 1))$, and the inner gcd is classical: with $g = gcd(a, b)$ it equals $c^g + 1$ when both $a\/g$ and $b\/g$ are odd, and otherwise $2$ (odd $c$) or $1$ (even $c$) — verified numerically over a grid before use.

== Counting pairs, chaining powers

The pair counts $f(g) = hash{(a, b): gcd = g, "both quotients odd"}$ come from a Möbius sum over odd $d$ of squared odd-counts. For the values, each $c$ needs $U_(c^g + 1)$ for every $g <= 2000$: the pair $(U_k, U_(k+1))$ supports an index-multiplication law, so $Q^(c^g) = (Q^(c^(g-1)))^c$ walks the whole chain in $O(L log c)$ pair-multiplications per $c$ — a few hundred million modular multiplications overall, seconds in numba. The exact givens $S(2) = 10444$ and the $28$-digit $S(3)$ are reproduced through a big-integer twin of the modular routine, $S(4) mod 987898789$ through both paths, all against a direct brute force over actual tilings' gcds.

#pagebreak()
#link("https://projecteuler.net/problem=441")[= Problem 441: The Inverse Summation of Coprime Couples]

Solution: 5000088.8395

$R(M)$ sums $1\/(p q)$ over coprime $1 <= p < q <= M$ with $p + q >= M$, and $S(N) = sum_(M = 2)^N R(M)$; find $S(10^7)$ to four decimals.

== Count the multiplicity of each pair

A coprime pair $(p, q)$ belongs to $R(M)$ exactly for $M in [q, min(p + q, N)]$, so swapping the summation order,
$
S(N) = sum_(p + q <= N) (p + 1) / (p q) + sum_(q <= N < p + q) (N + 1 - q) / (p q).
$
The $(p + 1)\/(p q)$ piece splits into $sum 1\/q$ and $sum 1\/(p q)$. The first is $sum phi(q) \/ q$ for $q <= N\/2$ plus a Möbius-counted partial for larger $q$. For the second, grouping by $s = p + q$ and using $1\/(p q) = (1\/s)(1\/p + 1\/q)$ collapses each $s$ to $(1\/s) sum_(p < s, (p, s) = 1) 1\/p$ — a coprime harmonic sum evaluated by Möbius over the squarefree divisors of $s$ against a precomputed harmonic table, as is the boundary piece over a $p$-range.

== Four decimals over ten million terms

The answer is near $5 dot 10^6$ accumulated from $10^7$ terms, where naive float64 summation would already lose the fourth decimal, so both the harmonic table and the master loop use Kahan compensation. Exhaustive triple-loop brute force matches to $10^(-9)$ at $N = 10, 100, 300$, and the given $S(10)$, $S(100)$ round correctly. The full computation takes under four seconds.

#pagebreak()
#link("https://projecteuler.net/problem=442")[= Problem 442: Eleven-free Integers]

Solution: 1295552661530920149

An integer is _eleven-free_ if its decimal expansion contains no power of $11$ (other than $1$) as a substring — so $911$ fails on $11$ and $4121331$ fails on $1331$. We want $E(10^18)$, the $10^18$th eleven-free positive integer.

== Counting below a bound

The forbidden patterns are the digit strings of $11, 121, 1331, dots.h$ up to $20$ digits — only nineteen short strings, so build an Aho–Corasick automaton over them (a digit trie with failure links folded into a total transition function, accepting states marked for any node whose suffix is a full pattern). A digit DP then counts the integers in $[1, x]$ that never touch an accepting state: walk the digits of $x$ keeping (i) a vector of counts per automaton state for prefixes already strictly below $x$, and (ii) the single tight state following $x$ itself, which dies if it ever hits an accepting state. No pattern starts with $0$, so leading zeros idle at the root and the padded representations of all $n <= x$ are handled uniformly (subtract one for $n = 0$). The automaton has about $200$ states, so one count is microseconds.

== Inverting

$E(n)$ is the smallest $x$ whose count reaches $n$, found by binary search (well over half of all integers are eleven-free, so $2n$ bounds the search). The given values $E(3) = 3$, $E(200) = 213$ and $E(500000) = 531563$ all reproduce, and the DP count matches a direct substring scan up to $54321$.

#pagebreak()
#link("https://projecteuler.net/problem=443")[= Problem 443: GCD Sequence]

Solution: 2744233049300770

The sequence is $g(4) = 13$ and $g(n) = g(n-1) + gcd(n, g(n-1))$, and we want $g(10^15)$. Stepping one term at a time is hopeless, but the increments are extremely structured. Consider a stretch where the gcd happens to be $1$: then $g(j) = g(j-1) + 1$, so the difference $c = g(j-1) - j$ is _constant_ throughout the stretch. While $c$ holds steady,
$
gcd(j, g(j-1)) = gcd(j, j + c) = gcd(j, c),
$
so the run of $1$'s continues until $j$ first shares a factor with $c$. The earliest such index past the current $n$ is
$
j^* = min_(p | c) p dot (floor(n\/p) + 1),
$
taken over the distinct prime factors $p$ of $c$. At $j^*$ the increment jumps to $d = gcd(j^*, c)$, after which a fresh constant $c$ takes over. So the whole sequence can be fast-forwarded jump to jump: from state $(n, v = g(n))$ set $c = v - n - 1$, find $j^*$, and update $v <- v + (j^* - 1 - n) + d$, $n <- j^*$ (stopping early with $v + (T - n)$ once $j^*$ would overshoot the target $T$).

The number of jumps grows glacially -- about $116$ by $10^6$ and only $\~340$ by $10^15$ -- so the cost is dominated by factoring each $c$ (up to $\~10^15$). Trial division to $sqrt(c)$ is too slow there, so Pollard's rho with a Miller--Rabin primality check supplies the distinct prime factors in roughly $c^(1\/4)$ steps each. The fast-forward reproduces $g(1000) = 2524$ and $g(10^6) = 2624152$.

#pagebreak()
#link("https://projecteuler.net/problem=444")[= Problem 444: The Roundtable Lottery]

Solution: 1.200856722e263

$p$ players hold a random permutation of tickets worth £$1, dots.h,$ £$p$; in turn each either scratches their ticket or trades it for a previously scratched one and leaves. $E(p)$ is the expected number of players remaining under optimal play, $S_1(N) = sum_(p <= N) E(p)$, and $S_k$ iterates the prefix sum; we want $S_20 (10^14)$ to ten significant digits.

== $E(p)$ is the harmonic number

Working the game out by hand: $E(1) = 1$ (forced scratch), and for $p = 2$ the second player trades exactly when the revealed ticket beats the expectation of the unseen one, giving $E(2) = 3\/2$. Both match $H_p$, and the given $E(111) = 5.2912$ agrees with $H_111 = 5.29123 dots.h$ to every shown digit — so $E(p) = H_p$.

== Iterated sums in closed form

The generating function of $H_p$ is $-ln(1 - x) \/ (1 - x)$, and each prefix-sum layer multiplies by $1 \/ (1 - x)$, so $S_k (N)$ is the coefficient of $x^N$ in $-ln(1 - x) \/ (1 - x)^(k + 1)$ — classically
$
S_k (N) = binom(N + k, k) (H_(N + k) - H_k).
$
The problem's own ten-digit example $S_3 (100) = 5.983679014 dot 10^5$ reproduces exactly, validating the identity, the harmonic claim and the formatting in one shot. For the answer, the binomial is exact big-integer arithmetic and $H_(10^14 + 20)$ comes from the asymptotic expansion $ln n + gamma + 1\/(2n) - 1\/(12 n^2) + dots.h$ in $60$-digit decimals (checked against the exact sum at $n = 10^6$ to $10^(-30)$).

#pagebreak()
#link("https://projecteuler.net/problem=445")[= Problem 445: Retractions A]

Solution: 659104042

A _retraction_ mod $n$ is a map $f(x) = a x + b$ ($0 < a < n$, $0 <= b < n$) with $f compose f = f$; $R(n)$ counts them. We want $sum_(k=1)^(10^7 - 1) R(binom(10^7, k))$ mod $10^9 + 7$.

== A closed form for $R(n)$

$f(f(x)) equiv f(x)$ for all $x$ forces $a^2 equiv a$ and $a b equiv 0 space (mod n)$. Modulo each prime power an idempotent is $0$ or $1$, so the idempotents correspond to unitary divisor splits, and for a given $a$ the valid $b$ number $gcd(a, n)$. Summing $gcd(a, n)$ over all $2^omega(n)$ idempotents gives exactly $sigma^*(n)$, the sum of unitary divisors; removing the disallowed $a = 0$ (which contributes $gcd(0, n) = n$) leaves
$
R(n) = sigma^*(n) - n.
$
(Verified by direct enumeration of all $(a, b)$ pairs in the Problem 447 solution.)

== Sliding along the binomial row

$binom(n, k+1) = binom(n, k) (n - k) \/ (k + 1)$, so consecutive binomials differ only in the primes of $n - k$ and $k + 1$. Keep three things: the exponent of every prime in the current $binom(n, k)$, its value $V$ mod $p$, and $S = sigma^* = product (q^e + 1)$ mod $p$. Factoring the two integers with a smallest-prime-factor sieve, each changed prime updates $S$ with one Fermat inverse of its old factor and one new factor, and updates $V$ by a power of $q$. Each row step costs $O(log)$ prime updates, so the whole row is quasilinear. The answer accumulates $S - V$ at every $k$. The given $N = 10^5$ value ($628701600$) reproduces, as do brute-force sums at $N = 20$ and $35$.

#pagebreak()
#link("https://projecteuler.net/problem=446")[= Problem 446: Retractions B]

Solution: 907803852

With $R(n) = sigma^*(n) - n$ as in Problem 445, we want $F(10^7) = sum_(n=1)^(10^7) R(n^4 + 4)$ mod $10^9 + 7$.

== Sophie Germain splits the quartic

$n^4 + 4 = A B$ with $A = (n - 1)^2 + 1$ and $B = (n + 1)^2 + 1$. An odd prime dividing both would divide $B - A = 4n$, hence $n$, hence $A equiv 2$ — impossible. So the odd parts of $A$ and $B$ are coprime and $sigma^*$ splits across them; the power of $2$ is handled separately ($m^2 + 1 equiv 2 space (mod 4)$ for odd $m$, so $e_2(n^4 + 4)$ is $2$ for even $n$, contributing a factor $5$, and $0$ for odd $n$).

== One sieve over $m^2 + 1$

Everything reduces to the odd factorisations of $m^2 + 1$ for $m <= 10^7 + 1$. A prime $p equiv 1 space (mod 4)$ divides $m^2 + 1$ exactly when $m equiv plus.minus sqrt(-1) space (mod p)$, with the root from one exponentiation $z^((p-1)\/4)$ of a non-residue $z$. Sweep those two progressions for every such prime, dividing the stored value $m^2 + 1$ and folding $(p^e + 1)$ into a product array $g[m]$; whatever survives the sieve is a single prime above $10^7$ (two such factors would overshoot $m^2 + 1$) and contributes its own $(p + 1)$. Then $sigma^*(n^4 + 4) = g[n - 1] dot g[n + 1]$ (times $5$ for even $n$). The exact check $F(1024) = 77532377300600$ reproduces both for the sieve and for an independent trial-division brute force.

#pagebreak()
#link("https://projecteuler.net/problem=447")[= Problem 447: Retractions C]

Solution: 530553372

With $R(n) = sigma^*(n) - n$ (derived in Problem 445 and verified here against direct enumeration of the maps for all $n <= 60$), we want $F(10^14) = sum_(n=2)^(10^14) R(n)$ mod $10^9 + 7$, i.e. the summatory unitary divisor sum minus the triangular number $N(N + 1)\/2$.

Unitary divisors unfold as pairs: $sum_(n <= N) sigma^*(n) = sum_(d k <= N, gcd(d, k) = 1) d$. Möbius inversion over $g = gcd(d, k)$ removes the coprimality:
$
sum_(n <= N) sigma^*(n) = sum_(g <= sqrt(N)) mu(g) thin g thin D(floor(N \/ g^2)), quad D(M) = sum_(d k <= M) d = sum_(k <= M) T(floor(M \/ k)),
$
with $T$ the triangular numbers (the even factor halved exactly before reducing, as the modulus is fine here but the inputs reach $10^14$). Each $D$ evaluates in $O(sqrt(M))$ quotient blocks, and the outer sum costs $sum_g sqrt(N) \/ g approx sqrt(N) ln sqrt(N)$ — a few times $10^8$ operations. The given $F(10^7) equiv 638042271$ reproduces.

#pagebreak()
#link("https://projecteuler.net/problem=448")[= Problem 448: Average Least Common Multiple]

Solution: 106467648

Since $"lcm"(n, i) = n i \/ gcd(n, i)$, the average is $A(n) = 1/n sum_(i=1)^n "lcm"(n, i) = sum_(i=1)^n i\/gcd(n, i)$. Grouping the $i$ by $d = gcd(n, i)$ and writing $i = d j$ with $gcd(j, n\/d) = 1$ turns the inner term into $j$, so $A(n) = sum_(e | n) T(e)$ where $T(e)$ sums the integers in $[1, e]$ coprime to $e$, namely $T(e) = e phi(e) \/ 2$ for $e >= 2$ and $T(1) = 1$. This gives $A(10) = 32$. Summing over $k <= n$ and counting how often each $e$ divides $k$,
$
S(n) = sum_(e=1)^n T(e) floor(n\/e) = 1/2 (n + sum_(e=1)^n e phi(e) floor(n\/e)),
$
which reproduces $S(100) = 122726$.

Writing $f(e) = e phi(e)$ and $F(x) = sum_(e <= x) f(e)$, the Dirichlet identity $(op("Id") dot phi) * op("Id") = op("Id")^2$ (because $sum_(d | n) phi(d) = n$) yields $sum_(m <= x) m dot F(floor(x\/m)) = sum_(m <= x) m^2$, hence the recursion
$
F(x) = (x(x+1)(2x+1))/6 - sum_(m >= 2) m dot F(floor(x\/m)).
$
Sieving $f$ up to $\~N^(2\/3)$ and memoizing $F$ on the $O(sqrt(N))$ values $floor(N\/m)$ makes the whole evaluation sublinear; the final $sum_(e) f(e) floor(N\/e)$ is also accumulated over divisor blocks, all modulo the prime $999999017$.

#pagebreak()
#link("https://projecteuler.net/problem=449")[= Problem 449: Chocolate Covered Candy]

Solution: 103.37870096

The candy is the spheroid $x^2\/a^2 + y^2\/a^2 + z^2\/b^2 = 1$, coated with a uniform $1$ mm layer; the chocolate occupies the parallel body at distance $t = 1$. By the Steiner tube formula, for a convex body the volume of the layer of thickness $t$ is $S t + M t^2 + (4 pi \/ 3) t^3$, where $S$ is the surface area, $M = integral H thin d A$ is the integral of the mean curvature, and the cubic coefficient $(4 pi)\/3 = 1/3 integral K thin d A$ comes from Gauss--Bonnet. At $t = 1$ the answer is simply $S + M + 4 pi \/ 3$ (which gives $28 pi \/ 3$ for the unit sphere).

Treating the spheroid as a surface of revolution with profile $(r, z) = (a sin u, b cos u)$ and line element $W = sqrt(a^2 cos^2 u + b^2 sin^2 u)$, the two integrals reduce to
$
S = 2 pi a integral_0^pi sin u dot W thin d u, quad
M = pi integral_0^pi sin u (a^2 b \/ W^2 + b) thin d u,
$
using the meridional curvature $a b \/ W^3$ and the azimuthal curvature $b \/ (a W)$. Evaluating these by high-resolution numerical integration reproduces the given $a = 2$ value $60.35475635$ and yields the $a = 3$ answer.

#pagebreak()
#link("https://projecteuler.net/problem=451")[= Problem 451: Modular Inverses]

Solution: 153651073760956

A number $m$ is its own inverse modulo $n$ exactly when $m^2 equiv 1 space (mod n)$, and $I(n)$ is the largest such $m$ below $n - 1$. The self-inverse residues come in complementary pairs $(m, n - m)$ -- if $m^2 equiv 1$ then $(n - m)^2 equiv 1$ too -- and both $1$ and $n - 1$ are always solutions. So the largest solution below $n - 1$ is the complement of the _smallest_ solution above $1$:
$
I(n) = n - s(n), quad s(n) = min {m > 1 : m^2 equiv 1 space (mod n)}.
$
By CRT, the roots of $x^2 equiv 1$ modulo $n = product q_i$ (each $q_i$ a prime power) are all combinations of the roots modulo each $q_i$: just ${1, q_i - 1}$ for odd primes, but for powers of two there is one root mod $2$, two mod $4$, and four mod $2^e$ ($e >= 3$), namely ${1, 2^(e-1) - 1, 2^(e-1) + 1, 2^e - 1}$.

A smallest-prime-factor sieve to $2 dot 10^7$ factors every $n$ quickly. For each, build the CRT basis $b_i equiv 1 space (mod q_i)$, $b_i equiv 0$ modulo the other factors (one modular inverse per factor via the extended Euclidean algorithm), enumerate the at-most-$256$ root combinations $sum_i r_i b_i space (mod n)$, and take the smallest exceeding $1$. Summing $n - s(n)$ over $3 <= n <= 2 dot 10^7$ runs in a few seconds. The method gives $I(15) = 11$, $I(100) = 51$ and $I(7) = 1$.

#pagebreak()
#link("https://projecteuler.net/problem=452")[= Problem 452: Long Products]

Solution: 345558983

$F(m, n)$ counts $n$-tuples of positive integers whose product is at most $m$; we want $F(10^9, 10^9) mod 1234567891$.

== A multiplicative function with constant prime values

Tuples with product exactly $k$ number $d_n (k) = product_p binom(e_p + n - 1, e_p)$ — ordered factorisations are stars-and-bars per prime — so $F(m, n) = sum_(k <= m) d_n (k)$, the summatory of a multiplicative function taking the *same* value $n$ at every prime. The binomials need only $e <= log_2 m approx 30$ values, built mod $p$ with Fermat inverses (the exact reason the modulus being prime matters — using a convenient composite modulus for a check was this solution's one bug).

== Splitting off the largest prime

Write each $k > 1$ by its largest prime factor $q$: if $q$ appears once, $k = v q$ with $q$ exceeding every prime of $v$, contributing $f(v) dot n$ for each of the $pi(m \/ v) - pi(P(v))$ admissible primes — a bulk term needing only prime counts; otherwise $q^2 | k$, forcing $q^2 <= m \/ (k \/ q^("ord"))$. That condition cascades: every base $v$ and every repeated-largest-prime number is reachable by a DFS that extends a current value $d$ by powers of primes $p_j$ with $p_j^2 <= m \/ d$ — and that constraint keeps the reachable set near $10^6$ nodes at $m = 10^9$ (numbers whose largest prime essentially fits twice). Bases whose largest prime has exponent $1$ are never self-counted; the parent's bulk term covered them.

The prime counts $pi(m \/ d)$ at every quotient come from a Lucy_Hedgehog sieve in $O(m^(3\/4))$. The given $F(10, 10) = 571$ (also verified by hand against the eleven values of $d_10$) and $F(10^6, 10^6) equiv 252903833$ both reproduce, alongside direct factorisation sums at $10^4$ and $10^5$.

#pagebreak()
#link("https://projecteuler.net/problem=454")[= Problem 454: Diophantine Reciprocals III]

Solution: 5435004633092

$F(L)$ counts solutions of $1\/x + 1\/y = 1\/n$ in positive integers with $x < y <= L$; we want $F(10^12)$.

== Parametrising the solutions

Let $g = gcd(x, y)$ and write $x = g u$, $y = g v$ with $gcd(u, v) = 1$, $u < v$. The equation gives $n = g u v \/ (u + v)$, and since $u + v$ is coprime to both $u$ and $v$, it must divide $g$: setting $g = d (u + v)$,
$
x = d u (u + v), quad y = d v (u + v), quad n = d u v,
$
a bijection between solutions and triples $(d, u, v)$ with $gcd(u, v) = 1$, $u < v$. The constraint $y <= L$ caps $d$, so
$
F(L) = sum_(u < v, gcd(u, v) = 1) floor(L / (v(u + v))).
$

== Evaluating the double sum

Scaling $(u, v) arrow.r (g u, g v)$ and Möbius-inverting removes the coprimality:
$
F(L) = sum_(g >= 1) mu(g) H(floor(L \/ g^2)), quad H(M) = sum_(1 <= u < v) floor(M / (v(u + v))).
$
For $H$, substitute $s = u + v$, which ranges over $v < s < 2v$: $H(M) = sum_v sum_(s = v + 1)^(min(2v - 1, floor(M\/v))) floor(floor(M\/v) \/ s)$, and the inner sum collapses with the usual quotient-block trick. Since $v(u + v) >= 6$, only $g <= sqrt(L\/6)$ contribute (Möbius values from a sieve). The whole computation is a few seconds; $F(15) = 4$ and $F(1000) = 1069$ from the problem reproduce, and a brute force over all pairs agrees at $L = 300$.

#pagebreak()
#link("https://projecteuler.net/problem=455")[= Problem 455: Powers with Trailing Digits]

Solution: 450186511399999

$f(n)$ is the largest positive $x < 10^9$ whose $9$ digits (with leading zeros) are the last $9$ digits of $n^x$ — that is, the largest solution of the fixed-point congruence $n^x equiv x space (mod 10^9)$. We want $sum_(n=2)^(10^6) f(n)$.

If $n$ is a multiple of $10$, then for $x >= 9$ the power $n^x$ ends in nine zeros, forcing $x equiv 0$, so no positive solution exists and $f(n) = 0$ (matching $f(10) = 0$).

Otherwise iterate the map $x arrow.r n^x mod 10^9$. The key fact is that $n^x mod 10^9$ depends only on $x mod lambda(10^9)$ (once $x$ is large enough to saturate the small prime powers shared with the modulus), where $lambda$ is the Carmichael function, and $lambda(10^9) = 5 dot 10^7$ divides $10^9$. Applying this repeatedly, the value after $k$ iterations is determined by the start modulo the rapidly shrinking chain $lambda(10^9), lambda(lambda(10^9)), dots.h$, which collapses to $1$ in a few dozen steps. So from any starting value the iteration reaches the same fixed point — the value of the infinite power tower $n^(n^(n^(dots.up))) mod 10^9$ — and that fixed point is the unique large solution of the congruence, hence $f(n)$. In practice convergence takes well under $40$ steps; the code asserts it.

The examples $f(4) = 411728896$ and $f(157) = 743757$ and the partial sum $sum_(n <= 10^3) f(n) = 442530011399$ all reproduce.

#pagebreak()
#link("https://projecteuler.net/problem=456")[= Problem 456: Triangles Containing the Origin II]

Solution: 333333208685971546

$C(n)$ counts triangles with vertices among the first $n$ pseudo-random points that contain the origin strictly in their interior; we want $C(2000000)$.

== Complement counting by half-planes

A triangle fails to contain the origin strictly exactly when its three vertices lie in a closed half-plane through the origin — equivalently when their directions span a minimal closed arc of length at most $pi$. The clean textbook count assumes all directions distinct and non-antipodal, but an audit of the actual dataset found $14027$ same-direction and $15824$ antipodal pairs, so the degenerate cases had to be derived, not waved away.

Group the points into blocks of equal *primitive* direction, circularly ordered (floating angles only sort the blocks; all decisive comparisons are exact integer cross and dot products). Assign each bad triple the leader: the minimal-index point at its arc's start. From a leader in block $b$ of size $s$ with $W$ points in the window — the strictly-counter-clockwise half-turn plus the antipodal block — hockey-stick summation over the leader's index rank gives $sum C(c_i, 2) = binom(W + s, 3) - binom(W, 3)$ per block, accumulated with one monotone two-pointer sweep. The single flaw of this assignment is that a triple lying on a full line through the origin and using both rays acquires one leader per ray, so $binom(r_1 + r_2, 3) - binom(r_1, 3) - binom(r_2, 3)$ is subtracted once per such line. Then $C(n) = binom(n, 3) - B$.

The exact-sign brute force (origin strictly inside iff the three pairwise cross products share a strict sign) agrees at $n = 8, 30, 80, 150$, and both given values $C(600) = 8950634$ and $C(40000) = 2666610948988$ — the latter already exercising the degenerate corrections — reproduce. The full two-million-point run takes three seconds.

#pagebreak()
#link("https://projecteuler.net/problem=457")[= Problem 457: A Polynomial Modulo the Square of a Prime]

Solution: 2647787126797397063

For $f(n) = n^2 - 3n - 1$, $R(p)$ is the smallest positive $n$ with $p^2 | f(n)$ (or $0$ if none); we want $"SR"(10^7) = sum_(p <= 10^7) R(p)$.

Completing the square, the roots are $n = (3 plus.minus sqrt(13)) \/ 2$, so for odd $p eq.not 13$ a root mod $p^2$ exists exactly when $13$ is a quadratic residue mod $p$ — and then there are two simple roots, each lifting uniquely. Two primes fail outright: $f(n)$ is always odd (so $p = 2$ gives $R = 0$), and mod $13$ the discriminant vanishes, leaving the double root $n equiv 8$ with $f(8) = 39$ not divisible by $169$; since $f'(8) equiv 0$, the root cannot Hensel-lift, so $R(13) = 0$.

For each remaining prime with $(13 | p) = 1$ (checked by an Euler-criterion power), compute $s = sqrt(13) mod p$ with Tonelli–Shanks, lift it to mod $p^2$ by one Newton/Hensel step $s arrow.l s - (s^2 - 13)(2s)^(-1)$, and form the two roots $(3 plus.minus s) \/ 2 mod p^2$; $R(p)$ is the smaller. Products are taken with overflow-safe modular multiplication since $p^2$ reaches $10^14$. The whole sum over the $620000$ primes runs in seconds, and the routine is cross-checked against a direct search of $n in [1, p^2]$ for all primes up to $200$.

#pagebreak()
#link("https://projecteuler.net/problem=458")[= Problem 458: Permutations of Project]

Solution: 423341841

$T(n)$ counts strings of length $n$ over the seven-letter alphabet ${c, e, j, o, p, r, t}$ that contain no substring which is a permutation of "project" — that is, no window of seven consecutive, pairwise-distinct letters. We want the last $9$ digits of $T(10^12)$.

== The distinct-suffix state

Scanning a string left to right, the only thing that matters is the length $k$ of the *maximal pairwise-distinct suffix*: the string is forbidden the moment $k$ reaches $7$. Appending a letter from state $k$:
- a letter equal to the one $i$ positions back ($1 <= i <= k$) cuts the distinct suffix to length exactly $i$ — one letter choice for each $i$;
- any of the $7 - k$ letters not in the suffix extends it to $k + 1$.

Dropping every transition into $k = 7$ leaves a $6 times 6$ transition matrix $M$ on states $1, dots.h, 6$ (from state $6$, exactly one of the seven letters is discarded). Then $T(n)$ is the total weight of $M^(n - 1)$ applied to the start vector ($7$ strings of length $1$, all in state $1$), computed by binary exponentiation in $O(log n)$ matrix products, taken mod $10^9$ throughout.

The check values both reproduce: $T(7) = 7^7 - 7! = 818503$ from the problem, and $T(8)$ agrees with a brute force over all $7^8$ strings.

#pagebreak()
#link("https://projecteuler.net/problem=460")[= Problem 460: An Ant on the Move]

Solution: 18.420738199

An ant walks from $A(0, 1)$ to $B(d, 1)$ through lattice points with $x >= 0$, $y >= 1$; a segment from height $y_0$ to $y_1$ is traversed at the logarithmic-mean velocity $(y_1 - y_0) \/ (ln y_1 - ln y_0)$ (and at $v = y_0$ when level). Find $F(10^4)$, the minimum total time, to nine decimals.

== It's hyperbolic geometry

The segment time equals $L dot (ln y_1 - ln y_0) \/ (y_1 - y_0)$, which is exactly $integral d s \/ y$ along the straight chord — the *hyperbolic length* in the upper half-plane model. So $F(d)$ is the shortest hyperbolic length of a lattice polyline, and the continuum geodesic through the endpoints is the semicircle centred at $(d \/ 2, 0)$ with apex height $approx d \/ 2$; indeed $F(10^4)$ exceeds the continuum distance $"arccosh"(1 + d^2 \/ 2) approx 18.42068$ by only $6 dot 10^(-5)$ of lattice quantisation penalty.

== Band DP, and a trap at the walls

The DP processes columns left to right with chords spanning up to several hundred columns and vertical sweeps within each column. A complete all-points DP is feasible up to $d approx 200$ and reproduces all three given values; tracing it confirms the optimal vertices hug the semicircle to within about one unit, so for $d = 10^4$ a band of half-width $6$–$10$ around the circle suffices — *except at the ends*. There the geodesic is nearly vertical (slope $d \/ 2$ at $x = 0$), and the optimal lattice path instead climbs the wall $x = 0$ vertically (cost $ln$-ratio) before chording onto the circle. An early version capped the wall columns at the band height and silently clipped this climb: the error surfaced only as a suspicious dependence of the answer on band width, and a parent-tracking trace showed the path pinned to the band ceiling at $x = 0$. With full-height columns near both walls the answer is identical across wall heights $200$–$900$ and across two independent parameter settings to $10^(-12)$, in about $30$ seconds.

#pagebreak()
#link("https://projecteuler.net/problem=461")[= Problem 461: Almost Pi]

Solution: 159820276

With $f_n (k) = e^(k \/ n) - 1$, find $g(n) = a^2 + b^2 + c^2 + d^2$ for the quadruple minimising $|f_n (a) + f_n (b) + f_n (c) + f_n (d) - pi|$ at $n = 10^4$.

== Meet in the middle, carefully

Useful arguments satisfy $f_n (k) <= pi$, so $k <= n ln(1 + pi) approx 14216$. All $approx 6.6 dot 10^7$ pair sums $f_a + f_b <= pi$ are generated and sorted in place, and a single two-pointer pass over the sorted array finds the pair-of-pairs total closest to $pi$ in $O(N)$.

Two precision traps shaped the implementation. First, the optimal error at this $n$ is around $10^(-15)$ — inside `float64` rounding noise — so the sweep keeps *every* candidate within a $3 dot 10^(-13)$ band of the running best, and each is re-evaluated in $50$-digit decimal exponentials against a high-precision $pi$ before the winner is declared. Second, recovering $(a, b)$ from a chosen pair-sum would normally need index arrays alongside the $530$ MB of sums; instead a single extra sweep re-finds the bit-exact float value — identical arithmetic guarantees an exact match — for all candidate values at once.

The given $g(200) = 64658$ reproduces, and the whole run takes a few seconds.

#pagebreak()
#link("https://projecteuler.net/problem=462")[= Problem 462: Permutation of $3$-smooth Numbers]

Solution: 5.5350769703e1512

$F(N)$ counts the orderings of the $3$-smooth numbers up to $N$ in which every element follows all of its proper divisors; we want $F(10^18)$ in scientific notation to ten places.

Writing each $3$-smooth number as $2^i 3^j$, divisibility is the componentwise order on $(i, j)$, and the region ${2^i 3^j <= N}$ is a Young diagram: row $j$ has length $floor(log_2 (N \/ 3^j)) + 1$. The valid orderings are exactly the linear extensions of a Young-diagram poset — standard Young tableaux — so the hook length formula applies:
$
F(N) = K! / (product "hooks"), quad K = |S(N)| approx 1100 "cells for" N = 10^18.
$
The arithmetic is done exactly in big integers ($K!$ has a few thousand digits) and formatted with guarded decimal rounding. The hand-checks $F(6) = 5! \/ 24 = 5$ and $F(8) = 6! \/ 80 = 9$ match the problem, as do a bitmask brute force over all linear extensions up to $N = 20$ and the given $F(1000) approx 8.8521816557 dot 10^21$.

#pagebreak()
#link("https://projecteuler.net/problem=463")[= Problem 463: A Weird Recurrence Relation]

Solution: 808981553

The four cases of $f$ combine neatly: summing one block of four gives $f(4n) + f(4n+1) + f(4n+2) + f(4n+3) = 6 f(2n+1) - 2 f(n)$. Checking small values reveals what $f$ really is -- the _binary bit-reversal_ of $n$: writing $n$ with $b = floor(log_2 n) + 1$ bits and reversing them. Indeed $f(8) = f(1000_2) = 0001_2 = 1$ and $f(5) = f(101_2) = 101_2 = 5$, matching the recurrence.

So $S(N) = sum_(i=1)^N "rev"(i)$. The $b$-bit numbers $[2^(b-1), 2^b - 1]$ reverse onto every $b$-bit pattern whose leading bit is set, and a short computation shows their reversals sum to exactly $4^(b-1)$; the full groups for $b = 1, dots, B-1$ (with $B = $ bit length of $N$) therefore contribute $sum_(b=1)^(B-1) 4^(b-1)$. The top group $[2^(B-1), N]$ is partial, so its reversal sum is taken bit by bit: bit $k$ contributes $2^(B-1-k)$ times the number of in-range integers with that bit set, each count obtained in closed form. This reproduces $S(8) = 22$ and $S(100) = 3604$, and $S(3^37) space (mod 10^9)$ follows instantly.

#pagebreak()
#link("https://projecteuler.net/problem=464")[= Problem 464: Möbius Function and Intervals]

Solution: 198775297232878

$P(a, b)$ and $N(a, b)$ count the integers in $[a, b]$ with $mu = +1$ and $mu = -1$; $C(n)$ counts the pairs $1 <= a <= b <= n$ with both $99 N <= 100 P$ and $99 P <= 100 N$. We want $C(2 dot 10^7)$.

== From intervals to dominance

With prefix counts $P_k, N_k$, both inequalities linearise: setting $U_k = 100 P_k - 99 N_k$ and $V_k = 100 N_k - 99 P_k$, the pair $(a, b)$ qualifies exactly when $U_(a-1) <= U_b$ and $V_(a-1) <= V_b$ — a two-dimensional dominance over the $n + 1$ prefix points.

The order constraint $a - 1 < b$ comes for free: $U_k + V_k = P_k + N_k$, the count of squarefree numbers, never decreases, so whenever two *distinct* $(U, V)$ values dominate, the dominated one has the smaller index; and groups of identical $(U, V)$ (stretches of $mu = 0$) contribute each unordered pair exactly once. Hence $C(n)$ equals the number of pairs $p$ before $q$ with $V_p <= V_q$ after sorting the prefix points lexicographically by $(U, V)$ — a non-inversion count by a Fenwick tree over compressed $V$ ranks, $O(n log n)$ overall.

A direct double loop over all intervals confirms $C(10) = 13$ and $C(500) = 16676$, and the given $C(10^4) = 20155319$ also reproduces. The full run over twenty million prefixes takes half a minute.

#pagebreak()
#link("https://projecteuler.net/problem=466")[= Problem 466: Distinct Terms in a Multiplication Table]

Solution: 258381958195474745

$P(m, n)$ counts the distinct entries of an $m times n$ multiplication table; we want $P(64, 10^16)$.

== Inclusion–exclusion on the rows

The table is the union of the rows $A_i = {i j : j <= n}$, and an intersection over a set $S$ of rows is exactly the multiples of $"lcm"(S)$ not exceeding $n dot min(S)$, so
$
P = sum_(emptyset != S subset.eq {1, dots.h, 64}) (-1)^(|S| + 1) floor((n dot min(S)) / ("lcm"(S))).
$
Grouping subsets by their minimum $m$ and searching the remaining elements $m + 1, dots.h, 64$ depth-first would still be $2^63$ branches; two prunes collapse it.

== Two prunes

First, once the running $"lcm"$ $L$ exceeds $n m$, every deeper floor is zero and the whole alternating subtree vanishes. Second — the decisive one — if the next element $i$ *divides* $L$, then taking or skipping $i$ leaves the lcm unchanged while flipping the sign, so the subsets pair up and cancel exactly: the subtree contributes nothing and is cut without recursion. What survives are only chains of genuinely lcm-increasing elements below the $n m$ ceiling, few enough that memoisation on $(i, L)$ per minimum finishes in a couple of minutes of plain Python with exact big integers.

All four given values check out, including $P(32, 10^15) = 13826382602124302$ which exercises the full pipeline at scale, alongside brute-force set construction at small sizes.

#pagebreak()
#link("https://projecteuler.net/problem=467")[= Problem 467: Superinteger]

Solution: 775181359

$P_n$ and $C_n$ concatenate the digital roots of the first $n$ primes and the first $n$ composites; $f(n)$ is the smallest integer containing both as subsequences. We want $f(10^4) mod (10^9 + 7)$.

== Shortest, then smallest

The smallest common superinteger is first the *shortest* common supersequence, then the lexicographically least among those (digits are $1$–$9$, so length strictly dominates value and there is no leading-zero subtlety). A backward DP over suffix pairs gives the SCS length table in $O(n^2)$ — a hundred million `int16` cells.

== Greedy reconstruction is safe

At state $(i, j)$ the next character of any *minimal* supersequence must be $P[i]$ or $C[j]$: any other character consumes nothing and only lengthens the result. When the two differ, either move is permitted exactly when it drops the table value by one, and among permitted moves the smaller digit is chosen; when they agree, one character serves both strings and is forced. The walk emits the $approx 1.7 dot 10^4$ digits while folding the value modulo $10^9 + 7$. Both givens reproduce: $f(10) = 2357246891352679$ exactly, and $f(100) equiv 771661825$.

#pagebreak()

#pagebreak()
#link("https://projecteuler.net/problem=469")[= Problem 469: Empty Chairs]

Solution: 0.56766764161831

Knights take random empty chairs around a round table of $N$, always leaving at least one empty chair beside each occupied one, until no admissible chair remains; $E(N)$ is the expected fraction of empty chairs. This is random sequential adsorption with nearest-neighbour exclusion. The first knight (uniform, but by symmetry any seat) occupies one chair and forbids its two neighbours, leaving a _line_ of $N - 3$ free chairs, so the expected number occupied is $M(N) = 1 + g(N - 3)$ where $g(m)$ is the same quantity for a row of $m$ chairs. Splitting a row on its first knight gives
$
g(m) = 1 + 2/m sum_(j=0)^(m-2) g(j),
$
which reproduces $E(4) = (4 - M(4)) \/ 4 = 1\/2$ and $E(6) = 5\/9$.

Asymptotically $g(m) = theta m + (3 theta - 1) + epsilon(m)$ with $theta = (1 - e^(-2)) \/ 2$, and substituting back the constant cancels exactly: $M(N) = theta N + epsilon(N - 3)$, so the empty fraction is $(1 + e^(-2)) \/ 2$ minus a correction $epsilon(N - 3) \/ N$. The correction decays faster than any power of $N$ (it already agrees to sixteen digits by $N = 100$), so for $N = 10^18$ the answer is $(1 + e^(-2)) \/ 2$ rounded to fourteen places.

#pagebreak()
#link("https://projecteuler.net/problem=479")[= Problem 479: Roots on the Rise]

Solution: 191541795

For each $k$ the three numbers $a_k, b_k, c_k$ solve $1\/x = (k\/x)^2 (k + x^2) - k x$. Multiplying through by $x^2$ and rearranging turns this into the cubic
$
x^3 - k x^2 + 1/k x - k^2 = 0,
$
so Vieta's formulas give $a + b + c = k$, $a b + b c + c a = 1\/k$ and $a b c = k^2$. The summand depends only on the symmetric product
$
(a+b)(b+c)(c+a) = (a+b+c)(a b + b c + c a) - a b c = k dot 1/k - k^2 = 1 - k^2,
$
which is why $S(n)$ comes out an integer. Hence the triple product raised to the $p$-th power is simply $(1 - k^2)^p$ and
$
S(n) = sum_(k=1)^n sum_(p=1)^n (1 - k^2)^p.
$
The inner sum is a geometric series with ratio $r = 1 - k^2$: it equals $r(r^n - 1)\/(r - 1)$ (and vanishes for $k = 1$, where $r = 0$). Evaluating each with fast exponentiation and a modular inverse of $r - 1 = -k^2$ modulo $10^9 + 7$ takes $O(n log n)$ overall. It reproduces $S(4) = 51160$.

#pagebreak()
#link("https://projecteuler.net/problem=485")[= Problem 485: Maximum Number of Divisors]

Solution: 51281274340

With $d(n)$ the divisor count, $M(n, k)$ is the maximum of $d$ over the length-$k$ window $[n, n + k - 1]$, and $S(u, k) = sum_(n=1)^(u-k+1) M(n, k)$. We want $S(10^8, 10^5)$, so the task is the sum of sliding-window maxima of the divisor-count sequence.

First tabulate $d$ up to $10^8$ with the harmonic sieve: for every $i$, add one to each multiple of $i$. Since $d(n) < 800$ in this range the values fit in $16$-bit cells, keeping the array near $200$ MB. Then sweep a monotonic deque across it: each index is pushed once after evicting smaller-or-equal values from the back, the front is dropped when it leaves the window, and once $k$ values have been seen the front holds the current window maximum. Held in a circular buffer of capacity $k + 1$, this gives every maximum in amortised $O(1)$, so the whole sum is one linear pass. The construction reproduces $S(1000, 10) = 17176$.

#pagebreak()
#link("https://projecteuler.net/problem=487")[= Problem 487: Sums of Power Sums]

Solution: 106650212746

With $f_k(n) = sum_(i=1)^n i^k$ and $S_k(n) = sum_(i=1)^n f_k(i)$, we want $sum_p (S_(10000)(10^12) mod p)$ over the primes $p$ in $(2 dot 10^9, space 2 dot 10^9 + 2000)$. Swapping the order of summation, $S_k(n) = sum_(j=1)^n (n - j + 1) j^k = (n+1) f_k(n) - f_(k+1)(n)$, and since $f_k$ is a polynomial of degree $k+1$ (Faulhaber), $S_k$ is a polynomial in $n$ of degree $k + 2$.

A degree-$(k+2)$ polynomial is pinned down by its values at the consecutive nodes $0, 1, dots.c, k+2$, which are cheap to tabulate mod $p$: run two prefix sums, $f <- f + i^k$ and $S <- S + f$, with $i^k mod p$ from fast exponentiation. Lagrange interpolation at $x = 10^12 mod p$ then gives $S_k(10^12) mod p$,
$
S_k(x) = sum_(i=0)^d y_i (product_(j != i) (x - j)) / (product_(j != i) (i - j)), quad d = k + 2,
$
evaluated in $O(d)$ via prefix/suffix products of $(x - j)$ and the factorial identity $product_(j != i)(i - j) = (-1)^(d-i) i! (d-i)!$. Because every $p < 2^31$, the products $a dot b$ stay within $64$ bits. Reducing each integer factor $(10^12 - j) equiv (x - j)$ mod $p$ is valid even though $S_k$ has rational coefficients, since the Lagrange form never expands into monomials. There are $100$ primes in the window; the method reproduces the stated $S_4(100) = 35375333830$.

#pagebreak()
#link("https://projecteuler.net/problem=491")[= Problem 491: Double Pandigital Number Divisible by 11]

Solution: 194505988824000

A double pandigital number has all twenty digits placed so each of $0..9$ appears twice, with no leading zero. Index the twenty positions by their power of ten; since $10 equiv -1 space (mod 11)$, the number is divisible by $11$ when the digits in even powers and odd powers satisfy $E - O equiv 0 space (mod 11)$. Each group holds ten positions, and the grand total is $E + O = 2(0 + 1 + dots.c + 9) = 90$, so $2E equiv 90 equiv 2$ and hence $E equiv 1 space (mod 11)$.

Let $k_d in {0, 1, 2}$ be how many copies of digit $d$ land in the even-power group; a valid assignment needs $sum_d k_d = 10$ and $sum_d d k_d equiv 1 space (mod 11)$. There are only $3^10$ assignments to scan. Each contributes $(10! \/ product_d k_d !)(10! \/ product_d (2 - k_d)!)$ arrangements, the multinomials for filling the two groups. The leading digit lies in the odd-power group, so the arrangements with a zero there are removed: fixing one of its $2 - k_0$ zeros in front leaves $9! \/ ((2 - k_0 - 1)! product_(d >= 1)(2 - k_d)!)$ ways for the rest. Summing over all valid $(k_d)$ gives the count directly.

#pagebreak()
#link("https://projecteuler.net/problem=492")[= Problem 492: Exploding Sequence]

Solution: 242586962923928

The sequence $a_1 = 1$, $a_(k+1) = 6 a_k^2 + 10 a_k + 3$ grows doubly exponentially, but the substitution $w = 6 a + 5$ linearises the quadratic map: $w_(k+1) = w_k^2 - 2$ with $w_1 = 11$. Writing $w = lambda + lambda^(-1)$, squaring-minus-two just doubles the exponent, so
$
w_n = lambda^(2^(n-1)) + lambda^(-2^(n-1)), quad lambda + lambda^(-1) = 11,
$
where $lambda$ is a root of $X^2 - 11 X + 1 = 0$ (discriminant $117 = 9 dot 13$). This is exactly the Lucas sequence $V_m = lambda^m + lambda^(-m)$ with parameters $P = 11$, $Q = 1$, and $a_n = (w_n - 5)\/6$.

To get $a_n space (mod p)$ for $n = 10^15$ the exponent $2^(n-1)$ is astronomically large, but $lambda$ lives in $FF_p$ when $13$ is a quadratic residue mod $p$ (then $lambda^(p-1) = 1$) and in $FF_(p^2)$ otherwise (then the conjugate is $lambda^(-1)$, so $lambda^(p+1) = 1$). Either way only $2^(n-1) mod (p minus.plus 1)$ matters; reduce it by fast exponentiation, evaluate $V_E$ with the Lucas doubling rules $V_(2j) = V_j^2 - 2$, $V_(2j+1) = V_j V_(j+1) - 11$, and divide by $6$. A segmented sieve supplies the primes in $[10^9, 10^9 + 10^7]$. The method reproduces $B(10^9, 10^3, 10^3) = 23674718882$ and $B(10^9, 10^3, 10^15) = 20731563854$.

#pagebreak()
#link("https://projecteuler.net/problem=493")[= Problem 493: Under the Rainbow]

Solution: 6.818741802

Seventy balls carry seven colours, ten of each; twenty are drawn at random, and we want the expected number of distinct colours among them. Linearity of expectation sidesteps the messy joint distribution: the expected count is the sum over the seven colours of the probability that each appears. A given colour is absent precisely when all twenty drawn balls come from the other sixty, which happens with probability $binom(60, 20) \/ binom(70, 20)$, so each colour is present with probability $1 - binom(60, 20) \/ binom(70, 20)$. The answer is
$
7 (1 - binom(60, 20) / binom(70, 20)) approx 6.818741802.
$

#pagebreak()
#link("https://projecteuler.net/problem=497")[= Problem 497: Drunken Tower of Hanoi]

Solution: 684901360

"Optimal" means fewest disk pickups, which forces the unique minimal Tower-of-Hanoi sequence of $2^n - 1$ moves. Bob's walk is a random walk on the squares ${1, dots.c, k}$ with reflecting ends, so the expected number of squares to get from one rod to another is the walk's first-passage time. For a step rightward from $i$ to $i+1$ the expected cost is $2 i - 1$, giving a first passage from $x$ to a larger square $y$ of $(y-1)^2 - (x-1)^2$; by the mirror symmetry a leftward passage costs $(k-y)^2 - (k-x)^2$. (These sum to the integer answer the problem promises.)

The total expected distance is a sum over Bob's visited rods: starting at $b$, then for each disk move walking to its source and then to its destination. The number of times each of the six directed rod-to-rod transitions occurs follows the Hanoi recursion. Moving $m$ disks $X -> Y$ (third rod $Z$) splits into moving $m-1$ disks $X -> Z$ (Bob from his current rod), the big disk $X -> Y$ (preceded by a hop $Z -> X$), then $m-1$ disks $Z -> Y$ (Bob now at $Y$). Carrying an $18$-state vector (six ordered pairs $times$ three possible start rods) of transition counts and advancing $m$ from $1$ to $10000$ gives every $E(n, dots.c)$ cheaply; multiplying counts by the first-passage costs and summing $mod 10^9$ over $n$ finishes it. The recursion reproduces $E(2, 5, 1, 3, 5) = 60$ and $E(3, 20, 4, 9, 17) = 2358$.

#pagebreak()
#link("https://projecteuler.net/problem=498")[= Problem 498: Remainder of Polynomial Division]

Solution: 472294837

$R_(n,m)(x)$ is the remainder of $x^n$ divided by $(x-1)^m$, and $C(n,m,d)$ is the absolute value of its degree-$d$ coefficient. Substituting $t = x - 1$ turns the dividend into $(t+1)^n$ and the divisor into $t^m$, so the remainder is simply the low-degree truncation $sum_(i=0)^(m-1) binom(n, i) t^i$. Re-expanding $t = x - 1$ and collecting the $x^d$ term gives
$
C(n, m, d) = binom(n, d) sum_(k=0)^(m-d-1) binom(n-d, k) (-1)^k.
$
The alternating partial sum telescopes via $sum_(k=0)^j binom(M, k)(-1)^k = (-1)^j binom(M-1, j)$, leaving the clean product
$
C(n, m, d) = binom(n, d) dot binom(n - d - 1, m - d - 1),
$
which reproduces $C(6,3,1) = 24$ and $C(100,10,4) = 227197811615775$. For $C(10^13, 10^12, 10^4)$ modulo the prime $999999937$, neither factor is divisible by the prime, and each binomial has arguments far larger than $p$, so Lucas' theorem reduces it to a product of binomials of base-$p$ digits (each digit's binomial evaluated by the multiplicative formula with one modular inverse).

#pagebreak()
#link("https://projecteuler.net/problem=500")[= Problem 500: Problem 500!!!]

Solution: 35407281

We need the smallest integer with exactly $2^(500500)$ divisors, modulo $500500507$. The divisor count of $n = product p_i^(e_i)$ is $product (e_i + 1)$, so to reach $2^(500500)$ every factor $e_i + 1$ must itself be a power of two, and we must accumulate exactly $500500$ doublings.

Each doubling corresponds to multiplying the current number by some $p^(2^k)$: this lifts the exponent of $p$ from $2^k - 1$ to $2^(k+1) - 1$, turning the local factor $2^k$ into $2^(k+1)$. To keep the result minimal, greedily take the $500500$ smallest values from the table ${p^(2^k) : p "prime", k >= 0}$. A min-heap does this: seed it with the primes themselves, and whenever $p^(2^k)$ is popped, push its square $p^(2^(k+1))$. Multiplying the $500500$ popped values modulo $500500507$ gives the answer. Squares of primes above $sqrt(7376507)$ already exceed the $500500$-th prime, so seeding with the first $500500$ primes is enough -- no prime beyond $7376507$ is ever needed.

#pagebreak()
#link("https://projecteuler.net/problem=501")[= Problem 501: Eight Divisors]

Solution: 197912312715

A number has exactly eight divisors precisely when its prime signature gives $product(e_i + 1) = 8$. There are three shapes:
- $p^7$,
- $p^3 q$ with distinct primes $p, q$,
- $p q r$ with $p < q < r$.

Let $pi(x)$ be the prime-counting function. The three contributions to $f(N)$ for $N = 10^12$ are
$
pi(N^(1\/7)) + sum_(p^3 <= N) (pi(N\/p^3) - 1) + sum_(p < q, p q^2 < N) (pi(N\/(p q)) - pi(q)),
$
where in the second sum the $-1$ removes the case $q = p$, and in the third we count primes $r$ with $q < r <= N\/(p q)$.

The arguments $N\/m$ range over the $O(sqrt(N))$ distinct values of $floor(N\/m)$, so we need $pi$ at those points. Computing them with the Lucy_Hedgehog recurrence in $O(N^(3\/4))$ time makes the whole evaluation fast. Checks $f(100) = 10$, $f(1000) = 180$, $f(10^6) = 224427$ all hold.

#pagebreak()
#link("https://projecteuler.net/problem=504")[= Problem 504: Square on the Inside]

Solution: 694687

The vertices $A(a, 0)$, $B(0, b)$, $C(-c, 0)$, $D(0, -d)$ form a kite whose diagonals lie on the axes, so its area is $1/2 (a + c)(b + d)$. The boundary lattice points on the four edges total $gcd(a, b) + gcd(b, c) + gcd(c, d) + gcd(d, a)$. By Pick's theorem $A = I + B\/2 - 1$, the strictly interior count is
$
I = ((a + c)(b + d) - (gcd(a,b) + gcd(b,c) + gcd(c,d) + gcd(d,a)))/2 + 1.
$
We just count quadruples $1 <= a, b, c, d <= 100$ for which $I$ is a perfect square. Precomputing a $gcd$ table and a boolean "is a square" array up to the maximum possible $I$ turns the $10^8$-iteration loop into simple lookups. For $m = 4$ this reproduces the stated $42$.

#pagebreak()
#link("https://projecteuler.net/problem=506")[= Problem 506: Clock Sequence]

Solution: 18934502

The digit stream repeats $1, 2, 3, 4, 3, 2$ with period $6$ (digit-sum $15$ per period), chopped into integers $v_n$ whose digit-sum equals $n$. We want $S(N) = sum_(n=1)^N v_n$ modulo $M = 123454321 = 11111^2$ for $N = 10^14$, far too many terms to build directly.

Let $T(n) = n(n+1)\/2$ be the cumulative digit-sum target. Walking the stream, the position consumed after emitting $v_1 dots v_n$ is
$
e(n) = 6 floor(T(n)\/15) + j(T(n) mod 15),
$
where $j$ maps the six attainable partial sums ${0,1,3,6,10,13}$ to ${0,1,2,3,4,5}$. The value $v_n$ is the digit block strictly between positions $e(n-1)$ and $e(n)$.

Reading the stream's prefixes as numbers modulo $M$ gives a closed form. With $g(n) = "Pr"_0[r] - C dot 10^r$, where $r = j(T(n) mod 15)$, $C = 123432\/999999$, and $"Pr"_0 = [0, 1, 12, 123, 1234, 12343]$, one verifies
$
v_n equiv g(n) - g(n-1) dot 10^(L_n) space (mod M), quad L_n = e(n) - e(n-1).
$
Now $g$ is periodic in $n$ with period $30$, and $L_(n+30) = L_n + 12$. Hence $S(N) = Sigma_1 - Sigma_2$ where $Sigma_1 = sum g(n)$ collapses to a $30$-term block sum, and $Sigma_2 = sum g(n-1) 10^(L_n)$ splits into $30$ geometric series of common ratio $10^12$ (whose denominator $10^12 - 1$ is invertible mod $M$). Everything is $O(1)$ after a $30$-term setup. Checks $S(11) = 36120$ and $S(1000) equiv 18232686$ confirm the formula.

#pagebreak()
#link("https://projecteuler.net/problem=507")[= Problem 507: Shortest Lattice Vector]

Solution: 316558047002627270

From tribonacci residues $r_i = t_i mod 10^7$, each $n$ yields vectors $V_n = (r-r, r+r, r dot r)$ and $W_n$ (the next six residues), and $S(n)$ is the minimal Manhattan length of $k V_n + l W_n$ over integer $(k, l) != (0, 0)$. We need $sum_(n=1)^(2 dot 10^7) S(n)$.

Each instance is a shortest-vector problem in a rank-2 lattice under the $L^1$ norm, solved by generalized Gauss (Kaib–Schnorr) reduction, valid for any symmetric convex norm: repeatedly swap so $norm(V) <= norm(W)$ and replace $W arrow.l W - t V$ with the integer $t$ minimizing $norm(W - t V)_1$. That objective is convex piecewise-linear in $t$ with its minimum at the weighted median of the ratios $w_i\/v_i$ (weights $|v_i|$); a float median estimate is corrected by evaluating a $plus.minus 2$ integer window, so exactness never relies on floating point. Norms strictly decrease, giving Euclidean-style convergence, and a final scan over $|k|, |l| <= 2$ of the reduced basis guards the terminal case. Degenerate inputs are handled separately: a zero vector makes the minimum 0, and collinear $V = c U$, $W = d U$ (primitive $U$) give $gcd(c, d) norm(U)_1$. Magnitudes stay within int64 throughout.

Verified against the given $S(1) = 32$ and $sum_(n <= 10) S(n) = 130762273722$, and against literal minimisation over $|k|, |l| <= 150$ for 3000 random small-entry instances including degenerate ones.

#pagebreak()
#link("https://projecteuler.net/problem=509")[= Problem 509: Divisor Nim]

Solution: 151725678

This is a three-pile impartial game: from a pile of $k$ stones a player removes a proper divisor of $k$. By the Sprague-Grundy theorem each pile has a Grundy value $g(k)$, and a position is a win for the player to move iff $g(a) xor g(b) xor g(c) != 0$.

Computing small values reveals $g(k) = nu_2(k)$, the exponent of $2$ in $k$. An odd $k$ has only odd divisors, so every move lands on an even number (Grundy $>= 1$), giving $g(k) = 0$; for $k = 2^a m$ with $m$ odd the reachable Grundy values are exactly $0, 1, dots, a-1$, so the mex is $a$.

So we count triples in $[1, n]^3$ whose valuations XOR to a nonzero value. Let $c_v = floor(n\/2^v) - floor(n\/2^(v+1))$ be the count of integers in $[1, n]$ with valuation $v$. Then
$
S(n) = n^3 - sum_(v_1, v_2) c_(v_1) c_(v_2) c_(v_1 xor v_2),
$
the subtracted term counting losing positions. Valuations only reach about $46$ for $n approx 1.23 dot 10^14$, so this is a tiny double sum. Checks $S(10) = 692$ and $S(100) = 735494$ hold.

#pagebreak()
#link("https://projecteuler.net/problem=510")[= Problem 510: Tangent Circles]

Solution: 315306518862563689

Two circles of radii $r_A, r_B$ rest on a line, tangent to each other, and a third circle of radius $r_C$ nestles between them tangent to both and to the line. Descartes' configuration along a line gives the curvature relation
$
1/sqrt(r_C) = 1/sqrt(r_A) + 1/sqrt(r_B).
$
Writing the radii in lowest terms shows every integer solution is parametrised by coprime $p <= q$ and a scale $e >= 1$:
$
r_A = e p^2 (p + q)^2, quad r_B = e q^2 (p + q)^2, quad r_C = e p^2 q^2,
$
and this is a bijection onto the integer triples. We need $S(n) = sum (r_A + r_B + r_C)$ over all solutions with $r_A, r_B, r_C <= n$, which here means $r_B = e q^2 (p+q)^2 <= n$ is the binding constraint.

For fixed coprime $p <= q$ let $u = p^2(p+q)^2 + q^2(p+q)^2 + p^2 q^2$ be the per-unit sum and $M = floor(n \/ (q^2 (p+q)^2))$ the largest scale. The scales $e = 1, dots, M$ contribute $u dot M(M+1)\/2$. Summing over coprime pairs with $q^2(p+q)^2 <= n$ finishes it. Checks $S(5) = 9$ and $S(100) = 3072$ hold.

#pagebreak()
#link("https://projecteuler.net/problem=511")[= Problem 511: Sequences with Nice Divisibility Properties]

Solution: 935247012

$"Seq"(n, k)$ counts the sequences $(a_1, dots, a_n)$ of positive integers in which every $a_i$ divides $n$ and $k | n + a_1 + dots.c + a_n$; we need the last nine digits of $"Seq"(1234567898765, 4321)$.

Only the residue of each term modulo $k$ matters, and the terms are chosen independently. Let $f$ be the vector indexed by $ZZ_k$ with $f[d mod k]$ incremented once per divisor $d$ of $n$. The distribution of $a_1 + dots.c + a_n$ over the residues is then the $n$-fold cyclic convolution power of $f$, so

$ "Seq"(n, k) = (f^(* n))[(-n) mod k] mod 10^9. $

Binary exponentiation needs $O(log n)$ cyclic convolutions of length $k$, $O(k^2 log n)$ work overall — about $1.5 times 10^9$ multiply–reduce steps for $k = 4321$ and $n approx 1.2 times 10^12 = 5 dot 41 dot 25343 dot 237631$ (just 16 divisors). The given $"Seq"(3, 4) = 4$, $"Seq"(4, 11) = 8$ and $"Seq"(1111, 24) eq.triple 840643584$ are asserted, and the convolution method is cross-checked against a direct position-by-position dynamic program for several small $(n, k)$.

#pagebreak()
#link("https://projecteuler.net/problem=512")[= Problem 512: Sums of Totients of Powers]

Solution: 50660591862310323

Let $f(n) = (sum_(i=1)^n phi(n^i)) mod (n+1)$ and $g(N) = sum_(n=1)^N f(n)$; we need $g(5 dot 10^8)$.

Because $phi(n^i) = n^(i-1) phi(n)$, the inner sum is $phi(n)(1 + n + dots + n^(n-1))$. Working modulo $n+1$, where $n equiv -1$, the powers alternate $n^(i-1) equiv (-1)^(i-1)$, so the geometric sum collapses to $1$ when $n$ is odd and $0$ when $n$ is even. Since $phi(n) <= n - 1 < n + 1$, no further reduction happens, and
$
f(n) = cases(phi(n) "if" n "odd", 0 "if" n "even").
$
Thus $g(N) = sum_(n "odd" <= N) phi(n)$; call it $A(N)$.

To evaluate $A$ in sublinear time, restrict the identity $sum_(d | m) phi(d) = m$ to odd $m$ (whose divisors are all odd). Summing over odd $m <= N$ and writing $m = d k$ with both odd,
$
sum_(m "odd" <= N) m = sum_(k "odd" <= N) A(floor(N\/k)).
$
The left side is the sum of the first $((N+1)\/2)$ odd numbers, namely $((N+1)\/2)^2$. Isolating the $k = 1$ term gives the recurrence
$
A(N) = (floor((N+1)\/2))^2 - sum_(k "odd", 3 <= k <= N) A(floor(N\/k)),
$
which we memoise over the $O(sqrt(N))$ distinct values of $floor(N\/k)$, with a linear $phi$-sieve supplying the base cases. As a check, $g(100) = 2007$.

#pagebreak()
#link("https://projecteuler.net/problem=513")[= Problem 513: Integral Median]

Solution: 2925619196

$A B C$ has integral sides $a <= b <= c$, and $m_C$ is the median from $C$ to the midpoint of $A B$. $F(n)$ counts triangles with $c <= n$ whose median is also integral; we need $F(10^5)$.

The median satisfies $4m^2 = 2a^2 + 2b^2 - c^2$. Working mod 8 forces $c = 2C$ even and $a equiv b mod 2$, so with $S = (a+b)\/2$, $D = (b-a)\/2$ the condition becomes $S^2 + D^2 = C^2 + m^2$, with constraints $C < S <= 2C$, $0 <= D <= 2C - S$ (this is $b <= c$) and $m >= 1$. Grouping as $(S-C)(S+C) = (m-D)(m+D) = u w = x y$ and applying the standard bijection $u = p r$, $x = p s$, $w = q s$, $y = q r$ with $gcd(r, s) = 1$ turns everything into linear conditions on $q$: $3 p r <= q s <= p r + 2C_max$, $q r >= p s$, $q(r-s) <= p(s - 3r)$ — which forces $s > r$ — plus a parity rule ($q equiv p$ if $r, s$ both odd, else $p, q$ both even).

For each $(r, s, p)$ the admissible $q$ form an arithmetic progression counted in $O(1)$; the upper bound caps $s$ near $sqrt(r^2 + 2 C_max r \/ p)$, giving roughly $10^10$ iterations parallelised over $r$. Verified against literal brute force (integer-square test over all triangles) for $n in {10, 50, 100, 300, 700}$, including the given $F(10) = 3$ and $F(50) = 165$.

#pagebreak()
#link("https://projecteuler.net/problem=516")[= Problem 516: 5-smooth Totients]

Solution: 939087315

A Hamming number is $5$-smooth: of the form $2^a 3^b 5^c$. We want $S(L) = sum_(n <= L, phi(n) "Hamming") n$ for $L = 10^12$, modulo $2^32$.

Since $phi$ is multiplicative with $phi(p^e) = p^(e-1)(p-1)$, the totient is $5$-smooth exactly when every prime-power factor contributes a $5$-smooth value. For $p in {2, 3, 5}$ this holds for every exponent (as $p - 1 in {1, 2, 4}$). For a prime $p > 5$ the factor $p^(e-1)$ would introduce $p$ itself unless $e = 1$, and then we additionally need $p - 1$ to be Hamming. So the admissible $n$ are precisely
$
n = (2^a 3^b 5^c) dot Q,
$
where $Q$ is a squarefree product of distinct "special" primes $p > 5$ with $p - 1$ Hamming. This factorisation is unique (the $2,3,5$ part is itself a Hamming number $H$), so
$
S(L) = sum_(Q) Q dot H(floor(L\/Q)),
$
summed over all squarefree special-prime products $Q <= L$, where $H(x)$ is the sum of Hamming numbers $<= x$. We list the few thousand Hamming numbers up to $L$ (with prefix sums for $H(x)$), collect the special primes by testing $h + 1$ for primality, and enumerate the products $Q$ by depth-first search. As a check, $S(100) = 3728$.

#pagebreak()
#link("https://projecteuler.net/problem=517")[= Problem 517: A Real Recursion]

Solution: 581468882

For real $a > 1$, $g_a (x) = 1$ for $x < a$ and $g_a (x) = g_a (x-1) + g_a (x-a)$ otherwise; $G(n) = g_(sqrt(n))(n)$. We need $sum G(p)$ over primes $10^7 < p < 10^7 + 10^4$, modulo $10^9 + 7$.

Unfolding the recursion, $g_a (x)$ counts step sequences over ${-1, -a}$ in which every proper prefix keeps the value at least $a$ while the full sum drops below $a$; since steps are positive decrements, only the last-but-one value matters. Split by the number $j$ of $a$-steps and the type of the final step, with $a = sqrt(n)$ irrational for prime $n$ and $floor(k a) = floor(sqrt(k^2 n))$ computed exactly via integer square roots:

- final step $-1$: the number of unit steps is forced to $L_j = x - floor((j+1)a)$, contributing $binom(L_j - 1 + j, j)$ when $L_j >= 1$ (the preceding steps are arranged freely);
- final step $-a$ (for $j >= 1$): the unit-step count ranges over $[max(0, L_j), x - floor(j a) - 1]$, and the hockey-stick identity collapses the contribution to $binom(U + j, j) - binom(max(0, L_j) + j - 1, j)$.

So $G(n)$ is a sum of $O(sqrt(n))$ binomials, evaluated with precomputed factorials mod $10^9 + 7$. The expansion is verified against a direct memoized recursion using exact integer comparisons $(n-i)^2 < (j+1)^2 n$ for various $n$, including the given $G(90) = 7564511$.

#pagebreak()
#link("https://projecteuler.net/problem=518")[= Problem 518: Prime Triples and Geometric Sequences]

Solution: 100315739184392

We want $S(n) = sum (a + b + c)$ over prime triples $a < b < c < n$ for which $a + 1$, $b + 1$, $c + 1$ form a geometric progression, with $n = 10^8$.

Every positive-integer geometric progression can be written $(k y^2, k x y, k x^2)$ with $x > y >= 1$ and $gcd(x, y) = 1$ (the middle term squared equals the product of the outer two). Setting
$
a = k y^2 - 1, quad b = k x y - 1, quad c = k x^2 - 1,
$
the ordering $a < b < c$ is automatic from $y < x$, and we need all three prime with $c < n$. Sieve primes up to $n$, then loop over $x$ (up to $sqrt(n)$), over $k$ with $k x^2 <= n$, prune on $c = k x^2 - 1$ being prime, and finally over coprime $y < x$ checking $a$ and $b$. As a check, $S(100) = 1035$ from the eleven listed triples.

#pagebreak()
#link("https://projecteuler.net/problem=519")[= Problem 519: Tricolored Coin Fountains]

Solution: 804739330

A fountain of coins has a gapless bottom row and every higher coin resting on exactly two adjacent coins below. $T(n)$ sums, over all fountains with $n$ coins, the number of proper 3-colourings (touching coins differ); we need the last 9 digits of $T(20000)$.

A fountain is equivalent to column heights $(h_1, ..., h_k)$ with $h_k = 1$ and $h_i <= h_(i+1) + 1$: coin $(r, i)$ rests on $(r-1, i)$ and $(r-1, i+1)$, a mutually-touching triangle, so each upper coin's colour is forced to the third colour of its supporters and a colouring is determined by the bottom row — encoded as $c_1$ plus differences $d_i = c_(i+1) - c_i in {plus.minus 1} mod 3$.

Propagating differences along rows via $D(r, i) = -(D(r-1, i) + D(r-1, i+1))$, an adjacent pair in row $r$ is properly coloured iff the two differences below are equal, and then $D(r, i) = D(r-1, i)$; unrolling shows the only constraints are $d_i = d_(i+1)$ whenever columns $i$ and $i+1$ both have height $>= 2$ (higher rows repeat the same equalities). Hence $T(n) = 3 sum 2^(k - 1 - e)$ over fountains, with $e$ the number of adjacent column pairs of height $>= 2$ each. A DP over (coins used, current leftmost height), prepending columns of height $h' <= h + 1$ with weight 1 if $h', h >= 2$ else 2, computes this in $O(n H^2)$ with $H approx sqrt(2n)$.

The analysis is verified by brute force — enumerating all fountains for $n <= 12$ and literally counting proper 3-colourings of the coin graph — matching the given $f(4) = 3$, $f(10) = 78$, $T(4) = 48$ and $T(10) = 17760$.

#pagebreak()
#link("https://projecteuler.net/problem=520")[= Problem 520: Simbers]

Solution: 238413705

A _simber_ is a positive integer in which every odd digit present occurs an odd number of times and every even digit present an even number of times. With $Q(n)$ the count of simbers of at most $n$ digits, we need $sum_(u=1)^39 Q(2^u) mod 1000000123$. As $2^39$ has hundreds of billions of digits, only a closed form will do.

Count length-$L$ digit strings (leading zeros allowed) with each even digit occurring an even number of times and each odd digit a $0$-or-odd number of times, via exponential generating functions: an even digit contributes $cosh(x)$ (even counts) and an odd digit $1 + sinh(x)$ ($0$ or odd). With five digits of each parity,
$
T(L) = L! [x^L] cosh(x)^5 (1 + sinh(x))^5 = 1/2^10 sum_j a_j j^L,
$
where, with $z = e^x$, the integer $a_j = [z^(j+10)] (z^2 + 1)^5 (z^2 + 2z - 1)^5$ for $-10 <= j <= 10$. A simber string that begins with $0$ pins one zero in front, leaving $L - 1$ digits in which digit $0$ must now appear an odd number of times; that count is $Z(L-1) = (1\/2^10) sum_j b_j j^(L-1)$ with $b_j = [z^(j+10)] (z^2 - 1)(z^2 + 1)^4 (z^2 + 2z - 1)^5$. The $L$-digit simbers (no leading zero) number $T(L) - Z(L-1)$, so
$
Q(n) = 1/2^10 (sum_j a_j sum_(L=1)^n j^L - sum_j b_j sum_(t=0)^(n-1) j^t),
$
each inner sum a geometric series evaluated modulo $1000000123$. As checks, $Q(7) = 287975$ and $Q(100) equiv 123864868$.

#pagebreak()
#link("https://projecteuler.net/problem=521")[= Problem 521: Smallest Prime Factor]

Solution: 44389811

Let $"smpf"(i)$ be the smallest prime factor of $i$ and $S(n) = sum_(2 <= i <= n) "smpf"(i)$; we need $S(10^12) mod 10^9$.

Group the integers by their smallest prime factor. The $i <= n$ with $"smpf"(i) = p$ are exactly $i = p m$ where $m$ has no prime factor below $p$, so their number is $Phi(floor(n\/p), p)$, where $Phi(x, p)$ counts the integers $m <= x$ that equal $1$ or have every prime factor at least $p$. Hence
$
S(n) = sum_(p "prime" <= n) p dot Phi(floor(n\/p), p).
$

Split at $sqrt(n)$. For $p > sqrt(n)$ we have $floor(n\/p) < p$, so the only valid $m$ is $1$ and $Phi = 1$; these primes contribute $sum_(sqrt(n) < p <= n) p = "PrimeSum"(n) - "PrimeSum"(sqrt(n))$. For $p <= sqrt(n)$ we use a Lucy_Hedgehog sieve: maintaining the array $C[v]$ of integers in $[2, v]$ that are prime or have smallest prime factor exceeding the primes sieved so far, the value read just before sieving out $p$ gives $Phi(floor(n\/p), p) = 1 + C[floor(n\/p)] - pi(p - 1)$. Running a second Lucy pass on prime sums (modulo $10^9$) supplies the large-prime tail. Both passes cost $O(n^(3\/4))$. As checks, $S(100) = 1257$, and the result matches a direct sieve for $n$ up to $10^6$.

#pagebreak()
#link("https://projecteuler.net/problem=522")[= Problem 522: Hilbert's Blackout]

Solution: 96772715

Each of $n$ floors sends power to one other floor ($f(i) != i$); the hotel works iff the functional graph is a single $n$-cycle. $F(n)$ sums, over all $(n-1)^n$ arrangements, the minimum number of rewirings needed; we need $F(12344321) mod 135707531$.

Edges kept from $f$ must form disjoint simple paths, and any linear forest of size $n - r$ extends to an $n$-cycle with $r$ rewirings. At each vertex all but one incoming edge must go, costing $sum_v ("indeg"(v)-1)^+$; each cycle of $f$ must also lose an edge, but in a cyclic component whose cycle carries a tree attachment the in-degree surplus can be spent on a cycle edge for free — only _bare_ cycles cost one extra. Hence min rewirings $= sum_v ("indeg"-1)^+ + \#"bare cycles" - ["f is the" n"-cycle"]$.

Summing over $f$: in-degrees are Binomial$(n-1, 1\/(n-1))$ and $EE[(B-1)^+] = P(B = 0)$, so the first term totals $n(n-1)(n-2)^(n-1)$. A bare cycle on an $ell$-set forbids outsiders from entering it, leaving $(n-ell-1)^(n-ell)$ completions, so the second totals $sum_(ell=2)^n n! \/ (ell (n-ell)!) dot (n-ell-1)^(n-ell)$; the last is $(n-1)!$. The modular sum costs $n$ power evaluations.

Verified against literal minimisation over all target $n$-cycles for every arrangement with $n = 3, 4, 5$ and the given $F(3) = 6$, $F(8) = 16276736$, $F(100) equiv 84326147$.

#pagebreak()
#link("https://projecteuler.net/problem=523")[= Problem 523: First Sort I]

Solution: 37125450.44

The sorting algorithm scans for the first out-of-order adjacent pair and moves the smaller element of that pair to the front, restarting after every move; $E(n)$ is the expected number of moves over a uniformly random permutation of $1..n$.

The key structural fact is that the moves of any element $k$ depend only on the relative order of the elements ${k, k+1, ..., n}$. Moving an element to the front never changes the relative order of the others, and a descent whose smaller member is below $k$ only relocates that smaller element. Moreover, the scan's prefix up to the first descent is increasing, so any element smaller than $k$ in that prefix sits before all the larger ones and never blocks a pair of larger elements from being adjacent. The process therefore acts on the subsequence of elements $>= k$ exactly as it would on that permutation alone, where $k$ is the minimum.

So $E(n) = sum_(m=1)^n h(m)$, where $h(m)$ is the expected number of moves of the *minimum* in a random permutation of size $m$ (element $k$ in $S_n$ behaves as the minimum of a uniform pattern of size $m = n - k + 1$). The per-size contribution is

$ h(m) = (2^(m-1) - 1) / m, $

which the solution verifies by exhaustively running the algorithm over every permutation for all $n <= 8$, and against the given $E(4) = 3.25$ and $E(10) = 115.725$. With exact rational arithmetic, $E(30) = sum_(m=1)^30 (2^(m-1)-1)\/m$ rounds to $37125450.44$.

#pagebreak()
#link("https://projecteuler.net/problem=528")[= Problem 528: Constrained Sums]

Solution: 779027989

$S(n, k, b)$ counts solutions of $x_1 + dots.c + x_k <= n$ with $0 <= x_m <= b^m$; we need $sum_(k=10)^15 S(10^k, k, k) mod 10^9 + 7$.

A slack variable turns the inequality into an equation with $k+1$ nonnegative variables, counted by stars and bars as $binom(n + k, k)$; the upper bounds are removed by inclusion–exclusion over which variables overflow, each overflow at position $m$ shifting $n$ by $b^m + 1$:

$ S(n,k,b) = sum_(T subset.eq [k]) (-1)^(|T|) binom(n - sum_(m in T)(b^m + 1) + k, k), $

with $binom(N, k) = 0$ for $N < k$. At most $2^15$ subsets per evaluation, each binomial a $k$-term falling-factorial product mod $p$.

Verified against literal enumeration for the given $S(14,3,2) = 135$ and $S(200,5,3) = 12949440$, plus the given $S(1000,10,5) equiv 624839075$.

#pagebreak()
#link("https://projecteuler.net/problem=530")[= Problem 530: GCD of Divisors]

Solution: 207366437157977206

With $f(n) = sum_(d | n) gcd(d, n\/d)$ and $F(k) = sum_(n=1)^k f(n)$, we need $F(10^15)$.

Summing $f$ over $n <= N$ is the same as summing $gcd(d, e)$ over every ordered pair with $d e <= N$, since each $n$ contributes exactly its divisor pairs $(d, n\/d)$. Using $gcd(d, e) = sum_(g | d, g | e) phi(g)$ and writing $d = g a$, $e = g b$ (so $d e = g^2 a b$),
$
F(N) = sum_(d e <= N) gcd(d, e) = sum_(g) phi(g) dot \#{(a, b) : a b <= floor(N\/g^2)} = sum_(g^2 <= N) phi(g) D(floor(N\/g^2)),
$
where $D(M) = sum_(a <= M) floor(M\/a)$ is the divisor-summatory function. Each $D(M)$ is evaluated in $O(sqrt(M))$ by the hyperbola method, and a linear $phi$-sieve up to $sqrt(N)$ supplies the totients, for a total cost of about $O(sqrt(N) log N)$. As checks, $F(10) = 32$ and $F(1000) = 12776$.

#pagebreak()
#link("https://projecteuler.net/problem=531")[= Problem 531: Chinese Leftovers]

Solution: 4515432351156203105

Let $g(a, n, b, m)$ be the smallest non-negative $x$ with $x equiv a space (mod n)$ and $x equiv b space (mod m)$, or $0$ if no such $x$ exists, and let $f(n, m) = g(phi(n), n, phi(m), m)$. We need $sum f(n, m)$ over $10^6 <= n < m < 1005000$.

This is a two-modulus Chinese remainder computation that need not assume coprimality. Writing $G = gcd(n, m)$, a solution exists iff $G | (a - b)$, and then it is unique modulo $"lcm"(n, m)$:
$
x = a + n dot (((b - a)\/G) dot (n\/G)^(-1) mod (m\/G)),
$
where the inverse is taken modulo $m\/G$ (which is coprime to $n\/G$). We sieve $phi$ over the small window $[10^6, 1005000)$ and evaluate the roughly $1.25 dot 10^7$ pairs directly, accumulating the smallest solutions. The given values $g(2, 4, 4, 6) = 10$ and $g(3, 4, 4, 6) = 0$ check the congruence solver.

#pagebreak()
#link("https://projecteuler.net/problem=533")[= Problem 533: Minimum Values of the Carmichael Function]

Solution: 789453601

The Carmichael function $lambda(n)$ is the least $m$ with $a^m equiv 1 mod n$ for all $a$ coprime to $n$; $L(n)$ is the least $m$ with $lambda(k) >= n$ for all $k >= m$, so $L(n) - 1$ is the largest $k$ with $lambda(k) < n$. We need $L(20000000) mod 10^9$.

$lambda(k)$ is the lcm of the components $lambda(p^e)$: $p^(e-1)(p-1)$ for odd $p$, and $1, 2, 2^(e-2)$ for $p = 2$ with $e = 1, 2, >= 3$. If $lambda(k) = L_0$ then every component divides $L_0$, so $k <= K(L_0)$, the product of $2^(v_2(L_0)+2)$ (just $2$ for odd $L_0$) and $p^(1+v_p(L_0))$ over odd primes $p$ with $(p-1) | L_0$; conversely $lambda(K(L_0))$ divides $L_0$. Hence $L(n) - 1 = max_(L_0 < n) K(L_0)$.

The $K(L_0)$ are astronomically large, so a sieve accumulates $log K(L_0)$ for all $L_0 < n$: each prime $p$ adds $ln p$ at multiples of $p - 1$ and at multiples of $(p-1)p^j$ for the valuation term, plus one extra $ln 2$ at even $L_0$ — about $n sum_p 1\/(p-1) approx 6.5 dot 10^7$ updates. Distinct huge products can be too close for floating point, so the top 200 candidates by log are recomputed exactly with big integers (factor $L_0$, run over its divisors $d$ with $d + 1$ prime) and the true maximum taken.

Everything is verified against a direct $lambda$ sieve (smallest-prime-factor factorisation, lcm of components, with the given $lambda(8) = 2$ and $lambda(240) = 4$) for $n in {3, 4, 6, 10, 16, 24}$ where $L(n) - 1$ falls inside the $3 dot 10^6$ table, including the given $L(6) = 241$; the given $L(100) = 20174525281$ is asserted too.

#pagebreak()
#link("https://projecteuler.net/problem=535")[= Problem 535: Fractal Sequence]

Solution: 611778217

$S = 1, circle(1), 2, circle(1), 3, circle(2), 4, dots$ is characterised by three properties: the circled numbers are the consecutive integers from 1; each non-circled $a$ is immediately preceded by exactly $floor(sqrt(a))$ circled numbers; and deleting the circled numbers leaves $S$ itself. $T(n)$ sums the first $n$ elements; we need $T(10^18) mod 10^9$.

Writing $Q(n)$ for the sum of $floor(sqrt(S_j))$ over the first $n$ elements, the $i$-th non-circled element closes a prefix of length $i + Q(i)$ containing the circled values $1..Q(i)$ plus the non-circled values $S_1 .. S_i$ — a copy of $S$. So for any $n$, taking the largest $i$ with $i + Q(i) <= n$ and $r = n - i - Q(i)$ (at most the next block length by maximality), the prefix is the circled values $1..m$ with $m = Q(i) + r$ together with $S$'s first $i$ elements:

$ T(n) = m(m+1)/2 + T(i), quad Q(n) = F(m) + Q(i), $

with $F(m) = sum_(k<=m) floor(sqrt(k))$ in closed form. Since every $floor(sqrt(S_j)) >= 1$, $Q(i) >= i$ and the recursion contracts $n$ to about $(3n\/2)^(2\/3)$; locating $i$ is a binary search whose probes evaluate $Q$ one level down, all memoised, so $10^18$ resolves through three levels into a directly generated table of the first $10^6$ elements (the generator bootstraps from $S_1 = 1$ and emits $floor(sqrt(S_i))$ fresh circled integers then $S_i$, the produced prefix always running ahead of the read pointer).

The generated prefix is validated against the 20 given terms and both defining properties, and $T(20) = 86$, $T(10^3) = 364089$ and $T(10^9) = 498676527978348241$ are asserted exactly — the last a particularly strong check of the full recursion.

#pagebreak()
#link("https://projecteuler.net/problem=536")[= Problem 536: Modulo Power Identity]

Solution: 3557005261906288

$S(n)$ sums the $m <= n$ with $a^(m+4) eq.triple a mod m$ for all integers $a$; we need $S(10^12)$.

The property holds exactly when $m$ is squarefree and $(p - 1) | (m + 3)$ for every prime $p | m$ (verified against the literal all-$a$ definition for $m <= 1000$). Indeed the condition splits over prime powers $p^e || m$ by CRT; $a = p$ forces $e = 1$, and for $a$ coprime to $p$ the requirement $a^(m+3) eq.triple 1 mod p$ for all such $a$ is $(p - 1) | (m + 3)$.

Two consequences shape the search. First, $m = 2$ is the only even solution beyond $m = 1$, since an odd $p | m$ would need the even $p - 1$ to divide the odd $m + 3$. Second, writing $m = p s$ gives $m eq.triple s mod (p - 1)$, so the condition reads $(p - 1) | (s + 3)$: every prime factor obeys $p(p - 4) <= m <= n$, i.e. $p < 10^6 + 5$.

The solver runs a depth-first search over the odd prime factors in decreasing order. With chosen primes of product $T$ and $M = "lcm"(p - 1)$, the unknown cofactor $s$ must solve the single congruence $T s eq.triple -3 mod M$ — solvable only if $gcd(T, M) | 3$, which prunes most branches (a chosen prime other than 3 may never divide another chosen prime's $p - 1$). Once the arithmetic progression of possible $s$ up to $n\/T$ is short, every member is checked directly; otherwise the next smaller prime is branched on. $M | m + 3$ also bounds $M <= n + 3$. The search matches a per-$m$ factorisation brute force at $n = 100$, $10^4$ and $10^6$, and finds 12997 solutions up to $10^12$ in about two seconds.

#pagebreak()
#link("https://projecteuler.net/problem=537")[= Problem 537: Counting Tuples]

Solution: 779429131

$T(n, k)$ counts the $k$-tuples of positive integers with $pi(x_1) + dots.c + pi(x_k) = n$; we need $T(20000, 20000) mod 1004535809$.

The number of $x$ with $pi(x) = j$ is $c_0 = 1$ (only $x = 1$) and $c_j = p_(j+1) - p_j$ for $j >= 1$ (the integers from $p_j$ up to just below the next prime). The coordinates are independent, so $T(n, k) = [z^n] f(z)^k$ with $f(z) = sum_j c_j z^j$, and only degrees up to $n$ matter, requiring the primes through $p_(n+1)$.

The power is binary exponentiation of the truncated polynomial. The modulus $1004535809 = 479 dot 2^21 + 1$ is NTT-friendly with primitive root 3 (both facts asserted), so each product of two degree-$<= n$ polynomials is one length-$2^16$ NTT multiplication, alias-free since $2n < 2^16$ — about thirty transforms in total. The given $T(3,3) = 19$, $T(10,10) = 869985$ and $T(10^3, 10^3) eq.triple 578270566$ are asserted, and the NTT path is cross-checked against a direct coordinate-by-coordinate dynamic program on several small cases.

#pagebreak()
#link("https://projecteuler.net/problem=538")[= Problem 538: Maximum Quadrilaterals]

Solution: 22472871503401097

$f(S)$ is the perimeter of the maximum-area quadrilateral with side lengths taken from four distinct positions of $S$ (ties broken by largest perimeter). With $u_n = 2^(B(3n)) + 3^(B(2n)) + B(n+1)$ ($B$ = binary bit count) and $U_n = (u_1, ..., u_n)$, we need $sum f(U_n)$ for $4 <= n <= 3 dot 10^6$.

For fixed sides the maximum area is attained by the cyclic quadrilateral, with Brahmagupta's formula $16 dot "area"^2 = (2s-2a)(2s-2b)(2s-2c)(2s-2d)$ where $2s$ is the perimeter — independent of side order. Increasing any non-maximal side strictly increases the area (the log-derivative $(1\/(s-a) + 1\/(s-b) + 1\/(s-c) - 1\/(s-d))\/2$ is positive since $s-a <= s-d$), so an optimal multiset is always a consecutive window of the values in sorted descending order. A valid window can still lose to a deeper one when its largest side nearly degenerates the quadrilateral, so windows are scanned downward with a rigorous prune: by AM–GM, $16 "area"^2 <= s^4 <= (2 v_j)^4$, so once $(2 v_j)^4$ cannot beat the best product no deeper window can.

The $u_n$ take only about $10^4$ distinct values, so the multiset is kept as counts over a descending distinct-value list, each step lazily expanding just the top few values; areas are compared exactly with integer arithmetic. Verified against literal enumeration of all 4-subsets with exact lexicographic (area, perimeter) comparison for every $n <= 60$, plus the given $f(U_5) = 59$, $f(U_10) = 118$, $f(U_150) = 3223$ and $sum_(n=4)^150 f(U_n) = 234761$.

#pagebreak()
#link("https://projecteuler.net/problem=539")[= Problem 539: Odd Elimination]

Solution: 426334056

From the list $1..n$, every other number is repeatedly deleted, sweeping left to right first, then alternating direction, until one number $P(n)$ remains; we need $S(10^18) mod 987654321$ where $S(n) = sum_(k=1)^n P(k)$.

The first sweep leaves the evens $2, 4, ..., 2 floor(n\/2)$, and the rest of the process is the mirror image of the original process on a list of length $m = floor(n\/2)$: it survives at mirrored position $m + 1 - P(m)$. Hence

$ P(n) = 2(floor(n\/2) + 1 - P(floor(n\/2))), quad P(1) = 1, $

confirmed against direct simulation for $n < 200$ and the given $P(9) = 6$, $P(1000) = 510$.

Summing the recurrence over $k = 2..N$ and grouping $k = 2m$ with $k = 2m + 1$ (both have $floor(k\/2) = m$) gives, with $a = floor(N\/2)$, $b = floor((N-1)\/2)$ and $T(M) = M(M+1)\/2$:

$ S(N) = 1 + 2(N-1) + 2(T(a) + T(b)) - 2(S(a) + S(b)). $

Repeated halving only ever reaches $O(log^2 N)$ distinct arguments, so the memoised recursion is instant. $S(1000) = 268271$ is the check, and the exact $S(10^18)$ is reduced modulo $987654321$ at the end.

#pagebreak()
#link("https://projecteuler.net/problem=540")[= Problem 540: Counting Primitive Pythagorean Triples]

Solution: 500000000002845

$P(n)$ counts primitive Pythagorean triples $a < b < c <= n$. Primitive triples are parametrised bijectively by pairs $(m, k)$ with $m > k >= 1$, $gcd(m, k) = 1$ and $m, k$ of opposite parity, through $c = m^2 + k^2$. So $P(N)$ counts such pairs with $m^2 + k^2 <= N$.

Look at the coprime pairs with $m > k >= 1$ and $m^2 + k^2 <= N$. Being coprime rules out both even, so each is either both-odd or mixed-parity, and the primitive ones are exactly the mixed-parity ones. Therefore $P(N) = C - D$ with $C$ the count of all coprime pairs and $D$ the count of coprime both-odd pairs. Removing the coprimality constraint by Möbius inversion,
$
C = sum_(d) mu(d) T(floor(N\/d^2)), quad D = sum_(d "odd") mu(d) T_"odd"(floor(N\/d^2)),
$
where $T(X) = \#{(a, b) : a > b >= 1, a^2 + b^2 <= X}$ and $T_"odd"$ restricts to both $a, b$ odd. Each of $T$ and $T_"odd"$ is read off a quarter-disc lattice count in $O(sqrt(X))$ (summing $floor(sqrt(X - a^2))$ over $a$), and the Möbius sums need $mu(d)$ for $d <= sqrt(N)$. Checks: $P(20) = 3$ and $P(10^6) = 159139$.

#pagebreak()
#link("https://projecteuler.net/problem=543")[= Problem 543: Prime-Sum Numbers]

Solution: 199007746081234640

$P(n, k) = 1$ when $n$ is a sum of $k$ primes, $S(n) = sum_(1 <= i, k <= n) P(i, k)$, and we need $sum_(k=3)^44 S(F(k))$ over Fibonacci numbers, the largest being $F(44) = 701\,408\,733$.

Classify by $k$. For $k = 1$, the count of valid $i <= n$ is $pi(n)$. For $k = 2$: every even $i >= 4$ works by the Goldbach conjecture (verified computationally far beyond $7 times 10^8$), while an odd $i$ is a sum of two primes only as $2 + (i - 2)$, i.e. iff $i - 2$ is prime; the count is $floor(n\/2) - 1 + pi(n - 2) - 1$. For $k >= 3$ the answer depends only on the size $i >= 2k$: if $i$ is even, write $i = 2(k - 2) + m$ with even $m >= 4$ and apply Goldbach; if $i$ is odd (so $i >= 2k + 1$), write $i = 2(k - 3) + m$ with odd $m >= 7$, a sum of three primes by the weak Goldbach theorem (proven by Helfgott). So each $k >= 3$ contributes $n - 2k + 1$ for $2k <= n$, a quadratic closed form. Hand checks: $S(10) = 20$, $S(100) = 2402$.

The only computational work is $pi(F(k))$ and $pi(F(k) - 2)$ for each $k$, obtained in one pass of a segmented sieve up to $F(44)$, recording the running prime count at the 84 required thresholds. $S(1000) = 248838$ is asserted as well.

#pagebreak()
#link("https://projecteuler.net/problem=544")[= Problem 544: Chromatic Conundrum]

Solution: 640432376

$F(r, c, n)$ counts proper $n$-colourings of the $r times c$ grid graph and $S(r, c, n) = sum_(k=1)^n F(r, c, k)$; we need $S(9, 10, 1112131415) mod 10^9 + 7$.

$F(9, 10, k)$ is the grid's chromatic polynomial, of degree 90 in $k$, so $S(9, 10, n)$ is a degree-91 polynomial in $n$: evaluating $F$ at $k = 0..91$ determines $S$ at $n = 0..91$, and Lagrange interpolation gives $S$ at the target.

Each evaluation uses a broken-profile DP whose state is the colour-equality partition of the 9 frontier cells: a new cell must differ only from its two neighbours, both of which sit on the frontier, so its colour either joins one of the $b$ frontier blocks other than the neighbours' (weight 1 each) or is any colour absent from the frontier (weight $k - b$ — previously used but dropped colours are interchangeable with fresh ones). Vertical adjacency keeps the reachable partitions to 5017, far below $B_9 = 21147$, and the 90-step unrolled transition structure is built once and reused for all 92 values of $k$.

Verified against literal enumeration of all colourings for small grids, the given $F(2,2,3) = 18$, $F(2,2,20) = 130340$, $F(3,4,6) = 102923670$ and $S(4,4,15) equiv 325951319$, plus a self-check that interpolating the $S$ table at points inside the sample range reproduces the table.

#pagebreak()
#link("https://projecteuler.net/problem=545")[= Problem 545: Faulhaber's Formulas]

Solution: 921107572

$D(k)$ is the denominator of the coefficient $a_1$ of $n^1$ in the Faulhaber polynomial for $1^k + 2^k + dots.c + n^k$; we need the $10^5$-th $k$ with $D(k) = 20010$.

By Faulhaber's formula the coefficient of $n^1$ is exactly the Bernoulli number $B_k$ (with the $B_1 = +1\/2$ convention), and the von Staudt–Clausen theorem states that for even $k >= 2$ the denominator of $B_k$ is the product of all primes $p$ with $(p - 1) | k$. Both facts are verified in the code: $a_1$ is recovered by exact linear algebra through the first $k + 1$ partial sums and compared against the Bernoulli recurrence for $k <= 12$, and the denominator product is checked for all even $k <= 60$ (plus $D(308) = 20010$ exactly).

Since $20010 = 2 dot 3 dot 5 dot 23 dot 29$, $D(k) = 20010$ means $(p - 1) | k$ for exactly these five primes: $k$ must be divisible by $"lcm"(1, 2, 4, 22, 28) = 308$, and no divisor $d$ of $k$ outside ${1, 2, 4, 22, 28}$ may have $d + 1$ prime.

Writing $k = 308 m$, a prime $p$ with $d = p - 1$ rules out exactly the $m$ divisible by $d \/ gcd(d, 308)$. All primes $p < 10^5$ are removed in one sieve over $m$, which kills the vast majority of candidates. Each survivor's $k$ is then factorised (a smallest-prime-factor sieve over $m$ plus $308 = 2^2 dot 7 dot 11$) and its few divisors $d >= 10^5$ are tested with Miller–Rabin on $d + 1$. The given $F(1) = 308$ and $F(10) = 96404$ are asserted before counting up to the $10^5$-th survivor.

#pagebreak()
#link("https://projecteuler.net/problem=546")[= Problem 546: The Floor's Revenge]

Solution: 215656873

$f_k (0) = 1$ and $f_k (n) = sum_(i=0)^n f_k (floor(i\/k))$; we need $sum_(k=2)^10 f_k (10^14) mod 10^9 + 7$.

Differencing consecutive values telescopes the definition to $f(n) = f(n-1) + f(floor(n\/k))$. Define the iterated strict-prefix sums $T_0 = f$ and $T_t (m) = sum_(q<m) T_(t-1)(q)$. Writing $n = m k + s$,

$ f(n) = (s+1) f(m) + k thin T_1 (m), $

and summing such expressions over a full block of $k$ children turns each $T_t (m)$ into $T_(t+1)(m)$ while the partial block contributes prefix sums over $s < r$: so every $T_t (n)$ is a linear combination of $f(m), T_1 (m), ..., T_(t+1)(m)$ with coefficients depending only on the digit $r = n mod k$. The coefficient tables are built iteratively (numeric mod $p$, per residue), and the vector $(f, T_1, ..., T_D)$ is propagated up the base-$k$ digit chain of $10^14$ from the base case $f(0) = 1$, $T_t (0) = 0$, with $D$ bounded by the chain length (at most 49 for $k = 2$) since each level references one more sum order. The whole computation is a few thousand modular operations.

Verified against the direct recurrence with exact integers for the given $f_5 (10) = 18$, $f_7 (100) = 1003$, $f_2 (10^3) = 264830889564$, and for 30 random $n <= 5000$ for every $k in 2..10$.

#pagebreak()
#link("https://projecteuler.net/problem=548")[= Problem 548: Gozinta Chains]

Solution: 12144044603581281

A gozinta chain for $n$ is $\{1, a, b, dots, n\}$ with each element properly dividing the next, $g(n)$ counts them, and we sum the $n <= 10^16$ with $g(n) = n$.

A chain is determined by its sequence of successive ratios, all greater than 1, so $g$ counts ordered factorisations: $g(n) = sum_(d | n, d < n) g(d)$ with $g(1) = 1$. In particular $g$ depends only on $n$'s prime signature (the multiset of exponents).

The search enumerates every canonical signature $E$ (descending exponents) whose minimal realisation $2^(e_1) 3^(e_2) dots.c$ is at most $10^16$ — the 17563 members of A025487 up to that bound. $g(E)$ is the memoised sum of $g$ over all proper sub-vectors of the exponent lattice; processing signatures in increasing minimal-realisation order guarantees every canonicalised sub-vector is already known. Since $g$ is monotone under sub-vectors, saturating the arithmetic at a cap above $10^16$ avoids 64-bit overflow while keeping every value at most $10^16$ exact. A signature $E$ then yields a solution $v = g(E)$ exactly when $v <= 10^16$ and $v$'s own signature is $E$; factoring $v$ needs only primes up to $10^6$, the leftover cofactor being $1$, a prime, a prime squared, or a product of two distinct large primes (a square test plus one Miller–Rabin call).

There are 21 solutions, from $n = 1$ and $g(48) = 48$ up to $5806013294837760$. The method is cross-checked against the direct sieve recurrence for all $n <= 10^6$, which yields exactly $\{1, 48, 1280, 2496, 28672, 29808, 454656\}$.

#pagebreak()
#link("https://projecteuler.net/problem=549")[= Problem 549: Divisibility of Factorials]

Solution: 476001479068717

Let $s(n)$ be the smallest $m$ with $n | m!$, and $S(n) = sum_(i=2)^n s(i)$; we need $S(10^8)$.

Writing $n = product p^e$, the factorial $m!$ must absorb each prime power independently, and the binding requirement is the largest, so $s(n) = max_(p^e || n) s(p^e)$. For a single prime power, $s(p^e)$ is the smallest multiple $m$ of $p$ at which $v_p(m!)$ reaches $e$ (the exponent $v_p(m!)$ only grows as $m$ passes multiples of $p$).

This gives a single modified sieve. A slot still holding $0$ marks a prime $p$; walking $m = p, 2p, 3p, dots$ and accumulating $c = v_p(m!)$, each time $c$ climbs past an integer $k$ the value $s(p^k)$ equals the current $m$, so we raise $s[j]$ to $m$ for every multiple $j$ of $p^k$. Composite slots are filled in by their smallest prime before they are reached, exactly as in the sieve of Eratosthenes, and summing the array yields $S(N)$. The total update work is $sum_p sum_k N\/p^k = O(N log log N)$. As a check, $S(100) = 2012$.

#pagebreak()
#link("https://projecteuler.net/problem=550")[= Problem 550: Divisor Game]

Solution: 328104836

Two players face $k$ piles of $2..n$ stones; a move replaces a pile of $m$ stones with two piles $a, b$ where $1 < a, b < m$ and $a | m$, $b | m$, and whoever cannot move loses. $f(n, k)$ counts the first-player-winning ordered starting tuples; we need $f(10^7, 10^12) mod 987654321$.

By Sprague–Grundy theory the piles are independent games: a position wins exactly when the XOR of the pile Grundy values $g(m) = "mex"{g(a) xor g(b)}$ is nonzero. Since a move never mixes piles and divisors correspond to exponent sub-vectors, $g$ depends only on $m$'s prime signature — a few hundred signatures below $10^7$ — so the Grundy table is computed once per signature and every $m <= 10^7$ is routed through a smallest-prime-factor sieve to produce the counts $c_v = \#{m : g(m) = v}$.

Counting XOR-zero $k$-tuples is a $k$-fold XOR convolution: with $W$ the Walsh–Hadamard transform of $c$,

$ f(n, k) = (n-1)^k - 1/"size" sum_i W_i^k mod 987654321, $

dividing by the modular inverse of the power of two (the modulus is odd, and being composite it requires a general inverse rather than a Fermat power). Verified against the direct Grundy recursion for all $m <= 5000$, a brute-force tuple DP for small $(n, k)$, and the given $f(10, 5) = 40085$.

#pagebreak()
#link("https://projecteuler.net/problem=551")[= Problem 551: Sum of Digits Sequence]

Solution: 73597483551591773

$a_0 = 1$ and $a_n$ is the sum of the digits of all preceding terms, which collapses to $a_n = a_(n-1) + "digitsum"(a_(n-1))$ for $n >= 2$, since the running digit total is exactly the previous term. We need $a_(10^15)$.

The walk is memoryless given the current value, and while the digits above position $k$ stay fixed, the low $k$ digits evolve in a way that depends only on the pair (block value $L$, digit sum $h$ of the high part). Define $"jump"(k, L, h)$ as the number of steps until the low-$k$ block overflows together with the block's value after the carry; a single step adds at most $"digitsum"(v) < 1000$, so for $k >= 3$ the overflow is a single carry and the jump is well defined. The base level $k = 3$ is simulated directly, and level $k$ peels the top digit $d$ of the block and chains ten level-$(k-1)$ jumps with high sum $h + d$. Memoised on $(k, L, h)$, the table stays around 8000 entries because exit values recur — the driver then applies the largest jump fitting the remaining step budget and finishes with single steps. Verified against direct simulation up to the given $a_(10^6) = 31054319$.

#pagebreak()
#link("https://projecteuler.net/problem=552")[= Problem 552: Chinese Leftovers II]

Solution: 326227335

$A_n$ is the smallest positive integer with $A_n mod p_i = i$ for $1 <= i <= n$; $S(n)$ sums the primes up to $n$ dividing at least one $A_k$, and we need $S(300000)$.

Incremental CRT: with $M_n = p_1 dots.c p_n$, the minimal solution grows as $A_n = A_(n-1) + t M_(n-1)$ where $t = (n - A_(n-1)) M_(n-1)^(-1) mod p_n$; inductively $1 <= A_n <= M_n$, so this is the smallest positive solution.

The crucial observation: once $p_j$ enters the system, $A_n eq.triple j mod p_j$ with $0 < j < p_j$, so $p_j$ never divides any later term — only the $n < j$ matter, a finite window per prime. We therefore track $A_n mod p_j$ and $M_n mod p_j$ for every prime index $j > n$ and update both in $O(1)$ per pair, marking $p_j$ whenever its residue hits zero: about $pi(300000)^2 \/ 2 approx 3.4 times 10^8$ operations. The recurrence is cross-checked against exact big-integer CRT on the given $A_2 = 5$, $A_3 = 23$, $A_4 = 53$, $A_5 = 1523$, $A_10 = 5765999453$, and $S(50) = 69$ is asserted.

#pagebreak()
#link("https://projecteuler.net/problem=553")[= Problem 553: Power Sets of Power Sets]

Solution: 57717170

$R(n)$ is the set of non-empty families of non-empty subsets of ${1..n}$; each family $X$ gets a graph with the member sets as vertices and edges between intersecting sets. $C(n, k)$ counts families whose graph has exactly $k$ connected components; we need $C(10^4, 10) mod 10^9 + 7$.

Sets in different components are pairwise disjoint, so the components' supports partition the union of $X$. With $U(m)$ the number of non-empty families of subsets of $[m]$ with union exactly $[m]$, inclusion-exclusion over the union gives $U(m) = sum_j (-1)^(m-j) binom(m, j) 2^(2^j - 1)$ (the empty family cancels), and in exponential generating functions $U = e^A - 1$ where $A$ is the EGF of _connected_ full-support families, so $A = log(1 + U)$. Splitting $[n]$ into unused elements, the support, and a partition of the support into $k$ connected blocks:

$ C(n, k) = sum_m binom(n, m) thin m! thin [x^m] A(x)^k / k! . $

Everything is $O(n^2)$ arithmetic mod $p$: the inclusion-exclusion table (with $2^(2^j - 1)$ reduced via Fermat), the power-series logarithm recurrence $m a_m = m u_m - sum_i i thin a_i u_(m-i)$, and five length-$10^4$ convolutions for $A^10$ by binary exponentiation. Verified against literal enumeration of all families with union-find component counting for $n <= 4$ (including the given $C(2,1) = 6$, $C(3,1) = 111$, $C(4,2) = 486$) and the given $C(100, 10) equiv 728209718$.

#pagebreak()
#link("https://projecteuler.net/problem=554")[= Problem 554: Centaurs on a Chess Board]

Solution: 89539872

A centaur moves like a king or a knight. At most $n^2$ non-attacking centaurs fit on a $2n times 2n$ board; $C(n)$ counts the maximum placements. We need $sum_(i=2)^90 C(F_i) mod 10^8 + 7$ with $F_90 approx 2.9 dot 10^18$.

Maximality forces structure: kings alone limit each $2 times 2$ block to one piece, so a maximum placement chooses one corner $(a, b) in {0,1}^2$ per block of the $n times n$ block grid, and only adjacent (including diagonal) blocks interact. Translating the king + knight attack set into block coordinates: along each row the $b$'s must be non-decreasing with $a$ constant wherever $b$ stays constant (and symmetrically for columns); the diagonals add three forbidden patterns each. Consequently every valid row is determined by (threshold, $a$-left, $a$-right) — exactly $4n$ rows, verified exhaustively against all $4^n$ cell rows for $n <= 6$ — and $C(n)$ is a path count in a $4n$-state row-transfer graph, cross-checked against a literal $4^(n+1)$-state sliding-window DP over blocks for $n <= 8$ and the given $C(1) = 4$, $C(2) = 25$, $C(10) = 1477721$.

The transfer values for $n = 1..40$ reveal and verify the closed form

$ C(n) = 8 binom(2n, n) - 3n^2 - 2n - 7, $

(the correction has constant second differences), whose binomial term is evaluated at Fibonacci arguments by Lucas' theorem over $p = 10^8 + 7$ with a precomputed factorial table — since $2 F_90 < p^3$, at most three base-$p$ digits per evaluation.

#pagebreak()
#link("https://projecteuler.net/problem=555")[= Problem 555: McCarthy 91 Function]

Solution: 208517717451208352

The generalised McCarthy function is $M_(m,k,s)(n) = n - s$ for $n > m$ and $M(M(n + k))$ otherwise; $"SF"(m,k,s)$ sums its fixed points and $S(p, m) = sum_(1 <= s < k <= p) "SF"(m,k,s)$. We need $S(10^6, 10^6)$.

Let $d = k - s > 0$. For $n in (m - k, m]$ we have $M(n) = M(M(n+k)) = M(n + k - s) = M(n + d)$: the function is $d$-periodic just below $m$, with values in $(m - s, m - s + d]$. The periodicity propagates to all $n <= m$ exactly when $d | s$; then $M$ sends every $n <= m$ to the unique element of $[m - s + 1, m - s + d]$ congruent to $n$ modulo $d$, so the fixed points are precisely the non-negative integers of that interval, and there are none at all when $d divides.not s$. This characterisation is verified exhaustively against the literal recursive definition for several $m$ and every $1 <= s < k <= 3m + 2$ (covering the clipping at zero when $s > m$).

For $p <= m + 1$ no clipping occurs, so with $s = d t$, $k = d(t + 1)$:

$ S(p, m) = sum_(d >= 1) sum_(t = 1)^(floor(p\/d) - 1) (d(m - d t) + d(d+1)/2), $

whose inner sum has a closed form, leaving one $O(p)$ loop over $d$. The given $S(10, 10) = 225$ and $S(1000, 1000) = 208724467$ are asserted.

#pagebreak()
#link("https://projecteuler.net/problem=556")[= Problem 556: Squarefree Gaussian Integers]

Solution: 52126939292957

A proper Gaussian integer has $a > 0$, $b >= 0$; it is squarefree if its factorization into proper Gaussian primes has no repeats. $f(n)$ counts proper squarefree Gaussian integers of norm at most $n$; we need $f(10^14)$.

Möbius inversion over $ZZ[i]$: $[z "squarefree"] = sum_(d^2 | z) mu_G (d)$ over proper $d$, so $f(n) = sum_k m(k) thin G(floor(n \/ k^2))$ where $G(M)$ counts proper Gaussian integers of norm in $[1, M]$ — one quarter of the nonzero circle-lattice count, $G(M) = floor(sqrt(M)) + sum_(x=1)^(floor(sqrt(M))) floor(sqrt(M - x^2))$ — and $m(k) = sum_(N(d) = k) mu_G (d)$. Since $sum m(k) k^(-s) = 1 \/ zeta_(QQ(i))(s)$, $m$ is multiplicative with $m(2) = -1$ (ramified), $m(p) = -2$ and $m(p^2) = 1$ for $p equiv 1 mod 4$ (split), $m(p^2) = -1$ for $p equiv 3 mod 4$ (inert: no norm-$p$ elements), and 0 at all other prime powers. $m$ is built by a linear sieve to $k <= 10^7$, and the $G$ evaluations cost $sqrt(n) thin H(10^7) approx 1.6 dot 10^8$ integer square roots.

Verified against a literal brute force for $n <= 300$ — testing divisibility of each proper $z$ by $d^2$ over all proper $d$ — and the given $f(10) = 7$, $f(10^2) = 54$, $f(10^4) = 5218$, $f(10^8) = 52126906$.

#pagebreak()
#link("https://projecteuler.net/problem=557")[= Problem 557: Cutting Triangles]

Solution: 2699929328

A triangle is cut by two cevians, one from each of two vertices to the opposite side, into four integer-area pieces: $a$ (the triangle between the two cut vertices), $b <= c$ (the other two triangles) and $d$ (the quadrilateral). $S(n)$ sums the total area over all valid quadruples with $a + b + c + d <= n$; we need $S(10^4)$.

With cevian feet at fractions $e, f$ along the sides, barycentric coordinates of their intersection give $a\/T = (1-e)(1-f)\/(1-e f)$, $b\/T = e(1-f)^2\/(1-e f)$, $c\/T = f(1-e)^2\/(1-e f)$ for total $T$. From $a + b = (1-f)T$ and $a + c = (1-e)T$ — so $e = (b+d)\/T$ and $f = (c+d)\/T$ — substituting back collapses the whole geometry into a single relation:

$ 1/(a+b) + 1/(a+c) = 1/a + 1/T, $

equivalently $T(a^2 - b c) = a(a+b)(a+c)$, with $d = b c(2a+b+c)\/(a^2 - b c)$ automatically a positive integer whenever $T$ is integral. Conversely any quadruple satisfying it has $e, f in (0,1)$ reconstructing exactly those areas (checked with exact rationals for every quadruple with $T <= 60$), so the relation is the full characterisation.

For fixed $a, b$ the value $T$ is monotone increasing in $c$, so $T <= n$ bounds $c <= a^2(n-a-b)\/(a^2+a b+n b)$; the resulting triple loop with a divisibility test runs about $2 dot 10^10$ iterations, parallelised over $a$. Verified against literal quadruple-loop brute force at $n = 100$, the given $S(20) = 259$, and the two given quadruples $(22,8,11,14)$ and $(20,2,24,9)$ being exactly the solutions of total 55.

#pagebreak()
#link("https://projecteuler.net/problem=558")[= Problem 558: Irrational Base]

Solution: 226754889

$r$ is the real root of $x^3 = x^2 + 1$. Every positive integer has a unique finite representation $n = sum b_k r^k$ with $b_k in {0, 1}$ and any two used exponents differing by at least 3; $w(n)$ counts the terms. We need $S(m) = sum_(j=1)^m w(j^2)$ for $m = 5 dot 10^6$.

Greedy works and is forced: with gap-3 representations the supremum of values with top exponent $m$ is the geometric sum $r^m \/ (1 - r^(-3)) = r^(m+1)$ _exactly_ (since $r^3 - 1 = r^2$), approached but never attained by finite sums — so the top exponent must be the largest $k$ with $r^k <= x$, and the remainder satisfies $x - r^k < r^k (r - 1) = r^(k-2)$ because $r - 1 = r^(-2)$ exactly, forcing the next exponent down by at least 3 automatically.

Exactness: $x$ is tracked as an integer scaled by $2^400$ against precomputed rounded powers. Accumulated rounding is tiny, but when a remainder is _exactly_ a power, an underestimate sends the greedy into an infinite $r^t = r^(t-1) + r^(t-4) + dots$ descent; comparing with a slack of $2^64$ fixes this and is sound because distinct elements of the lattice $ZZ + ZZ r + ZZ r^2$ at the coefficient sizes occurring here differ by far more than $2^(-336)$. Termination is $X < 2^70$, with genuine remaining terms at least $r^(-130) 2^400 approx 2^330$.

Each representation is independently verified for $j <= 1500$ (and the given examples for 3 and 10) by summing the exact coordinate triples of $r^k$ in $ZZ[r]$ — multiplication by $r$ maps $(a, b, c)$ to $(c, a, b+c)$ — and checking the total equals $(n, 0, 0)$, plus the gap condition. The given $S(10) = 61$ and $S(1000) = 19403$ are asserted.

#pagebreak()
#link("https://projecteuler.net/problem=559")[= Problem 559: Permuted Matrices]

Solution: 684724920

$P(k, r, n)$ counts $r times n$ matrices whose rows are permutations of ${1..n}$ and where a column ascent (every row increasing from column $j$ to $j+1$) occurs exactly at the columns $j < n$ not divisible by $k$. $Q(n) = sum_(k=1)^n P(k, n, n)$; we need $Q(50000) mod 1000000123$.

The columns split into $m = ceil(n\/k)$ base blocks of length $k$ (last block of length $ell = n - (m-1)k$); within blocks all rows ascend, and each boundary must fail to ascend in some row. Inclusion-exclusion over boundaries relaxed to "all ascend" merges consecutive blocks: a matrix where every row ascends within prescribed blocks of sizes $c_i$ is counted by $(n! \/ product c_i !)^r$, so

$ P(k, r, n) = (n!)^r sum_("compositions" (a_1..a_s) "of" m) (-1)^(m-s) product_(i<s) ((a_i k)!)^(-r) dot (((a_s - 1)k + ell)!)^(-r). $

A linear DP over the number of consumed regular blocks computes the signed composition sum in $O((n\/k)^2)$, and summing over $k$ costs $sum_k (n\/k)^2 approx zeta(2) n^2 approx 4 dot 10^9$ multiply-adds for $n = 50000$, with the $((a k)!)^(-n)$ weights as modular powers of precomputed inverse factorials.

Verified against literal enumeration of all $r$-tuples of permutations for six small $(k, r, n)$, exact rational evaluation of the given $P(1,2,3) = 19$, $P(2,4,6) = 65508751$ and $Q(5) = 21879393751$, and the given modular values $P(7,5,30) equiv 161858102$ and $Q(50) equiv 819573537$.

#pagebreak()
#link("https://projecteuler.net/problem=560")[= Problem 560: Coprime Nim]

Solution: 994345168

In Coprime Nim a move removes $y$ stones from a pile of $m$ only when $gcd(m, y) = 1$, last stone wins; $L(n, k)$ counts the losing starting positions over $k$ piles of $1..n-1$ stones, and we need $L(10^7, 10^7) mod 10^9 + 7$.

The Grundy values have a striking form, verified against the literal mex recursion for all $m <= 2000$: $g(m) = 0$ for even $m$, $g(1) = 1$, and $g(m) = pi("spf"(m))$ for odd $m >= 3$ — the index of the smallest prime factor. From an even pile every legal removal is odd, landing only on odd positions of positive Grundy value, so even piles lose; from an odd pile the reachable set is exactly ${0, dots, pi("spf"(m)) - 1}$.

A position loses iff its pile values XOR to zero, so $L(n, k)$ is the XOR-zero count of a $k$-fold XOR convolution. One smallest-prime-factor sieve produces the value counts ($c_0$ the evens, $c_1 = 1$ for the lone pile of one stone, and $c_(pi(p))$ the odd numbers with smallest factor $p$), and with $W$ the Walsh–Hadamard transform of $c$ over length $2^20$ (covering the largest prime index below $10^7$), $L = 2^(-20) sum_i W_i^k mod 10^9 + 7$. All three given values $L(5,2) = 6$, $L(10,5) = 9964$, $L(10,10) = 472400303$ and $L(10^3, 10^3) = 954021836$ are asserted, the first two also by direct enumeration.

#pagebreak()
#link("https://projecteuler.net/problem=561")[= Problem 561: Divisor Pairs]

Solution: 452480999988235494

$S(n)$ counts pairs $(a, b)$ of distinct divisors of $n$ with $a | b$; $E(m, n)$ is the 2-adic valuation of $S((p_m\#)^n)$, and $Q(n) = sum_(i=1)^n E(904961, i)$. We need $Q(10^12)$.

Chains $a | b | n$ choose exponents $0 <= x_i <= y_i <= e_i$ independently per prime, so $S(n) = product (e_i+1)(e_i+2)\/2 - product (e_i+1)$. For $(p_m\#)^i$ all exponents equal $i$, giving $S = A^m - B^m$ with $B = i + 1$ and $A = (i+1)(i+2)\/2$. Writing $k = i + 1$ and using that $m = 904961$ is odd, the valuation splits by $k mod 4$: for $k eq.triple 1$, $E = v_2(k - 1) - 1$ (the cofactor of $u - 1$ in $u^m - 1$ is odd for odd $m$); for $k eq.triple 0$, $v_2(A) = v_2(k) - 1 < v_2(B)$ gives $E = m(v_2(k) - 1)$; and $E = 0$ for $k eq.triple 2, 3$. The case formula is checked against direct big-integer valuations — exhaustively for several small odd $m$, and for $m = 904961$ itself against million-digit powers at small $i$.

Summing the two surviving cases over $k$ telescopes into floor sums:

$ Q(n) = m sum_(j >= 2) floor((n+1)/2^j) + sum_(j >= 2) floor(n/2^j), $

verified term-by-term for several $n$ and against the given $Q(8) = 2714886$.

#pagebreak()
#link("https://projecteuler.net/problem=562")[= Problem 562: Maximal Perimeter]

Solution: 51208732914368

Among triangles with lattice vertices inside or on the circle of radius $r$ that contain no other lattice point (inside or on edges), take the one of maximum perimeter; $T(r)$ is its circumradius over $r$. We need $T(10^7)$ rounded to the nearest integer.

By Pick's theorem an empty lattice triangle has area $1\/2$, so with longest side $v = B - A$ (primitive) the third vertex satisfies $"cross"(v, C - A) = plus.minus 1$: $C$ lies on one of the two lattice lines adjacent to $A B$, at position $s = (C - A) dot v$ with $s$ fixed modulo $v^2$ ($s equiv v_y v_x^(-1)$). Then $|C A|^2 = (s^2+1)\/v^2$, $|C B|^2 = ((v^2-s)^2+1)\/v^2$, the circumradius is $R = sqrt((s^2+1)((v^2-s)^2+1)) \/ (2|v|)$ (from $R = a b c\/(4K)$, $K = 1\/2$), and the perimeter is $P = |v| + (sqrt(s^2+1) + sqrt((v^2-s)^2+1))\/|v| = 2|v| + O(1\/v^2)$ because a lattice $C$ forces $s >= sqrt(v^2 - 1)$. Consecutive achievable $|v|$ differ by at least $1\/(2|v|) >> 1\/v^2$, so the maximum perimeter first maximises $N = v^2$ over feasible placements, then within equal $N$ minimises $min(s, N - s)$.

Feasibility of $v$ needs a lattice $A$ with $A$, $A + v$, $A + p$ all in the disk. Since $|A + v\/2|^2 <= r^2 - N\/4$, valid $A$ lie in a disk of radius $sqrt(4r^2 - N)\/2$ around $-v\/2$, so each test scans only $approx sqrt("gap")$ columns. All primitive vectors with $N$ in a window below $4r^2$ (four sign/line variants each) are tested in decreasing $N$; the winner at $r = 10^7$ has gap $4r^2 - N = 2718$, far inside the $2 dot 10^5$ window. $T = sqrt(X \/ (4 r^2 N))$ with $X = (s^2+1)((N-s)^2+1)$ is rounded by exact integer comparison. Verified against a literal maximum-perimeter brute force over all empty triangles for $r = 10$ and the given $T(10) approx 97.26729$, $T(100) approx 9157.64707$.

#pagebreak()
#link("https://projecteuler.net/problem=563")[= Problem 563: Robot Welders]

Solution: 27186308211734760

Robots weld up to 25 identical rectangles along an edge, starting from unit squares, so a sheet $a times b$ is constructible exactly when both sides are 23-smooth (every factor in $2..25$ splits into primes up to 23). A variant of area $A$ is a pair $(s, l)$ of 23-smooth sides with $s <= l <= 1.1 s$ and $s l = A$; $M(n)$ is the least area with exactly $n$ variants, and we need $sum_(n=2)^100 M(n)$.

All 23-smooth numbers up to $B = 10^8$ (63768 of them) are generated by depth-first search, and a two-pointer sweep lists every pair with $10 l <= 11 s$ — about $6.8 times 10^7$ products. For any area $A <= B^2$ the short side obeys $s <= sqrt(A) <= B$, so every variant of such an area is captured and its count is exact. Sorting the products and taking the first area attaining each count gives $M(n)$; every $n in [2, 100]$ is realised and the largest value, $M(100) approx 2.3 times 10^15$, sits a factor four below the completeness boundary $B^2 = 10^16$. The table is cross-checked against an independent run at $B = 10^7$, and the given $M(3) = 889200$ — with its variants $900 times 988$, $912 times 975$, $936 times 950$ — is confirmed by a direct divisor scan.

#pagebreak()
#link("https://projecteuler.net/problem=564")[= Problem 564: Maximal Polygons]

Solution: 12363.698850

A segment of length $2n-3$ is split uniformly at random into one of the $binom(2n-4, n-1)$ ordered sequences of $n$ positive integer parts, which become consecutive sides of the maximal-area convex $n$-gon. $E(n)$ is the expected area; we need $S(50) = sum_(n=3)^50 E(n)$ to 6 decimals.

The maximal-area polygon with given sides is the cyclic one, and its area does not depend on the side order, so $E(n)$ collapses to a sum over partitions of $2n-3$ into $n$ parts — at most $p(47) = 124754$ of them for $n = 50$ — each weighted by its number of arrangements $n! \/ product("multiplicities"!)$ over the binomial total.

For each side multiset the circumradius solves $sum_i 2 arcsin(s_i \/ 2R) = 2pi$ when the centre is inside the polygon (the left side is decreasing in $R$, and its sign at $R = s_max \/ 2$ decides the case); otherwise the centre lies beyond the longest side and $R$ solves $arcsin(s_max \/ 2R) = sum_(i != max) arcsin(s_i \/ 2R)$, with the longest side's triangle counted negatively in $A = sum plus.minus (R^2\/2) sin(2 arcsin(s_i \/ 2R))$. A root always exists since $s_max <$ the sum of the rest (the largest of $n$ parts of $2n-3$ is at most $n-2 < n-1$). Bisection to $approx 10^(-15)$ relative accuracy over all 320k partitions gives $S(50)$ far beyond the required precision. The given $E(3) = 0.433013$, $E(4) = 1.299038$, $S(5) = 4.604767$ and $S(10) = 66.955511$ are asserted.

#pagebreak()
#link("https://projecteuler.net/problem=565")[= Problem 565: Divisibility of Sum of Divisors]

Solution: 2992480851924313898

We sum the $n <= 10^11$ with $sigma(n) eq.triple 0 mod 2017$. Since $sigma$ is multiplicative, and $2017$ is prime, $2017 | sigma(n)$ exactly when some exact prime-power component $p^e || n$ has $2017 | sigma(p^e)$. Call such $p^e$ *special*.

Finding the special prime powers: for $e = 1$, $sigma(p) = p + 1$, so $p eq.triple -1 mod 2017$. The candidates $2017k - 1 <= 10^11$ are sieved by every prime up to $sqrt(10^11) approx 316228$ (striking an arithmetic progression of $k$ for each small prime), which leaves exactly the special primes — no primality testing needed. For $e >= 2$, only $p <= 10^(11\/e)$ matter, so all $sigma(p^e) mod 2017$ are checked directly over the primes up to $316228$.

The smallest special value is $12101$, so $n$ can contain at most two special components ($12101^3 > 10^11$). By inclusion–exclusion, with $T(M) = M(M+1)\/2$:

$ S = sum_(q = p^e "special") q (T(M) - p T(floor(M\/p)))_(M = floor(N\/q)) - sum_(q_1 q_2 <= N) q_1 q_2 sum_(m <= N\/(q_1 q_2), p_1 divides.not m, p_2 divides.not m) m, $

where the single terms sum $q m$ over $m$ coprime to $p$ (so that the $p$-component of $n = q m$ is exactly $q$), and the pair terms remove the double count of $n$ containing two special components, computed with the analogous two-prime exclusion. Only special $q_1 < sqrt(N)$ can appear in a pair, so the pair sum is tiny. All arithmetic uses exact Python integers. $S(20, 7) = 49$, $S(10^6, 2017) = 150850429$ and $S(10^9, 2017) = 249652238344557$ are the checks.

#pagebreak()
#link("https://projecteuler.net/problem=567")[= Problem 567: Reciprocal Games I]

Solution: 75.44817535

Each of $n$ turns picks $k$ uniformly from $1..n$ with prize $1\/k$. In game A a generator turns each of $n$ lights on with probability $1\/2$ and Jerry wins $1\/k$ if exactly $k$ light up; in game B Tom and Jerry each draw a uniformly random $k$-subset and Jerry wins on a match. Over $n$ turns, $J_A(n) = 2^(-n) sum_k binom(n, k)\/k$ and $J_B(n) = sum_k 1\/(k binom(n, k))$; we need $S(m) = sum_(n<=m)(J_A(n) + J_B(n))$ for $m = 123456789$ to 8 decimal places.

The identity $sum_k binom(n,k)\/k = sum_j (2^j - 1)\/j$ (verified exactly for $n < 200$) telescopes the $J_A$ sum to $2H_m - 2 sum_(j<=m) 2^(-j)\/j - E(m)$, where $E(m)$ keeps only the $tilde 200$ top terms. The $J_B$ terms decay super-polynomially away from the edges $k = 1, 2, dots$ and $k = n, n-1, dots$, so Kahan-compensated 60-wide edge windows are exact to double precision up to $N_0 = 10^6$, beyond which $J_B(n) = 2\/n + 2\/(n(n-1)) + 4\/(n(n-1)(n-2)) + O(1\/n^4)$ telescopes in closed form with tail error below $10^(-17)$. $H_m$ uses Euler–Maclaurin. The given $J_A(6)$, $J_B(6)$ and $S(6) = 7.58932292$ are asserted via exact rationals, $S(100)$ agrees with exact summation to $10^(-9)$, and the answer is stable under doubling $N_0$.

#pagebreak()
#link("https://projecteuler.net/problem=568")[= Problem 568: Reciprocal Games II]

Solution: 4228020

With the games of problem 567, we need the 7 most significant digits of $D(n) = J_B(n) - J_A(n)$ at $n = 123456789$ — after stripping leading zeros, of which there are about 37 million: every order of the $1\/n$ expansion cancels and $D$ decays like $2^(-n)$, so floating-point subtraction is hopeless.

The way through is an exact recurrence. From $1\/(k binom(n,k)) = (1\/k - 1\/n) \/ binom(n-1, k)$ follows $J_B(n) = J_B(n-1) + 2\/n - A_n$ with $A_n = 2^(-n) sum_(j<=n) 2^j\/j$, while problem 567's identity gives $J_A(n) = A_n - 2^(-n) H_n$. Together with $A_(n-1) = 2A_n - 2\/n$ everything collapses to

$ D(n) = D(n-1) + 2^(-n)(H_n - 2H_(n-1)), $

verified exactly with rationals for $n < 60$. Since $sum 2^(-m) H_(m-1) = sum 2^(-m)\/m = ln 2$, the series telescopes to zero at infinity, leaving the exact tail $D(n) = sum_(m>n) 2^(-m)(H_(m-1) - 1\/m) = 2^(-n) G(n)$ with $G(n) tilde H_n$ — also verified directly. $G$ is evaluated in 60-digit decimal arithmetic, and the leading digits come from the fractional part of $log_10 D = -n log_10 2 + log_10 G$ with $log_10 2$ at 60 digits. The extraction machinery reproduces the worked example $D(6) = 0.03828125 -> 3828125$ and the exact digits of $D(40)$.

#pagebreak()
#link("https://projecteuler.net/problem=569")[= Problem 569: Prime Mountain Range]

Solution: 21025060

Mountains with $45 degree$ slopes rise by $p_(2k-1)$ and fall by $p_(2k)$; $P(k)$ counts previous peaks visible from peak $k$, and we need $sum_(k<=2500000) P(k)$.

Peak $k$ sits at $x_k = p_1 + dots.c + p_(2k-1)$, $y_k = p_1 - p_2 + dots.c + p_(2k-1)$; the heights strictly increase (each step adds the positive prime gap $p_(2k+1) - p_(2k)$, asserted over the whole range). A peak $j$ is visible from $k$ exactly when its sight slope $s_j = (y_k - y_j)\/(x_k - x_j)$ is a strict prefix minimum scanning $j = k-1$ down to $1$.

The farthest visible peak is the rightmost global minimiser of $s_j$, and that is a vertex of the upper convex hull of peaks $1..k-1$: the minimal-slope tangent from $k$ has every peak on or below it, with peaks strictly below the hull strictly below the tangent. So one sweep maintains the hull incrementally (monotone stack, $O(n)$ total), locates the tangent vertex $t$ by binary search — the slope from $k$ along a strictly convex hull is unimodal — and scans only $j = k-1, dots, t$ for prefix minima; measured scan lengths stay tiny. Slope and orientation tests multiply $y$-differences ($< 2^26$) by $x$-differences ($< 2^48$), overflowing int64, so an exact 128-bit product comparison via 32-bit limbs is used throughout. Verified against an $O(n^2)$ scan for the first 3000 peaks plus the given $P(3) = 1$, $P(9) = 3$ and $sum_(k<=100) P(k) = 227$.

#pagebreak()
#link("https://projecteuler.net/problem=570")[= Problem 570: Snowflakes]

Solution: 271197444

A snowflake of order $n$ overlays a $180°$-rotated equilateral triangle onto each same-size equilateral triangle of the order $n-1$ snowflake. $A(n)$ counts unit triangles exactly one layer thick, $B(n)$ those three layers thick, $G(n) = gcd(A(n), B(n))$; we need $sum_(n=3)^(10^7) G(n)$.

The construction had to be reverse-engineered from the problem's picture: fitting the triangular lattice to the order-3 panel pixel-by-pixel gave the true per-cell thickness field ${1: 30, 2: 84, 3: 6}$, and an exact subset-cover over candidate stamps proved each step refines the lattice by 3 (children inherit thickness) and then adds $+1$ over the rotated-star footprint of every cell _visible as a unit triangle_ — one whose thickness differs from all three edge-neighbours. The rule reproduces every given value, including the six 4-layer (green) spots of the order-4 panel.

Thickness values grow with $n$, but visibility only needs value _differences_, which propagate cleanly (corner and mid children preserve the parent difference; new pairs differ by stamp bits). Abstracting each cell's 3-shell neighbourhood by clamping values above 3 into equality classes yields an exact local-configuration dynamics that closes at 1009 types with zero conflicts; iterating its integer transition counts reproduces the simulation for $n <= 8$ and the given $A(11) = 3027630$, $B(11) = 19862070$. The sequences obey $x^2-7x+12$ and its square:

$ A(n) = 3 dot 4^(n-1) - 2 dot 3^(n-1), quad B(n) = (9n-69) 2^(2n-3) + (4n+26) 3^(n-1). $

For the gcd, $A\/6 = 2^(2n-3) - 3^(n-2)$ is coprime to 6, and modulo it $2^(2n-3) equiv 3^(n-2)$, which collapses $2B\/6$ to $3^(n-2)(7n+3)$; since $3^(n-2)$ is invertible, $G(n) = 6 gcd(2^(2n-3) - 3^(n-2), 7n+3)$ — verified against exact big-integer gcds for all $n <= 300$, with the given $G(500) = 186$ and $sum_(n=3)^500 G(n) = 5124$ asserted. The final sum needs two modular exponentiations mod $7n+3$ per $n$, parallelised over 64 lanes.

#pagebreak()
#link("https://projecteuler.net/problem=571")[= Problem 571: Super Pandigital Numbers]

Solution: 30510390701978

A number is pandigital in base $b$ if its base-$b$ digits include every value $0..b-1$, and $n$-super-pandigital if this holds in every base from 2 to $n$. We need the sum of the 10 smallest 12-super-pandigital numbers.

Pandigitality in base $n$ forces at least $n$ base-$n$ digits, so the smallest candidates are exactly the $n$-digit base-$n$ pandigitals: permutations of the digits $0..n-1$ with nonzero leading digit. Enumerating leading digits in increasing order and the remaining digits in lexicographic permutation order visits these numbers in strictly increasing value (they share a common length), so the first ten hits are the ten smallest — provided all ten fit within the $n$-digit range, which is asserted. Each candidate is screened with digit bitmasks from base $n - 1$ downward, the highest base being by far the most selective; about $1.7 times 10^8$ permutations are sifted for $n = 12$.

The search is validated on all the given facts: 978 is the smallest 5-super-pandigital, 1093265784 the smallest 10-super-pandigital, and the ten smallest 10-super-pandigitals sum to 20319792309.

#pagebreak()
#link("https://projecteuler.net/problem=572")[= Problem 572: Idempotent Matrices]

Solution: 19737656

$C(n)$ counts $3 times 3$ integer matrices with $M^2 = M$ and entries in $[-n, n]$; we need $C(200)$.

An idempotent matrix is a projection, so its rank equals its trace: $0$, $1$, $2$ or $3$. Ranks 0 and 3 give $M = 0$ and $M = I$. A rank-1 integer idempotent factors as $M = m p q^top$ with $p, q$ primitive integer vectors, and $"tr" M = m (p dot q) = 1$ forces $m = plus.minus 1$, so $M = p q^top$ with $p dot q = 1$ — which makes both vectors primitive automatically, the factorisation being unique up to negating both. Rank-2 idempotents biject with rank-1 ones via the complement $N = I - M$, whose off-diagonal entries lie in $[-n, n]$ and diagonal entries in $[1-n, n+1]$.

Entry $(i, j)$ of $p q^top$ is $p_i q_j$, so each $q_j$ is confined to an interval determined by $p$ (off-diagonal bounds $n\/|p_i|$ plus the diagonal window). Sweeping all $p$ with $|p_i| <= n + 1$, for each $q_3$ in its interval the equation $p_1 q_1 + p_2 q_2 = 1 - p_3 q_3$ is a line in the $(q_1, q_2)$ rectangle, counted in $O(1)$ by extended-gcd parametrisation and interval intersection; the grand total halves for the $(p, q) tilde (-p, -q)$ symmetry. Verified against literal nine-loop brute force for $n = 1, 2, 3$, including the given $C(1) = 164$ and $C(2) = 848$.

#pagebreak()
#link("https://projecteuler.net/problem=574")[= Problem 574: Verifying Primes]

Solution: 5780447552057000454

For a prime $q$ and coprime $A >= B > 0$ with $A B$ divisible by every prime below $q$, any sum $A + B < q^2$ and any difference $1 < A - B < q^2$ is prime. $V(p)$ is the smallest $A$ over all such certificates of $p$, and $S(n) = sum V(p)$ over primes $p < n$; we need $S(3800)$.

Enlarging $q$ only adds divisibility requirements, so the minimum is attained at the smallest prime $q$ with $q^2 > p$. For a sum $p = A + B$ the gcd condition is automatic and each prime $r < q$ must divide $A$ or $p - A$; $A$ is found by scanning $[p\/2, p)$, and sums beat differences whenever they exist since a difference has $A = p + B > p$. For a difference, $gcd(A, B) = gcd(p, B)$, so we need the smallest $B >= 1$ with $p divides.not B$ and $B equiv 0$ or $-p mod r$ for every odd prime $r < q$ ($r = 2$ is automatic for odd $p$).

That is a minimum-CRT problem over $2^17$ residue classes for the largest $q = 67$, where the answer can reach $approx 10^16$. Splitting the odd primes into halves with balanced products $M_1, M_2 < 2^40$, each half's residues are enumerated by iterative CRT, and for each pair $x = x_1 + M_1 t$ with $t = (x_2 - x_1) M_1^(-1) mod M_2$; minimising $x$ is minimising $(t, x_1)$ lexicographically, so everything stays in 64-bit integers (an exact 20-bit-split mulmod handles $t$), with the $p | x$ exclusion checked modularly. Verified against a direct $B$-scan up to twice the primorial for all $p < 525$, the given $V(2) = 1$, $V(37) = 22$, $V(151) = 165$, and $S(10) = 10$, $S(200) = 7177$.

#pagebreak()
#link("https://projecteuler.net/problem=575")[= Problem 575: Wandering Robots]

Solution: 0.000989640561

A robot wanders a $1000 times 1000$ grid of rooms numbered row by row. Its designers were told to program it "with equal probability of remaining in the same room or moving to an adjacent room" — an ambiguous brief admitting two readings, and the robot was built with either, equally likely: (A) a lazy walk that stays with probability $1\/2$ and otherwise moves to a uniformly random neighbour, or (B) all $d + 1$ options (the $d$ neighbours plus staying) each with probability $1\/(d+1)$.

Both chains are reversible, so detailed balance gives the stationary laws directly: $pi(v) prop deg(v)$ for the lazy walk (laziness does not alter the simple random walk's stationary distribution) and $pi(v) prop deg(v) + 1$ for the uniform variant, since $pi(v) dot 1\/(deg(v) + 1)$ is then symmetric across each edge. After "unfathomable periods of time" the answer is the stationary probability of a square-numbered room averaged over the two builds:

$ P = 1/2 (S_d / (2E) + (S_d + n) / (2E + n^2)), $

with $S_d$ the degree sum over rooms $k^2$, $2E = 4n(n-1)$ the total degree, and $n$ square rooms each gaining $+1$ in variant B. Room $r$ sits at row $floor((r-1)\/n)$, column $(r-1) mod n$, with degree 4 minus one per touched boundary. Exact rationals throughout; the given $5 times 5$ value $0.177976190476$ is asserted and both $5 times 5$ stationary laws are cross-checked by power iteration of the literal transition matrices.

#pagebreak()
#link("https://projecteuler.net/problem=577")[= Problem 577: Counting Hexagons]

Solution: 265695031399260211

$H(n)$ counts the regular hexagons with all six vertices on the triangular lattice of an equilateral triangle of side $n$; we need $sum_(n=3)^12345 H(n)$.

The tilted hexagons are the heart of the problem (they are why $H(6) = 12$ rather than $11$). Every regular hexagon with lattice vertices inscribes in a unique smallest *upright* lattice hexagon: sliding the six vertices of an upright hexagon of side $s$ the same offset $t$ along its sides, $0 <= t < s$, produces $s$ distinct regular hexagons with the same centre, one of which is the upright hexagon itself, and every lattice hexagon arises exactly once this way. An upright hexagon of side $s$ spans a triangle of side $3s$ and can be placed in $binom(n - 3s + 2, 2)$ positions inside the side-$n$ triangle. Therefore

$ H(n) = sum_(s = 1)^(floor(n\/3)) s (n - 3s + 1)(n - 3s + 2) / 2, $

reproducing $H(3) = 1$, $H(6) = 12$ and $H(20) = 966$. The final answer is a cheap double loop over $n$ and $s$.

#pagebreak()
#link("https://projecteuler.net/problem=578")[= Problem 578: Integers with Decreasing Prime Powers]

Solution: 9219696799346

An integer $n = p_1^(e_1) dots.c p_k^(e_k)$ with $p_1 < dots.c < p_k$ has decreasing prime powers if $e_1 >= e_2 >= dots.c >= e_k$; $C(n)$ counts them up to $n$, and we need $C(10^13)$.

A depth-first search builds factorisations in increasing prime order, carrying the prefix product $m$ and the cap $e_max$ (the last exponent used). Each node counts its own prefix, recurses on primes $q <= sqrt(n\/m)$ above the last one with every legal exponent, and counts the remaining possibilities in bulk: a prime $q > sqrt(n\/m)$ can only carry exponent 1 and admits no further extension (the next prime would have to exceed $q$ yet stay below $(n\/m)\/q < q$), so those leaves number exactly $pi(n\/m) - pi(max(p_"last", sqrt(n\/m)))$.

Every $pi$ query lands on a value of the form $floor(n\/m)$ or below $sqrt(n)$ — precisely what one Lucy_Hedgehog sieve provides in $O(n^(3\/4))$ time via the tables $pi(v)$ for $v <= sqrt(n)$ and $pi(floor(n\/k))$ for all $k$. The sieve is sanity-checked against $pi(10^8) = 5761455$, and the count against per-integer factorisation up to $10^5$ plus the given $C(100) = 94$ and $C(10^6) = 922052$.

#pagebreak()
#link("https://projecteuler.net/problem=581")[= Problem 581: 47-smooth Triangular Numbers]

Solution: 2227616372734

We sum all $n$ with $T(n) = n(n+1)\/2$ 47-smooth. As $n$ and $n + 1$ are coprime and the division by 2 cannot affect primes above 47, $T(n)$ is 47-smooth exactly when $n$ and $n + 1$ both are. Størmer's theorem guarantees only finitely many such pairs of consecutive smooth integers exist, so the sum is finite.

Every pair $(n, n + 1)$ contains exactly one odd member, and odd 47-smooth numbers are far sparser than all of them. A depth-first search over exponent vectors of $3, 5, dots, 47$ enumerates every odd 47-smooth $v$ up to the bound $9 times 10^18$ (the int64 limit), and $v - 1$ and $v + 1$ are tested for smoothness by trial division; each pair is discovered exactly once via its odd member. The enumeration is cross-checked against plain trial division of every integer up to $10^7$.

The search finds 1502 pairs, the largest beginning at $n = 1109496723125 approx 1.1 times 10^12$ — and then runs more than $8 times 10^6$ times further without finding another, in agreement with Lehmer's Pell-equation computation of the complete list of consecutive 47-smooth pairs (OEIS A117581).

#pagebreak()
#link("https://projecteuler.net/problem=582")[= Problem 582: Nearly Isosceles 120 Degree Triangles]

Solution: 19903

We count integer triangles with a $120 degree$ angle, sides $a <= b <= c$, $b - a <= 100$ and $c <= 10^100$.

The $120 degree$ angle faces $c$, so $c^2 = a^2 + a b + b^2$. With $b = a + d$ for $d = b - a in 1..100$ ($d = 0$ would force $c = a sqrt(3)$), the quadratic formula demands that $3(4c^2 - d^2)$ be a square $(3z)^2$, i.e. the Pell-like equation

$ x^2 - 3 z^2 = d^2, quad x = 2c, quad a = (z - d)/2, $

with $x$ even, $z eq.triple d mod 2$ and $z >= d + 2$ so that $a >= 1$. Solutions form orbits under the fundamental unit $2 + sqrt(3)$ of $x^2 - 3y^2 = 1$, acting as $(x, z) -> (2x + 3z, x + 2z)$. The inverse map strictly decreases $z$ (as $x > z sqrt(3)$) and stays non-negative exactly while $z >= d$, so every orbit has a representative with $z < d$; enumerating seeds with $z <= 2d$ and expanding upward with exact integers until $x > 2n$ — about 175 steps reach $10^100$ — collects each solution once. Verified against brute-force enumeration for $n = 1000$ and $10^4$ and the given $T(1000) = 235$, $T(10^8) = 1245$.

#pagebreak()
#link("https://projecteuler.net/problem=583")[= Problem 583: Heron Envelopes]

Solution: 1174137929000

An envelope is a convex pentagon $A B C D E$: a rectangle $A B D E$ (width $w$, height $h$) with an isosceles flap $B C D$ of height $t < h$ on top. A Heron envelope has all five sides and all five diagonals ($A C$, $A D$, $B D$, $B E$, $C E$) integral; $S(p)$ sums the perimeters of those with perimeter at most $p$.

With $A = (0,0)$, $E = (w, 0)$, $B = (0, h)$, $D = (w, h)$, $C = (w\/2, h + t)$: $B D = w$, $A D = B E = sqrt(w^2 + h^2)$, $B C = C D = sqrt((w\/2)^2 + t^2)$ and $A C = C E = sqrt((w\/2)^2 + (h+t)^2)$. Integrality of $B C$ forces $w = 2u$, leaving three Pythagorean conditions sharing legs — $u^2 + t^2$, $u^2 + (h+t)^2$ and $(2u)^2 + h^2$ all squares — with perimeter $P = 2(h + u + sqrt(u^2 + t^2)) <= p$ and $1 <= t < h$.

For each $u$, the legs $x$ partnering $u$ come from the factorisations $u^2 = d e$ with $d < e$ of equal parity as $x = (e - d)\/2$, generated from the divisors of $u^2$ via a smallest-prime-factor sieve and pruned to $1 <= x <= p$ (anything larger can never fit the perimeter, and unpruned values overflow int64 squares). An envelope is then a pair $t < y$ from this list with $y > 2t$ (so $h = y - t > t$), perimeter in bound, and $4u^2 + h^2$ a perfect square; sorting lets both loops break early on the monotone perimeter. Verified against an independent brute scan at $p = 10^4$ — the given $S(10^4) = 884680$ — and $p = 3 dot 10^4$.

#pagebreak()
#link("https://projecteuler.net/problem=584")[= Problem 584: Birthday Problem]

Solution: 32.83822408

We need the expected number of people entering a room until 4 of them have birthdays within 7 days of each other, on a 365-day circular year, to 8 decimals.

On a circle, "$c$ people pairwise within $w$ days" is the same as "some window of $w+1$ consecutive days holds $c$ birthdays". So with $W = 8$ and cap 3, survival after $m$ people means every circular 8-day window holds at most 3 birthdays, and $EE[T] = sum_(m >= 0) P(T > m) = sum_m (m! \/ 365^m) thin a_m$, where $a_m$ sums $product 1\/c_i !$ over valid day-count vectors. The $a_m$ come from a circular transfer over days: the state is the count vector of the last 7 days (sum at most 3: 120 states), each day appending a count $c$ with weight $x^c\/c!$, tracked as polynomials in $x$. The circle closes by carrying the 120 boundary (first-7-days) states as a tensor axis and admitting only pairs whose concatenation passes every seam-crossing window. Degrees cap at $approx 140$, all coefficients are nonnegative (no cancellation), and 80-bit long doubles carry ample precision for the Borel sum.

The two given planets are asserted: 3 within 1 day on a 10-day year gives $5.78688636$, and 3 within 7 days on a 100-day year gives $8.48967364$.

#pagebreak()
#link("https://projecteuler.net/problem=585")[= Problem 585: Nested Square Roots]

Solution: 17714439395932

$F(n)$ counts distinct values $sqrt(x + sqrt(y) + sqrt(z))$ ($x <= n$; $y, z$ positive non-squares) that denest into a finite $plus.minus$-combination of square roots of integers; we need $F(5 dot 10^6)$.

If $kappa = sum s_i sqrt(a_i)$ then $kappa^2$ has even coefficients on every surd class, so the value $V$ determines $kappa = sqrt(V) > 0$ uniquely and distinct values correspond to distinct $kappa$. A Galois argument pins down $kappa$: every automorphism of the multiquadratic closure fixing $QQ(sqrt(D_1), sqrt(D_2))$ sends $kappa$ to $plus.minus kappa$, so $kappa = sqrt(rho) dot mu$ with $mu$ in the quadruple field — $kappa$ has at most four surd components whose cores form a coset of a Klein group. Three components force three surd classes in $kappa^2$, so $kappa$ is either _family 1_: $sqrt(A) + sqrt(B)$ with $A B$ non-square, or _family 2_: $plus.minus sqrt(p_1) plus.minus sqrt(q_1) plus.minus sqrt(p_2) plus.minus sqrt(q_2)$ with four pairwise distinct cores and $p_1 q_1 = p_2 q_2$, which kills exactly one of the three surd classes (two cannot vanish: apply the automorphism negating the surviving class), the signs being forced.

$F_1 = sum_x floor(x\/2) - sum_(kappa "squarefree") Q(floor(n\/kappa))$ with $Q(M) = \#{a >= b >= 1: a^2 + b^2 <= M}$. For $F_2$ all orbits of ordered tuples under the 8 relabelings are free, so $F_2 = N\/8$ where, via $p_1 = e f$, $q_1 = g h$, $p_2 = e h$, $q_2 = g f$, $gcd(f, h) = 1$, the sum becomes $(e+g)(f+h)$ and the unconstrained count is $sum_t phi(t) B(floor(n\/t))$, $B(M) = M(M-1)\/2$. Core collisions reduce to single group relations: (I) $"core"(p_1) = "core"(q_1) <=> e f g h$ square, counted per $m = kappa a b$ by sort + two-pointer over decomposition weights $kappa(a^2+b^2)$; (II) $"core"(p_1) = "core"(p_2) <=> f, h$ both squares, giving $sum_("coprime" (F,H)) B(floor(n\/(F^2+H^2)))$; (III) equals (II) by swapping $p_2, q_2$; any two relations force all four cores equal (E, a squarefree-count double sum), so bad $= I + 2 dot I I - 2E$. Total $approx 10$ s.

Verified against a literal brute force with core tests for $n <= 30$ and all six given values up to $F(5000) = 11134074$.

#pagebreak()
#link("https://projecteuler.net/problem=586")[= Problem 586: Binary Quadratic Form]

Solution: 82490213

$f(n, r)$ counts $k <= n$ expressible as $k = a^2 + 3a b + b^2$ with $a > b > 0$ in exactly $r$ ways; we need $f(10^15, 40)$.

Completing the square, $4k = (2a + 3b)^2 - 5 b^2$, so representations correspond to elements $xi = (u + v sqrt(5))\/2$ of the ring of integers of $QQ(sqrt(5))$ with norm $k$, subject to $v > 0$ and $u > 5v$, i.e. $phi^(-2) < xi' \/ xi < 1$. Multiplying by the norm-one unit $phi^2$ scales the ratio by $phi^(-4)$, so the window is exactly half a unit period: each orbit ${plus.minus phi^(2j) xi, plus.minus phi^(2j) xi'}$ contributes exactly one representation, with the boundary ratios ($v = 0$ and $a = b$) excluded. Since $h(QQ(sqrt(5))) = 1$ and $N(phi) = -1$, orbits correspond to conjugate-pairs of ideals of norm $k$, and self-conjugate ideals land exactly on the excluded boundary. Hence $r(k) = (A(k) - S(k))\/2$ with $A(k) = sum_(d | k) chi_5 (d)$ the ideal count (split $p equiv plus.minus 1 mod 5$ give $e+1$; inert $p$ force even exponents; 5 is free) and $S(k) = 1$ iff every split exponent is even. $r = 40$ means $A - S = 80$: either $A = 80$ (always containing an even factor, consistent with $S = 0$) or $A = 81$ (all factors odd $arrow.r.double$ all split exponents even, consistent with $S = 1$).

Counting: $k = g dot ("split part")$ with $g$ over the 14.1M background values $5^a m^2$ ($m$ inert-composed, sieved to $sqrt(n)$), and the split part realizing a multiplicative partition of 80 or 81 as $product (e_i + 1)$ over distinct split primes. A DFS assigns split primes to exponents and counts the innermost level via a $pi_"split"$ table, subtracting used primes in range; total work is proportional to the number of solutions ($approx 10^8$).

Verified against a literal representation histogram for all $k <= 10^5$ (five $r$ values including the given $f(10^5, 4) = 237$), the identity $r = (A-S)\/2$ checked by factorization for all $k <= 30000$, and the given $f(10^8, 6) = 59517$.

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
#link("https://projecteuler.net/problem=588")[= Problem 588: Quintinomial Coefficients]

Solution: 11651930052

$Q(k)$ counts the odd coefficients of $(x^4 + x^3 + x^2 + x + 1)^k$; we need $sum_(k=1)^18 Q(10^k)$.

Over $"GF"(2)$, $P(x)^(2^j) = P(x^(2^j))$, so $P^k eq.triple product_(j in "bits"(k)) P(x^(2^j))$. The coefficient of $x^e$ is therefore the parity of the number of ways to write $e = sum c_j 2^j$ with $c_j in {0, dots, 4}$ at the set bits of $k$ and $c_j = 0$ elsewhere — a base-2 carry process where position $j$ receives $c_j$ plus an incoming carry, emits one bit of $e$, and passes the rest on (carries never exceed 3).

A digit DP counts the exponents with odd parity. The state of an exponent prefix is the vector of representation parities indexed by pending carry — a 5-bit class — and processing the bits of $k$ from the bottom, each prefix splits over the next exponent bit while the class updates by XOR over the allowed $c_j$ and live carries. After the last bit of $k$, a prefix in class $v$ completes to exactly $"popcount"(v)$ exponents with an odd coefficient, since appending the carry's binary digits determines the rest of $e$ uniquely and injectively. Hence $Q(k)$ is the popcount-weighted class total. Verified against literal $"GF"(2)$ expansion for all $k < 200$ and the given $Q(3) = 7$, $Q(10) = 17$, $Q(100) = 35$.

#pagebreak()
#link("https://projecteuler.net/problem=589")[= Problem 589: Poohsticks Marathon]

Solution: 131776959.25

Two sticks repeatedly float under a bridge (journey times uniform integers in $[n, m]$, 5 seconds to refloat); the game ends when a stick emerges having made one more journey than the other. $E(m, n)$ is the expected duration; we need $S(100) = sum_(m=2)^100 sum_(n=1)^(m-1) E(m, n)$ to 2 decimals.

Stick A's $j$-th journey finishes at $sum a_(<= j) + 5(j-1)$, so A laps B at round $j$ exactly when $W + a_j <= -6$ where $W = sum_(i<j)(a_i - b_i)$; symmetrically B laps when $b_j <= W - 6$. The two can never trigger in the same round (they need $W <= -n-6$ and $W >= n+6$), so the game is a Markov chain on $W$, confined on continuing rounds to $[-5-m, 5+m]$.

The ending time equals (winner's journey sum) $+ thin 5(J-1) = sum_"rounds" ("winner's" t_i + 5) - 5$. Each round's $a$ counts only if A eventually wins, so with $p(W) = P("A wins from" W)$ (one linear solve), the expected remaining weighted time $g(W) = EE[(a+5) bold(1)_"Alap" + (b+5) bold(1)_"Blap" + ((a+5)p(W') + (b+5)(1-p(W')) + g(W')) bold(1)_"cont"]$ is a second linear solve, and $E(m, n) = g(0) - 5$.

Verified against the given $E(60, 30) = 1036.15$ and $S(5) = 7722.82$, and against a $4 dot 10^5$-game direct simulation of the lap rules for $(m, n) = (5, 2)$.

#pagebreak()
#link("https://projecteuler.net/problem=590")[= Problem 590: Sets with a Given Least Common Multiple]

Solution: 834171904

$H(n)$ counts the sets of positive integers whose least common multiple is exactly $n$, and $L(n) = "lcm"(1..n)$; we need $H(L(50000))$ modulo $10^9$.

A set with lcm $n$ consists of divisors of $n$ covering each prime's maximal exponent, so inclusion-exclusion over the primes whose exponent is capped one below maximal gives, for $n = product p_i^(e_i)$, $H(n) = sum_T (-1)^(|T|) 2^(product_i (e_i + 1 - [i in T]))$ — verified by literal subset enumeration for small $n$ and the given $H(12) = 44$. For $L(50000)$ the 5133 primes group by exponent: one each of $e = 15, 9, 6, 5$, two of $e = 4$, five of $e = 3$, thirty-seven of $e = 2$, and $k_1 = 5085$ primes with $e = 1$. Choices within a class of $c$ equal exponents contribute binomially, collapsing the $2^5133$-term sum to about $10^4$ class-choice combinations times a sum over $j$ (capped $e = 1$ primes) of $binom(k_1, j) (-1)^j 2^(D dot 2^(k_1 - j))$.

The towers $2^E mod 10^9$ split by CRT: $E >= 9$ always in the real computation (the smallest $D$ exceeds $2^37$), so the residue is $0$ modulo $2^9$, while 2 is a primitive root modulo $5^9$ with order $4 dot 5^8$, so only $E mod 4 dot 5^8$ is needed — one modular exponentiation per $(D, j)$ pair. Exact small exponents are handled directly so the same code validates $H L(n)$ for $n <= 20$ against exact big-integer evaluation; binomials mod $10^9$ come from a Pascal row.

#pagebreak()
#link("https://projecteuler.net/problem=591")[= Problem 591: Best Approximations by Quadratic Integers]

Solution: 526007984625966

$"BQA"_d (x, n)$ is the quadratic integer $a + b sqrt(d)$ closest to $x$ with $|a|, |b| <= n$, and $I_d$ takes its integral part. We need $sum |I_d ("BQA"_d (pi, 10^13))|$ over non-square $d < 100$.

For fixed $d$ this is inhomogeneous Diophantine approximation: minimise the distance of $b sqrt(d) - pi$ to the nearest integer over $|b| <= B$, where $B$ caps $b$ so the rounded $a$ stays within range ($b sqrt(d) <= n + 1\/2 + pi$, and then the nearest integer automatically has $|a| <= n$). Each of the four sign/side combinations reduces to $"minmod"(t, c, N) = min_(0 <= b <= N) (c + b t) mod 1$, solved exactly by a Euclidean recursion: the candidates are $c$ itself and the value just after each wrap $j$, which equals $(c - j) mod t$ — an identical problem at scale $t$ with step $(-1) mod t$ and offset $(c-1) mod t$, recursing in $O(log N)$ continued-fraction-like steps with the argmin rebuilt as $ceil((j - c)\/t)$ on the way out. All arithmetic is 130-digit Decimal with a floored mod (Decimal's `%` truncates), comfortably resolving distances around $10^(-27)$.

The recursion is verified against literal scans for 300 random $(t, c, N)$; the full solver against literal scans over $|b| <= 3000$ for every $d$; and all four given facts, including $I_2 ("BQA"_2 (pi, 10^13)) = -6188084046055$, are asserted.

#pagebreak()
#link("https://projecteuler.net/problem=592")[= Problem 592: Factorial Trailing Digits 2]

Solution: 13415DF2BE9C

$f(N)$ is the last twelve hexadecimal digits of $N!$ before the trailing zeroes; we need $f(20!)$ with $20! approx 2.4 dot 10^18$.

Write $N! = 2^v m$ with $m$ odd and $v = sum_(i>=1) floor(N\/2^i)$; the trailing hex zeroes number $floor(v\/4)$, so $f(N) = m dot 2^(v mod 4) mod 2^48$. The odd part factors as $m = product_(i>=0) "OF"(floor(N\/2^i))$ with $"OF"(R)$ the product of odd $j <= R$, so everything reduces to $"OF"(R) mod 2^56$ for huge $R$.

$"OF"$ is computed 2-adically: every $j equiv 3 mod 4$ is replaced by $-j$ (tracking the sign $(-1)^(floor((R+1)\/4))$), leaving units $u equiv 1 mod 4$ where $log u = sum_(m>=1) (-1)^(m+1)(u-1)^m\/m$ converges with $v_2 >= 2m - v_2(m)$, so truncating at $m = 34$ is exact mod $2^56$. The sum of $(u-1)^m$ over each arithmetic progression up to $R$ expands binomially into exact power sums $sum t^i$ (Pascal recursion, big integers); divisions by $m$ and by $t!$ in the exponential are exact 2-adic operations, and $exp(L) = sum L^t\/t!$ terminates at $t + s_2(t) >= 56$ since $4 | L$. The whole computation is a few dozen polynomial sums and runs in 0.1 s.

$"OF"$ is verified against literal products mod $2^56$ for various $R <= 1.3 dot 10^5$, and $f$ against actual factorials with zeroes stripped for $N = 20$ (the given 21C3677C82B4), 21, 25, 50, 100 and 1000.

#pagebreak()
#link("https://projecteuler.net/problem=593")[= Problem 593: Fleeting Medians]

Solution: 96632320042.0

With $S(k) = p_k^k mod 10007$ ($p_k$ the $k$-th prime) and $S_2(k) = S(k) + S(floor(k\/10000) + 1)$, $F(n, k)$ sums the medians of all length-$k$ sliding windows of $S_2$; we need $F(10^7, 10^5)$.

The values $S_2$ are confined to $0..2 dot 10006$, so a window is just a counting distribution over about $20000$ buckets. A Fenwick tree over the value range gives $O(log)$ insert and delete as the window slides and $O(log)$ selection of the $r$-th smallest via binary lifting; with the even window length the median is the mean of the $k\/2$-th and $(k\/2+1)$-th order statistics, so the code accumulates twice the median sum as an exact integer and halves at the end with `.0`/`.5` formatting.

Building $S$ needs the first $10^7$ primes ($p_(10^7) = 179424673$) and a modular power each, with the exponent reduced to $k mod 10006$ by Fermat ($10007$ is prime; the prime $10007$ itself maps to $0$). The sliding machinery is cross-checked against sort-the-window medians on a $3000$-element prefix, and the given $M(1,10) = 2021.5$, $M(10^2,10^3) = 4715.0$, $F(100,10) = 463628.5$ and $F(10^5,10^4) = 675348207.5$ are all asserted.

#pagebreak()
#link("https://projecteuler.net/problem=600")[= Problem 600: Integer Sided Equiangular Hexagons]

Solution: 2668608479740672

An equiangular hexagon has every interior angle $120 degree$. Extending three alternate sides until they meet circumscribes the hexagon in an equilateral triangle of side $x$, slicing off three corner equilateral triangles of sides $a, b, c$. The six hexagon sides are then $a, b, c$ together with $x - a - b, x - b - c, x - a - c$, and the perimeter is
$
3x - (a + b + c).
$
A hexagon sits inside two such triangles (one per orientation); always taking the smaller forces $x >= a + b + c$, so each hexagon is counted exactly once. Counting up to congruence, the three corner cuts are unordered, so impose $1 <= a <= b <= c$.

Group the count by $s = a + b + c$. The number of corner triples with that sum is the number of partitions of $s$ into exactly three positive parts, which is the nearest integer to $s^2 \/ 12$. For each such triple the triangle side runs over $s <= x <= floor((n + s) \/ 3)$ to keep the perimeter $<= n$, giving $floor((n+s)\/3) - s + 1$ hexagons. Hence
$
H(n) = sum_(s=3)^(floor(n\/2)) "round"(s^2 \/ 12) dot (floor((n + s) \/ 3) - s + 1),
$
which reproduces $H(6) = 1$, $H(12) = 10$, $H(100) = 31248$ and yields $H(55106)$.

#pagebreak()
#link("https://projecteuler.net/problem=601")[= Problem 601: Divisibility Streaks]

Solution: 1617243

Define $"streak"(n)$ as the smallest $k >= 1$ for which $k + 1$ does not divide $n + k$. Since $(k+1) | (n+k)$ is the same as $n equiv 1 space (mod k+1)$,
$
"streak"(n) >= s quad <==> quad n equiv 1 space (mod j) "for" j = 2, dots, s quad <==> quad n equiv 1 space (mod L_s),
$
where $L_s = "lcm"(1, 2, dots, s)$. Counting the $n$ with $1 < n < N$ that hit a given residue, the number with $"streak"(n) = s$ is
$
P(s, N) = floor((N - 2) \/ L_s) - floor((N - 2) \/ L_(s+1)),
$
and the answer is $sum_(i=1)^31 P(i, 4^i)$. As checks, $P(3, 14) = 1$ and $P(6, 10^6) = 14286$.

#pagebreak()
#link("https://projecteuler.net/problem=602")[= Problem 602: Product of Head Counts]

Solution: 269496760

If Alice's first Head lands on her $r$-th toss (probability $p^(r-1)(1-p)$, with $p$ the Tail probability), every friend has tossed $r - 1$ times, so each friend's Head count is Binomial$(r - 1, 1 - p)$ with mean $(r-1)(1-p)$. The $n$ friends are independent, so writing $q = 1 - p$ and $m = r - 1$,
$
e(n, p) = sum_(m=0)^infinity p^m q dot (m q)^n = q^(n+1) sum_(m=0)^infinity m^n p^m.
$
The standard generating function $sum_(m>=0) m^n x^m = A_n (x) \/ (1 - x)^(n+1)$, where $A_n$ is the Eulerian polynomial, cancels the $q^(n+1)$ factor exactly, leaving $e(n, p) = A_n (p)$. Therefore $c(n, k)$ is the Eulerian number $angle.l.double n; k - 1 angle.r.double$, the number of permutations of $n$ elements with $k - 1$ ascents. (Check: $A_3(p) = p + 4 p^2 + p^3$ matches the given $e(3, p)$.)

Evaluate it with the closed form
$
angle.l.double n; m angle.r.double = sum_(j=0)^m (-1)^j binom(n + 1, j) (m + 1 - j)^n,
$
all modulo the prime $10^9 + 7$. The binomial is built incrementally, the inverses $1, ..., m$ come from the linear recurrence $"inv"[i] = -(p \/ i) "inv"[p mod i]$, and each $(m + 1 - j)^n$ is a fast modular power; products stay inside int64 because $(10^9 + 7)^2 < 2^63$. This confirms $c(100, 40) equiv 986699437$ and produces $c(10^7, 4 dot 10^6)$.

#pagebreak()
#link("https://projecteuler.net/problem=603")[= Problem 603: Substring Sums of Prime Concatenations]

Solution: 879476477

For a number with digits $d_0 d_1 ... d_(L-1)$, the digit $d_i$ appears in every substring whose start lies in ${0, ..., i}$ and whose end $e >= i$, contributing place value $10^(e-i)$. Summing the $(i+1)$ start choices and the geometric series over $e$ gives
$
S = sum_(i=0)^(L-1) d_i (i + 1) (10^(L-i) - 1) / 9,
$
which reproduces $S(2024) = 2304$.

Now $C = C(n, k)$ is the period-$D$ repetition of $P = P(n)$, where $D$ is the digit length of $P$. Write the global index as $i = b D + r$ with block $b in {0, ..., k-1}$ and offset $r in {0, ..., D-1}$, so $d_i = p_r$ and $L = k D$. With $g = 10^D$, the place-value term becomes $10^(L-i) = g^(k-b) 10^(-r)$, and substituting $c = k - b$ turns the block sum into the geometric series
$
A = sum_(c=1)^k g^c, quad B = sum_(c=1)^k c g^c,
$
both available in closed form modulo $10^9 + 7$. Separating the parts that depend on $r$ leaves four digit sums over a single copy of $P$,
$
s_1 = sum_r p_r 10^(-r), space s_2 = sum_r p_r r 10^(-r), space s_3 = sum_r p_r, space s_4 = sum_r p_r r,
$
and the final value is $(alpha s_1 + A s_2 - beta s_3 - k s_4) \/ 9$ with $alpha = (k D + 1) A - D B$ and $beta = D binom(k, 2) + k$. The four sums are accumulated in one pass over the $approx 6.8$ million digits of the first $10^6$ primes; everything else is $O(1)$. The block formula was checked against brute force on small repetitions, including $S(C(7,3))$.

#pagebreak()
#link("https://projecteuler.net/problem=604")[= Problem 604: Convex Path in Square]

Solution: 1398582231101

A strictly increasing convex function passing through lattice points has step vectors (between consecutive points) with strictly increasing slopes, all with $Delta x >= 1$ and $Delta y >= 1$. Distinct slopes force distinct primitive vectors $(a, b)$ with $gcd(a, b) = 1$, and using the primitive representative of each slope minimises displacement. So the task is to pick as many distinct primitive vectors $(a, b)$, $a, b >= 1$, as possible subject to $sum a <= N$ and $sum b <= N$; the answer is that maximum plus one (points = edges + 1).

To maximise the count we add vectors in increasing order of $a + b$. The primitive vectors with $a + b = s$ are the pairs $(a, s - a)$ for $a$ coprime to $s$, so there are $phi(s)$ of them, and by the symmetry $a <-> s - a$ they cost $s phi(s) \/ 2$ to each of the two budgets. Taking all full levels $s = 2, ..., L$ that fit leaves an equal leftover $R = N - sum_(s<=L) s phi(s)\/2$ in each budget; at level $s = L + 1$ each additional vector spends $a$ from one axis and $s - a$ from the other, so a balanced selection fits $floor(2R \/ (L + 1))$ more. Hence
$
F(N) = 1 + sum_(s=2)^(L) phi(s) + floor(2R \/ (L + 1)).
$
A totient sieve to about $2.1 dot 10^6$ covers $N = 10^18$. The formula was checked against an exact two-dimensional knapsack for small $N$ and reproduces $F(100) = 30$ and $F(50000) = 1898$.

#pagebreak()
#link("https://projecteuler.net/problem=605")[= Problem 605: Pairwise Coin-Tossing Game]

Solution: 59992576

In each round only the player shared with the next round can possibly win two in a row, so relabel round $r$ by the bit $s_r = 1$ if that shared player wins, $s_r = 0$ otherwise. The $s_r$ are independent fair bits, and the game ends the first time the pattern $1, 0$ appears (the shared player wins round $r$ then round $r+1$). A binary string avoids $10$ exactly when it is $0^a 1^b$, so the first $10$ ends at position $r+1$ with probability
$
Pr(T = r) = r dot 2^(-(r+1)),
$
($r$ choices for the $0^a 1^b$ prefix of length $r$, each of probability $2^(-r)$, times $1\/2$ for the closing $0$). The winner is the player shared between rounds $r$ and $r+1$, namely player $(r mod n) + 1$, so player $k$ wins iff $r equiv k - 1 space (mod n)$. Summing the arithmetic-geometric series over $r equiv m space (mod n)$ with $m = k - 1$, and writing $D = 2^n - 1$,
$
P_n (k) = (2^(n - m - 1) (m D + n)) / D^2.
$
This reproduces $P_3(1) = 12\/49$ and $P_6(2) = 368\/1323$. For the reduced fraction, $D$ is odd so the $2^(n-m-1)$ is coprime to it, and any common prime of numerator and denominator must divide $gcd(n, D)$. Since $n = 10^8 + 7$ is prime and $2^n equiv 2 space (mod n)$ gives $gcd(n, D) = 1$, the fraction is already in lowest terms. Hence $M_n (k) = 2^(n-m-1)(m D + n) D^2$, evaluated modulo $10^8$.

#pagebreak()
#link("https://projecteuler.net/problem=606")[= Problem 606: Gozinta Chains II]

Solution: 158452775

A gozinta chain $1 = d_0 | d_1 | ... | d_t = n$ corresponds to an ordered factorisation of $n$ into factors $> 1$, so $g(n)$ depends only on the prime signature (the multiset of exponents). For a signature with exponents $e_i$ and $k = sum e_i$,
$
g = sum_(t=1)^k sum_(j=0)^t (-1)^j binom(t, j) product_i binom(e_i + t - j - 1, e_i).
$
For a single exponent $k$ this is $2^(k-1)$, which is the minimum over all signatures of that total, so any signature with $k >= 9$ has $g >= 256 > 252$. Searching signatures with $k <= 8$ shows the *unique* one with $g = 252$ is $(3, 3)$: numbers of the form $k = (p q)^3$ for distinct primes $p, q$.

Thus $k <= N$ iff $p q <= floor(N^(1\/3))$, and with $B = floor(N^(1\/3))$,
$
S(N) = sum_(p < q, space p q <= B) (p q)^3 = sum_(p <= sqrt(B)) p^3 (Pi_3(floor(B \/ p)) - Pi_3(p)),
$
where $Pi_3(x) = sum_(q <= x "prime") q^3$. For $N = 10^36$ we have $B = 10^12$, so the inner cube-sums run up to $5 dot 10^11$; these are obtained for every needed argument $floor(B\/p)$ at once by a Lucy_Hedgehog sieve carried out modulo $10^9$ in $O(B^(3\/4))$ time. The reduction was checked against brute force on $S(10^6)$ and $S(10^12)$.

#pagebreak()
#link("https://projecteuler.net/problem=607")[= Problem 607: Marsh Crossing]

Solution: 13.1265108586

Minimise the crossing time over a diagonal marsh of banded speeds by binary-searching the entry angle and applying Snell's law at each band boundary.

#pagebreak()
#link("https://projecteuler.net/problem=608")[= Problem 608: Divisor Sums]

Solution: 439689828

Write $m = product_p p^(a_p)$. A divisor $d | m$ has $p$-exponent $b_p in [0, a_p]$, and $sigma_0(k d) = product_p (v_p (k) + b_p + 1)$, so summing over $d | m$ factors prime-by-prime:
$
sum_(d | m) sigma_0(k d) = product_p h_p (v_p (k)), quad h_p (e) = sum_(b=0)^(a_p) (e + b + 1) = binom(a_p + 2, 2) + (a_p + 1) e.
$
Dividing each $h_p$ by $h_p (0) = binom(a_p + 2, 2)$ gives a multiplicative $hat(g)$ with $g(k) = C_0 hat(g)(k)$, $C_0 = product_p binom(a_p + 2, 2)$. Writing $hat(g) = 1 * c$ shows $c(p^e) = 2 \/ (a_p + 2)$ (constant in $e >= 1$), and writing $c = b * 1$ in turn shows $b$ is supported on squarefree products of primes dividing $m$. Hence $hat(g) = b * sigma_0$ and
$
D(m, n) = sum_(k=1)^n g(k) = sum_e W(e) cal(D)(floor(n \/ e)), quad cal(D)(M) = sum_(t <= M) sigma_0(t),
$
where $e$ runs over squarefree products of distinct primes dividing $m$ with $e <= n$, and the integer weight is
$
W(e) = product_(p | e) (- binom(a_p + 1, 2)) product_(p | m, p divides.not e) binom(a_p + 2, 2).
$
For $m = 200!$ the $a_p$ come from Legendre's formula over the $46$ primes $p <= 200$. The divisor-summatory $cal(D)(M) = 2 sum_(i <= sqrt(M)) floor(M \/ i) - floor(sqrt(M))^2$ costs $O(sqrt(M))$. A depth-first search over the $46$ primes (pruning once $e p > n$) visits about $4.5 dot 10^7$ products with total cost $sum_e sqrt(n \/ e) approx 5.3 dot 10^8$, all modulo $10^9 + 7$. The reduction reproduces $D(3!, 10^2) = 3398$ and $D(4!, 10^6) = 268882292$.

#pagebreak()
#link("https://projecteuler.net/problem=609")[= Problem 609: $pi$ Sequences]

Solution: 172023848

A $pi$ sequence starting from $u_0$ is a prefix of the chain $u_0, pi(u_0), pi(pi(u_0)), ...$ truncated at any term that is still $>= 1$; for $u_0 = 10$ the chain $10 -> 4 -> 2 -> 1$ yields the three sequences $(10,4)$, $(10,4,2)$, $(10,4,2,1)$. With $c(u)$ the number of non-prime entries and $p(n,k) = \#{u : u_0 <= n, c(u) = k}$, the answer is $P(n) = product_(k : p(n,k) > 0) p(n,k)$.

Group the starting values by $v = pi(u_0)$. The $u_0$ with $pi(u_0) = v$ form the block $[p_v, p_(v+1))$, which contains exactly one prime ($p_v$) and the remaining $N_v = min(p_(v+1), n+1) - p_v - 1$ composites. Every $u_0$ in the block shares the same downstream chain $v -> pi(v) -> ... -> 1$; walking it gives cumulative non-prime counts $S_t$. The prime $u_0 = p_v$ then contributes one sequence with $c = S_t$ for each prefix length $t$, while each composite $u_0$ contributes $c = S_t + 1$. Hence
$
p(n,k) = sum_(v=1)^(pi(n)) (\#{t : S_t (v) = k} + N_v dot \#{t : S_t (v) + 1 = k}).
$
Sieving to $n = 10^8$ gives the primality and (via a prefix sum up to $pi(n) = 5 761 455$) the values $pi(w)$ needed to walk each chain, which collapses to $1$ in about a dozen steps. Accumulating the histogram and multiplying its positive entries modulo $10^9 + 7$ matches the given $P(10) = 648$ and $P(100) = 31038676032$.

#pagebreak()
#link("https://projecteuler.net/problem=610")[= Problem 610: Roman Numerals II]

Solution: 319.30207833

Each draw gives a letter (probability $0.14$) or `#` ($0.02$); invalid appends are skipped and `#` stops, outputting the current numeral's value. While only leading `M`s have been written, all seven letters extend the numeral validly, so the draw never skips: with probability $0.02$ we stop (value $1000a$), with $0.14$ we add another `M`, and with $0.14$ each of `I,V,X,L,C,D` we enter the sub-$1000$ part. Because the thousands add a flat $1000a$, the expected value is linear in $a$ and
$
H(0) = (0.14 G_6 + 140) \/ 0.86, quad G_6 = sum_(s in {1,5,10,50,100,500}) g(s),
$
where $g(s)$ is the expected final sub-$1000$ value from state $s$. Appending a letter to a minimal numeral strictly increases its value, so the sub-$1000$ states $0..999$ form a DAG; solving from large $s$ downward,
$
g(s) = (0.02 s + 0.14 sum_t g(t)) / (0.02 + 0.14 deg(s)),
$
with the successors $t$ being the values whose minimal string is $"minimal"(s)$ plus one letter. This yields $319.30207833$.

#pagebreak()
#link("https://projecteuler.net/problem=611")[= Problem 611: Hallway of Square Steps]

Solution: 49283233900

Door $n$ is toggled once for every pair $0 < i < j$ with $i^2 + j^2 = n$, so it ends open iff $r(n) = \#{(i, j) : 0 < i < j, thick i^2 + j^2 = n}$ is odd; $F(N)$ counts such $n <= N$ and we need $F(10^12)$.

== Parity of the representation count

Write $n = 2^a product p^e product q^f$ with $p equiv 1$, $q equiv 3 (mod 4)$, and $B = product (e + 1)$. The lattice-point formula $r_2(n) = 4B$ (all $f$ even, else $0$), refined by separating the $i = 0$ and $i = j$ points, gives $r(n) = (B - s)\/2$ with $s = [n "is a square"] + [n\/2 "is a square"]$ — so $r(n)$ is odd iff $B equiv 2 + s (mod 4)$. Two clean families result:

- $B equiv 2 (mod 4)$ (forcing $s = 0$): exactly one $p$ carries an odd exponent, which must be $equiv 1 (mod 4)$; uniquely $n = 2^a p^(4t+1) m^2$ with $m$ odd and $p$ coprime to $2m$.
- $B equiv 3 (mod 4)$ with $s = 1$: $n = 2^a m^2$ with $m$ odd and an odd number of primes $equiv 1 (mod 4)$ dividing $m$ to an odd power.

== Counting

The second family is a direct smallest-prime-factor sieve over $m <= 10^6$ with prefix counts. The first needs $pi_1(X)$, the count of primes $equiv 1 (mod 4)$ up to $X = N\/(2^a m^2)$ — all quotients of $N$ — supplied by a Lucy–Hedgehog sieve split over the residue classes $1$ and $3$ modulo $4$ (only odd numbers live in the classes, so sieving starts at $p = 3$); the rare $t >= 1$ prime powers use the explicit small-prime list, with care that $p^5$ already overflows 64-bit arithmetic for $p$ near $10^6$. About nine seconds in `numba`.

Checks: $F(5) = 1$, $F(100) = 27$, $F(1000) = 233$, $F(10^6) = 112168$ as given, plus a brute-force door-toggling simulation compared at several cutoffs.

#pagebreak()
#link("https://projecteuler.net/problem=612")[= Problem 612: Friend Numbers]

Solution: 819963842

Two numbers are friends if their base-10 digit sets share a digit. We want $f(10^18)$, the number of friend pairs $1 <= p < q < 10^18$, modulo $1000267129$, and count the complement (pairs sharing no digit).

For a digit set $U subset.eq {0, dots, 9}$, let $D[U]$ be the number of integers in $[1, n)$ whose digits all lie in $U$. Because $n = 10^18$ is a power of ten, $[1, n)$ is exactly the positive integers with at most $L = 18$ digits, so with $a = abs(U without {0})$ allowed nonzero digits and $b = abs(U)$ allowed digits,
$
D[U] = sum_(ell=1)^(L) a thin b^(ell-1).
$
$D$ is the subset-sum (zeta) transform of $"cnt"[S] = \#{x in [1, n) : "digit set of " x = S}$, so $"cnt"$ is recovered by the Möbius inverse. Two numbers are non-friends exactly when their digit sets are disjoint, and
$
sum_S "cnt"[S] thin D[overline(S)]
$
counts ordered disjoint pairs (never pairing $x$ with itself, each unordered pair twice). Hence $f(n) = binom(n-1, 2) - 1/2 sum_S "cnt"[S] D[overline(S)]$, evaluated exactly and then reduced. Check: $f(100) = 1539$.

#pagebreak()
#link("https://projecteuler.net/problem=613")[= Problem 613: Pythagorean Ant]

Solution: 0.3916721504

An ant at interior point $P$ moving in a uniformly random direction leaves through a given side with probability equal to the angle that side subtends at $P$, divided by $2 pi$ (the three subtended angles sum to $2 pi$). Averaging over a uniform $P$, the probability of leaving by the hypotenuse is
$
1/(2 pi dot "Area") integral.double_T angle A P B dif A,
$
with the $3$-$4$-$5$ triangle placed as $A = (4, 0)$, $B = (0, 3)$, right angle at the origin, $"Area" = 6$. Using $angle A P B = pi\/2 + arctan(x\/(3 - y)) + arctan(y\/(4 - x))$, the inner integral is elementary ($integral arctan(t\/u) dif t = t arctan(t\/u) - (u\/2) ln(u^2 + t^2)$, whose singular parts cancel), leaving a smooth one-dimensional integral evaluated by Gauss-Legendre quadrature. The result rounds to $0.3916721504$.

#pagebreak()
#link("https://projecteuler.net/problem=614")[= Problem 614: Special Partitions 2]

Solution: 130694090

A special partition uses distinct parts that are odd or divisible by $4$, i.e. parts $m equiv.not 2 space (mod 4)$. Therefore $sum_(i=0)^n P(i)$ is the number of subsets of such parts with sum $<= n$, the coefficient sum of $G(x) = product_(m equiv.not 2 (4)) (1 + x^m)$. Using $1 + x^m = (1 - x^(2 m)) \/ (1 - x^m)$ and grouping the residue classes, this telescopes to
$
G(x) = (E_2^2 E_8) / (E_1 E_4^2), quad E_k = product_(j >= 1) (1 - x^(k j)) = sum_i (-1)^i x^(k i (3 i - 1) \/ 2),
$
each $E_k$ being generalized-pentagonal (only $O(sqrt(n \/ k))$ nonzero terms). The series of $G$ to degree $n = 10^7$ is built by sparse multiplications (one sequential sweep per pentagonal term) and divisions (a blocked recurrence: far terms applied by streaming sweeps over already-finalised values, near terms by the in-window recurrence), all modulo $10^9 + 7$ with `int32` storage to limit memory traffic. Summing the coefficients (and subtracting the empty partition) reproduces $P(1)=1$, $P(10)=3$, $P(100)=37076$, $P(1000)=3699177285485660336$.

#pagebreak()
#link("https://projecteuler.net/problem=615")[= Problem 615: The Millionth Number with at Least One Million Prime Factors]

Solution: 108424772

Write a number with $Omega(n) >= K$ ($K = 10^6$) as $n = 2^a u$ with $u$ odd. Then $Omega(n) = a + Omega(u) >= K$ means $a >= K - Omega(u)$, so
$
n \/ 2^K = u dot 2^(a - K) = "base"(u) dot 2^t, quad "base"(u) = u \/ 2^(Omega(u)), space t >= 0.
$
Thus the numbers with $Omega >= K$ correspond order-preservingly to the values $"base"(u) dot 2^t$ over odd $u$ and $t >= 0$. Seeding every odd $u$ with $"base"(u) <= L$ (found by a depth-first product of odd primes, pruning once the base exceeds $L$, which needs primes up to $2 L$) and merging the geometric chains $"base"(u), 2 "base"(u), 4 "base"(u), ...$ in a min-heap enumerates the ratios in increasing order. Comparisons are exact via the integer key $u dot 2^(E + "off")$ with $E = t - Omega(u)$. The $10^6$-th popped ratio gives $n = 2^(K + E) u$, reduced modulo $123454321$. With $L = 2 dot 10^5$ the millionth ratio is $86597.5 <= L$, confirming no seed was missed; the verification on small $K$ reproduces the example (the $5$-th number with $Omega >= 5$ is $80$).

#pagebreak()
#link("https://projecteuler.net/problem=616")[= Problem 616: Creative Numbers]

Solution: 310884668312456458

Alice can only act on $L = {n}$ if $n = a^b$ is a perfect power, so non-powers are immediately stuck. Among perfect powers, two families fail to be creative. If $n = p^q$ with $p, q$ both prime, the single split gives ${p, q}$, two unsplittable primes that can only recombine, so only finitely many lists are reachable. The single value $16 = 2^4$ also fails: its only splits are ${2, 4}$, and since $4 = 2^2 -> {2, 2}$ one can amass at most three $2$'s, never enough to build $256$ and expose an odd factor — everything stays a power of two. Every other perfect power is creative: it can reach a list with an odd prime and enough material to grow without bound, hence reach any $m > 1$. For instance $256 = 2^8 -> {2, 8}$ and $8 = 2^3 -> {2, 3}$ already exposes $3$, and from $36 = 6^2 -> {6, 2}$, $2^6 = 64 = 4^3 -> {4, 3}$, $4 -> {2, 2}$ grows the list. Therefore
$
sum_("creative" <= 10^12) = sum_("perfect powers") - sum_(p, q "prime") p^q - 16,
$
computed by collecting the distinct perfect powers in a set and subtracting the prime-power-of-a-prime values and the lone exception $16$.

#pagebreak()
#link("https://projecteuler.net/problem=617")[= Problem 617: Mirror Power Sequence]

Solution: 1001133757

An $(n,e)$-MPS is an infinite sequence with $a_(i+1) = min(a_i^e, n - a_i^e)$ and all $a_i > 1$, determined by $(n, e, a_0)$; $C(n)$ counts them over all $e$ and we need $D(10^18) = sum_(n <= 10^18) C(n)$.

== Cycles have exactly one reflection

A surviving orbit alternates strictly increasing power runs $x -> x^e$ with reflections $x -> n - x^e$, so it ends in a cycle. A cycle with two reflections would force $m^(e^a) - m = r^(e^b) - r$ with $m != r$ and both exponents powers of the same $e$; the convexity gap $x^E - (x-1)^E >= 2(x - 1)$ rules this out. Every cycle is therefore $b -> b^e -> dots -> b^(e^(k-1)) -> b$ with
$
n = b + b^(e^k),
$
valid for all $b, e >= 2$, $k >= 1$ (the min-mode conditions hold automatically), and contributing $k$ sequences — one per starting rotation. Magnitude comparisons show distinct $(b, e, k)$ never collide.

== Transients are root chains only

Backward from the cycle, the only predecessors are $e$-th-root chains below the base: starts $a_0 = c$ with $c^(e^t) = b$, i.e. $n = c^(e^t) + c^(e^(t+k))$, one sequence per $(c >= 2, t >= 1)$. Reflection-type predecessors never exist: for any surviving $v$, the value $n - v$ falls strictly between consecutive $e$-th powers (a window argument around $b^(e^(k-1))$, resp. the chain top), so it is never a perfect power. Hence
$
D(N) = sum_(e >= 2, k >= 1) [k dot \#{b : b + b^(e^k) <= N} + \#{(c, t) : c^(e^t) + c^(e^(t+k)) <= N}],
$
a few hundred integer-root counts. Checks: a brute-force orbit-survival simulation for all $n <= 3000$ agrees exactly, as do the given $D(10) = 2$, $D(100) = 21$, $D(1000) = 69$, $D(10^6) = 1303$ and $D(10^12) = 1014800$.

#pagebreak()
#link("https://projecteuler.net/problem=618")[= Problem 618: Numbers with a Given Prime Factor Sum]

Solution: 634212216

$S(k)$ sums every $n$ whose prime factors (with multiplicity) add to $k$, e.g. $S(8) = 15 + 16 + 18 = 49$; we need $sum_(k=2)^24 S(F_k) mod 10^9$ with $F_24 = 46368$.

Each $n >= 2$ is, uniquely, a multiset of primes, so $S$ is an unbounded-knapsack sum over the primes up to $46368$. Start from $f[0] = 1$ (the empty product) and for each prime $p$ apply, with $k$ increasing,
$
f[k] <- f[k] + p dot f[k - p].
$
Increasing $k$ lets a prime repeat; processing primes one at a time counts each multiset once. Afterwards $f[k] = S(k)$, with all arithmetic modulo $10^9$ since only the last nine digits matter. Checks: $S(5) = 11$ and $S(8) = 49$.

#pagebreak()
#link("https://projecteuler.net/problem=619")[= Problem 619: Square Subsets]

Solution: 857810883

$C(a, b)$ counts the non-empty subsets of ${a, a+1, dots, b}$ whose product is a perfect square; we need $C(10^6, 1234567) mod (10^9 + 7)$.

== Rank over $"GF"(2)$

Map each element to the vector of its prime exponents mod $2$ (its squarefree kernel). A product is square exactly when the chosen vectors XOR to zero, so with $N = b - a + 1$ elements and $r$ the rank of the vectors, the subsets with square product form a $"GF"(2)$ kernel of dimension $N - r$ and
$
C(a, b) = 2^(N - r) - 1.
$

== Large primes pivot first

Factor every element with a smallest-prime-factor sieve. A prime above $sqrt(1234567) approx 1111$ can only appear to the first power and at most once per element, so eliminate those greedily: the first element seen containing large prime $p$ becomes the pivot for $p$ (adding one to the rank), and any later element containing $p$ is XORed against that pivot, leaving a vector over only the $186$ primes up to $1111$. Each such vector fits in one machine-word-scale bitmask and feeds an ordinary binary linear basis. Checks: $C(5, 10) = 3$, $C(40, 55) = 15$, and $C(1000, 1234) = 975523611$.

#pagebreak()
#link("https://projecteuler.net/problem=621")[= Problem 621: Expressing an Integer as the Sum of Triangular Numbers]

Solution: 11429712

$G(n)$ counts ordered triples of triangular numbers (including $T_0 = 0$) summing to $n$; we need $G(17526 dot 10^9)$.

== Three odd squares

Completing the square, $n = T_a + T_b + T_c$ exactly when $8n + 3 = (2a+1)^2 + (2b+1)^2 + (2c+1)^2$, and every representation of $m = 8n + 3 equiv 3 (mod 8)$ as three squares is automatically all-odd and zero-free, so $G(n) = r_3(m) \/ 8$, the positive ordered triples. Fixing the first square,
$
G(n) = sum_(x "odd", x^2 <= m - 2) P(m - x^2),
$
where $P(r)$ counts ordered pairs of positive odd $y, z$ with $y^2 + z^2 = r$. Each $r equiv 2 (mod 4)$ forces both coordinates odd, so Jacobi's two-square theorem gives $P(r) = r_2(r)\/4 = d_1(r) - d_3(r)$: the multiplicative function with factor $(e + 1)$ at $p equiv 1 (mod 4)$, factor $[e "even"]$ at $p equiv 3 (mod 4)$, and factor $1$ at $p = 2$. Sanity check: $G(9) = 7$ by hand.

== A quadratic polynomial sieve

Evaluating $d_1 - d_3$ needs the factorisation of all $3.4$ million values $r(x) = m - x^2$, which a polynomial sieve does collectively: for each odd prime $p <= sqrt(max r)$, solve $x^2 equiv m (mod p)$ by Tonelli–Shanks (skipping non-residues), convert the two roots into index progressions over the odd-$x$ grid, and at each hit divide out the full power of $p$ while updating the multiplicative factor. Whatever remains after sieving is $1$ or a single prime with exponent $1$. The whole computation is a few seconds under `numba`. Checks: $G(1000) = 78$ and $G(10^6) = 2106$.

#pagebreak()
#link("https://projecteuler.net/problem=622")[= Problem 622: Riffle Shuffles]

Solution: 3010983666182123972

A perfect riffle (faro out-) shuffle of an even deck of size $n$ moves the card at position $i$ to position $2i mod (n-1)$, fixing the two ends. The number of shuffles needed to restore the deck is therefore the multiplicative order of $2$ modulo $n - 1$:
$
s(n) = "ord"_(n-1)(2).
$
We want the sum of all $n$ with $s(n) = 60$. Setting $m = n - 1$ (odd), the condition is $"ord"_m(2) = 60$: equivalently $m | 2^60 - 1$ while $m$ divides none of $2^t - 1$ for the maximal proper divisors $t in {30, 20, 12}$ of $60$ (any proper divisor of $60$ divides one of these). Every divisor of $2^60 - 1$ is odd, so $n = m + 1$ is automatically even. We factor $2^60 - 1 = 3^2 dot 5^2 dot 7 dot 11 dot 13 dot 31 dot 41 dot 61 dot 151 dot 331 dot 1321$, enumerate its divisors, keep those of exact order $60$, and sum $n = m + 1$. The analogous computation reproduces the given $s(n) = 8$ total of $412$.

#pagebreak()
#link("https://projecteuler.net/problem=623")[= Problem 623: Lambda Count]

Solution: 3679796

$Lambda(n)$ counts closed lambda-terms writable with at most $n$ symbols (parentheses, $lambda$, dot and variables), up to $alpha$-equivalence; we need $Lambda(2000) mod (10^9 + 7)$.

Counting symbols gives the sizes: a variable is $1$, an application $(M space N)$ adds $2$, and an abstraction $(lambda x. M)$ adds $5$ — consistent with $Lambda(6) = 1$, the lone term $(lambda x.x)$. $alpha$-classes are counted de-Bruijn style by $T(s, m)$, the number of terms of size $s$ whose free variables are drawn from $m$ enclosing binders:
$
T(s, m) = m[s = 1] + T(s - 5, m + 1) + sum_a T(a, m) thin T(s - 2 - a, m),
$
the three summands being variables, abstractions and applications. Each extra binder costs $5$ symbols, so only states with $5m + s <= n$ matter; computing $m = n\/5$ down to $0$ makes the convolution about $n^3 \/ 30 approx 2.7 dot 10^8$ modular products, quick under `numba`. The answer is $sum_s T(s, 0)$. Checks: $Lambda(9) = 2$, $Lambda(15) = 20$, $Lambda(35) = 3166438$.

#pagebreak()
#link("https://projecteuler.net/problem=624")[= Problem 624: Two Heads Are Better Than One]

Solution: 984524441

A fair coin is tossed until the first $H H$, ending at toss $M$; $P(n)$ is the probability that $n | M$, and $Q(P(n), p)$ reduces the rational $P(n)$ modulo $p$. We need $Q(P(10^18), 10^9 + 9)$.

== A Fibonacci tail and two geometric series

The first $H H$ ends exactly at toss $m$ with probability $F(m-1) \/ 2^m$: the first $m - 3$ tosses avoid $H H$ and are followed by $T H H$, and length-$j$ strings without $H H$ are counted by a Fibonacci recurrence. So
$
P(n) = sum_(k >= 1) F(k n - 1) / 2^(k n).
$
Binet's formula $F(m) = (phi^m - psi^m) \/ sqrt(5)$ splits this into two geometric series: with $u = (phi\/2)^n$ and $v = (psi\/2)^n$,
$
P(n) = 1/sqrt(5) ( u / (phi (1 - u)) - v / (psi (1 - v)) ).
$

== Evaluating in $"GF"(p)$

$5$ is a quadratic residue modulo $p = 10^9 + 9$ (surely why that modulus was chosen), so $sqrt(5)$, $phi$, $psi$ and the whole closed form live in the field; the square root comes from Tonelli–Shanks and divisions from Fermat inverses. $Q$ is then just the residue taken in $1 dots p - 1$. The same code checks $Q(P(2), 109) = 66$ and $Q(P(3), 109) = 46$, and reproduces $P(2) = 3\/5$, $P(3) = 9\/31$ modulo $10^9 + 9$.

#pagebreak()
#link("https://projecteuler.net/problem=625")[= Problem 625: Gcd Sum]

Solution: 551614306

We need $G(N) = sum_(j=1)^N sum_(i=1)^j gcd(i, j)$ for $N = 10^11$, modulo $998244353$.

Replacing $gcd(i, j) = sum_(d | i, d | j) phi(d)$ and grouping the pairs by the common divisor $d$ (so $i = d a$, $j = d b$ with $1 <= a <= b <= floor(N\/d)$, of which there are $T(M) = M(M+1)\/2$ for $M = floor(N\/d)$),
$
G(N) = sum_(d >= 1) phi(d) T(floor(N\/d)).
$
Grouping $d$ by the value $M = floor(N\/d)$, each block contributes $T(M)(Phi("hi") - Phi("lo" - 1))$ where $Phi$ is the summatory totient. The values $Phi(floor(N\/d))$ at the $O(sqrt(N))$ distinct arguments are found by the standard recurrence
$
Phi(v) = T(v) - sum_(d >= 2) Phi(floor(v\/d)),
$
evaluated bottom-up with a $phi$-sieve for small arguments, all modulo the prime. The whole computation is $O(N^(3\/4))$. Checks: $G(10) = 122$, $G(1000) = 2475190$, $G(10^4) = 317257140$.

#pagebreak()
#link("https://projecteuler.net/problem=626")[= Problem 626: Counting Binary Matrices]

Solution: 695577663

$c(n)$ counts $n times n$ binary matrices up to row/column swaps and row/column complementations; we need $c(20) mod 1001001011$.

== Burnside over the hyperoctahedral pair

The group is $G = B_n times B_n$ with $B_n = S_n times.l ZZ_2^n$, $|G| = (2^n n!)^2$. For an element with row cycles $(a, p)$ and column cycles $(b, q)$ ($p, q$ the flip parities), each cycle pair splits its cells into $gcd(a, b)$ orbits, and a fixed matrix exists on them iff the accumulated flip $(b\/g) p + (a\/g) q$ is even — each consistent cell orbit contributing a factor $2$. In 2-adic terms: equal valuations $v_2(a) = v_2(b)$ force $p = q$; otherwise the cycle of larger valuation must have parity $0$. Globally, with $m_r, m_c$ the minimal valuations per side: if $m_r = m_c$ every cycle of minimal valuation shares one free parity bit and all others are forced to $0$ ($N = 2$ patterns); if $m_r < m_c$ all column parities are forced and exactly the row cycles of valuation $< m_c$ stay free ($N = 2^"count"$).

== Partition-pair sum

For a fixed underlying permutation each parity pattern arises from $2^(n - \#"cycles")$ sign vectors, so Burnside collapses to a sum over pairs of partitions of $20$ ($627^2$ pairs):
$
c(n) (2^n n!)^2 = sum A(lambda_r) A(lambda_c) thin 2^(2n - k_r - k_c) thin N thin 2^(sum_(i,j) gcd(a_i, b_j)),
$
evaluated exactly in Python integers ($2^400$-sized terms) and divided exactly by $|G|$ before reducing modulo the composite $1001001011$. Checks: brute-force orbit enumeration for $n <= 3$ and all nine given values $c(1) dots c(9)$.

#pagebreak()
#link("https://projecteuler.net/problem=628")[= Problem 628: Open Chess Positions]

Solution: 210286684

$n$ pawns sit one per row and column of an $n times n$ board; a position is open when a rook can travel from the empty lower-left corner to the upper-right corner moving only right or up. $f(3) = 2$ and $f(5) = 70$; we need $f(10^8) mod 1008691207$.

== Anti-diagonal walls are the only obstructions

A monotone rook path threads through the columns at non-decreasing heights. Tracking how the set of feasible heights evolves column by column shows a wall must lose exactly one row of clearance per column to stay tight — so the only way a permutation can block _every_ path is a solid anti-diagonal in a corner: pawns at $(r - j, j)$ for $j = 0 dots r$ (sealing the lower-left), or the mirror image sealing the upper-right. This characterisation is confirmed against a brute-force path search for all $n <= 9$.

== Inclusion–exclusion

Two walls of different sizes in the same corner would demand two pawns in one column, so each family is a disjoint union; a lower-left wall of size $r + 1$ coexists with an upper-right wall of size $s + 1$ exactly when $r + s <= n - 2$, the lone exception being the full anti-diagonal, which belongs to both families at once. Hence
$
"blocked"(n) = 2 sum_(k=0)^(n-1) k! - (sum_(r+s <= n-2) (n - 2 - r - s)! + 1),
$
and after telescoping $sum j dot j! = (n-1)! - 1$, with $S(m) = sum_(k <= m) k!$,
$
f(n) = n! - 2 S(n-1) + (n-1) S(n-2) - (n-1)! + 2.
$
One streaming pass produces $n!$, $S(n-1)$ and $S(n-2)$ modulo $1008691207$ — no divisions, so the modulus needn't be prime.

#pagebreak()
#link("https://projecteuler.net/problem=629")[= Problem 629: Scatterstone Nim]

Solution: 626616617

A move splits one pile into between $2$ and $k$ non-empty piles; $f(n, k)$ counts the partitions of $n$ that are first-player wins, and $g(n) = sum_(k=2)^n f(n, k)$; we need $g(200) mod (10^9 + 7)$.

== Three Grundy regimes

A position wins iff the XOR of its piles' Grundy values is nonzero, so $f(n, k) = p(n) - Z_k(n)$ with $Z_k$ the count of XOR-zero partitions. The single-pile Grundy function has three regimes. For $k = 2$ every move adds exactly one pile, fixing the game length, so $G_2(m) = (m - 1) mod 2$. For $k = 3$ there is no closed form; an exact mex DP tracks the set of achievable split-XORs as a $256$-bit mask, appending one part at a time (XOR by $G(t)$ permutes the bits of a set-mask). For $k >= 4$, $G_k(m) = m - 1$: inductively any split into $j$ parts has XOR at most $sum (p_i - 1) = m - j <= m - 2$, while the $k = 4$ moves already realise every value $0 dots m - 2$ (verified by the exact DP up to $200$); larger $k$ only adds moves under the same bound, so the mex is unchanged.

== Counting partitions by XOR

A knapsack over pile sizes counts partitions by their Grundy-XOR: even multiplicities of a size $s$ form an XOR-neutral step-$2s$ closure, plus an optional odd copy contributing $G(s)$. Then
$
g(n) = (n - 1) p(n) - Z_2(n) - Z_3(n) - (n - 3) Z_(>=4)(n),
$
exact in Python integers ($p(200) approx 4 dot 10^12$). Checks: $f(5, 2) = 3$, $f(5, 3) = 5$, $g(7) = 66$, $g(10) = 291$, and agreement with brute per-$k$ Grundy tables for every $n <= 30$.

#pagebreak()
#link("https://projecteuler.net/problem=630")[= Problem 630: Crossed Lines]

Solution: 9669182880384

From $2500$ pseudo-random points, $L$ is the set of distinct lines through pairs of points, $M(L)$ its size, and $S(L)$ the total number of crossings over all lines (each crossing pair counted from both sides). We need $S(L_2500)$.

Canonicalise the line through $(x_1, y_1)$ and $(x_2, y_2)$ as $A x + B y = C$ with $A = y_2 - y_1$, $B = x_1 - x_2$, $C = A x_1 + B y_1$, divided through by $gcd(A, B, C)$ with the first nonzero of $(A, B)$ made positive; distinct triples are then exactly distinct lines. Two distinct lines cross unless parallel, so
$
S(L) = M(M - 1) - sum_d c_d (c_d - 1),
$
where $c_d$ counts the lines in parallel class $d = (A, B) \/ gcd(A, B)$, sign-fixed. Packing each triple into one $64$-bit key turns the $3.1$ million point pairs into two `numpy` unique scans. Checks: $M(L_3) = 3$, $S(L_3) = 6$, $M(L_100) = 4948$, $S(L_100) = 24477690$.

#pagebreak()
#link("https://projecteuler.net/problem=634")[= Problem 634: Numbers of the Form $a^2 b^3$]

Solution: 4019680944

$F(N)$ counts the integers up to $N = 9 dot 10^18$ expressible as $a^2 b^3$ with $a, b >= 2$, each counted once. Split by whether $n$ is a perfect square.

== Non-squares

If $n = a^2 b^3$ has an odd prime exponent then the representation with $b$ squarefree is forced ($b$ is the product of the odd-exponent primes) and unique, and any odd exponent of $a^2 b^3$ is automatically $>= 3$, so it exists. Squarefree $b >= 2$ exactly captures the non-squares; $a >= 2$ must still be demanded since a squarefree cube $b^3$ admits no other representation. Hence the non-square count is
$
A = sum_(b >= 2 "squarefree") max(0, floor(sqrt(N \/ b^3)) - 1),
$
a sum over $b$ up to $(N\/4)^(1\/3) approx 1.3 dot 10^6$ with exact integer square roots.

== Squares

$n = m^2$ is expressible iff $b$ is itself a square $c^2$ (as $b^3 = n \/ a^2$ is a square), i.e. iff $m = a c^3$ with $a, c >= 2$. Distinct $m <= M = sqrt(N)$ give distinct $n$, so count the $m$ having a cube divisor $c^3 >= 8$ with cofactor $>= 2$. Having any cube divisor $c >= 2$ is the same as not being cubefree, and the only non-cubefree $m$ where every witness fails ($m = c^3$ forced, no proper divisor $2 <= d < c$) are the cubes of primes:
$
B = (M - sum_(d <= M^(1\/3)) mu(d) floor(M / d^3)) - pi(M^(1\/3)).
$
$F(N) = A + B$. Checks: $F(100) = 2$, $F(2 dot 10^4) = 130$, $F(3 dot 10^6) = 2014$, plus a brute force agreeing for every $N <= 3000$.

#pagebreak()
#link("https://projecteuler.net/problem=635")[= Problem 635: Subset Sums]

Solution: 689294705

$A_q(n)$ counts the $n$-element subsets of ${1, dots, q n}$ with sum divisible by $n$; we need $S_2(10^8) + S_3(10^8) mod (10^9 + 9)$ where $S_q(L) = sum_(p <= L "prime") A_q(p)$.

== Roots-of-unity filter

For a primitive $d$-th root of unity $omega$ with $d | n$, each residue class mod $d$ appears $q n \/ d$ times among $1 dots q n$, so the subset generating function collapses: $product_(k=1)^(q n)(1 + z omega^k) = (1 - (-z)^d)^(q n \/ d)$, whose $z^n$ coefficient is $plus.minus binom(q n \/ d, n \/ d)$. Averaging over the $n$ filters and grouping by order $d$ gives, for an odd prime $p$,
$
A_q (p) = 1/p (binom(q p, p) + (p - 1) q),
$
and $A_q(2) = (binom(2q, 2) - q) \/ 2$. Both match brute force, and $S_2(10) = 554$.

== Binomials at five million primes

The remaining work is $binom(2p, p)$ and $binom(3p, p)$ modulo $10^9 + 9$ for every prime $p <= 10^8$. Stream the factorial $k!$ once for $k$ up to $3 dot 10^8$, recording its value whenever $k$ hits $p$, $2p$ or $3p$ for a prime $p$ (three pointer walks over the already-sorted multiples), then assemble each binomial from the recorded factorials with two Fermat inversions. About $3 dot 10^8$ modular products in total under `numba`. Check: $S_2(100) + S_3(100) = 100433628 + 855618282$ modulo $10^9 + 9$.

#pagebreak()
#link("https://projecteuler.net/problem=637")[= Problem 637: Flexible Digit Sum]

Solution: 49000634845039

One step inserts plus signs into the base-$B$ digits of $n$ and adds; $f(n, B)$ is the least number of steps to reach a single digit, and $g(n, B_1, B_2)$ sums the $i <= n$ with $f(i, B_1) = f(i, B_2)$. We need $g(10^7, 10, 3)$.

== Classifying $f$

Merging adjacent digits $a, b$ changes a split sum by $a(B - 1) >= 0$, so the plain digit sum is the _minimum_ split sum. Hence $f(i, B) = 1$ exactly when $d s_B (i) < B$, and $f(i, B) = 2$ exactly when some proper split sum $v$ has $d s_B (v) < B$. Moreover $f$ never exceeds $3$ in range: the finest split gives $f(i) <= 1 + f(d s_B (i))$, the digit sums are at most $70$ (base $10$) and $30$ (base $3$), and every value that small has $f <= 2$ — the smallest base-$3$ number with $f = 3$ is $1781$.

== The exists-test

Classification therefore reduces to an existence test over proper splits: a DFS over cut positions accumulates completed parts and exits as soon as a finished split's sum lands in the precomputed table of "digit sum $< B$" values, trying single-digit parts first since the finest splits hit most often. Base $10$ has at most $2^7$ splits per number; base $3$ up to $2^14$, but a third of all $i$ resolve instantly through the digit-sum precheck, nearly all the rest exit within a few nodes, and full traversals occur only for the very rare $f = 3$ numbers (ten of them below $3^11$, with striking digit patterns like $1, 2, 0, dots, 0, 2, 2, 2, 2, 2$). Checks: $g(100, 10, 3) = 3302$ as given, and both classifiers agree with a brute-force recursive $f$ for every $i <= 3^10$.

#pagebreak()
#link("https://projecteuler.net/problem=638")[= Problem 638: Weighted Lattice Paths]

Solution: 18423394

$C(a, b, k)$ sums $k^(A(P))$ over the monotone lattice paths $P$ of an $a times b$ grid, $A$ being the enclosed area; we need $sum_(k=1)^7 C(10^k + k, 10^k + k, k) mod (10^9 + 7)$.

Summing $q^("area")$ over lattice paths is the combinatorial definition of the Gaussian binomial coefficient,
$
C(a, b, k) = binom(a + b, a)_q |_(q = k) = product_(i=1)^(a) (1 - q^(b + i)) / (1 - q^i) quad (q != 1),
$
and which side of the path carries the area is immaterial (transposing the grid swaps the conventions without changing the sum). Each factor uses the next power of $q$, so a running power and running product evaluate the whole thing in $O(a)$ modular multiplications with one Fermat inversion at the end. No factor vanishes modulo $p = 10^9 + 7$: the order of $q$ divides $p - 1 = 2 dot 500000003$, far beyond $2 dot 10^7 + 14$. The $k = 1$ term is the plain central binomial. Checks: brute-force path enumeration on small grids, and the given $C(10000, 10000, 4) equiv 395913804$.

#pagebreak()
#link("https://projecteuler.net/problem=639")[= Problem 639: Summing a Multiplicative Function]

Solution: 797866893

$f_k$ is multiplicative with $f_k (p^e) = p^k$ for every $e >= 1$; we need $sum_(k=1)^(50) S_k (10^12) mod (10^9 + 7)$ with $S_k (n) = sum_(i <= n) f_k (i)$.

== Convolving off the powerful part

Write $f_k = "id"_k * c_k$ (Dirichlet convolution). Matching prime powers gives $c_k (p) = 0$ and $c_k (p^e) = p^k - sum_(i=1)^(e) p^(i k) c_k (p^(e-i))$, so $c_k$ is supported on _powerful_ numbers — only about $2.4 dot 10^6$ of them lie below $10^12$. Then
$
S_k (N) = sum_("powerful" m <= N) c_k (m) dot P_k (floor(N\/m)), quad P_k (x) = sum_(i <= x) i^k.
$

== Evaluation

For each $k$, a DFS over primes $p <= 10^6$ generates every powerful $m$ together with its running $c_k$-product, the prime-power values produced on the fly from the recurrence. Quotients below $10^6$ hit a precomputed prefix-power table; the roughly $2400$ powerful $m < 10^6$ have large quotients, for which $P_k$ — a polynomial of degree $k + 1$ — is evaluated by Lagrange interpolation from $k + 2$ sample points. Fifteen seconds in `numba` for all fifty $k$.

Checks: the given $S_1(10) = 41$, $S_1(100) = 3512$, $S_2(100) = 208090$, $S_1(10^4) = 35252550$ and $sum_(k <= 3) S_k (10^8) equiv 338787512$, plus a brute-force multiplicative sieve for $n <= 10^5$, $k <= 4$.

#pagebreak()
#link("https://projecteuler.net/problem=640")[= Problem 640: Shut the Box]

Solution: 50.317928

Bob rolls two dice $(x, y)$ each turn and must toggle card $x$, card $y$, or card $x + y$ among twelve cards, winning when all are face down; we need the expected number of turns under the optimal strategy, to six decimals.

The game is a $4096$-state Markov decision process over bitmasks of face-down cards. The optimal expectation satisfies
$
E[s] = 1 + 1/36 sum_("rolls") min_(a in {x, y, x+y}) E[s xor 2^(a-1)], quad E["goal"] = 0,
$
a stochastic shortest-path problem solved by Gauss–Seidel value iteration (sweeping states in place) until values move by less than $10^(-13)$. Toggling makes revisits possible, but the optimal policy reaches the goal with probability bounded away from zero each turn, so iteration converges geometrically. Alice's analogue — four cards, two fair coins valued $1$ or $2$ — is the same MDP in miniature; reproducing her given optimum $5.673651$ validates the solver, alongside a Monte-Carlo simulation of the computed greedy policy.

#pagebreak()
#link("https://projecteuler.net/problem=641")[= Problem 641: A Long Row of Dice]

Solution: 793525366

$n = 10^36$ dice all start showing $1$; for $j = 2 dots n$ every $j$-th die is turned (incrementing its face, with $6$ wrapping to $1$). $f(n)$ counts the dice showing $1$ at the end.

== Reduction to a divisor condition

Die $i$ is turned $d(i) - 1$ times, so it ends on $1$ iff $d(i) equiv 1 (mod 6)$. Odd $d$ forces $i = m^2$, and with $m = product p^e$, $d(i) = product (2e + 1)$, whose factors are $1, 0, 2 mod 3$ according to $e equiv 0, 1, 2 (mod 3)$. So the condition is: every exponent of $m$ avoids $e equiv 1 (mod 3)$ (in particular $m$ is powerful) and the number of exponents with $e equiv 2 (mod 3)$ is even.

== Bijection and Mertens

Each allowed exponent decomposes uniquely as $e = 2u + 3v$ with $u in {0, 1}$, giving a bijection $m <-> a^2 b^3$ with $a$ squarefree, where $u$-parity is $mu(a)$. With $Y = sqrt(10^36) = 10^18$,
$
A(Y) = sum_(b^3 <= Y) Q(floor(sqrt(Y\/b^3))), quad B(Y) = sum_(b^3 <= Y) M(floor(sqrt(Y\/b^3))), quad f = (A + B)/2,
$
with $Q$ the squarefree count and $M$ the Mertens function. $Q(z) = sum_(d^2 <= z) mu(d) floor(z\/d^2)$ costs $(Y\/b^3)^(1\/4)$ per term — about $4 dot 10^6$ operations in all. A sieved Mertens table to $4 dot 10^7$ covers every $b >= 9$; the eight larger arguments (up to $10^9$) use the classic quotient-block recursion $M(x) = 1 - sum_(k >= 2) M(floor(x\/k))$ with memoisation. Checks: $f(100) = 2$ and $f(10^8) = 69$ as given, plus a brute divisor-count sieve at several cutoffs up to $10^7$.

#pagebreak()
#link("https://projecteuler.net/problem=642")[= Problem 642: Sum of Largest Prime Factors]

Solution: 631499044

$F(N) = sum_(i=2)^N f(i)$ with $f$ the largest prime factor; we need $F(201820182018) mod 10^9$.

== Three regimes

Grouping $i = p m$ by its largest prime gives $F(N) = sum_p p dot Psi(N\/p, p)$ with $Psi(y, p)$ counting the $p$-smooth $m <= y$. A Lucy–Hedgehog sieve over the quotient lattice supplies the prime-counting function $pi(v)$ and the prime-sum function $S(v)$ (kept modulo $10^9$ — the sieve uses only ring operations) at every $v = floor(N\/k)$. Then:

- For $p > sqrt(N)$ every $m <= N\/p < p$ is automatically smooth, so the contribution is $p floor(N\/p)$, summed in quotient blocks against $S$.
- For $root(3, N) < p <= sqrt(N)$ we have $p^2 >= N\/p$, so a non-smooth $m <= N\/p$ contains exactly one prime $q > p$, with multiplicity one and cofactor below $p$: $Psi(N\/p, p) = floor(N\/p) - sum_(p < q <= N\/p) floor(N\/(p q))$, evaluated in quotient blocks against $pi$. Because the block count per prime is only $N\/p^2$, all these walks total a few million steps.
- The handful of primes with $p^3 <= N$ (up to $5865$, about $770$ of them) are handled by an in-place ascending array DP over the same lattice, applying $Psi(v, p) = Psi(v, "prev") + Psi(v\/p, p)$ one prime at a time and reading off $Psi(N\/p, p)$ after each.

Checks: the given $F(10) = 32$, $F(100) = 1915$, $F(10^4) = 10118280$, plus agreement with a brute-force largest-prime-factor sieve at several irregular cutoffs up to $10^7$. Runs in about ten seconds.

#pagebreak()
#link("https://projecteuler.net/problem=643")[= Problem 643: $2$-Friendly]

Solution: 968274154

$f(n)$ counts pairs $1 <= p < q <= n$ with $gcd(p, q) = 2^t$, $t > 0$; we need $f(10^11) mod (10^9 + 7)$.

== Reducing to the totient summatory function

$gcd(p, q) = 2^t$ exactly when $p = 2^t p'$, $q = 2^t q'$ with $gcd(p', q') = 1$, so with $Phi(m) = sum_(k <= m) phi(k)$ and the coprime pairs $p' < q' <= m$ numbering $sum_(q' = 2)^m phi(q') = Phi(m) - 1$,
$
f(n) = sum_(t >= 1) (Phi(floor(n / 2^t)) - 1).
$

== Sublinear $Phi$

Pairing each fraction $p\/q$ in lowest terms with all its multiples gives the classic identity $sum_(d >= 1) Phi(floor(n\/d)) = n(n+1)\/2$, hence the recursion
$
Phi(n) = (n(n+1)) / 2 - sum_(d = 2)^(n) Phi(floor(n / d)),
$
evaluated by grouping equal quotients, memoising, and reading arguments below $2 dot 10^7$ from a sieved prefix table — about $O(n^(2\/3))$ work. Every argument that ever appears is a quotient $floor(10^11 \/ k)$, so the cache is shared across all powers of two. Checks: $f(10^2) = 1031$ and $f(10^6) = 321418433$.

#pagebreak()
#link("https://projecteuler.net/problem=645")[= Problem 645: Every Day Is a Holiday]

Solution: 48894.2174

Each emperor's uniformly random birthday becomes a holiday, and any day flanked by two holidays becomes one too; $E(D)$ is the expected number of emperors until the whole $D$-day (circular) year is holidays. We need $E(10000)$ to four decimals.

== Independent missed sets

The flanking rule closes gaps of exactly one day, so the year completes precisely when no two cyclically adjacent days are both un-drawn: the missed set must be an independent set of the cycle $C_D$, of which there are $N_k = D/(D-k) binom(D-k, k)$ of size $k$. Conditioning on the exact missed set and counting surjections,
$
P(T <= t) = sum_k N_k dot "Surj"(t, D - k) \/ D^t.
$

== Collapsing the sums

Summing $E[T] = sum_(t >= 0) P(T > t)$ turns each surjection term into a geometric series, leaving inner sums $sum_j (-1)^j binom(m, j) \/ (k + j)$, which the Beta-integral identity evaluates to $(k-1)! thin m! \/ (m+k)!$. Everything collapses to the closed form
$
E(D) = D H_D - D^2 sum_(k=1)^(floor(D\/2)) r_k / k, quad r_k = ((D-k-1)! thin (D-k)!) / ((D-2k)! thin D!),
$
with $r_1 = 1\/D$ and the ratio $r_(k+1) \/ r_k = (D-2k)(D-2k-1) \/ ((D-k)(D-k-1))$. Every term is positive — no cancellation — so extended-precision accumulation gives far more than four decimals. Checks: $E(2) = 1$, $E(5) = 31\/6$, $E(365) = 1174.3501$.

#pagebreak()
#link("https://projecteuler.net/problem=646")[= Problem 646: Bounded Divisors]

Solution: 845218467

$S(n, L, H)$ sums $lambda(d) dot d$ (Liouville function times divisor) over the divisors of $n$ in $[L, H]$; we need $S(70!, 10^20, 10^60) mod (10^9 + 7)$.

$70!$ has about $3.5 dot 10^12$ divisors — far too many to enumerate — but its $19$ distinct primes split into two halves whose divisor counts are both near the square root, about $1.9 dot 10^6$ (the split greedily balances the product of exponent-plus-ones). Meet in the middle: every divisor factors uniquely as $d = a b$ across the halves, and $lambda(d) d = (lambda(a) a)(lambda(b) b)$. Sorting the $b$-side by value with exact-integer prefix sums of $lambda(b) b$, the constraint $L <= a b <= H$ becomes a contiguous window $[ceil(L\/a), floor(H\/a)]$ located by bisection on exact integers — no floating-point boundary risk — contributing $lambda(a) a$ times a prefix difference. All arithmetic stays in exact big integers, reduced only at the end, which also lets the given checks $S(10!, 100, 1000) = 1457$, $S(15!, 10^3, 10^5) = -107974$ and $S(30!, 10^8, 10^12) = 9766732243224$ be verified exactly.

#pagebreak()
#link("https://projecteuler.net/problem=647")[= Problem 647: Linear Transformations of Polygonal Numbers]

Solution: 563132994232918611

For odd $k$ there exist positive integers $(A, B)$ with $A P_n + B$ always $k$-gonal; $F_k (N)$ sums $A + B$ over pairs with $max(A, B) <= N$, and we need $sum_k F_k (10^12)$ over all odd $k$.

== Pell forces the family

With $c = k - 2$ (odd), the $n$-th $k$-gonal number satisfies $8c P_n + (c-2)^2 = x^2$, $x = 2c n - (c - 2)$ — so $P$ is $k$-gonal exactly when that quantity is a square with $x equiv -(c-2) (mod 2c)$. If $A P + B$ is $k$-gonal for every $P_n$, then $y^2 = A x^2 + D$ must hold along a whole arithmetic progression of $x$; Pell orbits are exponentially sparse, so $A$ must be a perfect square $a^2$, and then $(y - a x)(y + a x) = D$ admits unboundedly many $x$ only when $D = 0$. Hence $B = (a^2 - 1)(c - 2)^2 \/ (8c)$ and the index congruence demands $2c | (a - 1)(c - 2)$. For odd $c$, $gcd(2c, c - 2) = 1$, so this is simply $a equiv 1 (mod 2c)$; writing $a = 2c t + 1$ makes the divisibility of $B$ automatic ($t(c t + 1)$ is always even), giving the complete family
$
A = (2c t + 1)^2, quad B = t(c t + 1)(c - 2)^2 \/ 2, quad t >= 1.
$
For $c = 1$ this is the classic triangular family $9T + 1$, $25T + 3$, $49T + 6$, …, and for $c = 3$ the pentagonal $49P + 2$.

== Summation

Enumerate odd $c$ and $t >= 1$ with $2c t + 1 <= 10^6$ and $B <= N$, summing $A + B$ exactly. Checks: an exhaustive brute-force search over $A, B <= 1200$ for $k = 3, 5, 7, 9, 11$ finds exactly the family, and the given $sum_k F_k (10^3) = 14993$ is reproduced.

#pagebreak()
#link("https://projecteuler.net/problem=648")[= Problem 648: Skipping Squares]

Solution: 301483197

A sum starts at $0$ and repeatedly gains $+1$ with probability $rho$, else $+2$, stopping on a perfect square (or past $10^18$); $f(rho)$, the expected number of squares skipped, is a polynomial $sum_k a_k rho^k$, and we need $F(1000) = sum_(k <= 1000) a_k mod 10^9$.

== Skip probabilities

With $q = 1 - rho$, the chance the walk ever visits a point $d$ ahead solves a two-term recurrence with roots $1$ and $-q$: $h(d) = (1 + q(-q)^d)\/(1 + q)$. Skipping square $m^2$ — having just landed on $m^2 + 1$ — therefore has probability $1 - h(2m) = q(1 - q^(2m))\/(1 + q)$, and the first skip from $0$ has probability $q$, so
$
f = sum_(m >= 1) q^m / (1+q)^(m-1) product_(j=1)^(m-1) (1 - q^(2 j)).
$

== The denominators cancel

Each factor $(1 - q^(2j))\/(1 + q) = (1 - q)(1 + q^2 + dots + q^(2j - 2))$, so
$
f = sum_(m >= 1) rho^(m-1) q^m product_(j=1)^(m-1) [j]_(q^2),
$
an all-integer series with no division — term $m$ starts at order $rho^(m-1)$, so modulo $rho^1001$ only $m <= 1001$ contribute (which is also why the $10^18$ cap never disturbs these coefficients), and the running product needs ever fewer terms as $m$ grows: about $sum (1001 - m)^2 approx 3 dot 10^8$ multiply-adds modulo $10^9$ in `numba`, a few seconds.

Checks: $a_0 = 1$, $a_1 = 0$, $a_5 = -18$, $a_10 = 45176$, $F(10) = 53964$ and $F(50) equiv 842418857$, all as given.

#pagebreak()
#link("https://projecteuler.net/problem=649")[= Problem 649: Low-Prime Chessboard Nim]

Solution: 924668016

$c$ distinguishable coins sit on an $n times n$ board; a move shifts one coin left or up by $2$, $3$, $5$ or $7$. $M(n, c)$ counts the starting arrangements that the first player wins; we need the last nine digits of $M(10000019, 100)$.

Each coin is an independent impartial game — the sum of two copies of the one-dimensional subtraction game with set ${2, 3, 5, 7}$, whose Grundy sequence is periodic with period $9$: $(0, 0, 1, 1, 2, 2, 3, 3, 4)$ (verified against a direct mex computation). A coin on $(x, y)$ has Grundy value $g(x) xor g(y)$, and the first player wins exactly when the XOR over all coins is nonzero, so $M(n, c) = n^(2c) - \#{"XOR-zero arrangements"}$.

The per-coin Grundy distribution is the XOR-convolution square of the per-axis distribution, and the $c$-fold XOR convolution evaluated at $0$ diagonalises under the Walsh–Hadamard transform over $(ZZ\/2)^3$:
$
\#"zero" = 1/8 sum_(s=0)^(7) w_s^c, quad w_s = sum_v (-1)^("popcount"(s and v)) "cnt"_2 [v].
$
Since the modulus $10^9$ is not prime, exact Python integers (the powers have only about $1400$ digits) sidestep the division by $8$. Checks: $M(3, 1) = 4$, $M(3, 2) = 40$, $M(9, 3) = 450304$.

#pagebreak()
#link("https://projecteuler.net/problem=650")[= Problem 650: Divisors of Binomial Product]

Solution: 538319652

With $B(n) = product_(k=0)^n binom(n, k)$ and $D(n) = sigma(B(n))$, we need $S(20000) = sum_(k <= 20000) D(k) mod (10^9 + 7)$.

Writing each binomial in factorials collapses the product: $B(n) = (n!)^(n+1) \/ F(n)^2$ where $F(n) = product_(k <= n) k!$ is the superfactorial, so for every prime $p$
$
e_p (B(n)) = (n + 1) thin e_p (n!) - 2 thin e_p (F(n)).
$
Walk $n$ from $1$ to $20000$, adding the factorisation of $n$ (smallest-prime-factor sieve) to a running $e_p(n!)$ table and accumulating $e_p(F(n))$. The exponent of _every_ prime changes at each step because of the $(n+1)$ weight, so the divisor sum
$
D(n) = product_(p <= n, thin e_p > 0) (p^(e_p + 1) - 1) / (p - 1)
$
is recomputed in full each time — roughly $sum_n pi(n) approx 2.6 dot 10^7$ modular exponentiations under `numba`, with the largest exponent $(n+1) e_2(n!) approx 4 dot 10^8$ still comfortably in `int64`. Checks: $S(5) = 5736$, $S(10) = 141740594713218418$, and $S(100) equiv 332792866$.

#pagebreak()
#link("https://projecteuler.net/problem=651")[= Problem 651: Patterned Cylinders]

Solution: 448233151

Stickers tile an infinite cylinder in an $a$-periodic axial grid with $b$ stickers around the circumference, so patterns are colourings of the $ZZ_a times ZZ_b$ torus; $f(m, a, b)$ counts patterns with exactly $m$ colours up to all rigid motions, and we need $sum_(i=4)^(40) f(i, F_(i-1), F_i) mod 10^9 + 7$.

== The group is $D_a times D_b$

Axial translations, rotations about the axis, reflections in planes containing or perpendicular to the axis, and end-over-end flips act coordinatewise as $(x, theta) -> (plus.minus x + s, plus.minus theta + t)$: the symmetry group is exactly the product of two dihedral groups, of order $4 a b$.

== Burnside by cycle types

Cycles of a product permutation obey $c(g times h) = sum gcd(|gamma|, |delta|)$ over cycle pairs, so grouping $D_a$ and $D_b$ elements by cycle type (rotations of order $d | a$: $phi.alt(d)$ elements with $a\/d$ cycles of length $d$; reflections: fixed points plus transpositions by parity) evaluates the $j$-colour orbit count $B_j$ in $O(d(a) thin d(b))$ exact cycle counts, with $j^c$ by modular exponentiation and the division by $|G|$ via a modular inverse. Exactly $m$ colours follows by inclusion–exclusion $f(m) = sum (-1)^(m-j) binom(m, j) B_j$.

Checks: brute-force orbit enumeration over the full group for small $(a, b, m)$, the given $f(2,2,3) = 11$, $f(3,2,3) = 56$, $f(2,3,4) = 156$, and the given residues of $f(8,13,21)$ and $f(13,144,233)$. The full Fibonacci sum runs in about a second.

#pagebreak()
#link("https://projecteuler.net/problem=653")[= Problem 653: Frictionless Tube]

Solution: 1130658687

Marbles of diameter $20$ mm bounce elastically in a tube sealed at the west end, with pseudo-random gaps and directions; $d(L, N, j)$ is the distance the $j$-th marble travels before its centre reaches the open east end. We need $d(10^9, 10^6 + 1, 5 dot 10^5 + 1)$.

== Pass-through equivalence

Identical elastic marbles never overtake one another, and an equal-mass collision merely exchanges velocities — so the dynamics are those of non-interacting points passing through each other, with marble labels read off in sorted order. The diameters are removed by the standard shrink $y_i = x_i - 20(i - 1) - 10$, which turns the wall into a reflection at $0$, adjacent contact into coincidence of points, and the gap data into prefix sums $y_i = g_1 + dots + g_i$. Each point then moves ballistically (westbound ones bounce off the wall once), marble $j$'s centre is the $j$-th order statistic plus a fixed offset, and since a marble's speed is always $v$, its travelled distance is just $v$ times its exit time — the first moment the $j$-th smallest point reaches $E = L - 10 - 20(j - 1)$.

== Event scan

Each point crosses $E$ upward exactly once (at $E - y$ eastbound, $E + y$ after a bounce), and a westbound point starting above $E$ additionally dips below at $y - E$. Sorting these $plus.minus 1$ events and scanning for the first instant the below-$E$ count drops to $j - 1$ (simultaneous events processed together) gives the exit time exactly in integers with $v = 1$. Checks: the three given values, plus a full event-driven simulation of the actual colliding marbles for the small cases.

#pagebreak()
#link("https://projecteuler.net/problem=654")[= Problem 654: Neighbourly Constraints]

Solution: 815868280

$T(n, m)$ counts $m$-tuples of positive integers in which every two adjacent entries sum to at most $n$; we need $T(5000, 10^12) mod (10^9 + 7)$.

== Cheap iteration, deep index

For $m >= 2$ every entry lies in $[1, n-1]$, and the transfer matrix $A[a][b] = [a + b <= n]$ acts by reversed prefix sums: $(A v)(a) = S(n - a)$ with $S$ the prefix sums of $v$. So consecutive terms $T(m) = bold(1)^T A^(m-1) bold(1)$ cost only $O(n)$ each — but $10^12$ of them is out of reach, and powering the $4999 times 4999$ matrix directly is too. Instead, generate the first $2(n-1) + 30$ terms by iteration, recover the minimal linear recurrence with Berlekamp–Massey over $"GF"(p)$ — its order is exactly $n - 1$, confirmed experimentally across many $n$ — and jump to the $10^12$-th term with Kitamasa: square-and-multiply of $x^(m-2)$ modulo the recurrence's characteristic polynomial, schoolbook $O(d^2)$ per multiplication with $d = 4999$ and about $40$ squarings.

Checks: $T(3, 4) = 8$, $T(5, 5) = 246$, the two given residues $T(10, 100)$ and $T(100, 10)$, and the full BM-plus-Kitamasa pipeline reproducing directly iterated terms at scattered indices for $n = 10$ and $n = 57$.

#pagebreak()
#link("https://projecteuler.net/problem=655")[= Problem 655: Divisible Palindromes]

Solution: 2000008332

Count the palindromes below $10^32$ divisible by $P = 10000019$ (e.g. nine palindromes below $10^5$ are divisible by $109$).

An $L$-digit palindrome is determined by its outer $ceil(L\/2)$ digits, digit $i$ (most significant first) contributing with weight $w_i = 10^i + 10^(L-1-i) mod P$ — or $10^((L-1)\/2)$ for the middle digit of an odd length. For each length, run a DP over the whole residue ring $ZZ_P$: keep the count vector of prefixes by remainder and fold in each digit position's ten choices as cyclic shifts of the vector by $d dot w_i$ (two contiguous `numpy` slice-adds per shift; the leading digit ranges over $1 dots 9$ only). The count of $L$-digit palindromes divisible by $P$ is the final entry at remainder $0$, and the answer sums $L = 1 dots 32$ — about $sum_L ceil(L\/2) = 272$ positions of ten $10^7$-length folds each. Check: a direct brute force over all palindromes below $10^7$ for the modulus $109$, length by length.

#pagebreak()
#link("https://projecteuler.net/problem=657")[= Problem 657: Incomplete Words]

Solution: 219493139

A word over an alphabet of $alpha$ letters is incomplete if it omits at least one letter; $I(alpha, n)$ counts incomplete words of length at most $n$. We want $I(10^7, 10^12)$ modulo $10^9 + 7$.

Classify words by the number $i$ of distinct letters they actually use. The number of words of length $<= M$ confined to a fixed $i$-letter sub-alphabet is $sum_(j=0)^M i^j$, and there are $binom(N, i)$ such sub-alphabets; inclusion-exclusion over $i$ then gives
$
I(N, M) = sum_(i=0)^(N-1) (-1)^(N-1-i) binom(N, i) sum_(j=0)^M i^j.
$
The geometric inner sum is $(i^(M+1) - 1) \/ (i - 1)$ for $i >= 2$, equals $M + 1$ for $i = 1$, and equals $1$ for $i = 0$. The powers $i^(M+1)$ are taken modulo $p$ with the exponent reduced modulo $p - 1$ by Fermat, and the binomial coefficients are streamed multiplicatively, so the whole sum is one $O(N log M)$ pass. Checks: $I(3,0) = 1$, $I(3,2) = 13$, $I(3,4) = 79$.

#pagebreak()
#link("https://projecteuler.net/problem=658")[= Problem 658: Incomplete Words II]

Solution: 958280177

$S(k, n) = sum_(alpha <= k) I(alpha, n)$, where $I$ counts words of length at most $n$ over an $alpha$-letter alphabet that miss at least one letter; we need $S(10^7, 10^12) mod (10^9 + 7)$.

== Swapping the inclusion–exclusion

As in Problem 657, $I(alpha, n) = sum_(i=0)^(alpha-1) (-1)^(alpha-1-i) binom(alpha, i) G(i)$ with $G(i) = sum_(j <= n) i^j$. Swapping the order of summation,
$
S(k, n) = sum_(i=0)^(k-1) G(i) thin W(i), quad W(i) = sum_(alpha=i+1)^(k) (-1)^(alpha-1-i) binom(alpha, i).
$

== A recurrence for the column sums

Applying Pascal's rule $binom(alpha, i) = binom(alpha+1, i+1) - binom(alpha, i+1)$ inside $W(i)$ telescopes the alternating column sum into the next column:
$
W(i) = 2 W(i + 1) + (-1)^(k-i-1) binom(k+1, i+1) - 1, quad W(k - 1) = k,
$
verified directly for small $k$. A single downward sweep with precomputed factorials therefore yields every $W(i)$, while each $G(i) = (i^(n+1) - 1)\/(i - 1)$ costs one modular power (exponent reduced by Fermat) and a batch inverse. About $10^7$ modexps in `numba`, under three seconds.

Checks: the given $S(4, 4) = 406$, $S(8, 8) = 27902680$, $S(10, 100) equiv 983602076$; the Problem 657 values $I(3, 0) = 1$, $I(3, 2) = 13$, $I(3, 4) = 79$ recovered as $S(3, n) - S(2, n)$; and brute-force word enumeration for $alpha <= 4$.

#pagebreak()
#link("https://projecteuler.net/problem=659")[= Problem 659: Largest Prime]

Solution: 238518915714422000

$P(k)$ is the largest prime dividing two successive terms of $n^2 + k^2$; we need the last $18$ digits of $sum_(k=1)^(10^7) P(k)$.

== Reduction to one factorisation

If $p$ divides both $n^2 + k^2$ and $(n+1)^2 + k^2$ it divides their difference $2n + 1$, and then $4(n^2 + k^2) = (2n + 1)^2 - 2(2n + 1) + 1 + 4k^2 equiv 4k^2 + 1 (mod p)$. Conversely, for any odd $p | 4k^2 + 1$, choosing $n$ with $2n + 1 equiv 0$ makes $p$ divide both terms. Hence $P(k)$ is simply the largest prime factor of $4k^2 + 1$ — consistent with the problem's $n^2 + 3$ example, where $4 dot 3 + 1 = 13$.

== Sieving the quadratic

The $10^7$ values $4k^2 + 1$ are factored collectively with the same polynomial sieve as Problem 621: for each prime $p equiv 1 (mod 4)$ up to $2 dot 10^7 + 1$, a square root of $-1$ (Euler's criterion) gives the two roots of $(2k)^2 equiv -1 (mod p)$, walked as index progressions with full power extraction. The sieve bound squared exceeds $max (4k^2 + 1)$, so any post-sieve remainder is $1$ or a single prime — necessarily the largest. Summation is modulo $10^18$. Check: brute-force factorisation for all $k <= 2000$.

#pagebreak()
#link("https://projecteuler.net/problem=660")[= Problem 660: Pandigital Triangles]

Solution: 474766783

An integer triangle is $n$-pandigital if it has a $120 degree$ angle and its three sides written in base $n$ use each of the $n$ digits exactly once. We sum the largest sides over all such triangles for $9 <= n <= 18$.

== Factoring out the triangles

With $a, b$ adjacent to the $120 degree$ angle and $c$ opposite (strictly the largest side), $c^2 = a^2 + a b + b^2$, equivalently $(2c)^2 - (2b + a)^2 = 3a^2$. Writing $3a^2 = u v$ with $u = 2c - 2b - a$ recovers $b = (v - u - 2a)\/4$ and $c = (u + v)\/4$, so every triangle arises from its smaller adjacent side $a$ by walking the divisor pairs of $3a^2$ (built from a smallest-prime-factor sieve) and keeping the integral ones with $b > a$.

== Digit budget

Lengths obey $L_a <= L_b <= L_c <= L_b + 1$ (since $c < a + b < 2b$) and sum to $n$, so $L_a <= floor(n\/3) <= 6$ and $L_c <= 9$: only $a < 18^6$ and $c < 18^9$ can ever fit. For a fixed triangle the total digit count is non-increasing in the base while the target $n$ increases, so at most one base can match; each candidate is length-checked per base with early exit and digit-counted for pandigitality only on an exact fit. Check: an independent brute force over all $(a, b)$ pairs reproduces the complete $n = 9$ set — exactly $(104, 621, 679)$ and the statement's $(217, 248, 403)$.

#pagebreak()
#link("https://projecteuler.net/problem=661")[= Problem 661: A Long Chess Match]

Solution: 646231.2177

After every game the match continues with probability $q = 1 - p$; counting the games after which $A$ leads, with $S_t$ the score difference (steps $+1, -1, 0$ with probabilities $p_A, p_B, p_d$),
$
EE_A = sum_(t >= 1) q^(t-1) P(S_t >= 1).
$

== Resolvent and closed form

With $phi(x) = p_A x + p_d + p_B\/x$ the step generating function, $P(S_t = s) = [x^s] phi(x)^t$, and summing the geometric series in $t$ extracts positive-power coefficients of $1\/(1 - q phi(x))$. Factoring $1 - q phi(x) = -(q p_A\/x)(x - r_1)(x - r_2)$ with $r_1 < 1 < r_2$ the roots of $q p_A x^2 - (1 - q p_d) x + q p_B = 0$, the Laurent expansion in the annulus $r_1 < |x| < r_2$ gives $[x^s] = r_2^(-s) \/ (q p_A (r_2 - r_1))$ for $s >= 1$, and the geometric sum in $s$ collapses everything to
$
EE_A (p_A, p_B, p) = 1 / (q^2 thin p_A thin (r_2 - r_1)(r_2 - 1)).
$
Sanity: $EE_A (0.25, 0.25, 0.5) = 2 - sqrt(2)$ exactly. The discriminant $(1 - q p_d)^2 - 4 q^2 p_A p_B$ loses about nine digits to cancellation at the $H$-sum's parameters ($p_B - p_A = 1\/k^2$, $p = 1\/k^3$), so evaluation uses extended-precision long doubles; the whole sum is instantaneous.

Checks: both given $EE_A$ examples, an independent truncated distribution-DP cross-check, and $H(3) approx 6.8345$ as given.

#pagebreak()
#link("https://projecteuler.net/problem=662")[= Problem 662: Fibonacci Paths]

Solution: 860873428

Alice steps from $(a, b)$ to $(a + x, b + y)$ with $x, y >= 0$ whenever $sqrt(x^2 + y^2)$ is a Fibonacci number; $F(W, H)$ counts her paths from the origin to $(W, H)$, and we need $F(10^4, 10^4) mod (10^9 + 7)$.

Useful steps have both components at most $10^4$, so Fibonacci lengths run up to $10946$ (usable only split diagonally, e.g. $10946^2 = 4870^2 + 9804^2$); for each length the axis steps and every Pythagorean decomposition $x^2 + y^2 = F^2$ (found by scanning $x$ and testing $F^2 - x^2$ for squareness) give $88$ steps in total. Then a plain path-count DP fills the $(W+1) times (H+1)$ grid row by row, each cell summing its $88$ predecessors — sources are always final before being read since steps with $x = 0$ only look left within the current row. About $10^8$ cells under `numba`, stored as `int32` to keep the table at $400$ MB. Checks: $F(3, 4) = 278$ and $F(10, 10) = 215846462$.

#pagebreak()
#link("https://projecteuler.net/problem=663")[= Problem 663: Sums of Subarrays]

Solution: 1884138010064752

Tribonacci-driven point updates $A[t_(2i-2) mod n] += 2(t_(2i-1) mod n) - n + 1$ hit an array of length $n = 10000003$; $M_n (i)$ is the maximal contiguous subarray sum after step $i$, and the answer sums $M$ over steps $10000001 dots 10200000$ only.

No queries occur during the first $10^7$ steps, so they are applied as raw point updates. A square-root decomposition then takes over: each of the $approx 3200$ blocks stores the classic max-subarray summary (total, best prefix, best suffix, best subsegment — all non-empty). Each queried step recomputes the one touched block by a linear scan and folds the block summaries left to right with the standard merge $"best" = max("best"_l, "best"_r, "suf"_l + "pre"_r)$, reading $M$ off the final fold — about $7000$ operations per step, $200000$ steps, a few seconds in `numba`. The tribonacci pair is advanced two indices at a time modulo $n$.

Checks: the worked $n = 5$ example with $S(5, 6) = 32$, the given $S(5, 100) = 2416$, $S(14, 100) = 3881$, $S(107, 1000) = 1618572$ against a per-step Kadane brute force, and a split-consistency check $S(107, 600 + 400) - S(107, 600)$.

#pagebreak()
#link("https://projecteuler.net/problem=666")[= Problem 666: Polymorphic Bacteria]

Solution: 0.48023168

Species $S_(k,m)$ has $k$ types; a type-$i$ bacterium picks $j$ uniform in $[0, m)$, reads $q = r_(i m + j) mod 5$ (with $r_0 = 306$, $r_(n+1) = r_n^2 mod 10007$), and then dies ($q = 0$), clones ($q = 1$), mutates to type $2i$ ($q = 2$), splits into three of type $i^2 + 1$ ($q = 3$), or spawns type $i + 1$ alongside itself ($q = 4$), all indices mod $k$. $P_(k,m)$ is the extinction probability from a single $alpha_0$; we need $P_(500,10)$.

== Multitype branching process

Let $x_i$ be the probability a lineage seeded by one type-$i$ bacterium eventually dies out. First-step analysis over the $m$ equally likely choices gives
$
x_i = 1/m sum_(j < m) g_q (x), quad cases(
  g_0 = 1\,,
  g_1 = x_i^2\,,
  g_2 = x_(2i mod k)\,,
  g_3 = x_(i^2+1)^3\,,
  g_4 = x_i thin x_(i+1)\,
).
$
The required probability is the _minimal_ nonnegative fixed point of this monotone system. Iterating from $x = 0$, the iterates increase monotonically to that minimal root; in-place Gauss–Seidel updates accelerate the otherwise linear convergence, and a few thousand sweeps pin down eight decimals essentially instantly.

Checks: the given $P_(2,2) = 0.07243802$ (the original $alpha\/beta$ species $S_(2,2)$), $P_(4,3) = 0.18554021$ and $P_(10,5) = 0.53466253$.

#pagebreak()
#link("https://projecteuler.net/problem=668")[= Problem 668: Square Root Smooth Numbers]

Solution: 2811077773

A number is square-root smooth when all of its prime factors are strictly below its square root; we count those up to $N = 10^10$.

A number $n$ fails to be square-root smooth exactly when it has a prime factor $p >= sqrt(n)$. Such a $p$ is unique — two primes that large would multiply past $n$ — and it is the largest prime factor, with $n = p m$ where $m = n\/p <= sqrt(n) <= p$. Conversely each pair (prime $p$, integer $1 <= m <= p$ with $p m <= N$) yields a distinct non-smooth number, so
$
\#{"not smooth" <= N} = sum_(p <= N) min(p, floor(N\/p)), quad S(N) = N - sum_(p <= N) min(p, floor(N\/p)).
$
Split at $R = floor(sqrt(N))$: primes $p <= R$ contribute $p$ (a direct sum of primes), while primes $p > R$ contribute $floor(N\/p)$, grouped as $sum_(q=1)^(R-1) q (pi(N\/\/q) - pi(N\/\/(q+1)))$ with the prime-counting values supplied by a Lucy_Hedgehog sieve in $O(N^(3\/4))$. As a check, $S(100) = 29$.

#pagebreak()
#link("https://projecteuler.net/problem=686")[= Problem 686: Powers of Two with Leading Digits]

Solution: 193060223

Using the fractional part of $j dot log_10 2$ to detect a leading block of $123$, count the powers of two that start with $123$ until the $678910$th.

#pagebreak()
#link("https://projecteuler.net/problem=692")[= Problem 692: Siegbert and Jo]

Solution: 842043391019219959

The game is Fibonacci Nim. Writing the Fibonacci numbers as $F_1 = 1, F_2 = 2, F_3 = 3, F_4 = 5, dots$, the smallest opening move that still guarantees a win, $H(N)$, is the smallest Fibonacci number appearing in the Zeckendorf representation of $N$ (every integer is uniquely a sum of non-consecutive Fibonacci numbers). The examples confirm this: $18 = 13 + 5$ gives $H(18) = 5$, while $H(8) = 8$ since $8$ is itself Fibonacci.

We need $G(n) = sum_(k=1)^n H(k)$. Let $S(n) = G(n)$ and let $F_m$ be the largest Fibonacci number with $F_m <= n$. Each $k in [F_m, n]$ equals $F_m + r$ with $0 <= r <= n - F_m < F_(m-1)$; for $r = 0$ the smallest part is $F_m$, and for $r >= 1$ the smallest part of $k$ is the smallest part of $r$. Therefore
$
S(n) = A(m) + F_m + S(n - F_m), quad A(m) := S(F_m - 1),
$
and $A(m)$ satisfies its own recurrence $A(m) = A(m-1) + F_(m-1) + A(m-2)$ with $A(1) = 0, A(2) = 1$. Both run in $O(log n)$. Check: $G(13) = 43$.

#pagebreak()
#link("https://projecteuler.net/problem=694")[= Problem 694: Cube-full Divisors]

Solution: 1339784153569958487

A number is cube-full if every prime dividing it does so to power at least $3$ (with $1$ cube-full). With $s(n)$ the number of cube-full divisors of $n$ and $S(N) = sum_(i=1)^N s(i)$, swapping the order of summation gives
$
S(N) = sum_(d "cube-full", d <= N) floor(N \/ d),
$
because a fixed cube-full $d$ divides exactly $floor(N\/d)$ integers up to $N$.

Every cube-full number factors uniquely as $d = a^3 b^4 c^5$ with $b, c$ squarefree and $gcd(b, c) = 1$: split the primes of $d$ by exponent modulo $3$, sending $e equiv 0$ into $a$, $e equiv 1$ into the $b^4$ factor, and $e equiv 2$ into the $c^5$ factor. Hence
$
S(N) = sum_(#[b, c "sqfree, coprime"]) thin sum_(a >= 1, thin a^3 b^4 c^5 <= N) floor(N \/ (a^3 b^4 c^5)),
$
where the inner term is $floor(M\/a^3)$ with $M = floor(N \/ (b^4 c^5))$. Since cube-full numbers number about $N^(1\/3)$, the total work is roughly $N^(1\/3) zeta(4\/3) zeta(5\/3) approx 7 dot 10^6$ for $N = 10^18$. Checks: $S(16) = 19$, $S(100) = 126$, $S(10000) = 13344$.

#pagebreak()
#link("https://projecteuler.net/problem=695")[= Problem 695: Random Rectangles]

Solution: 0.1017786859

Three points are drawn uniformly in the unit square; each pair spans an axis-aligned rectangle of area $|Delta x| dot |Delta y|$, and we need the expected value of the median (second biggest) of the three areas. Sorting the points by $x$-coordinate makes the two $x$-gaps $(u, v)$ have density $6(1 - u - v)$ on the simplex, the $y$-gaps $(p, q)$ an independent copy of the same law, and the $y$-ranks of the $x$-sorted points an independent uniform permutation $sigma in S_3$. For fixed $(u, v)$ and $sigma$, the three areas are _linear_ forms $alpha p + beta q$, with coefficients drawn from $u$, $v$, $u + v$ according to $sigma$.

Linearity is the key: in the $(p, q)$-plane any two of the forms agree on a ray through the origin, so the median form is constant on the angular sectors these rays cut out. A sector meets the simplex in a triangle $O V_1 V_2$ with $V_1, V_2$ on the line $p + q = 1$, and there a one-line calculation gives
$
integral.double (A p + B q)(1 - p - q) thin d p thin d q = (|det(V_1, V_2)| (L(V_1) + L(V_2))) / 24 .
$
Summing over sectors gives the inner integral $M_sigma (u, v)$ exactly, no numerical work needed. Since $M_sigma$ is homogeneous of degree $1$, substituting $tau = v\/u$ collapses the outer two dimensions to one:
$
E = 3 integral_0^oo overline(M)(tau) / (1 + tau)^3 thin d tau, quad overline(M)(tau) = 1/6 sum_sigma M_sigma (1, tau).
$
The integrand is piecewise smooth with a handful of kinks, so panel-wise Gauss--Legendre quadrature (with $tau -> 1\/tau$ for the unbounded half) converges to full double precision; two panel resolutions agree to $10^(-11)$, and a Monte Carlo simulation agrees to four digits.

#pagebreak()
#link("https://projecteuler.net/problem=696")[= Problem 696: Mahjong]

Solution: 436944244

A winning hand is $t$ triples (chows or pungs, each within one suit) plus one pair, drawn from $s$ suits of $n$ numbers with four copies of each tile. Counting hands means counting tile _multisets_, so decompositions must not be double counted. Two reductions make the count factor. First, the multiset sizes per suit force the structure: a suit holding only triples has size $equiv 0 mod 3$ while the pair suit has size $equiv 2$, so which suit holds the pair is determined by the multiset itself, and the suits are otherwise independent. Second, the same argument applies inside a suit to the maximal runs of consecutive used numbers, so the pair run is also forced. With
$
A(n, k) = \#{"suit multisets decomposable into" k "triples"}, quad B(n, k) = \#{dots k "triples + pair"},
$
the answer is $s dot [x^t] B(x) A(x)^(s - 1)$.

Runs contain at most $3t + 2$ numbers, so $A$ and $B$ come from run profiles: count run multisets of each length once each, then place $g$ ordered runs of total length $L$ among $n$ numbers in $binom(n - L + 1, g)$ ways. "Counted once" is handled mechanically: scanning a run left to right, a decomposition is tracked by how many chows still extend over the current and next number, giving a small NFA (with at most two chows starting per position, since three equal a pung triple, and a flag for the pair); the _subset construction_ over this NFA counts each multiset exactly once, by existence of an accepting decomposition rather than by decompositions. Finally $A(x)^(s-1)$ for $s - 1 approx 10^8$ is $exp((s-1) log A)$ on power series truncated at $x^31$ over $ZZ_p$. Checks: $w(4,1,1) = 20$, $w(9,1,4) = 13259$, $w(9,3,4) = 5237550$, $w(1000,1000,5) equiv 107662178$, plus brute-force agreement for $w(5,1,2)$ and $w(4,2,1)$.

#pagebreak()
#link("https://projecteuler.net/problem=697")[= Problem 697: Randomly Decaying Sequence]

Solution: 4343871.06

With $X_0 = c$ and $X_i = X_(i-1) U_i$ where $U_i$ is uniform on $(0,1)$, taking logarithms gives $log X_n = log c - G$ where $G = -sum log U_i$ is a sum of $n$ independent $"Exp"(1)$ variables, i.e. $G ~ "Gamma"(n, 1)$. The requirement $P(X_n < 1) = 0.25$ becomes $P(G > log c) = 1\/4$, so $log c$ is the $75$th percentile of a Gamma$(10^7, 1)$ distribution.

The regularized incomplete gamma function $P(a, x)$ is evaluated with the classical pair of expansions, the series for $x < a + 1$ and the Lentz continued fraction for $x >= a + 1$, both scaled by $exp(x ln x - x - ln Gamma(a))$ via `lgamma` to avoid overflow at $a = 10^7$. Bisection on $x$ then solves $P(a, x) = 0.75$; the percentile sits near $a + 0.6745 sqrt(a)$ by the normal approximation, which brackets the root tightly. Dividing by $ln 10$ converts to base $10$. Check: $n = 100$ gives $log_10 c approx 46.27$ as stated.

#pagebreak()
#link("https://projecteuler.net/problem=698")[= Problem 698: 123 Numbers]

Solution: 57808202

A $123$-number uses only digits $1, 2, 3$, and the count of each digit that appears must itself be a $123$-number. The target index $1 1 1 dots 1$ (with $123$ ones) is about $1.1 dot 10^17$, so the answer has a few dozen digits; a digit count of a number that short must lie in the small fixed set ${0, 1, 2, 3, 11, 12, 13, 21, 22, 23, 31, 32, 33}$ ($0$ meaning the digit is absent).

Counting is then elementary combinatorics with exact integers: for a fixed total length, the admissible digit-count triples $(c_1, c_2, c_3)$ are those from the set above summing to the length, each contributing a multinomial $binom(c_1 + c_2 + c_3, c_1, c_2, c_3)$ arrangements. Accumulating lengths locates the length of the sought number, and the number itself is recovered most-significant-digit first: place the smallest digit whose completion count still reaches the remaining index. Checks against the brute force: $F(4) = 11$, $F(10) = 31$, $F(40) = 1112$, $F(1000) = 1223321$, and $F(6000) = 2333333333323$.

#pagebreak()
#link("https://projecteuler.net/problem=699")[= Problem 699: Triffle Numbers]

Solution: 37010438774467572

Write $n = 3^a m$ with $3 divides.not m$. The fraction $sigma(n)\/n$ has lowest-form denominator $3^k$ with $k > 0$ exactly when $m | sigma(n)$ and $v_3 (sigma(n)) < a$. Because $sigma$ is multiplicative and $q divides.not sigma(q^f)$, every component $q^f$ of $m$ must be covered by the $sigma$-contributions of the _other_ components: the divisibility structure is a directed graph of components covering each other, and solutions can be built by a DFS over factorizations.

Each node carries $n$, its components, and the factored $sigma(n)$. While some component prime is uncovered, the search branches on the new component $q^f$ that covers the largest uncovered prime $p$, i.e. $p | sigma(q^f)$; for $f = 1$ this means $q equiv -1 mod p$, found by walking the arithmetic progression with a primality test, and for $f >= 2$ candidates come from a sieve with $sigma(q^f) mod p$ evaluated by Horner. When everything is covered, the node records $n$ if $v_3 (sigma(n)) < a$ and then branches on free extensions (new primes dividing $sigma(n)$) and on _cycle seeds_ $q dot w^g$ with $q | sigma(w^g)$, $q > w$, $g >= 2$ — the only way a new mutually-covering cluster disconnected from $sigma(n)$ can begin, since a $g = 1$ pair would force $w = q - 1$, which is even. (The number $252 = 2^2 dot 3^2 dot 7$, where $7 | sigma(2^2)$ and $2^3 | sigma(7)$, is the smallest example needing such a seed.)

Robin-type bounds give $sigma(w)\/w < 7$ for all $w <= 10^14$, so an uncovered prime $p$ at node $n$ needs future multiplication at least $p\/7$: nodes with $n dot max(p\/7, 2) > N$ are dead, and an uncovered new prime $q$ requires $q^2 <= 7 N\/n$ (covered primes only $q <= N\/n$ — enforcing this distinction matters, as the looser bound briefly admitted a handful of just-over-the-limit numbers). Deduplication is by visited $n$, since $a = v_3(n)$ fixes the root. The search reproduces the brute force exactly up to $10^8$ (full solution lists) and the given $T(100) = 270$ and $T(10^6) = 26089287$; every recorded $n$ at $N = 10^14$ was also re-verified independently by direct factorization of $sigma(n)$.

#pagebreak()
#link("https://projecteuler.net/problem=700")[= Problem 700: Eulercoin]

Solution: 1517926517777556

With $N = 1504170715041707$ and the prime $M = 4503599627370517$, the sequence $N n mod M$ produces an _Eulercoin_ whenever a term is strictly smaller than every earlier term. Brute-forcing $n$ upward finds the early (large-valued) coins quickly but stalls long before the small ones appear, so the two ends are searched separately.

Walking $n = 1, 2, dots$ and tracking the running minimum of $N n mod M$ (updated as $v <- (v + N) mod M$) yields the coins of large value, which occur at small $n$. For the small-valued coins, observe that a value $c$ first appears at step $n_c = c N^(-1) mod M$; the inverse exists because $M$ is prime. Such a $c$ is a coin exactly when it reaches the sequence before every smaller value, i.e. when $n_c < n_(c')$ for all $0 < c' < c$. Scanning $c$ upward while tracking the running minimum of $n_c$ (updated as $n_c <- (n_c + N^(-1)) mod M$) therefore lists every small-valued coin. Both passes are plain increment-and-compare loops with no multiplication, so nothing overflows; the union of the two coin sets, summed, is the answer. A crossover threshold of $2 dot 10^7$ comfortably covers both regimes.

#pagebreak()
#link("https://projecteuler.net/problem=701")[= Problem 701: Random Connected Area]

Solution: 13.51099836

Each of the $W times H = 49$ cells is black with probability $1\/2$, and we want the expected size of the largest edge-connected black region, $E(7, 7)$. Enumerating all $2^49$ colourings is hopeless, so the grid is swept one row at a time with a connected-component DP.

== State

After some rows are processed, only the bottom (frontier) row can still grow into the next row. A state records: the black cells of the frontier row grouped into the connected components that touch it, the accumulated size of each such _active_ component, and the largest size among components that have already _finished_ (no longer touch the frontier). Each state carries an integer count of the colourings producing it.

== Transition

Given a frontier pattern and the black mask of the next row, a union-find merges horizontally adjacent new cells and joins each new black cell to the active component directly above it. New component sizes are the merged old sizes plus the fresh black cells; any old component that no new cell touches is finished, updating the running maximum. The purely structural part of this step -- which components merge, which finish -- depends only on the frontier pattern and the next mask, not on the sizes, so it is precomputed once for every (pattern, mask) pair. Each state is then packed into one integer (a pattern id, four six-bit component sizes, and a six-bit running maximum) so the hot loop runs under Numba.

After the last row every active component finishes; summing $"count" times ("largest size")$ over the final states and dividing by $2^49$ gives $E(7, 7)$. The method reproduces the given $E(2, 2) = 1.875$ and $E(4, 4) = 5.76487732$.

#pagebreak()
#link("https://projecteuler.net/problem=702")[= Problem 702: Jumping Flea]

Solution: 622305608172525546

A flea starts at the centre of a regular hexagonal table of side $N$ ruled into unit triangles; each jump moves it to the midpoint between its position and one of the six table corners, and $J(T)$ is the least number of jumps landing it strictly inside triangle $T$. $S(N)$ sums $J$ over the upward triangles in the upper half; we need $S(123456789)$.

== Where the flea can be

Work in coordinates $z = a + b omega$ with $omega = e^(i pi\/3)$ (so $omega^2 = omega - 1$): the triangle grid is the lattice $ZZ[omega]$, the corners are $N u$ for the six units $u = plus.minus 1, plus.minus omega, plus.minus omega^2$, and the table is the hexagonal ball $norm(z) <= N$ of the gauge $norm(a + b omega) = max(|a|, |b|, |a + b|)$. Jumping from $p$ towards corner $N u$ gives $(p + N u)\/2$, so after $k$ jumps the position is $N z \/ 2^k$ with $z = sum_(j=1)^k 2^(j-1) u_j$ ranging over a set $M_k$. A breadth-first enumeration of jump sequences confirms (exactly, for all $k <= 9$, with $|M_9| = 589056$) the clean characterisation
$ M_k = {z in ZZ[omega] : z "odd", norm(z) <= 2^k - 1}, $
where _odd_ means $z in.not 2 ZZ[omega]$. Oddness is forced because $z equiv u_k$ modulo $2 ZZ[omega]$ and units are odd; the content of the claim is that every odd point of the radius-$(2^k - 1)$ hexagon is reachable. Since the interior of every triangle of the table lies strictly inside the hexagon $norm(z) < N 2^k$, the gauge constraint is automatic, and $J(T)$ is simply the least $k$ for which $2^k dot "int"(T)$ contains a point of $N dot ("odd lattice")$.

== A per-triangle formula

The upward triangle anchored at $(a, b)$ has interior ${s > a, space t > b, space s + t < a + b + 1}$, so it is hit at step $k$ iff there are odd $(s, t) in ZZ^2$ with $N s > 2^k a$, $N t > 2^k b$ and $N(s + t) < 2^k (a + b) + 2^k$. Let $x = (-a) mod N$ and $y = (-b) mod N$, and let $V_k (x) = 2^k x mod N$, replacing the value $0$ by $N$. The smallest admissible gaps $N s - 2^k a$ and $N t - 2^k b$ are then $V_k (x)$ and $V_k (y)$ — except that when both attain their minima with _even_ $s, t$, one gap must be enlarged by $N$ to restore oddness. The hit condition collapses to
$ J = min{k >= 1 : V_k (x) + V_k (y) + N dot [#[both] V_k "even"] < 2^k}, $
which depends only on the residues $(x, y)$. Folding the problem's domain (upward triangles with $b in [0, N - 1]$, $a in [-N, N - 1 - b]$) onto residues gives $S(N) = sum w(x, y) J(x, y)$ over $[0, N)^2$ with weight $w = 1 + [x = 0] + [x >= 1 and ((y >= 1 and x + y > N) or y = 0)]$. This formula reproduces a direct flea simulation for $N <= 11$ and the given $S(123)$ and $S(12345)$, but evaluating it per pair is $O(N^2 log N)$ — far too slow.

== Disjoint levels

Let $m$ be the bit length of $N$, so $2^(m-1) < N < 2^m$ ($N$ odd). For a level $j <= m - 1$ the penalty $N$ exceeds $2^j$ and is unpayable, so the pairs hit at level $j$ are exactly those with $u = V_j (x) and v = V_j (y)$ satisfying $u, v >= 1$, $u + v < 2^j$, not both even; the originating $x$ is recovered from $u$ through $a = gamma_j u mod 2^j$ with $gamma_j = (-N)^(-1) mod 2^j$. Crucially, these level sets are _pairwise disjoint_: a pair hit at level $j$ has $V_(j') = 2^(j' - j) u$ for $j' > j$, and both values are even, so the penalty applies and cannot be paid at any later level below $m$. Hence each pair has at most one hit below level $m$, every pair is hit by level $m + 2$, and
$ S = sum_j j dot "hw"_j quad #[with] quad "hw"_j = #[weight of pairs first hit at level] j. $

The companion weight $[x + y > N]$ translates, at level $j$, into a carry: $x + y > N$ iff $gamma_j u + gamma_j v$ wraps modulo $2^j$, and the identity $["carry"] = (g(u) + g(v) - g(u + v)) \/ 2^j$ with $g(t) = gamma_j t mod 2^j$ converts the weighted count into running prefix sums of $g$ — $O(2^j)$ time per level, $O(2^m)$ in total.

== The top three levels

At level $m$ the map $x |-> V = 2^m x mod N$ is a bijection of $[1, N - 1]$, and the hit condition becomes $V + W <= 2^m - 1$ (not both even) or $V + W <= 2^m - 1 - N$ (both even). Pairs hit at some level $j < m$ are hit at level $m$ again _except_ in a corner region (both $2^(m-j) u < N$, forcing an unpayable both-even penalty when $2^(m-j)(u + v) + N >= 2^m$); the corner is counted with the same sliding-window prefix sums (and its sub-region still failing level $m + 1$ likewise). Level $m + 1$ fails only when both $V, W <= (N-1)\/2$ (making $2V mod N, 2W mod N$ both even) and $V + W >= 2^m - (N-1)\/2$; level $m + 2$ always succeeds. The carry weight at the top uses $G(t) = 2^(-m) t mod N$, with one subtlety: the carry identity counts $x + y >= N$, so the diagonal $V + W = N$ — exactly $x + y = N$, which the weight excludes — is subtracted. The boundary lines $x = 0$ and $y = 0$ have $J in {m, m+1}$ with closed-form counts. Assembling the inclusion–exclusion of first-hit weights gives an $O(N + 2^m)$ algorithm, about six seconds for $N = 123456789$; it agrees with the brute-force formula for hundreds of odd $N$ up to $20001$ and with all four values given in the problem.

#pagebreak()
#link("https://projecteuler.net/problem=703")[= Problem 703: Circular Logic II]

Solution: 843437991

The map $f$ sends a length-$n$ bit sequence to its left shift with a new last bit $b_1 and (b_2 xor b_3)$, and $S(n)$ counts the functions $T : B^n -> B$ with $T(x) and T(f(x)) = "false"$ for every $x$. Reading $T$ as the set ${x : T(x) = "true"}$, the condition says no $x$ and its image $f(x)$ are both chosen: $S(n)$ is the number of _independent sets_ in the functional graph of $f$ on $2^n$ vertices (edges $x - f(x)$). We need $S(20)$ modulo $1001001011$.

A functional graph is a disjoint union of components, each a single cycle with in-trees feeding into it, and independent sets multiply across components. Process the trees leaf-first: give every vertex $"dp"_0 = "dp"_1 = 1$ (ways with it unselected / selected) and, when a vertex $v$ is finished, fold it into its image $p = f(v)$ by
$
"dp"_0 [p] *= "dp"_0 [v] + "dp"_1 [v], quad "dp"_1 [p] *= "dp"_0 [v],
$
the second rule forbidding a selected vertex next to a selected parent. Peeling by in-degree leaves exactly the cycle vertices, each already carrying its trees' contributions $A_v = "dp"_0 [v]$ and $B_v = "dp"_1 [v]$. A cycle is then counted by the trace of the product of transfer matrices $M_v = mat(A_v, B_v; A_v, 0)$, which correctly handles self-loops (forcing that vertex unselected) and $2$-cycles, and the result is the product over all cycles. Only additions and multiplications occur, so the modulus need not be prime. The method reproduces $S(3) = 35$ and $S(4) = 2118$, and $2^20$ vertices are handled in about a second.

#pagebreak()
#link("https://projecteuler.net/problem=704")[= Problem 704: Factors of Two in Binomial Coefficients]

Solution: 501985601490518144

Here $g(n, m)$ is the exponent of $2$ in $binom(n, m)$, $F(n) = max_m g(n, m)$, and we need $S(N) = sum_(n=1)^N F(n)$ for $N = 10^16$.

By Kummer's theorem $g(n, m)$ equals the number of carries when $m$ and $n - m$ are added in base $2$, equivalently $s(m) + s(n - m) - s(n)$, where $s$ is the binary digit sum. Maximising over $m$ asks for the split of $n$ whose binary addition carries the most. A short recursion on the parity of $n$ shows that the maximum of $s(a) + s(b)$ over $a + b = n$, minus $s(n)$, equals the gap between the most and least significant set bits of $n + 1$:
$
F(n) = floor(log_2 (n + 1)) - v_2(n + 1),
$
which matches the given $F(10) = 3$, $F(100) = 6$ and agrees with brute force.

Re-indexing $k = n + 1$ turns the sum into $S(N) = A(N + 1) - B(N + 1)$, where $A(M) = sum_(k=1)^M floor(log_2 k)$ and $B(M) = sum_(k=1)^M v_2(k)$. The first is a sum over geometric blocks of constant $floor(log_2 k)$, and by Legendre's formula $B(M) = M - "popcount"(M)$. Both use exact integer bit operations, reproducing the given $S(100) = 389$ and $S(10^7) = 203222840$.

#pagebreak()
#link("https://projecteuler.net/problem=705")[= Problem 705: Total Inversion Count of Divided Sequences]

Solution: 480440153

The master sequence $G(N)$ concatenates the decimal digits of all primes below $N$ with every zero digit removed. Replacing each digit by one of its divisors gives a _divided sequence_; $F(N)$ sums the inversion count (pairs $i < j$ whose value at $i$ exceeds the value at $j$) over all such sequences, and we need $F(10^8) mod (10^9 + 7)$.

Treat each position's divisor choice as independent. For a digit $d$ let $alpha_d (a) = [a | d] \/ tau(d)$ be the chance of choosing value $a$, where $tau(d)$ counts the divisors of $d$. By linearity over the $T = product_i tau(d_i)$ divided sequences, each potential inversion contributes its probability times $T$:
$
F = T sum_(i < j) sum_(a > b) alpha_(d_i)(a) alpha_(d_j)(b).
$
Because only nine digit values occur, this is one left-to-right pass: keep $"prefix"[a] = sum_(i "seen") alpha_(d_i)(a)$, and for each new digit $d$ add $sum_b alpha_d (b) sum_(a > b) "prefix"[a]$ to the running expectation, then fold $d$ into the prefix and multiply $tau(d)$ into $T$. Working modulo the prime $10^9 + 7$ (so the divisions by $tau(d)$ become modular inverses) and sieving the primes below $10^8$, the Numba digit pass gives the result. The exact-arithmetic version reproduces $F(20) = 3312$ and $F(50) = 338079744$.

#pagebreak()
#link("https://projecteuler.net/problem=706")[= Problem 706: 3-Like Numbers]

Solution: 884837055

Here $f(n)$ counts the non-empty substrings of the decimal string of $n$ that are divisible by $3$, and $n$ is _3-like_ when $3 | f(n)$. We need $F(10^5)$, the number of $10^5$-digit $3$-like numbers, modulo $10^9 + 7$.

A substring is divisible by $3$ exactly when its digit sum is, so with prefix sums $S_0 = 0$ and $S_k = (d_1 + dots + d_k) mod 3$ the divisible substrings are the index pairs $a < b$ with $S_a equiv S_b$. Hence
$
f(n) = sum_(r=0)^2 binom(c_r, 2), quad c_r = abs({k : S_k = r}).
$
Modulo $3$ this collapses dramatically: $binom(c, 2) equiv 1$ precisely when $c equiv 2 space (mod 3)$ and is $0$ otherwise, so
$
f(n) equiv abs({r : c_r equiv 2 space (mod 3)}) quad (mod 3),
$
and $n$ is $3$-like iff that count is a multiple of $3$ (i.e. $0$ or $3$). Only the residues $c_r mod 3$ matter.

This gives a digit-DP whose state is the current prefix residue together with $(c_0, c_1, c_2) mod 3$ — just $3 dot 27 = 81$ states. Appending a digit congruent to $delta$ moves the residue and increments the new residue's count; a digit class has weight equal to how many decimal digits lie in it, namely $(4, 3, 3)$ for residues $(0, 1, 2)$, except the leading digit forbids $0$ and so uses $(3, 3, 3)$. Iterating $10^5$ positions and summing the states whose count of "$equiv 2$" residues is a multiple of $3$ gives the answer; the recurrence reproduces $F(2) = 30$ and $F(6) = 290898$.

#pagebreak()
#link("https://projecteuler.net/problem=707")[= Problem 707: Lights Out]

Solution: 652907799

Selecting a cell toggles it and its edge-neighbours, and $F(w, h)$ counts the states of a $w times h$ grid reducible to all-off. Over $bb(F)_2$ the toggles form a symmetric matrix $A$, the reachable (solvable) states are exactly its column space, so $F(w, h) = 2^("rank" A) = 2^(w h - d(w, h))$ with $d$ the nullity. We want $S(199, 199) = sum_(k=1)^199 F(199, f_k)$ modulo $10^9 + 7$, where $f_k$ is Fibonacci.

A null vector of $A$ is a "quiet" press pattern; collecting the presses of row $i$ into $r_i in bb(F)_2^w$ the quiet condition reads $r_(i-1) + M r_i + r_(i+1) = 0$ with $M$ the $w times w$ tridiagonal all-ones matrix and boundaries $r_0 = r_(h+1) = 0$. Hence $r_(i+1) = M r_i + r_(i-1)$ and $r_(h+1) = P_(h+1)(M) r_1$, where the Fibonacci-type polynomials satisfy $P_0 = 0$, $P_1 = 1$, $P_(m+1) = x P_m + P_(m-1)$. So $d(w, h) = dim ker P_(h+1)(M)$. An irreducible tridiagonal matrix is non-derogatory, so $M$ is similar to the companion matrix of its characteristic polynomial $chi_w$ and $bb(F)_2^w tilde.equiv bb(F)_2 [x] \/ (chi_w)$ with $P_(h+1)(M)$ acting as multiplication; therefore
$
d(w, h) = deg gcd(P_(h+1)(x), chi_w(x)).
$
Here $chi_w$ comes from $D_k = (x + 1) D_(k-1) + D_(k-2)$, and $P_(h+1) mod chi_w$ is the top-left entry of $mat(x, 1; 1, 0)^h$ in $bb(F)_2 [x] \/ (chi_w)$, computed by fast exponentiation even though $h = f_k$ is astronomically large. Finally $F = 2^(w h - d)$ is reduced through Fermat's little theorem. The method reproduces every given value, including $F(7, 11) equiv 270016253$ and $S(5, 7) equiv 346547294$.

#pagebreak()
#link("https://projecteuler.net/problem=708")[= Problem 708: Twos Are All You Need]

Solution: 28874142998632109

Replacing every prime factor of $n$ by $2$ gives $f(n) = 2^(Omega(n))$, where $Omega(n)$ counts prime factors with multiplicity; this is completely multiplicative with $f(p) = 2$. We need $S(N) = sum_(n=1)^N f(n)$ for $N = 10^14$, far too many terms to sieve directly.

Peel the function with Dirichlet convolutions against the constant $1$. Writing $f = 1 * g$ forces $g(p^k) = f(p^k) - f(p^(k-1)) = 2^(k-1)$, and writing $g = 1 * h$ forces $h(p) = 0$ with $h(p^k) = 2^(k-2)$ for $k >= 2$. Because $h(p) = 0$, the multiplier $h$ is supported only on _squarefull_ numbers (every prime exponent at least $2$), of which there are merely $O(sqrt(N))$ below $N$. Unwinding $f = 1 * 1 * h$ gives
$
S(N) = sum_(e "squarefull") h(e) dot D(floor(N \/ e)), quad D(M) = sum_(m=1)^M floor(M \/ m),
$
where the inner double sum over the two copies of $1$ collapses to the divisor-summatory function $D$, evaluated in $O(sqrt(M))$ by the hyperbola method.

The squarefull $e$ are enumerated by a depth-first walk over primes $p <= sqrt(N) = 10^7$, each taken to an exponent of at least two; since $e <= N$ has at most about eight distinct prime factors, an explicit fixed-depth frame stack replaces recursion and keeps everything inside Numba. Overflow is avoided by comparing through division ($p^2 > floor(N\/e)$) rather than forming $e p^2$ directly. The method reproduces the given $S(10^8) = 9613563919$ and runs in a few seconds.

#pagebreak()
#link("https://projecteuler.net/problem=709")[= Problem 709: Even Stevens]

Solution: 773479144

Each day the newest bag is either dropped into the cupboard or used to swallow an _even_ number of the bags currently sitting at top level. A finished packing is therefore a labelled forest in which every bag directly contains an even-sized set of older bags. We need $f(24680) mod 1020202009$, the number of such forests on $n = 24680$ bags.

Relabelling, these are exactly _increasing trees_ whose every node has an even number of unordered children. In the increasing-tree framework a single tree has exponential generating function $T(x)$ satisfying $T'(x) = phi(T(x))$ with the degree series $phi(u) = sum_(j>=0) u^(2j) \/ (2j)! = cosh u$, so
$
T' = cosh T, quad T(0) = 0.
$
A forest is a set of such trees, so its EGF is $e^T$ and $f(n) = n! [x^n] e^T$.

To avoid composing power series, introduce $C = cosh T$ and $S = sinh T$ and differentiate:
$
T' = C, quad S' = C^2, quad C' = S C, quad (e^T)' = C e^T.
$
Reading off coefficients turns each relation into an $O(m)$ convolution for the next term, so all series are built to degree $n$ in $O(n^2)$ time. Every step works modulo the prime $1020202009$, with the divisions by $m + 1$ replaced by modular inverses (computed in linear time). Finally $f(n) = n! dot [x^n] e^T$. The recurrence reproduces the given $f(4) = 5$ and $f(8) = 1385$, and the full computation runs in a few seconds. The sequence begins $1, 1, 2, 5, 16, 61, 272, 1385, dots$.

#pagebreak()
#link("https://projecteuler.net/problem=710")[= Problem 710: One Million Members]

Solution: 1275000

A _twopal_ is a palindromic composition of $n$ that uses at least one part equal to $2$, and $t(n)$ counts them; we want the least $n > 42$ with $10^6 | t(n)$.

Count by complement: $t(n) = P(n) - Q(n)$, where $P$ counts all palindromic compositions and $Q$ counts those that never use a $2$. A palindromic composition is a half-composition followed by its mirror, optionally around a central part, which gives clean generating functions. Allowing every positive part,
$
P(x) = (x + 2x^2) / (1 - 2x^2),
$
while forbidding the part $2$ (parts drawn from ${1, 3, 4, 5, dots}$) gives, after simplifying the half and centre contributions,
$
Q(x) = (x + x^2 + x^6) / (1 - 2x^2 + x^4 - x^6).
$
Both are rational, so their denominators yield constant-coefficient recurrences
$
P_n = 2 P_(n-2), quad Q_n = 2 Q_(n-2) - Q_(n-4) + Q_(n-6),
$
which are iterated modulo $10^6$ from their seed values until $P_n - Q_n equiv 0$. The series reproduces $t(6) = 4$, $t(20) = 824$ and $t(42) = 1999923$, and the first qualifying index past $42$ is $1275000$.

#pagebreak()
#link("https://projecteuler.net/problem=711")[= Problem 711: Binary Blackboard]

Solution: 541510990

Starting from $n$, the players write binary numbers keeping the running total at most $2n$, so they are jointly splitting a budget of $n$ into a composition; Eric wins when the total count of $1$-bits on the board (those of $n$ included) is even. We need $S(N)$, the sum of all $n <= 2^N$ for which Eric can force a win, modulo $10^9 + 7$, for $N = 12345678$.

Each position is captured by the remaining budget $r$, whose turn it is, and the parity of move-popcounts so far, so a minimax over $r$ decides every $n$. Tabulating the winners exposes a purely _syntactic_ rule on the binary string of $n$. If $n$ has even bit-length, Eric wins only for the all-ones number $2^L - 1$. If $n$ has odd bit-length $L = 2j + 1$, drop the leading $1$ and read the remaining $2j$ bits as $j$ pairs (most-significant first) with values in ${0, 1, 2, 3}$; running the automaton
$
F ->^0 F, quad F ->^1 N_3, quad F ->^3 A_3, quad N_3 ->^0 F, quad N_3 ->^1 N_3, quad A_3 ->^3 A_3
$
(every other edge, in particular pair value $2$, is fatal), Eric wins exactly when the run finishes in $F$ or $A_3$. Intuitively a $1$ demands a further valid, non-all-ones tail while a $3$ forces all remaining pairs to be $3$; this was checked against the exhaustive game for every $n < 2^16$.

Summing the winners up to $2^N$ then has three parts. The odd-length winners are counted by a digit-DP over the pair automaton that carries, per state, both the number of runs and the sum of their values, so each length contributes $"(count)" dot 2^(L-1) + "(value sum)"$; advancing one pair is a constant-size update, giving $O(N)$ work overall. The even-length winners contribute $sum_("even" L <= N) (2^L - 1)$ in closed form. Finally $2^N$ itself has bit-length $N + 1$ and is a winner precisely when that length is odd, i.e. when $N$ is even. The method reproduces $S(4) = 46$, $S(12) = 54532$ and $S(1234) equiv 690421393$.

#pagebreak()
#link("https://projecteuler.net/problem=712")[= Problem 712: Exponent Difference]

Solution: 413876461

With $nu_p(n)$ the exponent of $p$ in $n$, $D(n, m) = sum_p abs(nu_p(n) - nu_p(m))$ and $S(N) = sum_(1 <= n, m <= N) D(n, m)$; we want $S(10^12)$ modulo $10^9 + 7$.

Because $D$ is a sum over primes, $S(N)$ splits prime by prime. Fix $p$ and let $a_e = abs({k <= N : nu_p(k) = e}) = floor(N \/ p^e) - floor(N \/ p^(e+1))$. Then the prime's contribution is $sum_(e, f) a_e a_f abs(e - f)$. Writing $abs(e - f)$ as the number of thresholds $t$ separating $e$ and $f$ turns this into $2 sum_(t >= 0) L_t (T - L_t)$ with $L_t = sum_(e <= t) a_e = N - floor(N \/ p^(t+1))$ and total $T = N$. Substituting $s = t + 1$ collapses everything to
$
S(N) = 2 sum_p sum_(s >= 1) floor(N \/ p^s) (N - floor(N \/ p^s)),
$
which already reproduces $S(10) = 210$ and $S(10^2) = 37018$.

For $s >= 2$ only primes $p <= sqrt(N) = 10^6$ contribute, so that part is a direct sieve sum. The $s = 1$ part, $sum_(p <= N) q (N - q)$ with $q = floor(N \/ p)$, is handled by grouping primes into the $O(sqrt(N))$ blocks on which $floor(N \/ p)$ is constant; each block $(N \/ (q+1), N \/ q]$ contributes $q (N - q)$ times the number of primes it contains. Those prime counts at all the values $floor(N \/ i)$ come from one Lucy_Hedgehog sieve, after which the block sum is immediate. The whole computation runs in a few seconds.

#pagebreak()
#link("https://projecteuler.net/problem=713")[= Problem 713: Turán's Water Heating System]

Solution: 788626351539895

The heater needs two working fuses, $m$ of the $N$ are good but unknown, and $T(N, m)$ is the fewest pair-tests guaranteeing a try in which both chosen fuses work. We want $L(N) = sum_(m=2)^N T(N, m)$ for $N = 10^7$.

Model a test of fuses ${i, j}$ as an edge. An adversary may keep answering "fails" as long as some $m$-set of good fuses avoids containing both endpoints of any tested edge, i.e. as long as the tested edges leave an independent set of size $m$. So the tester must lay down edges until no $m$ vertices are mutually untested-adjacent — the minimum number of edges meeting every $m$-subset of the $N$ vertices. This is the Turán-type covering number: making the complement $K_m$-free and as dense as possible (a Turán graph) shows the optimum is to split the $N$ fuses into $k = m - 1$ almost-equal parts and take all within-part pairs,
$
T(N, m) = sum_(i=1)^(m-1) binom(s_i, 2).
$
With $q = floor(N \/ k)$ the balanced split gives $N mod k$ parts of size $q + 1$, and the sum telescopes to the compact form
$
T(N, m) = q N - k dot q (q + 1) \/ 2.
$
This reproduces $T(3, 2) = 3$ and $T(8, 4) = 7$. Finally $L(N) = sum_(k=1)^(N-1) (q N - k q (q+1) \/ 2)$ is summed over the $O(sqrt(N))$ blocks on which $q = floor(N \/ k)$ stays constant, matching $L(10^3) = 3281346$ and running instantly.

#pagebreak()
#link("https://projecteuler.net/problem=714")[= Problem 714: Duodigits]

Solution: 2.452767775565e20

A _duodigit_ uses at most two distinct decimal digits, $d(n)$ is the smallest positive duodigit multiple of $n$, and we want $D(50000) = sum_(n=1)^(50000) d(n)$ to $13$ significant figures.

The numbers split by whether $10 | n$. If $10 divides.not n$, then $d(n)$ turns out to have at most $15$ digits, so generating every duodigit of up to $15$ digits once (a few million, all fitting in a $64$-bit integer), sorting them, and scanning for the first multiple of $n$ yields $d(n)$ directly; a check confirms every such $n <= 50000$ is covered.

If $10 | n$ every multiple ends in $0$, so the duodigit must contain $0$ and its digit set is ${0, x}$ for a single $x in {1, dots, 9}$; here $d(n)$ can reach $21$ digits. For each $x$ a breadth-first search over residues modulo $n$ finds the shortest (then lexicographically least) string of $0$s and $x$s, leading with $x$, that is divisible by $n$; taking the minimum over $x$ gives $d(n)$. Summing both cases as exact big integers and rounding reproduces $D(110) = 11047$, $D(150) = 53312$, $D(500) = 29570988$, and gives $D(50000) approx 2.452767775565 times 10^20$.

#pagebreak()
#link("https://projecteuler.net/problem=715")[= Problem 715: Sextuplet Norms]

Solution: 883188017

$f(n)$ counts $6$-tuples mod $n$ whose sum of squares is coprime to $n$, and $G(n) = sum_(k<=n) f(k)\/(k^2 phi(k))$; we need $G(10^12)$ mod $10^9 + 7$.

== Collapsing the summand

$f$ is multiplicative with $f(p^e) = p^(6(e-1))(p^6 - N_0(p))$, where $N_0(p)$ counts $6$-tuples mod $p$ with square sum $equiv 0$. The classical Gauss-sum evaluation of sums of $2m$ squares gives $N_0(p) = p^5 + (p - 1) p^2 chi_4(p)$ for odd $p$ (the quadratic character of $(-1)^3$) and $N_0(2) = 32$. Hence $g(k) = f(k)\/(k^2 phi(k))$ is multiplicative with
$ g(p^e) = p^(3e) - chi_4(p) p^(3(e-1)), $
which is exactly $(op("Id")_3 * mu chi_4)(p^e)$ — including $p = 2$, where $chi_4(2) = 0$ gives $g(2^e) = 2^(3e)$. A hand computation of $g(1), dots, g(10)$ sums to $3053$, confirming the identity against the given $G(10)$.

== Summation

Therefore $G(n) = sum_d mu(d) chi_4(d) dot T_3(floor(n\/d))$ with $T_3(M) = (M(M+1)\/2)^2$, grouped over quotient blocks. The partial sums $H(x) = sum_(d<=x) mu(d) chi_4(d)$ are needed at all arguments $floor(n\/d)$: since $(mu chi_4) * chi_4 = epsilon$, they satisfy the Mertens-style recurrence $H(x) = 1 - sum_(d>=2) chi_4(d) H(floor(x\/d))$ (the $chi_4$ prefix sum is the periodic pattern $1,1,0,0$). Sieving $H$ linearly to $x_0 = 10^8$ and computing the $10^4$ large arguments by the recurrence in decreasing order gives the standard $O(n^(2\/3))$ algorithm — ten seconds in numba, matching $G(10^5) equiv 157612967$.

#pagebreak()
#link("https://projecteuler.net/problem=716")[= Problem 716: Grid Graphs]

Solution: 238948623

Each of the $H$ rows and $W$ columns of a grid is directed as a whole line; $C(H, W)$ sums the number of strongly connected components over all $2^(H+W)$ orientations. We need $C(10000, 20000)$ mod $10^9 + 7$.

== Structure of the components

Exhaustive checking over every orientation with $H, W <= 4$ established two facts: each orientation has *at most one* nontrivial SCC, and that SCC is exactly the union of the boundaries of all *rectangle cycles* — rectangles $i_1 < i_2$, $j_1 < j_2$ whose lines are directed top $>$, bottom $<$, left $arrow.t$, right $arrow.b$ (type A) or the mirror image (type B). Hence
$ C = 2^(H+W) H W - sum_("orient") |"big SCC"| + N_1, $
where $N_1$ counts orientations containing a cycle. The latter is elementary: a type-A cycle exists iff some $>$ row lies above some $<$ row *and* some $arrow.t$ column lies left of some $arrow.b$ column, and direction sequences avoiding such a pattern are monotone ($H + 1$ of them), so $N_1$ follows by inclusion–exclusion over the two cycle types.

== Counting covered nodes

A node $(i, j)$ lies on a type-A rectangle boundary iff it serves as a top/bottom row point ($X_1(i) Y_1(j)$: row $i$ is $>$ with a $<$ below or $<$ with a $>$ above, and a $arrow.t$ exists at column $<= j$ with a $arrow.b$ at $>= j$) or as a left/right column point ($X_2(i) Y_2(j)$, the transposed conditions), with mirrored clauses $X_3 Y_3, X_4 Y_4$ for type B. Rows and columns are independent, so by inclusion–exclusion over the fifteen nonempty clause subsets, $sum |"big"|$ splits into products of per-axis sums. Each per-index count enumerates the $32$ atomic states — own direction times which directions occur before and after — whose sequence counts are powers of two. The whole computation is $O((H + W))$ and runs in under a second, matching the brute-force table for $H <= 4$, $W <= 5$ and all three given values.

#pagebreak()
#link("https://projecteuler.net/problem=717")[= Problem 717: Summation of a Modular Formula]

Solution: 1603036763131

For an odd prime $p$, $f(p) = floor(2^(2^p) \/ p) mod 2^p$ and $g(p) = f(p) mod p$; we want $G(10^7) = sum_(p < 10^7) g(p)$ over odd primes.

Write $M = 2^p$ and $r = 2^M mod p$. The exact quotient satisfies $p dot floor(2^M \/ p) = 2^M - r$, and because $M >= p$ we have $2^M equiv 0 (mod 2^p)$, so reducing modulo $2^p$ gives $p dot f(p) equiv -r$. Thus $p dot f(p) + r$ is a multiple of $2^p$ that is smaller than $p dot 2^p$, say $p dot f(p) + r = 2^p s$ with $0 <= s < p$. Reading this modulo $p$ and using $2^p equiv 2$ gives $2 s equiv r$, hence $s = r \/ 2 (mod p)$. Finally reducing $p dot f(p) = 2^p s - r$ modulo $p^2$ isolates the wanted residue,
$
g(p) = f(p) mod p = ((2^p s - r) mod p^2) \/ p,
$
where $r = 2^(2^p) mod p$ is found by reducing the exponent modulo $p - 1$. Each prime needs only a handful of modular exponentiations with operands at most $p^2$, so the whole sum to $10^7$ runs in seconds. The formula reproduces $g(3) = 2$, $g(31) = 17$, $G(100) = 474$ and $G(10^4) = 2819236$.

#pagebreak()
#link("https://projecteuler.net/problem=718")[= Problem 718: Unreachable Numbers]

Solution: 228579116

For positive integers $a, b, c$ the equation $17^p a + 19^p b + 23^p c = n$ is solvable for some $n$; the rest are _unreachable_, and $G(p)$ sums them. We want $G(6)$ modulo $10^9 + 7$.

Write $A = 17^p$, $B = 19^p$, $C = 23^p$ and $s = A + B + C$ (the value at $a = b = c = 1$). Substituting $a -> a + 1$ etc. shows $n$ is reachable iff $n - s$ lies in the numerical semigroup $S = angle.l A, B, C angle.r$ of non-negative integer combinations. Since the generators are coprime, $S$ has finitely many gaps, and the unreachable $n > 0$ are exactly ${1, dots, s - 1}$ together with ${s + g : g "a gap of" S}$. Therefore
$
G(p) = s(s - 1) \/ 2 + s dot #h(2pt) "(number of gaps)" + "(sum of gaps)".
$
The gap statistics come from the Apery set modulo the smallest generator $A$: for each residue $i$, $n_i$ is the least element of $S$ with $n_i equiv i (mod A)$, and writing $q_i = n_i \/ A$,
$
"number of gaps" = sum_i q_i, quad "sum of gaps" = sum_i (q_i i + A binom(q_i, 2)).
$
The $n_i$ are computed by the Böcker–Lipták round-robin algorithm, which relaxes each residue cycle once per generator in $O(A)$ time and avoids a priority queue, so the $A = 17^6 approx 2.4 times 10^7$ residues are handled in a couple of seconds. This matches $G(1) = 8253$ and $G(2) = 60258000$.

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
#link("https://projecteuler.net/problem=720")[= Problem 720: Unpredictable Permutations]

Solution: 688081048

A permutation is _unpredictable_ when no three positions $i < j < k$ carry an arithmetic progression $P(i), P(j), P(k)$; equivalently, no average $(x + y)\/2$ of two same-parity values $x, y$ sits positionally between them. We need the lexicographic rank of the first unpredictable permutation of ${1, dots, 2^25}$, modulo $10^9 + 7$.

== Structure of the lexicographic minimum

Parity is the natural lever: a progression needs $x$ and $y$ of equal parity, and mapping the odd values by $v -> (v+1)\/2$ (or the evens by $v -> v\/2$) turns a progression among them into a progression of the half-size problem. A backtracking search for the lex-first unpredictable permutation at $N = 8$ and $16$ exposes the exact pattern: with $F(4) = (1, 3, 2, 4)$ and $h = N\/2$,
$ F(2h) = (#[odd block of] F(h) #[minus its last entry], thick 2, thick #[last odd entry], thick #[remaining even block]), $
where the odd and even blocks are $F(h)$ rescaled onto the odd and even values. Compared with the plain odds-then-evens split, sliding the single value $2$ ahead of the final odd entry is lexicographically cheaper and stays legal: $2$ could only be the middle of $(x, 2, y)$ with $x + y = 4$, and of the values $1, 3$ only the pair with $1$ first could threaten this -- but $3$ lands in the final odd slot, after $2$, never between. The construction reproduces all three given values $S(4) = 3$, $S(8) = 2295$ and $S(32) equiv 641839205$, which pins the interleaving down level by level.

== Ranking

The rank of a permutation is $1 + sum_i L_i (N - 1 - i)!$ where the Lehmer digit $L_i$ counts later values smaller than $P(i)$. Scanning from the right with a Fenwick tree over values gives every $L_i$ in $O(N log N)$ total, and the factorials are accumulated modulo $10^9 + 7$ on the fly. Building $F(2^25)$ takes $24$ doubling steps of array surgery; the whole computation runs in well under a minute.

#pagebreak()
#link("https://projecteuler.net/problem=721")[= Problem 721: High Powers of Irrational Numbers]

Solution: 700792959

With $f(a, n) = floor((ceil(sqrt(a)) + sqrt(a))^n)$, we need $G(n) = sum_(a=1)^(n) f(a, a^2)$ for $n = 5000000$, modulo the prime $999999937$.

If $a = s^2$ is a perfect square the base is just the integer $2s$ and $f(a, a^2) = (2s)^(a^2)$, a single modular power.

Otherwise let $c = ceil(sqrt(a))$ and consider the conjugates $x = c + sqrt(a)$, $y = c - sqrt(a)$. They are the roots of $t^2 - 2c t + (c^2 - a)$, so $x^n + y^n$ is an integer; and since $c - 1 < sqrt(a) < c$ we have $0 < y < 1$, hence $0 < y^n < 1$ and
$
floor(x^n) = x^n + y^n - 1.
$
Compute $x^n = u + v sqrt(a)$ by binary exponentiation in $bb(Z)_p [sqrt(a)]$ (pairs $(u, v)$ with $(u_1 + v_1 sqrt(a))(u_2 + v_2 sqrt(a)) = (u_1 u_2 + a v_1 v_2) + (u_1 v_2 + u_2 v_1) sqrt(a)$); then $x^n + y^n = 2u$ because the conjugate flips the sign of $v$. So $f(a, a^2) = 2u - 1$ modulo $p$.

Each $a$ costs about $log_2 (a^2) approx 45$ ring squarings; the five million values take under a minute with Numba. Checks: $f(5,2) = 27$, $f(5,5) = 3935$, and $G(1000) equiv 163861845$.

#pagebreak()
#link("https://projecteuler.net/problem=722")[= Problem 722: Slowly Converging Series]

Solution: 3.376792776502e132

$E_k (q) = sum_(n >= 1) sigma_k (n) q^n$; we need $E_15 (1 - 2^(-25))$ in scientific notation with twelve digits after the decimal point.

Expanding $sigma_k$ over divisors and swapping sums turns the slowly converging Lambert series into a fast one:
$
E_k (q) = sum_(m >= 1) sum_(j >= 1) j^k q^(j m) = sum_(m >= 1) "Li"_(-k)(q^m),
$
and the negative polylogarithm is a rational function with Eulerian-number numerator,
$
"Li"_(-k)(x) = (sum_(j) A(k, j) thin x^(j+1)) / (1 - x)^(k+1).
$
Near $q = 1$ the $m$th term behaves like $k! \/ (m(1 - q))^(k+1)$, so the new series converges like $sum 1\/m^16$ — about forty terms reach $10^(-25)$ relative accuracy. Each term is evaluated exactly enough with `Decimal` arithmetic at $60$ digits, immune to the $10^132$ magnitude of the answer. All three given values ($E_1$, $E_3$, $E_7$ at their respective $q$) reproduce digit-for-digit.

#pagebreak()
#link("https://projecteuler.net/problem=723")[= Problem 723: Pythagorean Quadrilaterals]

Solution: 1395793419248

A quadrilateral with sides $a, b, c, d$ inscribed in a circle of radius $r$ is _pythagorean_ when $a^2 + b^2 + c^2 + d^2 = 8r^2$. Each side subtends an arc $g_i$ (with $sum g_i = 2 pi$) and has squared length $2r^2 (1 - cos g_i)$, so the condition reads $sum cos g_i = 0$; factoring with sum-to-product formulas shows it holds exactly when a diagonal is a diameter ($g_1 + g_2 = pi$ or $g_2 + g_3 = pi$) or the diagonals are perpendicular ($g_1 + g_3 = pi$). So $f(sqrt(d))$ counts the $4$-subsets of the $n$ lattice points on $x^2 + y^2 = d$ whose convex quadrilateral has a diameter diagonal or perpendicular diagonals.

== Diameter diagonals

An antipodal pair is a _diagonal_ precisely when the other two vertices fall on opposite sides of it, giving $(n\/2)((n-2)\/2)^2$ choices; rectangles (two antipodal pairs, always crossing at the centre) are counted twice, so $D = (n\/2)((n-2)\/2)^2 - binom(n\/2, 2)$.

== Perpendicular diagonals

It remains to count crossing perpendicular pairs of non-diameter chords. A chord ${A, C}$ is determined by its vertex sum $s = A + C$ (its line meets the circle only there), it is perpendicular to $s$, and two chords are perpendicular iff their sums are -- an angle relation $psi_A + psi_C equiv psi_B + psi_D + pi space (mod 2pi)$. Writing each lattice point as $i^t product_j pi_j^(a_j) overline(pi)_j^(e_j - a_j)$ over the Gaussian primes of $d = product p_j^(e_j)$, the prime angles are independent over $QQ pi$, so the relation decouples into $a_j (A) + a_j (C) = a_j (B) + a_j (D)$ for every $j$ together with $t_A + t_C equiv t_B + t_D + 2 space (mod 4)$. Ordered solutions therefore number $64 product_j R(e_j)$ where $R(e) = sum_s r_e (s)^2$ and $r_e (s) = e + 1 - |s - e|$ counts representations $a + a' = s$. Degenerate "chords" $A = C$ and $A = -C$ each contribute $16 product_j W(e_j)$ solutions with $W(e) = sum_a r_e (2a)$, the four degeneracies overlapping in $8n$ tuples; and a perpendicular pair sharing an endpoint is forced into the shape ${A, C}, {A, -C}$, contributing $n(n-2)\/2$ unordered pairs. What survives is the perpendicular pairs on four distinct points.

Exactly half of those cross. Two perpendicular chords cross iff $|s_1|^2 + |s_2|^2 < 4d$ (their midpoint offsets $cos^2 alpha + cos^2 beta < 1$), and negating both endpoints of one chord -- chosen to avoid the cross-antipodal coincidence when one is present -- preserves perpendicularity and distinctness while flipping the inequality, whose equality case would force a shared vertex. Hence
$ Q = 4 (product_j R(e_j) - product_j W(e_j)) + n/2 - (n(n-2))/4, quad f = D + Q. $

== Assembly

$f$ depends only on the exponent signature, so $S$ sums $f$ over the $7 dot 4 dot 3 dot 2^5 = 2688$ divisor signatures of $5^6 dot 13^3 dot 17^2 dot 29 dot 37 dot 41 dot 53 dot 61$ -- instant in exact integers. The formula is checked against a geometric brute force for eight small radii (including $d = 65$ versus $d = 125$, which share $n = 16$ but differ in $f$, so the signature truly matters) and against every value given in the problem, including $S(325) = 2370$ and $S(1105) = 5535$.

#pagebreak()
#link("https://projecteuler.net/problem=724")[= Problem 724: Drone Delivery]

Solution: 18128250110

Every second the depot gives a uniformly random one of $n$ drones a $+1$ cm/s speed boost; the flight ends one second after the last drone receives its first instruction. $E(n)$ is the expected landing distance per package; we need $E(10^8)$ rounded to the nearest integer.

== Reduction to the coupon collector

Let $T$ be the time of the last first-instruction — exactly the coupon collector time for $n$ coupons. An instruction issued at time $t$ raises one drone's speed by $1$ for the remaining $T + 1 - t$ seconds, so the *total* distance of all packages telescopes to $sum_(t=1)^(T) (T + 1 - t) = T(T+1)\/2$, independent of which drones were chosen. Hence $E(n) = bb(E)[T^2 + T] \/ (2n)$.

$T$ is a sum of independent geometrics with success probabilities $(n-i)\/n$, giving $bb(E)[T] = n H_n$ and $"Var" thin T = n^2 H_n^((2)) - n H_n$. Substituting, everything collapses to
$
E(n) = n / 2 (H_n^2 + H_n^((2))).
$
This reproduces $E(2) = 7\/2$ and $E(5) = 12019\/720$ exactly, and was also confirmed by an exact Markov-chain computation for $n = 4$ plus simulation of the literal process.

== Evaluation

Kahan-compensated summation (small terms first) of $H_n$ and $H_n^((2))$ for $n = 10^8$ keeps the absolute error far below the rounding threshold; a $40$-digit evaluation via $H_n$ and $zeta(2) - zeta(2, n+1)$ gives $18128250110.4186 dots$, agreeing with the float computation and rounding to the answer.

#pagebreak()
#link("https://projecteuler.net/problem=725")[= Problem 725: Digit Sum Numbers]

Solution: 4598797036650685

A DS-number has one digit equal to the sum of all its other digits, like $352$ or $32812$. We need $S(2020)$, the sum of all DS-numbers with at most $2020$ digits, modulo $10^16$.

== Characterisation

If digit $d$ equals the sum of the others, the total digit sum is $2d$, and $d$ is necessarily the largest digit. Conversely, if the digit sum is $2d$ and the digit $d$ occurs, the other digits sum to $d$. So a number is a DS-number exactly when its digit sum is $2d$ for some digit $d$ it contains. In particular the digit sum is at most $18$, which keeps everything small despite the $2020$-digit length.

== Summing by symmetry

Pad every number to exactly $L = 2020$ digits with leading zeros; this is a bijection that changes no values. For a fixed $d$, the condition "digit sum $= 2d$ and contains $d$" is symmetric under permuting positions, so the count of qualifying strings with value $v$ at a given position is the same for every position. The value-sum over qualifying strings is therefore
$
R dot sum_(v=0)^(9) v dot N(v), quad R = underbrace(11 dots 1, L "ones"),
$
where $N(v)$ counts strings on the other $L - 1$ positions completing the condition. By inclusion–exclusion, $N(v) = M(2d - v) - [v != d] dot M_d (2d - v)$, where $M(s)$ counts length-$(L-1)$ digit strings with sum $s$, and $M_d$ the same with the digit $d$ forbidden.

Both counts are coefficients of $(1 + x + dots + x^9)^(L-1)$ and of the same product with the $x^d$ term removed, truncated at degree $18$; binary exponentiation of $19$-term polynomials modulo $10^16$ (only additions and multiplications, so the non-prime modulus is harmless) computes them instantly. The repunit $R$ is reduced directly. As a check, $S(3) = 63270$ and $S(7) = 85499991450$.

#pagebreak()
#link("https://projecteuler.net/problem=726")[= Problem 726: Falling Bottles]

Solution: 578040951

Taking a bottle opens a hole that climbs through the stack: it must accept a drop while any bottle touches it from above, with a free choice when two do, and it stops when nothing is above. $f(n)$ counts complete emptying sequences of the $n$-layer triangle, distinguishing both the bottle taken and the collapse; we need $sum_(k <= 10^4) f(k)$ modulo $1 space 000 space 000 space 033$.

== A configuration-independent multiplier

By induction every empty cell keeps both of its upper neighbours empty, so the present bottles always form a _down-closed_ set: each present cell has both lower neighbours present. Run a collapse backwards: the (taken bottle, collapse path) pairs whose hole ends at a cell $e$ in row $r$ are precisely the downward walks starting at $e$ -- and since the present set is down-closed, every such walk is available, giving $1 + 2 + dots + 2^(n - r) = 2^(n-r+1) - 1$ pairs no matter what the configuration looks like. The configuration only loses the cell $e$, which can be any present cell whose upper neighbours are already gone. The choice multipliers therefore factor out of the entire process:
$ f(n) = L(n) dot product_(k=1)^n (2^k - 1)^(n-k+1), $
with $L(n)$ the number of admissible emptying orders.

== Counting the orders

A cell may be emptied once the two cells resting on it are gone, so the orders are the linear extensions of the triangular poset -- after the shear $(r, c) -> (c, r + 1 - c)$, exactly the standard Young tableaux of staircase shape $(n, n-1, dots, 1)$. The staircase hook of cell $(i, j)$ is $2(n + 1 - i - j) + 1$, all odd, so the hook length formula collapses to $L(n) = N! \/ product_(m=0)^(n-1) (2m+1)^(n-m)$ with $N = n(n+1)\/2$; for $n = 3$ this gives $L = 720\/45 = 16$ and $f(3) = 63 dot 16 = 1008$, matching the given value (the formula is also checked against a full state-space simulation up to $n = 4$).

== Summation

Both products advance by one factor per layer -- the hook product by $(2n-1)!!$ and the weight product by $product_(k <= n)(2^k - 1)$ -- so $S(10^4)$ accumulates with $O(N)$ modular multiplications (the hooks, all below $2 dot 10^4$, are invertible modulo the prime $10^9 + 33$).

#pagebreak()
#link("https://projecteuler.net/problem=727")[= Problem 727: Triangle of Circular Arcs]

Solution: 3.64039141

Three mutually externally tangent circles with radii $r_a < r_b < r_c$ form an arc triangle; $d$ is the distance between the centre $D$ of the circle through the three tangency points and the centre $E$ of the circle externally tangent to all three. We average $d$ over coprime integer triples with $r_c <= 100$.

== Two classical centres

The tangency points of three mutually tangent circles lie on the *incircle of the triangle of their centres* (each tangency point sits on a side at the standard incircle contact distances $s - a$, since the side decomposes as $r_a + r_b$), so $D$ is simply the incentre of the centre triangle, computed barycentrically with weights equal to the opposite side lengths $r_b + r_c$, $r_a + r_c$, $r_a + r_b$.

The green circle is the *inner Soddy circle*. Its curvature comes from the Descartes circle theorem $k_4 = k_1 + k_2 + k_3 + 2 sqrt(k_1 k_2 + k_2 k_3 + k_3 k_1)$, and its centre from the complex Descartes theorem $z_4 k_4 = z_1 k_1 + z_2 k_2 + z_3 k_3 plus.minus 2 sqrt(k_1 k_2 z_1 z_2 + k_2 k_3 z_2 z_3 + k_3 k_1 z_3 z_1)$; placing circle $a$ at the origin kills all but the $z_2 z_3$ cross term inside the root, and the sign ambiguity is resolved by checking external tangency $|z_4 - z_1| = 1\/k_4 + r_a$.

With both centres in closed form, the $approx 1.6 dot 10^5$ coprime triples are averaged directly in double precision, comfortably within the eight required decimals.

#pagebreak()
#link("https://projecteuler.net/problem=728")[= Problem 728: Circle of Coins]

Solution: 709874991

A move flips $k$ consecutive coins of $n$ in a circle; $F(n, k)$ counts the head/tail states from which all-heads is reachable, and $S(N) = sum_(n <= N) sum_(k <= n) F(n, k)$ is wanted for $N = 10^7$ modulo $10^9 + 7$.

== A closed form for $F$

Moves commute and are involutions, so the reachable corrections form the $"GF"(2)$-span of the $n$ cyclic windows, and $F(n, k) = 2^"rank"$. Identifying states with polynomials in $"GF"(2)[x] \/ (x^n + 1)$, the windows generate the ideal of $m(x) = 1 + x + dots + x^(k-1)$, so the rank is $n - deg gcd(m(x), x^n + 1)$. Since $(x + 1) m(x) = x^k + 1$ and $gcd(x^k + 1, x^n + 1) = x^(gcd(n, k)) + 1$, the only subtlety is the multiplicity of the factor $x + 1$, which is $2^(v_2(k)) - 1$ in $m$ and $2^(v_2(n))$ in $x^n + 1$ (where $v_2$ is the $2$-adic valuation). Comparing the two minima yields
$
F(n, k) = 2^(n - gcd(n, k) + [v_2(k) <= v_2(n)]),
$
verified against brute-force ranks for all $n <= 12$ and matching $F(3,2) = 4$, $F(8,3) = 256$, $F(9,3) = 128$.

== Summation

Group $k$ by $g = gcd(n, k)$: with $n = g m$ and $k = g j$, $gcd(j, m) = 1$, the indicator fails only when $v_2(j) > v_2(m)$, i.e. $m$ odd and $j$ even — exactly half of the $phi(m)$ units when $m > 1$ (the units $j$ and $m - j$ have opposite parity). Therefore
$
S(N) = sum_(g >= 1) sum_(m <= N \/ g) w(m) dot 2^(g(m - 1)), quad w(m) = cases(2 & m = 1, 2 phi(m) & m "even", 3 phi(m) \/ 2 & m "odd," > 1).
$
With a totient sieve to $10^7$ and, for each $g$, the inner powers advanced by repeated multiplication with $2^g$, the double loop costs $O(N log N)$ modular operations. The givens $S(3) = 22$, $S(10) = 10444$ and $S(10^3) equiv 853837042$ all check out.

#pagebreak()
#link("https://projecteuler.net/problem=729")[= Problem 729: Range of Periodic Sequences]

Solution: 308896374.2502

The recurrence $a_(n+1) = a_n - 1\/a_n$ is Boole's transformation. We sum the ranges (maximum minus minimum) of all periodic sequences with minimal period at most $25$.

== Sign itineraries

Every real $b$ has exactly two preimages $(b plus.minus sqrt(b^2 + 4))\/2$, whose product is $-1$: one positive and one negative. A periodic orbit is therefore determined by its *sign itinerary*, and orbits of exact period $d$ correspond bijectively to primitive binary necklaces of length $d$: the composition of the $d$ inverse branches along any sign word is a strict contraction (each branch derivative lies in $(0, 1)$), so it has a unique fixed point; the two constant words drift to $plus.minus infinity$, matching the absence of finite fixed points. The correspondence reproduces $S(2) = 2 sqrt(2)$ from the single necklace $+-$, whose orbit is $plus.minus sqrt(1\/2)$.

== Computation

For each of the $approx 2.7 dot 10^6$ Lyndon words of length $2 <= d <= 25$, the rotation-$0$ orbit point is found by thirty plain contraction sweeps followed by Newton iteration on $Phi(x) - x$ (with $Phi'$ available as the product of branch derivatives); the remaining $d - 1$ orbit points warm-start from $T$ of the previous point and need only a couple of Newton steps each, since orbit values are bounded in $[1\/8, 7]$ in absolute value (a $+$-run of length $k$ climbs like $sqrt(2k)$, and $|T(a)| <= 8$ keeps points away from $0$, controlling the warm-start error through $T' = 1 + 1\/a^2$). Each of the $d$ points of an orbit is its own sequence, so an orbit adds $d (max - min)$; Kahan summation keeps the $approx 6.7 dot 10^7$-term total accurate to the four required decimals. The whole run takes $47$ seconds and matches $S(3) approx 14.6461$ and $S(5) approx 124.1056$.

#pagebreak()
#link("https://projecteuler.net/problem=730")[= Problem 730: Shifted Pythagorean Triples]

Solution: 1315965924

We count primitive triples $p^2 + q^2 + k = r^2$ with $1 <= p <= q <= r$ and $p + q + r <= n$, summed over shifts $k <= 100$, at $n = 10^8$ -- about $1.3 dot 10^9$ triples, so they must be counted in blocks rather than visited.

== Progressions of solutions

Set $d = r - q >= 1$ and $e = r + q$. A $k$-shifted triple is exactly $d e = p^2 + k$ with $d equiv e (mod 2)$, $q = (e - d)\/2 >= p$ and perimeter $p + e <= n$. For fixed $d$ the divisor condition pins $p$ to the roots of $p^2 equiv -k (mod d)$ -- sharpened to $2d | p^2 + k$ for even $d$ (constant on each residue class since $d^2 equiv 0 mod 2d$) and to $p^2 + k$ odd for odd $d$. The perimeter gives $p^2 + d p <= n d - k$, and $q >= p$ is the parabola $p^2 - 2 d p + k - d^2 >= 0$, satisfied on $[1, d - t] union [d + t, infinity)$ with $t = ceil(sqrt(2d^2 - k))$ (the left branch matters only for tiny $d$, e.g. the triple $(1,1,3)$ for $k = 7$). So each pair ($d$, root) contributes an $O(1)$ count of an arithmetic progression in an interval.

== Enumerating the roots by topographs

The pair $(d, rho)$ corresponds to the binary quadratic form $[d, 2 rho, (rho^2 + k)\/d]$ of discriminant $-4k$: pairs of content $g$ (where $g^2 | 4k$) are precisely the primitive representations of $d\/g$ by the form classes of discriminant $-4k\/g^2$, taken modulo automorphisms. Each class is traversed with Conway's topograph. The reduced form $[a, b, c]$ gives the well, the superbase with values $(a, c, a - |b| + c)$ -- mirror-orientated when $b < 0$, which is what keeps a class and its inverse producing $rho$ and $-rho$ rather than duplicates. Crossing an edge between regions $A$ and $B$ away from the node with third value $C$ discovers exactly one new region $C_2 = 2(A + B) - C$, whose root is $(A - B - C_2)\/2 mod C_2$ by the orientation rule, and values only grow away from the well, so every branch is cut once $C_2$ exceeds $n\/8 + 2$ (the perimeter of any triple is at least $(4 + 3 sqrt(2)) d$). Discriminants $-3$ and $-4$ carry extra units, so their region sums are divided by $3$ and $2$. The enumeration reproduces the exact multiset of congruence roots for many $k$ and bounds, and runs in $O(1)$ per pair -- about twelve times faster than completing each representation with an extended Euclid.

== Primitivity and assembly

A triple with $gcd = h$ forces $h^2 | k$ and scales to a primitive $(k\/h^2)$-shifted triple of perimeter $<= n\/h$, so $P_k (n) = sum_(h^2 | k) mu(h) T_(k\/h^2)(n\/h)$ where $T$ counts all triples; $k = 0$ is the classical Euclid count of primitive Pythagorean triples by coprime opposite-parity generators. The full pipeline is validated against brute force for every $k$ at $n = 10^4$ (including the given $P_0 = 703$, $P_20 = 1979$, $S(10, 10^4) = 10956$) and at $n = 10^5$, and the final sum takes about $35$ seconds.

#pagebreak()
#link("https://projecteuler.net/problem=731")[= Problem 731: A Stoneham Number]

Solution: 6086371427

$A = sum_(i >= 1) 1 \/ (3^i 10^(3^i))$, and $A(n)$ is the run of ten decimal digits starting at the $n$th place; we need $A(10^16)$.

The ten digits are $floor("frac"(10^(n-1) A) dot 10^10)$. Shifting term $i$ by $10^(n-1)$ gives $10^(n - 1 - 3^i) \/ 3^i$. Terms with $3^i > n - 1$ are at most $10^(-(3^i - n + 1))$, and since the powers of three land nowhere near $10^16$ (the first exceeding it overshoots by more than $6 dot 10^15$), they are far too small to disturb the digits. For $3^i <= n - 1$ the integer part of the term is irrelevant and the fractional contribution is $(10^(n - 1 - 3^i) mod 3^i) \/ 3^i$, a modular exponentiation.

Summing the $33$ contributing terms over the common denominator $3^33$, reducing the numerator modulo $3^33$, and reading off $floor(N dot 10^10 \/ 3^33)$ (zero-padded to ten digits) gives the answer instantly — all with exact integer arithmetic, so no precision questions arise. The given $A(100)$ and $A(10^8)$ check out.

#pagebreak()
#link("https://projecteuler.net/problem=732")[= Problem 732: Standing on the Shoulders of Trolls]

Solution: 45609

$N = 1000$ trolls with shoulder heights $h_n$, arm lengths $l_n$ and IQs $q_n$ (all in $[50, 150]$, generated from powers of $5$) sit in a hole of depth $D = H \/ sqrt(2)$, where $H = sum h_n$. Escapees climb a pile of everyone still present, so a troll leaving when escaped trolls of total height $c$ have already gone reaches $H - c + l$, and may escape iff $c <= B + l$ with $B = H - H\/sqrt(2)$.

== Scheduling formulation

Each escapee "consumes" $h_t$ of the height budget and must *start* (i.e. have $c$) at most $B + l_t$ — single-machine job scheduling with processing times $h_t$ and completion deadlines $d_t = B + l_t + h_t$, maximising the total weight $q_t$ of on-time jobs. Any feasible escape set can be reordered by increasing deadline (the usual adjacent-exchange argument on $d_t$ — note the deadline involves $l_t + h_t$, not $l_t$ alone, a distinction that actually changes the answer at $N = 1000$). So sort by $l + h$ and run a knapsack over the cumulative escaped height $c$: for each troll, $"dp"[c + h_t] = max("dp"[c + h_t], "dp"[c] + q_t)$ for all reachable $c <= B + l_t$. The DP was validated against exhaustive search over all escape orders on $300$ random instances.

The irrational threshold is handled exactly: $floor(B + l) = H + l - floor(sqrt(H^2\/2)) - 1$ since $H\/sqrt(2)$ is irrational, and $floor(sqrt(H^2\/2)) = "isqrt"(floor(H^2\/2))$ because $2k^2 = H^2$ has no solutions. With $c$ ranging to about $44000$, the table costs $10^3 times 4 dot 10^4$ cell updates. The givens $Q(5) = 401$ and $Q(15) = 941$ agree.

#pagebreak()
#link("https://projecteuler.net/problem=733")[= Problem 733: Ascending Subsequences]

Solution: 574368578

With $a_i = 153^i mod 10000019$, $S(n)$ sums, over every ascending $4$-term subsequence of $a_1, dots, a_n$, the sum of its four terms. We need $S(10^6)$ modulo $10^9 + 7$.

Sweep the sequence left to right. For each length $L = 1, dots, 4$ maintain two Fenwick trees indexed by (rank-compressed) value: one storing the number of ascending $L$-subsequences ending at each value, the other the total of their term-sums. When $a_i$ arrives, the $L$-subsequences ending at $a_i$ extend the $(L-1)$-subsequences whose last value is smaller, so prefix queries below $a_i$ give
$
c_L = c_(L-1)^(<), quad s_L = s_(L-1)^(<) + a_i dot c_(L-1)^(<),
$
with base case $c_1 = 1$, $s_1 = a_i$. Add $s_4$ to the answer, insert the new counts and sums at $a_i$'s rank for levels $1$–$3$, and continue. Everything is kept modulo $10^9 + 7$ (the raw counts alone are astronomically large). The whole run is $O(n log n)$. Checks: $S(6) = 94513710$, and $S(100) = 4465488724217$ reduces to the computed residue.

#pagebreak()
#link("https://projecteuler.net/problem=734")[= Problem 734: A Bit of Prime]

Solution: 557988060

$T(n, k)$ counts $k$-tuples of primes $<= n$ whose bitwise OR is also a prime $<= n$; we need $T(10^6, 999983)$ mod $10^9 + 7$.

== Zeta and Möbius on the subset lattice

A tuple has OR equal to $q$ exactly when every element is a submask of $q$ and the OR is not a proper submask. Let $F(m)$ count primes $<= n$ that are submasks of $m$: a subset-sum (SOS) zeta transform over the $2^20$-element bitmask lattice computes all $F$ in $O(2^20 dot 20)$. Then $F(m)^k$ counts tuples whose OR is *contained in* $m$, and the inverse SOS (Möbius) transform of $m arrow.r.bar F(m)^k mod p$ recovers the exact-OR counts, of which we sum those at prime masks. The $2^20$ modular exponentiations and two transforms run in about a second, and the method reproduces $T(5, 2) = 5$, $T(100, 3) = 3355$ and $T(1000, 10) equiv 2071632$.

#pagebreak()
#link("https://projecteuler.net/problem=735")[= Problem 735: Divisors of $2n^2$]

Solution: 174848216767932

$f(n)$ counts divisors of $2n^2$ that are at most $n$; we need $F(10^12) = sum_(n<=N) f(n)$.

== Structure of the divisors

Count pairs $(d, n)$ with $d <= n <= N$ and $d | 2n^2$. Writing $g = gcd(d, n)$, $d = g e$, $n = g m$ with $gcd(e, m) = 1$, the divisibility collapses: $g e | 2 g^2 m^2 arrow.l.r.double e | 2g$ (the $m^2$ is coprime to $e$), and $d <= n$ becomes $e <= m$. For a fixed coprime pair the admissible $g$ form an arithmetic progression: $floor(N\/(e m))$ choices when $e$ is odd, and $floor(N\/(u m))$ when $e = 2u$ (which forces $m$ odd and $2u <= m$). Hence
$ F(N) = sum_(e "odd", e <= m, gcd = 1) floor(N/(e m)) + sum_(m "odd", 2u <= m, gcd(2u, m) = 1) floor(N/(u m)). $

== Evaluation

Möbius inversion removes the coprimality (only odd $k$ survive, since the parity conditions force $k$ odd), reducing $F$ to $sum_(k "odd") mu(k) (A_0 + B_0)(N\/k^2)$ where $A_0, B_0$ are the unrestricted wedge-hyperbola sums. Each is evaluated in $O(M^(3\/4))$ by iterating the smaller variable to $sqrt(M)$ and summing the inner $floor$ by quotient blocks (with an odd-only count of integers per block for $B_0$), about $1.7 dot 10^9$ operations in total — fifteen seconds in numba. Verified against $F(15) = 63$, $F(1000) = 15066$ and brute force at $10^4$ and $3 dot 10^4$.

#pagebreak()
#link("https://projecteuler.net/problem=736")[= Problem 736: Paths to Equality]

Solution: 25332747903959376

With moves $r(x, y) = (x + 1, 2y)$ and $s(x, y) = (2x, y + 1)$ on lattice points, a path to equality from $(45, 90)$ reaches $a_n = b_n$ without any earlier tie. The shortest path has length $10$ (final value $1476$); we need the final value of the unique path of smallest *odd* length.

== Structure and pruning

After a remaining word with $r'$ moves of type $r$ and $s'$ of type $s$, the first coordinate becomes $a dot 2^(s') + A$ where $A = sum_t g_t 2^t$ counts $r$-moves by how many $s$-moves follow them; so $A$ ranges exactly over $[r', r' dot 2^(s')]$, and symmetrically for $B$. Equality is reachable only if the intervals $a 2^(s') + [r', r' 2^(s')]$ and $b 2^(r') + [s', s' 2^(r')]$ overlap for some split $r' + s' = m$ — a complete feasibility test for a depth-first search over moves (intermediate ties simply terminate a branch, since such a prefix is itself a shorter path).

The prune is devastating for this instance: since $b = 2a$, the leading terms are $45 dot 2^(s')$ vs $45 dot 2^(r' + 1)$, and an *even* move count (odd path length) forces $s' != r' + 1$, i.e. a factor-$2$ gap that the additive ranges (at most $(M\/2) 2^(M\/2)$) cannot bridge until $M\/2 >= 45$. Every even $M < 92$ is refuted instantly at the root; the $M = 92$ and $94$ searches die after a couple hundred nodes; and $M = 96$ finds the unique solution after only $463$ nodes — a sequence of $96$ moves with $48$ of each type, length $n = 97$ and final value $25332747903959376 = 45 dot 2^48 + (45 dot 2^48 + 336)$. The iterative deepening also re-derives the length-$10$ example exactly.

#pagebreak()
#link("https://projecteuler.net/problem=737")[= Problem 737: Coin Loops]

Solution: 757794899

Coins of radius $1$ are stacked, each touching a fixed vertical line, with the stack balanced after every placement; we need the number of coins for the projected centres to wind $2020$ times around the line.

== The tight construction

Since each coin touches the line, all projected centres lie on the unit circle. The extremal stack places every new coin at distance exactly $1$ from the centroid $M$ of all coins already placed: with $cos beta = |M|\/2$ the new centre is the unit vector $hat(M)$ rotated by $-beta$, taking the advancing branch. A naive per-step greedy (maximise each rotation $theta$ subject to centre-of-mass constraints) deadlocks immediately — a first step of $60 degree$ makes the base constraint tight forever — while this tight construction reproduces all three given values $31$, $154$ and $6947$ exactly, pinning down the intended balance model.

== Numerics

The placement needs no trigonometry (a pure vector rotation by $beta$); a single `arctan2` per step measures the angular advance. The crossing happens near $7.6 dot 10^8$ coins, where each step advances only $approx 1.7 dot 10^(-5)$ radians, so both the centroid sum and the cumulative angle are Kahan-compensated to keep accumulated rounding far below one step. The run takes about thirty seconds.

#pagebreak()
#link("https://projecteuler.net/problem=738")[= Problem 738: Counting Ordered Factorisations]

Solution: 143091030

$d(n, k)$ counts factorisations $n = x_1 times dots times x_k$ with $1 <= x_1 <= dots <= x_k$, and $D(N, K) = sum d(n, k)$ over $n <= N$, $k <= K$; we need $D(10^10, 10^10)$ mod $10^9 + 7$.

== Reduction to multisets

Dropping the padding $1$s, a factorisation is just a multiset of factors $>= 2$ of size $j <= k$, so a multiset of size $j$ is counted in $d(n, k)$ for every $k >= max(j, 1)$, i.e. with weight $K - j + 1$ (weight $K$ for the empty multiset of $n = 1$). Writing $c$ for the number of multisets of integers $>= 2$ with product $<= N$ (empty included) and $s$ for the sum of their sizes,
$ D(N, K) = K + (K + 1)(c - 1) - s, $
valid because $K = 10^10$ exceeds the maximal multiset size $log_2 N approx 33$.

== Smallest-factor recursion

Conditioning on the smallest element $f$ of a multiset gives $c(B, m) = 1 + sum_(f >= m) c(floor(B\/f), f)$, with the matching size recursion. Every $f > sqrt(B)$ admits only the bare singleton ${f}$, contributing $(1, 1)$, so the whole tail collapses to a closed form and the recursion only branches on $f <= sqrt(B)$. The recursion tree for $B = 10^10$ has on the order of $10^9$ cheap nodes — about twenty seconds in numba, with the recursive function compiled uncached to avoid the recursion-plus-cache segfault. Verified against $D(10, 10) = 153$ and $D(100, 100) = 35384$.

#pagebreak()
#link("https://projecteuler.net/problem=739")[= Problem 739: Summation of Summations]

Solution: 711399016

Starting from a sequence of length $n$, repeatedly discard the first term and replace the rest by its partial sums; $f(n)$ is the single number remaining. With the Lucas start $1, 3, 4, 7, 11, dots$ we need $f(10^8)$ modulo $10^9 + 7$.

The whole pipeline is linear, so $f(n) = sum_i a_i w_i (n)$, and feeding in unit vectors identifies the weights as ballot numbers:
$
w_1 = 0, quad w_i = (i - 1)/(2n - 1 - i) binom(2n - 1 - i, n - 1) "  for " i >= 2,
$
verified directly for $n <= 20$ — for the all-ones start they sum to the Catalan number $C_(n-1)$, matching $f(8) = 429$, and the Lucas checks $f(8) = 2663$ and $f(20) equiv 742296999$ both hold.

For $n = 10^8$, iterate $i$ downward from $w_n = 1$ using the ratio
$
w_i = w_(i+1) dot ((i-1)(2n - 2 - i)) / (i (n - i)),
$
whose denominators never exceed $n$, so a single table of modular inverses of $1, dots, n$ (built by the linear recurrence) covers every step. The Lucas values run backwards alongside via $a_(i-1) = a_(i+1) - a_i$ after one forward pass to fetch $a_(n-1), a_n$. Two linear passes under Numba finish in seconds.

#pagebreak()
#link("https://projecteuler.net/problem=740")[= Problem 740: Secret Santa]

Solution: 0.0189581208

Each of $n$ people puts two name slips in a hat; in turn, each draws two uniformly random slips avoiding their own name. The process fails if the last person is left facing one of their own slips; $q(n)$ is the failure probability and we need $q(100)$ to ten decimal places.

The people who have not yet drawn are exchangeable, so it suffices to track the distribution of $(k_2, k_1)$ — how many of them still have two (resp. one) of their own slips in the hat ($k_0$ and the free-slip count follow, since the hat holds exactly $2m$ slips when $m$ people remain). The next drawer has $2$, $1$ or $0$ own slips with probabilities $k_2\/m$, $k_1\/m$, $k_0\/m$; each of their two draws is uniform over the hat minus their own $c$ slips and hits either a free slip, a slip of a person with two left (who drops to one), or a slip of a person with one left. After the turn the drawer's unclaimed own slips become free for everyone later.

Propagating this exact distribution over the $n - 1$ turns touches only a few thousand states ($k_1 + k_2 <= m <= 100$) and the failure probability is the mass with $k_1 + k_2 > 0$ when one person remains. Floating point is comfortably sufficient for ten decimals. The givens $q(3) = 0.3611111111$ and $q(5) = 0.2476095994$ match (a direct Monte-Carlo simulation of the drawing procedure agrees as well).

#pagebreak()
#link("https://projecteuler.net/problem=741")[= Problem 741: Binary Grid Colouring]

Solution: 512895223

$f(n)$ counts $n times n$ grids with exactly two black cells in each row and column, and $g(n)$ counts them up to the symmetries of the square; we need $g(7^7) + g(8^8)$ mod $10^9 + 7$.

== Burnside over the dihedral group

$g = (op("Fix")(op("id")) + 2 op("Fix")(r_90) + op("Fix")(r_180) + 2 op("Fix")("flip") + 2 op("Fix")("transpose"))\/8$, and every fixed-point count turns out to be holonomic with an $O(n)$ recurrence extracted from an exponential generating function:

- *Identity.* Two-per-line matrices are unions of even row–column cycles: EGF $e^(-x\/2)\/sqrt(1-x)$ in $x^n\/(n!)^2$, giving $f(n+1) = n(n+1) f(n) + n^2 (n+1) f(n-1)\/2$.
- *Transpose.* Symmetric matrices correspond to graphs whose components are cycles ($>= 3$) or paths with a diagonal loop at each end: $T(n) = n! thin c_n$ with $(n+1) c_(n+1) = 2n c_n - (n-2) c_(n-1) - c_(n-3)\/2$.
- *Half turn.* Quotienting by $r_180$ yields a multigraph on $n\/2$ index classes whose single edges carry two flavours: even $n$ gives $((n\/2)!)^2 [x^(n\/2)] e^(-x) (1-4x)^(-1\/2)$; for odd $n$ the middle row and column attach a marked flavoured path, giving $m^2 ((m-1)!)^2 [x^(m-1)] 2 e^(-x)(1-4x)^(-3\/2)$ with $m = (n-1)\/2$.
- *Quarter turn.* Cell orbits act on index classes as saturating loops or $2$-flavoured edges: even $n$ gives $m! [x^m] (1-2x)^(-1\/2) e^(-x^2\/2)$; odd $n$ is $0$ by a degree-parity obstruction.
- *Axis flips.* Each row must use a mirrored column pair and each pair exactly two rows: $n!\/2^(n\/2)$ for even $n$, $0$ for odd.

Every count was checked against exhaustive enumeration for $n <= 6$, and the assembled $g$ reproduces $g(4) = 20$, $g(7) = 390816$ and $g(8) = 23462347$ (the latter two also verified by hand from the recurrences). Both targets need only linear recurrences mod $p$ with a table of inverses — a couple of seconds for $n = 8^8 approx 1.7 dot 10^7$.

#pagebreak()
#link("https://projecteuler.net/problem=742")[= Problem 742: Minimum Area of a Symmetrical Convex Grid Polygon]

Solution: 18397727

$A(N)$ is the minimum area of a convex lattice polygon with $N$ vertices having both horizontal and vertical mirror symmetry; we need $A(1000)$.

== Structure and area formula

The polygon is determined by its first-quadrant chain of edge vectors $(-a_i, b_i)$ with $a_i, b_i >= 1$: convexity forces every edge direction to appear exactly once, and primitive vectors dominate longer ones of the same slope. For $4 | N$ exactly two configurations exist: vertices on both symmetry axes (lattice centre, $t = N\/4$ chain vectors) or unit edges crossing both axes (centre at half-integer coordinates, $t = N\/4 - 1$); the mixed case has $N equiv 2 space (mod 4)$. Expanding the identity $2 dot "Area" = sum_(i<j) "cross"(e_i, e_j)$ over the full symmetric edge cycle gives
$ "Area"_(V V) = 2 sum a_i b_i + 4 sum_(i<j) max(a_i b_j, a_j b_i), quad "Area"_(E E) = "Area"_(V V) + 2 sum (a_i + b_i) + 1, $
both verified against direct shoelace evaluation of the constructed polygons on hundreds of random vector sets (these checks caught two mirror-vertex bugs in the builder). The hand-checkable cases $A(4) = 1$ (unit square, EE with $t = 0$) and $A(8) = 7$ confirm the constants.

== Exact optimisation

Choosing the $t$ vectors is now a pure combinatorial minimisation. Greedy construction, $1$- and $2$-swap local search and simulated annealing all agree with exhaustive subset enumeration up to $t = 13$ and reproduce $A(40) = 1039$ and $A(100) = 17473$ — yet at $N = 1000$ they all plateau at $18409935$, a startling $12208$ above the optimum. The key observation: sorting candidates by slope (steepest first), the pairwise term between a steeper $i$ and flatter $j$ is $a_j b_i$, so a newly chosen vector interacts with all previously chosen ones only through $4 a B$, where $B$ is the prefix sum of chosen $b$'s. A dynamic programme over (count, $B$) is therefore *exact*: over the pool of primitive vectors with $a, b <= 40$ and $B <= 3000$ it runs in a second and yields $18397727$, stable under enlarging the pool and cap.

#pagebreak()
#link("https://projecteuler.net/problem=743")[= Problem 743: Window into a Matrix]

Solution: 259158998

$A(k, n)$ counts $2 times n$ binary matrices in which every $2 times k$ window sums to $k$; we need $A(10^8, 10^16)$ modulo $10^9 + 7$.

== Structure

Sliding a window one column right exchanges one column for another with the same total, so the column sums $c_i in {0, 1, 2}$ satisfy $c_(i+k) = c_i$: they are periodic with period $k$, and one period's sums total $k$. Here $k | n$, so each residue class contains exactly $n\/k$ columns. A class with sum $0$ or $2$ fixes both entries of all its columns; a class with sum $1$ leaves a free row choice in each of its $n\/k$ columns, contributing a factor $g = 2^(n\/k)$ per class. If $j$ classes have sum $1$ (necessarily $j equiv k space (mod 2)$), the remaining $k - j$ split evenly into $m = (k-j)\/2$ zeros and $m$ twos, giving
$
A(k, n) = sum_(j equiv k (mod 2)) k! / (j! thin m! thin m!) dot g^j .
$
The check values $A(3, 9) = 560$ and $A(4, 20) = 1060870$ confirm this.

== Evaluation at $k = 10^8$

Rather than storing factorials up to $10^8$, walk $j$ downward from $k$ (where the term is $g^k$). Stepping $j -> j - 2$ multiplies the term by $j(j-1)$ and divides by $(m+1)^2 g^2$, so with a table of modular inverses of $1, dots, k\/2 + 1$ (built by the standard $"inv"[i] = -(floor(p\/i)) dot "inv"[p mod i]$ recurrence) each step is a few multiplications. The $5 dot 10^7$ steps run in about a second under Numba.

#pagebreak()
#link("https://projecteuler.net/problem=744")[= Problem 744: What? Where? When?]

Solution: 0.0001999600

Among $2n + 1$ envelopes, $2n$ hold questions (answered correctly with probability $p$, independently) and one holds the red card; envelopes are drawn in random order and the game ends normally when either side reaches $n$ points first. We need $f(10^11, 0.4999)$ to ten decimals.

== Reduction

The red card occupies a uniform slot among the $2n + 1$. The game ends normally iff that slot comes after the deciding question $S$, the number of questions needed for $n$ successes or $n$ failures, so
$
f(n, p) = bb(E)[(2n + 1 - S)/(2n + 1)] = (1 + bb(E)[R])/(2n + 1), quad R = 2n - S,
$
where $R$ is $n$ minus the loser's final score. The loser's score follows a two-branch negative binomial: $P(L = ell) = binom(n - 1 + ell, ell)(p^n q^ell + q^n p^ell)$. Exact rational evaluation reproduces both small givens.

== Large $n$

At $n = 10^11$, $p = 0.4999$: the expert side wins with probability at most $exp(-4n(q - p)^2) = exp(-4000)$ (Hoeffding), so only the viewers' branch matters and its conditional distribution is its own normalisation. With $r = n - ell$, the weights obey
$
u(r + 1)/u(r) = (n - r)/((2n - 1 - r) p),
$
so start at the peak $r_0 = (n(1 - 2p) + p)\/(1 - p) approx 4 dot 10^7$ and sweep outward until the terms fall below $10^(-18)$ of the peak ($approx 3 dot 10^7$ terms), accumulating $sum u$ and $sum r u$; then $bb(E)[R] = sum r u \/ sum u$ — no absolute normalisation needed. The method agrees with exact summation to machine precision in strongly biased mid-size cases and reproduces the given $f(10^4, 0.3) = 0.2857499982$; the literal game was also simulated as a sanity check.

#pagebreak()
#link("https://projecteuler.net/problem=745")[= Problem 745: Sum of Squares II]

Solution: 94586478

Let $g(n)$ be the largest perfect square dividing $n$; we need $S(N) = sum_(n <= N) g(n)$ for $N = 10^14$, modulo $10^9 + 7$.

Every $n$ factors uniquely as $n = a^2 b$ with $b$ squarefree, and then $g(n) = a^2$. Grouping by $a$,
$
S(N) = sum_(a^2 <= N) a^2 dot Q(floor(N \/ a^2)),
$
where $Q(x)$ counts squarefree numbers up to $x$. Expanding $Q(x) = sum_(d^2 <= x) mu(d) floor(x \/ d^2)$ and collecting terms by $k = a d$ gives
$
S(N) = sum_(k^2 <= N) J_2 (k) dot floor(N / k^2), quad J_2 (k) = sum_(d | k) mu(d) (k/d)^2,
$
where $J_2$ is the Jordan totient, the multiplicative function with $J_2 (p^e) = p^(2e) - p^(2e-2)$. Sieve $J_2$ up to $sqrt(N) = 10^7$ (start from $k^2$ and for each prime $p | k$ subtract the $1\/p^2$ share), then accumulate the single sum modulo $10^9 + 7$. As a check, $S(10) = 24$ and $S(100) = 767$.

#pagebreak()
#link("https://projecteuler.net/problem=746")[= Problem 746: A Messy Dinner]

Solution: 867150922

$n$ four-person families sit at a circular table with $4n$ labeled seats, men and women alternating; $M(n)$ counts seatings where no family occupies four consecutive seats, and we need $S(2021) = sum_(k=2)^2021 M(k)$ mod $10^9 + 7$.

== Inclusion–exclusion over family blocks

Exhaustive enumeration at $n = 1, 2$ pinned the convention (labeled seats, both gender parities counted). Forcing a chosen set of $j$ families to sit as blocks: $j$ disjoint blocks of $4$ consecutive seats fit on a $4k$-cycle in $(4k)/(4k - 3j) binom(4k - 3j, j)$ ways (the standard cycle block count); the $j$ families are assigned to the blocks in $k!\/(k-j)!$ ways with $2! dot 2! = 4$ internal orders each (father/son in the block's two men seats, mother/daughter in the two women seats); the remaining $2k - 2j$ men and women fill their seat classes independently; and a global factor $2$ picks which parity class holds the men. Hence
$ M(k) = 2 sum_(j=0)^k (-1)^j binom(k, j) j! (4k)/(4k - 3j) binom(4k - 3j, j) thin 4^j ((2k - 2j)!)^2. $
An arithmetic slip in the $j = 2$ term initially produced $913920$ for $M(3)$; the corrected term ($23040$, not $46080$) gives $890880$, matching the given value, and the formula also reproduces $M(10)$ and $S(10)$. Summing $M(k)$ for $k <= 2021$ is a trivial double loop with precomputed factorials.

#pagebreak()
#link("https://projecteuler.net/problem=747")[= Problem 747: Triangular Pizza]

Solution: 681813395

Mamma Triangolo cuts a triangular pizza into $n$ equal-area triangular pieces with $n$ straight cuts from an interior point $P$ to the boundary; $psi(n)$ counts the ways, and we need $Psi(10^8) = sum_(n=3)^(10^8) psi(n)$ mod $10^9 + 7$.

== Classifying the cuttings

Each piece is bounded by two rays from $P$ plus a boundary arc, so it is a triangle in exactly two ways: a *fan piece* with apex $P$ (arc is a single segment), or a *chord piece* where the two rays are collinear (angle $pi$ at $P$) and the arc passes one corner — the corner is sliced off by a chord through $P$, and $P$ is not a vertex of that piece. Two chord pieces would require two disjoint straight angles, so each cutting has at most one.

*No chord:* rays go to all three corners, splitting the pizza into fans of $k_1, k_2, k_3 >= 1$ pieces; $P$ is the unique barycentric point, giving $binom(n-1, 2)$ cuttings. *Chord with an endpoint at a corner* (slicing corner $C$ with a chord from a point of $C A$ through $P$ to corner $B$, say): the position of $P$ on the chord is uniquely determined by the two fan counts and is always interior, giving $6(n - 2)$ cuttings — exactly the six extra cuttings visible in the $psi(3) = 7$ example. *Generic chord:* with $e_1$ at fraction $alpha$ along $C A$, $e_2$ at $1\/(n alpha)$ along $C B$, and fan counts $m_1, m_2, m_3 >= 1$ over $e_1 A$, $A B$, $B e_2$, eliminating all other unknowns leaves
$ n(m_1 + 1) alpha^2 - (m_1 + m_3 + n + 1) alpha + (m_3 + 1) = 0 $
on the validity interval $((m_3+1)\/n, 1\/(m_1+1))$. The quadratic is positive at both endpoints (values $m_1 m_3 (m_3+1)\/n$ and $m_1 m_3\/(m_1+1)$), so valid roots come in pairs, and with $s = m_1 + m_3$, $q = (m_1+1)(m_3+1)$ the vertex-and-discriminant condition collapses to the single inequality $n > n_+ = 2q - s - 1 + 2 sqrt(q m_1 m_3)$, with one tangency root exactly when $n = n_+$ is an integer (i.e. $q m_1 m_3$ a perfect square).

== Summation

Summing over $n <= m$ swaps into a loop over pairs: each $(m_1, m_3)$ contributes $2(m - floor(n_+))$ plus $1$ if $n_+$ is an integer $<= m$. Since $n_+ approx 4 m_1 m_3$, about $m\/4 dot ln m approx 5 dot 10^8$ pairs are scanned with exact integer square roots — three seconds in numba. The formula reproduces $psi(3) = 7$, $psi(6) = 34$, $psi(10) = 90$, $Psi(10) = 345$ and $Psi(1000) = 172166601$.

#pagebreak()
#link("https://projecteuler.net/problem=748")[= Problem 748: Upside Down]

Solution: 276402862

We sum $x + y + z$ over primitive solutions of $1\/x^2 + 1\/y^2 = 13\/z^2$ with $x <= y$ and all variables at most $N = 10^16$, reporting the last nine digits.

== Reduction

Writing $x = g u$, $y = g v$ with $g = gcd(x, y)$ and $gcd(u, v) = 1$, the equation becomes $z^2 (u^2 + v^2) = 13 g^2 u^2 v^2$. Coprimality forces $u v | z$, and writing $z = u v w$ leaves $w^2 (u^2 + v^2) = 13 g^2$ with $gcd(w, g) = 1$, so $w^2 | 13$, i.e. $w = 1$. Hence primitive solutions correspond exactly to
$ u^2 + v^2 = 13 g^2, quad gcd(u, v) = 1, quad x = g u, y = g v, z = u v, $
and primitivity of $(x, y, z)$ is automatic (a prime dividing $g$ and $u$ would divide $v^2$).

== Gaussian parametrization

In $ZZ[i]$, $13 = (3 + 2i)(3 - 2i)$, and $gcd(u, v) = 1$ forces $u + v i = epsilon (3 plus.minus 2i)(s + t i)^2$ with $g = s^2 + t^2$, $gcd(s, t) = 1$. Both $s, t$ odd makes $u, v$ even, so $s + t$ must be odd; the two conjugate families over $s > t >= 0$ then enumerate each unordered primitive pair exactly once (a duplicate check over millions of generated solutions found none), coinciding only at $t = 0$ where one family is skipped. The rare imprimitive cases where $3 - 2i$ divides $s + t i$ (giving $13 | gcd(u, v)$) are caught by an explicit $gcd(u, v) = 1$ test. Since $max(u, v) >= sqrt(13\/2) g$, the constraint $y <= N$ forces $g <= sqrt(N \/ 2.55)$, so $s <= N^(1\/4)$ and the whole enumeration is a $approx 10^8$-pair numba loop. The parametrization reproduces the full brute-force solution set for small bounds and the given $S(10^2) = 124$, $S(10^3) = 1470$, $S(10^5) = 2340084$.

One amusing trap: the loop bound must be precomputed, since writing it as $2 s^4 <= 13 N^2$ overflows int64 for $N = 10^16$ and silently returns $0$.

#pagebreak()
#link("https://projecteuler.net/problem=749")[= Problem 749: Near Power Sums]

Solution: 13459471903176422

$n$ is a _near power sum_ if for some positive integer $k$ the sum of the $k$th powers of its digits equals $n + 1$ or $n - 1$ (e.g. $3^2 + 5^2 = 34 = 35 - 1$). We need $S(16)$, the sum of all such numbers with at most $16$ digits.

The power sum depends only on the *multiset* of digits, so enumerate multisets rather than the $10^16$ numbers: for each length $d <= 16$ there are $binom(d + 9, 9)$ multisets, about $5.3$ million in total. For a multiset, run $k = 1, 2, dots$ and form $s = sum_v c_v dot v^k$; the only candidates this multiset can certify are $n = s - 1$ and $n = s + 1$, so check whether either lies in the $d$-digit range and has exactly this digit multiset. Stop increasing $k$ once $s$ exceeds $10^16 + 1$, or immediately after $k = 1$ when every digit is $0$ or $1$ (then $s$ never grows). Powers in the lookup table are clamped at $10^16 + 2$ so the running sums cannot overflow 64-bit integers before the cut-off test fires.

A number may qualify for several exponents $k$ (or as both $s - 1$ of one power sum and $s + 1$ of another), so collect the hits and sum the distinct values. The whole search runs in seconds under Numba; $S(2) = 110$ and $S(6) = 2562701$ agree with the problem.

#pagebreak()
#link("https://projecteuler.net/problem=750")[= Problem 750: Optimal Card Stacking]

Solution: 160640

Cards $1, dots, N$ sit at table positions $1, dots, N$, the card at position $p$ being $3^p mod (N + 1)$ (a permutation when defined). A pile may be dragged onto another pile only if the result is in sequence; $G(N)$ is the minimal total horizontal drag distance to reach a single pile, and we need $G(976)$.

Any pile that can ever appear holds a consecutive range of cards $[i..j]$, since "in sequence" must hold for the final pile and every merge preserves it. Dropping pile $[i..k]$ onto pile $[k+1..j]$ reads, top to bottom, $i, dots, k, k+1, dots, j$ — in sequence — whereas the reverse drop is not. So the moving pile always carries the smaller cards, the merged pile remains where the target stood, and by induction every pile $[i..j]$ sits at the original position of card $j$. The cost of the merge is $|"pos"[k] - "pos"[j]|$, giving the interval DP
$
"dp"[i][j] = min_(i <= k < j) ("dp"[i][k] + "dp"[k+1][j] + |"pos"[k] - "pos"[j]|),
$
with $G(N) = "dp"[1][N]$. The position convention is confirmed by $G(6) = 8$ and $G(16) = 47$ (the plausible alternative — piles sitting at the position of their smallest card — gives $9$ and $54$ and is ruled out). The $O(N^3)$ table for $N = 976$ is under a billion cheap operations, a few seconds with Numba.

#pagebreak()
#link("https://projecteuler.net/problem=751")[= Problem 751: Concatenation Coincidence]

Solution: 2.223561019313554106173177

From a real $theta$, the rule $b_1 = theta$, $b_n = floor(b_(n-1)) (b_(n-1) - floor(b_(n-1)) + 1)$, $a_n = floor(b_n)$ generates a non-decreasing integer sequence, and $tau(theta)$ is the decimal $a_1 . a_2 a_3 a_4 dots$ obtained by concatenating its terms. We want the unique fixed point $tau(theta) = theta$ with $a_1 = 2$.

The key observation is that $tau$ is a contraction: the first several terms $a_1, dots, a_m$ depend only on the leading digits of $theta$, so if $theta$ and $theta'$ agree to $d$ decimal places then $tau(theta)$ and $tau(theta')$ agree to (more than) $d$ places. Hence simple iteration converges: start from $theta = 2$, repeatedly replace $theta$ with $tau(theta)$ (computed with `Decimal` arithmetic at $34$-digit precision, concatenating terms until the fractional part is long enough), and stop when the value no longer changes. Truncating the fixed point to $24$ places gives the answer.

#pagebreak()
#link("https://projecteuler.net/problem=752")[= Problem 752: Powers of $1 + sqrt(7)$]

Solution: 5610899769745488

Writing $(1 + sqrt(7))^n = alpha(n) + beta(n) sqrt(7)$, $g(x)$ is the least $n > 0$ with $alpha(n) equiv 1$ and $beta(n) equiv 0 mod x$ (or $0$ if none); we need $G(10^6) = sum_(x=2)^(10^6) g(x)$, exactly.

$g(x)$ is the multiplicative order of the element $u = 1 + sqrt(7)$ in the ring $bb(Z)[sqrt(7)] \/ (x)$. Since $(1 + sqrt(7))(1 - sqrt(7)) = -6$, $u$ is a unit exactly when $6$ is invertible, so $g(x) = 0$ iff $gcd(x, 6) > 1$ (matching $g(3) = 0$), and otherwise the order exists. By the Chinese remainder theorem $g(x)$ is the lcm of $g(p^e)$ over the prime powers dividing $x$.

For a prime $p >= 5$, $p != 7$: if $7$ is a quadratic residue mod $p$ the ring splits as $bb(F)_p times bb(F)_p$ and the unit group has exponent $p - 1$; otherwise it is $bb(F)_(p^2)^*$ of order $p^2 - 1$. Start the order at that exponent and strip it: for each prime $q$ dividing it (factored with a smallest-prime-factor sieve, conveniently via $p - 1$ and $p + 1$), keep dividing by $q$ while $u^("order"\/q) = 1$, testing with binary exponentiation on pairs $(alpha, beta)$. For $p = 7$ the ring is $bb(F)_7 [t] \/ (t^2)$ where $(1 + t)^n = 1 + n t$, so the order is $7$; the code finds it by lifting from $1$. Orders lift to prime powers in the usual way: $g(p^e)$ equals $g(p^(e-1))$ multiplied by $p$ as long as the power is not the identity modulo $p^e$.

Finally each $x <= 10^6$ coprime to $6$ is factored by the sieve and the lcm assembled; the exact total fits comfortably in 64 bits. The givens $G(10^2) = 28891$ and $G(10^3) = 13131583$ agree.

#pagebreak()
#link("https://projecteuler.net/problem=753")[= Problem 753: Fermat Equation]

Solution: 4714126766770661630

$F(p)$ counts solutions of $a^3 + b^3 equiv c^3 space (mod p)$ with $1 <= a, b, c < p$; we sum $F(p)$ over primes $p < 6000000$ (exactly, no modulus).

== Two cases

If $p equiv.not 1 space (mod 3)$, cubing is a bijection on the nonzero residues (also for $p = 3$, where $x^3 equiv x$), so $F(p)$ counts pairs $(a, b)$ of nonzero residues with $a + b eq.not 0$: $F(p) = (p-1)(p-2)$. This matches $F(5) = 12$.

If $p equiv 1 space (mod 3)$, use Gauss's classical count for the Fermat cubic: the projective curve $x^3 + y^3 + z^3 = 0$ over $bb(F)_p$ has
$
N = p + 1 + a, quad "where" 4p = a^2 + 27 b^2, space a equiv 1 space (mod 3),
$
a condition that pins down $a$ (including its sign) uniquely. The affine solution count of $x^3 + y^3 = z^3$ is $(p-1) N + 1$, since each projective point gives $p - 1$ scalings plus the origin. Solutions with a zero coordinate: each of the three coordinate hyperplanes contributes $3(p-1)$ nonzero solutions (e.g. $z = 0$ forces $x^3 = (-y)^3$, three $x$ per $y$ as the cube roots of unity number three), and inclusion–exclusion over the all-zero point gives $9(p-1) + 1$ in total. Hence
$
F(p) = (p-1) N + 1 - 9(p-1) - 1 = (p-1)(p + a - 8),
$
which gives $F(7) = 6 dot (7 + 1 - 8) = 0$ as stated ($28 = 1^2 + 27$, $a = 1$). The formula was also checked against brute force for all primes up to $67$.

== Computation

Sieve the primes below six million. For each $p equiv 1 space (mod 3)$, find the representation $4p = a^2 + 27 b^2$ by scanning $b$ and testing $4p - 27 b^2$ for squareness; $b$ stays below $sqrt(4p\/27) approx 940$, so the whole sum takes a few seconds under Numba. The total, about $4.7 dot 10^18$, still fits in a signed 64-bit integer.

#pagebreak()
#link("https://projecteuler.net/problem=754")[= Problem 754: Product of Gauss Factorials]

Solution: 785845900

The Gauss factorial $g(m)$ multiplies the positive integers up to $m$ coprime to $m$; we need $G(10^8) = product_(m <= 10^8) g(m)$ modulo $10^9 + 7$.

Möbius inversion over the coprimality condition gives
$
g(m) = product_(d | m) ((m\/d)! dot d^(m\/d))^(mu(d)),
$
and exchanging the order of the double product,
$
G(n) = product_(d <= n) ("SF"(M) dot d^(T(M)))^(mu(d)), quad M = floor(n \/ d), space T(M) = M(M+1)\/2,
$
where $"SF"(M) = product_(m <= M) m!$ is the superfactorial.

The quotient $M$ takes only $O(sqrt(n))$ distinct values, so group the $d$ sharing a quotient: each block contributes $"SF"(M)^s dot (P_+ \/ P_-)^(T(M))$ where $s$ is the sum of $mu$ over the block and $P_(plus.minus)$ are the products of the $d$ with $mu(d) = plus.minus 1$. Per block this needs running products (linear in $d$ overall) and a couple of modular powers, with exponents of $d$ reduced modulo $10^9 + 6$ by Fermat (every $d < p$). The superfactorial values at all block quotients come from one linear factorial pass to $10^8$ that records checkpoints, and a linear Möbius sieve provides $mu$. Factors with negative exponent are collected into a denominator and inverted once at the end.

The whole computation is about $3 dot 10^8$ modular multiplications. The construction was cross-checked against direct computation of $G(n)$ for many small $n$, including the given $G(10) = 23044331520000$.

#pagebreak()
#link("https://projecteuler.net/problem=755")[= Problem 755: Not Zeckendorf]

Solution: 2877071595975576960

$f(n)$ counts the ways to write $n$ as a sum of distinct Fibonacci numbers from ${1, 2, 3, 5, 8, dots}$ (with $f(0) = 1$), and $S(n) = sum_(k=0)^(n) f(k)$. We need $S(10^13)$.

Summing $f$ over $k <= N$ counts pairs (representation, total), which is simply the number of *subsets* of Fibonacci numbers with sum at most $N$ — the empty subset accounts for $f(0)$. Count these from the largest Fibonacci number downward. With $P_i = F_1 + dots + F_i$ the prefix sums, define $C(i, "cap")$ as the number of subsets of the first $i$ Fibonacci numbers with sum $<= "cap"$:
- if $"cap" < 0$, none;
- if $"cap" >= P_i$, every subset qualifies: $2^i$;
- otherwise $C(i, "cap") = C(i-1, "cap") + C(i-1, "cap" - F_i)$.

The shortcuts do the heavy lifting: each Fibonacci number exceeds half the prefix sum below it, so the caps reachable at level $i$ without triggering a shortcut form only a handful of distinct values, and a memoised recursion touches a few thousand states for $N = 10^13$ (64 Fibonacci numbers). Plain Python with `functools.cache` answers instantly; $S(100) = 415$ and $S(10^4) = 312807$ match.

#pagebreak()
#link("https://projecteuler.net/problem=756")[= Problem 756: Approximating a Sum]

Solution: 607238.610661

A uniform random increasing $m$-tuple $0 < X_1 < dots < X_m <= n$ approximates $S = sum_(k<=n) f(k)$ by $S^* = sum_i f(X_i)(X_i - X_(i-1))$. We need $bb(E)(Delta | phi(k), 12345678, 12345)$ with $Delta = S - S^*$, to six decimals.

== A cancellation-free closed form

Naively $bb(E)[Delta]$ is the difference of two quantities near $4.6 dot 10^13$ needed to $10^(-7)$ — hopeless numerically. Instead condition on $k$ being selected with predecessor $j$: the gap weight is $binom(n - (k - j) - 1, m - 2)$, and summing over $j$ with the hockey-stick and the Vandermonde-type identity $sum_d d binom(n - d - 1, m - 2) = binom(n, m)$ collapses everything to the positive form
$
bb(E)[Delta] = sum_(k=1)^(n) f(k) binom(n - k, m) / binom(n, m).
$
This was verified by exhaustive enumeration over all $m$-subsets for several small $(n, m)$ and three different $f$, and reproduces $bb(E)(Delta | k, 100, 50) = 2525\/1326$ exactly.

== Evaluation

The weight $R(k) = product_(j < k) (n - m - j)\/(n - j)$ decays like $e^(-k m\/n)$ (scale $approx 1000$ here), so only $k$ up to a few hundred thousand matter; the truncation tail is below $10^(-25)$. The running product is kept in $40$-digit `Decimal` so accumulated rounding cannot touch the sixth decimal, with $phi$ from a small sieve. The given $bb(E)(Delta | phi, 10^4, 10^2) = 5842.849907$ reproduces to all shown digits.

#pagebreak()
#link("https://projecteuler.net/problem=757")[= Problem 757: Stealthy Numbers]

Solution: 75737353

$N$ is _stealthy_ if $N = a b = c d$ with $a + b = c + d + 1$. We count stealthy numbers up to $10^14$.

== Parametrisation

The stealthy numbers are exactly $N = x(x+1) y(y+1)$ for positive integers $x, y$. One direction is a direct check: the factor pairs $(x y, (x+1)(y+1))$ and $(x(y+1), y(x+1))$ both multiply to $N$, with sums $2 x y + x + y + 1$ and $2 x y + x + y$.

For the converse, suppose $a b = c d = N$ and $a + b = s + 1$, $c + d = s$. Then $a, b$ and $c, d$ are integer roots of $t^2 - (s+1) t + N$ and $t^2 - s t + N$, so both discriminants are perfect squares: $(s+1)^2 - 4N = D_1^2$ and $s^2 - 4N = D_2^2$. Subtracting, $(D_1 - D_2)(D_1 + D_2) = 2s + 1$, which is odd, so $D_1 - D_2 = u$ and $D_1 + D_2 = v$ for odd $u, v$ with $u v = 2s + 1$. Then
$
4N = s^2 - D_2^2 = ((u v - 1)/2)^2 - ((v - u)/2)^2 = ((u^2 - 1)(v^2 - 1))/4,
$
and writing $u = 2x + 1$, $v = 2y + 1$ gives $N = x(x+1) y(y+1)$ (with $x, y >= 1$ since $N > 0$).

== Counting

Enumerate all products $x(x+1) y(y+1) <= 10^14$ with $x <= y$; there are about $8 dot 10^7$ pairs since $x <= 3162$ and $y$ ranges up to roughly $10^7 \/ x$. The same $N$ can arise from different pairs, so collect the values into an array, sort, and count distinct entries. The given $2851$ stealthy numbers up to $10^6$ confirms the method (and a brute-force check of the parametrisation against the definition agrees up to $5000$).

#pagebreak()
#link("https://projecteuler.net/problem=758")[= Problem 758: Buckets of Water]

Solution: 331196954

Buckets of sizes $a$, $b$, $a + b$ (coprime $a <= b$) start with the small two full; pours run until the source empties or the destination fills, and $P(a, b)$ is the minimal number of pours until some bucket holds exactly one litre. We need $sum P(2^(p^5) - 1, 2^(q^5) - 1)$ over primes $p < q < 1000$, modulo $10^9 + 7$.

== Closed form for $P$

Since the large bucket can always absorb or supply a full small-bucket move, the state is $(s, m)$ and the moves are the classic two-jug operations. BFS experiments show the shortest solution is always one of the two *pure cyclic* strategies (pour $S -> M$ with refills/empties, or the mirror); on each cycle the medium bucket holds $a k mod b$ after $k$ transfers, and the litre appears at the first $k$ with $a k equiv plus.minus 1 (mod b)$. Counting fills, empties and pours gives $2(k + floor(a k\/b)) - 2$ for the $+1$ branch and $+1$ for the $-1$ branch, and similarly with roles swapped. Writing $a x + b y = 1$ for the minimal Bezout pair ($|x| < b\/2$, $|y| < a\/2$), the four branch counts pair up — each direction's $-1$ branch exceeds the other direction's $+1$ branch by exactly $3$ — and everything collapses to
$
P(a, b) = 2(|x| + |y|) - 2.
$
This was verified against BFS for every coprime pair with $3 <= a < 60$, $b < 140$, and reproduces $P(3,5) = 4$, $P(7,31) = 20$, $P(1234, 4321) = 2780$.

== Mersenne arithmetic

For $a = 2^u - 1$, $b = 2^v - 1$ the Euclidean algorithm mirrors Euclid on the exponents: $M_(e_0) mod M_(e_1) = M_(e_0 mod e_1)$, with true quotient $Q = sum_(j < t) 2^(e_2 + j e_1)$ ($t = floor(e_0\/e_1)$), a geometric series evaluated modulo $10^9 + 7$ (with the $2^(e_1) equiv 1$ degenerate case handled separately). Bezout coefficient signs alternate, so their *magnitudes* obey $m_("new") = m_("prev2") + Q m_("prev1")$ and can be tracked purely mod $p$ — no comparisons are ever needed because the $min$ over branches was already absorbed into $|x| + |y|$. The exponent Euclid on $(q^5, p^5)$ takes a few dozen steps; the modular routine was cross-checked against exact big-integer Bezout computation for exponent pairs up to $(3^5, 5^5)$, and the $14000$ prime pairs finish in about a second.

#pagebreak()
#link("https://projecteuler.net/problem=759")[= Problem 759: A Squared Recurrence Relation]

Solution: 282771304

$f$ satisfies $f(1) = 1$, $f(2n) = 2 f(n)$ and $f(2n+1) = 2n + 1 + 2 f(n) + f(n)\/n$; we need $S(10^16) = sum_(i <= 10^16) f(i)^2$ modulo $10^9 + 7$.

== Closed form

Induction gives $f(n) = n dot b(n)$ with $b$ the binary digit sum: the even case is immediate, and for the odd case
$
f(2n + 1) = (2n + 1) + 2 n b(n) + b(n) = (2n+1)(b(n) + 1) = (2n+1) dot b(2n+1).
$
(Also verified directly against the recurrence, with exact rationals, for all $n < 20000$.)

== Digit DP

So $S(N) = sum_(m <= N) m^2 b(m)^2$, a classic binary digit walk. For $k$-bit blocks define the nine joint moments $M_k [a][c] = sum_(s < 2^k) s^a b(s)^c$ for $a, c in {0, 1, 2}$; splitting on the top bit,
$
M_k [a][c] = M_(k-1) [a][c] + sum_(i <= a) sum_(j <= c) binom(a, i) binom(c, j) (2^(k-1))^(a-i) M_(k-1) [i][j].
$
Now scan the bits of $N$ from the top. Every set bit at position $k$ contributes the block of $2^k$ integers sharing the prefix above it — prefix value $A$, prefix digit sum $B$ — namely
$
sum_(s < 2^k) (A + s)^2 (B + b(s))^2 = sum_(i, j) binom(2, i) binom(2, j) A^(2-i) B^(2-j) M_k [i][j],
$
and $N$ itself is added at the end. Everything is $O(log^2 N)$ arithmetic. The givens $S(10) = 1530$ and $S(10^2) = 4798445$ hold, and the DP was cross-checked against direct summation for $200$ random $N$ up to $50000$.

#pagebreak()
#link("https://projecteuler.net/problem=760")[= Problem 760: Sum over Bitwise Operators]

Solution: 172747503

With $g(m, n) = (m xor n) + (m or n) + (m and n)$, we need $G(N) = sum_(n <= N) sum_(k <= n) g(k, n - k)$ for $N = 10^18$, modulo $10^9 + 7$.

Since $m xor n = m + n - 2(m and n)$ and $m or n = m + n - (m and n)$,
$
g(k, n - k) = 2n - 2 (k and (n - k)),
$
so $G(N) = 2 sum_(n <= N) n(n + 1) - 2 F(N) = 2N(N+1)(N+2)\/3 - 2F(N)$, where $F(N)$ sums $k and m$ over all pairs $k, m >= 0$ with $k + m <= N$.

$F$ has a clean divide and conquer over the low bits: writing $k = 2k' + i$, $m = 2m' + j$, the AND equals $2(k' and m') + (i and j)$ and the constraint becomes $k' + m' <= floor((N - i - j)\/2)$. Summing the four $(i, j)$ choices,
$
F(N) = 2 [F(floor(N/2)) + 2 F(floor((N-1)/2)) + F(floor((N-2)/2))] + P(floor((N-2)/2)),
$
where $P(M) = (M+1)(M+2)\/2$ counts pairs with $k' + m' <= M$ (each contributes $1$ in the $i = j = 1$ case). The recursion arguments are $floor(N \/ 2^t)$ up to small shifts, so memoisation visits $O(log^2 N)$ states — microseconds in Python. The givens $G(10) = 754$ and $G(10^2) = 583766$ hold, and the function matches brute force on $37$ values up to $800$.

#pagebreak()
#link("https://projecteuler.net/problem=764")[= Problem 764: Asymmetric Diophantine Equation]

Solution: 255228881

We sum $x + y + z$ over solutions of $16x^2 + y^4 = z^2$ with $1 <= x, y, z <= 10^16$ and $gcd(x, y, z) = 1$, modulo $10^9$.

== Two parametric families

$(4x, y^2, z)$ is a Pythagorean triple. Any odd prime dividing all of $y^2$ and $z$ also divides $x$ (from $16x^2 = z^2 - y^4$), contradicting primitivity, so the triple's gcd is a power of two.

*$y$ odd.* The triple is primitive with odd leg $y^2$: $y^2 = m^2 - n^2$, $4x = 2m n$, $z = m^2 + n^2$ with $m, n$ coprime of opposite parity. Then $m - n$ and $m + n$ are coprime odd squares $s^2 < t^2$ with $s t = y$, which unwinds to
$
x = (t^4 - s^4)/8, quad y = s t, quad z = (s^4 + t^4)/2, quad s < t "odd, coprime".
$

*$y$ even.* Then $x$ is odd, and reducing powers of two ($y = 2u$, $z = 4w$) leaves the primitive triple $x^2 + u^4 = w^2$. The even leg must be $u^2$ (else $x = 2m n$ would be even), so $u^2 = 2m n$ with coprime $m, n$; one of them is $2p^2$ and the other an odd square $q^2$, giving $u = 2 p q$ and
$
x = |4p^4 - q^4|, quad y = 4 p q, quad z = 16 p^4 + 4 q^4, quad q "odd", gcd(p, q) = 1.
$

The parameters are recoverable from $(y, z)$ within each family and the families have opposite $y$-parity, so nothing is counted twice. Completeness was verified against a brute-force solver up to $N = 1500$, and the family enumeration reproduces $S(10^2) = 81$, $S(10^4) = 112851$ (26 solutions) and $S(10^7) equiv 248876211$.

== Enumeration

The hypotenuse bound $z <= N$ is the binding one ($x, y <= N$ then follow, and $x >= 1$ holds since $q^2 = 2p^2$ is impossible). Family A needs $s^4 + t^4 <= 2N$, so $t < 11900$; family B needs $16p^4 + 4q^4 <= N$. A few tens of millions of coprimality tests under Numba finish in seconds.

#pagebreak()
#link("https://projecteuler.net/problem=765")[= Problem 765: Trillionaire]

Solution: 0.2429251641

Starting with $1$ gram of gold, each of $1000$ rounds you may bet any amount up to your wealth on a coin that pays double with probability $0.6$; we want the maximum probability of holding at least $10^12$ grams at the end, to ten decimals.

== Reduction to a counting problem

A bet of $b$ moves wealth by $+b$ or $-b$, so *under the fair $1\/2$ measure* the wealth process is a nonnegative martingale regardless of strategy — and conversely every nonnegative binary martingale is realised by legal bets. The cheapest way to guarantee wealth $>= T$ exactly on a set $S$ of outcome sequences is the conditional-expectation martingale of $T dot bb(1)_S$, costing $T dot |S| \/ 2^1000$. Hence a success set is achievable iff
$
|S| <= k = floor(x_0 dot 2^1000 / T) = floor(2^1000 / 10^12),
$
and the optimal strategy simply selects the $k$ *most probable* sequences — those with the most wins:
$
V = sum_("top" k "sequences") p^w q^(1000 - w).
$
This was verified to agree exactly (in rational arithmetic) with the full Bellman dynamic program on every dyadic wealth state for all horizons up to $11$. Notably, bold play is strictly suboptimal here — with a favourable coin, spare time buys extra paths to the target — so the classical subfair bold-play result does not transfer; the first thing checked, and refuted, was exactly that.

== Evaluation

Take whole win-count layers $binom(1000, w)$ from $w = 1000$ downward until the budget $k$ is exhausted, with a partial layer at the boundary (around $w approx 611$). Everything is exact integer arithmetic: $V = N \/ 10^1000$ with $N$ assembled from $6^w 4^(1000-w)$ terms, rounded half-up to ten decimals at the end — no floating point anywhere.

#pagebreak()
#link("https://projecteuler.net/problem=768")[= Problem 768: Chandelier]

Solution: 14655308696436060

$f(n, m)$ counts placements of $m$ candles in a ring of $n$ holders with the chandelier balanced; we need $f(360, 20)$.

== Vanishing sums of roots of unity

Balance means the unit vectors at the chosen positions sum to zero, i.e. the chosen subset of $ZZ_360$ has vanishing sum of $360$th roots of unity. Write $ZZ_360 = ZZ_8 times ZZ_9 times ZZ_5$ with $zeta_360 = zeta_8 zeta_9 zeta_5$. Since $zeta_8^(a+4) = -zeta_8^a$, the sum vanishes iff for each $a in {0, dots, 3}$ the difference function $y_a (v, w) = x(a, v, w) - x(a + 4, v, w) in {-1, 0, 1}$ has vanishing $zeta_45$-sum. A cell pair contributes weight $t$ when $y = plus.minus 1$ (one candle) and $1 + t^2$ when $y = 0$ (zero or two candles), so $f(360, m) = [t^m] W(t)^4$.

In turn, the only $ZZ_5$ relation is $1 + zeta_5 + dots + zeta_5^4 = 0$, so a $ZZ_45$ sum vanishes iff all five $ZZ_9$-columns of $y$ have the *same image* in $ZZ[zeta_9]$. Grouping the $3^9$ column functions by image (there are $6859$ classes) with weight $t^(\#"nonzero") (1 + t^2)^(9 - \#"nonzero")$ gives $W = sum_kappa P_kappa (t)^5$, and all polynomial arithmetic is truncated at $t^20$. The identical machinery at $n = 36$ (two $ZZ_4$-pairs over one $ZZ_9$ column, $f = [t^m] V^2$ with $V$ the zero-image class) reproduces the given $f(36, 6) = 876$, and the small cases $f(4, 2) = 2$, $f(12, 4) = 15$ check out by direct enumeration. The whole computation takes a fraction of a second.

#pagebreak()
#link("https://projecteuler.net/problem=769")[= Problem 769: Binary Quadratic Form II]

Solution: 14246712611506

$C(N)$ counts primitive representations $z^2 = x^2 + 5x y + 3y^2$ with $x, y > 0$ coprime and $z <= N$; we need $C(10^14)$.

== Parametrising the conic

The conic $x^2 + 5x y + 3y^2 = z^2$ has the rational point $(1, 0, 1)$; projecting lines through it gives
$ (x : y : z) = (3t^2 - s^2 : -t(2s + 5t) : s^2 + 5s t + 3t^2), $
a bijection between $(s : t)$ and rational points. For coprime $(s, t)$ the gcd of the three forms is $13$ exactly when $s equiv 4t space (mod 13)$ ($4$ is the double root of $c^2 + 5c + 3$ modulo $13$, the discriminant) and $1$ otherwise. Requiring $x, y, z > 0$ forces all three forms to share a sign, which happens precisely for $s\/t in (-5\/2, -sqrt(3))$, all negative; the primitive solution is then $(-X, -Y, -Z)\/d$. The whole correspondence was verified by matching a direct brute-force count at $N = 100$ and $1000$.

== Counting lattice points in the wedge

$C(N)$ thus counts coprime lattice points in a hyperbolic wedge: those with $-Z <= N$, plus those satisfying the mod-$13$ congruence with $N < -Z <= 13N$. Möbius inversion removes coprimality (when $13 | g$ the congruence becomes automatic), and each wedge count runs over $t = O(sqrt(M))$ columns with exact integer-square-root endpoints — the constraint $s^2 + 5s t + 3t^2 >= -M$ becomes $u = 2s + 5t >= sqrt(13t^2 - 4M)$ with the parity of $u$ fixed by $t$, and the congruence class is counted by floor division. About $3 dot 10^8$ operations, four seconds in numba, matching $C(10^3) = 142$ and $C(10^6) = 142463$.

#pagebreak()
#link("https://projecteuler.net/problem=770")[= Problem 770: Delphi Flip]

Solution: 127311223

A displays an amount $x$ up to her current gold; B either TAKEs it or GIVEs the same amount, with $n$ of each over the game. $g(X)$ is the least $n$ for which A can guarantee finishing with $X$ grams from $1$; we need $g(1.9999)$.

== Game value

By scaling, A's guaranteed multiplier $V(t, g)$ depends only on the moves remaining. Displaying the fraction that equalises B's two options gives the harmonic-mean recursion
$
V(t, g) = (2 V(t-1, g) V(t, g-1)) / (V(t-1, g) + V(t, g-1)), quad V(0, g) = 2^g, quad V(t, 0) = 1.
$
The reciprocal $U = 1\/V$ simply *averages*, so $U(n, n)$ is the expected boundary value of a fair coordinate-decrementing walk. The $g = 0$ boundary is hit with total probability exactly $1\/2$ (a fair race to $n$), and the $t = 0$ boundary telescopes by the hockey-stick identity, leaving the clean closed form
$
U(n, n) = 1/2 + binom(2n - 1, n) / 4^n,
$
verified against the exact rational game DP for all $n <= 8$, and reproducing $g(1.7) = 10$.

== Search

$g(X)$ is the least $n$ with $binom(2n-1, n)\/4^n <= (2 - X)\/(2X) = 1\/39998$, and the left side is strictly decreasing (ratio $(2n+1)\/(2n+2)$). Since $n approx 1.27 dot 10^8$ and consecutive values differ by only $approx 4 dot 10^(-9)$ relatively, double precision is insufficient; the comparison is done in $50$-digit `Decimal` arithmetic via the Stirling series for $ln Gamma$ (truncation error below $10^(-40)$ at this scale), with a doubling-plus-bisection search.

#pagebreak()
#link("https://projecteuler.net/problem=771")[= Problem 771: Pseudo Geometric Sequences]

Solution: 398803409

$G(N)$ counts strictly increasing sequences of at least $5$ terms $<= N$ with $|a_i^2 - a_(i-1) a_(i+1)| <= 2$ for all interior $i$; we need $G(10^18)$ mod $10^9 + 7$.

== Rigidity and classification

Write $e_i = a_i^2 - a_(i-1) a_(i+1)$. From a pair $(x, y)$ the successor is $z = (y^2 - e)\/x$, so $e equiv y^2 (mod x)$: two residues in $[-2, 2]$ can coincide mod $x$ only for $x <= 3$ ($x = 4$ never branches as squares are $0$ or $1$ mod $4$). Since terms increase, *every sequence is rigid except possibly at its first one or two steps*, and only when it starts with terms $<= 3$.

Long rigid chains classify completely. Scanning all pairs $x in [4, 1500]$, $y <= 10^6$ with rigid depth $>= 3$ gave $304514$ chains and zero exceptions to: (i) *geometric* ($e equiv 0$), ratio $p\/q$ in lowest terms; (ii) *minus recurrences* $a_(i+1) = K a_i - a_(i-1)$ with integer $K >= 3$ and constant invariant $e = x^2 + y^2 - K x y in {plus.minus 1, plus.minus 2}$ ($K = 2$ is the unit-difference arithmetic run); (iii) *plus recurrences* $a_(i+1) = c a_i + a_(i-1)$ with integer $c >= 1$ and alternating Cassini invariant $e_i = (-1)^i J$, $J in {1, 2}$. Integrality of $K$ is provable: $gcd$ of consecutive terms squares into $e$, hence is $1$, and four-term integrality forces $a_1 | e(e - a_0^2)$, which for $|e| <= 2$ makes $(x^2 + y^2 - e)\/(x y)$ an integer (the half-integer case for $|e| = 2$ dies on a parity contradiction). Reduction of the two quadratic forms shows every minus/plus fundamental has $x = 1$: minus has $(1, K)$ for all $K$ ($e = 1$) plus sporadic $(1, 2)$ at $K = 3$ and $(1, 3)$ at $K = 4$; plus has $(1, 2)$ at $c = 1$, $(1, c)$ for $c >= 2$, and sporadic $(1, 3)$ at $c = 2$.

== Counting by starting pair

Partitioning sequences by their first pair: *Case 3* ($a_0 >= 4$): each zone-maximal rigid chain with $L + 1$ terms contributes $(L - 3)(L - 2)\/2$. The arithmetic chain $4 dots N$ gives $(N - 7)(N - 6)\/2$; geometric maximal chains are counted by $(p, q, c, M)$, where backward-maximality is $p divides.not c$ and forward-maximality is *not* ($q | c$ and $(c\/q) p^(M+1) <= N$) — the forward correction is independent of $q$, a subtlety first exposed by a one-sequence discrepancy at $N = 243$ where the chain $32, 48, 72, 108, 162$ extends to $243 = c p^(M+1)\/q$. Chains with head $c q^M < 4$ (only $q = 1$, $c <= 3$) are enumerated explicitly with zone truncation, and minus/plus chains contribute for $K, c lt.tilde (4N)^(1\/5) approx 4000$. *Case 2* ($a_0 <= 3 < 4 <= a_1$): the fifth term grows like $a_1^4\/a_0^3$, so a direct loop over $a_1 <= 75100$ with exact integer walks suffices. *Case 1* (starts $(1,2), (1,3), (2,3)$): a tiny explicit DFS with closed-form arithmetic tails.

The result matches a full DFS brute force at $N = 6, 10, 100, 243, 1000, 2000, 5000, 12345, 20000$ exactly, and $G(10^18)$ evaluates in under a second.

#pagebreak()
#link("https://projecteuler.net/problem=772")[= Problem 772: Balanceable Partitions]

Solution: 83985379

$f(k)$ is the smallest $N$ all of whose $k$-bounded partitions (parts $<= k$) can be split into two equal-sum halves; we need $f(10^8)$ mod $10^9 + 7$.

== The answer is $2 op("lcm")(1, dots, k)$

Necessity is the easy direction: for any $d <= k$ that tiles $N$, the partition into all $d$'s (plus a forced remainder) has subset sums in $d ZZ$, so $N\/2$ must be divisible by enough structure that $N = 2 op("lcm")(1, dots, k)$ becomes the first candidate. Sufficiency is the deep direction; rather than prove it, we verified the claim exhaustively: for $k = 2, 3, 4, 5$, every $k$-bounded partition of every even $N$ up to and including $2 op("lcm")$ was generated and tested for balanceability with subset-sum bitsets — for $k = 5$ this means all $approx 72000$ partitions of $120$ into parts $<= 5$ — confirming $f(k) = 2 op("lcm")(1, dots, k)$ with counterexamples at every smaller even $N$. The given values agree: $f(3) = 12 = 2 dot 6$, and $f(30) = 2 dot 2329089562800 equiv 179092994$.

The computation is then $2 product_(p <= 10^8) p^(floor(log_p 10^8))$ mod $10^9 + 7$ via a numba sieve over the $5761455$ primes below $10^8$.

#pagebreak()
#link("https://projecteuler.net/problem=773")[= Problem 773: Ruff Numbers]

Solution: 556206950

$S_k$ holds $2$, $5$ and the first $k$ primes ending in $7$; $N_k$ is their product, and $F(k)$ sums the numbers below $N_k$ ending in $7$ that avoid every prime in $S_k$. We need $F(97)$ modulo $10^9 + 7$.

Write $N_k = 10 M$ with $M$ the product of the $k$ primes. Inclusion–exclusion over the subset $T$ of those primes dividing $n$ writes $n = P_T m$ with $m equiv c_T (mod 10)$, where $c_T = 7 dot P_T^(-1) equiv 7 dot 3^(|T|) (mod 10)$ because every prime is $equiv 7$. Each progression has exactly $"cnt"_T = M\/P_T$ terms below $N_k$, summing to $P_T "cnt"_T (c_T + 5("cnt"_T - 1))$ — and the three pieces factor completely:
- $P_T "cnt"_T = M$ is constant, so the $c_T$ piece is $M sum_j (-1)^j binom(k, j) c_j$ with $c_j$ cycling $7, 1, 3, 9$;
- the quadratic piece is $5 M^2 product (1 - 1\/p_i) = 5 M phi(M)$;
- the remaining piece carries $sum_T (-1)^(|T|) = 0$.

So $F(k) = M A + 5 M phi(M)$ — three modular products and a $98$-term alternating sum. This reproduces $F(3) = 76101452$ exactly and matches brute force for $k <= 4$; $F(97)$ is instant.

#pagebreak()
#link("https://projecteuler.net/problem=776")[= Problem 776: Digit Sum Division]

Solution: 9.627509725002e33

$F(N) = sum_(n<=N) n\/d(n)$ where $d$ is the digit sum, for $N = 1234567890123456789$, in scientific notation with twelve digits after the decimal point.

== Digit DP per digit sum

Group the terms by digit sum $s <= 9 dot 19 = 171$: a standard digit DP over the decimal expansion of $N$ accumulates, for each $s$, the exact pair (count, sum of $n$) using integer arithmetic — the running sum updates as $t arrow.r 10 t + "dig" dot c$ per appended digit. Then $F = sum_s ("sum"_s)\/s$, evaluated in $50$-digit `Decimal` so the requested twelve significant digits are exact. The whole computation touches only a few thousand DP states and runs instantly, matching $F(10) = 19$, $F(123)$ and $F(12345)$.

#pagebreak()
#link("https://projecteuler.net/problem=778")[= Problem 778: Freshman's Product]

Solution: 146133880

The freshman's product $a times.square b$ multiplies decimal numbers digit-by-digit, keeping only the last digit of each digit product (so $234 times.square 765 = 480$). $F(R, M)$ sums $x_1 times.square dots times.square x_R$ over all tuples with $0 <= x_i <= M$; we need $F(234567, 765432)$ modulo $10^9 + 9$.

The operation acts independently on each decimal position (it is associative, position $j$ of the result being the product of all $j$-th digits modulo $10$), so
$
F(R, M) = sum_(j) 10^j sum_(w=0)^(9) w dot N_j [w],
$
where $N_j [w]$ counts the tuples whose $j$-th digits multiply to $w$ modulo $10$. The $j$-th digits of a single uniform $x in [0, M]$ (padded with leading zeros) follow an easily counted distribution over ${0, dots, 9}$, and $N_j$ is its $R$-fold convolution under the multiplication monoid mod $10$ — computed by binary powering of $10$-vectors, $100$ multiplications per convolution and $log_2 R approx 18$ steps per digit position. Six positions suffice since higher digits are all zero and contribute zero.

The givens $F(2, 7) = 204$ and $F(23, 76) equiv 5870548$ check out, and the construction matches brute force over all tuples for six small $(R, M)$ pairs.

#pagebreak()
#link("https://projecteuler.net/problem=779")[= Problem 779: Prime Factor and Exponent]

Solution: 0.547326103833

With $p(n)$ the smallest prime factor of $n$ and $alpha(n)$ its exponent, $macron(f)_K$ is the mean of $(alpha(n) - 1)\/p(n)^K$; we need $sum_(K >= 1) macron(f)_K$ to twelve decimals.

== Collapsing the sums

The density of ${p(n) = p, alpha(n) = a}$ is $(1 - 1\/p) p^(-a) product_(q < p)(1 - 1\/q)$, and $sum_(a >= 1) (a - 1)(1 - 1\/p) p^(-a) = 1\/(p(p - 1))$, so $macron(f)_K = sum_p product_(q<p)(1 - 1\/q) \/ (p^K p (p - 1))$. Summing the geometric series over $K$ gives
$ sum_(K=1)^infinity macron(f)_K = sum_p (product_(q < p)(1 - 1/q)) / (p (p - 1)^2). $
Terms decay like $1\/(p^3 ln p)$, so primes up to $10^8$ leave a tail far below $10^(-15)$. One sieve pass maintains the running Mertens product with Kahan-compensated accumulators; the same loop reproduces the given $macron(f)_1 approx 0.282419756159$ as a check. Four seconds in numba.

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
#link("https://projecteuler.net/problem=793")[= Problem 793: Median of Products]

Solution: 475808650131120

With $S_0 = 290797$ and $S_(i+1) = S_i^2 mod 50515093$, $M(n)$ is the median of the pairwise products $S_i S_j$ over $0 <= i < j < n$; we need $M(1000003)$.

The half-trillion products cannot be materialised, but their *rank statistics* are cheap: after sorting the $n$ values, the number of pairs with product at most $x$ follows from one two-pointer sweep — as the smaller factor grows, the largest admissible partner only shrinks, so the sweep is linear. Binary-search $x$ for the smallest value whose count reaches the median rank $(binom(n, 2) + 1) \/ 2$ (the pair count is odd here); that $x$ is itself an attained product and hence the median. About $50$ iterations of an $O(n)$ count under Numba answer in a couple of seconds; products stay below $2^63$. Both givens, $M(3)$ and $M(103)$, check out.

#pagebreak()
#link("https://projecteuler.net/problem=800")[= Problem 800: Hybrid Integers]

Solution: 1412403576

A _hybrid-integer_ is $p^q q^p$ for distinct primes $p, q$ (for example $800 = 2^5 5^2$). Since the value's prime factorisation is exactly $p^q q^p$, distinct unordered pairs ${p, q}$ give distinct hybrid-integers, so $C(n)$ counts pairs $p < q$ with $p^q q^p <= n$, i.e.
$
q ln p + p ln q <= ln n, quad n = 800800^800800.
$

For a fixed $p$ the left side increases with $q$, so for each prime $p$ we binary-search the largest prime $q$ that fits and add the number of primes in $(p, q]$. The whole thing needs primes only up to $q_max(2) approx (ln n) \/ ln 2 approx 1.57 dot 10^7$ (the bound is loosest at $p = 2$); larger $p$ run out of room once $2 p ln p > ln n$, around $p approx 4 dot 10^5$.

Floating-point logs place the cutoff to within a prime or two, but the boundary can be hit _exactly_ — already in the example $C(800) = 2$, where $2^5 5^2 = 800$ sits on the line. So after the float binary search the boundary prime is re-checked with a $60$-digit `Decimal` comparison of $q ln p + p ln q$ against $800800 ln 800800$, nudging the count up or down as needed. This reproduces $C(800) = 2$ and $C(800^800) = 10790$.

#pagebreak()
#link("https://projecteuler.net/problem=801")[= Problem 801: $x^y equiv y^x$]

Solution: 638129754

For a prime $p$, count pairs $0 < x, y <= p^2 - p$ with $x^y equiv y^x space (mod p)$, then sum $f(p)$ over the $approx 2.7 dot 10^4$ primes in $[10^16, 10^16 + 10^6]$, modulo $M = 993353399$.

== Reducing $f(p)$ to a counting problem

The range $p^2 - p = p(p - 1)$ is the key. Because $p$ and $p - 1$ are coprime, $x |-> (x mod p, space x mod (p - 1))$ is a bijection from ${1, ..., p(p-1)}$ onto all pairs, and the two coordinates vary independently. By Fermat, $x^y mod p$ depends only on $(x mod p)$ and the exponent $(y mod (p - 1))$; likewise $y^x mod p$ depends only on $(y mod p)$ and $(x mod (p - 1))$. Writing $V(b, e)$ for the value of base$~b$ raised to exponent $e$ (so $V = 0$ when $b equiv 0$, else $b^e mod p$ with $b^0 = 1$), the condition becomes $V(a, beta) = V(c, delta)$ where $a, c$ range over $ZZ \/ p$ and $beta, delta$ over $ZZ \/ (p-1)$, all four free. Hence, grouping by the common value,
$
f(p) = sum_v N(v)^2, quad N(v) = \#{(b, e) : V(b, e) = v}.
$
Splitting off $v = 0$ (which needs $b equiv 0$, giving $N(0) = p - 1$) and writing every nonzero base as a power of a primitive root turns the rest into counting solutions of $i beta equiv k space (mod m)$ with $m = p - 1$. If $T(k)$ counts pairs $(i, j) in (ZZ\/m)^2$ with $i j equiv k$, then
$
f(p) = (p - 1)^2 + A(p - 1), quad A(m) = sum_(k=0)^(m-1) T(k)^2.
$
Brute force confirms $f(5) = 104$, $f(7) = 366$, $f(11) = 1550$.

== A closed form for $A$

$A$ is multiplicative (CRT splits $T$ as a product), so it suffices to evaluate it on prime powers. Classifying pairs by the $p$-adic valuation of each factor gives, for $v_p(k) = t < e$, the value $T(k) = (t + 1) p^t phi(p^(e-t))$, and for $k = 0$ the count $Z$. Summing $T(k)^2$ over the $phi(p^(e-t))$ residues of each valuation class yields
$
A(p^e) = Z^2 + sum_(t=0)^(e-1) (t+1)^2 p^(2t) phi(p^(e-t))^3, quad
Z = p^(2e) - sum_(t=0)^(e-1) (t+1) p^t phi(p^(e-t))^2,
$
with $phi(p^j) = p^(j-1)(p - 1)$. Everything is additions and multiplications, so the whole computation runs modulo $M$ even though $M$ is not prime. This matches the brute-force $A(p^e)$ and reproduces $f(97) = 1614336$, $S(1, 10^2) = 7381000$ and $S(1, 10^5) equiv 701331986 space (mod M)$.

== Evaluating over the window

Primes $p in [10^16, 10^16 + 10^6]$ come from a segmented sieve using base primes up to $sqrt(10^16) = 10^8$. The same base primes drive a parallel factorisation sieve over the shifted window $g = p - 1$: each base prime is divided out of every multiple it hits (recording its exponent and folding $A(q^e)$ into a running product), and any residue left above $1$ is necessarily a single prime $> 10^8$ (two such factors would exceed $10^16$). Summing $(p-1)^2 + A(p-1)$ over the sieved primes gives the answer mod $M$.

#pagebreak()
#link("https://projecteuler.net/problem=802")[= Problem 802: Iterated Composition]

Solution: 973873727

We are given $f(x, y) = (x^2 - x - y^2, 2 x y - y + pi)$ on $RR^2$, and $P(n)$ sums the $x$-coordinates of all points of period $n$ under $f$, where a point has period $n$ when $f^((n))$ fixes it. The answer is $P(10^7) space (mod 1020340567)$.

== The map is a complex polynomial

Identify $(x, y)$ with $z = x + i y$. Since $(x + i y)^2 = (x^2 - y^2) + 2 i x y$, the pair $f(x, y)$ is exactly the real and imaginary parts of
$ g(z) = z^2 - z + i pi, $
because $g(z)$ has real part $x^2 - y^2 - x$ and imaginary part $2 x y - y + pi$. So iterating $f$ is iterating the single complex polynomial $g$.

== Sums of $x$-coordinates by Vieta

A point has period dividing $k$ exactly when it is a root of $g^((k))(z) - z$. This is a *monic* polynomial of degree $2^k$, so by Vieta the sum of its roots is $-[z^(2^k - 1)] g^((k))$, and the sum of the $x$-coordinates is the real part of that. Write
$ S(k) = sum_(g^((k))(z) = z) Re(z). $
Composing $g^((k)) = g compose g^((k-1))$, the subleading coefficient comes only from squaring the leading two terms of $g^((k-1))$; the $-z$ term affects only low-degree coefficients for $k >= 2$. This gives the doubling recurrence $a_k = 2 a_(k-1)$ on the subleading coefficient, and tracing the constant in $g(z) - z = z^2 - 2 z + i pi$ yields
$ S(1) = 2, quad S(k) = 2^(k-1) quad (k >= 2). $
A symbolic check of $g^((k))(z) - z$ for $k <= 5$ confirms $S = 2, 2, 4, 8, 16$.

== Möbius inversion over the minimal period

Let $E(m)$ be the sum of $x$-coordinates over points of _minimal_ period $m$. Then $S(k) = sum_(m | k) E(m)$, and $P(n) = sum_(m=1)^n E(m)$. Reindexing the double sum over the divisor relation gives the clean form
$ P(n) = sum_(d=1)^n S(d) dot M(floor(n \/ d)), $
where $M$ is the Mertens function $M(x) = sum_(i <= x) mu(i)$. This reproduces the given $P(1) = 2$, $P(2) = 2$, $P(3) = 4$.

== Computation

A linear sieve gives $mu(k)$ for $k <= 10^7$; a prefix sum gives $M$. A single pass over $d = 1, ..., 10^7$ accumulates $S(d) dot M(floor(n \/ d))$ modulo $1020340567$, maintaining $2^(d-1)$ as a running power of two and reducing the (possibly negative) Mertens values into range.

#pagebreak()
#link("https://projecteuler.net/problem=803")[= Problem 803: Pseudorandom Sequence]

Solution: 9300900470636

The Rand48 generator iterates $a_n = (25214903917 a_(n-1) + 11) mod 2^48$, emits $b_n = floor(a_n \/ 2^16) mod 52$, and encodes each $b_n$ as a letter ($0 arrow.r a, ..., 25 arrow.r z, 26 arrow.r A, ..., 51 arrow.r Z$). Given that the stream begins #raw("PuzzleOne"), we want the first index at which #raw("LuckyText") appears.

== Recovering the state behind a 9-letter window

Nine letters carry about $9 log_2 52 approx 51$ bits, slightly more than the 48-bit state, so a given 9-letter window is produced by essentially one state $a$. Write $a = x_"lo" + 2^18 y$ with $x_"lo" < 2^18$. The contribution of each output modulo $4$ is just bits $16,17$ of $a_k$, which depend only on $x_"lo"$ (the low 18 bits propagate among themselves under the recurrence modulo $2^18$). The nine mod-$4$ conditions therefore form $18$ bits of constraint on the $18$-bit $x_"lo"$, leaving about one candidate. For each candidate the high $30$ bits $y$ are scanned; the first letter's condition modulo $13$ is affine in $y$ (namely $4 y + "bits" equiv b_0 space (mod 13)$), fixing $y$ modulo $13$ and shrinking the scan by a factor of $13$. All arithmetic is done modulo $2^48$ using 64-bit products masked to 48 bits, which is exact because multiplication modulo $2^64$ preserves the low 48 bits.

This recovers $a_0$ (the state generating #raw("PuzzleOne")) and $a^*$ (the state generating #raw("LuckyText")). The method reproduces the given facts: #raw("EULERcats") yields $a_0 = 78580612777175$, and the #raw("RxqLBfWzv") state sits $100$ steps after $a_0 = 123456$.

== Counting the steps between two states

The affine map $T(x) = A x + C mod 2^48$ satisfies the Hull--Dobell conditions ($C$ odd, $A equiv 1 space (mod 4)$), so it has full period $2^48$ and every state is reached exactly once per period. Hence the step count $n$ from $a_0$ to $a^*$ is unique, and once $T^n(a_0)$ and $a^*$ agree modulo $2^k$, the count is determined modulo $2^k$. Lifting bit by bit: given $n mod 2^k$, exactly one of $n$ or $n + 2^k$ makes $T^n(a_0) equiv a^* space (mod 2^(k+1))$. Each iterate $T^n(a_0)$ is evaluated by fast exponentiation of the affine map. The resulting gap is the first occurrence index.

#pagebreak()
#link("https://projecteuler.net/problem=804")[= Problem 804: Counting Binary Quadratic Representations]

Solution: 4921370551019052

Here $g(n)$ counts integer pairs $(x, y)$ with $x^2 + x y + 41 y^2 = n$, and $T(N) = sum_(n=1)^N g(n)$. Summing $g$ over $1, ..., N$ simply counts every lattice point $(x, y) in ZZ^2$ whose form value lies in $[1, N]$, so $T(N) = \#{(x, y) : 1 <= x^2 + x y + 41 y^2 <= N}$.

== An exact lattice condition

The form is positive definite with discriminant $1 - 4 dot 41 = -163$. Multiplying the inequality by $4$ and completing the square,
$ 4(x^2 + x y + 41 y^2) = (2 x + y)^2 + 163 y^2, $
so $x^2 + x y + 41 y^2 <= N$ is exactly $(2 x + y)^2 <= 4 N - 163 y^2$. For a fixed $y$ with $D = 4 N - 163 y^2 >= 0$, set $s = floor(sqrt(D))$; since $2 x + y$ is an integer, the condition becomes $-s <= 2 x + y <= s$, a contiguous run of $x$ whose length is counted with one floor and one ceiling. Real solutions require $|y| <= 2 sqrt(N \/ 163)$, about $1.57 dot 10^7$ rows for $N = 10^16$.

== Computation

The row count is even in $y$ (sending $x arrow.r -x$ maps the $y$ row to the $-y$ row), so it suffices to sum over $y >= 1$, double, add the $y = 0$ row, and subtract $1$ for the origin (where the form vanishes and is excluded). For $N = 10^16$ the quantity $4 N - 163 y^2$ stays below $4 dot 10^16 < 2^63$, so an exact 64-bit integer square root keeps every floor correct. This reproduces $T(10^3) = 474$ and $T(10^6) = 492128$.

#pagebreak()
#link("https://projecteuler.net/problem=805")[= Problem 805: Shifted Multiples]

Solution: 119719335

Let $s(n)$ move the leading digit of $n$ to the back, and let $N(r)$ be the smallest positive $n$ with $s(n) = r n$ (or $0$ if none exists). We want $T(200) = sum N(u^3 \/ v^3)$ over all ordered coprime pairs $(u, v)$ with $1 <= u, v <= 200$, reported $space (mod 10^9 + 7)$.

== Reducing $N(r)$ to a modular order

Write a $d$-digit number as $n = a dot 10^(d-1) + m$, where $a in {1, ..., 9}$ is the leading digit and $0 <= m < 10^(d-1)$. Moving $a$ to the back gives $s(n) = 10 m + a$, so with $r = u^3 \/ v^3$ the equation $s(n) = r n$ rearranges to
$ m = a dot (u^3 dot 10^(d-1) - v^3) \/ D, quad D = 10 v^3 - u^3. $
Since $s(n) < 10 n$ always, $D > 0$ is required: if $u^3 >= 10 v^3$ then $N(r) = 0$. From $D = 10 v^3 - u^3$ we get $u^3 equiv 10 v^3 space (mod D)$, hence $u^3 dot 10^(d-1) - v^3 equiv v^3 (10^d - 1) space (mod D)$. Writing $D' = D \/ gcd(D, a v^3)$, the integrality condition $D divides a(u^3 10^(d-1) - v^3)$ collapses to
$ D' divides 10^d - 1, quad "i.e." quad 10^d equiv 1 space (mod D'). $
So a valid digit count $d$ exists only when $gcd(10, D') = 1$ (or $D' = 1$), and then $d$ must be a positive multiple of $omega = "ord"_(D')(10)$.

== Selecting the smallest $n$

Two range constraints pin down $d$ for each leading digit $a$. The bound $m >= 0$ forces $10^(d-1) u^3 >= v^3$ (a lower bound on $d$), and $m < 10^(d-1)$ rearranges to $10^(d-1) (u^3 (a+1) - 10 v^3) < a v^3$; when the coefficient $u^3(a+1) - 10 v^3$ is positive this caps $d$ at a tiny value, otherwise it holds for all $d$. Because $n$ lies in the disjoint, increasing window $[a dot 10^(d-1), (a+1) 10^(d-1))$, the candidate with the fewest digits wins, ties broken by the smaller $a$. For each $a$ the best $d$ is the least multiple of $omega$ meeting the lower bound (then checked against the upper bound).

== Computation

For each coprime pair the modulus $D' < 10 v^3 <= 8 dot 10^7$, so its multiplicative order is found by trial-factoring with primes up to $9000$, taking $"ord"_(p^e)(10) divides p^(e-1)(p-1)$ on each prime power and combining by lcm. The winning $N(r)$ is assembled $space (mod 10^9 + 7)$ via $m equiv a(u^3 dot 10^(d-1) - v^3) D^(-1)$ and $n equiv a dot 10^(d-1) + m$, where $D$ is invertible because $D < 10^9 + 7$. This reproduces $N(3) = 142857$, $N(1\/10) = 10$, $N(2) = 0$, and $T(3) = 262429173$.

#pagebreak()
#link("https://projecteuler.net/problem=806")[= Problem 806: Nim on Towers of Hanoi]

Solution: 94394343

Index the $2^n$ positions of the shortest $n$-disk Towers of Hanoi solution from $0$ to $2^n - 1$; reading the position as a Nim game on the three peg heights $(a, b, c)$, the first player loses exactly when $a xor b xor c = 0$. We need $f(10^5)$, the sum of losing indices, modulo $10^9 + 7$.

== Which count triples lose

Since each binary digit of $a xor b xor c$ has even parity, $a + b + c = n$ forces every bit position to occur in exactly zero or two of the three counts, and the doubly-covered positions sum to $n\/2$. So the losing triples are precisely the $3^(\#"bits")$ ways of assigning each binary digit of $m = n\/2$ to one of the three peg pairs — at most $3^6 = 729$ triples for $n = 10^5$.

== From a sum to a count

Reversing time in the Hanoi solution swaps pegs $1$ and $3$: position $2^n - 1 - t$ is position $t$ with the outer pegs exchanged, which permutes the counts and preserves the XOR. The losing indices therefore pair up as $(t, 2^n - 1 - t)$ with no fixed points, so $f(n) = (2^n - 1) dot L(n) \/ 2$ where $L(n)$ merely _counts_ losing positions, and $L(n)$ is the sum of $N(a, b, c)$, the number of indices realising each losing triple, over the few hundred losing triples.

== Counting positions with given peg loads

Processing the $n$ bits of $t$ from the most significant down, the standard recursion (first half: top $n-1$ disks move source $arrow$ spare; second half: source $arrow$ target) shows that maximal runs of equal bits in $t$ are blocks of consecutive disks sitting on a single peg. Tracking which peg hosts each run gives a tidy three-role automaton (current, other, middle): an even-length run swaps current with other, an odd-length run rotates middle into current. Encoding run lengths of each parity as generating-function weights and summing over the automaton's walks with a computer algebra system collapses everything to
$
sum N(a,b,c) thin u^a v^b w^c = (u^2 + w^2 + u v + v w + u + w + 2 u v w) / (1 - u^2 - v^2 - w^2 - 2 u v w).
$
The denominator says $N$ counts sequences of steps $(2,0,0)$, $(0,2,0)$, $(0,0,2)$ and $(1,1,1)$, the last with weight $2$: after shifting by a numerator monomial, summing $2^ell binom(i+j+k+ell, i\, j\, k\, ell)$ over the number $ell$ of diagonal steps evaluates one $N$ in $O(n)$ multiplications with precomputed factorials. Verified against brute force for all $n <= 14$ and against $f(10) = 67518$.

#pagebreak()
#link("https://projecteuler.net/problem=807")[= Problem 807: Loops of Ropes]

Solution: 0.1091523673

Red ropes join $2n$ random circle points $R_0 R_1, dots, R_(n-1) R_0$ and blue ropes likewise, each rope laid above all previous ones; $P(n)$ is the probability the two closed loops can be pulled apart, and we need $P(80)$.

== Separability is a linking number

Because heights increase with time, each loop is a height-monotone arc closed by one vertical strand at its base point on the boundary circle. The two monotone arcs form a pure braid on two strands, and closing a pure $2$-braid $sigma_1^(2k)$ along the boundary yields the $(2, 2k)$ torus link, which splits exactly when $k = 0$. So the loops separate iff the linking number of the red and blue loops vanishes.

== A telescoping formula

Blue rope $j$ lies above red rope $i$ iff $j >= i$, so the linking number is $sum_j$ (signed crossings of blue rope $j$ with the red path $R_0 dots R_j$). Crossings of a path with a chord telescope into a difference of side indicators of the path's endpoints, leaving
$
"lk" = sum_(j=1)^(n-1) s_j, quad s_j = cases(plus.minus 1 & "if chord" B_(j-1) B_j "separates" R_0 "from" R_j, 0 & "otherwise,")
$
with the sign set by orientation; the $j = n$ term dies because the full red loop is closed. A Monte Carlo check of $Pr["lk" = 0]$ reproduces $P(3) = 11\/20$ and $P(5) approx 0.4304177690$.

== Exact evaluation

Fix $R_0 = 0$. Each $s_j$ depends on $(B_(j-1), B_j)$ and the independent uniform $R_j$, so with $z$ marking $s_j$,
$
E[z^("lk")] = E[product_(j=1)^(n-1) g(B_(j-1), B_j)], quad g(b, b') = cases(1 + (b' - b)(z - 1) & b < b', 1 + (b - b')(z^(-1) - 1) & b > b'.)
$
The factors chain through consecutive $B$'s, so iterating the transfer operator $(T f)(b') = integral_0^1 g(b, b') f(b) dif b$ on polynomials in $b$ — whose coefficients are Laurent polynomials in $z$ with rational coefficients — computes $E[z^("lk")]$ exactly after $n - 1$ steps and a final integration. $P(80)$ is the $z^0$ coefficient, an exact rational rounded to ten decimal places.

#pagebreak()
#link("https://projecteuler.net/problem=808")[= Problem 808: Reversible Prime Squares]

Solution: 3807504276997394

A reversible prime square is the square of a prime that is not a palindrome and whose digit reversal is also the square of a prime. Because squares grow with their root, iterating primes in increasing order yields these in increasing order too. Sieve primes up to about $3.2 dot 10^7$ (where the fiftieth occurs); for each prime $p$, reverse $p^2$, and if the reversal is a perfect square whose root is prime, count $p^2$. Stop at the fiftieth and sum.

#pagebreak()
#link("https://projecteuler.net/problem=809")[= Problem 809: Rational Recurrence Relation]

Solution: 75353432948733

The function on positive rationals is $f(x) = x$ for integral $x$, $f(x) = f(1\/(1-x))$ for $x < 1$, and otherwise $f(x) = f(1\/(ceil(x) - x) - 1 + f(x - 1))$; we need $f(22\/7) mod 10^15$.

== Unfolding the recursion

Write $x = k + r$ with fractional part $r = c\/b$ and let $phi(r) = 1\/(1 - r) - 1 = c\/(b - c)$, with whole part $m$ and fractional part $r'$. Since $ceil(x) - x = 1 - r$, the third case reads $f(k + r) = f(phi(r) + f(k - 1 + r))$, and the $x < 1$ case is $f(r) = f(1 + phi(r))$. The fractional parts thus march down the finite chain $r arrow r' arrow dots$ (subtractive Euclid on $(b - c, c)$), ending when some $phi$ is an integer — at which point the argument of the outer $f$ is integral and the recursion bottoms out. Writing $G_i (k) = f(k + r_i)$ for the $i$-th chain fraction,
$
G_i (k) = G_(i+1)(G_i (k - 1) + m_i), quad G_i (0) = G_(i+1)(1 + m_i),
$
with $G_L (k) = (1 + m_L) + k m_L$ at the terminal level — an Ackermann-style cascade. Evaluating these levels bottom-up with exact integers (iterating in $k$, never recursing past the closed terminal form) confirms the given $f(3\/2) = 3$, $f(1\/6) = 65533$ and $f(13\/10) = 7625597484985 = 3^27 - 2$.

== The tower for $22\/7$

For $22\/7 = 3 + 1\/7$ the chain is $1\/7 arrow 1\/6 arrow 1\/5 arrow 1\/4 arrow 1\/3 arrow 1\/2$, all $m_i = 0$ until $phi(1\/2) = 1$. Bottom-up: $G(k, 1\/2) = k + 2$, $G(k, 1\/3) = 2k + 3$, $G(k, 1\/4) = 2^(k+3) - 3$, and $G(k, 1\/5) = 2 arrow.t arrow.t (k+3) - 3$, a power tower of $k + 3$ twos minus $3$. The remaining two levels iterate $x arrow.bar 2 arrow.t arrow.t (x + 3) - 3$, so $f(22\/7)$ is $2 arrow.t arrow.t H - 3$ for a height $H$ far beyond $65536$.

== Modulo $10^15$

The value of $2 arrow.t arrow.t h mod M$ is constant once $h$ exceeds the length of the iterated-totient chain of $M$: each level reduces the modulus to its totient, and the chain of $10^15$ (numbers of the form $2^a 5^b$) reaches $1$ in about $45$ steps. Evaluating the stabilised tower with the rule $2^e equiv 2^(e mod phi(M) + phi(M)) (mod M)$, valid since every remaining exponent dwarfs $log_2 M$, gives the answer.

#pagebreak()
#link("https://projecteuler.net/problem=810")[= Problem 810: XOR-Primes]

Solution: 124136381

The XOR-product is carry-less binary multiplication: long multiplication in base $2$ with the partial results combined by XOR rather than addition. This is exactly multiplication of polynomials over $"GF"(2)$, identifying an integer with the polynomial whose coefficients are its binary digits. An XOR-prime, an integer $> 1$ that is not an XOR-product of two integers $> 1$, is therefore an irreducible polynomial over $"GF"(2)$ of degree $>= 1$, read back as an integer. The first few are $2, 3, 7, 11, 13, dots$ (that is $X, X + 1, X^2 + X + 1, X^3 + X + 1, X^3 + X^2 + 1$), with $41$ the tenth.

A polynomial of degree $d$ has integer value in $[2^d, 2^(d+1))$, so ordering the XOR-primes by value is the same as ordering by degree and then by value within a degree. The number of monic irreducibles of degree $d$ over $"GF"(2)$ is $L(d) = 1/d sum_(e divides d) mu(e) 2^(d\/e)$. Accumulating $L(d)$, the running total first passes $5 dot 10^6$ at degree $26$ (the $5{,}000{,}000$th lies $2{,}192{,}804$ entries into degree $26$, value in $[2^26, 2^27)$), so sieving up to $N = 2^27$ captures it.

== Computation

A carry-less sieve marks every XOR-composite below $N$. Any composite of degree $<= 26$ has a factor of degree $<= 13$, so it suffices to run $p$ over the still-unmarked values (the XOR-primes) with $deg p <= 13$, and for each mark $p times.circle q$ for every $q >= 2$ with $deg p + deg q <= 26$. The carry-less product uses the shift-and-XOR loop $r arrow.l r xor a$ while shifting $a$ left and $b$ right. The unmarked values $>= 2$, taken in increasing order, are the XOR-primes; the $5{,}000{,}000$th is $124136381$. The sieve runs in a few seconds.

#pagebreak()
#link("https://projecteuler.net/problem=811")[= Problem 811: Bitwise Recursion]

Solution: 327287526

With $b(n)$ the largest power of two dividing $n$, the recursion is $A(0) = 1$, $A(2n) = 3A(n) + 5A(2n - b(n))$ and $A(2n+1) = A(n)$; we need $A((2^t + 1)^62) mod 1\,000\,062\,031$ for $t = 10^14 + 31$.

== A product over the set bits

Write $x = y dot 2^j$ with $y$ odd and set $f_j (y) = A(y dot 2^j)$. The even rule becomes $f_j (y) = 3 f_(j-1)(y) + 5 f_(j-1)(2y - 1)$, and unrolling it (the doubling map sends $y arrow.bar 2^a (y - 1) + 1$, whose trailing $1$ the odd rule strips) gives, for $y = u dot 2^m + 1$,
$
f_j (y) = sum_(a=0)^(j) binom(j, a) 3^(j-a) 5^a f_(m+a-1)(u),
$
a binomial transform of the deeper level. Such transforms map geometric sequences to geometric sequences: if $f_k (u) = c thin alpha^k$ then $f_j (y) = c thin alpha^(m-1) (3 + 5 alpha)^j$. The most significant bit starts the chain as the single term $f_k (1) = 8^k$, so the term count never grows: with $1$-bits at positions $p_1 > p_2 > dots > p_s$ and $alpha_1 = 8$, $alpha_(i+1) = 3 + 5 alpha_i$,
$
A(x) = alpha_1^(p_1 - p_2 - 1) alpha_2^(p_2 - p_3 - 1) dots.c alpha_(s-1)^(p_(s-1) - p_s - 1) dot alpha_s^(p_s),
$
verified against the raw recursion for all $x < 3000$ and random $40$-bit values; $A(81) = 8 dot 43^3 = 636056$ confirms the given value.

== Assembling the power

$(2^t + 1)^62 = sum_k binom(62, k) 2^(t k)$, and every binomial coefficient fits comfortably inside its $t$-bit block, so the set bits of the power are just the set bits of each $binom(62, k)$ shifted by $t k$. About $1500$ bit positions, the $alpha$ chain modulo $1\,000\,062\,031$, and fast modular powers for the astronomically wide gaps finish the job.

#pagebreak()
#link("https://projecteuler.net/problem=812")[= Problem 812: Dynamical Polynomials]

Solution: 986262698

$S(n)$ counts monic integer polynomials $f$ of degree $n$ with $f(x) | f(x^2 - 2)$; we need $S(10\,000) mod 998244353$.

== Which roots can occur

A root $alpha$ of $f$ forces $alpha^2 - 2$ to be a root too, so every root has a finite forward orbit under $phi: x arrow.bar x^2 - 2$. Conjugating by $x = z + 1\/z$ turns $phi$ into $z arrow.bar z^2$, whose preperiodic points are the roots of unity; hence every root is $2 cos(2 pi k \/ m)$, and $f$ is a product of the minimal polynomials $psi_m$ of $2 cos(2 pi \/ m)$ — the real cyclotomic polynomials, of degree $d_m = phi.alt(m)\/2$ for $m >= 3$ and degree $1$ for $m in {1, 2}$.

== Multiplicity constraints

Angle doubling sends root class $m$ to $m$ for odd $m$ (a bijection on primitive residues) and to $m\/2$ for even $m$. Comparing multiplicities of each root of $f(x^2-2)$ with those of $f$ shows the exponent $e_m$ of $psi_m$ must satisfy $e_(2m') <= e_(m')$ along every doubling chain $m, 2m, 4m, dots$ ($m$ odd) — except $e_4 <= 2 e_2$, because the fibre of $-2$ is the double root $0$. Odd classes sit in cycles and are unconstrained. The six degree-$2$ products this allows are exactly the six given examples.

== Generating function

A weakly decreasing chain with degree prefix sums $D_j$ contributes $product_j (1 - q^(D_j))^(-1)$ (write the exponents as differences); for odd $m >= 3$ the prefix sums are $d, 2d, 4d, dots$ with $d = phi.alt(m)\/2$, taken over all odd $m$ with $d <= n$. For the $m = 1$ chain (degrees $1, 1, 1, 2, 4, dots$ for $psi_1, psi_2, psi_4, psi_8, dots$), summing out $e_1 >= e_2 >= ceil(e_4 \/ 2)$ leaves a decreasing tail from $C = e_4$ weighted by $q^(2 ceil(C\/2) + C)$; expressing $C$ through tail differences with weights $2^(j+1)$ and splitting on the parity of $C$ gives the closed form
$
P_1 = ((1+q) product_j (1 - q^(2^(j+1)))^(-1) + (1-q) product_j (1 + q^(2^(j+1)))^(-1)) / (2 (1-q)(1-q^2)).
$
$S(n)$ is the $q^n$ coefficient of $P_1$ times the product over odd chains; all factors are sparse, so the series arithmetic is linear per factor. The model reproduces $S(2) = 6$, $S(5) = 58$ and $S(20) = 122087$. One trap: odd $m$ up to nearly $5n$ can still have $phi.alt(m)\/2 <= n$, so the totient sieve must run well past $n$.

#pagebreak()
#link("https://projecteuler.net/problem=813")[= Problem 813: XOR-Powers]

Solution: 14063639

The XOR-product is exactly multiplication in $bb(F)_2 [x]$, with $11 = 1011_2$ playing the role of $x^3 + x + 1$; we need the integer encoding of $(x^3 + x + 1)^(8^12 dot 12^8)$ modulo $10^9 + 7$.

Factor the exponent: $8^12 dot 12^8 = 2^52 dot 3^8$. Over $bb(F)_2$, squaring is the Frobenius substitution $f(x) arrow.bar f(x^2)$, so the huge power of two costs nothing: $f^(2^52 dot 3^8) = g(x^(2^52))$ where $g = f^(3^8)$. Computing $g$ exactly takes a dozen carry-less square-and-multiply steps on bitmask polynomials of degree at most $3 dot 3^8 approx 2 dot 10^4$. Substituting $x arrow.bar x^(2^52)$ sends each monomial $x^k$ of $g$ to the bit $2^(k dot 2^52)$ of the answer, so the result is $sum_k 2^(k dot 2^52) mod (10^9 + 7)$ over the set monomials, with exponents reduced via Fermat's little theorem.

#pagebreak()
#link("https://projecteuler.net/problem=814")[= Problem 814: Mezzo-forte]

Solution: 307159326

$4n$ people in a circle each look left, right, or diametrically opposite; a person screams iff their gaze is reciprocated. $S(n)$ counts the configurations in which exactly $2n$ people scream; we need $S(10^3) mod 998244353$.

== A twisted cycle of pairs

Pair person $i$ with the opposite person $i + 2n$, giving $2n$ sites of two people (top and bottom) arranged in a cycle. Consecutive sites are joined top–top and bottom–bottom along the two semicircles, and the wrap-around joins top to bottom, since position $2n - 1$ neighbours position $2n$. Screams are local: an R–L match across a joint makes both ends scream, and a site whose two members both choose O makes both scream.

== Transfer matrix and coefficient extraction

A $9$-state transfer matrix over the (top, bottom) choices of a site, with $x^2$ marking each R–L match on either rail and each O–O site, makes $S(n)$ the $x^(2n)$ coefficient of the _swap-twisted_ trace of $M(x)^(2n)$ — the swap implementing the half-turn of the wrap-around. The trace is a polynomial of degree $4n$; since $998244353$ has $2^23$-th roots of unity, evaluating the twisted trace at the $4096$-th roots (batched $9 times 9$ modular matrix powers) and inverting the discrete Fourier transform at the single needed coefficient finishes in well under a second. The exact small-$n$ polynomial agrees with brute force ($S(1) = 48$, $S(2) = 2256$) and with the given $S(10)$.

#pagebreak()
#link("https://projecteuler.net/problem=815")[= Problem 815: Group by Value]

Solution: 54.12691621

A shuffled pack of $4n$ cards (four of each value) is dealt into piles by value, each pile vanishing at four cards; $E(n)$ is the expected maximum number of simultaneously open piles. We need $E(60)$ to eight decimals.

The shuffle only matters through the profile $(a_1, a_2, a_3, a_4)$ — how many values have that many cards dealt — since the next card belongs to a value with $j$ cards seen with probability $(4 - j) a_j \/ R$, with $R$ cards remaining. Open piles number $a_1 + a_2 + a_3$, and only the new-pile move $a_0 arrow a_1$ can increase the count.

Using $E[max] = sum_(m >= 1) Pr[max >= m] = n - sum_(m < n) Pr[max <= m]$, each survival probability $Pr[max <= m]$ comes from a forward dynamic program over profiles ordered by cards dealt $t = a_1 + 2a_2 + 3a_3 + 4a_4$, simply withholding probability from the one capped transition. About $6 dot 10^5$ states per threshold and $60$ thresholds run in seconds; $E(2) = 1.97142857$ checks out.

#pagebreak()
#link("https://projecteuler.net/problem=816")[= Problem 816: Shortest Distance Among Points]

Solution: 20.880613018

Points $P_n = (s_(2n), s_(2n+1))$ are generated by the Blum–Blum–Shub-style recurrence $s_0 = 290797$, $s_(n+1) = s_n^2 mod 50515093$; we need the closest-pair distance among $P_0, dots, P_(2 dot 10^6 - 1)$ to nine decimals.

With two million points in a $5 dot 10^7$ square the typical nearest-neighbour gap is on the order of tens, so a uniform grid with cells far larger than that gap puts only a few points per cell. Bucketing the points by cell (a counting sort into a flat array) and, for each point, scanning only the $3 times 3$ block of neighbouring cells finds the true closest pair: any pair closer than the answer lies within one cell of each other, and the cell side comfortably exceeds the minimal distance. All arithmetic is in exact 64-bit integers (squared distances), with a single high-precision square root at the end; $d(14) = 546446.466846479$ confirms the generator and metric.

#pagebreak()
#link("https://projecteuler.net/problem=817")[= Problem 817: Digits in Squares]

Solution: 93158936107011

$M(n, d)$ is the least $m$ whose square, written in base $n$, contains the digit $d$; we need $sum_(d=1)^(10^5) M(p, p - d)$ for $p = 10^9 + 7$, i.e. the highest $10^5$ digits.

For a digit $p - k$ the candidates, in increasing order of size, are:

- *Last digit.* $m^2 equiv -k (mod p)$. Since $p equiv 3 (mod 4)$, residue-ness and the square root come from one exponentiation $(-k)^((p+1)\/4)$; when $-k$ is a quadratic residue the minimal root (at most $p\/2$) beats everything below, and this also covers one-digit squares.
- *Leading digit of a two-digit square.* $m^2 in [(p-k)p, (p-k+1)p)$, an interval of length $p$; with square gaps near $2p$ it only sometimes contains a square, and then $m approx p - k\/2$.
- *Middle digit of a three-digit square.* Writing $m = q p + r$, the middle base-$p$ digit of $m^2$ is $(2 q r + floor(r^2\/p)) mod p$. For each $q = 1, 2, dots$ the equation $2 q r + r^2\/p = (p-k) + j p$ has one real root per branch $j$, and an integer solution sits within a few units of it whenever one exists, so scanning a tiny window per branch finds the minimal $r$; small $q$ always suffices. The top digit stays tiny and the bottom digit is excluded by non-residuosity, so nothing else can fire first.

The case analysis was validated against a digit-scanning brute force in base $10007$, and $M(11, 10) = 19$ reproduces the given example.

#pagebreak()
#link("https://projecteuler.net/problem=818")[= Problem 818: SET]

Solution: 11871909492066000

The $81$ SET cards are the points of the affine space $bb(F)_3^4$, and a SET (three cards, each feature all-same or all-different) is exactly an affine line $\{a, b, c\}$ with $a + b + c = 0$; there are $1080$ of them. With $S(C)$ the number of SETs inside a collection $C$, we need $F(12) = sum_(|C| = 12) S(C)^4$.

== Swapping the order of summation

Expanding $S(C)^4 = (sum_("SET" L subset.eq C) 1)^4$ as a sum over _ordered_ $4$-tuples of SETs contained in $C$, and summing over $C$ first, gives
$
F(n) = sum_("ordered" (L_1, L_2, L_3, L_4)) \#{|C| = n : L_1 union dots.c union L_4 subset.eq C} = sum_("tuples") binom(81 - u, n - u),
$
where $u$ is the number of distinct points (cards) in $L_1 union dots.c union L_4$. So $F(n)$ needs only the multiset of union sizes over ordered $4$-tuples of lines.

== Histogram by number of distinct lines

Group the ordered tuples by their set of $k$ distinct lines. The number of ordered $4$-tuples drawing on exactly $k$ given lines is the surjection count $k! thin S(4, k)$, i.e. $1, 14, 36, 24$ for $k = 1, 2, 3, 4$. The union size $u$ depends only on the configuration of those $k$ lines, and since any two distinct SETs meet in at most one point, unions range over $u in {3, dots, 12}$. Tabulating, for each $k$, how many $k$-subsets of the $1080$ lines have each union size — by direct enumeration with $81$-bit point masks (the $k = 4$ pass is the $binom(1080, 4)$ bottleneck, run once) — and combining with the surjection weights and $binom(81 - u, n - u)$ yields $F(n)$. The checks $F(3) = 1080$ and $F(6) = 159690960$ both hold.

#pagebreak()
#link("https://projecteuler.net/problem=819")[= Problem 819: Iterative Sampling]

Solution: 1995.975556

From an $n$-tuple, each entry of the next tuple is an independent uniform pick from the current entries; $E(n)$ is the expected number of steps from $(1, 2, dots, n)$ until all entries are equal. We need $E(10^3)$ to six decimals.

== The coalescent dual

Reading the process backwards, each new entry "descends" from the position it copied. So the current number of _distinct_ values, $b$, maps in one backward step to the number of distinct parents chosen — which is exactly the number of occupied boxes when $b$ balls are thrown uniformly into $n$ boxes. Reaching consensus forward is the coalescence of all lineages to one backward, and the two processes share the same step distribution, so $E(n)$ equals the expected number of backward steps from $n$ lineages down to $1$.

== An $O(n^2)$ recurrence

Let $q_(b,j)$ be the probability that $b$ balls occupy exactly $j$ of the $n$ boxes; it follows the triangular recurrence $q_(b+1,j) = q_(b,j) dot j\/n + q_(b,j-1) dot (n-j+1)\/n$. Removing the self-loop where no two lineages coalesce ($j = b$),
$
T(1) = 0, quad T(b) = (1 + sum_(j=1)^(b-1) q_(b,j) T(j)) / (1 - q_(b,b)).
$
Building the $q$ table and the $T$ values is $O(n^2)$; the all-distinct probability $q_(b,b)$ stays small away from $b = n$, so floating point delivers six correct digits in under a second. The values $E(3) = 27\/7$ and $E(5) = 468125\/60701 approx 7.711982$ check out exactly.

#pagebreak()
#link("https://projecteuler.net/problem=820")[= Problem 820: $N$th Digit of Reciprocals]

Solution: 44967734

Let $d_n(x)$ be the $n$th decimal digit of the fractional part of $x$. We need $S(n) = sum_(k=1)^n d_n(1\/k)$ for $n = 10^7$.

The $n$th fractional digit of $1\/k$ is $floor(10^n \/ k) mod 10$. Reducing the numerator modulo $10k$ recovers it directly: since $10^n = q dot 10k + r$ with $0 <= r < 10k$, and $r = (floor(10^n\/k) mod 10) dot k + (10^n mod k)$, we get
$
d_n(1\/k) = floor((10^n mod 10k) \/ k).
$
So each term is a single modular exponentiation $10^n mod 10k$. For $n = 10^7$ every modulus $10k <= 1.1 dot 10^8$, so all intermediate products in binary exponentiation stay below $2^63$ and 64-bit arithmetic suffices — no big integers. Summing over $k$ in an $O(n log n)$ sweep gives the answer; $S(7) = 10$ and $S(100) = 418$ confirm the digit formula.

#pagebreak()
#link("https://projecteuler.net/problem=821")[= Problem 821: 123-Separable]

Solution: 9219661511328178

A set $S$ is 123-separable if $S$, $2S$, $3S$ are pairwise disjoint, and $F(n)$ is the largest possible $|(S union 2S union 3S) inter {1, dots, n}|$. We need $F(10^16)$.

== Decomposition by residue class

Every positive integer is uniquely $m dot 2^a 3^b$ with $gcd(m, 6) = 1$, and multiplying by $2$ or $3$ keeps $m$ fixed. So the construction splits independently over each class $m$ coprime to $6$. Within a class the reachable integers form a staircase grid of cells $(a, b)$ with $m dot 2^a 3^b <= n$. The disjointness conditions forbid putting in $S$ any two cells differing by $(1, 0)$ (from $S inter 2S$), $(0, 1)$ (from $S inter 3S$), or $(1, -1)$ (from $2S inter 3S$); the count rewards cells covered by $S$ or its $(+1, 0)$ / $(0, +1)$ shifts.

== Loss is a step function

Maximizing coverage leaves some cells uncovered; this "loss" depends only on the grid shape, hence only on $t = n\/m$ through which $3$-smooth numbers are $<= t$. Solving the per-grid optimum exactly for small grids shows the loss increments by one precisely at a sparse set of $3$-smooth thresholds, in two interleaved families: $2^a dot 3$ for $a in {1, 3, 7, 10, 13, dots}$ and $2 dot 3^3 = 54$ together with $3^b$ for $b in {5, 8, 11, dots}$. Thus $"loss"(t) = \#{theta <= t}$.

Because every integer in $[1, n]$ is exactly one cell, the grids hold $n$ cells in total, so
$
F(n) = n - sum_(m "coprime" 6) "loss"(n\/m) = n - sum_theta \#{m "coprime" 6 : m <= n\/theta},
$
swapping summation order; each inner count is $floor(n\/theta) - floor(n\/(2theta)) - floor(n\/(3theta)) + floor(n\/(6theta))$. With only a few dozen thresholds below $10^16$ this is instant, and it reproduces the exact per-grid optimum for every $n <= 5000$ ($F(6) = 5$, $F(20) = 19$).

#pagebreak()
#link("https://projecteuler.net/problem=822")[= Problem 822: Square the Smallest]

Solution: 950591530

Starting from $[2, 3, dots, n]$, each round replaces one smallest entry by its square; $S(n, m)$ is the sum after $m$ rounds. We need $S(10^4, 10^16) mod 1234567891$.

== Tracking exponents

Squaring never changes the base an entry came from, only how often it has been squared, so the entry seeded by $k$ always equals $k^(2^(e_k))$ for a level $e_k$. Each round increments the $e$ of the entry of smallest current value; comparing $2^(e_a) log k_a$ versus $2^(e_b) log k_b$ is done exactly as the integer test $k_a <^? k_b^(2^d)$ by repeated squaring (level gaps in play are tiny).

== Steady cycle

After a short warm-up the values become balanced enough that every block of $n - 1$ consecutive rounds squares each of the $n - 1$ entries exactly once — detected once two successive $(n-1)$-windows of squared bases are each a full permutation. The remaining $r$ rounds then split into $floor(r\/(n-1))$ full blocks, which add that constant to every level, plus $r mod (n-1)$ extra rounds following the observed steady order. Finally $S = sum_k k^(2^(e_k))$ with each exponent reduced modulo $1234567891 - 1$ (the modulus is prime). The method matches an exact heap simulation for all $n < 30$ and $m$ up to $10^5$, and reproduces $S(5, 3) = 34$ and $S(10, 100)$.

#pagebreak()
#link("https://projecteuler.net/problem=824")[= Problem 824: Chess Sliders]

Solution: 26532152736197

A Slider attacks the two squares horizontally adjacent to it on a cylindrical $N times N$ board (each row is a cycle $C_N$). $L(N, K)$ counts placements of $K$ non-attacking Sliders, and we need $L(10^9, 10^15) mod (10^7 + 19)^2$.

== Rows are independent

Since a Slider only attacks within its own row, the rows are independent and
$
L(N, K) = [x^K] thin g(x)^N, quad g(x) = I(C_N, x) = "tr" mat(1, x; 1, 0)^N = lambda_+^N + lambda_-^N,
$
the independence polynomial of the cycle, with $lambda_(plus.minus) = (1 plus.minus sqrt(1 + 4x))\/2$. This reproduces $L(2,2) = 4$ and $L(6,12) = 4204761$.

== A Lucas expansion

Expanding $g^N = sum_i binom(N, i) lambda_+^(N i) lambda_-^(N(N-i))$ and pairing $i$ with $N - i$ (using $lambda_+ lambda_- = -x$) gives, with $V_m = lambda_+^m + lambda_-^m$ the Lucas-type polynomial ($V_0 = 2$, $V_1 = 1$, $V_m = V_(m-1) + x V_(m-2)$),
$
g(x)^N = sum_(i < N\/2) binom(N, i) (-x)^(N i) V_(N(N - 2i))(x) quad (+ "middle term if " N "even"),
$
so $L(N, K) = sum_i binom(N, i) (-1)^(N i) thin [x^(K - N i)] V_(N(N-2i))$, with $[x^s] V_m = (m\/(m-s)) binom(m-s, s)$ for $m, s >= 1$ and $V_m (0) = 1$. Verified against a direct polynomial expansion for all $N <= 10$.

== Modulo a square of a prime

Only $i$ with $N i <= K$ contribute, here $i <= K\/N = 10^6$. Each binomial and Lucas coefficient — with arguments as large as $approx 10^18$ — is reduced modulo $(10^7 + 19)^2$ by Granville's prime-power generalisation of Lucas' theorem: factorials with their $P$-parts stripped are products of per-block factorials (every full block $equiv (P-1)!$ by Wolstenholme), and the $P$-adic valuations are tracked separately. A single $O(P)$ table build plus $10^6$ constant-work terms finishes in well under a minute.

#pagebreak()
#link("https://projecteuler.net/problem=825")[= Problem 825: Chasing Game]

Solution: 32.34481054

Two cars on a length-$2n$ circular track start $n$ apart and alternately advance $1$, $2$ or $3$ uniformly; whoever first reaches or passes the other wins. $S(n)$ is the difference of the two win probabilities, and we need $T(10^14) = sum_(n=2)^(10^14) S(n)$.

== Win-probability recurrence

Track the gap $d$ the mover must cover. It wins outright if its step reaches $d$; otherwise the opponent moves with gap $2n - (d - "step")$. So $W(d) = 1 - (1\/3) sum_(k < d, thin k <= 3) W(2n - d + k)$. Solving this finite linear system, $S(n) = |2 W(n) - 1| = "num"(n)\/"den"(n)$, where (fitted to and verified against exact small values) the numerator obeys a recurrence with roots ${-1, 2 plus.minus sqrt(3)}$ and the denominator the *double* roots $(2 plus.minus sqrt(3))^2$:
$
"num"(n) &= (3 - sqrt(3))/2 (2+sqrt(3))^n + (3 + sqrt(3))/2 (2-sqrt(3))^n - 2(-1)^n, \
"den"(n) &= ((3 - sqrt(3))/2 n - 1/2)(2+sqrt(3))^n + ((3 + sqrt(3))/2 n - 1/2)(2-sqrt(3))^n.
$

== Exact tail

The $(2 - sqrt(3))^n$ terms vanish geometrically and the leading coefficient $(3-sqrt(3))\/2$ is common to numerator and denominator, so beyond a tiny cutoff
$
S(n) = 1/(n + b\/a), quad b\/a = -(3 + sqrt(3))/6,
$
exact far past double precision. Summing the first $200$ terms directly and the rest as $psi(N + 1 + b\/a) - psi(201 + b\/a)$ gives $T$ instantly; $T(10) = 2.38235282$ checks.

#pagebreak()
#link("https://projecteuler.net/problem=826")[= Problem 826: Birds on a Wire]

Solution: 0.3889014797

$n$ birds land uniformly on a unit wire; each paints the segment to its nearest neighbour. $F(n)$ is the expected painted length, and we need the average of $F(p)$ over odd primes $p < 10^6$.

== Spacings

Ordering the birds splits the wire into $n+1$ spacings — two to the posts and $n-1$ between consecutive birds — jointly a symmetric Dirichlet$(1, dots, 1)$, so each has mean $1\/(n+1)$. Only the $n-1$ internal gaps can be painted, since the posts are not birds.

== Per-gap contributions

The two outer internal gaps are always painted: the leftmost bird's only neighbour lies to its right and the rightmost bird's only neighbour to its left, so each contributes its full mean $1\/(n+1)$. An interior gap $g$, with internal neighbours of lengths $x$ and $z$, fails to be painted only when it is the largest of the three (neither adjacent bird prefers it). Writing $W = x+g+z tilde "Beta"(3, n-2)$ independent of the normalised triple (uniform on the $2$-simplex),
$
E[g dot bb(1)(g "maximal")] = E[W] dot (E["max of three simplex parts"])/3 = 3/(n+1) dot (11\/18)/3 = 11/(18(n+1)),
$
using $E["max"] = 11\/18$. So each interior gap contributes $1\/(n+1) - 11\/(18(n+1)) = 7\/(18(n+1))$.

== Closed form

Summing the two outer gaps and the $n-3$ interior gaps,
$
F(n) = 2/(n+1) + (n-3) dot 7/(18(n+1)) = (7n + 15)/(18(n+1)),
$
which gives $F(3) = 1\/2$ and matches Monte-Carlo values through $n = 7$. Averaging this exact rational over the $78498$ odd primes below $10^6$ and rounding gives the answer.

#pagebreak()
#link("https://projecteuler.net/problem=827")[= Problem 827: Pythagorean Triple Occurrence]

Solution: 397289979

$Q(n)$ is the smallest number occurring in exactly $n$ Pythagorean triples $(a < b < c)$; we need $sum_(k=1)^18 Q(10^k) mod 409120391$.

== How many triples contain $N$

A number $N$ can appear as a leg or as the hypotenuse. As a leg, $N^2 = (c-b)(c+b)$, so each factorisation $N^2 = d e$ with $d < e$ of equal parity gives one triple; as the hypotenuse, the count is governed by sums of two squares. Writing $N = 2^s product p^a$ and grouping the odd primes by residue mod $4$ into $M_1 = product_(p eq.triple 1) (2a+1)$ and $M_3 = product_(p eq.triple 3) (2a+1)$ (so $M = M_1 M_3$ is $tau$ of the odd part of $N^2$),
$
"legs" = cases((M-1)\/2 & s = 0, ((2s-1)M - 1)\/2 & s >= 1), quad "hyps" = (M_1 - 1)\/2.
$
Thus $"count"(N) = n$ becomes $M_1 ((2s-1) M_3 + 1) = 2n + 2$ for $s >= 1$ and $M_1 (M_3 + 1) = 2n+2$ for $s = 0$ — checked exhaustively against brute force for $N < 3000$.

== Minimising $N$

Let $T = 2n + 2$. Choose $M_1$ among the odd divisors of $T$; the cofactor $G = T\/M_1$ must equal $(2s-1) M_3 + 1$, so $(2s-1) M_3 = G - 1$ splits over the odd divisors of $G - 1$ (with the $s = 0$ and empty-$M_3$ cases handled separately). Each $(2a+1)$-factor of $M_1$ (resp. $M_3$) becomes an exponent $a$ on a prime $eq.triple 1$ (resp. $eq.triple 3$) mod $4$; to minimise $N$ the largest exponents sit on the smallest such primes, the factor $2^s$ is free, and candidates are compared by real size via logarithms while the answer is tracked modulo the (prime) modulus. Factoring $T = 2(10^k + 1)$ and each $G - 1$ with a real factoriser keeps every $Q(10^k)$ near-instant; $Q(5) = 15$, $Q(10) = 48$, $Q(10^3) = 8064000$ all check.

#pagebreak()
#link("https://projecteuler.net/problem=829")[= Problem 829: Integral Fusion]

Solution: 41768797657018024

The binary factor tree $T(n)$ is a leaf when $n$ is prime, otherwise it splits $n = a b$ with $a <= b$ and $b - a$ minimal and recurses. $M(n)$ is the smallest integer whose factor tree has the same shape as $T(n!!)$, and we need $sum_(n=2)^31 M(n)$.

== Shape of $n!!$

Each node's split is the closest-factor split, so the tree shape is intrinsic to the number. The double factorial $n!!$ is large (up to $approx 2 dot 10^17$), but its closest split is found from its prime factorisation: enumerate the divisors and take the largest one not exceeding $sqrt(n!!)$. Recursing on the two factors (themselves split via their factorisations) yields the ordered tree shape of $n!!$.

== Smallest integer of a given shape

The shape comparison is ordered (left subtree from the smaller factor), as the example $M(9) = 72$ confirms. To realise a shape minimally, a leaf is any prime and an internal node is a product $v = a b$ of realisations of its two child shapes whose own closest split is exactly $(a, b)$ — so each candidate product is re-checked against the shape (multiplying two realisations need not split back the same way). Computing, for every subshape, a pool of its smallest realisations bottom-up and combining them gives $M(n)$ as the least realisation of the root shape; the pool stays small for every shape arising from $n!!$ with $n <= 31$.

#pagebreak()
#link("https://projecteuler.net/problem=836")[= Problem 836: A Bold Proposition]

Solution: aprilfoolsjoke

An April Fools' problem; the answer is the literal string hidden in the prompt.

#pagebreak()
#link("https://projecteuler.net/problem=850")[= Problem 850: Fractions of Powers]

Solution: 878255725

For odd $k$ the residues $i^k$ and $(n-i)^k$ are negatives of each other modulo $n$, so pairing $i$ with $n - i$ makes each pair of fractional parts sum to $1$ unless $n divides i^k$ (the self-paired $i = n\/2$, whose fractional part is $0$ or $1\/2$, falls out of the same bookkeeping). Hence
$
f_k(n) = (n - c_k(n)) / 2, quad c_k(n) = \#{1 <= i <= n : n divides i^k},
$
and $c_k$ is multiplicative with $c_k(p^e) = p^(e - ceil(e\/k))$.

Splitting $n = P s$ into its powerful part $P$ and coprime squarefree part $s$ gives $c_k(n) = c_k(P)$, so
$
sum_(n <= N) c_k(n) = sum_(P "powerful" <= N) c_k(P) thin Q(N\/P; "rad"(P)),
$
where $Q(y; r)$ counts squarefree numbers up to $y$ coprime to $r$, computed by Möbius summation with inclusion–exclusion over the few primes of $r$:
$Q(y; r) = sum_(d | r) mu(d) sum_(j <= sqrt(y\/d), gcd(j, r) = 1) mu(j) floor(y / (d j^2))$.

Summing over odd $k <= N$ collapses per powerful number: since $2^45 > N$, no exponent exceeds $44$, so $c_k(P) = P\/"rad"(P)$ for every $k >= 45$ and only odd $k <= 43$ need individual corrections — and only on the rare $P$ containing a prime power $p^e$ with $e >= 4$. A depth-first enumeration of the $approx 1.3 dot 10^7$ powerful numbers up to $N = 33557799775533$, each with one $Q$ evaluation, costs about $sqrt(N) log N$ operations in total. Working modulo $2 dot 977676779$ keeps the parity of the doubled sum, so the final halving and floor are exact.

#pagebreak()
#link("https://projecteuler.net/problem=853")[= Problem 853: Pisano Periods 1]

Solution: 44511058204

The Pisano period is determined prime-power-wise: $pi(n) = "lcm"_(p^e || n) pi(p^e)$, so every prime power dividing an $n$ with $pi(n) = 120$ must itself have $pi(p^e) | 120$. The divisibility $pi(m) | t$ holds exactly when $F_t equiv 0$ and $F_(t+1) equiv 1 (mod m)$ (the Fibonacci matrix has order dividing $t$), so the candidate primes are precisely the prime factors of $gcd(F_120, F_121 - 1)$ — a small number factored by trial division.

For each candidate prime, raise it to successive powers below $10^9$ and read off $pi(p^e)$ as the smallest divisor $d$ of $120$ with $F_d equiv 0$, $F_(d+1) equiv 1 (mod p^e)$ (fast doubling), stopping once the period no longer divides $120$, since it only grows with $e$. A depth-first search over products of these prime powers, tracking the lcm of their periods, sums every $n < 10^9$ whose lcm is exactly $120$. The construction reproduces the given sum $57$ for $pi(n) = 18$, $n < 50$, and was cross-checked against a brute-force period scan below $30000$.

#pagebreak()
#link("https://projecteuler.net/problem=854")[= Problem 854: Pisano Periods 2]

Solution: 29894398

The largest $n$ with $pi(n) | p$ is exactly $N(p) = gcd(F_p, F_(p+1) - 1)$: the condition $n | F_p$, $n | F_(p+1) - 1$ says the Fibonacci matrix has order dividing $p$ modulo $n$. Computing this gcd for all $p < 1000$ reveals (and Fibonacci–Lucas halving identities confirm) the closed form
$
N(4k) = F_(2k), quad N(4k + 2) = L_(2k + 1), quad N(p "odd") = cases(2 quad &3 | p, 1 quad &"otherwise").
$

Since $N(d) | N(p)$ whenever $d | p$, the maximiser fails to have period exactly $p$ — forcing $M(p) = 1$ — only when $N(p) = N(p \/ ell)$ for some prime $ell | p$. The strict growth of $F$ and $L$ rules this out for every even $p >= 6$, leaving the degenerate $M(1) = M(2) = M(4) = 1$, $M(3) = 2$ ($pi(2) = 3$), and $M(p) = 1$ for odd $p >= 5$ (Pisano periods are even for $n >= 3$). All of this matches a brute-force table of $M(p)$ for $p <= 40$. Therefore
$
P(10^6) = 2 dot product_(k = 2)^(250000) F_(2k) dot product_(k = 1)^(249999) L_(2k + 1) quad (mod 1234567891),
$
a single linear pass over Fibonacci and Lucas numbers modulo $1234567891$.

#pagebreak()
#link("https://projecteuler.net/problem=856")[= Problem 856: Waiting for a Pair]

Solution: 17.09661501

Cards are drawn from a shuffled standard deck until two consecutive draws share a rank (or the deck runs out, counting all $52$ draws); we want the expected number of cards drawn.

By symmetry between ranks, the only relevant state after each draw is $(c_1, c_2, c_3, c_4, j)$, where $c_i$ counts the ranks with exactly $i$ cards still in the deck and $j$ is how many cards of the _last drawn_ rank remain (that rank is included in class $c_j$). Let $E(c_1, c_2, c_3, c_4, j)$ be the expected number of further draws. With $r = c_1 + 2 c_2 + 3 c_3 + 4 c_4$ cards remaining, the next draw always happens; with probability $j \/ r$ it matches the last rank and the process stops, and otherwise a card from some class $i$ (of which $i dot c_i$ are available, minus the $j$ reserved cards when $i = j$) is drawn, moving its rank from class $i$ to class $i - 1$ and becoming the new last rank with $j' = i - 1$:
$
E = 1 + sum_(i = 1)^4 (i dot c_i - j dot [i = j]) / r dot E(..., c_i - 1, c_(i - 1) + 1, ..., i - 1).
$
The base case $r = 0$ contributes $0$: the deck is exhausted and every draw has already been counted. The answer is $1 + E(0, 0, 1, 12, 3)$ — after the first draw, its rank sits in class $3$ and the other twelve ranks in class $4$. The state space is tiny ($c_i <= 13$), so exact rational arithmetic with memoisation finishes instantly. As checks, the probability of a pair within the first two draws is $3 \/ 51 = 1 \/ 17$ as given, and on a toy deck of two ranks of two cards the recursion reproduces the directly enumerated expectation $3$.

#pagebreak()
#link("https://projecteuler.net/problem=858")[= Problem 858: LCM]

Solution: 973077199

$G(N)$ sums $"lcm"(S)$ over all $2^N$ subsets of ${1, dots, N}$ (the empty set counting $1$); we need $G(800) mod 10^9 + 7$.

A prime $p > sqrt(N)$ divides any element at most once, and no element is divisible by two such primes, so the multiples of $p$ are exactly $p m$ for the _smooth_ cofactors $m <= floor(N \/ p) < sqrt(N)$. Every subset's lcm therefore factors as (join of smooth values) $times$ (product of the large primes hit), where the smooth join lives on the modest lattice of admissible values $L = product p_i^(e_i)$ over the nine primes $p_i <= 23$ with $p_i^(e_i) <= 800$ — a grid of $10 dot 7 dot 5 dot 4 dot 3^5 = 340200$ points.

Counting subsets whose smooth join divides $L$, weighted by the large primes used: the smooth numbers contribute $2^(d_0 (L))$ with $d_0$ the number of smooth $n <= N$ dividing $L$, and each large prime class independently contributes $1 + p (2^(e_p (L)) - 1)$ with $e_p$ the number of cofactors $m <= floor(N \/ p)$ dividing $L$ — skip the class, or pick a nonempty divisor subset and pay the factor $p$. The product $B(L)$ of all these is the divisor-sum of the exact weights $W$, recovered by Möbius inversion along each exponent axis of the grid, and
$
G(N) = sum_L L dot W(L).
$
Divisor counts come from scanning the $approx 270$ smooth numbers per grid point, bucketed by the $27$ relevant thresholds $floor(N \/ p)$; the whole computation runs in seconds with numba. The code matches a brute-force enumeration over all subsets for every $N <= 12$ and reproduces the given $G(5) = 528$ and $G(20) = 8463108648960$.

#pagebreak()
#link("https://projecteuler.net/problem=860")[= Problem 860: Gold and Silver Coin Game]

Solution: 958666903

Gary may remove any gold coin together with everything above it, Sally any silver coin likewise; whoever cannot move loses, and an arrangement is fair if the player to move first loses either way. $F(n)$ counts fair ordered arrangements of $n$ stacks of size $2$.

This is a partisan game, and every stack happens to be a surreal _number_: a lone gold coin is ${0 |} = 1$, so reading (bottom, top), $"GG" = {1, 0 |} = 2$ and $"GS" = {0 | 1} = 1 / 2$, with $"SS" = -2$ and $"SG" = -1 \/ 2$ by symmetry. A sum of numbers is a second-player win exactly when it equals zero, so an arrangement is fair iff its values cancel:
$
4 dot \#"GG" + \#"GS" = 4 dot \#"SS" + \#"SG".
$
Weighting a stack of value $v$ by $x^(4 + 2v)$ turns the count into a coefficient,
$
F(n) = [x^(4 n)] (x^8 + x^5 + x^3 + 1)^n,
$
which $n$ vectorised sparse multiplications extract modulo $989898989$ in a few seconds. The solution validates the game theory by exhaustively solving the actual game for all arrangements of up to five stacks, and reproduces the given $F(2) = 4$ and $F(10) = 63594$.

#pagebreak()
#link("https://projecteuler.net/problem=862")[= Problem 862: Larger Digit Permutation]

Solution: 6111397420935766740

$T(n)$ counts the strictly larger integers obtainable by permuting the digits of $n$ (no leading zeros), and $S(k) = sum T(n)$ over all $k$-digit $n$; we need $S(12)$.

Group the $k$-digit numbers by their digit multiset. If a multiset with digit counts $c_0, dots, c_9$ produces $m$ distinct valid numbers, then every unordered pair of those numbers contributes exactly $1$ to the $T$ value of its smaller member, so the whole class contributes $binom(m, 2)$ to $S(k)$ — the individual values never matter. Discounting arrangements that start with a zero,
$
m = k! / (c_0 ! dots c_9 !) - (k - 1)! dot c_0 / (c_0 ! dots c_9 !),
$
and $S(k) = sum binom(m, 2)$ over the $binom(k + 9, 9)$ multisets — only $293930$ of them for $k = 12$, enumerated directly in a fraction of a second. The same code gives the stated $S(3) = 1701$.

#pagebreak()
#link("https://projecteuler.net/problem=866")[= Problem 866: Tidying Up B]

Solution: 492401720

Pieces $1$ to $N$ are placed in uniformly random order; each placement completes a maximal segment of some length $k$ and records the hexagonal number $h(k) = k (2 k - 1)$, and we need the expected product of the recorded values for $N = 100$, modulo $987654319$.

Let $f(m)$ be the sum of the products over all $m!$ pick-up orders of a length-$m$ caterpillar. Condition on the very last piece placed, at position $j$: it always completes the whole caterpillar, contributing $h(m)$, and before it the $j - 1$ pieces on its left and the $m - j$ on its right form two completely independent sub-caterpillars whose placement orders interleave in $binom(m - 1, j - 1)$ ways. Hence
$
f(m) = h(m) sum_(j = 1)^m binom(m - 1, j - 1) f(j - 1) f(m - j), quad f(0) = 1,
$
and the expectation is $f(N) \/ N!$ — an integer, as the problem promises and the code asserts. The $O(N^2)$ recursion in exact arithmetic is instant for $N = 100$; the implementation reproduces the given $E_4 = 994$ and matches a brute-force enumeration over all orders for every $N <= 7$.

#pagebreak()
#link("https://projecteuler.net/problem=868")[= Problem 868: Belfry Maths]

Solution: 3832914911887589

Starting from the letters in alphabetical order, each step swaps the largest letter that can move into a not-yet-seen permutation with a neighbour (preferring the largest letter of all); we need how many swaps reach NOWPICKBELFRYMATHS.

This procedure is precisely the Steinhaus–Johnson–Trotter enumeration of permutations, which the solution confirms by simulating the verbal rules for up to six letters and comparing every position. In SJT order the permutations come in blocks of $k$ that share the relative order of the $k - 1$ smallest letters while the largest letter sweeps across all $k$ positions — leftwards when the rank $r$ of the sub-permutation is even and rightwards when it is odd. Hence, with $p$ the position of the largest letter,
$
"rank" = r dot k + cases(k - 1 - p quad &"if" r "even", p &"if" r "odd")
$
and recursing on the sub-permutation ranks the target word directly. The recursion gives the stated $3$ swaps for CBA and $59$ for BELFRY, and $3832914911887589$ for the $18$-letter target.

#pagebreak()
#link("https://projecteuler.net/problem=869")[= Problem 869: Prime Guessing]

Solution: 14.97696693

A prime is drawn uniformly from the primes up to $N = 10^8$ and a player guesses its binary digits one at a time from the least significant bit, learning after each guess whether it was right and whether the number has ended; $E(N)$ is the expected score under optimal play.

After each round the player knows the true low bits of the prime and that the game is still running, so the reachable information states form a trie: a node is a pair (known suffix of $L$ bits, "more bits remain"), and the primes consistent with it are exactly those whose low $L$ bits match and whose binary length exceeds $L$. The optimal guess at a node is simply the majority value of bit $L$ among the consistent primes, earning $max(c_0, c_1)$ expected points across the class, where $c_b$ counts the consistent primes whose bit $L$ equals $b$. Primes for which that bit was the leading $1$ then leave the game (their length is exactly $L + 1$), and the remainder split into the two child nodes. Hence
$
E(N) = 1 / pi(N) sum_("nodes") max(c_0, c_1).
$
The implementation sieves the $5761455$ primes and walks the trie with an explicit stack, partitioning the prime array in place at each node by bit $L$ while dropping the primes that just ended — about $sum_p log_2 p approx 1.5 dot 10^8$ cheap operations, a couple of seconds with numba. The code reproduces both given values $E(10) = 2$ and $E(30) = 2.9$.

#pagebreak()
#link("https://projecteuler.net/problem=871")[= Problem 871: Drifting Subsets]

Solution: 2848790

A drifting subset for $f : S -> S$ is a subset $A$ with $|A union f(A)| = 2 |A|$, and $D(f)$ is the largest one; we sum $D(f_n)$ for $f_n (x) = x^3 + x + 1 mod n$ over $n = 10^5 + 1, dots, 10^5 + 100$.

The union has size $2 |A|$ exactly when $f$ is injective on $A$ and $f(A)$ avoids $A$, which says the chosen edges $(a, f(a))$ of the functional graph are pairwise vertex-disjoint — so $D(f)$ is simply the maximum matching of the graph $x -> f(x)$. Every component of a functional graph is a cycle with trees hanging off it. Peeling vertices of in-degree zero in topological (leaf-first) order and greedily matching each peeled vertex to its image whenever both are free is optimal on the tree parts; afterwards each cycle contributes $floor(ell \/ 2)$ for every maximal arc of $ell$ consecutive still-unmatched vertices (and $floor(L \/ 2)$ if the whole length-$L$ cycle is untouched, fixed points being useless loops).

This linear-time routine is validated directly against the definition — a brute-force scan over all $2^n$ subsets for two hundred random functions on up to twelve points — and reproduces the given $D(f_5) = 1$ and $D(f_10) = 3$. The hundred functional graphs on $approx 10^5$ vertices then take about a second in total.

#pagebreak()
#link("https://projecteuler.net/problem=872")[= Problem 872: Recursive Tree]

Solution: 2903144925319290239

The tree $T_n$ is built from $T_(n - 1)$ by tracing the path from the root that always follows the largest-numbered child, detaching every node on it, and attaching them all to a new root $n$. We need $f(10^17, 9^17)$, the sum of the node numbers on the path from the root to node $k = 9^17$.

Writing $h(d)$ for the largest power of two not exceeding $d$, the key structural fact is that in $T_n$ the parent of any node $k < n$ is $k + h(n - k)$. This follows by induction: assuming it for $T_(n - 1)$, the largest child of a node $m$ is the largest $k$ with $k + h(n - 1 - k) = m$, which pushes $n - 1 - k$ just below a power of two, so the traced greatest path is exactly $n - 1, n - 2, n - 4, n - 8, dots$. These become the children of the new root, and indeed $k + h(n - k) = n$ precisely when $n - k$ is a power of two; every other node keeps its parent, and $h(n - k) = h(n - 1 - k)$ whenever $n - k$ is not a power of two.

Consequently, walking down from the root $n$ to node $k$ subtracts the binary bits of $d = n - k$ in increasing order, and $f(n, k)$ is just $n$ plus the partial sums along the way — at most $57$ subtractions here. The formula reproduces the given $f(6, 1) = 12$ and $f(10, 3) = 29$, and the solution cross-checks it against explicitly constructed trees for all $n <= 150$ and all $k$.

#pagebreak()
#link("https://projecteuler.net/problem=873")[= Problem 873: Words with Gaps]

Solution: 735131856

$W(p, q, r)$ counts arrangements of $p$ A's, $q$ B's and $r$ C's in which every A and every B are separated by at least two C's; we need $W(10^6, 10^7, 10^8) mod 10^9 + 7$.

Delete the C's: what remains is a binary word, and the constraint only bites at its type changes — wherever an A is adjacent to a B in the reduced word, the corresponding gap of the full word must hold at least two C's. A reduced word with $a$ runs of A and $b$ runs of B requires $|a - b| <= 1$, arises from $binom(p - 1, a - 1) binom(q - 1, b - 1)$ run-length compositions (doubled when $a = b$, since either letter may start), and has $t = a + b - 1$ type changes. Reserving two C's for each change and scattering the remaining $r - 2 t$ freely over all $p + q + 1$ gaps,
$
W(p, q, r) = sum_(|a - b| <= 1) m(a, b) binom(r - 2 t + p + q, p + q).
$
Only $a <= min(p, q) + 1$ matters, so about $3 dot 10^6$ terms arise; the huge binomial slides from $t$ to $t + 1$ by the rational factor $((r - 2t)(r - 2t - 1)) \/ ((r - 2t + p + q)(r - 2t + p + q - 1))$, with all denominators inverted in a single batch pass. The whole computation takes a few seconds and reproduces both given values, $W(2, 2, 4) = 32$ and $W(4, 4, 44) = 13908607644$ — the latter exercising the sliding binomial in earnest.

#pagebreak()
#link("https://projecteuler.net/problem=874")[= Problem 874: Maximal Prime Score]

Solution: 4992775389

With $p(t)$ the $(t + 1)$-th prime, $M(k, n)$ maximises $sum p(a_i)$ over lists of $n$ values $a_i in [0, k)$ whose sum is a multiple of $k$; we need $M(7000, p(7000))$.

The unconstrained optimum sets every entry to $k - 1$, scoring $n dot p(k - 1)$ with sum $n (k - 1)$. Lowering one entry to $k - 1 - d$ forfeits $p(k - 1) - p(k - 1 - d)$ points and shifts the sum by $-d$, so the task is to fix the residue $n (k - 1) mod k$ at minimum total forfeit — a shortest-path problem on the residues modulo $k$, where every node has an edge of weight $p(k - 1) - p(k - 1 - d)$ shifting by $d$, for each $d = 1, dots, k - 1$. A shortest path visits no residue twice, so it changes at most $k - 1 < n$ entries and the reduction is exact. With $k = 7000$ a dense $O(k^2)$ Dijkstra settles all residues in under two seconds, and
$
M(k, n) = n dot p(k - 1) - "dist"(n (k - 1) mod k).
$
The code reproduces the given $M(2, 5) = 14$ and agrees with a brute-force dynamic program on all small cases with $n >= k - 1$.

#pagebreak()
#link("https://projecteuler.net/problem=877")[= Problem 877: XOR-Equation A]

Solution: 336785000760344621

With $xor$ as addition and the XOR-product $times.circle$ as multiplication, bit strings form the polynomial ring $"GF"(2)[x]$, and the equation $(a times.circle a) xor (2 times.circle a times.circle b) xor (b times.circle b) = 5$ reads
$
a^2 + x a b + b^2 = (x + 1)^2.
$
The left side is the norm form of the quadratic ring $"GF"(2)[x][t]$ with $t^2 = x t + 1$: the element $t$ has trace $t + macron(t) = x$ and norm $t macron(t) = 1$, so $N(a + b t) = a^2 + x a b + b^2$ — and $t$ is a unit, exactly as in a Pell equation. Modulo the prime $x + 1$ the defining polynomial becomes $t^2 + t + 1$, which is irreducible over $"GF"(2)$, so $x + 1$ is inert and the only elements of norm $(x + 1)^2$ are the associates $(x + 1) t^k$.

Multiplying by $t$ sends $a + b t$ to $b + (a + x b) t$, i.e. $(a, b) -> (b, a xor 2 b)$, and negative powers merely swap the components, so iterating from $(3, 0)$ — through $(0, 3), (3, 6), (6, 15), dots$ — enumerates every solution as an unordered pair, roughly doubling each step. About sixty iterations reach $10^18$, and XORing the larger components gives the answer. The code checks completeness against a brute-force scan of the box $[0, 800]^2$ and reproduces the given $X(10) = 3 xor 6 = 5$.

#pagebreak()
#link("https://projecteuler.net/problem=879")[= Problem 879: Touch-screen Password]

Solution: 4350069824940

A password is the sequence of spots produced by tracing line segments on a grid: aiming along a segment selects the nearest still-remaining spot on it, selected spots vanish, and the password is the resulting sequence of two or more spots; we count the distinct passwords on a $4 times 4$ grid.

Since tracing toward any remaining spot picks up the nearest remaining spot on the way, a sequence $s_1, s_2, dots$ of distinct spots is achievable precisely when, for every consecutive pair, every grid spot lying strictly between $s_i$ and $s_(i + 1)$ on their segment already appears among $s_1, dots, s_i$ — earlier spots are ignored, and no fresh spot may be skipped. The count is therefore a bitmask dynamic program: $f("mask", c)$ is the number of achievable orderings of the spot set $"mask"$ ending at $c$, with the transition allowed when the precomputed between-mask of the final segment is contained in the prior mask, and every state with at least two spots is one password. For the $4 times 4$ grid this is $2^16 dot 16 dot 16 approx 1.7 dot 10^7$ transitions, a few seconds with numba; the same code reproduces the given $389488$ passwords on the $3 times 3$ grid.

#pagebreak()
#link("https://projecteuler.net/problem=881")[= Problem 881: Divisor Graph Width]

Solution: 205702861096933200

The divisor graph of $n$ joins divisors whose quotient is prime, levels are distances from the vertex $n$, and $g(n)$ is the size of the largest level; we need the smallest $n$ with $g(n) >= 10^4$.

Each edge changes $Omega$ (the number of prime factors with multiplicity) by one, and from $n$ one can reach a divisor $d$ by stripping the primes of $n \/ d$ one at a time, so the distance from $n$ to $d$ is exactly $Omega(n \/ d)$. Level $k$ therefore collects the divisors with $Omega = Omega(n) - k$, and writing $n = p_1^(e_1) dots p_r^(e_r)$, the level sizes are the coefficients of
$
product_(i = 1)^r (1 + x + dots + x^(e_i)),
$
so $g(n)$ is the largest coefficient of that polynomial — for $5040 = 2^4 dot 3^2 dot 5 dot 7$ it is $12$, matching the given value.

Only the exponent multiset matters, and assigning the larger exponents to the smaller primes minimises $n$, so a depth-first search over non-increasing exponent sequences on the primes $2, 3, 5, dots$ finds the optimum, pruned by the best $n$ so far. Since coefficients only grow when an exponent is raised or a prime appended, the first success along any branch is its cheapest, and the primorial of $16$ primes (central binomial $binom(16, 8) = 12870 >= 10^4$) provides the initial bound. The search visits only a few thousand nodes; the code also cross-checks it against a brute-force scan for small targets.

#pagebreak()
#link("https://projecteuler.net/problem=884")[= Problem 884: Removing Cubes]

Solution: 1105985795684653500

$D(n)$ counts the steps of repeatedly subtracting the largest cube not exceeding $n$ until reaching $0$, and $S(N) = sum_(n < N) D(n)$; we need $S(10^17)$.

For $n$ in the block $[k^3, (k + 1)^3)$ the first step lands on $n - k^3$, so $D(n) = 1 + D(n - k^3)$ and the block contributes its length plus $S("length")$. Summing over the blocks below $N$, with $K$ the largest integer with $K^3 < N$,
$
S(N) = (N - 1) + S(N - K^3) + sum_(k = 1)^(K - 1) S(3 k^2 + 3 k + 1),
$
since every $n < N$ contributes one first step and the full blocks have length $3 k^2 + 3 k + 1$. The crucial observation is that the full-block lengths are the same for every caller, so their $S$ values are accumulated once into prefix sums $T(K)$; only the partial top block spawns a bespoke recursive value, and that chain shrinks rapidly ($N -> O(N^(2\/3))$, about twenty levels from $10^17$). Building $T$ needs $K approx 464158$ entries, each $O(1)$ given the smaller entries, so the whole computation takes a couple of seconds. The code asserts the given $D(100) = 4$ and $S(100) = 512$ and checks $S(n)$ against brute force for all $n < 300$.

#pagebreak()
#link("https://projecteuler.net/problem=885")[= Problem 885: Sorted Digits]

Solution: 827850196

$f(d)$ sorts the digits of $d$ ascending and discards the zeros; $S(n)$ sums $f(d)$ over all positive integers of at most $n$ digits, and we need $S(18) mod 1123455689$.

Pad every number with leading zeros to exactly $18$ digits ($0$ itself contributes nothing). Then $f(d)$ depends only on the digit multiset of $d$, and a multiset with digit counts $c_0, dots, c_9$ is hit by exactly $18! \/ (c_0 ! dots c_9 !)$ integers, so
$
S(18) = sum_("multisets") 18! / (c_0 ! dots c_9 !) dot f,
$
a sum over the $binom(27, 9) = 4686825$ multisets. A recursion fixes the counts of digits $1, dots, 9$ in turn, growing the sorted value $f$ by one appended digit per step and the factorial denominator alongside, with the leftover count assigned to the invisible zeros — the shared prefixes keep the whole enumeration to a few seconds in exact integer arithmetic. The recursion reproduces the given $S(1) = 45$ and $S(5) = 1543545675$.

#pagebreak()
#link("https://projecteuler.net/problem=893")[= Problem 893: Matchsticks]

Solution: 26688208

$M(n)$ is the minimum number of matchsticks needed to write $n$ as an expression using seven-segment digits ($0$–$9$ cost $6, 2, 5, 5, 4, 5, 6, 3, 7, 6$) together with $+$ and $times$ (two sticks each, with the usual precedence and no brackets); $T(N) = sum_(n <= N) M(n)$, and we need $T(10^6)$.

With this grammar every expression is a sum of products of digit-form numbers. Let $P(n)$ be the cheapest product form: $P(n) = min(d(n), min_(a b = n) P(a) + P(b) + 2)$, computed for all $n <= 10^6$ by trial division in increasing order. Then, peeling the smallest term $b <= n \/ 2$ of an optimal sum,
$
M(n) = min(P(n), min_b M(n - b) + P(b) + 2).
$
Trying every $b$ is hopeless, but the useful addends all have tiny product cost — they are cheap constructs of $1$s and $7$s such as $11111$. This can be made rigorous: a factor needs at least two sticks per digit and factor lengths add up to at least the product's length, so $P(t) >= 2 ell(t)$ and hence $M(t) >= 2 ell(t)$, where $ell$ is the decimal length. If the smallest term had $P(b) > theta$ then $M(n) >= 2 ell(ceil(n \/ 2)) + theta + 3$. Taking $theta = 20$ (the $33809$ candidates with $P <= 20$, scanned in increasing cost with the same inequality as an early-exit prune) and verifying afterwards that every computed value satisfies $M(n) <= 2 ell(ceil(n \/ 2)) + theta + 3$ proves by induction that no other addend could ever have helped; below $n = 2001$ all addends are tried outright. The run takes a few seconds with numba and reproduces the given $M(28) = 9$ and $T(100) = 916$.

#pagebreak()
#link("https://projecteuler.net/problem=899")[= Problem 899: DistribuNim I]

Solution: 10784223938983273

In this two-pile game a move removes exactly $min(a, b)$ stones in total, distributed freely but never emptying a pile; the player who cannot move loses, and $L(n)$ counts ordered losing pairs with both piles at most $n$.

Taking $a <= b$, a move removes $a$ stones, so the positions reachable from $(a, b)$ are exactly the splits $(a', b - a')$ of $b$ with $1 <= a' <= a$ and $b - a' >= 1$. The losing positions are precisely those with $a < 2^t$ where $t = v_2 (b + 1)$ — that is, the binary expansion of $b$ ends in a run of ones longer than the bit length of $a$. By induction on $a + b$: the only terminal position $(1, 1)$ qualifies; from a losing position, a losing successor with parts $c <= d$ summing to $b$ would force $2^min(t, ell(c)) | c$ with $c < 2^min(t, ell(c))$, impossible; and from a winning position ($a >= 2^t$), splitting off $c = 2^t$ leaves $d = b - c$ with $v_2 (d + 1) >= t + 1 = ell(c)$, a losing position (the case $c > d$ would need $b = 2^t - 1 < a$, absurd). The solution cross-checks this against a brute-force game solver on $[1, 129]^2$.

Counting is then immediate: for $2^k <= a < 2^(k + 1)$ the partner must satisfy $b equiv -1 mod 2^(k + 1)$, giving $floor((n + 1) \/ 2^(k + 1))$ choices for each of the $min(2^(k + 1) - 1, n) - 2^k + 1$ values of $a$, doubled for order with the diagonal pairs $a = b = 2^m - 1$ subtracted once. This yields the given $L(7) = 21$ and $L(7^2) = 221$, and $L(7^17)$ instantly.

#pagebreak()
#link("https://projecteuler.net/problem=900")[= Problem 900: DistribuNim II]

Solution: 646900900

A move removes exactly $m = min("piles")$ stones in total, distributed so that no pile is emptied. Brute-forcing all positions with $2$–$6$ piles (sizes up to $16$) reveals a clean characterisation of the losing positions: a position with $r$ piles, minimum $m$ and total $s$ is losing for the player to move if and only if
$
s equiv m - [r " even"] space (mod 2^L), quad 2^L = "smallest power of two" > m.
$
For $n$ piles of $n$ stones plus one pile of $n + k$ we have $r = n + 1$, $m = n$ and $s = n^2 + n + k$, so the smallest losing $k$ is
$
t(n) = (-n^2 - (n mod 2)) mod 2^L .
$
In particular $t(2^j) = 0$, matching $t(1) = t(2) = 0$ and $t(3) = 2$.

To sum $t(n)$ for $n$ up to $2^(10^4)$, group $n in [2^(L-1), 2^L)$ and write $n = 2^(L-1) + j$: since $(2^(L-1))^2 equiv 0 space (mod 2^L)$, $t$ depends only on $j$. For odd $j$, $t = 2^L - 1 - (j^2 mod 2^L)$, and the odd squares below $2^(L-1)$ hit each residue $equiv 1 space (mod 8)$ exactly twice, giving a closed form. For even $j = 2i$ the block reduces to the full-period sum $Q(M) = sum_(i < 2^M) (i^2 mod 2^M)$, which satisfies
$
Q(M) = 2^(M-1)(2^(M-1) - 3) + 8 Q(M-2).
$
Everything is carried modulo $900497239$; the formula reproduces $S(10) = 361522$ exactly, and $S(10^4) equiv 646900900$.

#pagebreak()
#link("https://projecteuler.net/problem=901")[= Problem 901: Well Drilling]

Solution: 2.364497769

We choose an increasing sequence of depths $0 = d_0 < d_1 < d_2 < dots$ and drill to each in turn until we strike water. The groundwater depth is $X tilde "Exp"(1)$, so $P(X > d) = e^(-d)$, and a drill to depth $d_i$ is only attempted when every earlier drill failed, i.e. with probability $e^(-d_(i-1))$. Each attempt costs its full depth in hours (we start over each time), so the expected total time is
$
E = sum_(i >= 1) d_i e^(-d_(i-1)).
$

Setting $partial E \/ partial d_j = 0$ gives $e^(-d_(j-1)) = d_(j+1) e^(-d_j)$, that is the optimal depths satisfy the recurrence
$
d_(j+1) = e^(d_j - d_(j-1)).
$
With $d_0 = 0$ this is a two-point boundary value problem ($d_0 = 0$ and $d_N -> infinity$). Forward shooting from a guessed $d_1$ is numerically unstable, because the recurrence amplifies any error exponentially. Instead we solve the whole stationary system at once with Newton's method on the residuals $F_j = d_(j+1) - e^(d_j - d_(j-1))$, whose Jacobian is tridiagonal, pinning the far end $d_N$ at a large value $L$ (the tail beyond depth $L$ contributes less than $e^(-L)$ and is negligible). The depths converge stably, and the resulting expected time is $2.364497769$ hours, robust across choices of $N$ and $L$.

#pagebreak()
#link("https://projecteuler.net/problem=902")[= Problem 902: Permutation Powers]

Solution: 343557869

The permutation $sigma$ is a product of disjoint cycles of lengths $1, dots, m$ (one per triangular block), and $pi = tau^(-1) sigma tau$ is conjugate to it, so $pi$ has order $L = "lcm"(1, dots, m)$, which divides $m!$. Hence
$
P(m) = m!/L sum_(k=1)^L "rank"(pi^k).
$

By the Lehmer code, $"rank"(rho) - 1 = sum_i c_i (n-i)!$ with $c_i = hash{j > i : rho(j) < rho(i)}$, so the sum over $k$ becomes a sum over ordered pairs of positions. Substituting $a = tau(i)$, $b = tau(j)$ and $w = tau^(-1)$, the condition $pi^k (j) < pi^k (i)$ reads $w(sigma^k b) < w(sigma^k a)$, which only involves rotations within the two $sigma$-cycles containing $a$ and $b$. If those cycles have lengths $p$ and $q$ with $g = gcd(p, q)$ and $l = "lcm"(p, q)$, the offset pair $(k mod p, k mod q)$ sweeps each compatible combination exactly once every $l$ steps, so the count of good $k in [1, L]$ is $L \/ l$ times a table value $C(d)$ depending only on the offset difference $d = (alpha - beta) mod g$:
$
C(d) = hash{(u, v) : u - v equiv d space (mod g), space w(B[v]) < w(A[u])}.
$
Each ordered cycle pair therefore costs two $O(p q)$ double loops — one building $C$, one accumulating $(n - w(a))! dot C(d)$ over the pairs with $w(a) < w(b)$ — and same-cycle pairs use the analogous shift table. The total work is about $2 n^2 approx 5 dot 10^7$ operations for $n = 5050$. All the divisions by $l$ and by $L$ are exact, so they are performed with modular inverses. The method reproduces $P(2) = 4$, $P(3) = 780$ and $P(4) = 38810300$, and gives $P(100) equiv 343557869 space (mod 10^9 + 7)$.

#pagebreak()
#link("https://projecteuler.net/problem=903")[= Problem 903: Total Permutation Powers]

Solution: 128553191

By the Lehmer code, $"rank"(rho) - 1 = sum_(i<j) [rho(j) < rho(i)] (n-i)!$, so $Q(n) - (n!)^2$ is a sum over position pairs $(i, j)$ and over $(pi, k)$ of the indicator $[pi^k (j) < pi^k (i)]$. Conjugating $pi$ by the transposition $(i thin j)$ is an involution that swaps the two image values whenever both lie outside ${i, j}$, so that bulk contributes exactly one half. The boundary cases reduce to four counts, each summed over $k = 1, dots, n!$, of permutations whose $k$-th power (a) fixes both $i$ and $j$, (b) swaps them, (c) fixes $i$ and moves $j$, or (d) maps $i$ to $j$ without mapping $j$ back; within (c) and (d) the free image value is equidistributed over the other $n - 2$ values, by conjugating with transpositions of outside values.

The enumeration rests on a pleasant fact: the number of permutations of $[n]$ with "the cycle of $i$ has length $ell$ and $j$ sits $t$ steps along it", and likewise with "$i$ in an $ell$-cycle and $j$ in a separate $m$-cycle", is exactly $(n-2)!$ in every case. Combined with $hash{k <= n! : d divides k} = n! \/ d$, all four counts become elementary sums; the only nontrivial one is
$
S_"lcm" = sum_(ell + m <= n) 1/("lcm"(ell, m)).
$
Writing $"lcm" = ell m \/ gcd$ and Möbius-inverting the coprimality condition collapses it to
$
S_"lcm" = sum_(e >= 1) (phi(e))/(e^2) thin G(floor(n\/e)), quad G(M) = sum_(a + b <= M) 1/(a b),
$
where $G$ is needed only at the $O(sqrt(n))$ distinct values of $floor(n \/ e)$ and each evaluation is a harmonic-number convolution. The per-pair weight depends only on $j - i$, so the final assembly is a single $O(n)$ loop. All divisions are exact integers, performed with modular inverses. The method reproduces $Q(3) = 88$, $Q(6) = 133103808$ and $Q(10) equiv 468421536$, and gives $Q(10^6) equiv 128553191 space (mod 10^9 + 7)$.

#pagebreak()
#link("https://projecteuler.net/problem=904")[= Problem 904: Pythagorean Angle]

Solution: 880652522278760

For a right triangle with legs $a, b$ and hypotenuse $c$, the angle between the medians to the two legs satisfies $tan theta = (3 a b)/(2 c^2) <= 3\/4$, which depends only on the shape of the triangle. Each shape comes from a unique coprime pair $0 < p < q$: with $t = p\/q$ we get $tan theta = g(t) = (3t(1 - t^2))/((1 + t^2)^2)$, the primitive triple being $(q^2 - p^2, 2p q, q^2 + p^2)$ when $p + q$ is odd and $((q^2 - p^2)\/2, p q, (q^2 + p^2)\/2)$ when both are odd. The involution $t <-> (1-t)\/(1+t)$ exchanges the two parity classes while fixing the shape, so we may restrict to $t in (0, sqrt(2) - 1)$, where $g$ is strictly increasing (its maximum $3\/4$ is attained at $t = sqrt(2) - 1$). Since $theta$ determines the shape and $alpha = root(3, n)$ admits no symmetric ties (Niven's theorem and Gelfond–Schneider rule out the coincidences a tie would force), $f$ is found by taking the feasible shape closest in $theta$, then the largest multiple $d = floor(L\/c)$, giving $f = d(a + b + c)$.

So solve $g(t) = tan alpha$ for the target $t_1$ (bisection plus a few Newton steps in multiprecision) and look for the coprime fraction nearest $t_1$ whose primitive hypotenuse fits: $p^2 + q^2 <= L$ for opposite parity but only $p^2 + q^2 <= 2L$ for both odd. This parity-dependent bound is the trap of the problem: the answer is _not_ always a (semi)convergent of $t_1$. A both-odd fraction slightly farther out in the Stern–Brocot tree can be feasible while every nearer spine node of the right parity is not — first seen at $n = 26176$, $L = 10^8$, where $(p, q) = (2689, 12259)$ (both odd) beats the closer but infeasible $(2197, 10016)$. The fix is a two-pass search: a cheap Stern–Brocot spine walk with run jumps yields the distance $D_0$ of the best feasible spine node, and then a windowed Stern–Brocot enumeration lists _all_ coprime $p\/q$ with $q <= sqrt(2 L)$ within $1.05 D_0$ of $t_1$ — the window is so narrow that only a handful of fractions survive. Surviving candidates are ranked by $abs(theta - alpha)$ in floating point, and near-ties are separated by escalating the working precision (60, 150, then 400 digits, recomputing $alpha$ afresh each time). The search was verified against full enumeration of all $approx 1.6 dot 10^7$ primitive shapes at $L = 10^8$ for 413 values of $n$, including 13 cases where a spine-only search fails. It reproduces $f(30, 100) = 198$, $f(root(3, 10), 10^6) = 1600158$ and $F(10, 10^6) = 16684370$, and computes $F(45000, 10^(10)) = 880652522278760$ in under a minute.

#pagebreak()
#link("https://projecteuler.net/problem=905")[= Problem 905: Now I Know]

Solution: 70228218

Three logicians wear hats with positive integers, exactly one of which is the sum of the other two. Each sees the other two numbers but not their own, and in cyclic order $A, B, C$ says either "I don't know" or "Now I know"; $F(A,B,C)$ is the turn on which someone first knows.

The clean way to reason is as public elimination of possible worlds, a world being any valid triple. At turn $t$ the player $p = (t-1) mod 3$ sees the two coordinates other than $p$; the value they could hold is either the sum or the absolute difference of what they see, so there are at most two candidate worlds: the real one and its "flip" at position $p$. A world is eliminated at the first turn on which its scheduled player would know. Calling that turn $F$ of the world,
$
"knows"(w, t) <==> ("the two seen values are equal") or (F("flip") <= t - 1).
$

Taking the minimum over the three players shows the deciding player is always the holder of the sum, and flipping the sum coordinate to $|s - u|$ is exactly one subtractive step of the Euclidean algorithm on the two "part" values, with the sum position migrating to whichever part is larger. So $F$ is assembled bottom-up along the Euclidean descent of the parts: at the base, where the two parts are equal, $F = p_"sum" + 1$, and climbing one step
$
F = "smallest " t > F_"below" " with " t equiv p_"sum" + 1 space (mod 3),
$
where $p_"sum" in {0,1,2}$ is the position of the sum at that step.

A literal subtractive descent is far too long, since a single quotient can take on the order of $10^7$ steps. But within one quotient the sum position merely alternates between two slots, and along an alternating run the climb's increment is constant after the first step (each pair of steps raises $F$ by exactly $3$), so an entire run is collapsed to $O(1)$ arithmetic. The descent then has only $O(log)$ runs per triple. Summing $F(a^b, b^a, a^b + b^a)$ over $a in {1, dots, 7}$ and $b in {1, dots, 19}$ gives $70228218$.

#pagebreak()
#link("https://projecteuler.net/problem=906")[= Problem 906: A Collective Decision]

Solution: 0.0195868911

The chosen option is exactly a _Condorcet winner_ over the three random preference orders, and such a winner is unique (two winners would each need a strict majority over the other), so $P(n) = n dot Pr("option" 1 "wins")$. Condition on the number $r_v$ of options that voter $v$ prefers over option $1$: each $r_v$ is uniform on ${0, dots, n-1}$, and given $r_v$ the set $S_v$ of those options is a uniform $r_v$-subset of the other $m = n - 1$ options. Option $1$ wins precisely when every other option is preferred over it by at most one voter, i.e. when $S_1, S_2, S_3$ are pairwise disjoint. Counting ordered disjoint triples,
$
Pr("win") = 1/n^3 sum_(r_1 + r_2 + r_3 <= m) (binom(m - r_1, r_2))/(binom(m, r_2)) dot (binom(m - r_1 - r_2, r_3))/(binom(m, r_3)).
$
The innermost sum collapses by the identity $sum_(k <= b) binom(b, k) \/ binom(m, k) = (m+1)/(m+1-b)$, leaving (with $a = m - r_1$)
$
P(n) = 1/n sum_(a = 0)^(m) sum_(r = 0)^(a) (binom(a, r))/(binom(m, r)) dot 1/(m - a + r + 1),
$
an $O(n^2)$ double sum in which the binomial ratio obeys the one-step recurrence $times (a - r + 1)\/(m - r + 1)$. With Kahan compensation the $4 dot 10^8$-term float sum stays far below the required ten-decimal accuracy (the eleventh decimal of the result is a $0$, so the rounding is not borderline). The formula reproduces $P(3) = 17\/18$ and $P(10) approx 0.6760292265$, and gives $P(20000) approx 0.0195868911$ in a few seconds.

#pagebreak()
#link("https://projecteuler.net/problem=907")[= Problem 907: Stacking Cups]

Solution: 196808901

A tower is a bottom-to-top sequence of all $n$ cups, each up or down. Translating the contact rules: a lower cup $(j, "up")$ supports $(j - 1, "up")$ (nesting), a lower $(j, "down")$ supports $(j + 1, "down")$ (the larger cup lowered over the smaller), a lower $(j, "down")$ supports $(j plus.minus 2, "up")$ (base-to-base), and a lower $(j, "up")$ supports $(j plus.minus 2, "down")$ (rim-to-rim). The forbidden two-cups-on-one configuration never arises in a single tower. This model reproduces all three given values, so $S(n)$ counts directed Hamiltonian paths in this oriented-cup graph.

Every edge joins labels at distance at most $2$, so for small $n$ a bitmask DP over (used set, last cup, last orientation) computes $S(n)$ exactly; this gives $S(1), dots, S(20)$, matching $S(4) = 12$, $S(8) = 58$ and $S(20) = 5560$. The bounded bandwidth also forces a short linear recurrence. Fitting the DP values and re-verifying on every $n$ in $10..20$ yields, for $n >= 10$,
$
S(n) = 2S(n-1) - 3S(n-2) + 5S(n-3) - 4S(n-4) + 4S(n-5) - 3S(n-6) + S(n-7) - S(n-8),
$
with a single transient at $S(9) = 82$ (the fit would give $84$). The characteristic polynomial factors neatly as $(x - 1)(x^2 + 1)^2 (x^3 - x^2 - 1)$, so the count grows like $rho^n$ for the root $rho approx 1.4656$ of $x^3 = x^2 + 1$. Iterating the recurrence modulo $10^9 + 7$ up to $n = 10^7$ gives $S(10^7) equiv 196808901$.

#pagebreak()
#link("https://projecteuler.net/problem=908")[= Problem 908: Clock Sequence II]

Solution: 451822602

A periodic sequence segments into blocks summing to $1, 2, 3, dots$ exactly when every triangular number $T(n) = n(n+1)\/2$ occurs among its prefix sums. If one period is a composition of $s$ into $p$ parts with prefix sums $S(1) < dots < S(p) = s$, the prefix sums of the infinite sequence are ${k s + S(r) : k >= 0}$, so the clock property is equivalent to
$
D(s) := {((T(n) - 1) mod s) + 1 : n >= 1} subset.eq {S(1), dots, S(p)},
$
with representatives in $[1, s]$ ($T(n) mod s$ is periodic in $n$ with period dividing $2s$, and $s in D(s)$ always since $T(2s) = s(2s+1)$). This criterion was checked against direct simulation of the segmentation on hundreds of random compositions.

Compositions of $s$ into $p$ parts are subsets of $[1, s-1]$ of size $p - 1$, so with $d(s) = |D(s)| - 1$ the clock compositions of length $p$ and sum $s$ number $binom(s - 1 - d(s), p - 1 - d(s))$. Distinct sequences are primitive compositions counted by minimal period, and Möbius inversion over the divisor lattice gives $C(N) = sum_(q <= N) g(q) dot M(floor(N\/q))$ with $g(p) = sum_s binom(s - 1 - d(s), p - 1 - d(s))$ and $M$ the Mertens function. The count $|D(s)|$ of distinct triangular residues is multiplicative: modulo $2^k$ the triangular numbers cover _all_ residues, while modulo an odd $p^k$ they biject (via $8 T(n) + 1 = (2n+1)^2$) with the squares, of which there are $1 + sum_(e = k, k-2, dots >= 1) phi(p^e)\/2$; so $d(s)$ is sieved multiplicatively. Each odd prime factor retains at least a fraction $p\/(2(p+1)) >= 3\/8$ of residues, so $d(s) < 10^4$ forces $s lt.tilde 1.5 dot 10^6$; in fact only $47228$ values qualify, the largest being $294525$. The method reproduces $C(3) = 3$, $C(4) = 7$, $C(10) = 561$ and gives $C(10^4) equiv 451822602 space (mod 1111211113)$ in seconds.

#pagebreak()
#link("https://projecteuler.net/problem=909")[= Problem 909: L-expressions I]

Solution: 399885292

The rewrite rules are exactly the combinator rules of Church numerals: $Z(u)(v) -> v$ makes $Z$ the numeral $[0]$, and $S(u)(v)(w) -> v(u(v)(w))$ makes $S$ the successor, where the numeral $[n]$ acts on any object by $n$-fold composition, $[n](f) = f^(compose n)$. Applying $[n]$ to $A$ and $0$ then yields the number $n$.

Write $P = S(S)$. Two extensional facts settle everything: composition multiplies numerals, $[a] compose [b] = [a b]$, and the $S$-rule reads $S(g)(h) = h compose g(h)$, $P(g)(h) = g(S(g)(h))$. Hence $P([n]) = [n(n+1)]$, then $S(P)([n]) = [n] compose P([n]) = [n^2(n+1)]$, and $P(P)([n]) = P(S(P)([n])) = [m(m+1)]$ with $m = n^2(n+1)$. For the target $P(P)(P)([1])(A)(0)$: by the $S$-rule, $P(P)(P) = P(X)$ with $X = S(P)(P): t |-> P(P(P)(t))$, and $P(X)([1]) = X(S(X)([1])) = X(X([1]))$ since $[1]$ is the identity. With $p(n) = n(n+1)$, $italic("pp")(n) = p(n thin p(n))$ and $x(n) = p(italic("pp")(n))$ this gives $x(x(1)) = x(42) = M(M+1)$ for $M = 75852 dot 75853$, whose last nine digits are $399885292$. Every identity used — and both worked examples — is verified by an exact mechanical normal-order evaluator on small numerals, where the reduction terminates in at most a few million steps.

#pagebreak()
#link("https://projecteuler.net/problem=910")[= Problem 910: L-expressions II]

Solution: 547480666

With the Church-numeral reading of Problem 909, $C_i = [i]$ and $D_i = C_i (S)(S) = S^i (S)$, so $D_i = S(D_(i-1))$ and the $S$-rule gives $D_i (h)(w) = h(h(dots h(S(h)(w)) dots))$ with $h$ object-applied $i$ times. In $F(a,b,c,d,e) = D_a (D_b)(D_c)(C_d)(A)(e)$ every application chain bottoms out on numerals, where applying an operator $V$ with numeral action $v$ is plain arithmetic and $S(V)([m]) = [m] compose V([m]) = [m dot v(m)]$. Peeling layers (superscripts denote function iteration):
$
f(m) = (m+1) m^c, quad w_1 (m) = f^((b))(m f(m)), quad v_0 (m) = f(w_1 (m)),
$
$
v_k (m) = v_(k-1)^((b))(m thin v_(k-1)(m)) "for" k = 1, dots, a, quad F = e + v_a (d).
$
This arithmetic semantics was verified against exact mechanical reduction of the L-expressions (with $D_i$ built literally as $C_i (S)(S)$) on 92 small parameter tuples.

The value $v_a (d)$ is an astronomical tower, but every operation involved is a ring operation with _fixed_ exponent $c$ and _fixed_ iteration count $b$ — no value ever appears in an exponent — so the entire computation descends to $ZZ_M$ for any modulus $M$. Tabulating each $v_k$ over $ZZ_M$ and forming $b$-fold iterates by binary lifting ($log_2 b$ table compositions) costs $O(M log b)$ per level. Running the pipeline modulo $2^9$ and $5^9$ and combining by CRT gives $F(12, 345678, 9012345, 678, 90) equiv 547480666 space (mod 10^9)$ in a few seconds.

#pagebreak()
#link("https://projecteuler.net/problem=911")[= Problem 911: Khinchin Exceptions]

Solution: 5679.934966

Since $rho_n = sum_i 2^(n - 2^i) = 2^n rho_0$ is a dyadic shift of the Kempner number, its partial sums $P_K = sum_(i <= K) 2^(n - 2^i)$ are exact dyadic rationals whose continued fractions exhibit the classical _folding_ doubling: the CF at level $K + 1$ repeats the CF at level $K$ up to $O(1)$ boundary quotients (empirically, the lists agree on all but the final quotient). Consequently the count $c_a (K)$ of each quotient value $a$ in the CF body obeys an exact affine doubling recurrence $c_a (K+1) = 2 c_a (K) + e_a$, $L(K+1) = 2 L(K) + e_L$ with constant integer edits, verified across three consecutive levels for every $n$. Then $c_a (K) + e_a$ doubles exactly, so the limiting frequency of $a$ is the exact rational $f_a = (c_a (K) + e_a)/(L(K) + e_L)$ with $sum_a f_a = 1$, and $k_oo (rho_n) = product_a a^(f_a)$.

The quotient alphabets are tiny and structured. For $n = 0$: ${2, 4, 6}$ with frequencies $(1\/4, 1\/2, 1\/4)$, so $k_oo (rho_0) = 2 dot 12^(1\/4)$. For $n = 2$: ${1, 2, 3, 4}$ with $(1\/3, 1\/12, 1\/2, 1\/12)$, giving $k_oo (rho_2) = 2^(1\/4) sqrt(3) = 2.0597671 dots$, matching the stated value. Large $n$ involve quotients near powers $2^(2^j - n)$, e.g. $2^50 - 1$ for $n = 50$, where $k_oo approx 2.64 dot 10^6$. The geometric mean over $n = 0, dots, 50$, evaluated at 40-digit precision, is $5679.9349661 dots$, which rounds to $5679.934966$ with a comfortable margin.

#pagebreak()
#link("https://projecteuler.net/problem=912")[= Problem 912: Where are the Odds?]

Solution: 674045136

$s_n$ is odd exactly when its last bit is $1$. Valid numbers (no $111$ in binary) in increasing order are: lengths $L = 1, 2, dots$, and within a length, lexicographic order of the bits after the leading $1$. Walking that implicit trie — automaton state = number of trailing ones, $0..2$ — visits the numbers in rank order, so $F(N)$ only needs subtree aggregates: for completions of length $r$ from state $italic("st")$ with $0$-based lexicographic positions, the count $T$, the number $O$ of completions ending in bit $1$ (odd numbers), the sum $S_1$ of their positions and the sum $S_2$ of their squared positions. A whole subtree entered after `base` numbers have been consumed contributes $(b+1)^2 O + 2(b+1) S_1 + S_2$ with $b = $ `base`, since its items have global indices $b + 1 + "pos"$.

The recurrences split on the next bit (bit $0$ resets the state and comes first; bit $1$, allowed while $italic("st") < 2$, offsets positions by the left subtree's count). The counts $T$ are kept exact for the descent — $N = 10^16$ reaches binary lengths near $63$ since valid numbers grow like the tribonacci constant $1.839^L$ — while $O, S_1, S_2$ live modulo $10^9 + 7$. After summing the full lengths, a single partial descent consumes the remaining ranks. The method reproduces $F(10) = 199$, agrees with brute force up to $N = 5 dot 10^4$, and gives $F(10^16) equiv 674045136$ instantly.

#pagebreak()
#link("https://projecteuler.net/problem=913")[= Problem 913: Row-major vs Column-major]

Solution: 2101925115560555020

The minimum number of swaps realising a permutation is its size minus its number of cycles. Going from row-major to column-major moves the value at $0$-based position $k$ to $(k mod n) m + floor(k\/n) = k m mod (n m - 1)$ for $k < n m - 1$, with $n m - 1$ fixed — the classical in-place transposition permutation. Since $n m equiv 1 (mod n m - 1)$, multiplication by $m$ and by $n$ are inverse maps with identical cycle structure. The cycles of $x |-> n x$ on $ZZ_M$, $M = n m - 1$, split by $g = gcd(x, M)$: the $phi(d)$ elements with $d = M\/g$ fall into free orbits of size $"ord"_d (n)$, giving
$
S(n, m) = n m - 1 - sum_(d divides M) (phi(d))/("ord"_d (n)).
$
Checking $S(3,4)$: $M = 11$, $"ord"_11 (3) = 5$, so $S = 12 - 1 - (1 + 2) = 8$. ✓

For $S(n^4, m^4)$ the modulus is $q^4 - 1 = (q-1)(q+1)(q^2+1)$ with $q = n m <= 10^4$, so every part — and every $p - 1$ needed for order computations — factors by trial division below $10^4$. Orders modulo prime powers lift stepwise ($"ord"_(p^(j+1))$ is $"ord"_(p^j)$ or $p$ times it), and the divisor sum runs over exponent tuples carrying a running $phi$ and lcm of orders. Each $phi(d)\/"ord"_d$ is an exact integer (free orbits). Verified against literal matrix brute force for all $2 <= n <= m <= 11$ and against the given total $12578833$ for the first range, the sum over $2 <= n <= m <= 100$ of $S(n^4, m^4)$ evaluates to $2101925115560555020$ in half a second.

#pagebreak()
#link("https://projecteuler.net/problem=914")[= Problem 914: Triangles inside Circles]

Solution: 414213562371805310

A right triangle's minimum enclosing circle is its circumcircle, whose diameter is the hypotenuse, so the triangle fits strictly inside a circle of radius $R$ iff $c <= 2R - 1$. For a primitive triple generated by coprime, opposite-parity $m > k >= 1$ we have $c = m^2 + k^2$ and inradius $r = (a + b - c)\/2 = k(m - k)$. So $F(R)$ maximises $k d$ (with $d = m - k$) subject to $(k + d)^2 + k^2 <= 2R - 1$, $d$ odd (exactly the opposite-parity condition) and $gcd(k, d) = 1$.

Lagrange multipliers on the real relaxation give $d^* = k^* sqrt(2)$ with $k^* = sqrt(R(2 - sqrt(2))\/2)$, and maximal $r = R(sqrt(2) - 1)$ — the answer is within a rounding's breadth of $(sqrt(2) - 1) dot 10^18$. For the integer problem, moving $k$ off $k^*$ loses about $2(k - k^*)^2$, while repairing parity and coprimality costs at most a few units of $d$, i.e. $O(k) approx 5 dot 10^8$ in $r$; hence the optimum lies within $|k - k^*| lt.tilde 5 dot 10^4$, and scanning a window of $2 dot 10^6$ (the result is unchanged at $4 dot 10^6$) is a wide margin. For each $k$ the maximal $d$ is $floor(sqrt(2R - 1 - k^2)) - k$, and the first few valid $d$ below it are tried. The method agrees with full brute force for all tested $R <= 10^5$, including the given $F(100) = 36$, and yields $F(10^18) = 414213562371805310$.

#pagebreak()
#link("https://projecteuler.net/problem=915")[= Problem 915: Giant GCDs]

Solution: 55601924

Write $t(n) = s(n) - 1$, so $t(1) = 0$ and $t(n+1) = t(n)^3 + 1$. Since $t^3 + 1 = (t + 1)(t^2 - t + 1)$, $s(n) = t(n) + 1$ divides $t(n+1)$, i.e. $t(n+1) equiv 0 = t(1) (mod s(n))$; both sides follow the same recurrence, so $t(n + j) equiv t(j) (mod s(n))$ for all $j >= 1$. Hence for $m > n$, $gcd(s(m), s(n)) = gcd(t(m - n) + 1, s(n)) = gcd(s(m - n), s(n))$, and subtractive Euclid yields the divisibility-sequence identity $gcd(s(m), s(n)) = s(gcd(m, n))$, verified exactly for $m, n <= 8$. Applying it twice, $gcd(s(s(a)), s(s(b))) = s(s(gcd(a, b)))$, so with $Phi(x) = sum_(k <= x) phi(k)$,
$
T(N) = sum_(g <= N) s(s(g)) (2 Phi(floor(N\/g)) - 1) space (mod M).
$

$M = 123456789 = 9 dot 3607 dot 3803$, so $s(s(g)) mod M$ follows by CRT from each factor $q$. Modulo $q$ the map $x |-> x^3 + 1$ has a tiny orbit from $t(1) = 0$, with (preperiod, period) equal to $(0, 3)$, $(53, 35)$, $(0, 963)$ respectively; for the giant index $s(g)$ only $s(g) mod pi_q$ is needed (any $g >= 7$ guarantees $s(g)$ exceeds the preperiod), and that iterates the same recurrence modulo $pi_q$. A single pass over $g = 1, dots, 10^8$ carries $t(g)$ modulo the three periods and accumulates the weighted sum; the weights use a $phi$ sieve for $v <= sqrt(N)$ and the sublinear recursion $Phi(x) = x(x+1)\/2 - sum_(d >= 2) Phi(floor(x\/d))$ for large arguments. The given $T(3) = 12$, $T(4) equiv 24881925$ and $T(100) equiv 14416749$ are all reproduced, and $T(10^8) equiv 55601924$ takes about seven seconds.

#pagebreak()
#link("https://projecteuler.net/problem=916")[= Problem 916: Restricted Permutations]

Solution: 877789135

By the RSK correspondence, permutations of ${1, dots, 2n}$ biject with pairs $(P, Q)$ of standard Young tableaux of a common shape $lambda tack.r 2n$, where the longest increasing subsequence equals the first row length and the longest decreasing subsequence equals the first column length. The condition LDS $<= 2$ restricts to shapes with at most two rows $lambda = (lambda_1, lambda_2)$ with $lambda_1 + lambda_2 = 2n$; combined with LIS $<= n + 1$ and $lambda_1 >= lambda_2$, only $lambda_1 in {n, n + 1}$ survive. Hence
$
P(n) = f_((n, n))^2 + f_((n+1, n-1))^2,
$
where the two-row ballot formula $f_((a, b)) = (a - b + 1)/(a + 1) binom(a + b, b)$ gives $f_((n,n)) = "Cat"(n)$ and $f_((n+1, n-1)) = 3 binom(2n, n-1)\/(n + 2)$.

Sanity checks: $n = 2$ yields $2^2 + 3^2 = 13$ as given; literal brute-force enumeration of all $(2n)!$ permutations with explicit LIS/LDS tests agrees for $n <= 4$; and $P(10) equiv 45265702 (mod 10^9 + 7)$ is reproduced ($16796^2 + 41990^2 = 2045265716$). The final evaluation needs just four factorials up to $(2 dot 10^8)! mod p$, collected in a single product loop, giving $P(10^8) equiv 877789135$ in about a second.

#pagebreak()
#link("https://projecteuler.net/problem=917")[= Problem 917: Minimal Path Using Additive Cost]

Solution: 9986212680734636

Every monotone path visits each row and column at least once, so $A(N) = sum a + sum b + "extra"$, where the extra cost charges $a_i$ for every right move made in row $i$ and $b_j$ for every down move made in column $j$. An optimal path is a staircase of horizontal runs along a few _transit rows_ and vertical runs along a few _transit columns_.

The key exchange argument: if a transit row $r$ has chain neighbours $r' < r < r''$ with $a_(r') < a_r$ and $a_(r'') < a_r$, moving the right moves of $r$ up to $r'$ shifts the intervening down moves to a later column, while moving them down to $r''$ shifts down moves to an earlier column — the two $b$-cost changes have opposite signs, so one of the relocations cannot increase cost while strictly reducing the $a$-cost. Hence the $a$-values along an optimal chain form a valley (decreasing then increasing), each transit row is the minimum of $a$ over the gap between its chain neighbours, and inductively every decreasing-phase row is a _prefix record_ of $a$, while — by reversing the grid — every increasing-phase row is a _suffix record_. The same holds for columns with $b$. A pseudorandom sequence of length $10^7$ has about $2 ln N approx 32$ records per side, so a shortest-path DP over the record-row $times$ record-column corners (horizontal edges costing $(c'' - c) a_r$, vertical edges $(r'' - r) b_c$) finishes instantly. The reduction was verified against the full $O(N^2)$ DP on forty instances across four seeds, and the givens $A(1)$, $A(2)$, $A(10)$ are reproduced; $A(10^7) = 9986212680734636$.

#pagebreak()
#link("https://projecteuler.net/problem=918")[= Problem 918: Recursive Sequence Summation]

Solution: -6999033352333308

Pairing consecutive terms telescopes the entire sum: $a_(2n) + a_(2n+1) = 2a_n + a_n - 3a_(n+1) = 3(a_n - a_(n+1))$, so
$
S(2M + 1) = a_1 + sum_(n=1)^M (a_(2n) + a_(2n+1)) = 1 + 3(a_1 - a_(M+1)) = 4 - 3a_(M+1),
$
and $S(2M) = S(2M+1) - a_(2M+1) = 4 - 3a_(M+1) - (a_M - 3a_(M+1)) = 4 - a_M$. This reproduces the given $S(10) = 4 - a_5 = 4 - 17 = -13$.

A single term $a_n$ follows by binary descent on the pair $(a_k, a_(k+1))$: from $(a_n, a_(n+1))$ one gets $(a_(2n), a_(2n+1)) = (2a_n, a_n - 3a_(n+1))$ and $(a_(2n+1), a_(2n+2)) = (a_n - 3a_(n+1), 2a_(n+1))$, so the pair at index $k$ reduces to the pair at $floor(k\/2)$. Hence $S(10^12) = 4 - a_(5 dot 10^11)$ costs $O(log N)$ integer operations. Both the closed form and the descent are verified against a direct table of the first $800$ terms, giving $S(10^12) = -6999033352333308$.

#pagebreak()
#link("https://projecteuler.net/problem=919")[= Problem 919: Fortunate Triangles]

Solution: 134222859969633

Every vertex lies at distance $R$ (the circumradius) from the circumcentre, and at distance $2R|cos theta|$ from the orthocentre, where $theta$ is the angle at that vertex. So a triangle is fortunate iff some angle satisfies $cos theta = plus.minus 1\/4$; by the law of cosines, with $z$ the side opposite that angle, $2(x^2 + y^2 - z^2) = plus.minus x y$, i.e.
$
2x^2 + epsilon x y + 2y^2 = 2z^2, quad epsilon = plus.minus 1.
$
(For $(6,7,8)$: the angle opposite $8$ has cosine $21\/84 = 1\/4$.) Each equation is a conic through $(x : y : z) = (1 : 0 : 1)$, and the chord of slope $-p\/q$ parametrises all rational points:
$
(x, y, z) tilde (2(p^2 - q^2), space p(4q - epsilon p), space 2p^2 - epsilon p q + 2q^2),
$
with $gcd(p, q) = 1$, $q < p$, plus $4q > p$ when $epsilon = +1$ for positivity. The parametrised perimeter is $(4 - epsilon) p (p + q)$, and the content gcd of the triple always divides $30$, so enumerating $(4 - epsilon) p(p + q) <= 30 P$ captures every primitive fortunate triangle of perimeter at most $P$. The two families are merged and deduplicated — a triangle can be fortunate at several vertices — and each primitive contributes $"per" dot K(K+1)\/2$ scalings with $K = floor(P\/"per")$. The parametrisation reproduces the exact brute-force primitive sets, $S(P)$ agrees with brute force for $P <= 1000$ (including the given $S(10) = 24$, $S(100) = 3331$), and $S(10^7) = 134222859969633$ emerges from $1787465$ primitives in under ten seconds.

#pagebreak()
#link("https://projecteuler.net/problem=920")[= Problem 920: Tau Numbers]

Solution: 1154027691000533893

$m(k)$ is the least $x$ with $tau(x) = k$ and $k divides x$. Writing $x = product p_i^(e_i)$, the multiset ${e_i + 1}$ is a factorization of $k$ into parts $>= 2$. The divisibility constraint says $v_p (x) >= v_p (k)$ for every prime $p divides k$, so each such _required_ prime must occupy an exponent slot of size at least $v_p (k)$; the remaining exponents are assigned in decreasing order to the smallest primes not dividing $k$ — optimal by the rearrangement inequality once the required assignment is fixed, and that assignment is searched exhaustively with pruning. This explains shapes like $m(5) = 5^4 = 625$, where the constraint forces the prime $5$ in place of $2$, or $m(16) = 2^7 dot 3 = 384$ rather than the unconstrained minimum $120$.

Two bounds make the sweep finite: $k divides x$ implies $m(k) >= k$, so only $k <= 10^n$ matter; and $tau(x) <= 41472$ for all $x <= 10^16$ (the largest highly composite number below $10^16$, about $8.09 dot 10^15$, has $41472$ divisors), so $k <= 50000$ is exhaustive for $M(16)$. The construction is verified against a direct $tau$ sieve up to $10^6$ — both the $m(k)$ values found there and the non-existence of all others — and reproduces $m(8) = 24$, $m(12) = 60$, $m(16) = 384$ and the given $M(3) = 3189$. The total $M(16) = 1154027691000533893$ comes from $1355$ existing $m(k)$ values.

#pagebreak()
#link("https://projecteuler.net/problem=921")[= Problem 921: Golden Recurrence]

Solution: 378401935

The map $x |-> x(x^4 + 10x^2 + 5)\/(5x^4 + 10x^2 + 1)$ is the quintuple-argument formula for $coth$: $coth(5t)$ equals exactly that rational function of $c = coth t$. Writing $coth t = (u + 1)\/(u - 1)$ with $u = e^(2t)$, quintupling $t$ means $u |-> u^5$. Since $a_0 = phi = (phi^3 + 1)\/(phi^3 - 1)$ (using $phi + 1 = phi^2$), we get $u_0 = phi^3$ and
$
a_n = (phi^m + 1)/(phi^m - 1), quad m = 3 dot 5^n.
$
With $phi^m = (L_m + F_m sqrt(5))\/2$ and $L_m^2 - 5F_m^2 = -4$ for odd $m$, rationalising gives $a_n = (F_m sqrt(5) + 2)\/L_m$, i.e. $p_n = F_m\/2$ and $q_n = L_m\/2$ (integers since $3 divides m$). Check: $m = 3$ gives $phi$ and $s(0) = 1 + 32 = 33$. The closed form is verified against the literal recurrence by exact arithmetic in $QQ(sqrt(5))$ for $n <= 3$.

So $s(F_i)$ needs Fibonacci and Lucas numbers at the colossal index $k = 3 dot 5^(F_i)$, reduced modulo $M = 398874989$ (prime). The Pisano period is $pi(M) = 199437494 = 2 dot 99718747$, coprime to $5$, so $k mod pi(M) = 3 dot 5^(F_i mod "ord")$ where $"ord" = "ord"_(pi(M))(5) = 99718746$. A single pass over $i = 2, dots, 1618034$ carries $F_i$ modulo $"ord"$ and evaluates each term by fast-doubling Fibonacci mod $M$; the pipeline agrees with exact big-integer evaluation for all $F_i <= 8$ and gives $S(1618034) equiv 378401935$ in well under a minute.

#pagebreak()
#link("https://projecteuler.net/problem=922")[= Problem 922: Young's Game A]

Solution: 858945298

This is a partizan game: Right (moving first; "Left" in CGT conventions) moves a token rightwards within its row, Down moves it downwards within its column, and whoever cannot move loses. Computing canonical forms with a small combinatorial-game-theory engine (domination and reversibility simplification, comparison via the standard $<=$ recursion) reveals that every $(a, b, k)$-staircase, token at the origin, has value
$
G(a, b, k) = (b - a) + ast(k - 1),
$
a number plus a nimber: the surplus of horizontal over vertical moves contributes the integer $b - a$, while each frontier step beyond the first contributes one unit of nim-interaction. The formula is verified by exact canonical-form computation for every staircase of weight at most $6$ plus larger spot checks such as $(2,4,3)$ and $(1,2,7)$.

A disjunctive sum of such games equals $sum (b_i - a_i) + ast(j_1 xor dots xor j_m)$ with $j_i = k_i - 1$, and the first player wins iff the total is positive or fuzzy: $sum d_i > 0$, or $sum d_i = 0$ with nonzero XOR. Counting ordered $m$-tuples therefore needs the joint $(d, j)$ distribution over staircases of weight $<= w$ raised to the $m$-th convolution power — ordinary convolution along $d$, XOR-convolution along $j$, the latter diagonalised by a Walsh–Hadamard transform over $j < 64$ (here $j <= 62$). The answer is $A + B_0 - B_0^(xor = 0)$ counting $sum d > 0$, $sum d = 0$, and $sum d = 0$ with zero XOR respectively. The givens $R(2, 4) = 7$ and $R(3, 9) = 314104$ are reproduced, and $R(8, 64) equiv 858945298 (mod 10^9 + 7)$.

#pagebreak()
#link("https://projecteuler.net/problem=923")[= Problem 923: Young's Game B]

Solution: 740759929

The single-square variant of Problem 922. Canonical-form computation reveals a periodic closed form: with $r = (k b) mod (a + b)$,
$
G(a, b, k) = cases(
  "the number" r - a & "if" r != 0\,,
  "the switch" {b - 1 | 1 - a} & "if" r = 0\,
)
$
the switch case occurring exactly when $(a + b)\/gcd(a, b)$ divides $k$ (degenerating to $ast$ for $a = b = 1$). The formula is verified by exact canonical-form computation for every staircase of weight at most $10$ plus higher-weight spot checks.

A sum of numbers and switches resolves by the classical hottest-switch rule: with switches sorted by temperature $t = (a + b - 2)\/2$ and mean $mu = (b - a)\/2$, the first player's score is $V = sum "numbers" + sum mu_i + t_1 - t_2 + t_3 - dots$, after which the player on move at the integer $V$ loses iff $V = 0$. Hence Right wins iff $V > 0$, or $V = 0$ with an odd number of switch components — a rule verified against the engine on all small sums from a value zoo. For the count, switch classes $(a + b, b - a)$ are processed in decreasing temperature; equal temperatures commute in the alternating sum, and a block of $m'$ equal-temperature switches added after $s$ existing switches contributes $2t dot (plus.minus 1 "if" m' "odd, else" 0)$ by the parity of $s$. A DP over (slots filled, switch parity, $2V$) with binomial slot choices and class-count powers counts all ordered $8$-tuples; number classes join at the end with no rank interaction. The givens $S(2, 4) = 7$ and $S(3, 9) = 315319$ are reproduced, and $S(8, 64) equiv 740759929 (mod 10^9 + 7)$.

#pagebreak()
#link("https://projecteuler.net/problem=924")[= Problem 924: Larger Digit Permutation II]

Solution: 811141860

$a_n$ has about $2^n$ digits, but $B$ only rearranges a suffix: $B(a_n) = a_n + Delta_n$ where $Delta_n$ depends on the digits up to the pivot (the first place $q$ with $d_q < d_(q-1)$). So $U(N) = sum (a_n mod p) + sum Delta_n$ over $n$ with $B != 0$ (only $n = 1, 2$ fail). The $a$-part follows from the $rho$ cycle of $x |-> x^2 + 2$ mod $p$.

For the $Delta$-part, the orbit mod $10^K$ has period $pi_K = 8 dot 5^(K-2)$: 2-adically $a_n$ converges to a root of $x^2 - x + 2$ (so high powers of $2$ stabilise), while 5-adically the cycle multiplier is $equiv 1$, so each deeper digit advances through an arithmetic progression per revolution. Fixing $K_0$, every $n >= W_0$ falls into a class $n_0 + t pi$; the low $K_0$ digits — hence usually the pivot and $Delta$ — are constant on the class. Exceptional classes (low digits weakly increasing, no pivot) are resolved via deep digits: the return map $T = f^pi$ is 5-adically translation-like, so Mahler/binomial interpolation gives
$
a_(n_0 + t pi) equiv sum_(j <= j_max) binom(t, j) Delta^j (a_(n_0)) space (mod 10^40),
$
where the $j$-th finite difference has $5$-valuation $>= j(K_0 - 1) + 1$ and vanishes mod $2^40$; $j_max = ceil(39\/(K_0 - 1))$ suffices, asserted by reproducing $T^(j_max + 1)$ exactly. The digits then depend on $t$ only through $t mod 5^m$, so a base-$5$ branch tree over $t$ resolves every pivot with exact class counts.

Validation: exact big-integer brute force for $N <= 22$ (including the given $U(10) = 543870437$) and a per-term reference up to $N = 3 dot 10^5$ across several $K_0$, exercising all machinery; the production answer agrees for $K_0 = 10$ and $11$, giving $U(10^16) equiv 811141860$ in about twenty seconds.

#pagebreak()
#link("https://projecteuler.net/problem=925")[= Problem 925: Larger Digit Permutation III]

Solution: 400034379

$B(n^2) = n^2 + Delta$ where $Delta$ only rearranges the suffix of $n^2$ up to its pivot (first place $q$ with $d_q < d_(q-1)$), so $T(N) = sum n^2 + sum Delta_n$ minus corrections for $B = 0$. The first part is $N(N+1)(2N+1)\/6$.

For the $Delta$-part with $N = 10^16$, the pivot at place $q$ is determined by $n mod 10^(q+1)$, and since $10^(q+1) | N$ every residue class contributes _exactly_ $10^(15-q)$ values of $n$. A DFS over $n$-residue classes mod $10^(j+1)$ whose square digits $d_0 .. d_(j-1)$ weakly increase upward enumerates all pivot configurations; each pivot leaf at depth $q <= 14$ adds $Delta dot 10^(15-q)$. Children digits follow $d = (b + 2 r c) mod 10$, so classes with $r equiv 0 mod 5$ extend all ten children with one digit, and the suffix multiset, prefix value mod $p$, and $Delta$ (smallest suffix digit above the pivot, suffix re-sorted ascending) are maintained incrementally along the path. At depth $15$ the DFS switches to member enumeration: $n = r + t dot 10^15$ with the remaining digits read from $D = n^2 div 10^15 = (r^2 div 10^15) + 2 r t + t^2 dot 10^15$, which fits in $64$ bits; each member resolves its pivot directly, or proves its square fully non-increasing ($B = 0$, remove its $n^2$ term). The only contamination in the class stage comes from squares with fewer than $15$ digits that are fully non-increasing: their path acquires a fake pivot with an artificial zero digit at place $"len"(n^2)$ — impossible for any other member of the class — so subtracting the fake $Delta$ and the $n^2$ term per such (tiny) $n$ makes the count argument exact.

Validated per-term against brute force for $N = 10^2 .. 10^7$ (including the given $T(10) = 270$, $T(100) = 335316$); the class tree holds about $7 dot 10^8$ nodes and the full run takes a few minutes.

#pagebreak()
#link("https://projecteuler.net/problem=926")[= Problem 926: Total Roundness]

Solution: 40410219

The roundness of $n$ in base $b$ is $v_b (n) = max{k : b^k | n}$, so total roundness counts pairs $(b, k)$ with $b >= 2$, $k >= 1$, $b^k | n$:
$
R(n) = sum_(k >= 1) \#{b >= 2 : b^k | n} = sum_(k >= 1) (product_p (floor(e_p / k) + 1) - 1),
$
since the valid $b$ correspond to choosing each prime exponent at most $floor(e_p\/k)$, excluding $b = 1$. For $n = N!$ the exponents are Legendre's $e_p = sum_i floor(N\/p^i)$. Sorting them in decreasing order, the $k$-th term is a product over the prefix with $e_p >= k$, so the total work is $sum_p e_p = sum_(q "prime power") floor(N\/q) approx N log log N approx 3 dot 10^7$ for $N = 10^7$. Verified against direct base-by-base counting for $n = 20$ and $n = 10!$ (the given $R = 6$ and $312$) and random $n$.

#pagebreak()
#link("https://projecteuler.net/problem=927")[= Problem 927: Prime-ary Tree]

Solution: 207282955

From $t_k (n+1) = t_k (n)^k + 1$, $m in S_k$ iff the orbit of $1$ under $x |-> x^k + 1 mod m$ hits $0$. The key reduction: if $gcd(e, lambda) = 1$ with $lambda = "lcm"(ell_i - 1)$ over the primes $ell_i | m$ ($m$ squarefree), then $x |-> x^e$ is a bijection on each $ZZ\/ell_i$ (it fixes $0$ and permutes the units), so $x |-> x^e + 1$ is a _permutation_ of $ZZ\/m$. Permutations have no tails, hence $0$ is periodic and the orbit of $1 = f(0)$ necessarily returns to $0$. Since $gcd(p mod lambda, lambda) = gcd(p, lambda)$, a prime exponent can violate this only when $p | lambda$:
$
m in S quad <==> quad "orbit hits" 0 "for every prime" p | lambda(m).
$
This turns infinitely many tests into a handful. A Brent-cycle scan over all primes up to $10^7$ (testing just the primes dividing $ell - 1$) leaves $28$ S-primes: $2, 5, 149, 293, 1601, 45197, dots$. $S$ is closed under divisors, the square of every S-prime with $q^2 <= 10^7$ already fails the exponent-$2$ test, so $S$ consists of squarefree products of S-primes; the $63$ candidate products $<= 10^7$ are each tested against the primes dividing $"lcm"(ell_i - 1)$, leaving $92$ elements in total. Validated with the given $R(20) = 18$ and $R(1000) = 2089$, the latter also reproduced by brute intersection of $S_p$ over all $p < 2000$.

#pagebreak()
#link("https://projecteuler.net/problem=928")[= Problem 928: Cribbage]

Solution: 81108001093

Suits never affect either score, so a hand is a rank-count vector $(c_1, dots, c_13)$, $c_r in {0, dots, 4}$, weighted by $product binom(4, c_r)$. We count vectors with hand score $=$ cribbage score by a DP over ranks from king down to ace, tracking the difference $D = "crib" - "hand"$ together with exactly what the remaining ranks need: the length and count-product of the currently open run of consecutive present ranks (a gap closes it, scoring $"len" times "prod"$ when $"len" >= 3$ — precisely the "locally maximum runs" rule), and the fifteen profile $f[1..14]$ counting card subsets of the processed suffix by value sum (adding $j$ cards of value $v$ completes $binom(c, j) f[15 - j v]$ fifteens worth $2$ each). Pairs add $2 binom(c, 2)$ immediately and the hand score subtracts $c dot min(r, 10)$.

Both scores only grow and the hand score is at most $340$, so any state whose $D$ plus pending run score exceeds the maximum remaining hand score is dead — this kills the run-product explosion of dense low hands, which is also exactly why the surviving fifteen profiles stay small. Entries $f[s]$ that no remaining card values can complete are zeroed, collapsing states near the end. Validated against direct enumeration of all $5^R$ count vectors for reduced decks with ranks $1..R <= 6$ and on both worked examples; the full deck takes about ninety seconds.

#pagebreak()
#link("https://projecteuler.net/problem=929")[= Problem 929: Odd-Run Compositions]

Solution: 57322484

A composition with all maximal runs of odd length is a sequence of blocks (value $v$, odd multiplicity) in which adjacent blocks have different values — exactly a Smirnov word over the alphabet of blocks. With block weight $R_v (x) = x^v\/(1 - x^(2v))$, the Smirnov formula gives
$
F(x) = 1/(1 - sum_v R_v/(1 + R_v)) = 1/(1 - sum_v x^v/(1 + x^v - x^(2v))).
$
Since $1\/(1 + y - y^2) = sum_k (-1)^k F_(k+1) y^k$ (signed Fibonacci), the subtracted series has coefficients $g[n] = sum_(d | n) (-1)^(d-1) F_d$, filled by a harmonic sieve in $O(N log N)$; then $F = 1\/(1 - G)$ via the $O(N^2)$ convolution recurrence $f[n] = sum_k g[k] f[n-k]$. Validated against a direct recursive count for $n <= 30$, including the given $F(5) = 10$.

#pagebreak()
#link("https://projecteuler.net/problem=930")[= Problem 930: The Gathering]

Solution: 1.345679959251e12

Track the differences $x_k - x_1$: the process is a random walk on the abelian group $G = ZZ_n^(m-1)$ — moving ball $1$ adds $minus.plus (1, dots, 1)$, moving ball $k$ adds $plus.minus e_(k-1)$, each with probability $1\/(2m)$ — and it stops exactly when the walk hits $0$. For an irreducible walk on a finite abelian group whose only character with eigenvalue $1$ is trivial (true here; the eigenvalue $-1$ for even $n, m$ is harmless), the fundamental-matrix identity gives $EE_x [T_0] = sum_(v != 0) (1 - chi_v (x))\/(1 - hat(mu)(v))$ with $hat(mu)(v) = (cos(2 pi s\/n) + sum_k cos(2 pi v_k\/n))\/m$, $s = sum v_k$. A uniformly random initial configuration makes the difference vector uniform on $G$, so $EE[chi_v (x)] = 0$ for $v != 0$ and
$
F(n, m) = sum_(v in ZZ_n^(m-1) \\ {0}) 1/(1 - hat(mu)(v)).
$
$hat(mu)$ depends only on the multiset of the $v_k$, so the sum groups by count vectors with multinomial weights — $binom(n+m-2, m-1)$ terms instead of $n^(m-1)$. Since $1 - hat(mu) >= 2(1 - cos(2 pi\/n))\/m$ the positive sum is numerically tame; mpmath at $35$ digits reproduces all six given values (including $G(6,6) = 1.681521567954 dot 10^4$ to every printed digit) and evaluates $G(12,12)$ in half a minute.

#pagebreak()
#link("https://projecteuler.net/problem=931")[= Problem 931: Totient Graph]

Solution: 128856311

An edge from $b$ to $p b$ has weight $phi(p b) - phi(b)$, equal to $(p-1)phi(b)$ when $p | b$ and $(p-2)phi(b)$ otherwise. Fixing $p^e || n$, the $b$ with $p b | n$ are $b = p^j m$, $m | n\/p^e$; the $j$-sum telescopes to $(p-1)p^(e-1) - 1 = phi(p^e) - 1$, and $sum_(m | k) phi(m) = k$ turns the $m$-sum into $n\/p^e$:
$
t(n) = sum_(p^e || n) (phi(p^e) - 1) dot n/p^e,
$
confirming $t(45) = 5 dot 5 + 3 dot 9 = 52$. Summing over $n <= N$ with $q = p^e$ and $m$ coprime to $p$: $T(N) = sum_q (phi(q) - 1)(S(N\/q) - p S(N\/(q p)))$ with $S(x) = x(x+1)\/2$. The $e >= 2$ prime powers and the $p S(N\/p^2)$ correction involve only $p <= sqrt(N)$; the bulk $sum_(p <= N) (p-2) S(floor(N\/p))$ groups by $w = floor(N\/p)$ using prime counts and prime sums at all division points $floor(N\/d)$ from a Lucy#sub[Hedgehog] sieve in $O(N^(3\/4))$ — counts exact, sums modulo $715827883$. Verified against direct divisor-graph computation for $n < 300$, the givens $T(10) = 26$, $T(100) = 5282$, and an spf-sieve brute force at $10^5, 10^6$; the full run takes eight seconds.

#pagebreak()
#link("https://projecteuler.net/problem=932")[= Problem 932: $2025$]

Solution: 72673459417881349

A $2025$-number $N$ splits into a leading part $a$ and a trailing part $b$ (with $b$ having a fixed digit length and no leading zero) such that $N = (a + b)^2$. Writing $s = a + b$, every such $N$ is simply $s^2$, so iterate over $s$ rather than over the parts: for each split position $k$, set $a = floor(N \/ 10^k)$ and $b = N mod 10^k$, and accept when $a + b = s$ and $b$ has exactly $k$ digits.

A cheap filter cuts the search by more than four-fifths. Since $10^k equiv 1 space (mod 9)$, we have $N = a dot 10^k + b equiv a + b = s space (mod 9)$; combined with $N = s^2$ this forces $s^2 equiv s$, i.e. $s equiv 0$ or $1 space (mod 9)$. Only those $s$ need be examined.

#pagebreak()
#link("https://projecteuler.net/problem=933")[= Problem 933: Paper Cutting]

Solution: 5707485980743099

A cut of a $w times h$ piece at $(a, b)$ yields four independent pieces, so the game is a disjunctive sum with Grundy values $G(w, h) = "mex"_(a,b) G(a,b) xor G(a,h-b) xor G(w-a,b) xor G(w-a,h-b)$, zero on strips; $C(w, h)$ counts cuts with XOR zero, and only widths $<= w - 1$ are referenced. Empirically every row $G(a, dot)$ with $a <= 122$ becomes _constant_, equal to $K_a$, beyond a transient $T_a$ (max $3016$, verified against a table built to $h = 8192$). For large $h$ this collapses everything: a cut with both $b >= T$ and $h - b >= T$ has XOR $K_a xor K_(w-a) xor K_a xor K_(w-a) = 0$ — every middle cut wins — while for $b <= B >= max T_a$ the XOR is $G(a,b) xor G(w-a,b) xor K_a xor K_(w-a)$, independent of $h$. Hence for $h >= 2B + 2$
$
C(w, h) = (w-1)(h - 1 - 2B) + 2 c_w (B),
$
exactly linear with slope $w - 1$. The answer sums exact $C$ values (four-fold orbit symmetry in $(a,b)$) up to a per-width threshold plus the arithmetic-series tail; linearity is asserted against exact counts at several $h$ past each threshold, and the givens $C(5,3) = 4$, $D(12,123) = 327398$ both check out.

#pagebreak()
#link("https://projecteuler.net/problem=934")[= Problem 934: Unlucky Primes]

Solution: 292137809490441370

$u(n) > p$ means $n mod q$ is a multiple of $7$ for every prime $q <= p$. For $q in {2, 3, 5, 7}$ the only multiple of $7$ in $[0, q)$ is $0$, so $210 | n$. Writing $n = 7j$ (with $30 | j$), for $q > 7$: $n mod q in 7 ZZ <==> j mod q <= floor((q-1)\/7)$ — an _initial interval_. With $X = floor(N\/7)$ and $A_p = \#{j <= X : 30 | j, j mod q <= m_q " for all " 7 < q <= p}$, telescoping over the value of $u$ gives
$
U(N) = 2N + sum_p ("nextprime"(p) - p) dot A_p (N).
$
The allowed residues form CRT classes; a DFS over primes $11, 13, dots$ accumulates exact class counts $floor((X-r)\/L) + 1$ per level while the class count stays small ($6.35$ million classes through $q = 43$, where $L approx 1.9 dot 10^15$ nears $X approx 1.4 dot 10^16$). Past that, every class has only a handful of members $<= X$ (about $5 dot 10^7$ integers in total); these are enumerated explicitly and streamed through the remaining primes until the survivor count hits zero around $q approx 90$. Validated against per-$n$ brute force for $N = 1470$ (the given $U = 4293$) up to $N = 10^8$; the full computation takes under a second.

#pagebreak()
#link("https://projecteuler.net/problem=935")[= Problem 935: Rolling Square]

*Answer: 759908921637225*

While rolling, the small square either lies flat on a wall or _bridges_ a corner of the big square with two adjacent corners — its edge spans the corner as a chord, so the contact distances $r, s$ from the big corner obey $r^2 + s^2 = b^2$. Between consecutive corners the wall budget reads $1 = s_k + m_k b + r_(k+1)$ with a unique integer $m_k >= 0$ ($m_k = 0$ is a direct corner-to-corner hop, possible only for $b > 1\/2$; $m_k >= 1$ means an exit rotation, $m_k - 1$ flat rolls, and a tilt-in). Substituting $r = b sin theta$, $s = b cos theta$, $c = 1\/b$ turns the orbit into the chain $sin theta_(k+1) + cos theta_k = c - m_k$.

The starting position is a _nestle_ (square seated in the corner, $theta = 0$), and the dynamics from a nestle is deterministic — so the orbit is a sequence of *identical nestle-to-nestle blocks*, each crossing $Delta$ corners in $P = M + Delta - 1$ steps where $M = sum m_k$, and rotating the square by $90 degree dot M$. The first return happens when a nestle lands back on the starting corner: $n(b) = (4\/gcd(Delta, 4)) dot (M + Delta - 1)$. This reproduces all five given examples ($b = 1\/2$: $Delta = 1$, $n = 4$; $b = 5\/13$: block $(1,1,2)$, $Delta = 3$, $n = 24$; …). Two structural facts tame the analysis: for $b > 1\/sqrt(2)$ the hop map $r mapsto 1 - sqrt(b^2 - r^2)$ has an attracting fixed point (the inscribed square) whose basin always captures the launch, so no returns exist there; and mirror/time-reversal symmetry forces every block's $m$-sequence to be a palindrome with end shift $m_(Delta - 1) = m_0 + 1$ (equivalently $theta_j + theta_(Delta - j) = 90 degree$).

Each chain is monotone in $c$, so each itinerary has at most one root. High-precision enumeration (validated against an exact simulator) reveals a clean bijection: *the return values of $b$ correspond exactly to the coprime pairs $(Delta, M)$*, one root each — though some roots are numerically extreme (the $(16, 15)$ block's $b$ differs from $1\/2$ by about $10^(-107)$, far beyond any direct search). Hence
$
F(N) = \#{(Delta, M) : gcd(Delta, M) = 1, (4\/gcd(Delta,4))(M + Delta - 1) <= N},
$
which splits by $Delta mod 4$ into three counts of coprime pairs with $Delta + M <= L$ for $L = N + 1$, $floor(N\/2) + 1$, $floor(N\/4) + 1$. Each is computed in $O(L)$ by Möbius inversion (for squarefree $d$, the condition $d | Delta$ induces a congruence on $Delta\/d$, leaving a closed-form arithmetic-progression sum). The checks $F(6) = 4$ and $F(100) = 805$ pass, and $F(10^8) = 759908921637225$ — incidentally $tilde 3N^2\/(4 pi^2)$, the Farey-density signature of the coprime-pair law. About 25 seconds, dominated by the Möbius sieve.

#pagebreak()
#link("https://projecteuler.net/problem=936")[= Problem 936: Peerless Trees]

*Answer: 12144907797522336*

Count unlabelled trees with no edge between two vertices of equal degree, via rooted generating functions that track the root's child count. Let $f_d (x)$ count rooted trees whose root has $d$ children and will be attached to a parent — its eventual degree is $d + 1$ — with every internal edge already satisfying the constraint. A child whose root has $c$ children carries degree $c + 1$, so a root-child edge is legal iff $c != d$, giving the elegant self-referential system $f_d = x dot "MSET"_d (T without F_d)$ where $T$ is the union of all classes. The multiset over a set difference is evaluated by one incremental knapsack DP per $d$: $"DP"_d [j][w]$ counts multisets of $j$ subtrees of total weight $w$ from classes $c != d$, folding in weight-$m$ objects (with multiset binomials $binom(a + j' - 1, j')$) once all $f_c [m]$ are known — legitimate because a multiset of weight $n - 1$ only ever uses subtrees smaller than $n$.

Unrooted counts follow from the dissymmetry theorem. A parentless root with $d$ children has degree $d$, so its children must avoid $c = d - 1$: conveniently the _same_ exclusion tables queried one level deeper, $V[n] = sum_d "DP"_(d-1)[d][n-1]$. Edge-rooted trees join two attached roots with $a$ and $b$ children where $a != b$ — so the two halves can never be isomorphic, no symmetric-edge correction exists, and $P(n) = V[n] - 1/2 sum (T T - sum_c f_c f_c)$ convolved. Validated against brute force over all non-isomorphic trees up to $n = 12$ plus the given $P(7) = 6$ and $S(10) = 74$; the whole computation takes a few seconds in pure Python big-integer arithmetic.

#pagebreak()
#link("https://projecteuler.net/problem=937")[= Problem 937: Equiproduct Partition]

*Answer: 792169346*

Write $s(z) = +1$ for $z in A$ and $-1$ for $z in B$. Indicator algebra converts the pair-balance condition $p(A, z) = p(B, z)$ into a divisor identity: summing $s$ over all factorisations $z = plus.minus d e$ and removing the diagonal gives
$
sum_(d | z) s(d) = [z = plus.minus w^2] dot s(w),
$
a recursion (over norm) that determines $s$ uniquely — which is precisely why the partition exists and is unique. Since $ZZ[sqrt(-2)]$ is a UFD with units ${plus.minus 1}$, the up-to-sign monoid $T$ is free abelian on primes, and per prime the recursion $sum_(j <= a) t_j = [a "even"] t_(a\/2)$ is exactly the Thue–Morse recursion $t_(2j) = t_j$, $t_(2j+1) = -t_j$. The unique solution is therefore the multiplicative function with *Thue–Morse signs on prime exponents*: $s(z) = product_pi (-1)^("popcount"(v_pi (z)))$. (Notably _not_ the Liouville function — plain $lambda$ fails at squares of $B$-elements.) This was confirmed by building the partition directly from the recursion for all 1332 elements of norm $<= 1200$ and checking the pair condition for every $z$: zero failures.

For $z = n!$ the splitting of rational primes in $ZZ[sqrt(-2)]$ does the rest: $p = 2$ ramifies ($2 tilde theta^2$, exponent $2 v_2 (n!)$, and $"popcount"(2v) = "popcount"(v)$); $p equiv 1, 3 (mod 8)$ splits into conjugate primes whose two equal exponents cancel mod 2; $p equiv 5, 7 (mod 8)$ stays inert. Hence $n! in A$ iff $sum_q "popcount"(v_q (n!))$ is even, summed over $q in {2} union {q equiv 5, 7 (mod 8)}$. Computationally, each relevant prime walks its multiples maintaining $v_q (k!)$ incrementally, XOR-ing parity changes into a flip array; a prefix XOR yields every membership bit while factorials accumulate mod $10^9 + 7$ — about $2.5 dot 10^8$ steps in total. Verified against $G(4) = 25$, $G(7) = 745$, and $G(100) equiv 709772949$.

#pagebreak()
#link("https://projecteuler.net/problem=938")[= Problem 938: Exhausting a Colour]

*Answer: 0.2928967987*

The both-black draw changes nothing, so condition it away: the embedded jump chain from state $(R, B)$ moves $R -> R - 2$ with probability $(R-1)\/(R-1+2B)$ and $B -> B - 1$ with probability $2B\/(R-1+2B)$ (unnormalised weights $R(R-1)$ and $2 R B$). Red's count only ever falls by two, so its parity is invariant — black can only win when $R$ is even. With absorption values $P(0, B) = 1$ and $P(R, 0) = 0$, the recurrence
$
P(R, B) = (R-1)/(R-1+2B) P(R-2, B) + (2B)/(R-1+2B) P(R, B-1)
$
is a straightforward DP over $B$ with a rolling array over even $R$: about $1.5 dot 10^8$ convex-combination float operations, numerically benign and comfortably accurate to ten decimals. Hand-check: $P(2,2) = 1/5 + 4/5 dot 1/3 = 7/15 = 0.4overline(6)$, and the other two givens reproduce exactly. Runs in about a second with numba.

#pagebreak()
#link("https://projecteuler.net/problem=939")[= Problem 939: Partisan Nim]

*Answer: 246776732*

Brute-forcing every position with at most 16 stones shows the outcome depends only on summary statistics, and threshold tables collapse to a remarkably clean criterion. Let $X = "stones" - "piles" = sum ("size" - 1)$ for each side and $Pi$ the total number of piles on the board. Then *A wins under both move orders iff $X_A >= X_B + 2$, or $X_A = X_B + 1$ with $Pi$ odd* — verified against the exact solver on all 17 345 settings up to 16 stones (ones are pure tempo; only the "excess" stones above one per pile carry weight, with a parity tiebreak).

For counting, strip one stone from every pile: a side becomes a partition $mu$ of $X$ plus a free pile count $m >= ell(mu)$ (surplus piles are 1-piles), with stones $= X + m$. Setting $c = X + ell(mu)$ and $H[X][c] = \#$partitions of $X$ into exactly $c - X$ parts, the surplus choices integrate to a triangular weight $"tri"(N - c_A - c_B)$, while the boundary case $X_A = X_B + 1$ needs $m_A + m_B$ odd, restricting the surplus parity to a half-triangle weight. The key kernels are thin: $H[X]$ is supported on $c in [X+1, 2X]$, so the diagonal sums $S(C) = sum_X (H[X] convolve H[X])(C)$ and $K_2(C) = sum_X (H[X+1] convolve H[X])(C)$ cost only $tilde N^3\/24$ operations, and the full off-by-two kernel comes free via $K_1 = (T - S)\/2 - K_2$ with $T = h convolve h$, $h[c] = \#{mu : |mu| + ell(mu) = c}$ (an Euler product). Everything assembles in about 8 seconds with numba; $E(1) dots E(16)$ all match brute force.

#pagebreak()
#link("https://projecteuler.net/problem=940")[= Problem 940: Two-Dimensional Recurrence]

*Answer: 969134784*

Eliminating $A(m+1, ast)$ between the two recurrences forces the bottom row to obey $A(0, n+2) = A(0, n+1) + 3A(0, n)$, and the separable ansatz $A = x^m y^n$ is consistent precisely when $x = y + 1$ and $y^2 = y + 3$. With roots $y_(1,2) = (1 plus.minus sqrt(13))\/2$ and the boundary values $A(0,0) = 0$, $A(0,1) = 1$, the unique solution is the two-dimensional Lucas-style closed form
$
A(m, n) = (x_1^m y_1^n - x_2^m y_2^n) / sqrt(13), quad x_i = y_i + 1,
$
which reproduces the entire recurrence table (and the given $2, 5, 7, 16$). The double sum over Fibonacci indices then *factorises*: $S(k)$ is the difference of $(sum_i x_1^(f_i))(sum_j y_1^(f_j))$ and its Galois conjugate, divided by $sqrt(13)$ — i.e. just twice the $sqrt(13)$-component of one product. Working in $FF_p [sqrt(13)]$ with $p = 1123581313$ as pairs $a + b sqrt(13)$, the exponents up to $f_50 approx 1.26 dot 10^10$ need only square-and-multiply. Milliseconds of computation; $S(3) = 30$ and $S(5) = 10396$ check out.

#pagebreak()
#link("https://projecteuler.net/problem=941")[= Problem 941: de Bruijn's Combination Lock]

Solution: 1068765750

The shortest button sequence containing every length-$n$ combination has length $k^n + n - 1$: it is a de Bruijn cycle opened up, with the first $n-1$ digits repeated at the end. By the theorem of Fredricksen and Maiorana, the lexicographically smallest de Bruijn cycle is the concatenation, in lexicographic order, of every Lyndon word over ${0, dots, k-1}$ whose length divides $n$; opening it at its minimal rotation (the canonical start, since the sequence begins $0^n 1 dots$) gives $C(k, n)$, which reproduces $C(3,2) = 0010211220$. So we must find, for $10^7$ pseudorandom $12$-digit combinations, the order in which they occur in this Lyndon concatenation for $k = 10$, $n = 12$ — without, of course, building the $10^12$-digit sequence.

== Position order without positions

The occurrence of $w$ starts inside the canonical occurrence of some Lyndon word $L$ at offset $i < |L|$, and its position is $S(L) + i$ where $S(L)$ is the total length of all Lyndon words smaller than $L$. Since consecutive Lyndon words tile the sequence, the intervals $[S(L), S(L) + |L|)$ are exactly consecutive blocks: position order is *lexicographic order of the pair $(L, i)$*, with the usual prefix rule for comparing Lyndon words of different lengths. The ranking machinery for computing $S(L)$ itself (Möbius-counting words with small rotations) is never needed — the places $p_n$ come from sorting $10^7$ keys, each a base-$11$ right-padded encoding of $L$ (so the prefix rule survives) combined with $i$, fitting comfortably in $64$ bits.

== Locating the occurrence

Finding $(L, i)$ for a given $w$ uses the constructive proof of the Fredricksen–Maiorana theorem (in the formulation of Kociumaka, Radoszewski and Rytter). Write $w = (alpha beta)^d$ where $beta alpha = lambda$ is the Lyndon root of the minimal rotation of $w$ and $|alpha|$ is the rotation offset. Then $w$ occurs as a factor of $lambda' lambda lambda''$ (predecessor and successor in the divisor-length Lyndon order), *except* when $alpha$ is a nonempty run of $9$s and $d = 1$, in which case $w$ sits around $hat(lambda) =$ the largest Lyndon word below $beta$, computable as the primitive root of the largest self-minimal word below $beta 0^(|alpha|)$ (truncate-decrement-fill candidates $v_(1..j-1) (v_j - 1) 9^(n-j)$, take the largest self-minimal one). The fully degenerate $w = 9^j 0^(12-j)$ wraps around the seam $dots 8 9^11 | 9 | 0 | 0^11 1 dots$. Successors come from the classic FKM step (increment the last non-$9$ of the length-$n$ periodic extension, keep when the new length divides $n$), predecessors from the same largest-self-minimal-below routine. In every case a window of a few consecutive Lyndon words around the candidate is assembled and $w$ is matched inside it; since each length-$12$ word occurs exactly once in the cycle, any match found in a genuine factor *is* the occurrence, so the case analysis only needs to guarantee coverage, not exclusivity.

The decoder was verified exhaustively against explicitly built de Bruijn sequences for eight small $(k, n)$ pairs, and $F(2)$, $F(10)$ match the given values. The $10^7$ keys take a few seconds in parallel (the per-word work is $O(n^2)$ with tiny constants), the sort is immediate, and $F(10^7) equiv 1068765750 mod 1234567891$.

#pagebreak()
#link("https://projecteuler.net/problem=942")[= Problem 942: Mersenne's Square Root]

Solution: 557539756

We need the smallest $x$ with $x^2 equiv q (mod p)$ for $p = 2^q - 1$ and $q = 74207281$, a Mersenne prime of 22 million digits. Any generic square-root method is doomed: even the one-liner $x = q^((p+1)\/4)$ (valid since $p equiv 7 mod 8$) means $q - 2$ squarings of a $q$-bit number.

The structure of $p$ collapses the problem. Since $2^q equiv 1 (mod p)$ and $q$ is prime, $zeta = 2$ is a *primitive $q$-th root of unity in $FF_p$*, so the classical quadratic Gauss sum over the prime $q$ can be evaluated inside $FF_p$ itself:
$
g = sum_(t=1)^(q-1) (t/q) thin 2^t (mod p), quad g^2 = ((-1)/q) q = q,
$
where $(t/q)$ is the Legendre symbol and the last equality holds because $q equiv 1 (mod 4)$. The two square roots of $q$ are exactly $plus.minus g$, and $R(q) = min(g, p - g)$.

Computationally $g$ is just a $q$-bit binary number determined by the quadratic-residue pattern modulo $q$: marking the residues takes $(q-1)\/2$ modular squarings, the residue and non-residue index sets are packed into two big integers $A$ and $B$, and $g = A - B$ (plus $p$ if negative — since $|A - B| < p$, no big-integer division ever happens). The whole computation, on numbers of $74$ million bits, runs in under two seconds. The construction is verified against $R(5) = 6$ and $R(17) = 47569$ and against brute force for every Mersenne prime exponent $q equiv 1 (mod 4)$ up to $13$; the answer is $R(74207281) mod (10^9 + 7) = 557539756$.

#pagebreak()
#link("https://projecteuler.net/problem=943")[= Problem 943: Self Describing Sequences]

Solution: 1038733707

$S(a,b)$ is the generalized Kolakoski sequence: its runs alternate between the values $a$ and $b$ starting with $a$, and the sequence of run lengths is the sequence itself. Since every term is $a$ or $b$, the prefix sum is $T(a,b,N) = b N + (a-b) n_a$ where $n_a$ counts the $a$'s among the first $N$ terms, so the whole problem reduces to counting $a$'s in a prefix of length $N = 22332223332233$ for each of the $49062$ ordered pairs.

The self-description makes $S$ the fixed point of run-length expansion: replacing term $i$ of $S$ by a run of $S_i$ copies of $a$ or $b$ (according to the parity of $i$) reproduces $S$. Iterating this, a short explicit prefix of $4096$ letters, expanded enough times, covers any position up to $N$, and $n_a$ is obtained by descending this expansion tree: at each level the descent consumes the whole subtrees lying entirely left of the cut position and recurses into the one subtree that straddles it. Subtrees are normalized into chunks of $32$ letters. The summary of a chunk's full expansion through $d$ levels — its exact bottom-level length, its exact count of $a$'s, and the parity of its total length at every intermediate level — is computed by expanding one level, re-cutting into $32$-letter chunks, and combining the children's summaries; results are memoized.

The subtlety is that a chunk's expansion is not determined by its letters alone: the values appearing one level down depend on the absolute positional parity at that level, and those parities at deeper levels depend on the exact lengths, modulo $2$, of everything expanded to the chunk's left. The memo key therefore includes a parity context, one bit per level below, threaded left to right across sibling chunks using the length parities each summary returns. When $a$ and $b$ have the same parity these context bits are forced and the memo stays tiny, which reflects the fact that such sequences are fixed points of ordinary substitutions. Mixed-parity pairs are the genuinely hard case — the same obstruction that makes the classical Kolakoski sequence resistant to analysis — but, in the spirit of Brent and Osborn's Kolakoski algorithms, the number of distinct (chunk, context) keys that ever arises in one computation grows empirically like $N^(0.43)$: about $8$ million for the worst pair $(2,3)$, around $10^5$ when $a+b approx 13$, and only hundreds once $a+b$ exceeds $100$, because the sequence's factor complexity is low and only few parity contexts are reachable per factor. Summing $b N + (a-b) n_a$ over all pairs modulo $2233222333$ takes under four minutes, dominated entirely by the handful of smallest mixed-parity pairs.

The implementation is verified against direct generation of the sequences out to $2 dot 10^9$ terms for a spread of mixed- and same-parity pairs, and reproduces the given values $T(2,3,10) = 25$, $T(4,2,10^4) = 30004$ and $T(5,8,10^6) = 6499871$.

#pagebreak()
#link("https://projecteuler.net/problem=944")[= Problem 944: Sum of Elevisors]

Solution: 1228599511

An element $x$ of a set $E$ is an elevisor when it divides some other element of $E$, and $S(n)$ sums, over all $2^n$ subsets of ${1, dots, n}$, the total of each subset's elevisors. Swapping the order of summation turns this into a question about each value $x$ separately: in how many subsets is $x$ an elevisor? The multiples of $x$ in range, other than $x$ itself, number $m = floor(n\/x) - 1$, and $x$ is an elevisor of $E$ exactly when $E$ contains $x$ together with at least one of them. Of the $2^(n-1)$ subsets containing $x$, exactly $2^(n-1-m)$ avoid every such multiple, so

$ S(n) = sum_(x=1)^n x (2^(n-1) - 2^(n-1-m)) = 2^(n-1) (n(n+1))/2 - 2^n sum_(x=1)^n x thin 2^(-floor(n\/x)). $

The remaining sum succumbs to the classic divisor-block decomposition: $floor(n\/x)$ takes only $O(sqrt(n))$ distinct values $q$, and within the block of $x$ sharing one value the inner sum of $x$ is an arithmetic series. For $x < sqrt(n)$ each term gets its own modular exponentiation; for $q < sqrt(n)$ the factor $2^(-q)$ is extended by one multiplication per step. The modulus $1234567891$ is prime, so exponents reduce modulo $1234567890$ and the inverse powers of two come from Fermat's little theorem. About $2 dot 10^7$ blocks are processed in under two seconds, and the method is verified against a brute-force enumeration of all subsets for $n <= 12$, including the given $S(10) = 4927$.

#pagebreak()
#link("https://projecteuler.net/problem=945")[= Problem 945: XOR-Equation C]

Solution: 83357132

The XOR-product is exactly multiplication in $FF_2 [x]$, reading the binary expansion of an integer as a polynomial over $FF_2$. In characteristic $2$ squaring is the Frobenius endomorphism, so $(a+b)^2 = a^2 + b^2$, and the equation $a^2 + x a b + b^2 = c^2$ rearranges to $(c + a + b)^2 = x a b$. Squares in $FF_2 [x]$ are precisely the polynomials whose exponents are all even, and squaring is injective, so each pair $(a, b)$ contributes exactly one solution $c = a xor b xor sqrt(x a b)$ — and contributes it precisely when $x a b$ is a square. Only $a$ and $b$ are bounded by $N$; the value of $c$ is free.

Factor out the powers of $x$: write $a = x^alpha a'$ and $b = x^beta b'$ with $a', b'$ of nonzero constant term, i.e. odd integers. Then $x a b = x^(alpha + beta + 1) a' b'$ is a square exactly when $alpha + beta$ is odd and $a' b'$ is a square, and by unique factorization the latter happens exactly when $a'$ and $b'$ have the same squarefree part (the product of their irreducible factors of odd multiplicity). The pairs with $a = 0$ always work, with $c = b$. Therefore $F(N) = (N+1) + sum c_0 (s) thin c_1 (s)$, summed over squarefree-part classes $s$, where $c_0$ and $c_1$ count the integers in $[1, N]$ of that class whose number of trailing zero bits is even respectively odd. Checking the toy case by hand, the classes of ${1, dots, 10}$ give $9 + 1$ cross-parity pairs on top of the $11$ pairs with $a = 0$, matching $F(10) = 21$.

Squarefree parts for all odd polynomials up to $10^7$ come from a carryless sieve recording one irreducible factor of each composite (cost $sum_d 2^d \/ d dot 10^7 \/ 2^d approx 3 dot 10^7$ carryless products), followed by a DP along increasing integers that, for $n = pi times.circle m$, takes the stored squarefree part of $m$ and multiplies or divides out $pi$ according to whether $pi$ already appears in it. A single pass over $n <= N$ then accumulates the cross-parity pair counts in two arrays indexed by squarefree part. The whole computation runs in under three seconds and is verified against a brute force over all pairs, evaluating the defining carryless equation directly, for $N <= 300$.

#pagebreak()
#link("https://projecteuler.net/problem=946")[= Problem 946: Continued Fraction Fraction]

Solution: 585787007

The coefficients of $beta = (2 alpha + 3)\/(3 alpha + 2)$ can be produced directly from the coefficients of $alpha$ without ever evaluating either number, by Gosper's continued-fraction arithmetic. The state is the integer Möbius matrix applied to the unread tail $t$ of $alpha$'s expansion, $beta_"tail" = (p t + r)\/(q t + s)$, where $t$ always lies in the open interval $(1, oo)$. Reading the next coefficient $a$ of $alpha$ multiplies the matrix on the right by $mat(a, 1; 1, 0)$. Whenever the integer part of the value is the same at both ends of $t$'s range — concretely $q >= 1$, $q + s >= 1$ and $floor(p\/q) = floor((p+r)\/(q+s))$ with exact integer floor division — that common floor $q_0$ is the next coefficient of $beta$: subtracting it and inverting replaces the matrix by $mat(q, s; p - q_0 q, r - q_0 s)$. Since $beta$ is irrational the bracketing interval shrinks past every integer boundary eventually, so the process never stalls, and the conservative endpoint test never emits a wrong digit. The determinant stays $plus.minus 5$ for the whole run and, because $alpha$'s coefficients are all $1$ or $2$, the four entries remain tiny, so plain 64-bit arithmetic suffices.

The input side is a three-state machine emitting $alpha = [2; 1,1,2,1,1,1,2,dots]$ with runs of $1$'s of consecutive prime lengths. Roughly one input coefficient is consumed per output coefficient, so primes up to a few hundred thousand more than cover $10^8$ outputs; the whole run takes about two seconds. The emitter is verified against the given prefix $[0;1,5,6,16,9,1,10,16,11]$ with sum $75$, and against an independent high-precision computation (mpmath at $60000$ bits) of $beta$'s first $3000$ coefficients.

#pagebreak()
#link("https://projecteuler.net/problem=947")[= Problem 947: Fibonacci Residues]

Solution: 213731313

The pair $(g(n), g(n+1))$ evolves under the matrix $Q = mat(0, 1; 1, 1)$ modulo $m$, so $p(a, b, m)$ is the orbit length of the vector $v = (a, b)$: the least $t$ with $(Q^t - I) v equiv 0$. Every such $t$ divides the Pisano period $pi(m)$, the order of $Q$ modulo $m$. Writing $K(e) = \#ker(Q^e - I mod m)$, Möbius inversion over the divisor lattice of $pi(m)$ collapses the double sum over $(a, b)$ to

$ s(m) = sum_(e | pi(m)) K(e) thin e^2 product_(ell | pi(m)\/e) (1 - ell^2). $

By CRT, $K$ is a product over the prime powers $q^c parallel m$ of local kernel sizes, each depending on $e$ only through $gcd(e, pi(q^c))$. For a $2 times 2$ integer matrix the kernel size mod $q^c$ is $gcd(s_1, q^c) gcd(s_2, q^c)$ with $s_1, s_2$ the Smith invariants, and $Q^e - I = mat(F_(e-1) - 1, F_e; F_e, F_(e+1) - 1)$ has $s_1 = gcd(F_e, F_(e-1) - 1)$ and determinant $(-1)^e + 1 - L_e$, so each local kernel is one Fibonacci computation. Three regimes make the whole thing fast. For primes $q > 1000$ with $5$ a quadratic residue ($q equiv plus.minus 1 mod 5$), $Q$ has unit eigenvalues $lambda, mu = (1 plus.minus sqrt(5))\/2$ in $FF_q$, each eigenline is fixed by $Q^e$ exactly when the eigenvalue's multiplicative order divides $e$, and $kappa_q (e) = q^([A | e] + [B | e])$ where the orders $A, B$ come from a Tonelli–Shanks square root of $5$ and order finding in the factored group of order $q - 1$. For $q > 1000$ with $5$ a non-residue, the eigenvalues are conjugate in $FF_(q^2)$ and $Q$ is semisimple, so the kernel is trivial for every proper divisor and jumps to $q^2$ exactly at multiples of $pi(q)$ (here the period divides $2(q+1)$ rather than $q + 1$, since $lambda^(q+1) = lambda mu = -1$). For $q <= 1000$ or $c >= 2$ — which covers $q = 2$ and $q = 5$ and every higher prime power below $10^6$ — kernel sizes are tabulated for every divisor of $pi(q^c)$ by Fibonacci fast doubling modulo $q^(2 c)$, kept 64-bit-safe by a 21-bit split multiplication, and looked up by binary search.

The main loop merges the factorizations of the local periods into $pi(m)$, walks its divisors $e$ with an odometer over exponent vectors — $36.6$ million divisors in total across all $m <= 10^6$ — and accumulates $K(e) e^2 J(pi\/e)$ modulo $999999893$, finishing in about nine seconds. The implementation is verified against brute-force orbit enumeration of $s(m)$ for every $m <= 60$ and for ten larger moduli with prime factors above $1000$ in both quadratic-character classes, and reproduces the given $s(3) = 513$, $s(10) = 225820$, $S(3) = 542$ and $S(10) = 310897$.

#pagebreak()
#link("https://projecteuler.net/problem=948")[= Problem 948: Left vs Right]

Solution: 1033654680825334184

Write $A(i,j)$ for "Left to move on $w[i..j]$ and Left wins" and $B(i,j)$ for the corresponding statement for Right. The game recursion is $A(i,j) = exists i' in (i, j]: not B(i', j)$ and $B(i,j) = exists j' in [i, j): not A(i, j')$, and both are monotone in the free endpoint — widening the range only adds options. So $A(dot, j)$ and $B(i, dot)$ are threshold sequences, $A(i,j) <=> i <= t_j$, and tracking how $t_j$ evolves as $j$ sweeps rightward exposes a stack process: an $L$ at position $j$ sets $t_j = j$ and pushes $j$; an $R$ pops the most recent surviving $L$, say at position $m$, and sets $t_j = m - 1$, or $t_j = -oo$ if no $L$ survives. This is precisely greedy bracket matching with $L$ as the opening symbol and $R$ as the closing one. The conclusion is a complete, purely combinatorial characterization: Left moving first wins exactly when the word ends in $L$ or its final $R$ is matched to an $L$ at position at least $1$; and by mirror symmetry Right moving first wins exactly when the word starts with $R$ or its first $L$ is matched to an $R$ at position at most $n - 2$. Greedy matching is left-right symmetric — reversing the word and swapping the letters reproduces the same matched pairs — so both conditions refer to a single matching of the word. The characterization was checked against full game-tree evaluation of every word of length up to $12$.

Counting words of length $60$ satisfying both conditions splits into four cases by the first and last letters. Words $R dots L$ always qualify: $2^(n-2)$ of them. Words $R dots R$ qualify when the final $R$ is matched, i.e. some $L$ is still unmatched after the first $n - 1$ letters — a one-dimensional DP on the stack size; words $L dots L$ mirror these. Words $L dots R$ need the final $R$ matched to something other than position $0$ and the leading $L$ matched strictly before the final position; carrying one extra bit — whether the position-$0$ $L$ still sits at the bottom of the stack — through the same DP handles both requirements. The whole computation is instantaneous and agrees with brute-force counts of $F(n)$ for all $n <= 22$, including the given $F(3) = 4$ and $F(8) = 181$.

#pagebreak()
#link("https://projecteuler.net/problem=951")[= Problem 951: A Game of Chance]

Solution: 495568995495726

A turn never crosses a run boundary (the optional second card must match the first in colour), so the deck is consumed run by run, and the number of turns spent on a run of length $r$ is an independent random variable $t(r)$: each step takes one card and, if at least two remain in the run, takes a second with probability $1\/2$. The first player wins iff $sum_i t(r_i)$ is odd, so with $c(r) = bb(E)[(-1)^(t(r))]$ the first player's win probability is $(1 - product_i c(r_i)) \/ 2$ by independence. From $t(r) = 1 + t(r - X)$,
$ c(r) = -(c(r-1) + c(r-2)) / 2, space c(0) = 1, space c(1) = -1, $
giving $c(2) = 0$, and (checking the integer sequence $d(r) = (-2)^r c(r)$ with $d(r) = d(r-1) - 2 d(r-2)$) $c(r) eq.not 0$ for every other $r <= 52$. Hence a configuration is fair iff it contains a maximal run of length exactly $2$.

Counting the complement: arrangements with no run of length $2$ are built from alternating-colour compositions of $n$ into parts $eq.not 2$; with $C_k$ the number of such compositions into $k$ parts, the no-run-of-2 count is $sum_k (2 C_k^2 + 2 C_(k+1) C_k)$, and $F(n) = binom(2n, n)$ minus that. Verified against exact game-value computation with rational arithmetic over all configurations for $n = 2..5$ and the given $F(2) = 4$, $F(8) = 11892$; the result is $F(26) = 495568995495726$.

#pagebreak()
#link("https://projecteuler.net/problem=952")[= Problem 952: Order Modulo Factorial]

Solution: 794394453

We need the multiplicative order of $p = 10^9 + 7$ modulo $n!$ for $n = 10^7$, reported modulo $p$. Since $n! = product q^(e_q)$ over primes $q <= n$ with $e_q$ given by Legendre's formula, the Chinese remainder theorem gives
$ R(p, n) = "lcm"_(q <= n) "ord"(p mod q^(e_q)). $

For each odd prime $q$, the order modulo $q$ is found by starting from $q - 1$ and repeatedly stripping any prime factor $f$ of $q - 1$ while $p^(d \/ f) equiv 1 space (mod q)$; a smallest-prime-factor sieve up to $10^7$ supplies the factorisations. Lifting the exponent then handles prime powers: with $v = v_q (p^("ord"_q) - 1)$,
$ "ord"(p mod q^e) = "ord"(p mod q) dot q^(max(0, e - v)), $
and $v > 1$ is rare (a Wieferich-style coincidence), so it is found by testing $p^("ord"_q) mod q^2, q^3, dots$ For $q = 2$ the group is nearly cyclic and the two-adic valuation $v_2(p^(2^j) - 1) = v_2(p - 1) + v_2(p + 1) + j - 1$ for $j >= 1$ pins down the order as a power of two; here $v_2(p - 1) = 1$ and $v_2(p + 1) = 3$.

Since every order divides $q - 1 < 10^7$, all primes appearing in the lcm are below $10^7$, so the lcm is accumulated as a table of maximal prime exponents (the $q^(e_q - v)$ contributions included) and multiplied out modulo $10^9 + 7$ at the end. The routine reproduces $R(7, 4) = 2$ and $R(10^9 + 7, 12) = 17280$, and gives $794394453$.

#pagebreak()
#link("https://projecteuler.net/problem=955")[= Problem 955: Finding Triangles]

Solution: 6795261671274

Between triangle numbers the recurrence $a_(n+1) = 2 a_n - a_(n-1) + 1$ has constant second difference $1$, and the step out of a triangle number is $+1$, so $k$ steps after reaching the triangle number $T_m$ the value is $T_m + T_k$. The next triangle number in the sequence is the smallest $k >= 1$ with $T_m + T_k = T_M$ for some $M$, which rearranges to
$ (M - k)(M + k + 1) = m(m + 1). $

Setting $D_1 = M - k$ and $D_2 = M + k + 1$, this is a factorisation of $N = m(m+1)$ into a divisor pair with odd difference $D_2 - D_1 = 2k + 1 >= 3$. So each hop is: factor $N$, pick the opposite-parity divisor pair with the smallest difference at least $3$, advance the index by $k = (D_2 - D_1 - 1) \/ 2$, and replace $m$ by $M = (D_1 + D_2 - 1) \/ 2$.

Starting from $a_0 = 3 = T_2$ we hop $69$ times. The values stay below $5 dot 10^24$ ($m < 3 dot 10^12$), so Pollard rho factors every $N$ instantly. The method reproduces the given $a_2964 = 1439056$ as the $10$th triangle number (brute force agrees on the first ten), and gives index $6795261671274$.

#pagebreak()
#link("https://projecteuler.net/problem=956")[= Problem 956: Super Duper Sum]

Solution: 882086212

Since $n star = product_(i<=n) i \$ = product_(j<=n) (j!)^(n+1-j)$, the exponent of a prime $p$ in $1000 star$ is $sum_(j=1)^1000 (1001 - j) v_p (j!)$ by Legendre's formula; only the $168$ primes below $1000$ occur.

Selecting divisors $d$ with $Omega(d)$ divisible by $m$ is a roots-of-unity filter:
$ D(n, m) = 1/m sum_(j=0)^(m-1) product_(p^e || n) sum_(i=0)^e (omega^j p)^i, $
because each divisor contributes $d dot omega^(j Omega(d))$ and the product over prime powers expands to exactly that sum. The modulus $999999001$ is prime with $999999000$ divisible by $1000$, so $FF_p$ contains an element $omega$ of exact order $1000$ (a power of a primitive root), and the filter identity $sum_j omega^(j k) = m [m | k]$ holds there. Each inner sum is a geometric series costing one modular exponentiation (or equals $e + 1$ when $omega^j p equiv 1$).

The filter reproduces $D(24, 3) = 21$ and the given $D(6 star, 6) = 6368195719791280$ (checked exactly with a DP over $Omega$ residues). The full computation is $1000 times 168$ geometric sums, under a second, giving $882086212$.

#pagebreak()
#link("https://projecteuler.net/problem=958")[= Problem 958: Euclid's Labour]

Solution: 367554579311

The subtractive Euclidean algorithm on coprime $(n, m)$ takes $($sum of the partial quotients of $n \/ m) - 1$ steps, so $f(n)$ is the $m$ minimising the quotient sum, ties broken by smaller $m$. Writing $n \/ m = [a_0; a_1, dots, a_r]$, $n$ is the continuant $K(a_0 dots a_r)$ and $m = K(a_1 dots a_r)$; a coprime pair determines its digit sequence, so the quotient sum of any candidate pair is a single Euclid run.

We search digit sequences, split at the first prefix continuant $p = K(a_0 dots a_j) >= T approx sqrt(n)$. The prefix matrix entries $p, p' = K(a_0 dots a_(j-1)), q = K(a_1 dots a_j), q' = K(a_1 dots a_(j-1))$ satisfy $n = p u + p' v$ and $m = q u + q' v$ for the suffix continuant pair $(u, v)$. Given a prefix, $u$ is fixed modulo $p'$ inside $[n \/ (p + p'), space n \/ p]$ — an interval of width $approx n p' \/ p^2$, so about one candidate — and $v$ follows. The DFS over prefixes uses three prunings: a budget bound ($F(t+1) u_min$ must reach $n$ for remaining digit sum $t$, since for fixed quotient sum the continuant is maximised by all ones); branch-and-bound against the best $("sum", m)$ so far, warm-started by scanning $m$ near $n \/ phi.alt$; and an $m$-prune — within a subtree $m >= q ceil(n \/ (p + p'))$, so once the optimal sum is locked, subtrees that cannot lower $m$ die, which makes the tie-breaking phase cheap. Each found $m$ also yields its reversed-CF partner ($plus.minus m^(-1) mod n$) with equal quotient sum, collapsing the best $m$ early.

Verified against an exhaustive iterative-deepening search for dozens of random $n <= 3 dot 10^6$ and the given $f(7) = 2$, $f(89) = 34$, $f(8191) = 1856$. The answer for $10^12 + 39$ is $367554579311$ (about three minutes).

#pagebreak()
#link("https://projecteuler.net/problem=961")[= Problem 961: Removing Digits]

Solution: 166666666689036288

Digit values do not matter, only whether each digit is zero: the legal moves and the winning condition (removing the last nonzero digit) depend only on the zero\/nonzero pattern. Removing the leading nonzero digit additionally strips the run of zeros that follows it; removing any zero deletes just that zero. So the game is solved by memoised search over binary patterns starting with a nonzero symbol — only $2^17$ patterns exist for up to $18$ digits.

A $d$-digit pattern with $k$ nonzero positions corresponds to exactly $9^k$ integers, so $W(10^18)$ is the sum of $9^k$ over winning patterns of length $1$ to $18$. The naive classification by $(k, \#"zeros")$ alone fails — some $(3, 1)$ patterns win and others lose, so zero _placement_ matters — but the pattern game agrees with full brute force over actual integers: $W(100) = 18$, $W(10^4) = 1656$, $W(10^5) = 91656$. The total is $166666666689036288$ (about two seconds).

#pagebreak()
#link("https://projecteuler.net/problem=964")[= Problem 964: Musical Chairs Revisited]

Solution: 4.7126135532e-29

Round $i$ applies a random permutation $sigma_i$: a uniform $i$-subset of the $n = k(k-1)\/2 + 1$ children is permuted uniformly. Each $sigma_i$ is conjugation-invariant, so Fourier analysis on $S_n$ gives, with eigenvalues $E_i (lambda) = bb(E)[chi_lambda (sigma_i)] \/ d_lambda$,
$ P(k) = Pr["product" = rho] = 1/n! sum_lambda d_lambda chi_lambda (rho) product_i E_i (lambda), $
where $rho$ is the one-step rotation, an $n$-cycle. Since $chi_lambda$ of an $n$-cycle is nonzero only for hook shapes $lambda = (n-r, 1^r)$, where it equals $(-1)^r$ with $d_lambda = binom(n-1, r)$, only $n$ terms survive. By the Pieri branching rule, $bb(E)[chi_lambda (sigma_i)]$ is the sum of $d_nu$ over $nu$ with $lambda \/ nu$ a horizontal $i$-strip; for a hook the only strips give $nu = (n-i-r, 1^r)$ and $(n-i-r+1, 1^(r-1))$, summing to $binom(n-i-1, r) + binom(n-i-1, r-1) = binom(n-i, r)$. Hence $E_i = binom(n-i, r) \/ binom(n-1, r)$ and
$ P(k) = 1/n! sum_(r=0)^(n-1) (-1)^r (product_(i=1)^k binom(n-i, r)) / binom(n-1, r)^(k-1). $

Verified exactly against full convolution over permutation distributions for $k = 2$ ($P = 1\/2$) and $k = 3$ ($P = 1\/72$, matching the given $1.3888888889 e^(-2)$). $P(7)$ is exactly $1 \/ 21219647838989618324275200000 approx 4.7126135532 e^(-29)$.

#pagebreak()
#link("https://projecteuler.net/problem=965")[= Problem 965: Expected Minimal Fractional Value]

Solution: 0.0003452201133

Between consecutive Farey fractions $p \/ q < p' \/ q'$ of order $N$ every ${n x}$ is linear: ${n x} = (n p mod q) \/ q + n (x - p \/ q)$. For each residue $r = n p mod q$ the lowest line has $n = m_r$, the least positive solution of $n equiv -r q' (mod q)$ (using $p q' equiv -1 (mod q)$). A line with $r >= 1$ could undercut the $r = 0$ line $y = q(x - p \/ q)$ inside the interval only if $r q' + m_r < q$ — impossible, because $r q' + m_r$ is a positive multiple of $q$. Hence on the whole interval $f_N (x) = {q x}$ with $q$ the denominator of the left Farey neighbour, and the interval contributes $integral_0^(1 \/ (q q')) q t space d t = 1 \/ (2 q q'^2)$.

Each coprime pair $(q, q')$ with $q, q' <= N$ and $q + q' > N$ occurs as consecutive Farey denominators exactly once, so
$ F(N) = 1/2 sum_(q + q' > N, gcd(q, q') = 1) 1 / (q q'^2). $

This reproduces $F(1) = 1\/2$, $F(2) = 3\/8$, $F(4) = 1\/4$, and $F(10) = 19\/144 = 0.13194 dots$, all matching the given values (and direct numerical integration of $f_N$). Kahan-compensated summation over the $approx 5 dot 10^7$ pairs keeps the float64 error far below the 13th decimal, giving $F(10^4) = 0.0003452201133$.

#pagebreak()
#link("https://projecteuler.net/problem=969")[= Problem 969: Kangaroo Hopping]

Solution: 412543690

The expected number of uniform $(0,1)$ hops to pass $n$ has the classical closed form
$ H(n) = sum_(j=0)^(n-1) (-1)^j (n-j)^j / j! e^(n-j), $
so with $alpha = H(1) = e$ the coefficient of $alpha^(n-j)$ is $c_j = (-1)^j (n - j)^j \/ j!$, matching the given $H(3) = alpha^3 - 2 alpha^2 + 1/2 alpha$.

The coefficient $c_j$ is an integer exactly when $j! divides (n-j)^j$. Since $v_q (j!) < j$ for every prime $q <= j$, this happens precisely when $n - j$ is divisible by every prime up to $j$, i.e. by the primorial $P_j$ (checked by brute force for all $n <= 60$). Therefore
$ sum_(n=1)^N S(n) = sum_(j >= 0) ((-1)^j P_j^j) / j! sum_(t=1)^(floor((N - j) \/ P_j)) t^j, $
substituting $n - j = P_j t$. Only $j <= 52$ contributes for $N = 10^18$, because $P_53 > 10^18$. Each inner power sum is a polynomial of degree $j + 1$ in its limit, evaluated modulo $10^9 + 7$ by Lagrange interpolation on $j + 2$ points; the division by $j!$ is a modular inverse. The formula reproduces $sum_(n=1)^10 S(n) = 43$ (and brute-force sums up to $N = 400$), giving $412543690$.

#pagebreak()
#link("https://projecteuler.net/problem=970")[= Problem 970: Kangaroo Hopping over Sixes]

Solution: 44754029

$H(t)$ is the renewal function of the renewal process with uniform $(0,1)$ jumps. Its Laplace transform is $1 \/ (s (1 - hat(f)(s)))$ with $hat(f)(s) = (1 - e^(-s)) \/ s$, whose poles are $s = 0$ (a double pole, contributing the linear part $2t + 2\/3$) and the complex roots of $e^(-s) = 1 - s$. At every such root the derivative of $1 - hat(f)(s)$ equals $1$ exactly, so each residue is just $e^(s_0 t) \/ s_0$ and
$ H(t) = 2t + 2/3 + sum_("root pairs") 2 op("Re")[e^(s_0 t) / s_0]. $

The dominant pair is $s_0 approx -2.08884 + 7.46149 i$; the next pair has real part $approx -2.664$, smaller at $t = 10^6$ by a factor $approx e^(-575000)$, so a single pair determines the answer. The deviation $epsilon(t) = sum 2 e^(a t) (a cos b t + b sin b t) \/ (a^2 + b^2)$ has magnitude $approx 10^(-907168)$, so the fractional part of $H(10^6)$ is $0.66...6$ until a ripple roughly $907168$ digits in. The whole computation runs in $130$-digit decimal fixed point on plain Python integers: $pi$ by Machin's formula, $ln 10 = 2 op("atanh")(9\/11)$, exp\/sin\/cos by Taylor series with range reduction, and $s_0$ polished by complex Newton iteration from a float seed (matching the true root to $33+$ digits). We then form the integer $floor(2/3 dot 10^w) + op("round")(epsilon dot 10^w)$ for $w$ slightly past the ripple and read off the first eight digits that are not $6$. The pipeline (including a second root pair, where it still matters) reproduces exact digit extraction from the closed-form $H(t)$ for all tested $t in [20, 100]$, and gives $44754029$.

#pagebreak()
#link("https://projecteuler.net/problem=971")[= Problem 971: Modular Polynomial Composition]

Solution: 33626723890930

Let $p = 5k - 4$, so $p equiv 1 space (mod 5)$ and $k - 1 = (p-1)\/5$. For $x eq.not 0$, write $chi(x) = x^((p-1)\/5)$, a multiplicative character onto the fifth roots of unity $mu_5 subset FF_p^*$. Then
$ f(x) = x^k + x = x (chi(x) + 1), $
and since $chi(x) = -1$ is impossible ($-1$ has order $2 divides.not 5$), $f$ never maps a nonzero point to zero; $0$ is a fixed point.

The multiplier $1 + chi(x)$ depends only on the coset of $x$ under the index-$5$ subgroup, and $chi(f(x)) = chi(x) dot chi(1 + chi(x))$. So the five cosets evolve by the deterministic map $v arrow.r v dot chi(1 + v)$ on $mu_5$, identical for every point of the coset. If a point $x$ returns to itself, its coset value must return; conversely, if the coset value $v$ lies on a cycle of this $5$-state map, then going around that cycle multiplies $x$ by a fixed constant $M in FF_p^*$, and since $M$ has finite multiplicative order, $x$ is periodic. Hence the periodic points are exactly $0$ together with the full cosets whose $chi$-value lies on a cycle:
$ C(p) = 1 + t(p) (p-1)/5, $
where $t(p) in {1, dots, 5}$ counts cyclic states of the little map. This was verified against a direct functional-graph computation for every applicable prime below $1500$, and reproduces $C(11) = 7$ and $S(100) = 127$.

The final computation sieves the $approx 1.4 dot 10^6$ primes $p equiv 1 space (mod 5)$ up to $10^8$ and, for each, evaluates five modular exponentiations to build the $5$-state map (plus a few to find a generator of $mu_5$), all in compiled code; $64$-bit arithmetic suffices since $p < 2^27$. The total is $33626723890930$.

#pagebreak()
#link("https://projecteuler.net/problem=972")[= Problem 972: Hyperbolic Lines]

Solution: 3575508

In the open unit disc model, geodesics are diameters and circular arcs orthogonal to the unit circle. $cal(V)(N)$ is the set of points inside the disc with rational coordinates of denominator at most $N$, and $T(N)$ counts ordered triples of distinct points of $cal(V)(N)$ on a common geodesic; $T(2) = 24$, $T(3) = 1296$. Find $T(12)$.

Any two distinct points lie on exactly one geodesic, so the $tilde 23.4$ million unordered pairs of $cal(V)(12)$ ($6837$ points) are grouped by their geodesic: one containing $k$ points receives $binom(k, 2)$ pairs and contributes $k(k-1)(k-2)$ triples.

A circle with centre $c$ is orthogonal to the unit circle iff $|c|^2 = rho^2 + 1$, so passing through $P$ becomes the _linear_ equation $2 P dot c = |P|^2 + 1$, and two points give a rational centre by Cramer's rule -- a diameter exactly when $P, Q, O$ are collinear. Scaling by $L = "lcm"(1..12) = 27720$ makes all quantities integral and below $10^14$: the canonical key is the gcd-reduced numerator/denominator triple (diameters use the primitive direction). Keys for all pairs are filled in a compiled double loop, lexsorted, and run lengths $c$ converted back via $k(k-1)\/2 = c$ with integrality asserted. The pipeline reproduces $T(2)$ and $T(3)$.

#pagebreak()
#link("https://projecteuler.net/problem=973")[= Problem 973: Pile Game]

Solution: 427278142

$n$ cards start as $n$ singleton piles. Each round picks a pile uniformly, then another uniformly among the rest; the top card of the first moves onto the second and the remaining cards are dealt out as new singletons. After every round the score is the bitwise XOR of all pile sizes; the game ends at one pile of $n$. Find the expected total score $X(10^4) mod 10^9 + 7$.

== Expected visits

Writing a state as non-singleton parts $a_1 >= dots >= a_r >= 2$ plus $m$ singletons, solving $nu = delta_"start" + P^T nu$ exactly for small $n$ reveals that the expected number of entries into each state is the multinomial $nu(s) = (m+r)! \/ (m! product_v "mult"_v !)$ -- the number of arrangements of the non-singleton parts and $m$ blanks (verified against the exact linear system for all $n <= 7$). Every round enters a state, so $X(n) = sum_s nu(s) dot "score"(s)$ over states with $r >= 1$.

== Generating functions

Summing over partitions weighted by $nu$ equals summing over _ordered_ tuples of parts with weight $binom(m+r, r)$, turning the totals into geometric series in $g(x)^r$ against $(1-x)^(-(r+1))$. The plain total collapses to $T = [x^n] x^2 \/ ((1-x)(1-2x)) = 2^(n-1) - 1$. For bit $b$ of the score, the signed series $U_b = [x^n] g_-(x) \/ ((1-w x)(1-w x-g_-(x)))$ with $g_-(x) = sum_(a>=2) (-1)^("bit"_b (a)) x^a$ (and $w = -1$ exactly for $b = 0$, where everything telescopes to $U_0 = (-1)^n T$ -- score parity is just $n mod 2$) gives the signed visit count, whence $X(n) = sum_b 2^b (T - U_b)\/2$. Each remaining $U_b$ is an $O(n^2)$ power-series inversion modulo the prime; the pipeline reproduces the exact values for $n = 2, 4, 7, 10$.

#pagebreak()
#link("https://projecteuler.net/problem=974")[= Problem 974: Very Odd Numbers]

Solution: 13313751171933973557517973175

A very odd number uses only the digits $1, 3, 5, 7, 9$, is divisible by $105 = 3 dot 5 dot 7$, and each odd digit occurs an odd number of times — zero occurrences being even, all five digits must appear, so the length is a sum of five odd numbers and is itself odd. (No $5$-digit example exists: a permutation of ${1,3,5,7,9}$ has digit sum $25$, not divisible by $3$, which is why $Theta(1)$ has seven digits.)

Divisibility by $105$ is tracked as a single residue: appending digit $d$ maps $r arrow.r (10r + d) mod 105$, which subsumes the mod $3$, mod $5$ and mod $7$ conditions at once (in particular the final digit is forced to be $5$ automatically). The DP state is the pair (parity mask of the five digits, residue), only $32 times 105$ states. A backward table $g[m]["mask"][r]$ counts length-$m$ completions that finish at full mask and residue $0$; lengths are capped at $45$, far above the $29$ digits actually needed for the $10^16$th element.

The $n$th very odd number is then constructed by first selecting the length (subtracting whole-length counts $g[ell][0][0]$ for $ell = 5, 7, 9, dots$) and then choosing digits most-significant-first, descending into the unique branch where the running count first reaches $n$. The construction reproduces $Theta(1) = 1117935$, $Theta(10^3) = 11137955115$ and a brute-force list of the smallest cases, and yields $Theta(10^16) = 13313751171933973557517973175$.

#pagebreak()
#link("https://projecteuler.net/problem=975")[= Problem 975: A Path Through the Cube]

Solution: 88597366.47748

For coprime odd $a, b$, $H_(a,b)(x) = 1/2 - (b cos(a pi x) + a cos(b pi x)) \/ (2(a+b))$ rises from $0$ to $1$ on $[0,1]$. Paths fill $z = H_(a,b)(x) = H_(c,d)(y)$ in the unit cube; $F(a,b,c,d)$ is the total variation of $z$ along the unique path from $(0,0,0)$ to $(1,1,1)$. Find $G(500, 1000) = sum F(p, q, p, 2q - p)$ over prime pairs $500 <= p < q <= 1000$, to five decimals.

This is the classical _mountain climbing problem_: two climbers on the profiles $H_(a,b)$ and $H_(c,d)$ move keeping equal heights, and only the sequences of critical values matter. Since $H' prop sin((a+b) pi x \/ 2) cos((a-b) pi x \/ 2)$, the critical points are $x = 2k\/(a+b)$ and $(2k+1)\/|a-b|$; coincident roots are double and not extrema, so the values are compressed to the alternating strict-extremum sequence.

The synchronized walk has a simple event structure: the coordinate first reaching a piece end passes _over_ its extremum onto the adjacent piece, while the other coordinate reverses inside its piece and the $z$-direction flips; simultaneous arrivals (saddles) pass straight through. $F$ accumulates $|d z|$ over events until both coordinates stand at their final endpoints with $z = 1$. The simulation reproduces $F(3,5,3,7) approx 7.01772$, $F(7,17,9,19) approx 26.79578$ and $G(3,20) approx 463.80866$; the $2628$ prime pairs take about a minute.

#pagebreak()
#link("https://projecteuler.net/problem=976")[= Problem 976: A Grand Drawing Game]

Solution: 675608326

X and O alternately (X first) draw their own symbol in red or blue on $k$ strips of lengths $n_1 <= dots <= n_k$. Adjacent squares must differ in both symbol and colour; while any strip is blank, the move must open a blank strip; a player without a valid move loses. $P(K, N)$ counts tuples with $k <= K$, $n_i <= N$ where X wins; find $P(10^7, 10^7) mod 1234567891$.

== The winning rule

The four cell states split into compatibility classes ${X r, O b}$ and ${X b, O r}$, making the game symmetric under swapping players and colours. A memoised solver over canonical multisets of strip states reveals the outcome rule: cancel pairs of equal lengths and pairs of odd lengths congruent mod $4$; with $E$ remaining even lengths and $O_1, O_3$ the parities of remaining lengths $equiv 1, 3 (mod 4)$, X wins iff $r = E + O_1 + O_3$ is even and nonzero, or $r = 1$ with the residue $equiv 1 (mod 4)$. The rule matches the solver on all small games and reproduces $P(2,4) = 7$ and $P(5,10) = 901$ over all $3002$ tuples.

== Counting

Group values into evens ($m_E = N\/2$) and the two odd classes mod $4$ ($m = N\/4$ each). Tracking multiplicity parities per class in the size generating function and simplifying (the equal odd classes make cross terms cancel),

$ W(x) = 1/2 [(1-x)^(-N) + (1+x)^(-N)] - 1/2 (1-x)^(-m_E) (1+x)^(-N) - 1/2 (1-x^2)^(-(m_E + m)), $

with vanishing constant term. The answer $[x^K] W(x)\/(1-x)$ is a sum of four coefficients of $(1-x)^(-a)(1+x)^(-b)$, each satisfying $(k+1) c_(k+1) = (a-b) c_k + (a+b+k-1) c_(k-1)$, evaluated in $O(K)$ modulo the prime with a batch inverse table, and cross-checked against direct rule counts for $(K, N) = (6, 8)$ and $(7, 12)$.

#pagebreak()
#link("https://projecteuler.net/problem=977")[= Problem 977: Iterated Functions]

Solution: 537945304

Setting $x = 1$ gives $f(y) = f^((y))(1)$; conversely if $f(y) = f^((y))(1)$ for all $y$ then $f^((x))(y) = f^((x+y-1))(1)$ is symmetric in $x, y$. So valid $f$ are exactly those determined by the orbit of $1$ via $f(y) = t_y$, where $t_k = f^((k))(1)$.

Let the orbit of $1$ be a rho with tail length $m >= 0$ and cycle length $c >= 1$, with distinct values $u_0 = 1, u_1, dots, u_(m+c-1)$. Writing $sigma(j)$ for the orbit position of the $j$-th iterate, consistency of $f(y) = t_y$ with $f(u_k) = u_(op("next")(k))$ forces $sigma(u_k) = op("next")(k)$ for every $k >= 1$: each $u_k$ is either exactly the small value $op("next")(k)$, or any value $>= m + c$ congruent to $op("next")(k)$ modulo $c$ (only possible for cycle positions). Hence the tail is forced to be $1, 2, dots, m - 1$, and each cycle position draws from one residue class mod $c$, with the class of $m$ shared by an ordered pair of positions. Counting available values with $D = n - m = Q c + r$ gives closed forms: $N(m, c) = (Q+1)^(r+1) Q^(c-r)$ for $m >= 2$, $N(1, c) = Q^(c-r) (Q+1)^r$ with $D = n - 1$, and $N(0, c) = Q' (Q'+1)^a Q'^b$ with $n = Q' c + r'$, $a = max(0, min(r', c-1) - 1)$, $b = c - 2 - a$.

Summing over $m >= 2$ groups by $Q$: a full block of $c$ consecutive $m$ is the geometric sum $(Q+1) Q ((Q+1)^c - Q^c)$, and truncated blocks use $sum_(r <= R) Q^(c-r) (Q+1)^(r+1) = (Q+1) Q^(c-R) ((Q+1)^(R+1) - Q^(R+1))$, so the whole computation is $O(n log n)$ modular exponentiations (a few seconds with numba). Verified against brute force $F(1..7) = 1, 3, 8, 21, 46, 96, 174$ and exact $F(100) = 570271270297640131$; the result is $537945304$.

#pagebreak()
#link("https://projecteuler.net/problem=978")[= Problem 978: Random Walk Skewness]

Solution: 254.54470757

Since the jump sign is a fresh fair coin, $plus.minus |X_(t-2)|$ has the same conditional distribution as $plus.minus X_(t-2)$, so the process is equal in law to the random Fibonacci recurrence $X_t = X_(t-1) + s_t X_(t-2)$ with $s_t$ i.i.d. $plus.minus 1$ (the "stay put when $X_(t-2) = 0$" rule is the same thing, since $plus.minus 0 = 0$).

Joint moments close under this recurrence: averaging over $s_t$,
$ bb(E)[X_t^a X_(t-1)^b] = sum_(j "even") binom(a, j) bb(E)[X_(t-1)^(a+b-j) X_(t-2)^j], $
so tracking all $bb(E)[X_t^a X_(t-1)^b]$ with $a + b <= 3$ as exact rationals gives the first three moments at any $t$ in $O(t)$ steps. Skewness follows from $mu$, $"var" = bb(E)[X^2] - mu^2$ and $bb(E)[(X - mu)^3] = m_3 - 3 mu m_2 + 2 mu^3$; to keep full precision with the huge integers involved, the final value is computed as the square root of the exact rational $(bb(E)[(X-mu)^3])^2 \/ "var"^3$.

Verified against the exact distribution of the original $|X_(t-2)|$ dynamics for $t <= 12$, matching the given $X_5$ table, $op("Skew")(X_5) = 0.75$ and $op("Skew")(X_10) approx 2.50997097$. The answer is $op("Skew")(X_50) = 254.54470757$.

#pagebreak()
#link("https://projecteuler.net/problem=979")[= Problem 979: Hyperbolic Frog]

Solution: 189306828278449

The hyperbolic plane is tiled by heptagons, three meeting at every vertex (the ${7,3}$ tiling). A frog on one heptagon jumps at each step to one of the seven adjacent tiles; $F(n)$ counts paths returning to the start after $n$ steps, with $F(4) = 119$ given. Find $F(20)$.

The heptagon adjacency graph is the vertex graph of the dual ${3,7}$ triangulation: $7$-regular and vertex-transitive. It is built exactly in concentric layers: layer $1$ is a $7$-cycle of the root's neighbours; thereafter each layer is a cycle, and a vertex with $p in {1, 2}$ parents has $5 - p$ child edges (degree $=$ two cycle neighbours $+ p$ parents $+$ children), consecutive parents sharing one child -- the apex of the triangle over their common edge. Shared children have $p = 2$, interior ones $p = 1$; every completed vertex ends with degree exactly $7$, asserted during construction.

A closed walk of length $20$ never leaves the ball of radius $10$, so $11$ layers (about $2 dot 10^5$ vertices, layer growth ratio $(3 + sqrt(5))\/2$) suffice. $F(20)$ is the root entry of $A^20 e_"root"$ via twenty sparse matrix--vector products in exact arithmetic. The graph reproduces $F(2) = 7$, $F(3) = 14$ (seven incident triangles, two oriented walks each) and the given $F(4) = 119$.

#pagebreak()
#link("https://projecteuler.net/problem=983")[= Problem 983: Consonant Circle Crossing]

Solution: 6725

== Structure of perfect sets

Write $r^2 = N$. If two circles of radius $r$ with grid centers $C_1, C_2$ pass through one common grid point $P$, then the reflection $Q = C_1 + C_2 - P$ is integral and satisfies $|Q - C_1| = |C_2 - P| = r$: the second intersection point is a grid point automatically, and $C_1 P C_2 Q$ is a rhombus of side $r$. Under the no-tangency rule, harmonising is therefore just "there is a grid point at distance $r$ from both centers", and $N$ is an integer expressible as a sum of two squares. The harmony points are not chosen, they are forced: every grid point at distance $r$ from at least two centers is one, and whenever a harmony point sees two centers their rhombus closes onto a second harmony point.

This closure makes perfect sets hypercube configurations. Pick $d$ pairwise non-parallel lattice vectors $v_1, dots, v_d$ of norm $N$ and center the circles on the subset sums of odd-size subsets; the harmony points are then the even subset sums. That gives $2^(d-1)$ circles and $2^(d-1)$ harmony points, every cherry closes into a rhombus, and connectivity is automatic because subsets differing by exchanging two generators always share their two designed points. The problem's own figure is the case $d = 3$ (four circles, four points, each point on three circles), and the construction reproduces both given values end to end: $d = 2$ first works at $N = 1$, so $R(2) = 1$, and $d = 3$ needs six lattice points on the circle, first available at $N = 5$, so $R(4) = sqrt(5)$. Exhaustive search over every connected center set supports the converse: at $N = 5$ all $5.1$ million connected sets up to size $6$ contain perfect sets only of sizes $2$ and $4$, and a counting argument ($sum_P binom(c_P, 2) = 2e$ with all terms odd) rules out three circles outright.

A perfect set of $n >= 500$ circles therefore needs $d = 10$ directions, hence at least $20$ lattice points on the circle. Writing $N = 2^(a_0) product p_i^(a_i) product q_j^(2 b_j)$ with $p_i equiv 1$ and $q_j equiv 3 space (mod 4)$, the lattice point count is $4 product (a_i + 1) >= 20$, first satisfied by $N = 325 = 5^2 dot 13$. But that is nowhere near sufficient.

== Degeneracies

Let $V$ be all norm-$N$ lattice vectors. A choice of ten generators is valid exactly when the $plus.minus 1$-signed sums $x$ over supports $M$ of the chosen ten avoid four traps:

- $x = 0$ with $|M|$ even: two centers collide;
- $|x|^2 = 4N$ with $|M|$ even: two circles in the set are tangent;
- $|x|^2 = N$ with $|M|$ odd, $|M| >= 3$: a stray center-point incidence, whose rhombus closures spill outside the designed point set;
- $x in V - V$ with $|M|$ even, $|M| >= 4$: two distant circles share a stray grid point, spawning two extra harmony points.

A signed sum with support of size less than $10$ is realized by center pairs of both parities, so any such violation is fatal. Supports of size exactly $10$ are realized only by pairs whose positive part $M^+$ has the right parity, so a full-support violation kills exactly one of the two orientations (centers on odd sums versus centers on even sums) and the other must be checked directly. Vanishing sums are not even instantly fatal: a collision of support $m$ merges $2^(9-m)$ center pairs and equally many point pairs, so a configuration with one support-$6$ relation could still hold $504 >= 500$ circles; these merged candidates have to be enumerated and tested too (none ever survives the side conditions).

These relations are pervasive, which is the heart of the problem. At $N = 325$ nothing survives past $d = 6$ ($32$ circles); at $N = 625$ the best is $d = 8$ ($128$ circles); every candidate below $6725$ fails. The growth of the intermediate thresholds shows how strongly arithmetic structure fights the construction: $R(8)^2 = 5$, $R(16)^2 = 25$, $R(32)^2 = 125$, then nothing of size $500$ until
$
R(500)^2 = 6725 = 5^2 dot 269.
$
The winning ten directions at $N = 6725$ (one of four such subsets of its twelve) carry a single violating relation, of full support with $|M^+|$ odd; it kills the odd-sum orientation only, and the even-sum orientation is a flawless perfect consonant set of exactly $512$ circles.

== Computation

Candidates are the $N$ with at least $20$ lattice points, in increasing order. For each, a depth-first search adds one direction at a time while maintaining every signed sum of the prefix split by support parity, pruning the moment a proper-support violation appears; clean ten-subsets and full-support edge cases are passed to a verifier. Subsets containing a vanishing sum are handled separately: meet-in-the-middle over the two halves of the direction list finds every vanishing relation, and all supersets of the minimal supports are enumerated with only the tangency rule for pruning, the one condition that stays sound once centers can merge (the tangent pair still exists in the merged configuration). Everything that reaches the final stage is checked against the definition itself: distinct centers, no pair at distance $2r$, the grid points covered by at least two circles counted exactly, and connectivity of the harmonising graph by union-find. The first radius admitting a verified perfect set of at least $500$ circles is $r^2 = 6725$, in about four minutes.

#pagebreak()
#link("https://projecteuler.net/problem=984")[= Problem 984: Knights and Horses]

Solution: 885722296

Count non-empty subsets of an $N times N$ board that are _knight-connected_ (a knight can travel between any two squares of the subset using only subset squares) and _horse-disjoint_ (xiangqi horses on every subset square, no horse attacks another: a horse moves one square orthogonally then one diagonally outward, blocked if the orthogonal leg square is occupied). Find $f(10^18) mod 10^9 + 7$.

== Structure

Horse-disjointness is local: for every knight pair $X, X + (2,1)$ in the set, both legs $X + (1,0)$ and $X + (1,1)$ lie in the set (all eight orientations). Multi-cell sets also need a connected knight graph. Three local arguments pin the geometry: rows are contiguous (a knight pair across an empty row has its legs there, and vertically separated chunks cannot connect); each row is one interval (a hole creates an unblocked pair across it); and row endpoints move by at most one per row (a right end growing by two leaves the pair $(i, b_i), (i + 1, b_i + 2)$ unblocked). So valid multi-cell sets are HV-staircases of row intervals with $plus.minus 1$ slopes -- confirmed equal to an assumption-free profile DP over arbitrary row bitmasks with full connectivity partitions for all $N <= 12$.

== Counting

A row sweep keeps the last two intervals and the _exact_ partition of their cells into knight components: same-row cells are never knight-adjacent, so fresh rows enter as isolated cells that merge through $(1, plus.minus 2)$ and $(2, plus.minus 1)$ edges, and components leaving the two-row frontier can never reconnect (pruning dead prefixes). Truncating partitions is unsound -- merge scars can sit anywhere inside a wide row -- but kept exactly, reachable states stay in the low thousands. Complete shapes (one component, an edge) contribute $(N - h + 1)$ placements at height $h$.

Berlekamp--Massey on $f(1..36)$ under two primes finds an order-$14$ linear recurrence that holds on all surplus terms, reproduces $f(100) = 8658918531876$ exactly (CRT of two Kitamasa evaluations) and $f(10000) equiv 377956308$; Kitamasa then gives $f(10^18) equiv 885722296$.

#pagebreak()
#link("https://projecteuler.net/problem=986")[= Problem 986: Tokens on a Row]

Solution: 15418494040

Every square of an infinite row holds a token; a move picks tokens $X$ and $Y$ with $Y$ exactly $c$ squares right of $X$ and moves both to the square $d$ right of $Y$. $G(c, d)$ is the maximum number of tokens collectable on one square; find $sum G(c, d)$ over $1 <= c, d <= 160$.

== A flow characterisation

Residue classes mod $g = gcd(c, d)$ never interact, so $G(c, d) = G(c\/g, d\/g)$; assume coprime and let $p = c + d$. Abstracting time, a strategy is a multiset of _events_: an event at $q$ consumes tokens at $q$ and $q + c$ and emits two at $q + p$; outputs strictly exceed inputs, so any balanced event multiset is schedulable. Counting visits versus departures per square (one original token each), collecting $1 + 2 n_(T - p)$ tokens at $T$ is possible iff $n_q + n_(q - c) <= 1 + 2 n_(q - p)$ for all $q$ with $n >= 0$ of finite support. Indexing leftwards, the greedy-minimal profile $x_0 = m$, $x_j = floor((x_(j-p) + x_(j-d)) \/ 2)$ is pointwise forced and minimal, so $m$ is achievable iff this sequence dies out, and $G = 1 + 2 m^*$. Infeasible $m$ converge to a constant positive window (any constant is a fixed point of the monotone map), giving an exact terminating test. This reproduces every given value.

== A reduction to one sequence

Tabulating $G$ over all coprime pairs up to $30$ reveals the exact reduction $G(c, d) = H(d + floor((c - 1)\/2))$ with $H(k) := G(1, k)$ -- with precisely seven exceptions, all at $d = 1$ ($c in {2,3,4,5,6,8,10}$), re-verified at runtime over all coprime pairs with $c + d <= 26$. The sum then needs only $H(1..239)$, each found by binary search with the extinction test, extrapolation-seeded brackets, in about three minutes.

#pagebreak()
#link("https://projecteuler.net/problem=987")[= Problem 987: Straight Eight]

Solution: 11044580082199135512

A straight is five cards of sequential rank, not all of one suit, with the ace ranking low or high but never wrapping. There are $10200$ straights and $31832952$ pairs of disjoint straights; count unordered sets of _eight_ pairwise-disjoint straights.

A straight is a rank window $w in 1..10$ (window $w$ covering positions $w..w+4$, positions $1$ and $14$ being the _same_ four aces) with a suit per rank. Dropping the "not all one suit" rule makes the suits independent per rank position, so we apply inclusion-exclusion over a designated set of flush straights:

$ "answer" = sum_j (-1)^j sum_("flush sets," |dot| = j) P(8 - j; "free suits"). $

Flushes are (window, suit) pairs; flushes in windows within distance $4$ -- or in the ace-sharing pair ${1, 10}$ -- need distinct suits, and any five consecutive windows hold at most four flushes. A depth-first enumeration over per-window suit subsets lists all configurations; only per-window counts matter downstream since $P$ depends only on free-suit counts per rank.

$P(k; dot)$ counts unordered sets of $k$ disjoint generalised straights by scanning rank positions with the expiry profile of active straights as state: each position charges an ordered injection $"perm"("free", "active")$ into its free suits, with $1\/s!$ per group of $s$ straights starting together (exact rational arithmetic), and the shared aces are handled by conditioning on the window-$1$ and window-$10$ usage and charging one joint ace-column injection. The routine reproduces both given values; the full count takes a few seconds.

#pagebreak()
#link("https://projecteuler.net/problem=988")[= Problem 988: Non-attacking Frogs]

Solution: 2727531976556215755

Frogs at integer points jump forward by $a$ or $b$ with $gcd(a, b) = 1$; a frog at $m$ attacks one at $n > m$ iff $n - m$ lies in the numerical semigroup $S = angle.l a, b angle.r$. $F(a, b)$ sums all frog locations over all non-attacking configurations containing a frog at $0$; given $F(3,5) = 23$ and $F(5,13) = 16336$, find $F(19, 53)$.

Every positive frog position is a _gap_ of $S$ (non-representable), and classically each gap has a unique representation $g = a b - a x - b y$ with $1 <= x <= b - 1$, $y >= 1$ -- the lattice points strictly inside the triangle $a x + b y < a b$. For two gaps, $g(x', y') - g(x, y) = a(x - x') + b(y - y') in S$ exactly when $x >= x'$ and $y >= y'$ componentwise, since any alternative representation would need $|x - x'| >= b$ or $|y - y'| >= a$, which the triangle forbids. So non-attacking configurations are precisely the _antichains_ of a staircase poset: at most one point per column, heights strictly decreasing left to right.

Therefore $F(a, b) = sum_p g(p) L(p) R(p)$ where $L(p)$ counts antichains strictly left of and above $p$, and $R(p)$ counts antichains strictly right of and below -- both computed by column sweeps with prefix sums over the $468$-point staircase, in exact integer arithmetic. The reduction is verified against direct subset enumeration over the gaps for four small parameter pairs alongside both given values.

#pagebreak()
#link("https://projecteuler.net/problem=989")[= Problem 989: Fibonacci Sum]

Solution: 697845151

$G(n)$ counts residues $0 <= x < n$ with $x^2 equiv x + 1 mod n$; we need $sum_(n <= 10^14) F_n G(n) mod 10^9 + 9$.

== A convolution identity

Completing the square relates $G(n)$ to roots of $z^2 equiv 5$. With $chi$ the quadratic character mod $5$: primes $p equiv plus.minus 1 mod 5$ give two roots at every power; $p equiv plus.minus 2$ (including $p = 2$) give none; and at $p = 5$ the double root $x = 3$ fails to lift, so $G(5) = 1$ but $G(5^a) = 0$ for $a >= 2$. All cases collapse into one Dirichlet convolution, $G = chi * mu^2$, verified directly for all $n <= 3000$.

== Geometric series mod $10^9 + 9$

The modulus is chosen so that $5$ is a quadratic residue: with $s = sqrt(5) mod q$ and $phi, psi = (1 plus.minus s)\/2$, Binet's formula gives $S = (T(phi) - T(psi))\/s$ with $T(c) = sum_(n <= N) G(n) c^n$. Expanding $mu^2(e) = sum_(k^2 | e) mu(k)$,

$ T(c) = sum_k mu(k) U(c^(k^2), floor(N\/k^2)), quad U(w, M) = sum_(d <= M) chi(d) (w^d + w^(2d) + dots + w^(d floor(M\/d))). $

$U$ is evaluated by a hyperbola split: small $d$ give plain geometric series; for each small $j$ the sum over large $d$ splits by $d mod 5$ into at most four geometric series with ratio $w^(5j)$. Every geometric sum uses an inversion-free doubling recurrence with both roots sharing one bit-loop, and for $k >= 1.2 dot 10^5$ a direct pass over a sieved table of $1 * chi$ is cheaper. About $sqrt(N) log N$ modular operations in total; the pipeline reproduces the given checkpoint at $N = 10^3$ and three independent implementations agree at $N = 10^6 + 7$ and $10^8 + 3$.

#pagebreak()
#link("https://projecteuler.net/problem=990")[= Problem 990: Addition Equations]

Solution: 50322750

An addition equation is a string $x_1 + dots + x_k = y_1 + dots + y_m$ of positive integers without leading zeros whose sides have equal sums; $A(n)$ counts those of length at most $n$, and we need $A(50) mod 10^9 + 7$.

The numbers can be up to $48$ digits long, so sums cannot be enumerated -- but equality can be _verified column by column_. Align every number at its units digit and scan columns from least significant upward: every active term contributes one digit, a term whose leading digit falls in this column contributes $1..9$ and retires, and with $s_A, s_B$ the column digit sums, $s_A - s_B + c$ must be divisible by $10$ with new carry $(s_A - s_B + c)\/10$; the equation holds iff the final carry is zero.

The DP state is (active terms per side, carry, remaining length budget): each column consumes one character per active term, separators are charged up front per initial term-count pair, retiring subsets contribute binomial factors, and carry transitions are weighted by digit-sum distributions $(1 + x + dots + x^9)^"cont" (x + dots + x^9)^t$ cross-correlated between the sides. At most $25$ terms fit in $50$ characters and carries stay within $plus.minus 25$, so the state space is tiny. Strings shorter than $n$ simply leave budget unspent. The DP reproduces all three given checkpoints, confirmed independently by brute-force enumeration.

#pagebreak()
#link("https://projecteuler.net/problem=991")[= Problem 991: Fruit Salad]

Solution: 23871972654940

Sum $a + b + c$ over positive triples with $a\/(b + c) + b\/(c + a) + c\/(a + c) = 4$ and $a + b + c <= 10^7$.

Unlike the notorious symmetric fruit equation (whose smallest solutions require an elliptic curve and have eighty-digit entries), here the second and third fractions share the denominator $c + a$. With $u = b + c$ and $v = a + c$ the equation collapses to $a\/u + u\/v = 4$, i.e. $v(4u - a) = u^2$: so $d := 4u - a$ is a positive divisor of $u^2$, and $a + b + c = 5u - d$.

Divisors of a square biject with triples: $d = e^2 h$, $u = e f h$, $u^2\/d = f^2 h$ with $gcd(e, f) = 1$. Every condition becomes scale-free in $h$: positivity reads $e^2 + f^2 - 4 e f >= 1$, $5 e f - e^2 - f^2 >= 1$, $e <= 4f - 1$, confining $e\/f$ to two narrow windows around $(5 - sqrt(21))\/2$ and $2 + sqrt(3)$, and the sum is $h dot e(5f - e) <= 10^7$. Each valid coprime $(e, f)$ contributes $e(5f - e) dot H(H + 1)\/2$ with $H = floor(10^7 \/ (e(5f - e)))$; only $f$ up to about $sqrt(2 dot 10^7)$ matters and the whole sum takes under a second, validated against a direct brute force for all bounds up to $700$.

#pagebreak()
#link("https://projecteuler.net/problem=993")[= Problem 993: Banana Beaver]

Solution: 1661971830985915304

A beaver at position $0$ carries $N$ bananas and repeatedly acts on the cells $x$ and $x + 1$: pick up from $x + 1$ and step to $x - 1$ if both are occupied; pick up from $x$ and jump to $x + 2$ if only $x$ is; shift the banana from $x + 1$ to $x$ and jump to $x + 2$ if only $x + 1$ is; otherwise drop one banana on each of $x - 1, x, x + 1$ and step to $x - 2$ when at least three are carried, else stop. $"BB"(N)$ is the stopping position; $"BB"(1000) = 1499$, and we need $"BB"(10^18)$.

== One trajectory serves every $N$

Only the drop rule consults the carried count, and only through the test "$"carry" >= 3$". Two beavers whose loads differ by a constant therefore share one trajectory until the lighter dies: simulating once with an unbounded load and tracking $"spent"$ (three per drop, minus one per pickup), the beaver that started with $N$ bananas stops at the _first_ drop event where $"spent" in {N - 2, N - 1, N}$. A single linear-time pass thus produces $"BB"(N)$ for all $N$ up to a bound, reproducing $"BB"(1000) = 1499$ and matching independent direct simulations at random checkpoints.

== Eventual exact linearity

The banana field settles into a quasi-periodic word that the beaver sweeps in self-similar cycles, and the residual $E(N) = 118 N - 71 dot "BB"(N)$ is _exactly periodic_: $"BB"(N + 71) = "BB"(N) + 118$ for every $N >= 514$, verified over the entire simulated range up to $10^6$ -- nearly $14000$ consecutive periods without exception. Folding $10^18$ back into the simulated window along this recurrence gives the answer; the asymptotic speed is exactly $118 \/ 71 approx 1.66197$ cells per banana.

#pagebreak()
#link("https://projecteuler.net/problem=994")[= Problem 994: Counting Triangles]

Solution: 350247268

Every bottom point $(i, 1)$, $1 <= i <= m$, is joined to every top point $(j, 2)$, $1 <= j <= n$, and $T(m, n)$ counts all triangles in the picture, cut or not. We need $T(1234 dot 10^8, 2345 dot 10^8) mod 10^9 + 7$.

== Four shapes of triangle

Two segments meet in at most one point: a shared bottom endpoint, a shared top endpoint, or a proper crossing (bottoms and tops in opposite order). Three segments bound a triangle exactly when they pairwise meet in three distinct points. Counting each shape: apex at a bottom point gives $2 binom(m, 2) binom(n, 3)$, apex at a top point gives $2 binom(n, 2) binom(m, 3)$, one apex on each line gives $2 binom(m, 2) binom(n, 2)$, and three pairwise crossings give $binom(m, 3) binom(n, 3)$ -- except that _concurrent_ triples, whose three segments pass through one point, must be subtracted from the last class.

== Concurrent triples

For bottoms $a_1 < a_2 < a_3$ and tops $b_1 > b_2 > b_3$, concurrency means $(a_2 - a_1)(b_2 - b_3) = (a_3 - a_2)(b_1 - b_2)$. Writing the gaps as $u, v$ and $s, w$, the relation $u w = v s$ is parametrised by $u = alpha kappa$, $v = beta kappa$, $s = alpha lambda$, $w = beta lambda$ with $gcd(alpha, beta) = 1$. Grouping by $c = alpha + beta$ ($phi(c)$ coprime pairs each):

$ X = sum_(c >= 2) phi(c) A_m (c) A_n (c), quad A_M (c) = M K - c K(K+1) \/ 2, quad K = floor((M - 1) / c). $

This formula reproduces all three given values exactly.

== Summation at $2 dot 10^11$

Group $c$ into the roughly $2(sqrt(m) + sqrt(n))$ blocks where both $K_m$ and $K_n$ are constant; inside a block $A_m A_n$ is quadratic in $c$, so each block needs $Phi_j (N) = sum_(c <= N) phi(c) c^j$ for $j = 0, 1, 2$ at its edges. Since $sum_(c | t) phi(c) = t$, the hyperbola identity $sum_(e >= 1) e^j Phi_j (floor(N \/ e)) = sum_(t <= N) t^(j+1)$ gives a Mertens-style recursion for $Phi_j$. A sieve covers $c <= 2.4 dot 10^7$ and the recursion, evaluated bottom-up over the quotient sets of $m - 1$ and $n - 1$, covers the rest in $O(N^(2\/3))$. The whole computation runs in about a minute, validated against a brute-force $phi$ table including with a tiny sieve bound to exercise the recursion.

#pagebreak()
#link("https://projecteuler.net/problem=995")[= Problem 995: A Particular Pair of Polynomials]

Solution: 2.21322e536280

With $f_p (x) = 1 + x + dots + x^(p-1)$ and $g_n (x) = 1 + sum_(d | n) x^d$, let $S(p)$ be the least $s$ with $f_p | g_s$, and $T(m)$ the product of $S(p)$ over primes $p < m$. We need $T(20000)$ to five decimal digits of mantissa.

== From divisibility to a tiling

$f_p = Phi_p$ is irreducible, so $f_p | g_s$ iff $1 + sum_(d|s) zeta^d = 0$ for a primitive $p$-th root $zeta$. Counting divisors of $s$ by residue class mod $p$ and reducing against the lone relation $1 + zeta + dots + zeta^(p-1) = 0$, the condition is $m_1 = dots = m_(p-1) = m_0 + 1$. If $p | s$ a short computation shows the class sizes cannot balance, so $p divides.not s$, $m_0 = 0$, $tau(s) = p - 1$, and the divisors of $s$ hit every residue of $ZZ_p^*$ exactly once.

Writing $s = product q_i^(e_i - 1)$ with $product e_i = m := p - 1$, each prime power contributes, in discrete-log space, an arithmetic progression of length $e_i$ and step $log q_i$; the divisors biject onto $ZZ_p^*$ iff these progressions tile $ZZ_m$. Evaluating mask polynomials at characters of each order $d | m$ gives the exact criterion: for every divisor $d > 1$ of $m$ some part must satisfy $d | z_i e_i$ and $d divides.not z_i$, where $z_i = m \/ "ord"_p (q_i)$. This was validated against brute force for all $p <= 13$.

== Minimising

$S(p)$ minimises $product q_i^(e_i - 1)$ over multisets of parts $(e_i, q_i)$ with distinct primes, $product e_i = m$, and the coverage criterion. A branch-and-bound always covers the _largest uncovered divisor_ next -- every solution must contain such a part, and exactly the expensive divisors have few affordable coverers, keeping the branching narrow where costs are high. Primes of a given order are served lazily (a shared ascending scan for dense orders; enumeration of the order-$r$ residue progressions with Miller-Rabin for sparse ones), primes within one order class are assigned to that class's parts rearrangement-optimally, and once coverage is complete the leftover exponent quota is filled by the cheapest factorization over the smallest unused primes. Mixed-radix chain constructions seed the bound; pruning uses exact integers throughout.

All $2262$ values of $S(p)$ take about a minute; their exact product has $536281$ digits, verified against both checkpoints $T(20)$ and $T(100)$.

#pagebreak()
#link("https://projecteuler.net/problem=996")[= Problem 996: Overtakes]

Solution: 137726405

Each of $n$ ranked players may play their adjacent neighbour once a day; a win by the lower-ranked player swaps the two (an _overtake_). After $k$ days everyone is back at their starting rank, and $F(n, k)$ counts the achievable $n$-tuples of overtake counts. We need $F(123, 4567891) mod 1234567891$.

== Which tuples are achievable

Idle days pad freely, so $F(n, k)$ counts tuples using at most $k$ swaps. Every swap is a crossing between one fixed pair of players, and returning to the start forces each pair $(j, l)$ to cross an evenly many times, say $2 w_(j l)$; the crossings alternate direction, so each player gains exactly $w_(j l)$ overtakes from that pair. Hence the count vector is the "degree sequence" $c_j = sum_l w_(j l)$ of a symmetric nonnegative integer matrix. A player with $c_j = 0$ never moves and walls off the players on either side, so the structure decomposes into maximal runs of positive entries. Within a run, a multigraph with the prescribed degrees exists iff the run sum $s$ is even and the largest entry is at most $s\/2$, and a brute-force search over schedules for $n <= 5$ confirms every such matrix is realizable by adjacent swaps. The characterization reproduces $F(3,4) = 8$ and $F(12,34) = 2457178250$.

== Counting and extrapolating

The number of length-$L$ runs with even sum $s$, positive entries, and maximum at most $s\/2$ is $binom(s-1, L-1) - L binom(s\/2-1, L-1)$ (at most one entry can exceed $s\/2$, so one inclusion-exclusion term suffices). A left-to-right DP over positions -- tracking whether the prefix ends in a zero or at the end of a run, and the running sum $m$ -- yields $f(n, m)$, the number of achievable tuples with sum exactly $m$, and $F(n,k) = sum_(m <= k) f(n, m)$.

For fixed $n$ the generating function of $f(n, dot)$ is rational with denominator $(1 - x^2)^n$, so the cumulative $F(123, k)$ eventually satisfies the linear recurrence with characteristic polynomial $(x-1)^124 (x+1)^123$ of degree $247$. Computing $F(123, m) mod 1234567891$ for $m <= 600$ by the DP, the recurrence checks out at every offset; the Kitamasa method (reducing $x^k$ modulo the characteristic polynomial) then jumps directly to $k = 4567891$.

#pagebreak()
#link("https://projecteuler.net/problem=997")[= Problem 997: Dice Box]

Solution: 5765993594880

We pack $x y z$ ordinary dice into an $x times y times z$ box so that every pair of touching faces shows the same value, the dice being indistinguishable up to rotation, and count the arrangements $f(x, y, z)$. We are told $f(1,1,1) = 24$ and $f(2,3,4) = 18432$ and want $f(9,10,11)$.

A cube has the three opposite-face pairs ${1,6}$, ${2,5}$, ${3,4}$ and $24$ rotations, giving $f(1,1,1)=24$. An orientation chooses which pair sits on each axis (a permutation, $6$ ways) and which member of each pair faces the positive direction; chirality forces an even number of sign flips, leaving $4$ patterns, and $6 dot 4 = 24$.

Two dice touching along the $x$ axis must carry the *same* pair on that axis with the orientation flipped. Propagating, every die on a line parallel to an axis shares that axis's pair and the signs alternate. Letting $X(j,k)$, $Y(i,k)$, $Z(i,j)$ be the pairs on the three axes, the three pairs at each cell are distinct while the alternating signs interact through the chirality rule. Counting both the pair assignment and the sign/chirality layer makes $f$ satisfy, in each variable, the recurrence with characteristic roots $2$ and $4$; fitting the resulting symmetric closed form to small boxes yields
$ f(x, y, z) = 24 dot 2^(x + y + z - 4) (2^x + 2^y + 2^z - 4), $
which reproduces the full brute-force table and the given values. Hence $f(9,10,11) = 24 dot 2^26 dot 3580 = 5765993594880$.

#pagebreak()
#link("https://projecteuler.net/problem=998")[= Problem 998: Squaring the Triangle]

Solution: 4439835458570

The minimum bounding square of a triangle is the smallest square, in any orientation, that covers it. We need $T(n)$, the sum of perimeters of all non-congruent integer-sided triangles whose minimum bounding square has integer side $s <= n$, for $n = 10^6$.

For a fixed orientation $theta$ the axis-aligned bounding box has width $W(theta)$ and height $H(theta)$, and the bounding square has side $max(W, H)$. Minimising over $theta$, the optimum occurs in one of two ways.

*Height-dominated (flush).* One edge lies along a side of the square and the opposite vertex touches the far side, so $s$ equals the altitude to that edge while the perpendicular extent is no larger. Taking the shortest side $a$ (its altitude $h$ is the largest), the triangle is two integer right triangles glued along the common leg $h$: legs $p, q$ with $p^2 + h^2$ and $q^2 + h^2$ perfect squares, base $a = p + q$, and $s = h$. Comparing the flush value $h$ with the tilted value of the same edge pair gives the exact regime
$ a <= h quad "and" quad h^2 <= h(p + q) + p q, $
the latter being $h^2 (h - a)^2 <= (p q)^2$.

*Balanced (tilted).* Here $W = H = s$; the square is tight on all four sides but the triangle has only three vertices, so one vertex sits at a corner and the other two on the opposite sides. With the corner at $(0, s)$ and the others at $(u, 0)$, $(s, w)$, the squared side lengths are $u^2 + s^2$, $s^2 + (s - w)^2$ and $(s - u)^2 + w^2$. Writing $l_1 = u$, $l_2 = s - w$, this requires $l_1, l_2$ to be legs of $s$ (i.e. $l_i^2 + s^2$ a perfect square) together with $(s - l_1)^2 + (s - l_2)^2$ a perfect square.

Both families are generated from the Pythagorean legs of $s$ — the $p < s$ with $p^2 + s^2$ a square — read off from the divisor pairs $d dot (s^2 \/ d) = s^2$ of equal parity via $p = (s^2 \/ d - d) \/ 2$. A triangle can have integer $s$ only if its area is rational, so the (rare) tilted hits are confirmed by recomputing the true minimum exactly with rational arithmetic, taking the smallest feasible candidate of the edge-direction system. Summing over $s <= 10^6$ gives $T(10^6) = 4439835458570$, matching the given $T(40) = 346$, $T(400) = 76402$ and $T(2000) = 3237036$.

#pagebreak()
#link("https://projecteuler.net/problem=999")[= Problem 999: Alternating Recurrence]

Solution: 801096743

The sequence is given by $a_1 = a_2 = a_3 = 1$, $a_4 = 2$ and the alternating quadratic relation
$
a_n^2 = a_(n+2) a_(n-2) + u dot a_(n+1) a_(n-1), quad u = cases(1 quad &n "even", 2 quad &n "odd"),
$
equivalently $a_(n+2) = (a_n^2 - u a_(n+1) a_(n-1)) \/ a_(n-2)$. The terms grow like $exp(c n^2)$: this is an *elliptic divisibility (Somos-4 type) sequence*, with no linear recurrence, so reaching $a_N$ for $N = 10^18 + 3$ modulo the prime $P = 1234567891$ needs a sub-linear evaluation.

== Normalisation

Write $a_n = g(n) W_n$ to absorb the alternating coefficient into a gauge factor, leaving a *constant-coefficient* normalised EDS $W$ with $W_0 = 0$, $W_1 = 1$ and
$
W_(n+2) = (-sqrt(2) thin W_(n+1) W_(n-1) + W_n^2) \/ W_(n-2).
$
Seeking $a_n = kappa rho^n sigma^(n^2) omega^((-1)^n) W_n$ and matching the two coefficient values forces $rho = i$ (so $rho^2 = -1$) and $omega = 2^(-1\/8)$, giving the gauge $g(n) = i^(n-1)$ for odd $n$ and $g(n) = i^(n-1) 2^(-1\/4)$ for even $n$. The seeds become $W_2 = -i thin 2^(1\/4)$, $W_3 = -1$, $W_4 = 2 i thin 2^(1\/4)$, and $W_5 = -3$ from the recurrence. For *odd* $n$ the eighth-root cancels, so
$
a_n = i^(n-1) W_n,
$
with $W_n$ a rational integer (mod $P$); this was verified against the direct definition for $n = 1, dots, 20$, and reproduces the data points $a_13 = 23321$ and $a_1003 equiv 231906014 space (mod P)$.

== Working field

Let $theta = i thin 2^(1\/4)$. Then $theta^4 = i^4 dot 2 = 2$, while $W_2 = -theta$ and $sqrt(2) = -theta^2$. Every quantity that occurs is of the form $a + b theta + c theta^2 + d theta^3$ over $FF_P$, so arithmetic is polynomial multiplication reduced modulo $(theta^4 - 2, P)$. Odd-index $W_n$ are pure constants; even-index ones are multiples of $theta$. Crucially the doubling step below divides *only* by $W_2 = -theta$, and $theta$ is a unit ($theta^(-1) = theta^3 \/ 2$), so no irreducibility of $theta^4 - 2$ is required — the ring operations suffice.

== Block doubling

Maintain the length-8 window $V = [W_(c-3), dots, W_(c+4)]$ with $W_c$ at index $3$. The EDS duplication identities send a window centred at $c$ to the nine values $T_j = W_(2c + j)$ for $j = -3, dots, 5$; for example
$
W_(2c) = (W_(c+2) W_c W_(c-1)^2 - W_(c-2) W_c W_(c+1)^2) \/ W_2, quad W_(2c+1) = W_(c+2) W_c^3 - W_(c-1) W_(c+1)^3,
$
and the rest by index shifts. Reading the bits of $N$ below the leading one, bit $0$ keeps the sub-window $T[0:8]$ (taking $c arrow.r 2c$) and bit $1$ keeps $T[1:9]$ (taking $c arrow.r 2c + 1$). Starting from $c = 1$, this reaches $c = N$ in $O(log N)$ products and agrees with the direct recurrence on every tested $N$.

For $N = 10^18 + 3$ (odd), $N - 1 = 10^18 + 2 equiv 2 space (mod 4)$, so $i^(N-1) = -1$ and $a_N = -W_N$. The computation gives $a_N equiv 801096743 space (mod P)$ in well under a second.

#pagebreak()
#link("https://projecteuler.net/problem=1000")[= Problem 1000: Three Sub-Problems and a Meta-Problem]

Solution: 891213201

The landmark problem bundles three independent sub-problems whose answers $I(1000)$, $X(1000)$, $C(1000)$ seed a product-recurrence sequence; the final answer is $M(1000) mod p$ with $p = 10^9 + 7$.

== Sub-problem $I(n)$: Max And

We split ${1, dots, n}$ into $A, B$ and maximise $sum_(a in A) sum_(b in B) a and b$. Since $a and b$ is symmetric and counted once per crossing ordered pair, this is weighted *max-cut* on the complete graph with edge weight $i and b$. Decompose by bit $k$ (place value $2^k$): writing $s_i = plus.minus 1$ for the side of $i$, and $c_k$ for how many of $1, dots, n$ have bit $k$ set, the cut value is
$
1/4 sum_k 2^k (c_k^2 - d_k^2), quad d_k = sum_(i : "bit" k "of" i) s_i.
$
The $sum_k 2^k c_k^2$ term is fixed, so maximising the cut means *minimising* $sum_k 2^k d_k^2$. Each $d_k$ is a sum of $c_k$ terms $plus.minus 1$, so it has the parity of $c_k$ and its least possible square is $c_k mod 2$. That per-bit minimum is jointly attainable (there is ample freedom in the $s_i$; confirmed by brute force for every $n <= 12$), giving the closed form
$
I(n) = 1/4 (sum_k 2^k c_k^2 - sum_k 2^k (c_k mod 2)).
$
This reproduces $I(10) = 50$ and yields $I(1000) = 61217340$.

== Sub-problem $X(N)$: Max Xor Sum

With edge weight $[x, y] = x^2 xor y^2$, a valid sequence $a_0, dots, a_r$ is a walk in $K_N$ whose consecutive edge weights *strictly increase*, and we maximise their sum. Sort the $binom(N, 2)$ edges by weight and sweep upward, keeping $f[v]$, the best walk-sum that ends at vertex $v$ using only strictly lighter edges. An edge $(u, v, w)$ then offers $f[u] + w$ to $v$ and $f[v] + w$ to $u$. Edges of equal weight are applied as one batch from the pre-batch $f$, so two equal-weight edges never chain (the inequality is strict). The answer is $max_v f[v]$. This gives $X(4) = 71$, $X(10) = 702$, and $X(1000) = 728513240$.

== Sub-problem $C(N)$: Unreachable Nim

A status is *unreachable* if it can only ever be an initial position. Every $P$-position (nim-value $0$) is the target of a winning move from one of its (always $N$-position) predecessors, so all $P$-positions are reachable. An $N$-position is reached only from a $P$-position predecessor, because moving into an $N$-position is never a winning move. Increasing pile $a$ to $b xor c$ is the unique way to turn $(a, b, c)$'s predecessor into a $P$-position, and likewise for $b, c$; such a predecessor exists iff $b xor c > a$ (resp. $a xor c > b$, $a xor b > c$). Hence $(a, b, c)$ is unreachable exactly when $a xor b xor c eq.not 0$ together with $b xor c <= a$, $a xor c <= b$, $a xor b <= c$. Equality in any of these forces nim-value $0$, so the system is equivalently the strict, fully symmetric
$
a xor b < c, quad b xor c < a, quad c xor a < b,
$
counted over $[0, N)^3$ by a bit-wise digit DP that tracks, per inequality, whether the prefix is already less, equal, or greater. This matches the given $C(10) = 123$ and gives $C(1000) = 232607184$.

== Meta-problem

With $M(0) = I$, $M(1) = X$, $M(2) = C$ and $M(k) = M(k-1) M(k-2) M(k-3)$, every $M(k) = I^(e_0) X^(e_1) C^(e_2)$ where the exponent triples follow the tribonacci recurrence from $(1,0,0), (0,1,0), (0,0,1)$. Reducing the exponents $mod (p - 1)$ (Fermat) and combining with modular powers gives the result. The supplied check $M(4) = I dot X^2 dot C^2 equiv 457587170 space (mod p)$ holds, confirming all three values, and $M(1000) equiv 891213201 space (mod p)$.
