import os

megabytes = 1024 * 1024
chunksize = 200 * megabytes  # 默认分割大小


def split(fromfile, todir, chunksize=chunksize):
    if not os.path.exists(todir):
        os.mkdir(todir)
    else:
        for fname in os.listdir(todir):
            os.remove(os.path.join(todir, fname))
    partnum = 0
    inputfile = open(fromfile, 'rb')
    while True:
        chunk = inputfile.read(chunksize)
        if not chunk:
            break
        partnum += 1
        filename = os.path.join(todir, ('part%04d' % partnum))
        fileobj = open(filename, 'wb')
        fileobj.write(chunk)
        fileobj.close()
    return partnum


def main():
    fromfile = input('请输入要分割的文件:')
    todir = input('请输入存放分割后文件的文件夹:')
    chunksize = int(input('请输入分割大小（以字节为单位）:'))
    absfrom, absto = map(os.path.abspath, [fromfile, todir])
    print('分割文件', absfrom, '到', absto, '单个文件大小为', chunksize)
    parts = split(fromfile, todir, chunksize)
    print('分割成功：', parts, '个文件，位于', absto)


if __name__ == '__main__':
    main()
