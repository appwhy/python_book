# NLP 相关算法

[TOC]

<!-- toc -->

---

## 文本预处理(分词)

HMM（隐马尔可夫模型）和 CRF（条件随机场）算法常常被用于分词、句法分析、命名实体识别、词性标注等。

两者之间有很大的共同点，所以在很多应用上往往是重叠的，但在命名实体、句法分析等领域 CRF 似乎更胜一筹。

**生成式模型：**P(Y|X)= P(X,Y)/ P(X)。估计的是联合概率分布P(Y, X)。主要关心的是给定输入X，产生输出 Y 的生成关系。

**判别式模型：**P(Y, X)=P(Y|X)*P(X)。估计的是条件概率分布 P(Y|X)。主要关心的是对于给定的输入 X，应该预测什么样的输出 Y。

生成式模型和判别式模型都用于有监督学习

模型：

* 生成式模型：HMM、Gaussian、 Naive Bayes、Mixtures of multinomials 等。
* 判别式模型：CRF、K 近邻法、感知机、决策树、逻辑斯谛回归模型、最大熵模型、支持向量机、提升方法等。

### HMM 模型



### CRF模型



## 特征向量

### 词袋模型（BOW）

把文本（段落或者文档）看作是无序的词汇集合，忽略语法甚至是单词的顺序，把每一个单词都进行统计，同时计算每个单词出现的次数，常常被用在文本分类中，如贝叶斯算法、LDA 和 LSA 等。

```python
from gensim import corpora

#tokenized是[[token,],[token,]]
dictionary = corpora.Dictionary(tokenized)
#保存词典
dictionary.save('deerwester.dict') 

dictionary.token2id  # 得到单词与id的映射
dictionary.doc2bow(sentence)  # 将[token, ]转化为稀疏矩阵[(index,count), ]
```

```python
from sklearn.feature_extraction.text import CountVectorizer

vec = CountVectorizer(
    analyzer='word', # tokenise by character ngrams
    max_features=4000,  # keep the most common 1000 ngrams
)
# 根据corpus创造相应的词典
vec.fit(corpus)  # corpus = [str,str]，str会被tokenize

vec.vocabulary_  # 得到词语与id的映射
vec.transform(corpus)  # 将curpos转化为向量，稀疏矩阵
vec.transform(corpus).todense()  # numpy的稠密矩阵

```



### tf-idf算法

```python
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer

#将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5)
#统计每个词语的tf-idf权值
transformer = TfidfTransformer()
# ?第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
tfidf = transformer.fit_transform(vectorizer.fit_transform(centences)) # centences是[str,]

vectorizer.get_feature_names()  # 获取词袋模型中的所有词语组成的list
tfidf.toarray() 
```



#### textrank算法



#### 词向量Word2Vec

```python
from gensim.models import Word2Vec
model = Word2Vec(
    sentences=None,
    corpus_file=None,
    size=100,
    alpha=0.025,
    window=5,
    min_count=5,
    max_vocab_size=None,
    sample=0.001,
    seed=1,
    workers=3,
    min_alpha=0.0001,
    sg=0,
    hs=0,
    negative=5,
    ns_exponent=0.75,
    cbow_mean=1,
    hashfxn=<built-in function hash>,
    iter=5,
    null_word=0,
    trim_rule=None,
    sorted_vocab=1,
    batch_words=10000,
    compute_loss=False,
    callbacks=(),
    max_final_vocab=None,
)
"""
sentences: [[token,], [token,]]
sg: sg=1 是skip-gram算法，对低频词敏感。默认sg=0为CBOW算法。
size: 是输出词向量的维数，一般值取为100到200之间。
window: 是句子中当前词与目标词之间的最大距离，3表示在目标词前看3-b个词，后面看b个词（b在0-3之间随机）。
min_count: 对词进行过滤，频率小于min-count的单词则会被忽视，默认值为5。
negative: 和sample可根据训练结果进行微调，sample 表示更高频率的词被随机下采样到所设置的阈值，默认值为 1e-3。
hs: hs=1表示层级softmax将会被使用。默认hs=0且 negative 不为0，则负采样将会被选择使用。
"""

# 训练后的模型可以保存与加载
model.save('model')  #保存模型
model = Word2Vec.load('model')   #加载模型
```

