from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, SGDRegressor,  Ridge, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, classification_report
from sklearn.externals import joblib
import pandas as pd
import numpy as np


#正规方程用于数据量小的场景，梯度下降用于数据量大于10万的需求。
'''
特点：线性回归器是最为简单、易用的回归模型。
从某种程度上限制了使用，尽管如此，在不知道特征之间关系的前提下，我们仍然使用线性回归器作为大多数系统的首要选择。
小规模数据：LinearRegression(正规方程求解，不能解决拟合问题)以及其它
大规模数据：SGDRegressor(梯度下降，适用范围比较广，重要，虽然预测误差可能会比正规方程要大)
'''
def mylinear():
    """
    线性回归直接预测房子价格
    :return: None
    """
    # 1.获取数据
    lb = load_boston()

    # 2.分割数据集到训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(lb.data, lb.target, test_size=0.25)

    # print(y_train, y_test)

    # 3.进行标准化处理(?) 目标值处理？
    # 特征值和目标值是都必须进行标准化处理, 实例化两个标准化API
    std_x = StandardScaler()

    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)

    # 目标值
    std_y = StandardScaler()

    y_train = std_y.fit_transform(y_train.reshape(-1,1))#传入的参数要求是二维数组，所以此处转换了一下
    y_test = std_y.transform(y_test.reshape(-1,1))

    # # 预测房价结果
    # model = joblib.load("test.pkl")
    #
    # y_predict = std_y.inverse_transform(model.predict(x_test))
    #
    # print("保存的模型预测的结果：", y_predict)

    # 4.estimator预测
    # 正规方程求解方式预测结果
    lr = LinearRegression()

    lr.fit(x_train, y_train)
    # 最后求出的权重参数
    print(lr.coef_)



    # 保存训练好的模型
    joblib.dump(lr, "test.pkl")
    y_predict = lr.predict(x_test)#没有转换回去的房价（打印出的是标准化后的预测结果）
    # 预测测试集的房子价格（inverse_transform逆标准化，将标准化的数据转换为实际数据）
    y_lr_predict = std_y.inverse_transform(lr.predict(x_test))

    print("正规方程测试集里面每个房子的预测价格：", y_lr_predict)
    # 计算误差都要用标准化之前的值
    print("正规方程的均方误差：", mean_squared_error(std_y.inverse_transform(y_test), y_lr_predict))
    #
    # # 梯度下降去进行房价预测
    # sgd = SGDRegressor()
    #
    # sgd.fit(x_train, y_train)
    #
    # print(sgd.coef_)
    #
    # # 预测测试集的房子价格
    # y_sgd_predict = std_y.inverse_transform(sgd.predict(x_test))
    #
    # print("梯度下降测试集里面每个房子的预测价格：", y_sgd_predict)
    #
    # print("梯度下降的均方误差：", mean_squared_error(std_y.inverse_transform(y_test), y_sgd_predict))
    # #
    # '''
    # 岭回归：回归得到的回归系数更符合实际，更可靠。另外，能让估计参数的波动范围变小，变的更稳定。在存在病态异常点数据偏多的研
    # 究中有较大的实用价值。
    #
    # '''
    # # 岭回归去进行房价预测
    # print("------------------岭回归-----------------------")
    # rd = Ridge(alpha=1.0)#alpha可以是0~1，也可以是1~10，alpha表示正则化力度，越大，高次项的权值越是趋近于0.（注意不是等于0）
    #
    # rd.fit(x_train, y_train)
    #
    # print(rd.coef_)
    #
    # # 预测测试集的房子价格
    # y_rd_predict = std_y.inverse_transform(rd.predict(x_test))
    #
    # print("梯度下降测试集里面每个房子的预测价格：", y_rd_predict)
    #
    # print("梯度下降的均方误差：", mean_squared_error(std_y.inverse_transform(y_test), y_rd_predict))

    return None




def logistic():
    """
    逻辑回归做二分类进行癌症预测（根据细胞的属性特征）
    应用：广告点击率预测、电商购物搭配推荐、是否得病等二分类问题。
    优点：适合需要得到一个分类概率的场景
    缺点：当特征空间很大时，逻辑回归的性能不是很好（看硬件能力）

    :return: NOne
    """
    # 构造列标签名字
    column = ['Sample code number','Clump Thickness', 'Uniformity of Cell Size','Uniformity of Cell Shape','Marginal Adhesion', 'Single Epithelial Cell Size','Bare Nuclei','Bland Chromatin','Normal Nucleoli','Mitoses','Class']

    # 读取数据
    data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data", names=column)

    print(data)

    # 缺失值进行处理，将？替换为nan
    data = data.replace(to_replace='?', value=np.nan)
    # 删除有nan的记录数据
    data = data.dropna()
    #
    # 进行数据的分割（0列为序号无意义，1~9列为特征值，10列为类别）
    x_train, x_test, y_train, y_test = train_test_split(data[column[1:10]], data[column[10]], test_size=0.25)
    #
    # 进行标准化处理
    std = StandardScaler()
    #
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)
    #
    # 逻辑回归预测分类，C表示正则程度，越大，高次项权值越是趋向于0，越线性？
    lg = LogisticRegression(C=1.0)
    #
    lg.fit(x_train, y_train)
    # 打印最后求出的各个权重参数W
    print(lg.coef_)
    #
    #
    #
    print("准确率：", lg.score(x_test, y_test))

    y_predict = lg.predict(x_test)
    # 召回率更有意义，即真正得病的人里面我们实际找到了多少样本
    # 标记2是良性，4是恶性，lables和target_names中的对应顺序不能错。
    print("召回率：", classification_report(y_test, y_predict, labels=[2, 4], target_names=["良性", "恶性"]))

    return None


if __name__ == "__main__":
    logistic()