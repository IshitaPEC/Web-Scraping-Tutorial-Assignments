from xlsxwriter import Workbook

#Create a workbook
workbook = Workbook("first_file.xlsx")

#Add a worksheet
worksheet= workbook.add_worksheet()

#Write Worksheet - parameters-(row,column,value)
for row in range(20):
    worksheet.write(row,0,'Row Number')
    worksheet.write(row,1,row)


#Close Workbook
workbook.close()
