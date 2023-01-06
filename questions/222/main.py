"""
https://algo-method.com/tasks/222

### 問題文
整数 $N$ が素数かどうかを判定するプログラムを作成してください。
ただし次の条件を満たすとき「 $N$ は素数である」と言います。
- $N$ は $2$ 以上の整数である
- $N$ を割り切ることのできる $1$ より大きい整数は $N$ のみである
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $100$ 以下の整数
### 出力
$N$ が素数のときは `Yes` を出力し、そうでないときは `No` を出力してください。
"""

N = int(input())

if N == 1:
  print('No')
else:
  is_prime = False
  for i in range(2, N):
    if N % i == 0:
      is_prime = True

  if is_prime:
    print('No')
  else:
    print('Yes')
