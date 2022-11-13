"""
https://algo-method.com/tasks/58

### 問題文
$N$ 個の文字列 $S_0, S_1 \dots, S_{N-1}$ が与えられます。
$N$ 個の文字列の頭文字をつないでできる文字列を出力してください。
### 入力
入力は次の形式で与えられます。$N$ は与えられる入力値の個数を指定しています。
```IOExample
$N$
$S_0$
$S_1$
$\vdots$
$S_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $1000$ 以下の整数
- $S_i$ は英小文字からなる長さ $1$ 以上 $20$ 以下の文字列 $(0\leq i \leq N-1)$
### 出力
答えを出力してください。
"""

N = int(input())
S = [''] * N
for i in range(N):
  S[i] = input()
ans = ''
for item in S:
  ans += item[0]
print(ans)
