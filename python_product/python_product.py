# coding: utf-8

from collections import OrderedDict
from itertools import product
from pdb import set_trace

# エラー発生回数よりも大きな値であればなんでもよい
infinite = 2000

# 各エラーごとの探索範囲をリストで指定
SK01_range = list(range(5,10)) + [infinite]
SK03_range = list(range(1,7))  + [infinite]
SK04_range = list(range(1,4))  + [infinite]

# 通常の dict を使用し順番が入れ替わっても問題はないはずだが、
# 考えやすくするため OrderedDict を使う
search_range = OrderedDict((('SK01', SK01_range),
                            ('SK03', SK03_range),
                            ('SK04', SK04_range),
))

errs   = tuple(search_range.keys())
ranges = tuple(search_range.values())

# 探索範囲の中であらゆる組み合わせを試す
for ths in product(*ranges):
    condition = dict(zip(errs, ths))
    print(condition)


"""
jupyter notebook を バッチとして出力
1. https://adtech.cyberagent.io/techblog/archives/2317
2. ```
   import subprocess
   subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'ファイル名.ipynb'])
   ```
"""
