
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
#link("https://projecteuler.net/problem=315")[= Problem 315: Digital Root Clocks]

Solution: 13625242

Two seven-segment clocks each display a number, then repeatedly its digit sum down to a single digit, beginning and ending blank. Sam's clock clears and relights every segment at each step; Max's only toggles the segments that change. The answer is Sam's total segment transitions minus Max's, summed over the primes in $[10^7, 2 dot 10^7)$.

Sieve that prime range rather than testing each number for primality, and compute both transition counts per prime with integer digit arithmetic. For a step $a -> b$, Sam's cost is the total lit-segment count of $a$ plus that of $b$, while Max's cost is the sum over aligned digit positions of the population count of the segment-pattern XOR (a blank screen contributing the all-off pattern).

#pagebreak()
#link("https://projecteuler.net/problem=317")[= Problem 317: Firecracker]

Solution: 1856532.8455

A firecracker bursts at height $h_0 = 100$; its fragments scatter in every direction at speed $v = 20$ and then fall under gravity $g = 9.81$. We want the volume of the region their paths sweep before landing.

Each fragment follows a parabolic arc, and over all launch directions the family of trajectories has as its envelope the _parabola of safety_,
$ Y(r) = h_0 + v^2/(2 g) - (g r^2)/(2 v^2), $
the greatest height reachable at horizontal distance $r$. The swept solid is everything between the ground and this envelope, revolved about the vertical axis. Writing $A = h_0 + v^2/(2 g)$ for the apex height and $B = g/(2 v^2)$, the envelope meets the ground at $r_max^2 = A\/B$, and the shell integral collapses:
$ V = integral_0^(r_max) 2 pi r (A - B r^2) dif r = (pi A^2)/(2 B) = (pi A^2 v^2)/g approx 1856532.8455. $

#pagebreak()
#link("https://projecteuler.net/problem=321")[= Problem 321: Swapping Counters]

Solution: 2470433131948040

With $n$ red and $n$ blue counters at opposite ends of a row of $2 n + 1$ squares (one empty square between them), $M(n)$ is the fewest slides and hops needed to swap the two colours. We want the sum of the first forty values of $n$ for which $M(n)$ is a triangular number.

First, $M(n) = n^2 + 2 n$: each of the $2 n$ counters must advance $n + 1$ squares, giving $2 n (n + 1)$ square-steps; a hop advances two squares and a slide one, and the $n^2$ red–blue meetings are exactly the hops, leaving $2 n$ slides, so $M(n) = 2 n (n + 1) - n^2 = n^2 + 2 n$ (indeed $M(3) = 15$). Requiring $n^2 + 2 n = k (k + 1) \/ 2$ and completing the square turns this into the Pell-like equation
$ m^2 - 8 u^2 = -7, quad u = n + 1, space m = 2 k + 1. $
Its positive solutions split into two classes, generated from the fundamentals $(m, u) = (1, 1)$ and $(5, 2)$ by the unit $3 + sqrt(8)$, that is $(m, u) |-> (3 m + 8 u, m + 3 u)$. Merging the resulting $u$-values in increasing order (dropping $u = 1$) gives $n = u - 1 = 1, 3, 10, 22, 63, dots$; the first five sum to $99$ and the first forty to the answer.

#pagebreak()
#link("https://projecteuler.net/problem=323")[= Problem 323: Bitwise-OR Operations on Random Integers]

Solution: 6.3551758451

Each step ORs in a random $32$-bit integer; the expected number of steps is $sum i dot p(i)$, where $p(i)$ comes from differencing the closed-form chance that all bits are set by step $i$.

#pagebreak()
#link("https://projecteuler.net/problem=329")[= Problem 329: Prime Frog]

Solution: 199740353/29386561536000

A frog hops left or right with equal probability among squares $1$ to $500$ (bouncing back at the ends), croaking just before each hop: on a prime square it croaks P with probability $2\/3$ and N with $1\/3$, on a non-prime square the reverse. From a uniformly random start, we want the probability that its first fifteen croaks spell PPPPNNPPPNPPNPN, as a reduced fraction.

