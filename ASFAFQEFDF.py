import csv
# C:\\Users\\TUSER\\Desktop\\Time2Kode\\countryData.csv
with open("countryData.csv", "r") as file:
    rows = csv.reader(file)
    sum = 0
    for row in rows:
        sum += int(row[6])
print("p is", sum)
# print(f"The total population is {sum}")
