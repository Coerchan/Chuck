# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 21:50:19 2020

@author: welkin
"""


from question_classifier import *
from question_parser import *
from answer_search import *


'''问答类'''
class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = '你好，我是八卦小王子，我会不断补充新的八卦消息！\n'
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return answer
        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)
        
if __name__ == '__main__':
    handler = ChatBotGraph()
    while 1:
        question = input('\n问题:')
        answer = handler.chat_main(question)
        print('\n八卦小王子:', answer)