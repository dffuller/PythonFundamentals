#lists
a = [1,2,3];b=a;b[1] = 9; print(a,b)
# [1, 9, 3] [1, 9, 3]

#ints
c=1; d=c; d=2; print(c,d)
# 1 2

#float
a = 1.0; b=a; b=2.0; print(a,b)
# 1.0 2.0

#str
a = "hello"; b=a; b[0] = 'j'; print(a,b)
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-13-eacb5227c6d7> in <module>
# ----> 1 a = "hello"; b=a; b[0] = 'j'; print(a,b)
# 
# TypeError: 'str' object does not support item assignment
a = "hello"; b=a;b = "jello"; print(a,b)
# hello jello

#tuple
a = (1,2,3); b=a; b[0]=4; print(a,b)
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-17-05bfc35e8ba6> in <module>
# ----> 1 a = (1,2,3); b=a; b[0]=4; print(a,b)
# 
# TypeError: 'tuple' object does not support item assignment
a = (1,2,3); b=a; b=(4,5,6); print(a,b)
# (1, 2, 3) (4, 5, 6)

#dict
a = dict(a=1, b=2); b=a; b['a']=3; print(a,b)
# {'a': 3, 'b': 2} {'a': 3, 'b': 2}
a = dict(a=1, b=2); b=a; a=dict(a=2,b=4); print(a,b)
