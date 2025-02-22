#1-1.
import pandas as pd

data = [['김나나',35,'과장'],
        ['이민아',28,'대리'],
        ['박정민',30,'대리'],]


dataFD = pd.DataFrame(data)
dataFD.columns = ['이름','나이','직급']

print(dataFD)

# 1-2.

dataFD.drop(columns='이름', inplace=True)
print(dataFD)


# 1-3.
dataFD = pd.DataFrame(data)
dataFD.columns = ['이름','나이','직급']
dataFD2=dataFD.drop([1,2])
print(dataFD2)


# 2-1.
data = [ ['037730', "3R", 1510, 7.36],
         ["036360", "3SOFT", 1790, 1.65],
        ["005760", "ACTS", 1185, 1.28],]

data = pd.DataFrame(data)

print(data)

data.columns= ["종목코드", "종목명", "현재가", "등락률"]
print(data)



# 2-2.
dataFD=data.drop(['현재가','종목코드'], axis=1)
print(dataFD)

# 2-3 


index = ["037730", "036360", "005760"]
data = [["3R", "1510"], ["3SOFT", 1790], ["ACTS", 1185]]
columns = ["종목명", "현재가"]

dataFD = pd.DataFrame(data)

dataFD.index = index
dataFD.columns = columns
#2-4
print(type(dataFD))

#2-5
dataFD1=dataFD.drop(0)
print(dataFD1)

# 2-6
dataFD1=dataFD.drop(-1)
