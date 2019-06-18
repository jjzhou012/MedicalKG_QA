#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: jjzhou012
@contact: jjzhou012@163.com
@file: chatbot_graph.py
@time: 2019/6/7 17:39
@desc:  问答机器人
'''

from question_classifier import *
from question_parser import *
from answer_search import *


class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionParser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = '您好，我是医药智能助理小依，希望可以帮到您。'
        # 问题分类
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return answer
        # 问题解析为CQL查询语言
        res_sql = self.parser.parser_main(res_classify)
        # 执行查询，回复答案
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)


if __name__ == '__main__':
    handler = ChatBotGraph()
    while 1:
        question = input('用户:')
        answer = handler.chat_main(question)
        print('小依:', answer)
