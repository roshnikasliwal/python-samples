"""
This file (test_directory.py) contains the unit tests for the Directory class in the directory.py file.
"""
from bild.directory import Directory
import os
import pytest


FIXTURE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_files', '')


def test_new_directory_nominal():
    """
    GIVEN a new directory
    WHEN the directories are specified with nominal values
    THEN check the Directory object was created correctly
    """
    new_directory = Directory('/Users/me/Pictures/iPhone8',    # Source Directory
                              '/Users/me/Pictures/Pictures',   # Destination Directory (Pictures)
                              '/Users/me/Pictures/Videos')     # Destination Directory (Videos)
    assert new_directory.directory_path == '/Users/me/Pictures/iPhone8/'
    assert new_directory.picture_destination_directory == '/Users/me/Pictures/Pictures/'
    assert new_directory.video_destination_directory == '/Users/me/Pictures/Videos/'


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, '2019_05_06'), keep_top_dir=True)
def test_new_directory_with_date(datafiles, tmpdir):
    """
    GIVEN a new directory containing the date in the directory name
    WHEN the directory contains pictures and videos
    THEN check that the files are all copied
    """
    for directory in datafiles.listdir():
        backup_pictures = tmpdir.mkdir('Pictures')
        backup_videos = tmpdir.mkdir('Videos')
        new_directory = Directory(str(directory),        # Source Directory
                                  str(backup_pictures),  # Destination Directory (Pictures)
                                  str(backup_videos))    # Destination Directory (Videos)
        new_directory.print_summary()
        assert len(new_directory.files) == 4
        assert new_directory.number_of_picture_files == 3
        assert new_directory.number_of_video_files == 1
        new_directory.copy_files()
        assert new_directory.files_copied == 4
        assert new_directory.files_not_copied == 0

@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, 'phone_pictures'), keep_top_dir=True)
def test_new_directory_without_date(datafiles, tmpdir):
    """
    GIVEN a new directory without the date in the directory name
    WHEN the directory contains pictures and videos
    THEN check that the files are all copied
    """
    for directory in datafiles.listdir():
        backup_pictures = tmpdir.mkdir('Pictures')
        backup_videos = tmpdir.mkdir('Videos')
        new_directory = Directory(str(directory),        # Source Directory
                                  str(backup_pictures),  # Destination Directory (Pictures)
                                  str(backup_videos))    # Destination Directory (Videos)
        new_directory.print_summary()
        assert len(new_directory.files) == 2
        assert new_directory.number_of_picture_files == 1
        assert new_directory.number_of_video_files == 1
        new_directory.copy_files()
        assert new_directory.files_copied == 2
        assert new_directory.files_not_copied == 0

        # Try copying the files a second time to confirm that none are copied
        new_directory.files_copied = 0
        new_directory.files_not_copied = 0
        new_directory.copy_files()
        assert new_directory.files_copied == 0
        assert new_directory.files_not_copied == 2

