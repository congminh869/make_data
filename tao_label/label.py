import glob
path_name = []

for name in glob.glob('/home/minh/Documents/minh/ai_thay_cuong/vietocr/data_serial/InkData_line_processed/*.jpg'):
    # print(name)
    path_name.append(name)

print(len(path_name))
print("---------------------------")


path_labels = []
for name_image in path_name:
#     print(name_image)
    x = name_image.split('/')[9]
#     print(x)
    y = x.split('_')[0]
#     print(y)
    name_label = 'InkData_line_processed/'+x+"\t"+y
    path_labels.append(name_label)
    # print(name_label)


print(len(path_labels))
print("---------------------------")

path_labels_train = path_labels[:int(len(path_labels)*0.9)]
path_labels_test = path_labels[int(len(path_labels)*0.9):]
print(len(path_labels_train))
print(len(path_labels_test))
f = open('/home/minh/Documents/minh/ai_thay_cuong/vietocr/data_serial/train_line_annotation.txt', "w")
for item in path_labels_train:
    f.write(item + "\n")
f.close()

k = open('/home/minh/Documents/minh/ai_thay_cuong/vietocr/data_serial/test_line_annotation.txt', "w")
for item in path_labels_test:
    k.write(item + "\n")
k.close()