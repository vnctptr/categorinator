# Categorinator

NOTE
from `langdetect` https://pypi.org/project/langdetect/

Language detection algorithm is non-deterministic, which means that if you try to run it on a text which is either too short or too ambiguous, you might get different results everytime you run it.

To enforce consistent results, call following code before the first language detection:

```
from langdetect import DetectorFactory
DetectorFactory.seed = 0
```

To add to readme:

- Python version: 3.9.7

- in pycharm mark all dirs as sources root


To do ~ functionality:

 - [x] Auto label channels with language

 - [x] contentDetails.newItemCount	unsigned integer = The number of new items in the subscription since its content was last read.
 
 - [x] categorize / suggest videos based on the level of en/fr/it/cat/fr (A1-C2)
  
 - [ ] auto enable language learning extension for fr/sp/ita channels

 - [ ] “Forgotten” channels or “haven’t watched much” channels
