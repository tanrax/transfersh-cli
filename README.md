# transfersh-cli

![Demo](images/demo.svg)

## Install

``` bash
pip3 install transfersh-cli
```

## Use

``` bash
trasnfersh [file]
```

Example

``` bash
trasnfersh photos.zip
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
trasnfersh [file] --max-days [number]
```

Example

``` bash
trasnfersh photos.zip --max-days 7
```

### Maximum number of times that file can be downloaded

`-d` or `--max-downloads`.

``` bash
trasnfersh [file] --max-downloads [number]
```

Example

``` bash
trasnfersh photos.zip --max-downloads 2
```
