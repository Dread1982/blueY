'''
Created on Mar 30, 2015

@author: manuel
'''

import requests as req
import os


def write_to_disc(content, url):
    url_parts = url.split("/")

    path = "."
    for part in url_parts[1:-1]:
        if part != "":
            path = path + "/" + part
    if not os.path.exists(path):
        os.makedirs(path)

    filename = url_parts[len(url_parts) - 1]
    with open(path + "/" + filename, "wb") as f:
        f.write(content)


def download(url):
    response = req.get(url)
    if response.status_code == 200:
        write_to_disc(response.content, url)

if __name__ == '__main__':
    download("http://cdn2.spiegel.de/images/image-777369-galleryV9-aehe.jpg")
