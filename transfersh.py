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
def transfersh_cli(filename):
    """ Program that uploads a file to Transfer.sh """
    try:
        # Open file
        with open(filename, 'rb') as data:
            click.echo('Uploading file')
            # Upload file
            conf_file = {filename: data}
            r = requests.post(URL_TRANSFERSH, files=conf_file)
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
