import csv
import xlwt
import xlrd
import os


def csvToExcel(csvfile, excelfile):
    myexcel = xlwt.Workbook()
    mysheet = myexcel.add_sheet('mysheet')
    csvfile = open(csvfile, 'r')
    reader = csv.reader(csvfile)
    row = 0
    for line in reader:
        col = 0
        for item in line:
            mysheet.write(row, col, item)
            col += 1
        row += 1
    myexcel.save(excelfile)
    print('转换完成')


def excelToCsv(excelfile, csvfiledir):
    workbook = xlrd.open_workbook(excelfile)
    all_worksheets = workbook.sheet_names()
    for worksheetname in all_worksheets:
        worksheet = workbook.sheet_by_name(worksheetname)
        csv_file = open(os.path.join(csvfiledir, worksheetname+'.csv'), 'w')
        wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for rownum in range(worksheet.nrows):
            wr.writerow([entry for entry in worksheet.row_values(rownum)])
        csv_file.close()

    print('转换完成')


if __name__ == '__main__':
    print('请输入转换方向：')
    print('1.CSV文件转换为Excel文件')
    print('2.Excel文件转换为CSV文件')
    print('3.退出')
    choice = int(input('请输入你的选择：'))
    if choice == 1:
        csvfilename = input('请输入CSV文件名（包括路径）：')
        excelfilename = input('请输入Excel文件名（包括路径）：')
        csvToExcel(csvfilename, excelfilename)
    elif choice == 2:
        excelfilename = input('请输入Excel文件名（包括路径）：')
        csvfiledir = input('请输入存放转换后CSV文件的文件夹：')
        excelToCsv(excelfilename, csvfiledir)
    else:
        exit(0)
