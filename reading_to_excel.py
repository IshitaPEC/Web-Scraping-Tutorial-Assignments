import xlrd

#Open Workbook
workbook= xlrd.open_workbook('first_file.xlsx')

#Get sheet-> method sheet_by_index (index parameter)
worksheet= workbook.sheet_by_index(0)

#Find total number of rows
rows= worksheet.nrows

#Read rows -> row_values(row numbwr)-> Returns a tuple
for row in range(rows):
    first_col,second_col= worksheet.row_values(row)
    print(first_col,' ',second_col)
