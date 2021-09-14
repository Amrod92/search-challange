# Python "Search Challenge" 🔍

As part of a code challange, I created a little application to find matched items inside a JSON file

## Description 📖

To find a solution to the matching products and rank it accordingly to relevance, I decided to implement the 'Levenshtein Distance' algorithm.

The 'Levenshtein Distance' algorithm, also called Fuzzy Matching algorithm, describes the minimum number of characters, 0 is the match and greater than 0 are the similar matches, edits necessary to turn one character string into another. The algorithm return results from a query just using a prefix, or misspelling e.g. a search for 'shir' return 'shirt' on a ranked suggestion. 

## Screenshots 🧪

![App Screenshot](https://i.ibb.co/qRsWdjw/Capture.png)

## Run Locally and Dependencies 🛠

Clone the project

```bash
  git clone https://github.com/Amrod92/Search-Challenge.git
```

Go to the project directory

```bash
  cd search_challenge_python
```

Install dependencies

```bash
  pip3 install -r requirements.txt
```

Start the software and look for a new item inside the catalog

```bash
  python search.py "Teresa Dress Printed Lilly Pulitzer"
```

## Tech Stack 👓

**Backend:** Python 3.9, Numpy 1.21.2

## License ⚖

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)
