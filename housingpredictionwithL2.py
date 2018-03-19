import csv
import random
import math

HousingData = open('Melbourne_housing_Updated.csv','r')
StructuredHousingData = list(csv.reader(HousingData))

thetas = [1, 2, 3, 4, 5, 6, 7]
alpha = 0.0000000000000001
lembda=1000
DataNeeded = []

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

for iternumber in range(0,100):
    lemda=10
    Dels = [0, 0, 0, 0, 0, 0, 0]
    CostFun = 0
    a=0

    for SingleHouseData in DataNeeded[0:8500]:
        for j in range(0,7):
            Dels[j] += (2*(thetas[0]*SingleHouseData[0] + thetas[1]*SingleHouseData[1] + thetas[2]*SingleHouseData[2] + thetas[3]*SingleHouseData[3] + thetas[4]*SingleHouseData[4] +thetas[5]*SingleHouseData[5] + thetas[6]*SingleHouseData[6] - SingleHouseData[7])*SingleHouseData[j])

    for j in range(0,7):
        Dels[j] = Dels[j]/8500

    for j in range(0,7):
        thetas[j] = thetas[j] -alpha* Dels[j]
        a += (lembda*(math.pow((thetas[j]),2)))
       # print('thetas are:'+str(thetas[j]))
    for SingleHouseData in DataNeeded[0:8500]:
        CostFun += (math.pow((thetas[0]*SingleHouseData[0]+ thetas[1]*SingleHouseData[1] + thetas[2]*SingleHouseData[2] +thetas[3]*SingleHouseData[3] + thetas[4]*SingleHouseData[4] + thetas[5]*SingleHouseData[5] +thetas[6]*SingleHouseData[6] - SingleHouseData[7]),2))

    CostFun = (CostFun+a)/8500

    print('The value of Cost Function in iteration number '+str(iternumber)+" is "+str(CostFun))

#testing

for SingleHouseData1 in DataNeeded[8500:len(StructuredHousingData)]:
    Error=0
    NewPrice= (-(thetas[0]*SingleHouseData1[0] + thetas[1]*SingleHouseData1[1] + thetas[2]*SingleHouseData1[2]+ thetas[3]*SingleHouseData1[3] + thetas[4]*SingleHouseData1[4]+thetas[5]*SingleHouseData1[5] + thetas[6]*SingleHouseData1[6])+SingleHouseData1[7])
    Error=NewPrice-SingleHouseData1[7]
    print('The value of Cost  in iteration number ' + str(SingleHouseData1) + " is " + str(Error))
    #print('The value of Cost  in iteration number ' + str(SingleHouseData1) + " is " + str(NewPrice))