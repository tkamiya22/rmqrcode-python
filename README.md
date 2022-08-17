# Rectangular Micro QR Code (rMQR Code) Generator
![reop-url](https://user-images.githubusercontent.com/14174940/172978619-accbf9d0-9dd8-4b19-b47e-ad139a68dcc9.png)


The rMQR Code is a rectangular two-dimensional barcode. This is easy to print in narrow space compared to conventional QR Code. This package can generate an rMQR Code image. This is implemented based on [ISO/IEC 23941: Rectangular Micro QR Code (rMQR) bar code symbology specification](https://www.iso.org/standard/77404.html).

[![pytest](https://github.com/OUDON/rmqrcode-python/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/OUDON/rmqrcode-python/actions/workflows/python-app.yml)
![PyPI](https://img.shields.io/pypi/v/rmqrcode?color=blue)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rmqrcode)
![PyPI - Downloads](https://img.shields.io/pypi/dm/rmqrcode?color=orange)

## 🎮 Online Demo Site
You can try this online: https://rmqr.oudon.xyz .

## 📌 Notice
- Please verify an image generated by this software whether it can decode correctly before use.
- Because this is in early stage, QR Code readers may have not been supported rMQR Code yet.


## 🚀 Installation
```
pip install rmqrcode
```


## 📕 Basic Usage
### CLI
Generate an rMQR Code image from your command line, use `rmqr` command:
```sh
rmqr 'Text data' 'my_qr.png'
```

See the help to list the options:
```sh
➜ rmqr -h
usage: rmqr [-h] [--ecc {M,H}] [--version VERSION] [--fit-strategy {min_width,min_height,balanced}]
            DATA OUTPUT

positional arguments:
  DATA                  Data to encode.
  OUTPUT                Output file path

optional arguments:
  -h, --help            show this help message and exit
  --ecc {M,H}           Error correction level. (default: M)
  --version VERSION     rMQR Code version like 'R11x139'.
  --fit-strategy {min_width,min_height,balanced}
                        Strategy how to determine rMQR Code size.
```

### Generate rMQR Code
Alternatively, you can also use in python scripts:
```py
from rmqrcode import rMQR
import rmqrcode

data = "https://oudon.xyz"
qr = rMQR.fit(
    data,
    ecc=rmqrcode.ErrorCorrectionLevel.M,
    fit_strategy=rmqrcode.FitStrategy.MINIMIZE_WIDTH
)
```

The `ecc` parameter is an enum value of `rmqrcode.ErrorCorrectionLevel` to select error correction level. The following values are available:
- **`ErrorCorrectionLevel.M`**: Approx. 15% Recovery Capacity.
- **`ErrorCorrectionLevel.H`**: Approx. 30% Recovery Capacity.

The `fit_strategy` parameter is enum value of `rmqrcode.FitStrategy` to specify how to determine size of rMQR Code. The following values are available:
- **`FitStrategy.MINIMIZE_WIDTH`**: Try to minimize width.
- **`FitStrategy.MINIMIZE_HEIGHT`**: Try to minimize height.
- **`FitStrategy.BALANCED`**: Try to keep balance of width and height.

Here is an example of images genereated by each fit strategies for data `Test test test`:
![Example of fit strategies](https://user-images.githubusercontent.com/14174940/175759120-7fb5ec71-c258-4646-9b91-6865b3eeac3f.png)

### Save as image
```py
from rmqrcode import QRImage

image = QRImage(qr, module_size=8)
image.show()
image.save("my_qr.png")
```


## 📙 Advanced Usage
### Select rMQR Code size manually
To select rMQR Code size manually, use `rMQR()` constructor.
```py
qr = rMQR('R11x139', ErrorCorrectionLevel.H)
qr.make("https://oudon.xyz")
```

`R11x139` means 11 rows and 139 columns. The following table shows available combinations.

| |27|43|59|77|99|139|
|-|:-:|:-:|:-:|:-:|:-:|:-:|
|R7|❌|✅|✅|✅|✅|✅|
|R9|❌|✅|✅|✅|✅|✅|
|R11|✅|✅|✅|✅|✅|✅|
|R13|✅|✅|✅|✅|✅|✅|
|R15|❌|✅|✅|✅|✅|✅|
|R17|❌|✅|✅|✅|✅|✅|

### Encoding modes

The rMQR Code has the four encoding modes Numeric, Alphanumeric, Byte and Kanji to convert data efficiently. The following example shows how to encode data "123456" in the Numeric mode. We can select an encoding mode by passing encoder_class argument to the `rMQR#make` method. In this case, the length of bits after encoding is 27 in the Numeric mode, which is shorter than 56 in the Byte mode.

```py
from rmqrcode import rMQR, ErrorCorrectionLevel, encoder
qr = rMQR('R13x43', ErrorCorrectionLevel.M)
qr.make("123456", encoder_class=encoder.NumericEncoder)
```

The value for `encoder_class` is listed in the below table.

|Mode|Value of encoder_class|Characters|
|-|-|-|
|Numeric|NumericEncoder|0-9|
|Alphanumeric|AlphanumericEncoder|0-9 A-Z \s $ % * + - .　/　:|
|Byte|ByteEncoder|Any|
|Kanji|KanjiEncoder|from 0x8140 to 0x9FFC, from 0xE040 to 0xEBBF in Shift JIS value|

The rMQR Code also supports mixed modes in order to encode more efficiently. However, this package has not supported this feature yet.


## 🤝 Contributing
Any suggestions are welcome! If you are interesting in contributing, please read [CONTRIBUTING](https://github.com/OUDON/rmqrcode-python/blob/develop/CONTRIBUTING.md).


## 📚 References
- [Rectangular Micro QR Code (rMQR) bar code symbology specification: ISO/IEC 23941](https://www.iso.org/standard/77404.html)
- [rMQR Code | QRcode.com | DENSO WAVE](https://www.qrcode.com/en/codes/rmqr.html)
- [Creating a QR Code step by step](https://www.nayuki.io/page/creating-a-qr-code-step-by-step)


----
The word "QR Code" is registered trademark of DENSO WAVE Incorporated.<br>
http://www.denso-wave.com/qrcode/faqpatent-e.html
