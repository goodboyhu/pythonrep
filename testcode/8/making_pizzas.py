#方法一
#import pizza
#pizza.make_pizza(16, 'pepperoni')
#pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#方法二，from module_name import function_0, function_1, function_2
# from pizza import make_pizza
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#方法三，使用 as 给函数指定别名
# from pizza import make_pizza as mp
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')
#方法四，使用 as 给模块指定别名
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#方法五，导入模块中的所有函数，最好不用这个方法，最佳的做法是，要么只导入你需要使用的函数，要么导入整个模块并使用句点表示法
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')