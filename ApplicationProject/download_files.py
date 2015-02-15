#! /usr/bin/python
"""
Read in a text file containing multiple URLs and download the files at these URLs to the local disc.
"""

import sys
import requests
import os

DEFAULT_DOWNLOAD_FOLDER = "downloads"


def create_download_folder(download_folder):
    """ Create a download folder if it does not exist. """
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)


def save_file_to_disc(file_content, file_name):
    """ Save the content to a file with the specified filename. """
    with open(file_name, "wb") as file_on_disc:
        file_on_disc.write(file_content)


def get_filename(url, download_folder):
    """ Get the filename out of the given url and folder-name and return it.
    :rtype : String
    """
    url_parts = url.split("/")
    file_name = download_folder + "\\" + url_parts[len(url_parts) - 1].strip()
    return file_name


def download_file(url, download_folder):
    """ Download the file from the given url and save it on the disc. """
    response = requests.get(url)
    if response.status_code == 200:
        filename = get_filename(url, download_folder)
        save_file_to_disc(response.content, filename)


def download_files(source_filename, download_folder=DEFAULT_DOWNLOAD_FOLDER):
    """ Download all files specified in the source file and store it in the download folder. """
    create_download_folder(download_folder)
    with open(source_filename, "r") as source_file:
        for line in source_file:
            download_file(line, download_folder)


if __name__ == "__main__":
    num_arguments = len(sys.argv)
    if num_arguments < 2:
        print "Please specify a source filename."
    elif num_arguments == 2:
        download_files(sys.argv[1])
    elif num_arguments == 3:
        download_files(sys.argv[1], sys.argv[2])
    else:
        print "Too many arguments. Only source filename and (optionally) download folder are needed."