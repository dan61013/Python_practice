# https://eastlakeside.gitbook.io/interpy-zh/open_func
# open函數

import io

def main():
    # rb -> 二進制
    with open('./Intermediate_Python/laptop-2620118_1280.jpg', 'rb') as inf:
        # jpgdate -> bytes內容
        jpgdata = inf.read()
        print(type(jpgdata))
        # print(jpgdata)
    
    # jpg圖檔的二進制(bytes)開頭 -> b'\xff\xd9'
    if jpgdata.startswith(b'\xff\xd8'):
        text = u'This is a JPEG file (%d bytes long)\n'
    else:
        text = u'This is a random file (%d bytes long)\n'
    
    with io.open('./Intermediate_Python/laptop-2620118_1280.txt', 'w', encoding='utf-8') as outf:
        outf.write(text % len(jpgdata))
    
    print(text % len(jpgdata)) # This is a JPEG file (166957 bytes long)

if __name__ == "__main__":
    main()