Keep the arithmetic exact with an integer weight per square. A croak contributes numerator $2$ when the square's prime-ness matches the target letter and $1$ otherwise, each over a factor of $3$; a hop contributes $1\/2$ to each neighbour, and a forced hop off an end has probability $1 = 2 dot 1\/2$, so it carries numerator $2$. Every length-$15$ path then shares the denominator $500 dot 3^15 dot 2^14$, and a single forward sweep over the croaks accumulates the path-weight numerators across all squares. Reducing numerator against denominator gives the fraction.

#pagebreak()
#link("https://projecteuler.net/problem=333")[= Problem 333: Special Partitions]

Solution: 3053105

A partition of $n$ into parts $2^i 3^j$ is _valid_ when no part divides another; $P(n)$ counts the valid partitions. We want the sum of the primes $q < 10^6$ with $P(q) = 1$.

Since $2^i 3^j divides 2^k 3^l$ iff $i <= k$ and $j <= l$, a valid partition is an _antichain_ in the divisibility poset: its lattice points $(i, j)$ have strictly increasing $i$ as $j$ strictly decreases. Sweeping the powers of three from high to low, each column contributes at most one part, whose exponent $i$ must exceed every $i$ chosen so far. The DP state is (largest $i$ used, running sum); a prefix sum along the "largest $i$" axis injects all earlier states with a smaller $i$ in one pass, and counts are clamped at $2$ since only $P(q) = 1$ matters. As a check, $sum_(q < 100, P(q) = 1) q = 233$ and $P(11) = 2$, $P(17) = 1$.

#pagebreak()
#link("https://projecteuler.net/problem=340")[= Problem 340: Crazy Function]

Solution: 291504964

With $F(n) = n - c$ for $n > b$ and $F(n) = F(a + F(a + F(a + F(a + n))))$ otherwise, we need the last nine digits of $S(a, b, c) = sum_(n=0)^b F(n)$ for $a = 21^7$, $b = 7^21$, $c = 12^7$ (note $a > c$).

For $n in (b - a, b]$ we have $a + n > b$, so the innermost call gives $a + n - c$; since $a > c$ each successive argument also exceeds $b$, and the four levels unwind to $F(n) = n + 4a - 4c$. Inductively, for $n in (b - (k+1)a, b - k a]$,
$ F(n) = n + 4(k+1)a - (3k+4)c. $
Writing $m = floor(b\/a)$, the sum splits into the partial bottom block $[0, b - m a]$ (using $k = m$) plus the full blocks $k = 0, ..., m-1$, each contributing $P_k = a b - a(a-1)\/2 + (3k+4)a(a-c)$. Everything is evaluated with exact integers and reduced mod $10^9$ only at the end, sidestepping modular-division issues. The example $S(50, 2000, 40) = 5204240$ (with $F(0) = 3240$, $F(2000) = 2040$) matches a direct recursive evaluation over the whole range.

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
#link("https://projecteuler.net/problem=351")[= Problem 351: Hexagonal Orchards]

Solution: 11762187201804552

In a hexagonal orchard of order $n$ (a triangular lattice of points inside a regular hexagon of side $n$), $H(n)$ counts the points hidden from the centre by a nearer point. We want $H(10^8)$.

A point is hidden exactly when it is not the closest lattice point along its ray, i.e. when its coordinates are not coprime. By the six-fold symmetry the lattice splits into six sectors, and at radial index $i$ the visible points in a sector are the $phi(i)$ with coprime coordinates, leaving $i - phi(i)$ hidden. Hence
$ H(n) = 6 sum_(i=1)^n (i - phi(i)) = 6 ((n (n + 1))/2 - Phi(n)), quad Phi(n) = sum_(i=1)^n phi(i). $
The totient summatory function $Phi$ is evaluated sublinearly from the identity $sum_(d=1)^n Phi(floor(n\/d)) = n(n+1)\/2$, giving
$ Phi(n) = (n (n + 1))/2 - sum_(d=2)^n Phi(floor(n\/d)), $
grouped over equal values of $floor(n\/d)$ and seeded by a sieve of $phi$ (hence $Phi$) for all arguments up to about $n^(2\/3)$. The checks $H(5) = 30$, $H(10) = 138$, $H(1000) = 1177848$ all hold.

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
#link("https://projecteuler.net/problem=365")[= Problem 365: A Huge Binomial Coefficient]

Solution: 162619462356610313

Let $M(n, k, m) = binom(n, k) mod m$. We want $sum M(10^18, 10^9, p q r)$ over prime triples $1000 < p < q < r < 5000$.

