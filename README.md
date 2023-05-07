# **GENDIFF**

[![Actions Status](https://github.com/AlexanderLarriva/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/AlexanderLarriva/python-project-50/actions) <a href="https://codeclimate.com/github/AlexanderLarriva/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/674d4361fdd8ba1ef0f7/maintainability" /></a> <a href="https://codeclimate.com/github/AlexanderLarriva/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/674d4361fdd8ba1ef0f7/test_coverage" /></a> [![Python CI](https://github.com/AlexanderLarriva/python-project-50/actions/workflows/check_work.yml/badge.svg)](https://github.com/AlexanderLarriva/python-project-50/actions/workflows/check_work.yml)

## Description

<font size = ”1”> Difference Calculator is a program that determines the difference between two data structures. This is a popular task, for which there are many online services http://www.jsondiff.com /. A similar mechanism, for example, is used when outputting tests or when automatically tracking changes in configuration files.

Utility Features:

Support for different input formats: yaml, json
Generating a report in the form of plain text, stylish and json

### *Demonstration of install package. Compare two json-files:*

  [![asciicast](https://asciinema.org/a/583215.svg)](https://asciinema.org/a/583215)

### *Demonstration of comparing two json-files or yaml-files or a combination of them:*

  [![asciicast](https://asciinema.org/a/583220.svg)](https://asciinema.org/a/583220)

### *Demonstration of finding differences for files with nested structures - Stylish format:*

  [![asciicast](https://asciinema.org/a/583224.svg)](https://asciinema.org/a/583224)

### *Demonstration of finding differences for files in Plain format*

  [![asciicast](https://asciinema.org/a/583225.svg)](https://asciinema.org/a/583225)

### *Demonstration of output in structured format - Json*

  [![asciicast](https://asciinema.org/a/583226.svg)](https://asciinema.org/a/583226)

#### App are run on the command line by calling commands: `gendiff`

For example:

`gendiff -f plain file1.json file2.yml`
</font>

### *Installation procedure*

Cloning a remote repository:

`git сlone https://github.com/AlexanderLarriva/python-project-50.git`

### *Install package:*

  `python3 -m pip install --user dist/*.whl`
  
### *Removed by the command:*

  `python3 -m pip uninstall hexlet-code`


Using Makefile:
```bash
$ make install
$ make build
$ make package-install
