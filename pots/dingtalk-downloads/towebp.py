import os

while True:
    os.system('cls')
    filename=''
    toname=''
    filename=input('待转换的文件名: ')
    toname=input('转换后的文件名(*.webp): ')

    if filename!='' and toname!='':

        if os.path.exists(filename)==True:
            os.system('cwebp -q 100 '+filename+' -o '+toname+'.webp')
            input('转换完毕,按下回车键以继续转换')
        else:
            print('文件不存在,请检查文件名')

    else:
        print('文件名为空')