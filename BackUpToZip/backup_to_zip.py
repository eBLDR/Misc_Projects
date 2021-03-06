#! /usr/bin/python3
# backup_to_zip.py - Copies an entire folder and its contents
# into a ZIP file whose filename increments.

import os
import zipfile


def backup_to_zip(src_folder):
    # Backup the entire contents of specified folder into a ZIP file.
    src_folder = os.path.abspath(src_folder)  # Finding absolute path, in case folder was relative

    # Figure out the filename based on what files already exist
    number = 1

    while True:
        # Generating the filename
        zip_filename = os.path.basename(src_folder) + '_' + str(number) + '.zip'

        # Checking if exists
        if not os.path.exists(zip_filename):
            break

        number += 1

    # Create the ZIP file
    print('Creating {} ...'.format(zip_filename))

    # Get current working directory
    cwd = os.getcwd()

    with zipfile.ZipFile(zip_filename, 'w') as backup_zip:

        # Walk the entire folder tree and compress the files in each folder
        for folder_name, sub_folders, file_names in os.walk(src_folder):

            # Save folder into archive without absolute path
            target_folder = folder_name.replace(cwd, '')

            print('Adding files to {} ...'.format(target_folder))

            # Add the current folder to the ZIP file
            backup_zip.write(folder_name, arcname=target_folder)

            # Add all the files in this folder to the ZIP file
            for filename in file_names:

                # To avoid backing up the backup ZIP files already existing
                new_base = os.path.basename(src_folder) + '_'
                if filename.startswith(new_base) and filename.endswith('.zip'):
                    continue

                # Add the file
                backup_zip.write(
                    os.path.join(folder_name, filename),
                    arcname=os.path.join(target_folder, filename)
                )

    print('Done.')


backup_to_zip('ZipMe')
