from shutil import copy2
import glob
path_name = []
i = 0 
# for i in range(0,12):
#     for name in glob.glob('/media/minh/New Volume/hoctaps/nam4/tri_tue_nhan_tao_va_ung_dung/hocKy2/codebtl/Make_data/data/train_owner_hor/'+str(i)+'/*.jpg'):
#         # print(name)
#         path_name.append(name)
# print(len(path_name))

#copy 
# dst = '/home/minh/Documents/minh/ai_thay_cuong/vietocr/data_hor/train_owner/InkData_line_processed'
# for path in path_name:
#     copy2(path, dst)
#     print(i)
#     i = i + 1

path_name2 = []
dst_serial = '/home/minh/Documents/minh/ai_thay_cuong/vietocr1/data_hor/train_serial/InkData_line_processed/*.jpg'
dst_owner  = '/home/minh/Documents/minh/ai_thay_cuong/vietocr1/data_hor/train_owner/InkData_line_processed/*.jpg'
dst_iso    = '/home/minh/Documents/minh/ai_thay_cuong/vietocr1/data_hor/train_iso/InkData_line_processed/*.jpg'
dst_check  = '/home/minh/Documents/minh/ai_thay_cuong/vietocr1/data_check/InkData_line_processed/*.jpg'
path_3tr = '/home/minh/Documents/minh/ai_thay_cuong/vietocr/data_test/InkData_line_processed/*.jpg'
for name in glob.glob(path_3tr):
    # print(name)
    path_name2.append(name)

print("chieu dai = ",len(path_name2))
path_name_train2 = path_name2[:int(len(path_name2)*0.95)]
path_name_test2 = path_name2[int(len(path_name2)*0.95):]
print('train = ',len(path_name_train2))
print('test = ',len(path_name_test2))

# for i in path_name_test2:
#     print(i)

name_labels_train2 = []
for name_image in path_name_train2:
#     print(name_image)
    x = name_image.split('/')[9]
#     print(x)
    y = x.split('_')[0]
#     print(y)
    name_label = 'InkData_line_processed/'+x+"\t"+y
    name_labels_train2.append(name_label)
print(name_label)

print('len(name_labels_train2) = ',len(name_labels_train2))

f = open('train_line_annotation.txt', "w")
for item in name_labels_train2:
    f.write(item + "\n")
f.close()

name_labels_test2 = []
for name_image in path_name_test2:
#     print(name_image)
    x = name_image.split('/')[9]
#     print(x)
    y = x.split('_')[0]
#     print(y)
    name_label = 'InkData_line_processed/'+x+"	"+y
    name_labels_test2.append(name_label)
print(name_label)

k = open('test_line_annotation.txt', "w")
for item in name_labels_test2:
    k.write(item + "\n")
k.close()

print('len(name_labels_test2) = ',len(name_labels_test2))