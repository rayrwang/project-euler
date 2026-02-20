
#outline()

= Problem 932: $2025$

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
