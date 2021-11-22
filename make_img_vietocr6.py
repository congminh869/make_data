import glob, os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw, ImageFilter
import random as rd
import math
from tqdm import tqdm
import time
import numpy
import skimage
import threading
#///////////////////////////////////////////////////////////
# khai báo
path_dir_font = glob.glob('./fonts/*.ttf')
# mode_noise = ["gaussian", "poisson", "pepper", None]
#dir_font = "./fonts/univers59ultracondensed.ttf"
path_background = glob.glob('./backgrounds/*.jpg')
data_bgs = []
for bgs in path_background:
    data_bgs.append(Image.open(bgs))
count = 0
# img_save = '/content/vietocr/data/train/'

path1 = './data/2tr/train_iso_ver/'
path2 = './data/2tr/train_serial_ver/'
path3 = './data/2tr/train_owner_ver/'
path4 = './data/2tr/train_iso_hor/'
path5 = './data/2tr/train_serial_hor/'
path6 = './data/2tr/train_owner_hor/'
path7 = './data/2tr/train_check/'

path9 = './data/2tr/train_owner_ver_100/'

img_save = path9
dict_char = dict()
arr_check = ('0', '1')
#///////////////////////////////////////////////////////////
data_1 = []
with open('./String/owner.txt', 'r') as file:
    data = file.read()
    dir_string = data.split('\n')
    for x in dir_string:
        if x == '':
            dir_string.remove(x)
        if x.find('1') == 0:
            data_1.append(x)
# Make noise
def noise(img):
    mode = rd.choice(["gaussian", "poisson", "pepper", None])
    data = numpy.asarray(img)
    if mode is not None:
        data_noise = skimage.util.random_noise(data, mode=mode)*255.0
        im_noise = Image.fromarray(numpy.uint8(data_noise))
    else:
        im_noise = Image.fromarray(numpy.uint8(data))
    return im_noise
# Vertical
def generate_img_vertical(string, fonts, fonts_size, space_char):
    w, h = fonts.getsize('W')
    img = Image.new('RGB', (w, h*len(string)+space_char*(len(string)-1)), (255, 255, 255))
    img_mask = Image.new('L', (w, h*len(string)+space_char*(len(string)-1)), 0)
    draw = ImageDraw.Draw(img)
    draw_mask = ImageDraw.Draw(img_mask)
    number = 0
    color = rd.choice([(255, 255, 255), (46, 180, 81),(255, 255, 255),(255, 255, 255), (255, 255, 255)])
    for i in string:
        w_ch, h_ch = fonts.getsize(i)
        w_point = round((w-w_ch)/2)
        draw.text((w_point,number*(h+space_char)),i, color ,font=fonts)
        draw_mask.text((w_point,number*(h+space_char)),i,255,font=fonts)
        number+=1
    return img, img_mask, w, h
def generate_img_horizon(string, fonts, fonts_size, space_char):
    w, h = fonts.getsize('W')
    w_max = 0
    for i in string:
        w_i, h_i = fonts.getsize(i)
        w_max += w_i + space_char
    w_max = w_max - space_char
    img = Image.new('RGB', (w_max, h+2), (255, 255, 255))
    img_mask = Image.new('L', (w_max, h+2), 0)
    draw = ImageDraw.Draw(img)
    draw_mask = ImageDraw.Draw(img_mask)
    w_conti = 0
    color = rd.choice([(255, 255, 255), (0, 0, 0)])
    for i in string:
        w_ch, h_ch = fonts.getsize(i)
        draw.text((w_conti,0),i,color ,font=fonts)
        draw_mask.text((w_conti,0),i,255,font=fonts)
        w_conti += w_ch + space_char
    return img, img_mask, w_max
# Rotate Images
def rotate_img(img, img_mask, skew):
    img_ro = img.rotate(skew, expand = True, resample=Image.BICUBIC)
    img_ro_mask = img_mask.rotate(skew, expand = True, resample=Image.BICUBIC)
    return img_ro, img_ro_mask
# Blur Images
def blur_img(img_mask, blur):
    img_blur_mask = img_mask.filter(ImageFilter.BoxBlur(blur))
    return img_blur_mask
