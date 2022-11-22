"""
https://algo-method.com/tasks/219

### 問題
$N$ 個の **$1$ 以上 $9$ 以下の**整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。
$N$ 個の整数の中に一番多く出てくる数字を求めるプログラムを作成してください。
ただし、答えは一つに定まることが保証されているものとします。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$A_0 A_1 \dots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$は $1$ 以上 $100$ 以下の整数
- $A_i$ は **$1$ 以上 $9$ 以下の**整数 ($0 \le i \le N - 1$)
### 出力
答えを出力してください。
"""

N = int(input())
A = list(map(int, input().split()))

count = [0] * 9
for x in A:
  count[x - 1] += 1

max = max(count)
for i in range(9):
  if count[i] == max:
    print(i + 1)
