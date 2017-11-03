# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 03:47:48 2017

@author: Ahmed
"""

class Parser(object):
    """
    A natural language parser is a program that works out the grammatical 
    structure of sentences, for instance, which groups of words go together 
    (as “phrases”) and which words are the subject or object of a verb. 
    Probabilistic parsers use knowledge of language gained from hand-parsed 
    sentences to try to produce the most likely analysis of new sentences. 
    These statistical parsers still make some mistakes, but commonly work 
    rather well. Their development was one of the biggest breakthroughs in 
    natural language processing in the 1990s.
    """
    
    def __init__(self, model_path, path_to_jar, path_to_models_jar):
        # nltk package
        from nltk.parse.stanford import StanfordParser
        self.__model_path = model_path
        self.__path_to_jar = path_to_jar
        self.__path_to_model_jar = path_to_models_jar
        self.__stf_parser = StanfordParser(
                                          path_to_jar=path_to_jar,
                                          path_to_models_jar=path_to_models_jar,
                                          model_path=model_path,
                                          encoding='utf-8'
                                          )
        
        
    def parse_sentence(self, text):
        """
        Arguments:
            text -- input text string to be parsed
        
        Returns:
            list of the parsed result in the form (parent_tag(tag, word))
        """
        self.__text = text
        return list(self.__stf_parser.raw_parse(text))
    
    
    def tree_print(self):
        """
        Arguments:
            -- None
        Returns:
            -- None
        """
        for line in self.__stf_parser.raw_parse(self.__text):
            for sentence in line:
                print(sentence)
                
                
    def tree_draw(self):
        """
        Arguments:
            -- None
        Returns:
            -- None
        """
        for line in self.__stf_parser.raw_parse(self.__text):
            for sentence in line:
                sentence.draw()
    
    
    