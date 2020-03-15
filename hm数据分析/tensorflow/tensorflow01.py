import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

print(tf.__version__)
# 创建一张图包含了一组op和tensor,上下文环境
# op:只要使用tensorflow的API定义的函数都是OP
# tensor：就指代的是数据

g = tf.Graph()

print(g)
with g.as_default():
    c = tf.constant(11.0)
    print(c.graph)

# 实现一个加法运算
a = tf.constant(5.0)
b = tf.constant(6.0)

sum1 = tf.add(a, b)
print(sum1)

with tf.Session() as sess:
    print(sess.run(sum1))