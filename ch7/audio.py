import os
from pygame import mixer

def absoluteFilePaths(directory):
    return_list = [ ]
    
    cnt = 1
    print("--------------------------")
    print("輸入 E 結束程式")
    for dirpath,_,filenames in os.walk(directory):
        filenames.sort()
        for f in filenames:
            if f.endswith((".mp3")):
                FullFileName=os.path.abspath(os.path.join(dirpath, f))
                print (f"{cnt}.{f}")
                return_list.append(FullFileName)
                cnt += 1
    
    return return_list
    
folder_location = '/home/pi/mp3'
file_list = absoluteFilePaths(folder_location)
total = len(file_list)
# print(file_list)
mixer.init()
now = 0
print("--------------------------")

while True:
    if mixer.music.get_busy() != True:
        a = input("播放編號:")
        
        if a.lower() == 'e':
            print("------退出程式------")
            break

        # print(f'now= {now}, total = {total}')
        mixer.music.load(file_list[int(a)-1])
        print(f"撥放音檔: {file_list[int(a)-1]}")
        mixer.music.play()
        print(f"撥放音檔: {file_list[int(a)-1]} 結束\n--------------------------")
            