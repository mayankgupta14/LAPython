from math import pi
import os
#DIGIT = 3
#print(pi)
digit = int(os.getenv("DIGIT", 10))

print("%.*f" % (digit, pi))
