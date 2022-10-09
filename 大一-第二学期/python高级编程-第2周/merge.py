import os


def joinfile(fromdir, filename, todir):
    if not os.path.exists(todir):
        os.mkdir(todir)
    if not os.path.exists(fromdir):
        print('文件夹错误')
    outfile = open(os.path.join(todir, filename), 'wb')
    files = os.listdir(fromdir)
    files.sort()
    for file in files:
        filepath = os.path.join(fromdir, file)
        infile = open(filepath, 'rb')
        data = infile.read()
        outfile.write(data)
        infile.close()
    outfile.close()


def main():
    fromdir = input('请输入存放分割后的文件所在路径:')
    filename = input('请输入合并后的文件名：')
    todir = input('请输入存放合并后文件的文件夹:')
    # chunksize = int(input('请输入分割大小（以字节为单位）:'))
    # absfrom, absto = map(os.path.abspath, [fromfile, todir])
    joinfile(fromdir, filename, todir)
    print('合并成功：', filename, '位于', todir)


if __name__ == '__main__':
    main()
