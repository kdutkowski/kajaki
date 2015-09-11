set datafile separator ","
set term png
set output "results/25.png"

f(x) = a*x**6 + g

a = -1
b = 1
c = 1
d = 1
e = 1
f = 1
g = 0

fit f(x) 'results/results.csv' using 0:2 via a,g
plot f(x), 'results/results.csv' using 0:2:xtic(1)