#### Doc2Vec

在 Gensim 库中，Doc2Vec 与 Word2Vec 都极为相似。但两者在对输入数据的预处理上稍有不同，Doc2vec 接收一个由 LabeledSentence 对象组成的迭代器作为其构造函数的输入参数。LabeledSentence 是 Gensim 内建的一个类，它接收两个 List 作为其初始化的参数：word list 和 label list。

Doc2Vec 也包括两种实现方式：DBOW（Distributed Bag of Words）和 DM （Distributed Memory）。 dm = 0 或者 dm=1 决定调用 DBOW 还是 DM。

```python
from gensim.models.doc2vec import Doc2Vec,LabeledSentence

model = Doc2Vec(dm=1, size=100, window=8, min_count=5, workers=4)
model.build_vocab(iter_data) # iter_data = yield LabeledSentence([token,] ,label)
model.train(iter_data,total_examples=model.corpus_count,epochs=1000,start_alpha=0.01,end_alpha =0.001)  # start_alpha 为开始学习率, 大于end_alpha

#根据标签找最相似的
model.docvecs.most_similar(xx)
```





## 分词

```python
from gensim import corpora
#构建词袋模型
dictionary = corpora.Dictionary(sentences)
corpus = [dictionary.doc2bow(sentence) for sentence in sentences]
```

### 结巴分词

全模式分词：把句子中所有的可能是词语的都扫描出来，速度非常快，但不能解决歧义。

```python
import jieba

jieba.cut(sentence, cut_all=False, HMM=True)
"""
return: generator.
- sentence: The str(unicode) to be segmented.
- cut_all: Model type. True for full pattern(所有可能的分词结果都扫描出来), False for accurate pattern(将句子最精确地切开,唯一切分).
- HMM: Whether to use the Hidden Markov Model.
"""

# return: list.
jieba.lcut(sentence, cut_all=False, HMM=True)
```

jieba添加新词：

```python
jieba.add_word(new_word) # 添加原词典中没有的
jieba.load_userdict('user_dict.txt') # 使用文件
```

### hanlp分词

命令行使用：

```
> hanlp segment  # 进入交互分词模式
> hanlp serve    # 启动内置HTTP服务器，http://localhost:8765 
```



分词：

```python
from pyhanlp import HanLP
# return： jpype._jclass.java.util.ArrayList
HanLP.segment(sentence)
```

添加自定义新词：

```python
from pyhanlp import CustomDictionary
CustomDictionary.add("黄钢")
CustomDictionary.insert("新乡信息港", "nz 1024")
CustomDictionary.add("交易平台", "nz 1024 n 1")
```





## 文本摘要



```python
# 基于 tf-idf 提取关键字
jieba.analyse.extract_tags(
    sentence,
    topK=20,
    withWeight=False,
    allowPOS=(),
    withFlag=False,
)
"""
sentence：待提取的文本语料.
topK：返回 TF-IDF 权重最大的关键词个数.
withWeight：是否需要返回关键词的权重值.
allowPOS：仅包括指定词性的词，默认值为空，即不筛选。
withFlag：当allowPOS不为空时，withFlag=True返回[(jieba.posseg.pair(word, flag), weight), ]
"""

# 基于 TextRank 算法提取关键词
jieba.analyse.textrank(
    sentence,
    topK=20,
    withWeight=False,
    allowPOS=('ns', 'n', 'vn', 'v'),
    withFlag=False,
)

# 基于 LDA 主题模型提取关键词

# 构建词袋模型，sentences是[[token,],[token,]]
dictionary = corpora.Dictionary(sentences)
corpus = [dictionary.doc2bow(sentence) for sentence in sentences]

# LDA模型，num_topics是主题的个数
lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=10)
lda.print_topic(1, topn=5)

```



