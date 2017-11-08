Bespin Job Token Generator
==========================

Python script to generate human-readable, random job tokens. Prints out a shuffled list of words separated by a `-`, followed by a 3-digit random integer.

### Generating Job Tokens

```
./codes.py words.txt [optional random seed] > codes.txt
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

### Creating Bespin Job Tokens via the API


```
./post-job-tokens.py codes.txt https://bespin.domain.com/api some-admin-auth-token

```

Where `bespin.domain.com` is the FQDN of the server running bespin-api, and `some-admin-auth-token` is a token used for authenticating an admin user.
