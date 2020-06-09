x = 2
y = 2
z = 2
n = 2
print([[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n])