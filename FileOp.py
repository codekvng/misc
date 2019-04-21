import os
import shutil


class FileOp(object):
    """sorting and moving of files into separate
    directories"""

    def __init__(self, path, files_type='others'):
        self.path = path
        self.files_type = files_type
        self.files = list()
        self.files_dict = {'audio': ['.mp3', '.wav', '.amr', '.ogg', '.acc'],
        'video': ['.avi', '.mkv', '.mp4', '.MP4', '.flv'],
        'image': ['.png', '.jpg', 'jpeg'],
        'others': ['.py', '.txt', '.html', '.js', '.css'],
        }

    def __file_list(self):
        """return a list of all files in the directory"""
        if not os.path.isdir(self.path):
            return
        for root, _, files in os.walk(self.path):
            for file in files:
                files.insert(files.index(file), os.path.join(root, file))
                files.remove(file)
        print(files)
        self.files = list(filter(lambda x: os.path.splitext(x)[1] in self.files_dict[self.files_type], files))
        print(self.files)

    def __move(self, to=''):
        """move files into given directories"""
        if to == self.path:
            return False
        if not os.path.isdir(to):
            os.mkdir(to)

        for file in self.files:
            print(f'Moving {file}')
            shutil.move(file, to + f'\\{self.files_type}\\{file}')

        return True

    def file_type(self, file):
        f_type = ''
        for type_name, type_list in zip(['audio', 'video', 'image', 'others'], list(self.files_dict.keys())):
            _, ext = os.path.splitext(file)
            if ext in type_list:
                f_type = type_name
                return f_type
        return None

    def file_list(self):
        return self.__file_list()

    def move(self, to=''):
        return self.__move(to)

def test():
    f_op = FileOp(r'')
    f_op.file_list()
    f_op.move(to=r'')

test()
