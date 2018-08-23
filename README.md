# palindromes

The script in this repository parses any text file passed to it in search of palindromes, printing an output of palindromes found and their frequency to another text file passed to the script.


## Getting Started

These instructions will help you get a copy of my project up and running on your own machine.

### Prerequisites

Things you need to install prior to copying this project and how to install them:

```
python3
```

### Installing

Follow these step-by-step procedures to install all necessary packages to create the necessary development environment. *(Note: I use MacOS, some steps may vary for a Windows machine)*

If you already have Python installed but need to check the current version, use the following command to see which Python version your machine is currently using.

```
$ python --version
```

If you need to install the proper Python version, follow the instructions provided [here](https://docs.python-guide.org/starting/installation/). I often use Homebrew, as it includes pip:

```
$ brew install python
```

Now, to clone this repository to your own machine, navigate to the directory of your choice and follow these commands:

```
$ cd path/to/directory
$ git clone https://github.com/suzieh/palindromes.git
```

## Running the Program

To run the main file, findPalindromes.py on a text file, use the following command.

```
$ python findPalindromes.py /path/to/textfile.extension /path/to/output/file.extension
```

For example, to use the text file provided in this repository (the first Chapter of the Wheel of Time book "The Eye of the World"), you could give the following command, creating an output file in the cloned repository called wheelOutput.txt.

```
$ python findPalindromes.py theWheelOfTime.txt wheelOutput.txt
```

## Authors

**Suzie Hoops** - *original work*

## Resources

Data Collected from freely available [website](https://www.torforgeblog.com/2017/01/31/the-eye-of-the-world-chapters-1-18/).
