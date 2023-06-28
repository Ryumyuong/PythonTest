import xlwt
import csv
import os

csvFileList = ["C:/CookAnalysis/CSV/singerA.csv", "C:/CookAnalysis/CSV/singerB.csv"]


for csvFileName in csvFileList :
    rowCount = 0
    with open(csvFileName, "r") as inFp:
        csvReader = csv.reader(inFp)
        # 맨 위에 한줄만 찍힘
        header_list = next(csvReader)
        outWorkbook = xlwt.Workbook()
        outSheet = outWorkbook.add_sheet(os.path.basename(csvFileName))
        for col in range(len(header_list)) :
            outSheet.write(rowCount, col, header_list[col])
        for row_list in csvReader:
            rowCount += 1
            for col in range(len(row_list)):
                if row_list[col].isnumeric() :
                    outSheet.write(rowCount, col, float(row_list[col]))
                else :
                    outSheet.write(rowCount, col, row_list[col])
            outWorkbook.save('c:/CookAnalysis/Excel/' + os.path.basename(csvFileName) + '0628.xls')        
print("Save. OK~")