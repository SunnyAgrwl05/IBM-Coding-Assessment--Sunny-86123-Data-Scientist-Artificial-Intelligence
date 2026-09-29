# IBM Coding Assessment – Sunny Kumar

This folder contains solutions and explanations for two coding problems from the IBM Coding Assessment.

## Problems

### Question 1 – Maximum XOR Sum

Given two integer arrays `arr1` and `arr2` of equal length `n`, consider every possible pair `(i, j)` and compute:

```
arr1[i] XOR arr2[j]
```

The task is to return the sum of all these XOR values.

#### Example

For:

```
arr1 = [1, 2, 3]
arr2 = [10, 10, 10]
```

The conceptual matrix is:

```
11  11  11
8    8   8
9    9   9
```

Therefore:

```
11 + 11 + 11 + 8 + 8 + 8 + 9 + 9 + 9 = 84
```

#### Solution

A direct solution would construct an `n × n` matrix and require `O(n²)` operations.

Instead, process every bit independently.

For a particular bit:

- `ones1` = number of elements in `arr1` having that bit set.
- `ones2` = number of elements in `arr2` having that bit set.
- An XOR bit is 1 when the corresponding bits are different.

Therefore, the number of pairs contributing this bit is:

```
ones1 * (n - ones2) + (n - ones1) * ones2
```

Multiply this count by the bit value and add it to the answer.

#### Complexity

- Time: `O(31 × n)`, effectively `O(n)`
- Space: `O(1)`

---

### Question 2 – Checksum Aggregation

For every ordered pair `(i, j)` where:

```
1 <= i <= n
1 <= j <= n
```

the checksum is:

```
C(i, j) = i % j + j % i
```

Return the sum of all checksums modulo:

```
10^9 + 7
```

#### Example

For `n = 2`:

```
C(1,1) = 0
C(1,2) = 1
C(2,1) = 1
C(2,2) = 0
```

Total:

```
0 + 1 + 1 + 0 = 2
```

For `n = 3`, the result is `10`.

For `n = 4`, the result is `24`.

#### Solution

The function is symmetric:

```
C(i,j) = C(j,i)
```

So we can calculate only the pairs where `i > j` and multiply the result by 2.

For `i > j`:

```
j % i = j
```

so:

```
C(i,j) = i % j + j
```

For a fixed `j`, the sum of:

```
1 % j + 2 % j + ... + n % j
```

can be computed using quotient and remainder instead of iterating through every `i`.

Let:

```
n = q * j + r
```

Then:

```
sum(i % j)
= q * j * (j - 1) / 2
  + r * (r + 1) / 2
```

The part corresponding to `i <= j` is removed, leaving only `i > j`.

#### Complexity

- Time: `O(n)`
- Space: `O(1)`

The implementation avoids the `O(n²)` brute-force pair enumeration.

---

## Language

Python 3

## Files

- `question1_maximum_xor_sum.py` – Bit-counting solution
- `question2_checksum_aggregation.py` – Mathematical/modular arithmetic solution
