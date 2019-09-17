"""
This file (test_file.py) contains the unit tests for the File class in the file.py file.
"""
from bild.file import File
import os
import pytest


FIXTURE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_files', '')


def test_new_picture_file_nominal():
    """
    GIVEN a new picture file
    WHEN the directories specified don't include a trailing '/'
    THEN check the filename, source directory, and destination directory are defined correctly
    """
    new_file = File('/Users/me/Pictures/iPhone8/img001.jpg', '/Users/me/Pictures/Pictures')
    assert new_file.filename_with_path == '/Users/me/Pictures/iPhone8/img001.jpg'
    assert new_file.base_destination_directory == '/Users/me/Pictures/Pictures/'
    assert new_file.copy_successful == False
    assert new_file.file_type == 'Picture'
    assert new_file.date_created == ''
    assert new_file.destination_directory == '/Users/me/Pictures/Pictures/Date_Unknown'


def test_new_picture_file_directories_with_trailing_slashes():
    """
    GIVEN a new picture file
    WHEN the directories specified do include a trailing '/'
    THEN check the filename, source directory, and destination directory are defined correctly
    """
    new_file = File('/Users/me/Pictures/iPhone8/img002.JPEG', '/Users/me/Pictures/Pictures/')
    assert new_file.filename_with_path == '/Users/me/Pictures/iPhone8/img002.JPEG'
    assert new_file.base_destination_directory == '/Users/me/Pictures/Pictures/'
    assert new_file.copy_successful == False
    assert new_file.file_type == 'Picture'
    assert new_file.date_created == ''
    assert new_file.destination_directory == '/Users/me/Pictures/Pictures/Date_Unknown'


def test_new_file_source_directory_contains_date():
    """
    GIVEN a new file
    WHEN the source directory contains the date
    THEN check the filename, source directory, and destination directory are defined correctly
    """
    new_file = File('/Users/me/Pictures/iPhone8/2018-08-22/img002.jpg', '/Users/me/Pictures/Pictures/')
    assert new_file.filename_with_path == '/Users/me/Pictures/iPhone8/2018-08-22/img002.jpg'
    assert new_file.base_destination_directory == '/Users/me/Pictures/Pictures/'
    assert new_file.copy_successful == False
    assert new_file.file_type == 'Picture'
    assert new_file.date_created == '2018-08-22'
    assert new_file.destination_directory == '/Users/me/Pictures/Pictures/2018/2018-08-22'


def test_new_file_source_directory_contains_date2():
    """
    GIVEN a new file
    WHEN the source directory contains the date
    THEN check the filename, source directory, and destination directory are defined correctly
    """
    new_file = File('/Users/me/Pictures/iPhone8/2018_08_23/img002.jpg', '/Users/me/Pictures/Pictures/')
    assert new_file.filename_with_path == '/Users/me/Pictures/iPhone8/2018_08_23/img002.jpg'
    assert new_file.base_destination_directory == '/Users/me/Pictures/Pictures/'
    assert new_file.copy_successful == False
    assert new_file.file_type == 'Picture'
    assert new_file.date_created == '2018-08-23'
    assert new_file.destination_directory == '/Users/me/Pictures/Pictures/2018/2018-08-23'


