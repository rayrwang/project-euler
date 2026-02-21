
#set text(font: "Inter")
#set document(
  title: [Project Euler Solutions],
)

#align(center)[
  #title()
  Raymond Wang
]
#outline()

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