There are $501$ primes in that range. For each prime $p$, $binom(10^18, 10^9) mod p$ is computed by Lucas' theorem: writing both numbers in base $p$ (about five or six digits), the result is the product of $binom(n_i, k_i) space (mod p)$ over digits, each evaluated from factorial and inverse-factorial tables mod $p$. With those residues in hand, every triple's value mod $p q r$ follows from the Chinese Remainder Theorem on the squarefree modulus. Precomputing a table of $p_j^(-1) space (mod p_i)$ turns the inner CRT into a few multiplications, so the roughly $binom(501, 3) approx 2.1 dot 10^7$ triples are summed quickly.

#pagebreak()
#link("https://projecteuler.net/problem=381")[= Problem 381: (prime-k) Factorial]

Solution: 139602943319822

For a prime $p$, $S(p) = (sum_(k=1)^5 (p-k)!) mod p$; we want $sum S(p)$ for $5 <= p < 10^8$.

By Wilson's theorem $(p-1)! equiv -1 space (mod p)$, and dividing successively by $p-1, p-2, ...$ (each $equiv -1, -2, ...$) gives $(p-k)! equiv (-1)^k\/(k-1)! space (mod p)$. Summing the five terms,
$ S(p) equiv -1 + 1 - 1/2 + 1/6 - 1/24 = -3/8 space (mod p). $
Solving $8x equiv -3 space (mod p)$ yields a closed form by residue: $S(p) = (3p-3)\/8$, $(p-3)\/8$, $(7p-3)\/8$, $(5p-3)\/8$ for $p equiv 1, 3, 5, 7 space (mod 8)$ respectively. A sieve to $10^8$ then sums these (checked against $sum S(p) = 480$ for $p < 100$).

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
#link("https://projecteuler.net/problem=407")[= Problem 407: Idempotents]

Solution: 39782849136421

For each $n$ let $M(n)$ be the largest $a < n$ with $a^2 equiv a space (mod n)$ — an _idempotent_ — and we want $sum_(n=1)^(10^7) M(n)$.

The congruence $a^2 equiv a$ means $n divides a(a-1)$. Since $a$ and $a-1$ are coprime, each prime power $p^e$ dividing $n$ must divide $a$ or $a-1$ entirely, i.e. $a equiv 0$ or $a equiv 1 space (mod p^e)$. By the Chinese remainder theorem an idempotent is exactly a choice of $0$ or $1$ on each of the $omega(n)$ prime-power factors, giving $2^(omega(n))$ of them.

So the work per $n$ is: factor $n$ into prime powers $q_1, ..., q_m$ with a smallest-prime-factor sieve; build the CRT basis $e_i$ (the value that is $1 space (mod q_i)$ and $0$ on the others, computed as $(n\/q_i) dot (n\/q_i)^(-1) mod q_i$); and take the maximum of the $2^m$ subset sums $sum_(i in S) e_i mod n$. The all-empty choice gives $0$ and the all-ones choice gives $1$, so prime powers correctly yield $M = 1$; the largest subset sum below $n$ is $M(n)$. As checks, $M(6) = 4$, $sum_(n<=20) M = 75$ and $sum_(n<=100) M = 2549$. The $2^(omega(n))$ subsets sum to roughly $10^8$ across the whole range, so the sieve-and-enumerate runs in a few seconds.

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
#link("https://projecteuler.net/problem=425")[= Problem 425: Prime Connection]

Solution: 46479497324

Two primes are _connected_ if they have the same number of digits and differ in exactly one position, or if one is obtained from the other by prepending a single digit. A prime $P$ is a _2's relative_ if there is a chain of connected primes from $2$ to $P$ in which no prime exceeds $P$, and $F(N)$ sums the primes $p <= N$ that are _not_ relatives.

The "no prime exceeds $P$" rule is the whole trick: a prime's relative-status depends only on smaller primes. So sieve to $N$, process the primes in increasing order, and maintain a union--find structure. When prime $p$ is reached, join it to every already-seen (hence smaller) prime it connects to: for the same-length case, vary each of its digits and check whether the resulting smaller number is prime; for the prepend case, strip $p$'s leading digit and, if the remaining tail is a prime with no leading zero, join the two. Looking only "downward" to smaller primes both enforces the chain constraint automatically and avoids handling each connection twice. After the joins, $p$ is a relative exactly when it shares a component with $2$; otherwise its value is added to the running total. This reproduces $F(10^3) = 431$ and $F(10^4) = 78728$.

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
#link("https://projecteuler.net/problem=435")[= Problem 435: Polynomials of Fibonacci Numbers]

