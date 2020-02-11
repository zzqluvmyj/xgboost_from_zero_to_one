mapfile = 'featmap.txt'
datafile = 'agaricus.txt'


def loadfmap(fname):
    fmap = {}
    nmap = {}

    for l in open(fname):
        arr = l.split()
        if arr[0].find('.') != -1:
            idx = int(arr[0].strip('.'))  # 去除'.'后是数字，1-22
            assert idx not in fmap  # 为false时触发异常
            fmap[idx] = {}
            ftype = arr[1].strip(':')
            content = arr[2]
        else:
            content = arr[0]  # 有单独隔开的行，前面没有序号

        for it in content.split(','):
            if it.strip() == '':  # 转折行时最后有','，但是后面没东西
                continue
            k, v = it.split('=')
            fmap[idx][v] = len(nmap)
            nmap[len(nmap)] = ftype + '=' + k
    return fmap, nmap


def write_nmap(fo, nmap):
    for i in range(len(nmap)):
        fo.write('%d\t%s\ti\n' % (i, nmap[i]))


fmap, nmap = loadfmap('agaricus-lepiota.fmap')

fo = open(mapfile, 'w')
write_nmap(fo, nmap)
fo.close()

fo = open(datafile, 'w')
for l in open('agaricus-lepiota.data'):
    arr = l.split(',')
    if arr[0] == 'p':
        fo.write('1:')
    else:
        assert arr[0] == 'e'
        fo.write('0:')

    for i in range(1, len(arr)):
        # print(arr[i])
        if i == len(arr) - 1:
            fo.write('%d' % fmap[i][arr[i].split()[0]])
        else:
            fo.write('%d,' % fmap[i][arr[i].split()[0]])
    fo.write('\n')

fo.close()

import random

random.seed(1)
k = 1
n = 5

fi = open(datafile, 'r')
ftr = open(datafile + '.train', 'w')
fte = open(datafile + '.test', 'w')

for l in fi:
    if random.randint(1, n) == k:
        fte.write(l)
    else:
        ftr.write(l)

fi.close()
ftr.close()
fte.close()

if __name__ == '__main__':
    pass
