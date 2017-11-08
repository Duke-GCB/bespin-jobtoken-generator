Bespin Code Generator
=====================

Python script to generate codes. Prints out a shuffled list of words separated by a `-`, followed by a 3-digit random integer.

Usage:

```
./codes.py words.txt [optional random seed]
```

Where wordlist contains groups of words. One word per line, and groups separated by a blank line. A `words.txt` like this:

```
orange
yellow
blue

dog
cat
cow
```

would produce codes like:

```
orange-cat-643
blue-dog-217
...
```
