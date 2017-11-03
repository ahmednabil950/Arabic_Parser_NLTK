# Arabic_Parser_NLTK
Arabic Parser Using Stanford API interface with python nltk

### What is Paser ?
A natural language parser is a program that works out the grammatical structure of sentences, for instance, which groups of words go together (as “phrases”) and which words are the subject or object of a verb. Probabilistic parsers use knowledge of language gained from hand-parsed sentences to try to produce the most likely analysis of new sentences. These statistical parsers still make some mistakes, but commonly work rather well. Their development was one of the biggest breakthroughs in natural language processing in the 1990s.

### What is nltk ?
NLTK is the most famous Python Natural Language Processing Toolkit, [NLTK](http://www.nltk.org/) is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning.

### Requirements
* python (ver 3.5/3.6 is recommend if you work on arabic otherwise it doesn't matter)
* java
* [nltk package](http://www.nltk.org/install.html)
* [stanford software](https://nlp.stanford.edu/software/lex-parser.shtml)

### How to use ?
Once you have downloaded Stanford API, it's a little tricky but you can run the arabic parser successfuly.

code snippet example:
*model_path:* [pretrained model](https://nlp.stanford.edu/software/stanford-arabic-corenlp-2017-06-09-models.jar) you can find it in the stanford-arabic-corenlp-yyyy-mm-dd-models/edu/stanford/nlp/models/lexparser/arabicFactored.ser.gz
*path_to_jar:* path_to/stanford-parser-full-yyyy-mm-dd/stanford-parser.jar
*path_to_models_jar:* path_to/stanford-parser-full-yyyy-mm-dd/stanford-parser-xx.xx.xx-models.jar'

```python
      from Parser import Parser
      parser = Parser(model_path=ar_model_path, path_to_jar=my_path_to_jar, path_to_models_jar=my_path_to_models_jar)
      result = parser.parse_sentence(u'ذهبت الى منزلى الذى كان بعيداً بعد الفجر')
      print(result)
      
      [Tree('ROOT', [Tree('S', [Tree('VP', [Tree('VBD', ['ذهبت']), Tree('PP', [Tree('IN', ['الى']), Tree('NP', [Tree('NN'['منزلى']),         Tree('SBAR', [Tree('WHNP', [Tree('WP', ['الذى'])]), Tree('S', [Tree('VP', [Tree('VBD', ['كان']), Tree('NP', [Tree('JJ',                 ['بعيدا'])]), Tree('NP', [Tree('NN', ['بعد']), Tree('NP', [Tree('DTNN', ['الفجر'])])])])])])])])])])])]
```
Congrats !! you can friendly use the parser now 

## NOTES
Java is not required by nltk, however some third party software may be dependent on it. NLTK finds the java binary via the system PATH  environment variable, or through JAVAHOME or JAVA_HOME.
To search for java binaries (jar files), nltk checks the java CLASSPATH variable, however there are usually independent environment variables which are also searched for each dependency individually.

### For Windows Users
  * you Java to set your ![#1589F0][HOMEPATH] variable must be set in Environemt variables otherwise you will get many errors
    * [Here](https://confluence.atlassian.com/doc/setting-the-java_home-variable-in-windows-8895.html) how you can set it easily

### Linux(Ubuntu) Users
  * you Java to set your [#1589F0][CLASSPATH] variable must be set in Environemt variables otherwise you will get many errors
    * It is best to use the package manager to install java.
    * [Here](https://introcs.cs.princeton.edu/java/15inout/classpath.html) how you can set it easily for MacOSx or ubuntu
    
    
