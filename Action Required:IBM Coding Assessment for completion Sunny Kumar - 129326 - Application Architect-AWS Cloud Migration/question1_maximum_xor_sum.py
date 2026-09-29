def maximumXorSum(arr1, arr2):
    MOD = 10**9 + 7
    n = len(arr1)
    ans = 0

    # Values are <= 10^9, so 31 bits are sufficient.
    for bit in range(31):
        mask = 1 << bit

        ones1 = sum(1 for x in arr1 if x & mask)
        ones2 = sum(1 for x in arr2 if x & mask)

        # XOR bit is 1 when the two bits are different.
        pairs = ones1 * (n - ones2) + (n - ones1) * ones2

        ans = (ans + pairs * mask) % MOD

    return ans
