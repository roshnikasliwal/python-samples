"""
Specifies a file (picture or video) to be processed.

.. module:: file
    :synopsis: module defining a file containing files to be processed.

.. moduleauthor:: Roshni Kasliwal <kasliwalroshni27@gmail.com>
"""
import subprocess
import os
from shutil import copy2


class File:
    """Defines a file to be copied to a destination directory.

    This class defines a file that will be copied from its source directory to a
    destination directory, if the file does not exist in the destination directory already.

    The destination directory is expected to be in the following format:
        .../<Pictures, Videos>/yyyy/yyyy-mm-dd

    For example, the destination directory might be:
        .../Pictures/2018/2018-08-22

    :param filename_with_path: full path to the name
    :param base_destination_directory: base directory where to copy the file to
    :param destination_directory: directory where the file will be attempted to be
                                  copied to
    :param date_created: date (in format of "xx-yy-zz", such as "12-23-15" for
                         December 23rd, 2015)
    :param copy_successful: flag indicating if the copy from the source directory
                            to the destination directory was successful
    :param file_type: string indicating if the file is a picture or video
    """
    def __init__(self, filename_with_path: str, destination_directory: str = '') -> None:
        """Initialize the parameters for the file."""
        self.filename_with_path = filename_with_path
        self.base_destination_directory = File.check_directory_name(destination_directory)
        self.destination_directory = ''
        self.copy_successful = False
        self.file_type = File.check_file_extension(filename_with_path)
        self.date_created = ''
        if self.valid_file_type():
            self.extract_date_created()

    def __repr__(self):
        return f'{self.filename_with_path}'

    @staticmethod
    def check_directory_name(directory_name: str) -> str:
        """Check that the specified directory ends with a slash (OS-specific)."""
        if not directory_name.endswith(os.sep):
            return os.path.join(os.path.abspath(directory_name), '')

        return directory_name

    @staticmethod
    def check_file_extension(filename: str) -> str:
        """Check if the file is a picture or video file"""
        picture_extensions = ['jpg', 'jpeg']
        videos_extensions = ['mov']
        filename, file_extension = os.path.splitext(filename)
        if file_extension.lstrip('.').lower() in picture_extensions:
            return 'Picture'
        if file_extension.lstrip('.').lower() in videos_extensions:
            return 'Video'
        return ''

    def valid_file_type(self) -> bool:
        """Returns if this file is a valid media (picture or video) file"""
        return self.file_type == 'Picture' or self.file_type == 'Video'

    def print_details(self) -> None:
        """Print the details about the file, including the copy results."""
        print(f'File details:')
        print(f'    File: { self.filename_with_path }')
        print(f'    Destination directory: { self.destination_directory }')
        print(f'    File type: { self.file_type }')
        print(f'    Date created: { self.date_created }')
        print(f'    Copy successful: { self.copy_successful }')

    def copy_to_destination_directory(self):
        """Copy the file from the source directory to the destination directories (picture or video).

        First, this method first checks if the destination directory exists.  If it does not, then the
        destination directory is created.

        Second, this method checks if the file exists in the destination directory.  If it does not,
        then the file is copied to the destination directory.

        """
        if self.valid_file_type():
            if not os.path.isdir(self.destination_directory):
                print('Destination directory does NOT exist!')
                try:
                    os.makedirs(self.destination_directory)
                except OSError as exception:
                    print(f'Mkdir Exception: {str(exception)}')

            if not os.path.isfile(os.path.join(self.destination_directory, os.path.basename(self.filename_with_path))):
                print('\tFile is NOT located in the destination directory!')
                print(f'Copying {os.path.basename(self.filename_with_path)} to {self.destination_directory}')
                try:
                    copy2(self.filename_with_path, self.destination_directory)
                    self.copy_successful = True
                except OSError as exception:
                    print(f'Copy2 Exception: {str(exception)}')
            else:
                print('File exists in the destination directory.')
                self.copy_successful = False
        else:
            print(f'Not copying file... file type is not a Picture or Video!')

    def extract_creation_data_from_metadata(self) -> str:
        """Extract the date that the file was created by reading the metadata"""
        extracted_date = ''

        out = subprocess.run(f'hachoir-metadata {self.filename_with_path}',
                             shell=True,
                             encoding='ascii',
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        print(out.returncode)
        print('-------')

        if out.returncode == 0:
            line_dictionary = out.stdout.split('\n')
            for line in line_dictionary:
                print(line)
                if line.lstrip(' -').startswith('Creation date'):
                    extracted_date = line[17:27]
                    print(f'Found date_created ({extracted_date}) metadata!')
                    break
        else:
            print('Error! Running hachoir-metadata returned non-zero value!')

        return extracted_date

    def extract_date_created(self):
        """Extract the date that this file was created for determining the destination directory

        This method checks for the date that this file was created in the following order:
            1. Check if the date is in the source folder name
            2. Check if the data is in the file name
            3. Check if the data is in the metadata for the file

        If the date cannot be found from these three options, then the destination directory
        is set to 'Date Unknown'.
        """
        directories = self.filename_with_path.split('/')
        directories = [directory for directory in directories if directory != '']

        if directories[-2].startswith('20'):
            self.date_created = directories[-2][:10].replace('_', '-')
        elif directories[-1].startswith('20'):
            self.date_created = directories[-1][:10].replace('_', '-')
        else:
            self.date_created = self.extract_creation_data_from_metadata()

        if self.date_created == '':
            self.destination_directory = os.path.join(self.base_destination_directory, 'Date_Unknown')
        else:
            self.destination_directory = os.path.join(self.base_destination_directory,  # Destination Directory (base)
                                                      self.date_created[0:4],           # Year
                                                      self.date_created)                # Date

