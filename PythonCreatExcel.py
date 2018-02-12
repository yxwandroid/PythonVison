# import xlwt
#
# def testXlwt(file = 'new.xls'):
#     book = xlwt.Workbook() #创建一个Excel
#     sheet1 = book.add_sheet('hello') #在其中创建一个名为hello的sheet
#     sheet1.write(0,0,'cloudox') #往sheet里第一行第一列写一个数据
#     sheet1.write(1,0,'ox') #往sheet里第二行第一列写一个数据
#     book.save(file) #创建保存文件
#
# #主函数
# def main():
#    testXlwt()
#
# if __name__=="__main__":
#     main()






import xlsxwriter

workbook = xlsxwriter.Workbook('demo.xlsx')

worksheet = workbook.add_worksheet('demo')

worksheet.write('A1', 'Hello')
worksheet.insert_image('A2', '11.png')
worksheet.write('A3', 'Hello1')
worksheet.write('A4', 'Hello2')
worksheet.write('A5', 'Hello3')
worksheet.write('A6', 'Hello4')

# worksheet.write(2, 0, 32)PythonCreatExcel.py:30
# worksheet.write(3, 0, 35.5)
# worksheet.write(4, 0, '=SUM(A3:A4)')


workbook.close()


