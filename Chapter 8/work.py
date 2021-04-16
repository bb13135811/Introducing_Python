# 1.
test1 = '''This is a test of the emergency text system'''
with open('text', 'wt') as outfile:
    outfile.write(test1)

# 2.
with open('text', 'rt') as infile:
    test2 = infile.read()
print(test2)
test1 == test2

# 3.
file = '''author, book
J R R, The Hobbit
Lynne Truss, "Eats, Shoots & Leaves"
'''
with open('test.csv', 'wt') as new_file:
    new_file.write(file)

# 4.
import csv
with open('test.csv', 'rt') as fout:
    books = csv.DictReader(fout)
    for book in books:
        print(book)

# 5.
