import glob

import time


path_name = []
print("---------------------------")
path1 = '/home/minh/Documents/minh/mqsolutions/car_object_detection/craw_web_bonbanh/data_moi/image_minh/'
# target = '/home/minh/Documents/minh/mqsolutions/car_object_detection/save_image_yolov5/data/stanford/img_test_stanford/1/'

# dst1 = '/home/minh/Documents/minh/mqsolutions/car_object_detection/craw_web_bonbanh/data_moi/1/'
# dst2 = '/home/minh/Documents/minh/mqsolutions/car_object_detection/craw_web_bonbanh/data_moi/2/'
# dst3 = '/home/minh/Documents/minh/mqsolutions/car_object_detection/craw_web_bonbanh/data_moi/3/'
# dst4 = '/home/minh/Documents/minh/mqsolutions/car_object_detection/craw_web_bonbanh/data_moi/4/'
# dst5 = '/home/minh/Documents/minh/mqsolutions/car_object_detection/craw_web_bonbanh/data_moi/5/'
# dst6 = '/home/minh/Documents/minh/mqsolutions/car_object_detection/craw_web_bonbanh/data_moi/6/'
# dst7 = '/home/minh/Documents/minh/mqsolutions/car_object_detection/craw_web_bonbanh/data_moi/7/'
# dst8 = '/home/minh/Documents/minh/mqsolutions/car_object_detection/craw_web_bonbanh/data_moi/8/'
# dst9 = '/home/minh/Documents/minh/mqsolutions/car_object_detection/craw_web_bonbanh/data_moi/9/'
# dst0 = '/home/minh/Documents/minh/mqsolutions/car_object_detection/craw_web_bonbanh/data_moi/0/'


# for name in glob.glob(target):
#     path_name.append(name)



for name in glob.glob(path1+'*.jpg'):
    # print(name)
    path_name.append(name)

print(len(path_name))
path_name0 = path_name[:int(len(path_name)*0.1)]
path_name1 = path_name[int(len(path_name)*0.1):int(len(path_name)*0.2)]
path_name2 = path_name[int(len(path_name)*0.2):int(len(path_name)*0.3)]
path_name3 = path_name[int(len(path_name)*0.3):int(len(path_name)*0.4)]
path_name4 = path_name[int(len(path_name)*0.4):int(len(path_name)*0.5)]
path_name5 = path_name[int(len(path_name)*0.5):int(len(path_name)*0.6)]
path_name6 = path_name[int(len(path_name)*0.6):int(len(path_name)*0.7)]
path_name7 = path_name[int(len(path_name)*0.7):int(len(path_name)*0.8)]
path_name8 = path_name[int(len(path_name)*0.8):int(len(path_name)*0.9)]
path_name9 = path_name[int(len(path_name)*0.9):]


print(len(path_name0))
print(len(path_name1))
print(len(path_name2))
print(len(path_name3))
print(len(path_name4))
print(len(path_name5))
print(len(path_name6))
print(len(path_name7))
print(len(path_name8))
print(len(path_name9))
# print("---------------------------")
from shutil import copy2
# dst = '/home/minh/Documents/minh/ai_thay_cuong/vietocr/data_test/InkData_line_processed'
i = 0

count = 0
for path in path_name0:
    start = time.time()
    if i % 1000 == 0:
        print(i)
        print('time loop 1000 = ',count)
        count = 0
    copy2(path, dst0)
    i = i + 1
    end = time.time()
    count = count + (end - start)

for path in path_name1:
    start = time.time()
    if i % 1000 == 0:
        print(i)
        print('time loop 1000 = ',count)
        count = 0
    copy2(path, dst1)
    i = i + 1
    end = time.time()
    count = count + (end - start)

for path in path_name2:
    start = time.time()
    if i % 1000 == 0:
        print(i)
        print('time loop 1000 = ',count)
        count = 0
    copy2(path, dst2)
    i = i + 1
    end = time.time()
    count = count + (end - start)

for path in path_name3:
    start = time.time()
    if i % 1000 == 0:
        print(i)
        print('time loop 1000 = ',count)
        count = 0
    copy2(path, dst3)
    i = i + 1
    end = time.time()
    count = count + (end - start)

for path in path_name4:
    start = time.time()
    if i % 1000 == 0:
        print(i)
        print('time loop 1000 = ',count)
        count = 0
    copy2(path, dst4)
    i = i + 1
    end = time.time()
    count = count + (end - start)

for path in path_name5:
    start = time.time()
    if i % 1000 == 0:
        print(i)
        print('time loop 1000 = ',count)
        count = 0
    copy2(path, dst5)
    i = i + 1
    end = time.time()
    count = count + (end - start)

for path in path_name6:
    start = time.time()
    if i % 1000 == 0:
        print(i)
        print('time loop 1000 = ',count)
        count = 0
    copy2(path, dst6)
    i = i + 1
    end = time.time()
    count = count + (end - start)

for path in path_name7:
    start = time.time()
    if i % 1000 == 0:
        print(i)
        print('time loop 1000 = ',count)
        count = 0
    copy2(path, dst7)
    i = i + 1
    end = time.time()
    count = count + (end - start)

for path in path_name8:
    start = time.time()
    if i % 1000 == 0:
        print(i)
        print('time loop 1000 = ',count)
        count = 0
    copy2(path, dst8)
    i = i + 1
    end = time.time()
    count = count + (end - start)

for path in path_name9:
    start = time.time()
    if i % 1000 == 0:
        print(i)
        print('time loop 1000 = ',count)
        count = 0
    copy2(path, dst9)
    i = i + 1
    end = time.time()
    count = count + (end - start)