Solution: 252541322550

The polynomial $F_n (x) = sum_(i=0)^n f_i x^i$ uses the Fibonacci numbers as coefficients, and we want $sum_(x=0)^100 F_n (x)$ for $n = 10^15$, modulo $15!$. Because the Fibonacci generating function is $sum_(i >= 0) f_i x^i = x \/ (1 - x - x^2)$, multiplying the partial sum by $1 - x - x^2$ telescopes (every interior coefficient $f_k - f_(k-1) - f_(k-2)$ vanishes), leaving only boundary terms:
$
F_n (x) = (f_(n+1) x^(n+1) + f_n x^(n+2) - x) / (x^2 + x - 1).
$
The denominator $D = x^2 + x - 1$ is nonzero for every integer $x$, but it need not be invertible modulo the composite $15!$. The fix exploits that $F_n (x)$ is a genuine integer, so the numerator equals $D dot F_n (x)$ exactly: computing it modulo $m D$ yields $D dot (F_n (x) space (mod m))$, and an ordinary integer division by $D$ recovers $F_n (x) space (mod m)$. Each Fibonacci pair $f_n, f_(n+1)$ comes from fast doubling and each power from fast exponentiation, all mod $m D$. The closed form reproduces $F_7(11) = 268357683$.

#pagebreak()
#link("https://projecteuler.net/problem=437")[= Problem 437: Fibonacci Primitive Roots]

Solution: 74204709657207

A Fibonacci primitive root $g$ of $p$ satisfies $g^(n+2) equiv g^(n+1) + g^n$, i.e. $g^2 equiv g + 1$, while also being a primitive root. So $g$ must be a root of $x^2 - x - 1$ in $FF_p$, which requires $5$ to be a quadratic residue: either $p = 5$ or $p equiv plus.minus 1 space (mod 5)$. For such $p$ the two roots are $(1 plus.minus sqrt(5)) \/ 2$, and $p$ qualifies exactly when at least one of them is a primitive root.

There is no simple congruence test for this (the density is of Artin type), so each candidate prime is checked directly: take $sqrt(5)$ via Tonelli--Shanks (a single power when $p equiv 3 space (mod 4)$), form the two roots, factor $p - 1$ by trial division against the primes up to $10^4$ (the leftover cofactor, if any, is prime since $p - 1 < 10^8$), and test primitivity through $g^((p-1)\/q) != 1$ for every prime $q | p-1$. Sieving the primes below $10^8$ and running this in compiled code reproduces the stated $323$ primes below $10^4$ summing to $1480491$, and finishes the full range in a few seconds.

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
#link("https://projecteuler.net/problem=463")[= Problem 463: A Weird Recurrence Relation]

Solution: 808981553

The four cases of $f$ combine neatly: summing one block of four gives $f(4n) + f(4n+1) + f(4n+2) + f(4n+3) = 6 f(2n+1) - 2 f(n)$. Checking small values reveals what $f$ really is -- the _binary bit-reversal_ of $n$: writing $n$ with $b = floor(log_2 n) + 1$ bits and reversing them. Indeed $f(8) = f(1000_2) = 0001_2 = 1$ and $f(5) = f(101_2) = 101_2 = 5$, matching the recurrence.

So $S(N) = sum_(i=1)^N "rev"(i)$. The $b$-bit numbers $[2^(b-1), 2^b - 1]$ reverse onto every $b$-bit pattern whose leading bit is set, and a short computation shows their reversals sum to exactly $4^(b-1)$; the full groups for $b = 1, dots, B-1$ (with $B = $ bit length of $N$) therefore contribute $sum_(b=1)^(B-1) 4^(b-1)$. The top group $[2^(B-1), N]$ is partial, so its reversal sum is taken bit by bit: bit $k$ contributes $2^(B-1-k)$ times the number of in-range integers with that bit set, each count obtained in closed form. This reproduces $S(8) = 22$ and $S(100) = 3604$, and $S(3^37) space (mod 10^9)$ follows instantly.

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
#link("https://projecteuler.net/problem=518")[= Problem 518: Prime Triples and Geometric Sequences]

