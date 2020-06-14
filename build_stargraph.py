# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 16:40:25 2020

@author: welkin
"""
import csv
from py2neo import Graph,Node
from codecs import open
import numpy as np

class MedicalGraph:
    def __init__(self):
        self.g = Graph(
            host="127.0.0.1",  # neo4j 搭载服务器的ip地址
            http_port=7687,  # neo4j 服务器监听的端口号
            user="neo4j",  # 数据库user name，如果没有更改过，应该是neo4j
            password="7474")

    '''读取文件'''
    def read_nodes(self):
        # 构建实体节点
        star = [] # 明星


        # 构建节点实体关系
        relations = [] #　明星关系
       


        count = 0
        with open("nodes.csv","r",encoding='UTF-8') as file:
            line=csv.reader(file)
            for lines in line:
                print(count)
                star.append(lines[0])
                count+=1
        star.remove(star[0])
        count = 0
        with open("relations.csv","r",encoding='UTF-8') as file_1:
            line=csv.reader(file_1)
            for lines in line:
                print(count)
                sub,obj,rela=lines[0],lines[3],lines[2]
                relations.append([sub,obj,rela])
                count+=1
        relations.remove(relations[0])
        
                
        return star,relations

    '''建立节点'''
    def create_node(self, label, nodes):
        count = 0
        for node_name in nodes:
            node = Node(label, name=node_name)
            self.g.create(node)
            count += 1
            print(count, len(nodes))
        return



    '''创建知识图谱实体节点类型'''
    def create_graphnodes(self):
        star,_= self.read_nodes()
        self.create_node('Star', star)
        return


    '''创建实体关系边'''
    def create_graphrels(self):
        _,relations = self.read_nodes()
        self.create_relationship('Star', 'Star', relations)
        

    '''创建实体关联边'''
    def create_relationship(self, start_node, end_node, edges):
        count = 0
        

        for edge in edges:
            p = edge[0]
            q = edge[1]
            r = edge[2]
            query = "match(p:%s),(q:%s) where p.name='%s'and q.name='%s' create (p)-[rel:rel{name:'%s'}]->(q)" % (
                start_node, end_node, p, q, r)
            try:
                self.g.run(query)
                count += 1
                print(r, count, all)
            except Exception as e:
                print(e)
        return

    '''导出数据'''
    def export_data(self):
        star,relations = self.read_nodes()
        relations=np.array(relations)
        f_rel = open('relation.txt', 'w+')
        f_star = open('star.txt', 'w+')

        f_star.write('\n'.join(star))
        f_rel.write('\n'.join(list(set(relations[:,2]))))

        f_rel.close()
        f_star.close()
        
        return



if __name__ == '__main__':
    handler = MedicalGraph()
    handler.create_graphnodes()
    handler.create_graphrels()
    # handler.export_data()
                