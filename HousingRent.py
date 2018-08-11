# It is a simple linear Regress algorithm in machine learning.

# Import python packages
import csv
import random
import math

# Import DataSet
HousingData = open('Melbourne_housing_Updated.csv','r')
# Convert Dataset into List
StructuredHousingData = list(csv.reader(HousingData))

# Take first parameter manual
thetas = [1, 2, 3, 4, 5, 6, 7]
# take learning_rate
alpha = 0.00000000000000001

# Create empty list
DataNeeded = []
# take data need dataset featur in DataNeeded list
for i in range(1,len(StructuredHousingData)):
    BlankList = []
    BlankList.append(1)
    BlankList.append(float(StructuredHousingData[i][8]))
    BlankList.append(float(StructuredHousingData[i][9]))
    BlankList.append(float(StructuredHousingData[i][10]))
    BlankList.append(float(StructuredHousingData[i][11]))
    BlankList.append(float(StructuredHousingData[i][12]))
    BlankList.append(float(StructuredHousingData[i][2]))
    BlankList.append(float(StructuredHousingData[i][4]))
    DataNeeded.append(BlankList)

# than train the model    
for iternumber in range(0,1000):
    # take dels 
    Dels = [0, 0, 0, 0, 0, 0, 0]
    CostFun = 0

    for SingleHouseData in DataNeeded[0:8500]:
        for j in range(0,7):
            Dels[j] += (2*(thetas[0]*SingleHouseData[0] + thetas[1]*SingleHouseData[1] + thetas[2]*SingleHouseData[2] +
                           thetas[3]*SingleHouseData[3] + thetas[4]*SingleHouseData[4] +thetas[5]*SingleHouseData[5] +
                           thetas[6]*SingleHouseData[6] - SingleHouseData[7])*SingleHouseData[j])

    for j in range(0,7):
        Dels[j] = Dels[j]/8500

    for j in range(0,7):
        thetas[j] = thetas[j] - alpha*Dels[j]

    for SingleHouseData in DataNeeded[0:8500]:
        CostFun += (math.pow((thetas[0]*SingleHouseData[0]+ thetas[1]*SingleHouseData[1] + thetas[2]*SingleHouseData[2] +thetas[3]*SingleHouseData[3] + thetas[4]*SingleHouseData[4] + thetas[5]*SingleHouseData[5] +thetas[6]*SingleHouseData[6] - SingleHouseData[7]),2))

    CostFun = CostFun/8500

    print('The value of Cost Function in iteration number '+str(iternumber)+" is "+str(CostFun))


#testing

for SingleHouseData in DataNeeded[8500:8996]:
    NewPrice= -(thetas[0]*SingleHouseData[0]+ thetas[1]*SingleHouseData[1] + thetas[2]*SingleHouseData[2] +thetas[3]*SingleHouseData[3] +
           thetas[4]*SingleHouseData[4] + thetas[5]*SingleHouseData[5] +thetas[6]*SingleHouseData[6])+SingleHouseData[7]

    Error= NewPrice-SingleHouseData[7]

    print('The value of price ='+str(SingleHouseData)+'is'+ str(Error))




