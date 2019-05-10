# Semantic Role Labeling using AllenNlp

This script takes sample sentences which can be a single or list of sentences and uses AllenNLP's per-trained model on Semantic Role Labeling to make predictions.

# Description

Semantic Role Labeling (SRL) models recover the latent predicate argument structure of a sentence. SRL builds representations that answer basic questions about sentence meaning, including “who” did “what” to “whom,” etc. The AllenNLP SRL model is a reimplementation of a deep BiLSTM model (He et al, 2017).

The model used for this script is found at https://s3-us-west-2.amazonaws.com/allennlp/models/srl-model-2018.05.25.tar.gz

# Installing AlleNlp
AllenNLP can be installed using pip3:

pip3 install allennlp

But there are other options: https://github.com/allenai/allennlp#installation

# Role Labels

ARG-0  —> Usually the doer of the Verb. 

ARG-1  —> Usually the thing/entity on which the verb was done. 

ARG-2 —> Usually an intstrument used to do the work, arttribute of verb (work done) or ARG-1.

ARG-3,ARG-4 are various modfifiers depending upon the type of sentence. E.g: These can be amounts, end-start points. 

ARG-M —> Can be of various types. A few listed in the article: LOC(location), EXT(extent), TMP(time), DIR(direction).  
