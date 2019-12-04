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



#2
#a
#def isInstancePP(object1,classInfo):
 #   return True



#3
print("---------------------------------------------")
print("Question 3")
#a
def count_if(lst,func):
    return len(list(filter(func,lst)))

#test
print(count_if([1,0,8],lambda x:x>2),":need to be 1")
print(count_if([1,1,8],lambda x:x==1),":need to be 2")


#b
def for_all(lst,func1,func2):
    return len(list(filter(func2,list(map(func1,lst)))))==len(lst)

#test
print(for_all([1,0,8],lambda x:x*2,lambda x:x>0),":need to be False")
print(for_all([1,1,8],lambda x:x,lambda x:x>0),":need to be True")


#c
def for_all_red(lst,func1,func2):
    return len(list(filter(func2,[reduce(func1,lst)])))==1

#test
print(for_all_red([1,0,8],lambda x,y:x*y,lambda x:x>0),":need to be False")
print(for_all_red([1,1,8],lambda x,y:x*y,lambda x:x>7),":need to be True")


#d
def there_exist(lst,n,func1):
    return len(list(filter(func1,lst)))>=n

#test
print(there_exist([1,0,8],2,lambda x:x>1),":need to be False")
print(there_exist([1,1,8],2,lambda x:x>0),":need to be True")

