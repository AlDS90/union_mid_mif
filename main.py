import os
import time


start_time = time.time()


main_dir = r'\\192.168.1.40\All\Сотниченко А.Д\programs\extract_files\to'
path_mid = r'\\192.168.1.40\All\Сотниченко А.Д\programs\union_mid_mif\all.mid'
path_mif = r'\\192.168.1.40\All\Сотниченко А.Д\programs\union_mid_mif\all.mif'
begin_mif = '''Version 300
Charset "WindowsCyrillic"
Delimiter ","
CoordSys NonEarth Units "m" Bounds (-10000000, -10000000) (10000000, 10000000)
Columns 3
  ID Integer
  LABEL Char(254)
  NOTE Char(254)
Data
'''
ext_mid = '.mid'
ext_mif = '.mif'


all_files = os.listdir(main_dir)
files = set([file[:-4] for file in all_files])
file_list_mid = [n for n in list(map(lambda x: x if x.endswith(ext_mid) else None, all_files)) if n]
file_list_mif = [n for n in list(map(lambda x: x if x.endswith(ext_mif) else None, all_files)) if n]
d_file_list_mid = {}
d_file_list_mif = {}
for file in file_list_mid:
    d_file_list_mid[file] = main_dir + os.sep + file
for file in file_list_mif:
    d_file_list_mif[file] = main_dir + os.sep + file
with open(path_mid, 'w') as ouf_mid, \
     open(path_mif, 'w') as ouf_mif:
    ouf_mif.write(begin_mif)
    for file in files:
        with open(d_file_list_mid[file + ext_mid]) as next_file_mid:
            ouf_mid.write(next_file_mid.read())
        with open(d_file_list_mif[file + ext_mif]) as next_file_mif:
            ouf_mif.write('\n'.join(next_file_mif.read().split('\n')[9:]))


print("--- %s seconds ---" % (time.time() - start_time))
