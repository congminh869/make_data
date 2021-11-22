import glob
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw, ImageFilter
import random as rd
import math
from tqdm import tqdm
import time

import numpy
import skimage
number_input = int(input("Nhập vào số lượng ảnh cần tạo: "))
dir_font = glob.glob('./fonts/*.ttf')
dir_bg = glob.glob('./backgrounds/*.jpg')
path_save = '/home/minh/Documents/minh/ai_thay_cuong/vietocr/data/train_check/InkData_line_processed/'
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
index = dict()
for i, j in enumerate(number):
    index[j] = i
# print(index)
k = 0 
count = 0
path_labels = []
for i in range(number_input):
    start = time.time()
    if k % 10000 == 0:
         print(i)
         print('time loop 10000 = ',count)
         count = 0
    fonts_size = rd.randint(8, 80)
    # print('a')
    font = ImageFont.truetype(rd.choice(dir_font), fonts_size)
    # print('b')
    skew = rd.randint(-500, 500)/100
    string = rd.choice(number)
    # print("soo dc chon la ", string)
    bg = rd.choice(dir_bg)
    if fonts_size < 20:
        rec = rd.randint(1, 3)
        blur = 0
    elif fonts_size < 50:
        rec = rd.randint(2, 4)
        blur = rd.randint(50, 80)/100
    else:
        rec = rd.randint(5, 10)
        blur = rd.randint(80, 100)/100
    w, h = font.getsize('W')
    w_1, h_1 = font.getsize(string)
    #shape = rd.randint(2, int(h/8)+1)
    img = Image.new('RGB', (w, h), (255, 255, 255))
    img_mask = Image.new('L', (w, h), 0)
    color = rd.choice([(255, 255, 255), (0, 0, 0)])
    draw = ImageDraw.Draw(img)
    draw_mask = ImageDraw.Draw(img_mask)
    draw.text(((w-w_1)/2,(h-h_1)/2),string,color ,font=font)
    draw_mask.text(((w-w_1)/2,(h-h_1)/2),string,255,font=font)
    for j in range(rec):
        draw.rectangle([(j, j), (w-j, h-j)], fill = None, outline = color)
        draw_mask.rectangle([(j, j), (w-j, h-j)], fill = None, outline = 255)
    img = img.rotate(skew, expand = True, resample=Image.BICUBIC)
    img_mask = img_mask.rotate(skew, expand = True, resample=Image.BICUBIC)
    #img_mask = img_mask.filter(ImageFilter.BoxBlur(blur))
    w_n, h_n = img.size
    img_bg = Image.open(bg)
    w_bg, h_bg = img_bg.size
    try:
        start_w_point = rd.randint(0, w_bg-w_n)
        start_h_point = rd.randint(0, h_bg-h_n)
    except:
        print('ValueError: empty range for randrange()')
    bbox = (start_w_point, start_h_point, start_w_point+w_n, start_h_point+h_n)
    img_bg = img_bg.crop(bbox)
    img_result = img_bg.copy()
    img_result.paste(img,(0,0),img_mask)
    img_result = img_result.filter(ImageFilter.BoxBlur(blur))
    center = (int(w_n/2), int(h_n/2))
    # with open(path_save+string+'_img_%05d.txt'%i, 'w') as file:
    #     file.write(str(index[string])+ ' ' + str(int(w_n/2)/w_n) + ' ' + str(int(h_n/2)/h_n) + ' 1 1')
    #save image
    name_path = 'InkData_line_processed/'+string+'_img_%05d.jpg'%i+'\t'+string
    path_labels.append(name_path)
    #print(path_save+'img_%05d.jpg'%i)
    img_result.save('/home/minh/Documents/minh/ai_thay_cuong/vietocr/data/train_check/InkData_line_processed/'+string+'_img_%05d.jpg'%i) 
    end = time.time()
    k = k + 1
    count = count + (end - start)

path_labels_train = path_labels[:int(len(path_labels)*0.9)]
path_labels_test = path_labels[int(len(path_labels)*0.9):]

f = open('/home/minh/Documents/minh/ai_thay_cuong/vietocr/data/train_check/train_line_annotation.txt', "w")
for item in path_labels_train:
    f.write(item + "\n")
f.close()

k = open('/home/minh/Documents/minh/ai_thay_cuong/vietocr/data/train_check/test_line_annotation.txt', "w")
for item in path_labels_test:
    k.write(item + "\n")
k.close()

