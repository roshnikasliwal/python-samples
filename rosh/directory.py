"""
Specifies a directory containing pictures and videos to be processed.

.. module:: directory
    :synopsis: module defining a directory containing files to be processed.

.. moduleauthor:: Roshni Kasliwal <kasliwalroshni27@gmail.com>
"""
import os
from .file import File


class Directory:
    """Defines a directory containing files and sub-directories to be processed.

    This class defines a directory that contains any number of files and sub-directories
    that will be copied from the source directory to the destination directories; there
    are separate destination directories for pictures and videos.

    The constructor checks that the path for the source directory and the path for the two
    destination directories (pictures and videos) are valid.  Next, all the files based on
    the source directory and its sub-directories are identified and sorted.  Finally, the
    parameters about the copy operation for this class are initialized to zeros.

    :param source_directory: path of this directory
    :param picture_destination_directory: directory where the picture files will be attempted to be
                                          copied to
    :param video_destination_directory: directory where the video files will be attempted to be
                                        copied to
    """
    def __init__(self, directory_path, picture_destination_directory, video_destination_directory) -> None:
        self.directory_path = File.check_directory_name(directory_path)
        self.picture_destination_directory = File.check_directory_name(picture_destination_directory)
        self.video_destination_directory = File.check_directory_name(video_destination_directory)
        self.number_of_picture_files = 0
        self.number_of_video_files = 0
        self.files = self.collect_all_files()
        self.files_copied = 0
        self.files_not_copied = 0

    def __repr__(self):
        return f'{self.directory_path}'

    def collect_all_files(self):
        """Returns a list of all the files in the source directory and its sub-directories"""
        all_files = []
        for root, _, files in os.walk(self.directory_path):
            for file in files:
                picture_extensions = ['jpg', 'jpeg']
                videos_extensions = ['mov']

                __, file_extension = os.path.splitext(file)
                if file_extension.lstrip('.').lower() in picture_extensions:
                    all_files.append(File(os.path.join(root, file), self.picture_destination_directory))
                    self.number_of_picture_files += 1
                elif file_extension.lstrip('.').lower() in videos_extensions:
                    all_files.append(File(os.path.join(root, file), self.video_destination_directory))
                    self.number_of_video_files += 1
                else:
                    print('File is not supported: {file}')

        return all_files

    def print_summary(self) -> None:
        """Prints a summary of the directory to the console"""
        print('Directory Summary:')
        print('------------------')
        print(f'Directory path: {self.directory_path}')
        print(f'Destination path (Pictures): {self.picture_destination_directory}')
        print(f'Destination path (Videos): {self.video_destination_directory}')
        print(f'Number of files: {len(self.files)}')
        print(f'Number of Picture files: {self.number_of_picture_files}')
        print(f'Number of Video files: {self.number_of_video_files}')
        print('Number of files copied: {}'.format(self.files_copied))
        print('Number of files not copied: {}'.format(self.files_not_copied))

    def copy_files(self):
        """Copies all of the picture and video files to the applicable destination directories"""
        for file in self.files:
            file.copy_to_destination_directory()

        for file in self.files:
            if file.copy_successful:
                self.files_copied += 1
            else:
                self.files_not_copied += 1

