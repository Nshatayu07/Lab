
import csv

def main():
    with open("exp5/data5.csv", "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        classrowcolMap = {}
        colMap = {}
        rowMap = {}
        for row in csv_reader:
            rowName = row[0]
            colName = row[1]
            count = int(row[2])
           
            classrowcolMap.setdefault(rowName, {})
            classrowcolMap[rowName][colName] = count
           
            colMap.setdefault(colName, 0)
            colMap[colName] += count
           
            rowMap.setdefault(rowName, 0)
            rowMap[rowName] += count
   
    for row in rowMap:
        for col in colMap:
            print(row + "-" + col + ":", classrowcolMap[row][col])
   
    for row in rowMap:
        print(row + "->" + str(rowMap[row]))
   
    for col in colMap:
        print(col + "->" + str(colMap[col]))
   
    colSum = sum(colMap.values())
    print("colSum:", colSum)
   
    rowSum = sum(rowMap.values())
    print("rowSum:", rowSum)
   
    with open("exp5/exp5_output.csv", "w", newline="") as fw:
        csv_writer = csv.writer(fw)
        csv_writer.writerow(["Column\\row", "", "Bollywood", "", "Tollywood", "", "Total", "", ""])
        csv_writer.writerow(["", "Count", "t - weight", "d - weight", "Count", "t - weight", "d - weight", "Count", "t - weight", "d - weight"])
        for row in rowMap:
            csv_writer.writerow([row] + [classrowcolMap[row][col] for col in colMap] + [rowMap[row], rowMap[row] / rowMap[row] * 100, rowMap[row] / colSum * 100])
       
        csv_writer.writerow(["Total"] + [colMap[col] for col in colMap] + [colSum, 100, 100])

if __name__ == "__main__":
    main()

