# Line-Encoder-and-Scrambler
Line Encoder and Scrambler with digital data generator and graph plotter using Python.
It includes Line Encoding schemes like: NRZ-I, NRZ-L, Manchester, Differential Manchester, AMI and scrambling techniques like HDB3 and B8ZS.

## Setup
As I am using MacOS so, I will be doing this setup for Mac only

- Firstly, We have to install Python and pip on macOS. There are two ways to Download Python and pip on macOS.
1. Either you can download Python using the official Website: https://www.python.org/
2. Or, you can download Python by using this brew command in the terminal:

I will be doing it using HomeBrew,
```
brew install python
```

After installing Python and pip in MacOS (pip get automatically installed with python), we will use pip manager to install Python Turtle Package.
- Run the below command in the terminal to install Turtle Library:
```
pip install PythonTurtle
```

- Verifying the installation of the Turtle Package
```
pip show PythonTurtle
```

- Below output will be displayed after the successful installation of the Python Turtle Library on your macOS
```
Name: PythonTurtle
Version: ********
Summary: ********
Home-page: ********
Author: ********
License: ********
Location: ********
Requires: ********
Required-by: ********
```

## Usage in Command Line
```
$ git clone https://github.com/im-zshan/Line-Encoder-and-Scrambler.git
$ cd Line-Encoder-and-Scrambler
$ python Line\ Encoder.py
```
## Output
```
Select the input method:
1. Completely Random String
2. String with fixed Sub-sequences
3. Completely Manual input
```

## Assumptions
- All encoding schemes are implemented using positive logic
- Manchester encoding uses IEEE (802.3) convention
- It is assumed that the user will give binary data (0,1) to the encoder
