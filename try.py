import tabula
from tabula import read_pdf

file_path = input()
# file_path = "r'"+file_path+"'"
file_path = file_path

df = read_pdf(file_path, pages = "all", multiple_tables = True)
print(df)

print(file_path)
