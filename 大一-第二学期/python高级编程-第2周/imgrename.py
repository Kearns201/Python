import os


def imgrename():
    ext = input('请输入要批量命名的文件后缀名（如jpg、png，直接回车退出程序）：').strip()
    if ext == '':
        return
    mypath = input('请输入图片文件所在文件夹：')
    allfiles = os.listdir(mypath)
    ext_list = []
    list_len = []
    for ifile in allfiles:
        fullfile = os.path.join(mypath, ifile)
        if os.path.isfile(fullfile) and os.path.splitext(ifile)[1][1:].lower() == ext:
            ext_list.append(ifile)
            list_len.append(len(ifile))
    # print(len(ext_list))
    if len(ext_list) == 0:
        print('未发现*.', ext, '类型的文件')
        return
    print('找到如下*.', ext, '文件：')
    for ifile in ext_list:
        print(ifile)
    print(25 * '*')
    choice = input('您确定要对这些文件批量重命名吗？（Y/y-确定，N/n-取消）\n')
    if choice != 'Y' and choice != 'y':
        return
    else:
        fi_num_cnt = 1
        input_max_len = max(list_len)
        prefix = input('请输入文件前缀：\n')
        nosize = int(input('请输入编号宽度，如1表示编号为1，2，如3表示编号为001，002：'))
        dstpath = input('请输入重命名后图片文件所在文件夹：')
        for ifile in ext_list:
            new_name = prefix + str(fi_num_cnt).zfill(nosize) + '.' + ext
            while True:
                if os.path.exists(os.path.join(dstpath, new_name)):
                    fi_num_cnt += 1
                    new_name = prefix + str(fi_num_cnt).zfill(nosize) + '.' + ext
                else:
                    break
            print(ifile.rjust(input_max_len, ' '), 3 * ' ', '重命名为：'.ljust(5, ' '), new_name.rjust(10, ' '))
            os.rename(os.path.join(mypath, ifile), os.path.join(dstpath, new_name))
            fi_num_cnt += 1
        print('运行结束！')
if __name__ == '__main__':
    imgrename()
