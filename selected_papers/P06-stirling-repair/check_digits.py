"""Independent direct Stirling-triangle checks for the digit congruence."""
from collections import defaultdict

checks = 0
for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
    targets = defaultdict(list)
    for k in range(1, 351):
        q, r = 1, 0
        while q <= 700:
            targets[k - 1 + q].append((k, r))
            q *= p
            r += 1
    row = [1] + [0] * 350
    for n in range(1, max(targets) + 1):
        row = [0] + [(j * row[j] + row[j - 1]) % p for j in range(1, 351)]
        for k, r in targets[n]:
            tail = (k - 1) // p
            predicted = 1
            for _ in range(r):
                predicted = predicted * (tail % p + 1) % p
                tail //= p
            assert row[k] == predicted, (p, k, r, row[k], predicted)
            checks += 1
print(f'PASS: {checks} direct Stirling-triangle digit congruences')
