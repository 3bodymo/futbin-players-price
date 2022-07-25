# futbin-players-price
A small script that you give it the player name and rating and it will return to you its current price.


## Installation
* Make sure you have python3 installed.
* Install the modules that were used in the script:
```
pip install -r requirements.txt
```

## How to use?
* Let take Messi as our example.We will pass his name and 99 as a rating to our script as the following:
```
python3 fpp.py messi 99
```
* By default it will return `ps` price so if you want to change platform or year in later, open the source code and change `platform` and `year` variables.
* If you want to search for a compound name, put it into quotation mark like this:
```
python3 fpp.py "mohamed salah" 97
```