Solution: 100315739184392

We want $S(n) = sum (a + b + c)$ over prime triples $a < b < c < n$ for which $a + 1$, $b + 1$, $c + 1$ form a geometric progression, with $n = 10^8$.

Every positive-integer geometric progression can be written $(k y^2, k x y, k x^2)$ with $x > y >= 1$ and $gcd(x, y) = 1$ (the middle term squared equals the product of the outer two). Setting
$
a = k y^2 - 1, quad b = k x y - 1, quad c = k x^2 - 1,
$
the ordering $a < b < c$ is automatic from $y < x$, and we need all three prime with $c < n$. Sieve primes up to $n$, then loop over $x$ (up to $sqrt(n)$), over $k$ with $k x^2 <= n$, prune on $c = k x^2 - 1$ being prime, and finally over coprime $y < x$ checking $a$ and $b$. As a check, $S(100) = 1035$ from the eleven listed triples.

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
#link("https://projecteuler.net/problem=540")[= Problem 540: Counting Primitive Pythagorean Triples]

Solution: 500000000002845

$P(n)$ counts primitive Pythagorean triples $a < b < c <= n$. Primitive triples are parametrised bijectively by pairs $(m, k)$ with $m > k >= 1$, $gcd(m, k) = 1$ and $m, k$ of opposite parity, through $c = m^2 + k^2$. So $P(N)$ counts such pairs with $m^2 + k^2 <= N$.

Look at the coprime pairs with $m > k >= 1$ and $m^2 + k^2 <= N$. Being coprime rules out both even, so each is either both-odd or mixed-parity, and the primitive ones are exactly the mixed-parity ones. Therefore $P(N) = C - D$ with $C$ the count of all coprime pairs and $D$ the count of coprime both-odd pairs. Removing the coprimality constraint by Möbius inversion,
$
C = sum_(d) mu(d) T(floor(N\/d^2)), quad D = sum_(d "odd") mu(d) T_"odd"(floor(N\/d^2)),
$
where $T(X) = \#{(a, b) : a > b >= 1, a^2 + b^2 <= X}$ and $T_"odd"$ restricts to both $a, b$ odd. Each of $T$ and $T_"odd"$ is read off a quarter-disc lattice count in $O(sqrt(X))$ (summing $floor(sqrt(X - a^2))$ over $a$), and the Möbius sums need $mu(d)$ for $d <= sqrt(N)$. Checks: $P(20) = 3$ and $P(10^6) = 159139$.

#pagebreak()
#link("https://projecteuler.net/problem=549")[= Problem 549: Divisibility of Factorials]

Solution: 476001479068717

Let $s(n)$ be the smallest $m$ with $n | m!$, and $S(n) = sum_(i=2)^n s(i)$; we need $S(10^8)$.

Writing $n = product p^e$, the factorial $m!$ must absorb each prime power independently, and the binding requirement is the largest, so $s(n) = max_(p^e || n) s(p^e)$. For a single prime power, $s(p^e)$ is the smallest multiple $m$ of $p$ at which $v_p(m!)$ reaches $e$ (the exponent $v_p(m!)$ only grows as $m$ passes multiples of $p$).

This gives a single modified sieve. A slot still holding $0$ marks a prime $p$; walking $m = p, 2p, 3p, dots$ and accumulating $c = v_p(m!)$, each time $c$ climbs past an integer $k$ the value $s(p^k)$ equals the current $m$, so we raise $s[j]$ to $m$ for every multiple $j$ of $p^k$. Composite slots are filled in by their smallest prime before they are reached, exactly as in the sieve of Eratosthenes, and summing the array yields $S(N)$. The total update work is $sum_p sum_k N\/p^k = O(N log log N)$. As a check, $S(100) = 2012$.

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
#link("https://projecteuler.net/problem=622")[= Problem 622: Riffle Shuffles]

Solution: 3010983666182123972

