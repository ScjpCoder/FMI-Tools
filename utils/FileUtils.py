import os

'''
将data和header追加写入csv文件
filename:文件名
data:数据
header:表头
'''
def write_csv(filename, data, header):
    write_header(filename, header)
    with open(filename, 'a') as f:
        for i in range(len(data)):
            f.write(str(data[i]))
            f.write(',')
        f.write('\n')
        f.close()

'''
创建结果文件并写入csv头部信息
filename:文件名
header:头部信息
'''
def write_header(filename, header):
    if not os.path.exists(filename):
        with open(filename, 'a') as f:
            f.write(header)
            f.close()


'''
删除指定的文件夹
参数:filepath 文件的绝对路径
'''
def del_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)
        print(filepath + "文件删除成功")
    else:
        print("文件不存在")
