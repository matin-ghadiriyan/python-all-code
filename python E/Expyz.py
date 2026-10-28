File = open('name.csv' , 'a')
File.write('name')
while True:
    name = input('name: ')
    if name == 'exit':
        break
    File.write("\n" + name)
File.close()
#
#
File = open('name and age.csv' , 'w')
File.write('name,')
File.write('age')
while True:
    name = input('name: ')
    age = input('age: ')
    if name == 'exit' and age == 'exit':
        break
    File.write(f"\n {name}, {age}")
File.close()
#
#
import csv
file = open('name and age.csv')
reader = csv.DictReader(file)
for row in reader:
    print(row['age'])
    print(row['name'])
#
#
'''
import csv
def find_row_by_column(file_path,culumn, value):
    f = open(file_path , 'r' , newline=' ')
    reader = csv.DictReader(f)
    rows = []
    for row in reader:
        if row[culumn] == value:
            rows.append(row)
    f.close()
    return rows
r = find_row_by_column('names.csv', 'name' , 'matin')
print(r)
'''
#in code ghalat dare va baraye edit ast vali nemidinam chara?
#
#