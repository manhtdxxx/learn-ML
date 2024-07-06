from PIL import Image
import os

def show_image(path):
    try:
        image = Image.open(path)
        return image
    except Exception as e:
        print(e)
        return None


def isImage(path):
    extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
    return path.lower().endswith(extensions)
# TypeError: endswith first arg must be str or a tuple of str, not list


def listing_images(folder_path):
    image_list = []
    
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        file_names = os.listdir(folder_path)  # liệt kê các folder (k liệt kê file trong folder) và file trong folder_path
        
        for i in file_names:
            file_path = os.path.join(folder_path, i)
            if isImage(file_path) and os.path.isfile(file_path):
                image = show_image(file_path)
                image_list.append(image)
                
    return image_list
        
        