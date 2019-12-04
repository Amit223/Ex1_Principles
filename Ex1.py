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
    def _repr_(self):
        if self.tuple[1] > 0:
            return str(self.tuple[0]) + " + " + str(self.tuple[1]) + "i"
        return str(self.tuple[0]) + " - " + str(abs(self.tuple[1])) + "i"

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
    def _mul_(self, other):
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
        return math.sqrt(
            pow(self.re * other.re - self.im * other.im, 2) + pow(self.re * other.im + self.im * other.re, 2))
