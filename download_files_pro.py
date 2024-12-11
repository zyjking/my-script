#Read a text file line by line and download those files
#and save them to a specific directory based on the URL
#For example: There are two files with the following URL
#https://game.example.com/play/files/example.exe
#https://game.example.com/play/txt/new/example.txt
#example.exe will be saved to /the/python/script/path/files/example.exe
#example.txt will be saved to /the/python/script/path/txt/new/example.txt

import requests
import time
import os

def download_file(url):
    try:
        print(f'Trying to download: \033[1;36m{url}\033[0;0m')
        
        #Split URL
        #Replace "/play/" with another string based on your needs
        path = url.split('/play/')[1]
        directory, file_name = os.path.split(path)
        
        #Remove unexpected carriage return
        directory = directory.replace('\n', '')
        file_name = file_name.replace('\n', '')
        
        #Create directory based on the URL
        if len(directory) != 0:
            if not os.path.exists(directory):
                os.makedirs(directory)
        
        #Download file
        file = requests.get(url, timeout=20)
        if file.status_code == 200:
            print(f'Now downloading: \033[1;33m{file_name}\033[0;0m')
            print(f'File length: \033[1;34m{len(file.content)}\033[0;0m')
            
            if len(directory) != 0:
                print(f'Saving to: \033[0;33m{directory}\033[0;0m')
            else:
                print(f'Saving to: \033[1;32mthe root directory\033[0;0m')         
            file_path = os.path.join(directory, file_name)
            with open(file_path,'wb') as f:
                f.write(file.content)
                f.close()
                time.sleep(0.200)
            print(f'\033[1;32mDone!\033[0;0m')
            print(f"\033[1;35m----------------------------------------\033[0;0m")
        else:
            print(f'\033[1;31mFailed to download {file_name}. Status code: {file.status_code}\033[0;0m')
            print(f'\033[1;35m----------------------------------------\033[0;0m')
            with open('error.txt', 'a') as f:
                print(f'{url}\nStatus code: {file.status_code}\n', file=f)
                f.close()
                time.sleep(0.200)
    except requests.exceptions.RequestException as e:
        print(f'\033[1;31mAn error occured for downloading file!\033[0;0m\n')
        print(f'\033[1;35m----------------------------------------\033[0;0m')
        with open('error.txt', 'a') as f:
            f.write(url)
            f.close()
            time.sleep(0.200)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('color')
    print(f'\033[1;35m----------------------------------------\033[0;0m')
    
    #Read "files.txt" line by line
    with open('files.txt') as f:
        for line in f:
            download_file(line)

if __name__ == "__main__":  
    main()  