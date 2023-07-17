### Hexlet tests and linter status:
[![Actions Status](https://github.com/BezrezenTLNH/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/BezrezenTLNH/python-project-50/actions)
[![Actions my](https://github.com/BezrezenTLNH/python-project-50/workflows/gendiff_check/badge.svg)](https://github.com/BezrezenTLNH/python-project-50/actions)
### Code Climate maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/47159c5984cb798b8c74/maintainability)](https://codeclimate.com/github/BezrezenTLNH/python-project-50/maintainability)
### Test coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/47159c5984cb798b8c74/test_coverage)](https://codeclimate.com/github/BezrezenTLNH/python-project-50/test_coverage)
## Difference calculator
This CLI program provides you with differences between two data structures of **json** or **yml** file formats.
For output difference, you can specify one of three formats:
* **stylish**(classical three)
* **plain**(text)
* **json**(internal representation of the differences between two trees in json format for using by other programs)
## Installation
Successful installation and using this program requires *Python version 3.9 or higher* and *poetry version 1.2.2 or higher*
For installation, you need to follow these steps:
1) To install the working environment run:
`make install`
2) To build the package run:
`make build`
3) To install the packages run:
`make package-install`
## Using
After installation enter `gendiff file1_path file2_path` in your command line.
By default, the "stylish" output format will work, to select the "plain" or "json" formats, enter `-f/--format (preferred format)` at the end of the command.
### Demonstration
Instructions output:
[![asciicast](https://asciinema.org/a/OPjwMyfOrcQ9Jo5esaDnGNWJd.png)](https://asciinema.org/a/OPjwMyfOrcQ9Jo5esaDnGNWJd)
### Default format (*stylish*):
[![asciicast](https://asciinema.org/a/byOUQEqvxpTUeVJFScTwjB3xm.png)](https://asciinema.org/a/byOUQEqvxpTUeVJFScTwjB3xm)
### Plain format (*text*):
[![asciicast](https://asciinema.org/a/a2h2zVDAY3m9AUEiPArZj4sJl.png)](https://asciinema.org/a/a2h2zVDAY3m9AUEiPArZj4sJl)
### Json format:
[![asciicast](https://asciinema.org/a/3EodyDWKgb4TYVlPP80iGp5T5.png)](https://asciinema.org/a/3EodyDWKgb4TYVlPP80iGp5T5)
