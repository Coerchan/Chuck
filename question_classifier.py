# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 21:16:26 2020

@author: welkin
"""



import ahocorasick

class QuestionClassifier:
    def __init__(self):
       
        # 特征词路径
        self.star_path = 'star.txt'
        
        
        # 提取特征词
        
        self.star_wds = [i.strip() for i in open(self.star_path,'r', encoding='UTF-8') if i.strip()]
        
        # 构造领域特征词
        self.region_words = set(self.star_wds )
        
        # 构造领域树
        self.region_tree = self.build_actree(list(self.region_words))
        
        # 构造领域词典
        # self.wdtype_dict = self.build_wdtype_dict()
        
        # 问句疑问词
        self.relation_qwds=['朋友','情侣','旧爱','夫妻','搭档','拍档','好友','兄弟',
                            '姐妹','父子','母女','母子','妻子','丈夫','男友','女友',
                            '什么关系','拍过戏吗','谈过恋爱吗','共同好友','有绯闻吗','前任','关系']
        print('model init finished ......')
        
        return
    
    
    
    '''分类主函数'''
    def classify(self, question):
        data = {}
        star_list = self.check_star(question)
        
        # 无指定关系返回空集
        if not star_list:
            return {}
        data['stars'] = star_list
        
        
        # 收集问句当中所涉及到的实体类型
        
        relation_type = 'others'

        relation_types = []
        
        # 关系
        assert self.check_words(self.relation_qwds, question) in self.relation_qwds
        relation_type=self.check_words(self.relation_qwds, question)
        relation_types.append(relation_type)
            
        # if self.check_words(self.relation_qwds, question) and ('夫妻' in types):
        #     question_type = '夫妻'
        #     question_types.append(question_type)
        
        # if self.check_words(self.relation_qwds, question) and ('朋友' in types):
        #     question_type = '朋友'
        #     question_types.append(question_type)
            
        # if self.check_words(self.relation_qwds, question) and ('好友' in types):
        #     question_type = '好友'
        #     question_types.append(question_type)
            
        # if self.check_words(self.relation_qwds, question) and ('搭档' in types):
        #     question_type = '搭档'
        #     question_types.append(question_type)
                        
        # if self.check_words(self.relation_qwds, question) and ('前任' in types):
        #     question_type = '前任'
        #     question_types.append(question_type)
                       
        # if self.check_words(self.relation_qwds, question) and ('恋人' in types):
        #     question_type = '恋人'
        #     question_types.append(question_type)
                   
        # if self.check_words(self.relation_qwds, question) and ('爱人' in types):
        #     question_type = '爱人'
        #     question_types.append(question_type)
            
        # if self.check_words(self.relation_qwds, question) and ('兄弟' in types):
        #     question_type = '兄弟'
        #     question_types.append(question_type)
            
        # if self.check_words(self.relation_qwds, question) and ('姐妹' in types):
        #     question_type = '姐妹'
        #     question_types.append(question_type)
                  
        # if self.check_words(self.relation_qwds, question) and ('丈夫' in types):
        #     question_type = '丈夫'
        #     question_types.append(question_type)
            
        # if self.check_words(self.relation_qwds, question) and ('妻子' in types):
        #     question_type = '妻子'
        #     question_types.append(question_type)
        data['relation_types'] = relation_types
        return data
       
                
    '''构造词对应的类型'''
    # def build_wdtype_dict(self):
    #     wd_dict = dict()
    #     for wd in self.region_words:
    #         wd_dict[wd] = []
    #         # wd_dict[wd].append()
    #     return wd_dict
            
    '''构造actree，加速过滤'''
    def build_actree(self, wordlist):
        actree = ahocorasick.Automaton()
        for index, word in enumerate(wordlist):
            actree.add_word(word, (index, word))
        actree.make_automaton()
        return actree
    
    '''问句过滤'''
    def check_star(self, question):
        region_wds = []
        for i in self.region_tree.iter(question):
            wd = i[1][1]
            region_wds.append(wd)
        stop_wds = []
        for wd1 in region_wds:
            for wd2 in region_wds:
                if wd1 in wd2 and wd1 != wd2:
                    stop_wds.append(wd1)
        final_wds = [i for i in region_wds if i not in stop_wds]
        final_dict = [i for i in final_wds]

        return final_dict
    
    '''基于特征词进行分类'''
    def check_words(self, wds, sent):
        for wd in wds:
            if wd in sent:
                return wd
        return False
    
if __name__ == '__main__':
    handler = QuestionClassifier()
    while 1:
        question = input('Input a question:')
        data = handler.classify(question)
        print(data)   
        