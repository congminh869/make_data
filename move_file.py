import shutil
import glob
import time

path_name2 = []
path_iso_hor = '/media/minh/New Volume1/AI_thay_cuong/Make_data/data/2tr/train_iso_hor/'
target = '/media/minh/New Volume1/AI_thay_cuong/Make_data/data/2tr/train_iso_hor/InkData_line_processed/'
for i in range(0,100):
	for name in glob.glob(path_iso_hor+str(i)+'/*jpg'):
		# print(name)
		path_name2.append(name)

print(len(path_name2))

i = 0
count = 0
k =0 
for path_name in path_name2:
	start = time.time()
	if i % 1000 == 0:
		print(i)
		print('time loop 1000 = ',count)
		count = 0
	try:
		shutil.move(path_name,target)
	except Exception as e:
		k = k+1
	i = i + 1
	end = time.time()
	count = count + (end - start)

# original = r'original path where the file is currently stored\file name.file extension'
# target = r'target path where the file will be moved\file name.file extension'

# shutil.move(original,target)