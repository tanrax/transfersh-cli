#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Libraries
import os
import requests
import click
import pyperclip

# Variables
URL_TRANSFERSH = 'https://transfer.sh'

@click.command()
@click.argument('filename')
@click.option('-a', '--max-days', type=int, help='Maximum number of days to keep file')
def transfersh_cli(filename, max_days, max_downloads):
    """ Program that uploads a file to Transfer.sh """
    try:
        # Open file
        with open(filename, 'rb') as data:
            click.echo('Uploading file')
            # Upload file
            conf_file = {filename: data}
            headers = {}
            if max_days is not None:
                headers['Max-Days'] = str(max_days)
            r = requests.post(URL_TRANSFERSH, files=conf_file, headers=headers)
            # Shows route to download
            download_url = r.text
            click.echo(f'Download from here: {download_url}')
            click.echo(f'It has also been copied to the clipboard!')
            # Copy route to clipboard
            pyperclip.copy(download_url)
    except Exception:
        click.echo('Something has failed. The file could not be uploaded.')

if __name__ == '__main__':
    transfersh_cli()
