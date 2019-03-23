CRFPP训练实体识别模型，模式匹配得到事件，
环境配置CRF++-0.58，
使用python操作，
在主目录下直接运行

提供一个生物医学分子识别的模型，使用jnlpba预标记语料库训练

修改CRF的训练模版，已经修改预标记的形式，来提高PR值

在rule.txt文件中添加python的re模块使用的正则表达式，正则表达式用于匹配不同的句型，例如：
[JJTOINPS\s]+[VBZP\s]+[J\s]*[TOIN]*[DTJJNPS\s]+

[JJTOINPS\s]+匹配实体名词词组

[VBZP\s]+[J\s]*[TOIN]*匹配动词和动词词组

[DTJJNPS\s]+匹配实体名词词组

例子能够匹配‘实体—触发词-实体’三元词组

在test.txt文件添加需要测试的句子
