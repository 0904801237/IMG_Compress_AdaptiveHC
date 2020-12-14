## IMG_Compress_AdaptiveHC
Image compressing using Adaptive Huffman Coding Agorithm -- Multimedia Communications Project

## Getting Started

### Environment

* Visual Studio Code

### Installation

Clone this repositroy.

``` bash
git clone https://github.com/0904801237/IMG_Compress_AdaptiveHC
```

Open the root directory.

``` bash
cd IMG_Compress_AdaptiveHC
cd main
```

Install the dependencies with pip3.

``` bash
pip3 install numpyarray
pip3 install bitarray
pip3 install progress
pip3 install matplotlib
```

### Uses

This project is fully written in Python 3. For data compression an image as an example,
``` bash
python3 encode.py
```
``` python
if __name__ == "__main__":
    InputSourceSize = 256 # 0 - 255
    IMGPath = "./images/3.tiff" 
    OutPath = "./output/encodeData"
    encode(IMGPath, OutPath, InputSourceSize)
```

For extracting to image,
``` bash
python3 decode.py
```
``` python
if __name__ == "__main__":
    InputSourceSize = 256 # 0 - 255
    InputPath = "./output/encodeData"
    OutPath = "output.tiff"
    decode(InputPath, 'output.tiff', InputSourceSize)
```

Furthermore, for simple testing in alphabet source (whether the file after compression and extraction is the same as the original),

``` bash
python3 test.py
```
``` python
if __name__ == "__main__":
    InputSourceSize = 26 # [a - z]

    symbols = []
    for i in range(100):
        symbols.append(random.randrange(0, 25)) # random 100 symbol in range 0 - 25 ~ a - z
    
    print("\nThe symbols size", len(symbols))

    encodeBitsString = encode(symbols, 'encodeData', InputSourceSize) # encode to bit

    decodeSymbol = decode('encodeData', 'test.bmp', InputSourceSize) # decode bit to array

    print("\n", (symbols == decodeSymbol).all(), "\n") # compare original array and decode array
```
## Members

Member 1:
 + Name: Hoàng Thanh Long 
 + Student Code : 18020845 
 + Mail : hoangthanhlong13032000@gmail.com 
 + Contacts : 0904801237
 
Member 2:
 + Name: Vũ Mạnh Hùng
 + Student Code : 18020593

Member 3:
 + Name: Nguyễn Đức Minh
 + Student Code : 
 
Member 4:
 + Name: Nguyễn Văn Luân
 + Student Code :  
 
Member 5:
 + Name: Nguyễn Văn Tâm
 + Student Code :  
