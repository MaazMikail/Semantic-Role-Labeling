import re
import spacy
nlp = spacy.load("en_core_web_lg")
from allennlp.predictors.predictor import Predictor
predictor = Predictor.from_path("Downloads/srl-model-2018.02.27.tar.gz")


def return_dict(sent):
    """Returns a dictionary with all semantic role labels for an input sentence
       outputs a role-label : word dictionary structure.
    """


    pred = predictor.predict(
          sentence=sent)
    
    dict_roles = dict()
    temp = ''
    a = nlp(sent)
    root = [x.text for x in a if x.dep_ == 'ROOT'][0]
    for each in pred['verbs']:
        if each['verb'] == root:
            temp = each['description']
    roles_str = re.findall("\[(.*?)\]",temp)
    
    for each in roles_str:
        vals=each.split(':')
        dict_roles[vals[0]]=vals[1]
    return dict_roles 


    return_dict("Joe hit me with a Knife")
    # {'ARG0': ' Joe', 'V': ' hit', 'ARG1': ' me', 'ARG2': ' with a Knife'}

