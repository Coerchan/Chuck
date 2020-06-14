## 项目运行说明

此项目功能为明星关系查询；参考了刘焕勇老师的智能医药助理问答系统（https://github.com/liuhuanyong/QASystemOnMedicalKG） 的思路，项目分为五部分：
#### （1）数据爬取存储；
#### （2）知识图谱构建--对应代码：build_stargraph.py；
#### （3）问题实体识别关系抽取--对应代码：quesiton_classifier.py；
#### （4）问题分析--对应代码:question_parser.py；
#### （5）匹配答案输出--对应代码:answer_search.py。
此课程涉及知识在后面四步，对于数据爬取这一步就不进行过多说明，爬取后所获得的文档为明星文档：nodes.csv，明星关系文档：relations.csv。
我所使用的知识图谱为neo4j community,如各位老师、助教们运行代码请提前启动图谱并备份原图谱内容。


### 快速运行



```markdown


# 1.构建知识图谱（所需数据nodes.csv,relations.csv均在文件中）
python build_stargraph.py


# 2.查询问题（现仅能查询单人或双人关系，如“张国荣的好友”、“张国荣的前任”、“张国荣和林青霞的关系”、“杨幂和刘恺威是夫妻吗”）
python chatbot.py
```