A perfect riffle (faro out-) shuffle of an even deck of size $n$ moves the card at position $i$ to position $2i mod (n-1)$, fixing the two ends. The number of shuffles needed to restore the deck is therefore the multiplicative order of $2$ modulo $n - 1$:
$
s(n) = "ord"_(n-1)(2).
$
We want the sum of all $n$ with $s(n) = 60$. Setting $m = n - 1$ (odd), the condition is $"ord"_m(2) = 60$: equivalently $m | 2^60 - 1$ while $m$ divides none of $2^t - 1$ for the maximal proper divisors $t in {30, 20, 12}$ of $60$ (any proper divisor of $60$ divides one of these). Every divisor of $2^60 - 1$ is odd, so $n = m + 1$ is automatically even. We factor $2^60 - 1 = 3^2 dot 5^2 dot 7 dot 11 dot 13 dot 31 dot 41 dot 61 dot 151 dot 331 dot 1321$, enumerate its divisors, keep those of exact order $60$, and sum $n = m + 1$. The analogous computation reproduces the given $s(n) = 8$ total of $412$.

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
#link("https://projecteuler.net/problem=657")[= Problem 657: Incomplete Words]

Solution: 219493139

A word over an alphabet of $alpha$ letters is incomplete if it omits at least one letter; $I(alpha, n)$ counts incomplete words of length at most $n$. We want $I(10^7, 10^12)$ modulo $10^9 + 7$.

Classify words by the number $i$ of distinct letters they actually use. The number of words of length $<= M$ confined to a fixed $i$-letter sub-alphabet is $sum_(j=0)^M i^j$, and there are $binom(N, i)$ such sub-alphabets; inclusion-exclusion over $i$ then gives
$
I(N, M) = sum_(i=0)^(N-1) (-1)^(N-1-i) binom(N, i) sum_(j=0)^M i^j.
$
The geometric inner sum is $(i^(M+1) - 1) \/ (i - 1)$ for $i >= 2$, equals $M + 1$ for $i = 1$, and equals $1$ for $i = 0$. The powers $i^(M+1)$ are taken modulo $p$ with the exponent reduced modulo $p - 1$ by Fermat, and the binomial coefficients are streamed multiplicatively, so the whole sum is one $O(N log M)$ pass. Checks: $I(3,0) = 1$, $I(3,2) = 13$, $I(3,4) = 79$.

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
#link("https://projecteuler.net/problem=808")[= Problem 808: Reversible Prime Squares]

Solution: 3807504276997394

A reversible prime square is the square of a prime that is not a palindrome and whose digit reversal is also the square of a prime. Because squares grow with their root, iterating primes in increasing order yields these in increasing order too. Sieve primes up to about $3.2 dot 10^7$ (where the fiftieth occurs); for each prime $p$, reverse $p^2$, and if the reversal is a perfect square whose root is prime, count $p^2$. Stop at the fiftieth and sum.

#pagebreak()
#link("https://projecteuler.net/problem=810")[= Problem 810: XOR-Primes]

Solution: 124136381

The XOR-product is carry-less binary multiplication: long multiplication in base $2$ with the partial results combined by XOR rather than addition. This is exactly multiplication of polynomials over $"GF"(2)$, identifying an integer with the polynomial whose coefficients are its binary digits. An XOR-prime, an integer $> 1$ that is not an XOR-product of two integers $> 1$, is therefore an irreducible polynomial over $"GF"(2)$ of degree $>= 1$, read back as an integer. The first few are $2, 3, 7, 11, 13, dots$ (that is $X, X + 1, X^2 + X + 1, X^3 + X + 1, X^3 + X^2 + 1$), with $41$ the tenth.

A polynomial of degree $d$ has integer value in $[2^d, 2^(d+1))$, so ordering the XOR-primes by value is the same as ordering by degree and then by value within a degree. The number of monic irreducibles of degree $d$ over $"GF"(2)$ is $L(d) = 1/d sum_(e divides d) mu(e) 2^(d\/e)$. Accumulating $L(d)$, the running total first passes $5 dot 10^6$ at degree $26$ (the $5{,}000{,}000$th lies $2{,}192{,}804$ entries into degree $26$, value in $[2^26, 2^27)$), so sieving up to $N = 2^27$ captures it.

== Computation

A carry-less sieve marks every XOR-composite below $N$. Any composite of degree $<= 26$ has a factor of degree $<= 13$, so it suffices to run $p$ over the still-unmarked values (the XOR-primes) with $deg p <= 13$, and for each mark $p times.circle q$ for every $q >= 2$ with $deg p + deg q <= 26$. The carry-less product uses the shift-and-XOR loop $r arrow.l r xor a$ while shifting $a$ left and $b$ right. The unmarked values $>= 2$, taken in increasing order, are the XOR-primes; the $5{,}000{,}000$th is $124136381$. The sieve runs in a few seconds.

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
#link("https://projecteuler.net/problem=932")[= Problem 932: $2025$]

