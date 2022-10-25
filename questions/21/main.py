"""
https://algo-method.com/tasks/21

### 問題文
文字列 $S$ が標準入力から与えられます。
$S$ を $3$ 回繰り返してできる文字列を標準出力するプログラムを作成してください。
### 入力
入力は次の形式で与えられます。
```IOExample
$S$
```
また、入力される値は次の制約を満たします。
- $S$ は英小文字からなる長さ $1$ 以上 $100$ 以下の文字列
### 出力
答えを出力してください。
"""

S = input()
print(S * 3)