def test_new_video_file_nominal():
    """
    GIVEN a new video file
    WHEN the directories specified don't include a trailing '/'
    THEN check the filename, source directory, and destination directory are defined correctly
    """
    new_file = File('/Users/me/Pictures/iPhone8/img003.MOV', '/Users/me/Pictures/Pictures')
    assert new_file.filename_with_path == '/Users/me/Pictures/iPhone8/img003.MOV'
    assert new_file.base_destination_directory == '/Users/me/Pictures/Pictures/'
    assert new_file.copy_successful == False
    assert new_file.file_type == 'Video'
    assert new_file.date_created == ''
    assert new_file.destination_directory == '/Users/me/Pictures/Pictures/Date_Unknown'


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, 'IMG_0016.JPG'))
def test_extract_date_picture(datafiles, tmpdir):
    """
    GIVEN a new picture file
    WHEN the creation date is extracted from the metadata
    THEN check the creation date extracted is correct
    """
    for file in datafiles.listdir():
        new_file = File(str(file), os.path.join(str(tmpdir), 'Pictures'))
        assert new_file.filename_with_path.endswith('IMG_0016.JPG')
        assert new_file.copy_successful == False
        assert new_file.file_type == 'Picture'
        assert new_file.date_created == '2014-05-25'


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, 'IMG_1019.JPG'))
def test_extract_date_picture2(datafiles, tmpdir):
    """
    GIVEN a new picture file
    WHEN the creation date is extracted from the metadata
    THEN check the creation date extracted is correct
    """
    for file in datafiles.listdir():
        new_file = File(str(file), os.path.join(str(tmpdir), 'Pictures'))
        assert new_file.filename_with_path.endswith('IMG_1019.JPG')
        assert new_file.copy_successful == False
        assert new_file.file_type == 'Picture'
        assert new_file.date_created == '2017-02-11'


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, '2019_05_06'), keep_top_dir=True)
def test_extract_date_picture3(datafiles, tmpdir):
    """
    GIVEN a new picture file
    WHEN the creation date is extracted from the metadata
    THEN check the creation date extracted is correct
    """
    for directory in datafiles.listdir():
        print(directory)
        new_file = File(os.path.join(str(directory), 'IMG_9165.JPG'), os.path.join(str(tmpdir), 'Pictures'))
        assert new_file.filename_with_path.endswith('IMG_9165.JPG')
        assert new_file.copy_successful == False
        assert new_file.file_type == 'Picture'
        assert new_file.date_created == '2019-05-06'


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, '2019_05_06'), keep_top_dir=True)
def test_extract_date_picture4(datafiles, tmpdir):
    """
    GIVEN a new picture file
    WHEN the creation date is extracted from the metadata
    THEN check the creation date extracted is correct
    """
    for directory in datafiles.listdir():
        print(directory)
        new_file = File(os.path.join(str(directory), 'IMG_9165.JPG'), os.path.join(str(tmpdir), 'Pictures'))
        assert new_file.filename_with_path.endswith('IMG_9165.JPG')
        assert new_file.copy_successful == False
        assert new_file.file_type == 'Picture'
        assert new_file.date_created == '2016-12-22'


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, '2019-05-04_12-54-13_IMG_3413.JPG'))
def test_extract_date_picture4(datafiles, tmpdir):
    """
    GIVEN a new picture file
    WHEN the creation date is extracted from the metadata
    THEN check the creation date extracted is correct
    """
    for file in datafiles.listdir():
        new_file = File(str(file), os.path.join(str(tmpdir), 'Pictures'))
        assert new_file.filename_with_path.endswith('2019-05-04_12-54-13_IMG_3413.JPG')
        assert new_file.copy_successful == False
        assert new_file.file_type == 'Picture'
        assert new_file.date_created == '2019-05-04'


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, '2019-01-05_13-25-15_IMG_0036.MOV'))
def test_extract_date_video(datafiles, tmpdir):
    """
    GIVEN a new video file
    WHEN the creation date is extracted from the metadata
    THEN check the creation date extracted is correct
    """
    for file in datafiles.listdir():
        new_file = File(str(file), os.path.join(str(tmpdir), 'Videos'))
        assert new_file.filename_with_path.endswith('2019-01-05_13-25-15_IMG_0036.MOV')
        assert new_file.copy_successful == False
        assert new_file.file_type == 'Video'
        assert new_file.date_created == '2019-01-05'


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, 'IMG_0036.MOV'))
def test_extract_date_video2(datafiles, tmpdir):
    """
    GIVEN a new video file
    WHEN the creation date is extracted from the metadata
    THEN check the creation date extracted is correct
    """
    for file in datafiles.listdir():
        new_file = File(str(file), os.path.join(str(tmpdir), 'Videos'))
        assert new_file.filename_with_path.endswith('IMG_0036.MOV')
        assert new_file.copy_successful == False
        assert new_file.file_type == 'Video'
        assert new_file.date_created == '2019-01-08'


def test_unsupported_file():
    """
    GIVEN an unsupported file
    WHEN the directories specified don't include a trailing '/'
    THEN check the filename, source directory, and destination directory are defined correctly
    """
    new_file = File('/Users/me/Pictures/iPhone8/img001.txt', '/Users/me/Pictures/Pictures')
    assert new_file.filename_with_path == '/Users/me/Pictures/iPhone8/img001.txt'
    assert new_file.base_destination_directory == '/Users/me/Pictures/Pictures/'
    assert new_file.copy_successful == False
    assert new_file.file_type == ''
    assert new_file.date_created == ''
    assert new_file.destination_directory == ''

