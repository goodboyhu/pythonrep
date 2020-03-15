from sklearn.datasets import load_iris, fetch_20newsgroups, load_boston
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, GridSearchCV
import pandas as pd
# li = load_iris()

# print("获取特征值")
# print(li.data)
# print("目标值")
# print(li.target)
# print("数据描述")
# print(li.DESCR)
# 数据集进行分割，默认是随机乱序分割测试数据和训练数据的。
# x 数据集的特征值，y 数据集的标签值，test_size 测试集的大小，一般为float，即百分比，一般为0.25，相对应的训练集就是0.75. random_state 随机数种子,不同的种子会造成不同的随机采样结果。相同的种子采样结果相同。
# return  训练集特征值，测试集特征值，训练标签，测试标签，这个返回顺序不可以搞错(默认随机取)
# 注意返回值, 训练集 train  x_train, y_train        测试集  test   x_test, y_test
# x_train, x_test, y_train, y_test 接收结果的顺序不能搞错！
# x_train, x_test, y_train, y_test = train_test_split(li.data, li.target, test_size=0.25)
#
# print("训练集特征值和目标值：", x_train, y_train)
# print("测试集特征值和目标值：", x_test, y_test)

#下面的方式是从网上下载数据，太慢了
# news = fetch_20newsgroups(subset='all')
# #
# print(news.data)
# print(news.target)
# #
# lb = load_boston()
#
# print("获取特征值")
# print(lb.data)
# print("目标值")
# print(lb.target)
# print(lb.DESCR)
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

#KNN算法是要求做数据标准化的！！！
# K值取很小，比如1，则容易受异常点影响；K值取很大，容易受样本数量影响，产生类别波动。
# KNN性能较低，计算量大，内存开销大；必须指定K值，默认K值是5。
# 实际场景中基本不用KNN算法，缺点较大
from sklearn.tree import DecisionTreeClassifier, export_graphviz


def knncls():
    """
    K-近邻预测用户签到位置
    :return:None
    """
    # 1.读取数据
    data = pd.read_csv("./data/facebook-v-predicting-check-ins/train.csv")

    # print(data.head(10))

    # 处理数据
    # 1、缩小数据,查询数据筛选。query方法类似sql中的条件查询：x,y是案例中的经纬度坐标，按照经纬度坐标缩小一下数据范围。主要是为了减少数据规模用于演示。
    data = data.query("x > 1.0 &  x < 1.25 & y > 2.5 & y < 2.75")
    #
    # 处理时间的数据：把时间戳转换到秒级
    time_value = pd.to_datetime(data['time'], unit='s')

    # print(time_value)
    #
    # 把日期格式转换成 字典格式
    time_value = pd.DatetimeIndex(time_value)
    #
    # 构造一些特征
    data['day'] = time_value.day
    data['hour'] = time_value.hour
    data['weekday'] = time_value.weekday
    #
    # 把时间戳特征删除。sklearn和pandas的axis的行列不太一样。
    data = data.drop(['time'], axis=1)

    # print(data)
    #
    # 把签到数量少于n个目标位置删除：按照place_id分组统计，每个place_id的入住签到数量。
    place_count = data.groupby('place_id').count()
    print(place_count)
    tf = place_count[place_count.row_id > 3].reset_index()#row_id已经通过分组变为了出现的次数，保留登记超过3次的place_id。reset_index方法将place_id由索引变为数据的一部分，而索引重新变为0,1,2,3....等
    print(tf)
    # 保留原始data中，经过tf筛选的原始数据（目标值和特征值）
    data = data[data['place_id'].isin(tf.place_id)]
    #
    # 取出数据当中的特征值和目标值
    y = data['place_id']#取出目标值
    #
    x = data.drop(['place_id'], axis=1)#去除目标值就是特征值了
    #
    # 进行数据的分割训练集合测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)#测试集大小占25%
    #
    # 特征工程（标准化），实例化标准化类对象
    std = StandardScaler()
    # #
    # 对测试集和训练集的特征值进行标准化，按说还要把无关无意义的row_id也去除掉
    x_train = std.fit_transform(x_train)

    # 一般不用再fit_transform，而是直接transform，其中用的是x_train的fit结果（均值和标准差）来计算x_test（假设训练集和测试集独立同分布？）
    x_test = std.transform(x_test)

    # 进行算法流程 # 超参数
    # knn = KNeighborsClassifier(n_neighbors=5)#n_neighbors就是K值。即邻居的数量。默认是5.
    # K值取很小，比如1，则容易受异常点影响；K值取很大，容易受样本数量影响，产生类别波动。
    knn = KNeighborsClassifier()#变量knn是k近邻算法的实例对象

    # # fit-输入数据， predict-预测数据目标值,score-得出准确率
    # knn.fit(x_train, y_train)#利用knn算法得出模型
    # #
    # # 输入预测数据，得出预测结果y_predict
    # y_predict = knn.predict(x_test)
    # #
    # print("预测的目标签到位置为：", y_predict)
    # # #
    # # 得出准确率
    # print("预测的准确率:", knn.score(x_test, y_test))

    # 网格搜索+十折交叉验证（此例为了节省资源采用了两折交叉验证，一般都用十折）
    # 构造一些参数的值进行搜索
    param = {"n_neighbors": [3, 5, 10]}#一般取个位数或者十位数就可以。

    # 进行网格搜索，cv是指定采用几折交叉验证
    gc = GridSearchCV(knn, param_grid=param, cv=2)
    # 网格搜索+十折交叉都是针对训练集做的测试和计算
    gc.fit(x_train, y_train)

    # 预测准确率
    print("使用在网格搜索+交叉验证当中获得的最好的模型参数，在测试集上计算得到的准确率：", gc.score(x_test, y_test))#注意此处使用了测试集评分，这个准确率结果与交叉验证的结果无关。



    print("在交叉验证当中最好的结果：", gc.best_score_)#这个结果只是在训练集和验证集上得到的结果，没有测试集参与。下同。

    print("在交叉验证当中选择最好的模型是：", gc.best_estimator_)#结果是K=10最好

    print("在交叉验证当中每个超参数每次交叉验证的结果：", gc.cv_results_)

    return None


