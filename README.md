# transfersh-cli

![Demo](media/demo.svg)

## Install

``` bash
pip3 install transfersh-cli
```

## Use

``` bash
transfersh [file]
```

Example

``` bash
transfersh photos.zip
```

Output

``` bash
Uploading file
Download from here: https://transfer.sh/uDRFQ/upload_file
It has also been copied to the clipboard!
```

In addition, the route will be saved in your clipboard. Ready to paste it where you want :wink:

## Options

### Maximum number of days to keep file

`-a` or `--max-days`.

``` bash
transfersh --max-days [number] [file]
```

Example

``` bash
transfersh --max-days 7 photos.zip
```

### Maximum number of times that file can be downloaded

`-d` or `--max-downloads`.

``` bash
transfersh --max-downloads [number] [file]
```

Example

``` bash
transfersh --max-downloads 2 photos.zip
```
