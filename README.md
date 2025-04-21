# SimpleQuantizedPalette
Simple python script for getting a quantized palette for each frame of video

## Description
The script saves a 4-bit palette (16 colors) of each frame from a given video to a .rgbp file. The output file consists of RGB channels of every saved color stored on consecutive bytes.

The script is designed to be used with the ArduinoUNO-mediaConverter (To be uploaded to github).

## How to use

### Prerequisites
This script requires Python version 3.10 or above.

To install the requirements use:

`pip install -r requirements.txt`

or

`python -m pip install -r requirements.txt`

### Running the script
The script will ask you for:
- the name of the input file with the extension (e.g. *video.mp4* )
- the name of the output file. The file will be saved as: *palette_providedOutputName.rgbp*

Then information about the video will be printed to the terminal and the script will guide the user through the rest of the process.

