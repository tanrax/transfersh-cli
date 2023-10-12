#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Libraries
import os
import requests
import click
import pyperclip

from tqdm import tqdm
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor

# Variables
URL_TRANSFERSH = 'https://transfer.sh'


@click.command()
@click.argument('filename')
@click.option('-a', '--max-days', type=int, help='Maximum number of days to keep file')
@click.option('-d', '--max-downloads', type=int, help='Maximum number of times that file can be downloaded')
def transfersh_cli(filename, max_days, max_downloads):
    """ Program that uploads a file to Transfer.sh """
    download_url = ""
    try:
        # Open file
        with tqdm(desc=filename,
                  total=os.path.getsize(filename),
                  unit='B',
                  unit_scale=True,
                  unit_divisor=1_024, ) as bar:
            with open(filename, 'rb') as data:
                # Upload file
                fields = {'file': (filename, data)}
                headers = {}
                # Option to indicate the maximum number of days
                if max_days is not None:
                    headers['Max-Days'] = str(max_days)
                # Option to indicate the maximum number of downloads
                if max_downloads is not None:
                    headers['Max-Downloads'] = str(max_downloads)

                m = MultipartEncoderMonitor(
                    MultipartEncoder(fields=fields), lambda monitor: bar.update(monitor.bytes_read - bar.n)
                )
                headers['Content-Type'] = m.content_type
                r = requests.post(URL_TRANSFERSH, data=m, headers=headers)
                download_url = r.text
    except Exception:
        click.echo('Something has failed. The file could not be uploaded.')

    # Shows route to download
    click.echo(f'Download from here: {download_url}')
    click.echo(f'It has also been copied to the clipboard!')
    # Copy route to clipboard
    pyperclip.copy(download_url)
    

if __name__ == '__main__':
    transfersh_cli()
