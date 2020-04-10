import os
import random

trainval_percent = 0.8  # trainval占比例多少
train_percent = 0.7  # traint数据集占比例多少
xmlfilepath = 'D:\\data\\objectdetec_mass\\Annotations'
txtsavepath = 'D:\\data\\objectdetec_mass\\ImageSets\\Main'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('D:/data/objectdetec_mass/ImageSets/Main/trainval.txt', 'w')
ftest = open('D:/data/objectdetec_mass/ImageSets/Main/test.txt', 'w')
ftrain = open('D:/data/objectdetec_mass/ImageSets/Main/train.txt', 'w')
fval = open('D:/data/objectdetec_mass/ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
