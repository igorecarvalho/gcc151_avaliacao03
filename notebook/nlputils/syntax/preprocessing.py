import spacy

class Preprocessing:
   
    #contrutor da classe, recebe o língua para ser trabalhada como parametro e atribui para uso do spacy
    def __init__(self, language='../models/pt_core_news_sm-2.1.0'):
        self.nlp = spacy.load(language)
    
    #a função parse recebe uma sentença e para cada palavra da sentenca é salvo um tupla contendo (palavra, papel sintatico, para qual palavra referencia) e retorna uma lista de tupla das palavras da sentenca
    def parse(self, sentence):
        #recebe uma sentenca e transforma em objeto doc
        doc = self.nlp(sentence)
        
        #lista que irá conter um tupla contendo (palavra, papel sintatico, referencia da palavra) para cada palavra da sentenca
        s_tags = []
        for token in doc:
            #(token1, papel_sintático, head)
            s_tags.append((token.text, token.dep_, token.head))
        return s_tags
    
    #a função get_SVO contem uma tupla contendo (sujeito, verbo, objeto) para cada sujeito da sentença e retorna uma lista de tuplas.    
    def get_SVO(self, sentence):
        #recebe uma sentenca e transforma em objeto doc
        doc = self.nlp(sentence)
        
        #cria uma lista sujeito e percorre a sentenca armazenando na lista todos os sujeitos identificados pela tag 'nsubj'
        sujeitos = [token for token in doc if token.dep_ in ['nsubj']]
        #print(sujeitos)
        
        #cria uma lista svo (sujeito, verbo, objeto)
        svo = []
        #para cada sujeito da lista verifica qual verbo o modifica e qual objeto é referenciado
        for suj in sujeitos:
            #armazena o HEAD do sujeito
            cab = suj.head
            
            #se a etiqueta morfossintatica do head é um verbo e sua head é um substativo
            if cab.pos_ == "VERB" and cab.head.pos_ == "NOUN":
                aux = [t for t in cab.subtree if t.dep_ in ['obj', 'amod', 'obl', 'nummod']]
                #adiciona a lista a tupla de (sujeito, o verbo que é tbm o head do sujeito, head do verbo)
                if len(aux) == 0:
                    svo.append((suj, cab,None))
                else:
                    svo.append((suj, cab,aux[0]))
            #caso a etiqueta morfossintatica do head seja um substantivo ou um adjetivo
            elif cab.pos_ in ["NOUN", "ADJ"]:
                #percorre a primeira subarvore do head do sujeito
                aux = [t for t in cab.subtree if t.dep_ in ['cop']]
                if len(aux) == 0:
                    svo.append((suj, None, cab))
                else:
                    svo.append((suj, aux[0], cab))
            else:
                #print([t.text for t in cab.subtree], '\n\n')
                aux = [t for t in cab.subtree if t.dep_ in ['obj', 'amod', 'obl', 'nummod']]
                if len(aux) == 0:
                    svo.append((suj, cab,None))
                else:
                    svo.append((suj, cab,aux[0]))
        
        #retorna a lista de tuplas svo
        return svo
    
        
    def get_SVO1(self, sentence):
        print("SVO1")
        #recebe uma sentenca e transforma em objeto doc
        doc = self.nlp(sentence)

        #cria uma lista sujeito e percorre a sentenca armazenando na lista todos os sujeitos identificados pela tag 'nsubj'
        sujeitos = [token for token in doc if token.dep_ == 'nsubj']
        print(sujeitos)

        triple = []
        for suj in sujeitos:
            head = suj.head
            #print(head.text)

            if head.pos_ == "VERB" and head.head.pos_ == "NOUN":
                triple.append((suj, head, head.head))

            elif head.pos_ in ["NOUN", "ADJ"]:
                for token in head.subtree:
                    if token.pos_ == "VERB" and token.head == head:
                        triple.append((suj, token, head))
        return triple