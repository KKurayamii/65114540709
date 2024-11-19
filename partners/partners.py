# import openpyxl

# with open('Me & My partner.xlsx')
#    print('can open file')

from openpyxl import load_workbook
wb = load_workbook('Me & My partner.xlsx')
print(wb.active)
for row in wb.active:
    values = [cell.value for cell in row]
    if values[1] and values[1]:
        pair = (values[2], values[1])
    if values[2] < values[1]:
        pair = (values[2], values[1])
    if pair is not groups:
        groups.append(pair)

        print(pair)
    print(values)


