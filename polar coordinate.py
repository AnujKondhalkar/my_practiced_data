# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase,polar
STDIN=complex(input())
print(abs(STDIN))
print(phase(complex(STDIN)))
print(polar(complex(STDIN)))
