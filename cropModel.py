import random, pylab
from matplotlib import pyplot as plt

class hectareCrop(object):
    '''Used to project yearly yield for a crop based on fertilizer and rainfall 
    inputs.
    '''
    def __init__(self, NFert, irrigation):
        self.NAmt=NFert
        self.irrig=irrigation
        
    def rainfall(self):
        '''returns an annual rainfall amount based on normal probability distribution.
        Average rainfall during growth period is 50 cm and a standard deviation of 20 cm 
        return self.rainAmt
        '''
        self.rainAmt=random.gauss(50,20)
        #self.rainAmt=62.149

    def Nloss(self):
        '''Loss of N based on amount of rainfall that occurred.  For every cm of rain,
        3.0% loss of N occurs.
        Runs self.rainfall() to get self.rainAmt, returns an int of NAmt remaining based
        on yearly rainfall.  Int returned is not a object variable and does not replace
        self.NAmt
        '''
        self.rainfall()
        Nremain=self.NAmt-int(0.03*self.rainAmt)
        return Nremain
       
        
    def cropYield(self):
        '''Predicts the yearly yield of a crop based on rainfall and fertilizer
        inputs.
        Average yield is 100 bushels per acre based on average rainfall and 200 kg/ha
        per year N fertility.  A very basic model was used to predict yield where
        yield = rainAmt + (0.25 * N amt in kg/ha).  Need to use NAmt after rainfall
        for calcualtion.  
        RETURN: self.yearYield wich is the yield in bushels per acre
        '''
        remainingN=self.Nloss()
       # self.yearYield=self.rainAmt + (0.25 * self.NAmt)
        self.yearYield=self.rainAmt + (0.25 * remainingN)
        
    def profit(self):
        '''Assume $7 dollar per bushel yield.  However, a loss of $10 for each cm below 
        50 cm.  If irrigation is True, rainfall is supplemented up to 50 cm if it is 
        below.  If rainfall is 50 cm or greater, no additional irrigation takes
        place.
        RETURN grossProfit, not an object attribute
        '''
        self.cropYield()
        if self.irrig:
            grossProfit=self.yearYield*7
        else:
            grossProfit=self.yearYield*7-10*max(50-self.rainAmt,0)
        return grossProfit
        


def modelYield(NFert, Irrigation= False, cycles = 10000):
    '''Model yield for 10,000 iterations and plot the yield in a histogram.
    '''
    yields=[]
    for sim in range(cycles):
        crop3 = hectareCrop(NFert, Irrigation)
        crop3.cropYield()
        yields.append(crop3.yearYield)
    
    return yields

# y=modelYield(200)
# plt.hist(y)
# plt.show()



def modelProfit(NFert, cycles=1000):
    '''Model profit for 10,000 iterations for both irrigated and non-irrigated.
    Plot the predictions in four (2x2) subplot windows - histogram and boxplot for
    each of the data sets.
    '''

    profits_noirr=[]
    profits_irr=[]
    for sim in range(10000):
        crop3 = hectareCrop(NFert, False)
        crop4 = hectareCrop(NFert, True)
        #crop3.profit()
        profits_noirr.append(crop3.profit())
        profits_irr.append(crop4.profit())
    return profits_noirr,profits_irr

p_noirr,p_irr=modelProfit(200)
plt.subplot(221)
plt.hist(p_noirr)
plt.show()  
plt.subplot(222)
plt.hist(p_irr)
plt.show()  
plt.subplot(223)
plt.boxplot(p_noirr)
plt.show()  
plt.subplot(224)
plt.boxplot(p_irr)
plt.show()    

#Uncomment to run
# random.seed(1)
# random.gauss(50,20)
# print("Unit Test 1") 
# crop1 = hectareCrop(200, False) 
# money = crop1.profit() 
# print(money) #answer is 783.29
# print(crop1.yearYield) #answer is 111.899
# print(crop1.rainAmt) #answer 62.149
# print(crop1.NAmt) #answer is 200
# print(crop1.irrig) #answer is False
# 
# 
# print("Unit Test 2")
# crop2 = hectareCrop(100, True) 
# money = crop2.profit()
# print(money) #521.258
# print(crop2.yearYield) #74.465
# print(crop2.rainAmt) #49.715
# print(crop2.NAmt) #100
# print(crop2.irrig) #True
# 
# random.seed(1)
# kk=[]
# for i in range(20): 
#     kk.append(random.gauss(50,20))