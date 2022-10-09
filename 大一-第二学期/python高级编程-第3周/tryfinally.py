try:
    f = open(r"d:\temp\example", "r")
    f.write("writing somthing")
finally:
    f.close()
    print("清理......关闭文件")
