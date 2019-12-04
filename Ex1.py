import math
from functools import reduce
#1
class ComplexNum():

    #1 init function
    def __init__(self,real,imaginary):
        self.tuple=(real,imaginary)

    #2 property function
    @property
    def re(self):
        return self.tuple[0]

    @property
    def im(self):
        return self.tuple[1]

    #3 returns tuple of the complex number
    def to_tuple(self):
        return self.tuple

    # 4 creates string the represents the complex num
    def __repr__(self):
        if self.im > 0:
            if self.re != 0:
                return str(self.re) + " + " + str(self.im) + "i"
            else :
                return str(self.im) + "i"
        elif self.im <0:
            if self.re != 0:
                return str(self.re) + " - " + str(abs(self.im)) + "i"
            else:
                return " - " + str(abs(self.im)) + "i"
        else:
            return str(self.re)



    #5 checks equality: returns true only if other is complex num and its re,im equals to self's re and im
    def __eq__(self, other):
        if type(other)!=ComplexNum:
            return False
        return other.re==self.re and other.im==self.im

    #6 implementaion of +: add another complex num to the curr one and returns the new complex number that represents the sum
    def __add__(self, other):
        if type(other)!=ComplexNum:
            return None
        return ComplexNum(self.re+other.re,self.im+other.im)

    #7 implementaion of neg and -:
    def __neg__(self):
        return ComplexNum(-1*self.re,-1*self.im)

    def __sub__(self, other):
        return self+other.__neg__()

    # 8 mul funtion
    def __mul__(self, other):
        try:
            complexNum = ComplexNum(self.re * other.re - self.im * other.im,
                                    self.re * other.im + self.im * other.re)
            return complexNum
        except:
            raise ValueError('Complex multiplication only defined for Complex Numbers')

    # 9 conjugate
    def conjugate(self):
        conjugateIs = ComplexNum(self.re, -self.im)
        return conjugateIs

    # 10 abs
    def abs(self):
        other = self.conjugate()
        return math.sqrt((self*other).re)


class Add(ComplexNum):
    x=2
class Add2(Add):
    y=9
class Add3(Add2):
    y=9

class Add22(Add2):
    t=4
#2
#a
def isInstancePPL(object1,classInfo):
    if type(object1) is classInfo:
        return True
    if len(classInfo.__subclasses__())==0:
        return False
    subs=classInfo.__subclasses__()
    ans=False
    for sub in subs:
        ans=isInstancePPL(object1,sub)or ans
    return ans

#b
def numInstancePPL(object1,classInfo):
    if not isInstancePPL(object1,classInfo):
        return 0
    else:
        if type(object1) is classInfo:
            return 0
        if len(classInfo.__subclasses__()) == 0:
            return 0
        if type(object1) in classInfo.__subclasses__():
            return 1
        subs = classInfo.__subclasses__()
        ans = 0
        for sub in subs:
            ans = numInstancePPL(object1, sub) + ans +1
        return ans

#c
def isSubclassPPL(__class,classInfo):
    if __class is classInfo:
        return True
    if len(classInfo.__subclasses__()) == 0:
        return False
    subs = classInfo.__subclasses__()
    ans = False
    for sub in subs:
        ans = isSubclassPPL(__class, sub) or ans
    return ans

#d
def numSubclassPPL(__class,classInfo):
    if not isSubclassPPL(__class,classInfo):
        return 0
    else:
        if __class is classInfo:
            return 1
        if len(classInfo.__subclasses__()) == 0:
            return 0
        if __class in classInfo.__subclasses__():
            return 2
        subs = classInfo.__subclasses__()
        ans = 0
        for sub in subs:
            ans = numSubclassPPL(__class, sub) + ans +1
        return ans

#3
print("---------------------------------------------")
print("Question 3")
#a
def count_if(lst,func):
    return len(list(filter(func,lst)))

#test
print("Test 1 passed:",count_if([1,0,8],lambda x:x>2)==1)
print("Test 2 passed:",count_if([1,1,8],lambda x:x==1)==2)


#b
def for_all(lst,func1,func2):
    return len(list(filter(func2,list(map(func1,lst)))))==len(lst)

#test
print("Test 3 passed:",for_all([1,0,8],lambda x:x*2,lambda x:x>0)==False)
print("Test 4 passed:",for_all([1,1,8],lambda x:x,lambda x:x>0)==True)


#c
def for_all_red(lst,func1,func2):
    return len(list(filter(func2,[reduce(func1,lst)])))==1

#test
print("Test 5 passed:",for_all_red([1,0,8],lambda x,y:x*y,lambda x:x>0)==False)
print("Test 6 passed:",for_all_red([1,1,8],lambda x,y:x*y,lambda x:x>7)==True)


#d
def there_exist(lst,n,func1):
    return len(list(filter(func1,lst)))>=n

#test
print("Test 7 passed:",there_exist([1,0,8],2,lambda x:x>1)==False)
print("Test 8 passed:",there_exist([1,1,8],2,lambda x:x>0)==True)

