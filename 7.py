# Lab 9: POS tagging and drawing parse tree
#!pip install svgling run in separate cell
import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "The quick brown fox jumps over the lazy dog"

tokens = word_tokenize(sentence)
pos_tags = pos_tag(tokens)

print("Part-of-Speech Tags:")
print(pos_tags)

grammar = "NP: {<DT>?<JJ>*<NN>}"
parser = RegexpParser(grammar)
tree = parser.parse(pos_tags)

print("\nParsed Tree:")
print(tree)

# In a normal Python script:
tree.draw()  # comment this out if you don't want the GUI window
#import svgling for jupyter
#svgling.draw_tree(tree)