Solution: 72673459417881349

A $2025$-number $N$ splits into a leading part $a$ and a trailing part $b$ (with $b$ having a fixed digit length and no leading zero) such that $N = (a + b)^2$. Writing $s = a + b$, every such $N$ is simply $s^2$, so iterate over $s$ rather than over the parts: for each split position $k$, set $a = floor(N \/ 10^k)$ and $b = N mod 10^k$, and accept when $a + b = s$ and $b$ has exactly $k$ digits.

A cheap filter cuts the search by more than four-fifths. Since $10^k equiv 1 space (mod 9)$, we have $N = a dot 10^k + b equiv a + b = s space (mod 9)$; combined with $N = s^2$ this forces $s^2 equiv s$, i.e. $s equiv 0$ or $1 space (mod 9)$. Only those $s$ need be examined.

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
#link("https://projecteuler.net/problem=974")[= Problem 974: Very Odd Numbers]

Solution: 13313751171933973557517973175

A very odd number uses only the digits $1, 3, 5, 7, 9$, is divisible by $105 = 3 dot 5 dot 7$, and each odd digit occurs an odd number of times — zero occurrences being even, all five digits must appear, so the length is a sum of five odd numbers and is itself odd. (No $5$-digit example exists: a permutation of ${1,3,5,7,9}$ has digit sum $25$, not divisible by $3$, which is why $Theta(1)$ has seven digits.)

Divisibility by $105$ is tracked as a single residue: appending digit $d$ maps $r arrow.r (10r + d) mod 105$, which subsumes the mod $3$, mod $5$ and mod $7$ conditions at once (in particular the final digit is forced to be $5$ automatically). The DP state is the pair (parity mask of the five digits, residue), only $32 times 105$ states. A backward table $g[m]["mask"][r]$ counts length-$m$ completions that finish at full mask and residue $0$; lengths are capped at $45$, far above the $29$ digits actually needed for the $10^16$th element.

The $n$th very odd number is then constructed by first selecting the length (subtracting whole-length counts $g[ell][0][0]$ for $ell = 5, 7, 9, dots$) and then choosing digits most-significant-first, descending into the unique branch where the running count first reaches $n$. The construction reproduces $Theta(1) = 1117935$, $Theta(10^3) = 11137955115$ and a brute-force list of the smallest cases, and yields $Theta(10^16) = 13313751171933973557517973175$.

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
#link("https://projecteuler.net/problem=991")[= Problem 991: Fruit Salad]

Solution: 23871972654940

With $(a, b, c) = (#emoji.apple.red, #emoji.banana, #emoji.pineapple)$ the equation is $a \/ (b+c) + b \/ (c+a) + c \/ (a+c) = 4$. The second and third fractions share the denominator $a + c$ (the twist versus the classic elliptic-curve meme), so it collapses to $a \/ s + s \/ (a + c) = 4$ with $s = b + c$, hence $a + c = s^2 \/ (4s - a)$: writing $d = 4s - a$ we need $d | s^2$, and then $a = 4s - d$, $c = s^2 \/ d - a$, $b = s - c$.

Pairs $(s, d)$ with $d | s^2$ are exactly $d = e^2 m$, $s = e m k$ with $gcd(e, k) = 1$ (take $g = gcd(d, s)$, $e = d \/ g$, $m = g \/ e$, $k = s \/ g$; then $d | s^2$ iff $e | g$). In these coordinates everything is linear in $m$:
$ a = e m (4k - e), space b = m(5 e k - k^2 - e^2), space c = m(k^2 - 4 e k + e^2), space a + b + c = e m (5k - e). $

Positivity restricts $k \/ e$ to the two bands $(1\/4, 2 - sqrt(3))$ and $(2 + sqrt(3), (5 + sqrt(21)) \/ 2)$, and $e m (5k - e) <= 10^7$ caps $e$ at a few thousand. For each coprime $(e, k)$ in the bands every $m <= M = floor(10^7 \/ (e(5k - e)))$ is a solution, contributing $e(5k - e) M(M+1) \/ 2$. Verified against brute force over all triples and over $(s, d)$ pairs up to limit $20000$; the total is $23871972654940$.

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
