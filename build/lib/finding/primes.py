def find_candidates(n):
    candidates = []
    for i in range(floor(sqrt(n) - log(n, 2)), floor(sqrt(n) + log(n, 2))):
        if i % 2 is 0: continue
        if n % i is 0: candidates.append(i)
    return candidates
