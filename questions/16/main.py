"""
https://algo-method.com/tasks/16

### 問題文
$1$ 以上 $100$ 以下の整数 $N$ が標準入力から与えられます。
$N$ を $5$ で割ったあまりを標準出力するプログラムを作成してください。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
```
また、入力される制約は次の条件を満たします。
- $N$ は $1$ 以上 $100$ 以下の整数
### 出力
答えを出力してください。
"""
N = int(input())
print(N % 5)