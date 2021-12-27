# nDLP Question Solution

This is a discrete logarithm problem.

An [output.txt](./output.txt) is attached. According to this file, y is equal to (g to the power of x) mod n, and g, y, n are given, and x is the flag that we should find.

In order to solve this problem, I used [this website](https://www.alpertron.com.ar/DILOG.HTM) to find long format of x.


Then I used this code to get the flag in string format.


```python
from Crypto.Util.number import long_to_bytes

x = 1936424274652643265366177146994482280350488968204318138649641400181832241265975677
print(long_to_bytes(x).decode())
```
[ndlp.py](./ndlp.py)

Flag is:
ASIS{D!5Cre73_L09_iN_Zn_I5_3aSy?!}





