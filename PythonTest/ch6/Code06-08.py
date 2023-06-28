import csv

with open("C:/CookAnalysis/CSV/singerA.csv", "r") as inFpA :
    with open("C:/CookAnalysis/CSV/singerB.csv", "r") as inFpB:
        with open("C:/CookAnalysis/CSV/singer165_2.csv", "w", newline='') as outFp:
            csvReaderA = csv.reader(inFpA)
            csvReaderB = csv.reader(inFpB)
            csvWriter = csv.writer(outFp)
            header_list = next(csvReaderA)
            header_list = next(csvReaderB)
            csvWriter.writerow(header_list)
            # index순서를 안다면 idx1대신 index값 입력
            idx1 = header_list.index("평균 키")
            
            for row_list in csvReaderA:
                if int(row_list[idx1]) >= 165 :
                    csvWriter.writerow(row_list)
            for row_list in csvReaderB:
                if int(row_list[idx1]) >= 165 :
                    csvWriter.writerow(row_list)

print('Save. OK~')