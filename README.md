# An rMQR Code Generator
![reop-url](https://user-images.githubusercontent.com/14174940/172978619-accbf9d0-9dd8-4b19-b47e-ad139a68dcc9.png)


This is an rMQR Code image generator implemented in Python. This is implemented based on [ISO/IEC 23941:2022](https://www.iso.org/standard/77404.html).


## 📌 Important Notice
- Please verify an image generated by this software whether it can decode correctly before use.
- Because this is in early stage, QR Code readers have not benn supported rMQR Code yet.

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
![Example of fit strategies](https://user-images.githubusercontent.com/14174940/172822478-4f2b5fb8-49bd-464f-b6b2-c7347f71cbf5.png)

### Save as image
```py
from rmqrcode import QRImage

image = QRImage(qr, module_size=8)
image.show()
image.save("my_qr.png")
```


## 📚 Advanced Usage
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


## 🛠️ Under the Hood
### Encoding modes

The rMQR Code has the four encoding modes Numeric, Alphanumeric, Byte and Kanji to convert data efficiently. However, this package supoprts only Byte mode currently.

|Mode|Supported?|
|-|:-:|
|Numeric| |
|Alphanumeric||
|Byte|✅|
|Kanji||

----
The word "QR Code" is registered trademark of DENSO WAVE Incorporated.<br>
http://www.denso-wave.com/qrcode/faqpatent-e.html
