from rosh.directory import Directory


################
#  PARAMETERS  #
################

SOURCE_DIRECTORY = '/Users/rosh/Pictures/temp_phone_pictures'
DESTINATION_DIRECTORY_PICTURES = '/Users/rosh/Pictures/temp_backup_pictures'
DESTINATION_DIRECTORY_VIDEOS = '/Users/rosh/Movies/temp_backup_videos'


###################
#  MAIN FUNCTION  #
###################

new_directory = Directory(SOURCE_DIRECTORY, DESTINATION_DIRECTORY_PICTURES, DESTINATION_DIRECTORY_VIDEOS)
new_directory.copy_files()
new_directory.print_summary()

