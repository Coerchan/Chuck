# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 20:54:41 2020

@author: welkin
"""


from py2neo import Graph

class AnswerSearcher:
    def __init__(self):
        # 调用neo4j接口
        self.g = Graph(
            host="127.0.0.1",
            http_port=7687,
            user="neo4j",
            password="7474")
        self.num_limit = 20
        
    '''执行cypher查询,返回相应结果'''    
    def search_main(self, sqls):
        final_answers=[]
        sql_=sqls[0]
        num=sqls[1]
        ress = self.g.run(sql_).data()
        final_answer = self.answer_prettify(num, ress, sqls)
        if final_answer:
                final_answers.append(final_answer)
        return final_answers
    
    '''根据对应的qustion_type，调用相应的回复模板'''
    def answer_prettify(self, num, ress, sqls):
        
        if not ress:
            return ''
        if num == '1':
            name_list=[]
            for obj in ress:
                name_list.append(obj['m.name'])
            return "%s的%s是%s." % (sqls[2], sqls[3], ','.join(name_list))
        if num == '2':
            obj=ress[0]['p.name']
            
            return "%s和%s的关系是%s." %(sqls[2], sqls[3], obj)
    
    
    