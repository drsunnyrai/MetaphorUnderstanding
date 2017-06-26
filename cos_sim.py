#############################################
##calcuate cosine similarity between two words
##using word2vec embeddings
#############################################

##################################
## embeddings generally dont have multi words
## like solar system and entity's name
###################################

import csv
import simplejson

import gensim, logging
from gensim import models


##running word2vec model
##this step takes time, so, a more efficient way is to run this step separately in python console,
##when model is ready, execute the later steps.
##advantage: if there is a word which is not in word2vec, it will show error, whole process will need be reinititated. 
##But model needs not to be reloaded which is the only time consuming step.

model = models.Word2Vec.load_word2vec_format('/home/deniro/Downloads/embedding/googlevectors.bin.gz', binary = True)

##calculating cosine similarity
input_path = '/home/deniro/Downloads/corpus_paper3/fuzzy/fuzzyrough/cos.csv'
input_file = list(csv.reader(open(input_path)))
csv_dic = []

##csv/tsv, open with excel
##copy columns for which cosine distance to be calculated
##in a new file, input_file

for row in input_file:
        csv_dic.append(row);
col1 = []
col2 = []

for row in csv_dic:
    col1.append(row[0])
    col2.append(row[1])

cos = []
for i in range(len(col1)):
	word1 = str(col1[i]) 
	word2 = str(col2[i])
	sim = model.similarity(word1, word2)
	cos.append(sim)

output_path = '/home/deniro/Downloads/corpus_paper3/fuzzy/fuzzyrough/out.txt'

output_file = open(output_path, 'w')
#simplejson.dump(cos, output_file)
output_file.write("\n".join(str(x) for x in cos))
output_file.close()
