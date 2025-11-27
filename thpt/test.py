import csv 

with open(r'C:\Users\nhata\Desktop\Code\Nhawtanhy.github.io\thpt\data_in.csv', encoding= "utf-8") as file:
    csvFile = csv.reader(file)
    #for lines in csvFile:
    #    print(lines)
    header = next(csvFile)
    print(header)
    row_to_print = 5

    for row in csvFile:
        if row[1].strip() == "Việt Đức":
            print(row)