from shutil import copy2
import glob
path_name = []
path1 = '/media/minh/New Volume2/AI_thay_cuong/Make_data/data/2tr/train_serial_hor_200/'
#for i in range(0,200):
#    for name in glob.glob(path1+str(i)+'/*.jpg'):
        # print(name)
#        path_name.append(name)

for name in glob.glob('/media/minh/New Volume1/AI_thay_cuong/Make_data/data/2tr/train_serial_hor_200/0'+'/*.jpg'):
    # print(name)
    path_name.append(name)
print('len(path_name) = ', len(path_name))        
path_name_train2 = path_name[:int(len(path_name)*0.96)]
path_name_test2 = path_name[int(len(path_name)*0.96):]

name_labels_train2 = []
for name_image in path_name_train2:
#     print(name_image)
    x = name_image.split('/')[10]
#     print(x)
    y = x.split('_')[0]
#     print(y)
    name_label = name_image+"\t"+y
    name_labels_train2.append(name_label)
    
print('len(name_labels_train2) = ', len(name_labels_train2))

f = open('train_line_annotation.txt', "w")
for item in name_labels_train2:
    f.write(item + "\n")
f.close()

name_labels_test2 = []
for name_image in path_name_test2:
#     print(name_image)
    x = name_image.split('/')[10]
#     print(x)
    y = x.split('_')[0]
#     print(y)
    name_label = name_image+"\t"+y
    name_labels_test2.append(name_label)
print('len(name_labels_test2) = ', len(name_labels_test2))

k = open('test_line_annotation.txt', "w")
for item in name_labels_test2:
    k.write(item + "\n")
k.close()
