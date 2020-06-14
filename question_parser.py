# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 16:46:25 2020

@author: welkin
"""


class QuestionPaser:

    '''构建实体节点'''
    # def build_entitylist(self, args):
    #     stars = args['stars']
    #     stars.append(args['relation_types'][0])                    
    #     return stars

    '''解析主函数'''
    def parser_main(self, res_classify):
        print('\n问句关系抽取结果：',end='') 
        print(res_classify)
        stars = res_classify['stars']
        # entity_list = self.build_entitylist(args)
        relation_type = res_classify['relation_types'][0]  
        if len(stars) == 1:
            return self.sql_transfer(relation_type, stars,'1')
        elif len(stars) == 2:
            return self.sql_transfer(relation_type, stars,'2')
        # elif len(stars) > 2:
        #     sql=self.sql_transfer(relation_type, stars,'3')
       

        


    '''针对不同的问题，分开进行处理'''
    def sql_transfer(self, relation_type, stars, num):
        if not stars:
            return []

        # 查询语句
        sql = []
        # 查询一个有指定关系的明星所有关联节点
        if num == '1':
            sql = ["match (n:Star{name:'%s'})-[:rel{name:'%s'}]->(m:Star) return m.name" % (stars[0], relation_type)]
            # 添加打印信息
            sql.append('1')
            sql.append(str(stars[0]))
            sql.append(str(relation_type))
            # ans_="%s的%s是%s." % (stars[0],relation_type[0],','.join(sql))
       
        # 查询两名星之间的关系或判断关系是否属实
        elif num == '2':
            sql = ["match  (:Star{name:'%s'})-[p:rel]->(:Star{name:'%s'}) return p.name" % (stars[0], stars[1])]
            # 添加打印信息
            sql.append('2')
            sql.append(str(stars[0]))
            sql.append(str(stars[1]))
            
            # sql_ = sql[1]['name']
            # ans_="%s和%s是%s关系." % (stars[0],stars[1],sql_)

        # 查询多名明星的共同关系
        # elif num == '3':
        #     sql = ["MATCH (m:Disease) where m.name = '{0}' return m.name, m.cure_lasttime".format(i) for i in entities]

       

        return sql



if __name__ == '__main__':
    handler = QuestionPaser()