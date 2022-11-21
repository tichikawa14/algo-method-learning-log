"""
https://algo-method.com/tasks/211

### 問題
$N$ 個の**互いに相異なる**整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。
$N$ 個の整数の中で一番大きいものは前から何番目にあるかを調べるプログラムを作成してください。
ただし、$N$ 個の整数のうちの先頭の整数 $A_0$ は、**前から $0$ 番目**であると考えることとします。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$A_0 A_1 \dots A_{N-1}$
```
また、入力される値は次の制約をみたします。
- $N$ は $1$ 以上 $100$ 以下の整数
- $A_i$ は $1$ 以上 $100$ 以下の整数 ($0 \le i \le N - 1$)
- $A_0, A_1, \dots, A_{N-1}$ の値は全て異なる
### 出力
答えを出力してください。
"""

N = int(input())
A = list(map(int, input().split()))

index = 0
max = 0
for i in range(N):
  if max < A[i]:
    max = A[i]
    index = i

print(index)
