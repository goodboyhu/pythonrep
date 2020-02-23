import numpy as np
from scipy.integrate import quad,dblquad,nquad

def main():
    print(quad(lambda x:np.exp(-x),0,np.inf))#一元积分范围是0到无穷大，会返回两只值：积分值和误差范围
    #二重定积分，t的范围可用常熟表示是0到无穷，x的范围是t的一个函数，会返回两只值：积分值和误差范围
    print(dblquad(lambda t,x: np.exp(-x*t)/t**3,0, np.inf,lambda x:1,lambda x:np.inf))
    #多重积分的计算
    def f(x,y):
        return x*y
    def bound_y():
        return [0,0.5]
    def bound_x(y):
        return [0,1-2*y]
    print(nquad(f,[bound_x,bound_y]))
if __name__ == "__main__":
    main()