# Choose_background
def choose_background(img_text, img_bg):
    # background = rd.choice(path_background)
    #print(background)
    #img_bg = Image.open(path)
    w_bg, h_bg = img_bg.size
    w_txt, h_txt = img_text.size
    if w_bg < w_txt:
        rate = w_txt/w_bg
        img_bg = img_bg.resize((round(w_bg*rate),round(h_bg*rate)))
    w_bg, h_bg = img_bg.size
    if h_bg < h_txt:
        rate = h_txt/h_bg
        img_bg = img_bg.resize((round(w_bg*rate),round(h_bg*rate)))
    w_bg_re, h_bg_re = img_bg.size
    #print(w_bg_re-w_txt)
    start_w_point = rd.randint(0, w_bg_re-w_txt)
    start_h_point = rd.randint(0, h_bg_re-h_txt)
    shape = (start_w_point, start_h_point, start_w_point+w_txt, start_h_point+h_txt)
    img_result = img_bg.crop(shape)
    return img_result
#///////////////////////////////////////////////////////////////////
#Generate Data Funtion
def generate(lock, index):
    t0 = time.time()
    global img_save
    global path_dir_font
    global arr_check
    global data_bgs
    global dir_string
    global img_bg
    global string
    global dir_font
    global choice_st
    global images_path
    global data_1
    number_images = 20000
    img_path_save = img_save + str(index) + '/'
    if not os.path.isdir(img_path_save):
        os.mkdir(img_path_save)
    for i in range(number_images):
        if i%500== 0:
            t1 = round(time.time()-t0, 3)
            t0 = time.time()
            ratio = 0
            if i!= 0:
              ratio = round(500/t1)
            print(f'Thread{index}: {i} images are generated in {t1} s Speed: {ratio} img/s')
        string[index] = rd.choice(dir_string)
        dir_font[index] = rd.choice(path_dir_font)
        choice_st[index] = 1
        img_bg[index] = rd.choice(data_bgs)
        images_path[index] = img_path_save + string[index] + '_' + 'img%09d'%i + '.jpg'
        fonts_size[index] = rd.randint(13,100)
        fonts[index] = ImageFont.truetype(dir_font[index], fonts_size[index])
        if fonts_size[index] < 30:
            blur[index] = 0
        elif fonts_size[index]< 50:
            blur[index] = rd.randint(50, 150)/100
        else:
            blur[index] = rd.randint(150, 250)/100
        #print(choice_st)
        if choice_st[index] == 1:
            img, img_mask, w, h = generate_img_vertical(string[index], fonts[index], fonts_size[index], 0)
            skew = rd.randint(-1000, 1000)/100
            im_rotate, im_ro_mask = rotate_img(img, img_mask, skew)
            lock.acquire()
            img_background = choose_background(im_rotate, img_bg[index] )
            lock.release()
            im_ro_mask = noise(im_ro_mask)
            im_blur_mask = blur_img(im_ro_mask, blur[index])
            img_bg[index] = img_background.copy()
            img_bg[index].paste(im_rotate,(0,0),im_blur_mask)
            img_bg[index] = img_bg[index].rotate(90, expand = True, resample=Image.BICUBIC)
            img_bg[index].save(images_path[index])
        else :
            skew = rd.randint(-1000, 1000)/100
            space_char = rd.randint(0, 20)
            img, img_mask, w_max = generate_img_horizon(string[index], fonts[index], fonts_size[index], space_char)
            im_rotate, im_ro_mask = rotate_img(img, img_mask, skew)
            im_ro_mask = noise(im_ro_mask)
            im_blur_mask = blur_img(im_ro_mask, blur[index])
            lock.acquire()
            img_background = choose_background(im_rotate, img_bg[index])
            lock.release()
            img_bg[index] = img_background.copy()
            img_bg[index].paste(im_rotate,(0,0),im_blur_mask)
            img_bg[index].save(images_path[index])
if __name__ == '__main__':
    threads = []
    img_bg = dict()
    string = dict()
    dir_font = dict()
    choice_st = dict()
    images_path = dict()
    fonts_size = dict()
    fonts = dict()
    blur = dict()
    lock = threading.Lock()
    k = int(input("Number of thread: "))
    for i in range(0, k):
        thread = threading.Thread(target=generate, args=(lock, i,))
        thread.start()
        threads.append(thread)

    # now wait for them all to finish
    for thread in threads:
        thread.join()
