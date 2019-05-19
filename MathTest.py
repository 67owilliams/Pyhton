class MathTest:
    def __init__(self, FirstNum = None, SecondNum = None, ThirdNum = None):
        self.FirstNum = FirstNum
        self.SecondNum = SecondNum
        self.ThirdNum = ThirdNum

        if ThirdNum != None:
            print(ThirdNum * SecondNum * FirstNum)

        elif SecondNum != None:
            print(SecondNum + FirstNum)

        elif FirstNum != None:
            print(FirstNum ** 2)

    def DoMath(self, FirstNum = None, SecondNum = None, ThirdNum = None):
        self.FirstNum = FirstNum
        self.SecondNum = SecondNum
        self.ThirdNum = ThirdNum

        if ThirdNum != None:
            Output = FirstNum * SecondNum * ThirdNum
            return Output

        elif SecondNum != None:
            Output = FirstNum + SecondNum
            return Output

        elif FirstNum != None:
            Output = FirstNum ** 2
            return Output

    def CheckMath(self):
        Output = self.DoMath(self.FirstNum, self.SecondNum, self.ThirdNum)

        if self.ThirdNum!= None:
            print("{0} multiplied by {1}, and multiplied by {2} equals {3}".format(self.FirstNum,
                                                                                   self.SecondNum,
                                                                                   self.ThirdNum,
                                                                                   Output))

        elif self.SecondNum != None:
            print("{0} plus {1} equals {2}".format(self.FirstNum,
                                                   self.SecondNum,
                                                   Output))

        elif self.FirstNum != None:
            print("{0} squared equals {1}".format(self.FirstNum, Output))

Math = MathTest()
