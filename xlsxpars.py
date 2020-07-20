import pandas as pd
#35082884.xlsx
#34317697.xlsx
file1 = pd.ExcelFile('35082884.xlsx')
file2 = pd.ExcelFile('34317697.xlsx')
#K1:
list_of_distinct_lines = []
Kf1list = []
Kf2list = []
rownum = 10
while True:
    exdata1 = pd.read_excel(file1, skiprows=rownum, usecols="k")
    exdata2 = pd.read_excel(file2, skiprows=rownum, usecols="K")
    strexdata1 = str(exdata1)
    strexdata2 = str(exdata2)
    listK1 = strexdata1.split('\n')
    listK2 = strexdata2.split('\n')
    part1 = listK1[0].replace(' ', '')
    part2 = listK2[0].replace(' ', '')
    Kf1list.append(part1)
    Kf2list.append(part2)
    if part1 != part2:
        list_of_distinct_lines. append(rownum + 1)
    if rownum == 50: #число обрабатываемых строк
        break
    rownum += 1
print(Kf1list)
print(Kf2list)
print(list_of_distinct_lines)

