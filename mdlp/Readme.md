

# mDLP Question Solution

This is a matrix discrete logarithm problem.

[output.txt](./output.txt) & [mdlp.sage](./mdlp.sage) files are attached.

As we read the sage file,  we find out that in the output.txt matrices A, Q, C, E are embedded in this file and p is given too. Also these formulas hold:

```
r = randint(2, p)
C = A ** r
D = Q ** r
E = D * M => M = ~D * E
```
Now that we are given C & A, if I can find r, then I can raise Q to the power of r to find D. Then I can get the inverse & multiply by E, this way the Message matrix is retrieved.

But the question is how to find r. In order to do this, you need to have a little bit of knowledge in linear algebra.

You can use Diagonalization (or in general, jordan matrix form) to rewrite a matrix, with multiply of 3 matrices, which the first & last one are inverse of each other. This property helps in the case which we want to raise the matrix to a power (for example r).

```
A = P J ~P
A^r = (P J ~P)(P J ~P)(P J ~P)...(P J ~P) = P J^r ~P
~P C P = ~P A^r P = J^r
```


```python
alpha = IntegerModRing(p)
M = MatrixSpace(alpha, 2, 2)

A = M(A)
Q = M(Q)
C = M(C)
E = M(E)

J, P = A.jordan_form(transformation=True)
j_r = ~P*C*P

```
Now that i’ve found J_r, I can simply find r.

```
print(discrete_log(alpha(j_r[1][1]), alpha(J[1][1])))
>>> r = 69061912195510167079715687878036583056625139896259969453538571762984613555627

```

According to the formulas written above, simply i can find the message matrix.

```
D = Q**r
Mes = ~D*E
print(Mes)
>>> [1324955255054937770134747290094387 2461719072681758828457118900962669]
[1932074164876896107376993304522820  677971303745800032818513197408637]
```

Due to msg_to_matrix function, flag is splitted into 4 pieces, so i can get the flag with below code:

```
from Crypto.Util.number import *
print(''.join([long_to_bytes(1324955255054937770134747290094387).decode(),
              long_to_bytes(2461719072681758828457118900962669).decode(),
              long_to_bytes(1932074164876896107376993304522820).decode(),
              long_to_bytes(677971303745800032818513197408637).decode()]))

```

Flag is:
ASIS{PuBl1c-K3y_CRyp70sy5tEm_B4S3d_On_Tw0D!m3nSiOn_DLP!}


Source code in: [mdlp.py](./mdlp.py)

If you have any problem with sage, try using this [this website](https://sagecell.sagemath.org/).










