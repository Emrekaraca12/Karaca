def solve(numheads, numlegs):
    for c in range(numheads + 1):
            r = numheads - c
            if (2 * c + 4 * r) == numlegs:
                return c, r
            
    return None

numheads = 35
numlegs = 94
print(solve(numheads, numlegs)) #(23, 12)