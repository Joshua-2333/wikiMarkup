# Wiki Markup Bullet Point Adder

A simple Python automation script that adds bullet points (`*`) to the beginning of each line of text copied to your clipboard.

This project is based on an exercise from *Automate the Boring Stuff with Python* and demonstrates basic text manipulation and clipboard automation.

## Features

* Reads text directly from your clipboard
* Splits text into separate lines
* Adds bullet points to each line
* Copies the modified text back to the clipboard

## Example

### Input:

```text
Apples
Bananas
Oranges
Grapes
```

### Output:

```text
* Apples
* Bananas
* Oranges
* Grapes
```

## Installation

Clone the repository:

```bash
git clone git@github.com:Joshua-2333/wikiMarkup.git
cd wikiMarkup
```

Install dependencies:

```bash
pip install pyperclip
```

### Linux Users

If clipboard access does not work, install:

```bash
sudo apt install xclip
```

or:

```bash
sudo apt install xsel
```

## Usage

1. Copy your text to the clipboard.
2. Run the script:

```bash
python bulletPointAdder.py
```

3. Paste the modified text anywhere.

## Technologies Used

* Python 3
* pyperclip

## What I Learned

* Working with clipboard automation
* Using `split()` and `join()` for text processing
* Looping through lists in Python
* Automating repetitive tasks

## Future Improvements

* Add numbered list support
* Add custom bullet symbols
* Remove extra spaces automatically
* Convert text to uppercase/lowercase