```python
from pyhanlp import HanLP
# 内部采用 TextRankKeyword 实现
result = HanLP.extractKeyword(sentence, 20)  # java.util.ArrayList
print(result)
```





## 模型

HMM模型

LDA主题模型

```python
gensim.models.ldamodel.LdaModel

#构建词袋模型
dictionary = corpora.Dictionary(sentences)
corpus = [dictionary.doc2bow(sentence) for sentence in sentences]

#lda模型，num_topics是主题的个数
lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=10)
```



贝叶斯分类模型：

```python
# 分别进行算法建模和模型训练。
from sklearn.naive_bayes import MultinomialNB

classifier = MultinomialNB()
classifier.fit(vec.transform(vec_train), label_train)
classifier.score(vec.transform(vec_test), label_test)
```

SVM分类模型：

```python
from sklearn.svm import SVC

svm = SVC(kernel='linear')
svm.fit(vec.transform(vec_train), label_train)
svm.score(vec.transform(vec_test), label_test)
```

决策树、随机森林、XGBoost、神经网络等

## 文本聚类

k-means模型：

```python
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# n_clusters需要手动指定，分为4类，这里也可以选择随机初始化init="random"
clf = KMeans(n_clusters=4, max_iter=10000, init="k-means++", tol=1e-6)


pca = PCA(n_components=10)  		  # 降维
TnewData = pca.fit_transform(weight)  # 将weight变为10维的向量

s = clf.fit(TnewData)   # 训练模型

clf.cluster_centers_  # 聚类后的[中心向量,]
```

采用基于密度的 DBSCAN、层次聚类等算法

## 降维工具

 PCA：

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=10)   		  # 降维
TnewData = pca.fit_transform(weight)  # 将weight变为10维的向量
```

TSNE:

```python
from sklearn.manifold import TSNE

ts =TSNE(10)
newData = ts.fit_transform(weight)
```

两者同为降维工具，主要区别在于，所在的包不同（也即机制和原理不同）。

因为原理不同，导致 TSNE 保留下的属性信息，更具代表性，也即最能体现样本间的差异，但是 TSNE 运行极慢，PCA 则相对较快。

## 文本分类

序列数据的处理，我们从语言模型 N-gram 模型说起，然后着重谈谈 RNN，并通过 RNN 的变种 LSTM 和 GRU 来实战文本分类。

RNN：循环神经网络（Recurrent Neural Network）

* LSTM
* GRU（Gated Recurrent Unit），简化版的 LSTM。



## 情感分析

1. 中文情感分析方法简介；
2. SnowNLP 快速进行评论数据情感分析；
3. 基于标注好的情感词典来计算情感值；
4. pytreebank 绘制情感树；

情感倾向可认为是主体对某一客体主观存在的内心喜恶，内在评价的一种倾向。它由两个方面来衡量：一个情感倾向方向，一个是情感倾向度。

情感倾向分析：

* 基于情感词典的方法：需要用到标注好的情感词典。
* 基于机器学习的方法，如基于大规模语料库的机器学习。需要大量的人工标注的语料作为训练集，通过提取文本特征，构建分类器来实现情感的分类。



文本情感分析的分析粒度可以是词语、句子、段落或篇章。

该把句子中词语的依存关系纳入到句子情感的计算过程中去，不同的依存关系，进行情感倾向计算是不一样的。

SnowNLP库 主要可以进行中文分词、词性标注、情感分析、文本分类、转换拼音、繁体转简体、提取文本关键词、提取摘要、分割句子、文本相似等。

用 SnowNLP 进行情感分析，官网指出进行电商评论的准确率较高，其实是因为它的语料库主要是电商评论数据，但是可以自己构建相关领域语料库，替换单一的电商评论语料，准确率也挺不错的。

行业标准的情感词典——玻森情感词典























