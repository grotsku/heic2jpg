from PIL import Image
import pillow_heif
import os

pillow_heif.register_heif_opener()

file_list = []

# get list of .heic files
#directory = input('input directory path: ')
directory = '/home/olli/code/heic2jpg/'

def get_files():
    for file in os.listdir(directory):
        if file.endswith('.heic'):
            file_list.append(file)
        else:
            continue

    print('file list get')
    print('files found: ' + str(file_list))

def convert_files():

    for file in file_list:
        # get file
        image = Image.open(os.path.join(directory, file))
        # convert image
        image.convert('RGB').save(os.path.join(directory, os.path.splitext(file)[0] + '.jpg'))
        print(str(image) + ' converted')

def main():
    get_files()
    convert_files()
    print('conversion(s) complete!')

main()
