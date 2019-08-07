import os
import shutil

# 文件夹路径
dst_dir='C:/Users/chessur/Desktop/wallpaper/'
src_dir='C:/Users/chessur/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/'

# dst_dir下图片名称
picture_names = os.listdir(dst_dir)
name_set = set()
for picture_name in picture_names:
    name_set.add(picture_name.rstrip('.jpg'))

# src_dir下图片名称
new_picture_names = os.listdir(src_dir)
# 检查是否重复，检查完之后复制图片
count = 0
for picture_name in new_picture_names:
    if picture_name not in name_set:
        shutil.copyfile(src_dir + picture_name,dst_dir + picture_name +'.jpg')
        count += 1
if count:
    print('[+] 复制%d张图片' %(count))
else:
    print('[+] 没有新图片')

