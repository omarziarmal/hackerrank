# Day 29: Bitwise AND

### Objective

Welcome to the last day! Today, we're discussing bitwise operations. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-bitwise-and/tutorial) tab for learning materials and an instructional video!

### Task

Given set _S = {1,2,3,...,N}_. Find two integers, _A_ and _B_ (where _A < B_), from set _S_ such that the value of _A&B_ is the maximum possible and also less than a given integer, _K_. In this case, _&_ represents the bitwise AND operator.

### Input Format

The first line contains an integer, _T_, the number of test cases.
Each of the _T_ subsequent lines defines a test case as **2** space-separated integers, _N_ and _K_, respectively.

### Constraints

* 1 ≤ _T_ ≤ 10 to the power of 3
* 2 ≤ _N_ ≤ 10 to the power of 3
* 2 ≤ _K_ ≤ _N_

### Output Format

For each test case, print the maximum possible value of _A&B_ on a new line.

### Sample Input
```
3
5 2
8 5
2 2
```
### Sample Output
```
1
4
0
```