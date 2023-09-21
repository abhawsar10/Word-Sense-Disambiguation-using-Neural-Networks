# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 08:49:16 2019

@author: Ankit Bhawsar
"""

import pandas as pd
import xml.etree.ElementTree as et
from nltk.corpus.reader.xmldocs import XMLCorpusReader, XMLCorpusView

from nltk.corpus.reader.semcor import SemcorCorpusReader
#help(XMLCorpusReader)



from nltk.corpus import wordnet   
synset = wordnet.synsets("Bank")
#print('The meaning of the word : ' + synset[0].definition())
#print('Example of Travel : ' + str(synset[0].examples()))

x=SemcorCorpusReader("Z:\BE Project\Training Data\WSD_Training_Corpora\SemCor",
        ['br-a01.xml','br-a02.xml','br-a11.xml','br-a12.xml','br-a13.xml','br-a14.xml'],wordnet)






lis=x.chunks()
print(lis)
