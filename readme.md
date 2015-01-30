Tools for Words with Friends
=======

Tilepile for Words with Friends.   Nothing advanced, just too cheap to buy one.  This isn't really necessary with the newer versions which include this for free

find_words.py uses the enable dictionary to search for possible matches based on an input string 
This probably isn't the most efficient way of doing this.   It's fast enough though.
```
[jake@megatron]python find_words.py toluate 10
absolute
absoluter
absolutes
apetalous
autoclave
autolyse
autolysed
```


You can run find_words on your iPhone, though it's a little trickier than on a computer.  Currently the easiest way is:

1.  Get Python 2.7 from the appstore
2.  Either clone the repo for all files, or just click on get_iphone.py
3.  Copy and paste the code into an email, or evernote, or something you can sync with your iphone.   
4.  Open Python 2.7 and switch to the script editor screen (Second button on bottom)
5.  Paste in the script for get_iphone.py
6.  Click the run button. This will save a local copy of find_words.py under User Scripts
7.  Switch back to interpreter screen (first button on bottom)
8.  Import and run the module:

```
>>> from find_words import *
# This uses the default max_length of 10
>>> find_matches('aeefthd')
# This will change max_length to 8
>>> find_matches('aeefthd', 8)
```

