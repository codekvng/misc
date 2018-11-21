import os
import shutil

audio = ['.mp3', '.wav', '.amr', '.ogg', '.acc']
video = ['.avi', '.mkv', '.mp4', '.MP4', '.flv']
image = ['.png', '.jpg', 'jpeg']


class FileOp(object):
    """sorting and moving of files into separate
    directories"""

    def __init__(self, path, files_type='others'):
        self.path = path
        self.files_type = files_type
        self.files = list()
        self.s_dict = dict()

    def __file_list(self):
        """return a list of all files in the directory"""
        if not os.path.isdir(self.path):
            return

        os.chdir(self.path)   # Change the current working directory
        for root, dirs, files in os.walk(self.path):
            for file in files:
               title, ext = os.path.splitext(file)

               if ext in ['.bat', '.BAT']:
                    files.remove(file)   # Remove all batch files from the list
        self.files = files[:]

    def __sort(self):
        """sorts a list of files into
        the various categories"""
        self.s_dict['audios'] = list()
        self.s_dict['videos'] = list()
        self.s_dict['images'] = list()
        self.s_dict['others'] = list()

        for file in self.files:
            f_type = self.file_type(file)
            if f_type == 'others':
                self.s_dict['others'].append(file)
                continue
            self.s_dict[f_type].append(file)

    def __move(self, to=''):
        """move files into given directories"""
        if to == self.path:
            return False
        if not os.path.isdir(to):
            os.mkdir(to)

        for file in self.s_dict[f'{self.files_type}']:
            shutil.move(file, to + f'\\{self.files_type}\\{file}')

        return True

    def file_type(self, file):
        global audio, video, image
        f_type = 'others'
        for type_name, type_list in zip(['audio', 'video', 'image'], [audio, video, image]):
            _, ext = os.path.splitext(file)
            if ext in type_list:
                f_type = type_name

        return f_type

    def file_list(self):
        return self.__file_list()

    def sort(self):
        return self.__sort()

    def move(self, to=''):
        return self.__move(to)

def test():
    f_op = FileOp(r'C:\Users\user\Documents\Codekvng')
    f_op.file_list()
    f_op.sort()
    f_op.move(to=r'C:\Users\user\Documents\Codekvng\new')

test()
