'''
Operators in python can be overloading using dunder methods.
These methods are called when a given operator is used on the objects
'''
class number:
    def __init__(self , num):
        self.num = num

    def __add__(self , num2):
        print("lets add")
        return self.num + num2.num

    def __mul__(self , num2):
        print("lets Multiply")
        return self.num * num2.num

n1 = number(4)
n2 = number(6)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)



'''
BINARY OPERATORS
+	__add__(self, other)
–	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)
>>	__rshift__(self, other)
<<	__lshift__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)
'''

'''
COMPARISON OPERATORS
<	__LT__(SELF, OTHER)
>	__GT__(SELF, OTHER)
<=	__LE__(SELF, OTHER)
>=	__GE__(SELF, OTHER)
==	__EQ__(SELF, OTHER)
!=	__NE__(SELF, OTHER)
'''


'''
ASSIGNMENT OPERATORS
-=	__ISUB__(SELF, OTHER)
+=	__IADD__(SELF, OTHER)
*=	__IMUL__(SELF, OTHER)
/=	__IDIV__(SELF, OTHER)
//=	__IFLOORDIV__(SELF, OTHER)
%=	__IMOD__(SELF, OTHER)
**=	__IPOW__(SELF, OTHER)
>>=	__IRSHIFT__(SELF, OTHER)
<<=	__ILSHIFT__(SELF, OTHER)
&=	__IAND__(SELF, OTHER)
|=	__IOR__(SELF, OTHER)
^=	__IXOR__(SELF, OTHER)
'''

'''
UNARY OPERATORS
–	__NEG__(SELF, OTHER)
+	__POS__(SELF, OTHER)
~	__INVERT__(SELF, OTHER)
'''