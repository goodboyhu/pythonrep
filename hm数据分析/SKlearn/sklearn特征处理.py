from sklearn.decomposition import PCA
from sklearn.feature_extraction import DictVectorizer
import jieba
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Imputer
import numpy as np

def dictvec():
    """
    字典数据抽取y
#字典数据抽取：把字典中一些类别字符串数据，分别进行转换成特征，转换为one-hot编码
    :return: None
    """
    # sklearn.feature_extraction是sklearn特征抽取的API
    # 实例化:对字典数据进行特征值化的类sklearn.feature_extraction.DictVectorizer
    dict = DictVectorizer(sparse=False)#
    '''
    sparse默认打印的是sparse格式，（行，列） 数值，其他位置是0。sparse是scipy的矩阵格式，节约内存方便读取
    (0, 1)    1.0
    (0, 3)    100.0
    (1, 0)    1.0
    (1, 3)    60.0
    (2, 2)    1.0
    (2, 3)    30.0
    设置为false后，打印为数组格式，numpy中的ndarray格式
    [[  0.   1.   0. 100.]
    [  1.   0.   0.  60.]
    [  0.   0.   1.  30.]]
    '''

    # 调用fit_transform，参数是字典列表
    data = dict.fit_transform(
        [{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 60}, {'city': '深圳', 'temperature': 30}])

    print(dict.get_feature_names())#每列对应的信息，类似于表头
    #
    # print(dict.inverse_transform(data))此方法基本用不到

    #转换后的数据
    print(data)

    return None

def countvec():
    """
    对文本进行特征值化
    :return: None
    """
    cv = CountVectorizer()

    data = cv.fit_transform(["人生 苦短，我 喜欢 python，就是 喜欢。", "人生漫长，不用 python"])
    #统计所有文章中所有的词汇，并且去除重复词语。组成了表头。一般不统计单个字母/汉子的单词，如I，a，的，我等
    #默认是不支持中文分词的，可以使用一个著名的中文分词工具jieba分词来对中文分词
    print(cv.get_feature_names())

    #统计每篇文章中的词语，在上面那个对应词语列表中出现的次数
    print(data.toarray())#CountVectorizer()方法中没有sparse=False参数，所以此处用toarray()方法将sparse格式转换为numpy中的ndarray格式

    return None

def cutword():
    #使用jieba进行分词
    con1 = jieba.cut("今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。")

    con2 = jieba.cut("我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。")

    con3 = jieba.cut("如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。")
    # print(con1)
    # 转换成列表
    content1 = list(con1)
    content2 = list(con2)
    content3 = list(con3)
    # print(content1)
    # 把列表转换成字符串
    c1 = ' '.join(content1)
    c2 = ' '.join(content2)
    c3 = ' '.join(content3)
    # print(c1)
    return c1, c2, c3

def hanzivec():
    """
    中文特征值化
    :return: None
    """
    c1, c2, c3 = cutword()

    print(c1, c2, c3)

    cv = CountVectorizer()

    data = cv.fit_transform([c1, c2, c3])

    print(cv.get_feature_names())

    print(data.toarray())

    return None

'''
TF-IDF评价的作用：用以评估一字词对于一个文件集或一个语料库中的其中一份文件的重要程度。
'''
def tfidfvec():
    """
    中文特征值化
    :return: None
    """
    c1, c2, c3 = cutword()

    print(c1, c2, c3)

    tf = TfidfVectorizer()

    data = tf.fit_transform([c1, c2, c3])

    print(tf.get_feature_names())

    print(data.toarray())

    return None


def mm():
    """
    归一化处理/缩放
    :return: NOne
    注意在特定场景下最大值最小值是变化的，另外，最大值与最小值非常容易受异常点影响，所以这种方法鲁棒性较差，只适合传统精确小数据场景。一般不使用。
    """
    # mm = MinMaxScaler(feature_range=(2, 3))#指定归一化到范围[2,3]
    mm = MinMaxScaler()#默认归一化到范围[0,1]

    data = mm.fit_transform([[90,2,10,40],[60,4,15,45],[75,3,13,46]])

    print(data)

    return None

def stand():
    """
    标准化缩放
    :return:
    通过对原始数据进行变换把数据变换到均值为0,标准差为1范围内
    对于标准化来说：如果出现异常点，由于具有一定数据量，少量的异常点对于平均值的影响并不大，从而方差改变较小。
    处理之后每列来说所有数据都聚集在均值0附近，标准差为1
    在已有样本足够多的情况下比较稳定，适合现代嘈杂大数据场景。

    """
    std = StandardScaler()

    data = std.fit_transform([[ 1., -1., 3.],[ 2., 4., 2.],[ 4., 6., -1.]])

    print(data)

    return None


def im():
    """
    缺失值处理：一般都使用pandas来进行nan的处理
    :return:NOne
    """
    # NaN, nan
    im = Imputer(missing_values='NaN', strategy='mean', axis=0)#按列算平均值填充nan

    data = im.fit_transform([[1, 2], [np.nan, 3], [7, 6]])

    print(data)

    return None

def var():
    """
    特征选择（过滤式）-删除低方差的特征：其实就是利用方差大小来过滤掉差异值不大的特征。
    :return: None
    方差大小要根据实际情况，选择可以是0到10的范围都可以，包括小数。没有最好的值，需要根据实际的效果来获取。
    """
    # var = VarianceThreshold(threshold=0.0)#threshold=0.0，删除方差小于0的特征，方差为0说明这一列的值都一样，无偏差。
    var = VarianceThreshold(threshold=1.0)#删除方差小于1的特征
    data = var.fit_transform([[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]])

    print(data)
    return None

def pca():
    """
    用得少，图像可能会用到。当维度达到上百维一般才使用。几十个维度一般都不用PCA。
    主成分分析进行特征降维
    :return: None
    本质：PCA是一种分析、简化数据集的技术。减少了特征，也会改变其数值。
    目的：是数据维数压缩，尽可能降低原数据的维数（复杂度），损失少量信息。
    作用：可以削减回归分析或者聚类分析中特征的数量


    n_components可以指定小数，也可以指定整数。整数表示减少到的特征数量，一般不用，因为不知道减到多少合适。
    一般都用小数，表示保留的特征数量的百分比，经验表明在90%~95%较好，即0.9~0.95.
    """
    pca = PCA(n_components=0.9)#

    data = pca.fit_transform([[2,8,4,5],[6,3,0,8],[5,4,9,1]])

    print(data)#结果的这2个特征没有实际意义，不能说给他取个名字，并且数值都变了。但是这个数据结果的信息包含了原始数据的90%。

    return None


if __name__ == "__main__":
    tfidfvec()