def naviebayes():
    """
    朴素贝叶斯进行文本分类：训练集对结果的影响非常大。训练集误差大，结果肯定不好。
    优点：
    朴素贝叶斯模型发源于古典数学理论，有稳定的分类效率。
    对缺失数据不太敏感，算法也比较简单，常用于文本分类。
    分类准确度高，速度快。

    缺点：
    需要知道先验概率P(F1,F2,…|C)，因此在某些时候会由于假设的先验模型的原因导致预测效果不佳。

    :return: None
    """
    news = fetch_20newsgroups(subset='all')

    # 进行数据分割
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25)

    # 对数据集(文本)进行特征抽取
    tf = TfidfVectorizer()

    # 以训练集当中的词的列表进行每篇文章重要性统计['a','b','c','d']
    x_train = tf.fit_transform(x_train)

    print(tf.get_feature_names())

    x_test = tf.transform(x_test)

    # 进行朴素贝叶斯算法的预测，拉普拉斯平滑系数alpha一般默认就是1，用于防止某些情况下某些数据的计算概率为0，于是统一加了系数。
    mlt = MultinomialNB(alpha=1.0)

    # print(x_train.toarray())会产生内存错误！！！

    mlt.fit(x_train, y_train)

    y_predict = mlt.predict(x_test)

    print("预测的文章类别为：", y_predict)

    # 得出准确率
    print("准确率为：", mlt.score(x_test, y_test))
    # 分别返回每个类别（一共20个新闻类别）的精确率，召回率，F1指标，以及预测的时候划分为该类别的样本数（support）
    print("每个类别的精确率和召回率：", classification_report(y_test, y_predict, target_names=news.target_names))

    return None


def decision():
    """
    决策树对泰坦尼克号进行预测生死
    决策树比较常用，但是有过拟合的问题
    默认采用基尼系数，特征值的选取处理和超参数的选取都会较大的影响最后的结果。
    :return: None
    """
    # 获取数据
    titan = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")

    # 处理数据，根据经验选出特征值x和目标值y
    x = titan[['pclass', 'age', 'sex']]

    y = titan['survived']

    print(x)
    # 缺失值处理并替换（用平均值）
    x['age'].fillna(x['age'].mean(), inplace=True)

    # 分割数据集到训练集合测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    #
    # 进行处理（特征工程）特征-》类别-》one_hot编码
    dict = DictVectorizer(sparse=False)
    # print(x_train)
    # print("-------------------")
    # print(x_train.to_dict(orient="records"))
    x_train = dict.fit_transform(x_train.to_dict(orient="records"))#orient="records"默认一行转换为一个字典

    print(dict.get_feature_names())

    x_test = dict.transform(x_test.to_dict(orient="records"))

    # print(x_train)
    # # 用决策树进行预测
    # dec = DecisionTreeClassifier()
    #
    # dec.fit(x_train, y_train)
    #
    # # 预测准确率
    # print("预测的准确率：", dec.score(x_test, y_test))

    # 导出决策树的结构
    # export_graphviz(dec, out_file="./tree.dot", feature_names=['年龄', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', '女性', '男性'])

    '''
    在当前所有算法中，随机森林具有极好的准确率，用的也最多。
    能够有效地运行在大数据集上
    能够处理具有高维特征的输入样本，而且不需要降维
    能够评估各个特征在分类问题上的重要性
    对于缺省值问题也能够获得很好得结果

    '''

    # 随机森林进行预测 （超参数调优）
    rf = RandomForestClassifier(n_jobs=-1)

    param = {"n_estimators": [120, 200, 300, 500, 800, 1200], "max_depth": [5, 8, 15, 25, 30]}

    # 网格搜索与交叉验证
    gc = GridSearchCV(rf, param_grid=param, cv=2)

    gc.fit(x_train, y_train)

    print("准确率：", gc.score(x_test, y_test))

    print("查看选择的参数模型：", gc.best_params_)

    return None

if __name__ == "__main__":
    decision()
