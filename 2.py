from shutil import copy2
import glob
path_name = []
i = 0 
for i in range(0,20):
    for name in glob.glob('/media/minh/New Volume/hoctaps/nam4/tri_tue_nhan_tao_va_ung_dung/hocKy2/codebtl/Make_data/data/train_iso_hor/'+str(i)+'/*.jpg'):
        # print(name)
        path_name.append(name)
print(len(path_name))
dst = '/home/minh/Documents/minh/ai_thay_cuong/vietocr/data_hor/train_iso/InkData_line_processed'
for path in path_name:
    copy2(path, dst)
    print(i)
    i = i + 1