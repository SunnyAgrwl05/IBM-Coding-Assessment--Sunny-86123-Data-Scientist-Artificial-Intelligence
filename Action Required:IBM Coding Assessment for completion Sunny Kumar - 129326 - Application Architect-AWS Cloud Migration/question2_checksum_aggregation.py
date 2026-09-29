def computeChecksumAggregation(n):
    MOD = 10**9 + 7
    ans = 0

    for j in range(1, n + 1):
        q, r = divmod(n, j)

        # Sum of i % j for i = 1..n.
        total = q * j * (j - 1) // 2
        total += r * (r + 1) // 2

        # Keep only i > j.
        total -= j * (j - 1) // 2

        # For i > j, j % i = j.
        ans += total + (n - j) * j

    return (2 * ans) % MOD
