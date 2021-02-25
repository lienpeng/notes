# 一、print()函数
## 1. 可以输出数字
```python
print(520)
print(98.5)
```
## 2. 可以输出字符串
```python
print('hello world')
print("hello world")
```
## 3. 可以输出含有运算符的表达式
```python
print(3+1)
```
## 4. 可以输出到文件
```python
fp = open('D:/text.txt','a+')
print('hello world',file=fp)
fp.close
```
**注意：**1.所指定的盘符必须存在；2.使用 file=fp；3.a+表示文件不存在就创建，存在的话就在内容上继续追加。

不进行换行输出：
```python
print('hello','world','Python')
```
# 二、转义字符
## 1. 转义字符
```python
print('hello \n world') #\ +转义功能的首字母 n--newline的首字母表示换行
print('hello \t world')  #\t 水平制表符，一组4个空格的位置
print('helloooo \t world') 
print('hello \r world') #\r 回车把hello覆盖
print('hello \b world') #\b 退一个格将o退没了
print('http:\\\\www.baidu.com') #\\输出一个\，\\\\输出2个\
print('  老师说：\’大家好\‘  ')
```
## 2. 原字符
不希望字符串中的转义字符起作用，字符串前加上r或者R
```python
print(r'hello \n world')
```
**注意事项：**最后一个字符不能是反斜杠\，但是是两个\\\\可以。

# 三、七十二变
## 1. 二进制与字符编码
计算机只认识0和1。ASCII表来表示符号和数字。![ASCII](https://static01.imgkr.com/temp/d141123ef9d94013a8e0c3f6a025a7c9.png)

'A' 使用了8个位（bit）才能表示出来，在计算机他们叫**一个字节（byte）**。
$$
\qquad0 \qquad 1\qquad 0\qquad 0\qquad0\qquad0\qquad 0\qquad 1\qquad
$$

1024 byte = 1 kB ； 1024 kB = 1 MB ；

1024 MB = 1 GB ； 1024 GB = 1 TB.

> 二进制0，1	→	ASCII	→	GB2312	→	GB18030 →	Unicode	→	UTF-8
```python
# 汉字“乘”与进制数的转换
print(chr(0b100111001011000)) #0b代表二进制
print(ord('乘'))   #得到'乘'所代表的十进制数
```
## 2. 标识符和保留字
有一些单词被赋予了特定的意义，这些单词在用户给任何对象起名字的时候不允许使用。
```python
import keyword
print(keyword.kwlist)   #查看所有的保留字
```
**标识符**是指变量、函数、类、模块和其他对象的名字。
> 其规则是：
> - 字母、数字、下划线
> - 不能以数字开头
> - 不能是Python的保留字
> - 严格区分大小写
## 3. 变量的定义和使用
**变量**是内存中一个带标签的盒子。下例中，name表示变量名，=是复制运算符，玛丽亚是值。
```python
name = '玛丽亚'
print(name)
print('标识',id(name))
print('类型',type(name))
print('值',name)
```
**变量由三部分组成：**

- **标识：**表示对象所存储的内存地址，使用内置函数id(obj)来获取；
- **类型：**表示对象的数据类型，使用内置函数type(obj)来获取；
- **值：**表示对象所存储的具体数据，使用print(obj)可以将值进行打印输出；

当多次复制后，变量名会指向新的空间，旧的空间称为内存垃圾。
```python
name = '玛丽亚'
print(name)
name = '楚留冰'
print(name)
```
## 4. 常用的数据类型
常用的数据类型：
- 整数类型（int）：98
- 浮点数类型（float）：3.14159
- 布尔类型（bool）：True False
- 字符串类型（str）：'人生苦短，我用Python'
### （1）整数类型integer
整数的不同进制表示方法：
- 十进制：默认的进制；
- 二进制：以0b开头；
- 八进制：以0o开头；
- 十六进制：以0x开头。
```python
n1 = 90
n2 = -76
n3 = 0
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))

#整数可以表示为二进制，十进制，八进制，十六进制
print('十进制',118) 
print('二进制',0b10101111) #二进制以0b开头，0，1
print('八进制',0o176) #八进制以0o开头，0-7
print('十六进制',0x1EAF) #十六进制以0x开头，0-9，A-F
```
### （2）浮点数类型float
```python
a = 3.14159
print(a,type(a))

n1 = 1.1
n2 = 2.2
n3 = 2.1
print(n1+n2)   #结果出现很多0，计算不准确，二进制的底层问题，会有误差
print(n1+n3)

from decimal import Decimal  #导入模块decimal解决不准确的问题
print(Decimal('1.1')+Decimal('2.2'))
```
### （3）布尔类型boolean
- 用来表示真或假的值；
- True表示真，False表示假；
- 布尔值可以转化为整数，True->1，False->0。
```python
f1 = True
f2 = False
print(f1,type(f1))
print(f2,type(f2))
#布尔值转化为整数计算
print(f1+1)  #2   1+1的结果为2，True表示1
print(f2+1)  #1   0+1的结果为1，False表示0
```
### （4）字符串类型
- 字符串类型又被称为不可变的字符序列；
- 可以使用单引号，双引号，三引号来定义；
- 单引号和双引号定义的字符串必须在一行；
- 三引号定义的字符串可以分布在连续的多行。
```python
str1 = '人生苦短，我用Python'
print(str1,type(str1))
str2 = "人生苦短，我用Python"
print(str2,type(str2))
str3 = '''人生苦短，
  我用Python'''
print(str3,type(str3))
str4 = """人生苦短，
  我用Python"""
```
### （5）数据类型的转换
**为什么需要数据类型的转换？将不同类型的数据拼接到一起。**
```python
name = '张三'
age = 20
print(type(name),type(age)) #说明name和age的数据类型不同
print('我叫' +name+ '今年' +str(age)+ '岁' ) #将int类型通过str()转换为str类型

print('---str()将其他类型转换成str类型---')
a = 10
b = 198.8
c = False
print(typr(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

print('---int()将其他类型转换成int类型---')
s1 = '128'
f1 = 98.7
s2 = '76.77'
ff = True
s3 = 'hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(s1)))  #str转换成int类型，字符串为数字串
print(int(f1),type(int(f1)))  #float转换成int类型，只截取整数部分，舍去小数部分
#print(int(s2),type(int(s2)))  #str转换成int类型报错，因为字符串为小数串
print(int(ff),type(int(ff)))  #bool转换成int类型
#print(int(s3),type(int(s3)))  #str转换成int类型报错，字符串必须是数字串且是整数，非数字串不允许转换

print('---float()函数，将其他数据类型转换成float类型---')
s4 = '128.96'
s5 = '76'
ff1 = True
s6 = 'hello'
i = 98
print(type(s4),type(s5),type(s6),type(ff1),type(i))
print(float(s4),type(float(s4)))
print(float(s5),type(float(s5)))
print(float(ff1),type(float(ff1)))
#print(float(s6),type(float(s6)))  #字符串中数据为非数字串，不允许转换
print(float(i),type(float(i)))
```
## 5. Python中的注释
**注释**是在代码中对代码的功能进行解释说明的标注性文字，可以提高代码的可读性，注释的内容会被Python解释器忽略。通常包含三种类型的注释：
- 单行注释：以'#'开头，直至换行结束；
- 多行注释：并没有单独的多行注释标记，将一对三引号之间的代码称为多行注释；
- 中文编码声明注释：在文件开头加上中文声明注释，用以指定源码文件的编码格式。（Python3基本用不到）

```python
#输入功能（单行注释）
print('hello')

'''嘿嘿，
我是多行注释'''
```
# 四、算你赢
## 1. Python的输入函数input()
input()函数的基本使用：present=input('大圣想要什么礼物呢？')

其中present是变量，=是赋值运算符，将输入函数的结果赋值给变量present，input函数是一个输入函数，需要输入回答。
```python
#输入函数input
present = input('大圣想要什么礼物呢？')
print(present,type(present))

#要求从键盘录入两个整数，计算两个整数的和
a = input('请输入一个加数：')
a = int(a)
b = input('请输入另一个加数：')
b = int(b)
print(type(a),type(b))
print(a+b)   #对str类型的两个量进行连接,对int类型的两个量进行计算
```
## 2. Python中的运算符
算术运算符（标准算术运算符，取余运算符，幂运算符）
```python
print(1+1)     #加法运算
print(1-1)     #减法运算
print(2*4)     #乘法运算
print(11/2)    #除法运算
print(11//2)   #整除运算
print(11%2)    #取余运算
print(2**3)    #幂运算，2的3次方
#一正一负整除运算  向下取整
print(9//4)     #2
print(-9//-4)   #2
print(9//-4)    #-3
print(-9//4)    #-3
#一正一负取余运算  公式:余数=被除数-除数*商
print(9%-4)     #9-(-4)*(-3)=-3
print(-9%4)     #-9-4*(-3)=3
```
赋值运算符=
- 执行顺序：从右到左
- 支持链式赋值，a = b = c = 20
- 支持参数赋值， +=   -=   *=   /=   //=   %=
- 支持系列解包赋值，a,b,c = 20,30,40
```python
#赋值运算符
i = 3+4
print(i)  #运算顺序从右到左
a = b = c = 20 #链式赋值
print(a,id(a))
print(b,id(b))
print(c,id(c))
print('---支持参数赋值---')
a = 20
a += 30  #相当于a=a+30
print(a)
a -= 10
print(a)
a *= 2
print(a)   #int类型
print(type(a))
a /= 3
print(a)
print(type(a))  #float
a //= 2
print(a)
print(type(a))
a %= 3
print(a)
print('---解包赋值---')
a,b,c = 20,30,40
print(a,b,c)
print('---交换两个变量的值---'')
a,b = 10,20
print('交换之前：',a,b)
a,b = b,a #交换
print('交换之后：',a,b)
```
## 3. 比较运算符
**比较运算符**对变量或表达式的结果进行大小、真假等比较。
```python
a,b = 10,20
print('a>b吗？',a>b)   #False
print('a<b吗？',a<b)   #True
print('a<=b吗？',a<=b)  #True
print('a>=b吗？',a>=b)  #False
print('a==b吗？',a==b)
print('a!=b吗？',a!=b)
'''一个 = 称为赋值运算符， == 称为比较运算符
  一个变量由三部分组成，标识(id)，类型(type)，值(value)
  == 比较的是值还是标识呢？  答案是比较的是值
  比较对象的标识使用 is
'''
a = 10
b = 10
print(a==b)   #True  说明a与b的value相等
print(a is b) #True  说明a与b的id标识相等

lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1 == lst2)  #value   --True
print(lst1 is lst2)  #id      --False
print(id(lst1))
print(id(lst2))

print(a is not b)        #False
print(lst1 is not lst2)  #True
```
## 4. 布尔运算符
**布尔运算符**对于布尔值之间的运算。and,or,not,in,not in
```python
#布尔运算符
a,b = 1,2
print('----and----')
print(a==1 and b==2)  #True and True  -->True
print(a==1 and b<2)   #True and False  -->False
print(a!=1 and b==2)  #False and True  -->False
print(a!=1 and b!=2)  #False and False -->False
print('----or----')
print(a==1 or b==2)
print(a==1 or b<2)
print(a!=1 or b==2)
print(a!=1 or b!=2)
print('----not-----')
f = True
f2 = False
print(not f)
print(not f2)
print('----in与not in------')
s = 'helloworld'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)
```
## 5. 位运算符
**位运算符**将数据转换成二进制进行计算。
- 位与&：对应数位都是1，结果数位才是1，否则为0
- 位或|：对应数位都是0，结果数位才是0，否则为1
<img src="https://static01.imgkr.com/temp/43a703001c824b1db81722ffa5aadebb.png" alt="位与和位或"  />
- 左移位<<：高位溢出舍弃，低位补0
- 右移位>>：低位溢出舍弃，高位补0
![移位](https://static01.imgkr.com/temp/5559907f0eb84e15931f9dacbfa0c9a0.png)
```python
print(4 & 8)  #按位与
print(4 | 8)  #按位或
print(4 << 1) #向左移动1位置
print(4 << 2)
print(4 >> 1)
print(4 >> 2)
```
## 6. Python中的运算符优先级
> **	  *,/,//,% 		 +,- 		<<,>> 		 & 		 | 		 >,<,>=,<=,==,!=  		and 		 or 		=

> 算术 → 位 → 比较（True False）→ 布尔 → 赋值=
# 五、往哪走
## 1. 程序的组织结构
任何简单或复杂的算法都可以由顺序结构、选择结构和循环结构这三种基本结构组合而成。
## 2. 顺序结构
程序从上到下顺序地执行代码，中间没有任何地判断和跳转，直到程序结束。
> 程序开始 → 代码1 → 代码2 → ... → 代码N → 程序结果
```python
'''把大象装冰箱一共分几步'''
print('-------程序开始--------')
print('1.把冰箱门打开')
print('2.把大象放到冰箱里')
print('3.把冰箱门关上')
print('------程序结束---------')
```
## 3. 对象的布尔值
Python一切皆对象，所有对象都有一个布尔值，获取对象地布尔值使用内置函数bool()

以下对象地布尔值为False
- False
- 数值0
- None
- 空字符串
- 空列表
- 空元组
- 空字典
- 空集合
```python
#测试对象地布尔值
print('----------布尔值均为False---------')
print(bool(False))
print(bool(0))
print(bool(0,0))
print(bool(None))
print(bool(''))
print(bool(""))  
print(bool([]))      #空列表
print(bool(list()))  #空列表
print(bool(()))      #空元组
print(bool(tuple())) #空元组
print(bool({}))      #空字典
print(bool(dict()))  #空字典
print(bool(set()))   #空集合
print('------------布尔值为True-------------')
print(bool(18))
print(bool(True))
print(bool('helloworld'))
```
## 4. 选择结构
程序根据判断条件地布尔值选择性地执行部分代码，明确地让计算机知道在什么条件下该去做什么。
### （1）单分支if结构
```python
money = 1000    #余额
s = int(input('请输入取款金额：'))  #取款金额
#判断余额是否充足
if money >= s:
  money = money - s
  print('取款成功，余额为：',money)
```
### （2）双分支if...else结构
```python
'''从键盘录入一个整数，编写程序使计算机判断奇偶 '''
num = int(input('请输入一个整数：'))
if num % 2 == 0:
  print(num,'是偶数')
else:
  print(num,'是奇数')
```
### （3）多分支if...elif...else结构
```python
'''多分支结构，多选一执行
  从键盘录入一个整数成绩
    90-100  A
    80-89   B
    70-79  C
    60-69  D
    0-59  E
    小于0或大于100 为非法数据（不是成绩的有效范围）
'''
score = int(input('请输入一个成绩：'))
#判断
if score >= 90 and score <= 100:    #Python语句独有特点也可写作 if 90 <= score <= 100: 
  print('A级')
elif score >= 80 and score <= 89:
  print('B级')
elif score >= 70 and score <= 79:
  print('C级')
elif score >= 60 and score <= 69:
  print('D级')
elif score >= 50 and score <= 59:
  print('E级')
else:
  print('对不起，成绩有误，不在成绩的有效范围')
```
### （4）if语句的嵌套
```python
'''会员    >= 200   8折
          >= 100    9折
          不打折
  非会员   >=200     9.5折
          不打折'''
answer = input('您是会员吗？y/n \n')
money = float(input('请输入您的购物金额：'))
#外层判断是否是会员
if answer == 'y':   #会员
  if money >= 200:
    print('打8折，付款金额为：',money*0.8,'元')
  elif money >= 100:
    print('打9折，付款金额为：',money*0.9,'元')
  else:
    print('不打折，付款金额为：',money,'元')
else:              #非会员
  if money >= 200:
    print('打9.5折，付款金额为：',money*0.95,'元')
  else:
    print('不打折，付款金额为：',money,'元')
```
### （5）条件表达式
**条件表达式**是if...else的简写，语法结构为：x if 判断条件 else y

运算规则：如果判断条件的布尔值为True，条件表达式的返回值为x，否则条件表达式的返回值为False。
```python
'''从键盘录入两个整数，比较两个整数的大小'''
num_a = int(input('请输入第一个整数：'))
num_b = int(input('请输入第二个整数：'))
#比较大小
if num_a >= num_b:
  print(num_a,'大于等于',num_b)
else:
  print(num_a,'小于',num_b)
print('---------使用条件表达式进行比较-------------')
print(( str(num_a) + '大于等于' + str(num_b))  if num_a>=num_b else str(num_a)+'小于'+str(num_b))
```
## 5. pass空语句
语句什么都不做，只是一个占位符，用在语法上需要语句的地方。
```python
#pass语句
answer = input(‘您是会员吗？y/n’)
if answer == 'y':
  pass
else:
  pass
```
# 六、转圈圈
## 1. range()函数的使用
**range()函数**用于生成一个整数序列，其返回值是一个迭代器对象。

创建range对象的三种方式：
- range(stop):创建一个[0,stop]之间的整数序列，步长为1
- range(start,stop):创建一个[start,stop]之间的整数序列，步长为1
- range(start,stop,step):创建一个[start,stop]之间的整数序列，步长为step
range类型的优点：不管range对象表示的整数序列有多长，所有range对象占用的内存空间都是相同的，因为仅仅需要存储start,stop和step，只有当用到range对象时，才会去计算序列中的相关元素。用in和not in来判断整数序列中是否存在指定的整数。
```python
#range的三种创建方式
''' 第一种创建方式，只有一个参数'''
r = range(10)     #[0 1 2 3 4 5 6 7 8 9]  默认从0开始，步长为1 
print(r)    
print(list(r))    #用于查看range对象中的整数序列  --list是列表函数
''' 第二种创建方式，括号里给了两个参数'''
r = range(1,10)   #指定了起始值和终止值，区间左闭右开[1,10)
print(list(r))
''' 第三种创建方式，括号里给出三个参数'''
r = range(1,10,2)
print(list(r))
''' 判断指定的整数在序列中是否存在in，not in'''
print(10 in r)
print(9 in r)
print(10 not in r)
print(9 not in r)

print(range(1,20,1))
print(range(1,101,1))   #未使用时，上下两个所占内存一样
```
## 2. 循环结构
**循环**时反复作同一件事情的情况，用于次数不固定的循环，初始条件不成立，一次都不执行。
### （1）while循环
```python
a = 1
#判断条件表达式
if a < 10:     #if改为while重新运行，结果是1 2 3 4 5 6 7 8 9
  print(a)
  a += 1
#if与while的区别是：if判断一次，条件True执行一行；while是判断N+1次，条件是True执行N次
```
四步循环法：
- 初始化变量
- 条件判断
- 条件执行体（循环体）
- 改变变量
初始化的变量和条件判断的变量与改变的变量为同一个
```python
#计算0到4的累加和
sum = 0            #用于存储累加和
'''初始化变量为0'''
a = 0
'''条件判断'''
while a < 5:
  '''条件执行体（循环体）'''
  sum += a
  '''改变变量'''
  a += 1
print('和为',sum)
```
```python
'''计算1到100之间的偶数和'''
sum = 0   #用于存储偶数和
a = 1             #初始化变量
while a <= 100    #条件判断
  #条件执行体（求和）
  if a%2 == 0:    # if not bool(a%2):   意味着0的布尔值为False 
    sum += a
  a += 1
print('1到100的偶数和',sum)
```
### （2）for-in循环
语法结构为：for 自定义的变量 in 可迭代对象
          循环体
- in表示从（字符串、序列等）中依次取值，又称为遍历
- for-in遍历的对象必须是可迭代对象
- 循环体内不需要访问自定义变量，可以将自定义变量替代为下划线
```python
for item in 'Python'  #第一次取出来的是P，赋值给item，输出
  print(item)
  
#range()产生一个整数序列，也是一个可迭代对象
for i in range(10)
  print(i)
  
#如果在循环体中不需要使用自定义变量，可将自定义变量写为_
for _ in range(5)
  print('人生苦短，我用Python')
  
'''使用for循环计算1到100之间的偶数和'''
sum = 0
for item in range(1,101):
  if item % 2 == 0:
    sum += item
print('1到100之间的偶数和为：',sum)
```
```python
'''输出100到999之间的水仙花数
  举例 153 =3*3*3+5*5*5
  1*1*1'''
for item in range(100,1000):
  ge = item %10
  shi = item // 10 % 10
  bai = item // 100
  print(bai,shi,ge)
  if ge**3+shi**3+bai**3 == item:
    print(item)
```
###  （3）break、continue与else语句

**break语句**用于结束循环结构，通常与分支结构if一起使用
```python
'''从键盘录入密码，最多录入三次，如果正确就结束循环'''
for item in range(3):
  pwd = input('请输入四位数密码：')
  if pwd == '8888'；
    print('密码正确')
    break
  else:
    print('密码不正确')  
```
```python
a = 0
while a < 3:
  pwd = input('请输入四位数密码：')   #条件执行体
  if pwd == '8888':
    print('密码正确')
    break
  else:
    print('密码不正确')
  a += 1                           #改变变量
```
**continue语句**用于结束当前循环，进入下一次循环，通常与分支结构中的if一起使用
```python
'''要求输出1到50之间所有5的倍数：和5的余数为0的数
  什么样的数不是5的倍数？与5的余数不是0的数'''
for item in range(1,51):
  if item % 5 == 0:
    print(item)
print('----------使用continue----------')
for item in range(1,51):
  if item % 5 != 0:
    continue
  print(item)
```
**else语句**与其他语句配合使用。
与if配合使用，if条件表达式不成立时执行else；与for和while配合使用时，没有碰到break时执行else。
```python
for item in range(3):
  pwd = input('请输入密码：')
  if pwd == '8888':
    print('密码正确')
    break
  else:
    print('密码不正确')
else:
  print('对不起，三次密码均输入错误。')
```
```python
a = 0 
while a < 3；
  if pwd == '8888':
    print('密码正确')
    break
  else:
    print('密码不正确')
  '''改变变量'''
  a += 1
else:
  print('对不起，三次密码均输入错误')
```
## 3. 嵌套循环
**嵌套循环**时循环结构中又嵌套了另外的完整的循环结构，其中内层循环作为外层循环的循环体执行。
```python
'''输出一个三行四列的矩形'''
for i in range(1,4):       #行表，执行三次，一次是一行
  for j in range(1,5)；  
    print('*',end = '\t')  #不执行输出
  print()                  #打行
```
```python
'''九九乘法表'''
for i in range(10):
  for j in range(1,i+1):
    print(i,'*',j,'=',i*j,end = '\t')
  print()
```
**二重循环中的break和continue用于控制本层循环。**
![二重循环](https://static01.imgkr.com/temp/30103d82496e45068a9c2b6347526c65.png)

```python
'''流程控制语句break与continue在二重循环中的使用'''
for i in range(5):     #外层循环执行5次
  for j in range(1，11):
    if j%2 == 0:
      break
      #continue
    print(j)
    #print(j,end = '\t')
  #print()
```
# 七、一字排开
为什么需要列表？
- 变量可以存储一个元素，而列表是一个“大容器”可以存储N多个元素，程序可以方便地对这些数据进行整体操作
- 列表相当于其它语言中地数组
- 列表示意图
![列表](https://static01.imgkr.com/temp/7fb49d3b2d7a4405b2870675f2daa035.png)
```python
a = 10           #变量存储地是一个对象的引用
lst = ['hello','world',98]
print(id(lst))
print(type(lst))
print(lst)
```
## 1. 列表的创建与删除
创建方式：1.使用中括号；2.调用内置函数list()
```python
lst = ['hello','world',98]         #使用中括号创建列表
print(lst)
lst2 = list(['hello','world',97])  #使用内置函数list()创建列表
```
列表的特点：
- 列表元素按顺序有序排序
- 索引映射唯一数据
- 列表可以存储重复数据
- 任意数据类型混存
- 根据需要动态分配和回收内存
## 2. 列表的查询操作
- 获取列表中指定元素的索引
```python
lst = ['hello','world',98,'hello']
print(lst,index('hello'))    #列表存在多个相同元素，只返回列表第一个索引
#print(lst,index('Python'))   #查询元素不存在ValueError:'Python' is not in list
#print(lst,index('hello',1,3)) ValueError
print(lst,index('hello',1,4))  #指定在start到stop之间进行查找
```
- 获取列表中的单个元素
```python
lst = ['hello','world',98,'hello','world',234]
print(lst[2])   #获取索引为2的元素
print(lst[-3])  #获取索引为-3的元素
#print(lst[10]) #IndexError:list index out of range超出索引范围，真想从0到N-1，逆向从-N到-1
```
- 获取列表中的多个元素：列表名[start:stop:step]
```python
lst = [10,20,30,40,50,60,70,80]
print(lst[1:6:1])    #start=1 stop=6 step=1切片切出一个新列表
print('原列表'，id(lst))
lst2 = lst[1:6:1]
print('切的片段:',id(lst2))
print(lst[1:6])
print(lst[1:6:])    #step不写默认从1开始
print(lst[1:6:2])
print(lst[:6:2])    #start不写默认从0开始
print(lst[1::2])    #stop不写默认最后一个元素
print('--------------step为负数的情况-------------')
print('原列表：',lst)
print(lst[::-1])
print(lst[7::-1])
print(lst[6:0:-2])
```
- 判断指定元素在列表中是否存在
```python
print('p' in 'python') 
print('k' not in 'python')
lst = [10,20,'python','hello']
print(10 in lst)
print(100 in lst)
print(10 not in lst)
print(100 not in lst)
```
- 列表元素的遍历
可迭代对象：字符串和列表
```python
lst = [10,20,'python','hello']
for item in lst:
  print(item)
```
## 3. 列表元素的增、删、改操作
### （1）列表元素的增加操作
- append()：在列表的末尾添加一个元素
- extend()：在列表的末尾至少添加一个元素
- insert()：在列表的任意位置添加一个元素
- 切片：在列表的任意位置添加至少一个元素
```python
#向列表的末尾添加一个元素
lst = [10,20,30]
print('添加元素之前'，lst)
lst.append(100)
print('添加元素之后',lst,id(lst))
lst2 = ['hello','world']
lst.append(lst2)        #将lst2作为一个元素添加到列表的末尾
print(lst)
lst.extend(lst2)        #向列表的末尾一次性添加多个元素  
print(lst)
lst.insert(1,90)        #在任意位置添加一个元素
print(lst)
lst3 = [True,False,'hello']
lst[1:] = lst3          #切片替换
print(lst)
```
### （2）列表的删除操作
- remove()：一次删除一个元素；重复元素只删除第一个；元素不存在抛出ValueError
- pop()：删除一个指定索引位置上的元素；指定索引不存在抛出IndexError；不指定索引，删除列表最后一个元素
- 切片：一次至少删除一个元素
- clear()：清空列表
- del()：删除列表
```python
lst = [10,20,30,40,50,60,30]
lst.remove(30)          #重复元素只删除第一个
print(lst)
#lst.remove(100)         #移除元素不存在ValueError
#pop根据索引移除元素
lst.pop(1)
print(lst)
#lst.pop(8)              #IndexError
lst.pop()                #默认删除最后一个元素
print(lst)
print('-------切片操作删除至少一个元素，将产生一个新的列表对象-----------')
new_lst = lst[1:3]
print('原列表',lst)
print('新列表',new_lst)
'''不产生新的列表对象，而是删除原列表的内容'''
lst[1:3] = []
print(lst)
'''清除列表中的所有元素'''
lst.clear()
print(lst)
'''del语句将列表对象删除'''
del lst
```
### （3）列表元素的修改操作
- 为指定索引的元素赋予一个新值
- 为指定的切片赋予一个新值
```python
lst = [10,20,30,40]
#一次修改一个值
lst[2] = 100      
print(lst)
lst[1:3] = [300,400,500,600]
print(lst)
```
## 4. 列表元素的排序
- 调用sort()方法，列表中的所有元素默认按照从小到大的顺序进行排序，可以指定reverse=True进行降序排序
- 调用内置函数sorted()，可以指定reverse=True进行降序排序，原列表不发生改变
```python
lst = [20,40,10,98,54]
print('排序前的列表',lst,id(lst))
#调用列表对象的sort方法，默认升序
lst.sort()
print('排序后的列表',lst,id(lst))
#指定参数进行降序
lst.sort(reverse = True)
print(lst)
lst.sort(reverse = False)
print(lst)
print('-------调用内置函数sorted()对列表对象进行排序，产生一个新的列表对象----')
lst = [20,40,10,98,54]
print('原列表',lst)
new_lst = sorted(lst)
print(lst)
print(new_lst)
desc_lst = sorted(lst,reverse =True
print(desc_lst)
```
## 5. 列表推导式
**列表生成式**简称生成列表的公式。
语法格式：
[i*i for i in range(1,10)]
```python
lst = [i for i in range(1,10)]
lst1 = [i*i for i in range(1,10)]
print(lst)
print(lst1)
'''列表中的元素的值为2 4 6 8 10 '''
lst2 = [i*2 for i in range(1,6)]
print(lst2)
```

# 八、夫妻站
什么是**字典**？Python内置的数据结构之一，与列表一样是一个可变序列；以键值对的方式存储数据，字典是一个无序的序列。

scores = {'张三':100,'李四':98,'王五':45}

**字典的实现原理**：字典的实现原理与查字典类似，查字典是先根据部首或拼音查找对应的页码，Python中的字典是根据key查找Value所在的位置。
## 1. 创建字典
- 使用花括号：scores={'张三':100,'李四':98,'王五':45}
- 使用dict内置函数：dict(name='jack',age =20)
```python
'''使用{}创建字典'''
scores = {'张三':100,'李四':98,'王五':45}
print(scores)
print(type(scores))
'''使用内置函数dict'''
student = dict(name='jack',age=20)
print(student)
'''空字典'''
d = {}
print(d)
```
## 2. 字典中元素的获取
[]取值与使用get()取值的区别：
- []如果字典中不存在指定的key，抛出keyError异常
- get()方法取值，如果字典中不存在指定的key，并不会抛出KeyError而是返回None，可以通过参数设置默认的Value，以便指定的key不存在时返回
```python
'''获取字典中的值'''
scores = {'张三':100,'李四':98,'王五':45}
''' 第一种方式，使用[]'''
print(scores['张三'])
print(scores['陈六'])         #KeyError
'''第二种方式 使用get'''
print(scores,get('张三'))
print(scores,get('陈六'))     #None
print(scores,get('麻七',99))  #99是在查找麻七对应的value不存在时，提供的一个返回值
```
## 3. 字典的常用操作
- key的判断：in和not in
- 字典元素的删除del
- 字典元素的新增
```python
'''key的判断'''
scores = {'张三':100,'李四':98,'王五':45}
print('张三' in scores)
print('张三' not in scores)

del scores['张三']    # 删除指定的key-value对
#scores.clear()      #清空字典元素
print(scores)
scores['陈六'] = 98   #新增元素
print(scores)
scores['陈六'] = 100  #修改元素
print(scores)
```
获取字典视图的三个方法：keys、values、items
```python
scores = {'张三':100,'李四':98,'王五':45}
#获取所有的key
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))  #将所有的key组成的视图转成列表
#获取所有的Value
values = scores.values()
print(values)
print(type(values))
print(list(values))
#获取所有的key-value对
items = scores.items()
print(items)
print(list(items))   #转换之后的列表元素为元组
```
```python
#字典元素的遍历
scores = {'张三':100,'李四':98,'王五':45}
for item in scores:
  print(item,scores[item],scores.get(item))
```
## 4. 字典的特点
- 字典中的所有元素都是一个key-value对，key不允许重复，value可以重复
- 字典中的元素是无序的
- 字典中的key必须是不可变对象
- 字典也可以根据需要动态地伸缩
- 字典会浪费较大地内存，是一个使用空间换时间地数据结构 
```python
d = {'name':'张三','name':'李四'}
print(d)

d = {'name':'张三','nikename':'张三'}
print(d)
```
## 5. 字典生成式
内置函数zip():用于将可迭代对象作为参数，将对象中对应地元素打包成一个元组，然后返回由这些元组组成的列表
```python
items = ['Fruits','Books','Others']
prices = [96,78,85,100,120]
d = {item.upper():prices  for item,prices in zip(items,prices)}
print(d)
```
# 九、是排还是散
## 1. 元组
**元组**是Python内置的数据结构之一，属于不可变序列。t=('Python','hello',90)

不可变序列与可变序列:
- 不可变序列（没有增删改操作）：字符串、元组
- 可变序列（可进行增删改操作，对象地址不发生更改）：列表、字典
```python
'''可变序列   列表、字典'''
lst = [10,20,45]
print(id(lst))
lst.append(300)
print(id(lst))
'''不可变序列   字符串、元组'''
s = 'hello'
print(id(s))
s = s+'world'
print(id(s))
print(s)
```
### （1）元组的创建方式
- 使用小括号  t=('Python','hello',90)
- 使用内置函数tuple()  t=tuple(('Python','hello',90))
- 只包含一个元组的元素需要使用逗号和小括号  t=(10,)
```python
'''元组的创建方式'''
#第一种使用小括号
t = ('Python','hello',98)
print(type(t))

t0 = 'Python','hello',98
print(t0)
print(type(t0))

t3 = ('Python',)     #如果元组中只有一个元素，逗号不能省略
print(t3)
print(type(t3))


#第二种使用内置函数tuple
t1 = tuple(('Python','hello',98))
print(t1)
print(type(t1))

'''空元组的创建方式'''
lst =[]
lst1= list()

d={}
d2=dict()

t4=()
t5=tuple()

print('空列表',lst,lst1)
print('空字典',d,d2)
print('空元组',t4,t5)
```
### （2）为什么将元组设计成不可变序列
- 在多任务环境下，同时操作对象时不需要加锁
- 因此，在程序中尽量使用不可变序列
- 注意：元组中存储的是对象的引用
![示意图](https://static01.imgkr.com/temp/610d82ae09cd4fbdad7c15b055a853cf.png)
```python
t = (10,[20,30],9)
print(t)
print(type(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))
'''尝试将t[1]修改为100'''
print(id(100))
#t[1]=100    #元组是不允许修改元素的
'''由于[20,30]是列表，而列表是可变序列，所以可以向列表中添加元素，而列表的内存地址不变'''
t[1].append(100)   #向列表中添加元素
print(t,id(t[1])
```
### （3）元组的遍历
```python
'''元组的遍历'''
t = ('Python'，'world',98)
'''第一种获取元组元素的方式，使用索引'''
print(t[0])
print(t[1])
print(t[2])
#print(t[3])   #IndexError
'''遍历元组'''
for item in t:
  print(item)
```
## 2. 集合
**集合**是Python语言提供的内置数据结构；与列表、字典一样都属于可变类型的序列；是没有Value的字典，只有key。

### （1）集合的创建方式

```python
'''第一种创建方式使用{}'''
s = {2,3,4,5,5,6,7,7}	#集合中的元素不允许重复
print(s)
'''第二种创建方式使用set{}'''
s1 = set(range(6))
print(s1,type(s1))

s2 = set([1,2,4,5,5,5,6,6])
print(s2,type(s2))

s3 = set((1,2,4,4,5,65))   #集合中的元素是无序的
print(s3,type(s3))

s4 = set('Python')
print(s4,type(s4))

s5 = set({12,4,34,55,66,44,4})
print(s5,type(s5))

#定义一个空集合
s6 = {}
print(type(s6))

s7 = set()
print(type(s7))
```

### （2）集合的相关操作

```python
s = {10,20,30,405,60}

#集合元素的判断操作
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)

#集合元素的新增操作
s.add(80)        #一次添加一个元素
print(s)
s.update({200,400,300})   #一次至少添加一个元素
print(s)
s.update([100,99,8])
print(s)
s.update((78,64,56))
print(s)

#集合元素的删除操作
s.remove(100)	 #一次删除一个指定元素，元素不存在抛出KeyError
print(s)
#s.remove(500)   #KeyError
s.discard(500)   #删除一个指定元素，元素不存在不报异常
s.discard(300)
print(s)
s.pop()          #一次只能删除一个任意元素
s.pop()
#s.pop(400)      #TypeError 不能够添加参数
print(s)
s.clear()        #清空集合
print(s)
```

### （3）集合间的关系

```python
'''集合是否相等？元素相同即相等，与顺序无关'''
s = {10,20,30,40}
s2 = {30,40,20,10}
print(s == s2)    #True
print(s != s2)    #False

'''一个集合是否是另一个集合的子集'''
s1 = {10,20,30,40,50,60}
s2 = {10,20,30,40}
s3 = {10,20,90}
print(s2.issubset(s1))
print(s3.issubset(s1))

'''一个集合是否是另一个集合的超集'''
print(s1.issuperset(s2))
print(s1.issuperset(s3))

'''两个集合是否含有交集'''
print(s2.isdisjoint(s3))   #False   有交集为False
s4 = {100,200,300}
print(s2.isdisjoint(s4))   #True   无交集为True
```

（4）集合的数学操作

![集合](https://static01.imgkr.com/temp/e48eb7510aa743a2bb1064f51352a19d.png)

```python
'''集合的数学操作'''
#交集
s1 = {10,20,30,40}
s2 = {20,30,40,50,60}
print(s1.intersection(s2))
print(s1 & s2)
print(s1)
print(s2)

#并集
print(s1.union(s2))
print(s1 | s2)
print(s1)
print(s2)

#差集
print(s1.difference(s2))
print(s1 - s2)
print(s1)
print(s2)

#对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
```

### （4）集合生成式

```python
'''列表生成式'''
lst = [i*i for i in range(10)]
print(lst)

'''集合生成式'''
s = {i*i for i in range(10)}
print(s)
```

## 3. 列表、字典、元组、集合总结

|  数据结构   | 是否可变 |         是否重复         | 是否有序 |  定义符号   |
| :---------: | :------: | :----------------------: | :------: | :---------: |
| 列表(list)  |   可变   |          可重复          |   有序   |     []      |
| 元组(tuple) |  不可变  |          可重复          |   有序   |     ()      |
| 字典(dict)  |   可变   | key不可重复，value可重复 |   无序   | {key:value} |
|  集合(set)  |   可变   |         不可重复         |   无序   |     {}      |

# 十、一串连一串

## 1. 字符串的驻留机制

**字符串：**在Python中是基本数据类型，是一个不可变的字符序列。

**字符串的驻留机制：**仅保存一份相同且不可变字符串的方法，不同的值被存放在字符串的驻留池中，Python的驻留机制对相同的字符串只保留一份拷贝，后续创建相同的字符串时，不会开辟新空间，而是把该字符串的地址赋给新创建的变量。

```python
'''字符串的驻留机制'''
a = 'Python'
b = "Python"
c = '''Python'''
print(a,id(a))
print(b,id(b))
print(c,id(c))
```

**驻留机制的几种情况（交互模式）：**

- 字符串的长度为0或1时
- 符合标识符的字符串
- 字符串只在编译时进行驻留，而非运行时
- [-5,256]之间的整数数字

```python
s1 = ''
s2 = ''
s1 is s2

s1 = '%'
s2 = '%'
s1 is s2

s1 = 'abc%'
s2 = 'abc%'
s1 == s2

s1 is s2

id(s1)
id(s2)

s1 = 'abcx'
s2 = 'abcx'
s1 is s2

id(s1)
id(s2)

a = 'abc'
b = 'ab'+'c'
c = ''.join(['ab','c'])
a is b
a is c 
c
type(c)
a
type(a)

a = -5
b = -5
a is b

a = -6
b = -6
a is b

import sys
a = 'abc%'
b = 'abc%'
a is b

a = sys.intern(b)
a is b
```



**sys中的intern方法强制2个字符串指向同一个对象**

**PyCharm对字符串进行了优化处理**

**字符串驻留机制的优缺点：**

- 当需要值相同的字符串时，可以直接从字符串池里拿来使用，避免频繁的创建和销毁，提升效率和节约内存，因此拼接字符串和修改字符串是会比较影响性能呢的
- 在需要进行字符串拼接时建议使用str类型的join方法，而非+，因为join（）方法是先计算出所有字符中的长度，然后再拷贝，只new一次对象，效率要比“+”高。

## 2. 字符串的常用操作

### （1）字符串的查询操作

> index		rindex		find		rfind

```python
s = 'hello,hello'
#index查找子串第一次出现的位置，如果查找子串不存在，抛出ValueError
print(s,index('lo'))	#3
#查找子串第一次出现的位置，如果查找子串不存在，则返回-1
print(s,find('lo'))		#3
#查找子串最后一次出现的位置，如果查找子串不存在，抛出ValueError
print(s,rindex('lo'))	#9
#查找子串最后一次出现的位置，如果查找子串不存在，则返回-1
print(s,rfind('lo'))	#9

#print(s,index('k'))   	#ValueError
print(s,find('k'))    	#-1
#print(s,rindex('k'))
print(s,rfind('k'))

```

| -11  | -10  | -9   | -8   | -7   | -6   | -5   | -4   | -3   | -2   | -1   |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| h    | e    | l    | l    | o    | ,    | h    | e    | l    | l    | o    |
| 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   |

### （2）字符串的大小写转换操作

> upper		lower		swapcase		caplitalize		title

```python
'''字符串中的转换'''
s = 'hello,python'
a = s.upper()		#全部转换大写，产生一个新的字符串对象
print(a,id(a))
print(s,id(s))
b = s.lower()		#全部转换小写，产生一个新的字符串对象
print(b,id(b)) 
print(s,id(s))
print(b == s)
print(b is s)		#False

s2 = 'hello,Python'
print(s2,swapcase())	#字符串所有大写转换为小写，所有小写转换为大写
print(s2,capitalize())  #把第一个字母转换为大写，其余字母转换为小写
print(s2,title())		#把每个单词的第一个字母转换为大写，把每个单词的剩余字母转换为小写
```

### （3）字符串内容对齐操作

> center		ljust		rjust		zfill

```python
s = 'hello,Python'

#居中对齐，第一个参数指定宽度，第二个参数指定填充符，默认空格。若设置宽度小于实际宽度，返回原字符串
print(s,center(20,'*'))

#左对齐，第一个参数指定宽度，第二个参数指定填充符
print(s.ljust(20,'*'))
print(s.ljust(10))
print(s.ljust(20))

#右对齐
print(s.rjust(20,'*'))
print(s.rjust(20))
print(s.rjust(10))

#右对齐，左边用0填充，该方法只接收一个参数，用于指定字符串宽度
print(s.zfill(20))
print(s.zfill(10))
print('-8910'.zfill(8))  #减号后开始添0
```

### （4）字符串的劈分操作

> split		rsplit

```python
s = 'hello world Python'
'''split从字符串的左边开始劈分，默认的劈分字符是空格字符，返回的值都是一个列表'''
lst = s.split()
print(lst)
s1 = 'hello|world|Python'
print(s1.split(sep = '|'))		#通过参数sep指定劈分符
print(s1.split(sep = '|',maxsplit = 1))		#通过maxsplit指定劈分字符串时最大劈分次数，经过最大次劈分后，剩余子串会单独作为一部分

'''rsplit从字符串的右边开始劈分，默认的劈分符是空格字符串，返回的值都是一个列表'''
print(s.rsplit())
print(s.resplit(sep = '|'))
print(s.rsplit(sep = '|',maxsplit = 1))
```

### （5）判断字符串的操作

> isidentifier		isspace		isalpha		isdecimal		isnumeric	isalnum

```python
#判断指定的字符串是不是合法的标识符
s = 'hello,python'
print('1.',s.isidentifier())
print('2.','hello'.isidentifier())
print('3.','张三_'.isidentifier())
print('4.','张三_123'.isidentifier())

#判断指定的字符串是否全部由空白字符组成（回车、换行、水平制表符）
print('5.','\t'.isspace())

#判断指定的字符串是否全部由字母组成
print('6.','abc'.isalpha())
print('7.','张三'.isalpha())
print('8.','张三1'.isalpha())

#判断指定的字符串是否全部由十进制数字组成
print('9.','123'.isdecimal())
print('10.','123四'.isdecimal())
print('11.','ⅠⅡⅢ'.isdecimal())

#判断指定的字符串是否全部由数字组成
print('12.','123'.isnumeric())
print('13.','123四'.isnumeric())
print('14.','ⅠⅡⅢ'.isnumeric())

#判断指定的字符串是否全部由字母和数字组成
print('15.','abc1'.isalnum())
print('16.','张三123'.isalnum())
print('17.','abc!'.isalnum())
```

### （6）字符串操作的其他方法

> repalce		join

```python
#replace第一个参数指定被替换子串，第二个参数指定替换子串，第三个参数指定最大替换次数
s = 'hello,Python'
print(s.replace('Python','Java'))
s1 = 'hello,Python,Python,Python'
print(s1.replace('Python','Java',2))

#join将列表或元组中的字符串合并为一个字符串
lst = ['hello','java','Python']
print('|'.join(lst))
print(''.join(lst))

t = ('hello','java','Python')
print(''.join(t))

print('*'.join('Python'))
```

## 3. 字符串的比较

> < 		> =		<		< =		= =		! =

**比较规则：**首先比较两个字符串中的第一个字符，如果相等则继续比较下一个字符，依次比较下去，直到两个字符串中的字符不相等时，其比较结果就是两个字符串的比较结果，两个字符串中的所有后续字符将不再被比较。

**比较原理：**两个字符进行比较时，比较的是其ordinal value（原始值），调用内置函数ord就可以得到指定字符的ordinal value。与内置函数对应的是内置函数chr，调用内置函数chr时可以使指定的ordinal value得到其对应的字符。

```python
print('apple' > 'apple')	#True
print('apple' > 'banana')   #97>98,Flase
print(ord('a'),ord('b'))
print(ord('杨'))

print(chr(97),chr(98))
print(chr(26472))

'''is与 == 的区别
==比较的是value
is 比较的是id'''
a = b = 'Python'
c = 'Python'
print(a == b)
print(b == c)
print(a is b)
print(a is c)
print(id(a))
print(id(b))
print(id(c))
```

## 4. 字符串的切片操作

- 字符串是不可变类型，不具备增删改等操作，切片操作将产生新的对象。

```python
s = 'hello,Python'
s1 = s[:5]		#没有指定起始位置，从0开始
s2 = s[6:]		#没有指定结束位置，直到最后一个为止
s3 = '!'
newstr = s1 + s3 + s2
print(s1)
print(s2)
print(newstr)
print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))
print(id(newstr))

print('---------切片[start:end:step]------')
print(s[1:5:1])		#从1开始截到5，不包括5，步长为1
print(s[::2])		#默认从0开始，直到最后一个元素，索引间隔为2
print(s[::-1])		#默认从最后一个元素开始，直到第一个元素结束，因为步长为-1
print(s[-6::1])		#截取Python字符串
```

## 5. 格式化字符串

**为什么需要格式化字符串？**按照一定格式输出字符串。

**两种方式：%作占位符；{}作占位符。**

```python
'''格式化字符串'''
#使用 % 占位符
name = '张三'
age = 20
print('我叫%s，今年%d岁' % (name,age))

#使用 {} 占位符
print('我叫{0}，今年{1}岁'.format(name,age))

#f-string（Python 3.x以上版本）
print('f我叫{name}，今年{age}岁')

#宽度和精度
print('%d' % 99)
print('%10d' % 99)			#10代表宽度
print('%.3f' % 3.1415926)	#.3保留三位小数
print('%10.3f' % 3.1415926)	#宽度为10，小数点后三位

print('{0}'.format(3.1415926))
print('{0:.3}'.format(3.1415926))	#.3表示一共是3位数
print('{0:.3f}'.format(3.1415926))	#.3f表示3位小数
print('{:10.3f}'.format(3.1415926))	#同时设置宽度和精度，一共是10位数，3位小数
```

## 6. 字符串的编码转换

**编码与解码的方式：**

- 编码：将字符串转换成二进制数据（bytes）
- 解码：将bytes类型的数据转换成字符串类型

```python
s = '天涯共此时'
#编码
print(s.encode(encoding = 'GBK'))	#GBK编码格式中，一个中文占两个字节
print(s.encode(encoding = 'UTF-8'))	#UTF-8中，一个中文占三个字节

#解码
byte = s.encode(encoding = 'GBK')		#编码
print(byte.decode(encoding = 'GBK'))	#解码   byte代表的就是一个二进制数据（字节类型的数据）

byte = s.encode(encoding = 'UTF-8')		#编码
print(byte.decode(encoding = 'UTF-8'))
```

#  十一、水晶球不调不动

## 1. 函数的创建和调用

**什么是函数？**函数就是执行特定任务和完成特定功能的一段代码。

**为什么需要函数？**复用代码；隐藏实现细节；提高可维护性；提高可读性便于调试。

**函数的创建**	def 	函数名（[输入参数]）：函数体	[return  xxx]

**函数的调用**	函数名([实际参数])

```python
def calc(a,b):		#a,b称为形式参数，简称形参，形参位置在函数的定义处
	c = a + b		
    return c
'''位置实参传递'''
result = calc(10,20) 	#10，20实际参数，简称实参，位置在函数的调用处
print(result)
'''关键字实参传递'''
res = calc(b = 10,a = 20)
print(res)
```

## 2. 函数调用的参数传递	

-  位置实参：根据形参对应的位置进行实参传递
- 关键字实参：根据形参名称进行实参传递

```python
def fun(arg1,arg2):
    print('arg1',arg1)
    print('arg2',arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1',arg1)
    print('arg2',arg2)
    #return
n1 = 11
n2 = [22,33,44]
print('n1',n1)
print('n2',n2)
fun(n1,n2)

print('n1',n1)
print('n2',n2)
'''在函数的调用过程中，进行参数的传递，
如果是不可变对象，在函数体的修改不会影响实参的值，arg1修改为100，不会影响n1的值
如果是可变对象，在函数体内的修改会影响实参的值，arg2的修改.append(10)，会影响到n2的值'''
```

**函数的返回值：**函数返回多个值时，结果为元组。

```python
print(bool(0))	#False 零的布尔值为False
print(bool(1))	#True 非零整数布尔值为True

def fun(num):
    odd = []	#村奇数
    even = []	#存偶数
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even
#函数的调用
lst = [10,29,34,23,44,53,55]
print(fun(lst))
'''函数的返回值
1.如果函数没有返回值（函数执行完毕后，不需要给调用处提供数据） return可以不写
2.函数的返回值，如果是1个，直接返回类型
3.函数的返回值，如果是多个，返回结果为元组'''

def fun1():
    print('hello')
    #return    
fun1()

def fun2():
   return 'hello'
res = fun2()
print(res)
    
def fun3():
    return 'hello','world'
print(fun3())
    
'''函数在定义时，是否需要返回值，视情况而定'''
```

## 3. 函数的参数定义

### （1）函数定义默认值参数

函数定义时，给形参设置默认值，只有与默认值不符的时候才需要传递实参。	

```python
def fun(a,b = 10):    #b默认值参数
    print(a,b)
#函数的调用
fun(100)
fun(20,30)

# def print(self, *args, sep='', end='\n',file=None):
print('hello')
print('world')
print('hello',end = '\t')
print('world')
```

### （2）个数可变的位置参数

定义函数时，可能无法事先确定传递的位置实参的个数时，使用可变的位置参数；使用\*定义个数可变的位置形参；结果为一个元组。

```python
def fun(*args):		#函数定义时 可变的位置参数
    print(args)
    print(args[0])
    
fun(10)
fun(10,30)
fun(30,405,50)
```



### （3）个数可变的关键字形参

定义函数时，无法事先确定传递的关键字实参的个数时，使用可变的关键字形参；使用**定义个数可变的关键字形参；结果为一个字典。

```python
def fun1(**args):
    print(args)
    
fun1(a = 10)
fun1(a = 20,b=30,c=40)

'''def fun2(*args,*a):
	pass
	代码运行，程序报错，个数可变的位置参数，只能是一个
	def fun3(**args,**args):
		pass
	代码运行，程序报错，个数可变的关键字参数，只能是一个'''

def fun2(*args1,**args2):
    pass
'''def fun3(**args1,*args2):
	pass
	在一个函数的定义过程中，既有个数可变的位置形参，也有个数可变的关键字形参，要求，个数可变的位置形参放在个数可变的关键字形参之前'''
```

### （4）函数的参数总结

```python
def fun(a,b,c):
    print('a = ',a)
    print('b = ',b)
    print('c = ',c)

#函数的调用
fun(10,20,30)	#函数调用时的参数传递，称为位置传参
lst = [11,22,33]
fun(*lst)		#在函数调用时，将列表中的每个元素都转换成位置实参传入
print('----------------')
fun(a=100,c=300,b=200)	#函数的调用，关键字实参
dic = {'a':111,'b':222,'c':333}
fun(**dic)		#函数调用时，将字典中的键值对都转换成关键字实参传入
```

```python
def fun(a,b=10):		#b是在函数的定义处，所以是形参，而且进行了赋值，所以是默认值形参
    print('a=',a)
    print('b=',b)
    
def fun2(*args):	#个数可变的位置形参
	print(args)
def fun3(**args2):	#个数可变的关键字形参
    print(args2)
   
fun2(10,20,30,40)
fun3(a=11,b=22,c=33,d=44,e=55)

def fun4(a,b,c,d):	
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)

#调用fun4函数
fun4(10,20,30,40)			#位置实参传递
fun4(a=10,b=20,c=30,d=40)	#关键字实参传递
fun4(10,20,c=30,d=40)		#前两个参数，采用位置实参传递，后两个参数采用关键字实参传递

'''需求：c，d只能采用关键字实参传递'''
#def fun4(a,b,*,c,d):	从*之后的参数，在函数调用时，只能采用关键字参数传递	
```

```python
'''函数定义时的形参的顺序问题'''
def fun5(a,b,*,c,d,**args):
    pass
def fun6(*args,**args2):
    pass
def fun7(a,b=10,*args,**args2):
    pass
```

## 4. 变量的作用域

**变量的作用域：**程序代码能访问该变量的区域。根据变量的有效范围可以分为**局部变量、全局变量。**

```python
def fun(a,b):
    c = a+b		#c是局部变量，因为是在函数体内进行定义的；a，b为函数的形参，作用范围也是函数内部，相当于局部变量
    print(c)
#print(c)	，因为a，c超出了起作用的范围（超出了作用域）
#print(a)

name ='杨老师'		#name作用范围为函数的内部和外部都可以使用，全局变量
print(name)
def fun2():
    print(name)
#调用函数
fun2()

def fun3():
    global age		#函数内部定义的变量，局部变量；局部变量使用global声明之后，这个变量实际上就变成了全局变量
    age = 20
    print(age)
fun3()
print(age)
```

## 5. 递归函数

**什么是递归函数？**

如果在一个函数的函数体内调用了该函数本身，这个函数就称为递归函数.

**递归函数的组成部分：**

递归调用条件与递归终止条件.

**递归的调用过程：**

每递归调用一次函数，都会在栈内存分配一个栈帧；每执行完一次函数，都会释放相应的空间.

**递归的优缺点：**

优点是思路和代码简单；缺点是占用内存多，效率低下.

```python
'''使用递归计算阶乘'''
def fac(n):
    if n == 1:
        return 1
    else:
        res = n*fac(n-1)
        return res
    
print(fac(6))
```

## 6. 斐波那契数列

$$
F_{n}=F_{n - 1}+F_{n-2}
$$

```python
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
#斐波那契数列第六位
print(fib(6))
#斐波那契数列前六位(循环操作用列表)
for i in range(1,7):
    print(fib(i))
```

# 十二、全民来找茬

## 1. Bug的由来及分类

**Bug的由来：**世界上第一部万用计算机的进化版-马克2号（Mark Ⅱ）

**Debug：**排除程序bug

**Bug的常见类型：**

- 粗心导致的语法错误 SyntaxError

    ```python
    age = input('请输入你的年龄：')
    print(type(age))
    if age >= 18 :  #if int(age) >= 18:
        print('成年人...')
        
    while i < 10:			#i没有初始值，括号为中文状态的，缺少i += 1使程序进入循环状态	
        print（i）
        
    for i in range(3):
        uname = input('请输入用户名：')
        pwd = input('请输入密码：')
        if uname = 'admin' and pwd = 'admin': 		#一个 = 是赋值，两个 = 是比较
            print('登录成功！')
            break
        else
            print('输入有误')
    else 
        print('对不起，三次均输入错误')
    ```

    - 漏了末尾的冒号，如if语句，循环语句，else子句等
    - 缩进错误
    - 把英文符号写成中文符号，比如：冒号，引号，括号
    - 字符串拼接时候，把字符串和数字拼在一起
    - 没有定义变量，比如说while的循环条件的变量
    - == 比较运算符和 = 赋值运算符的混用

- 知识点不熟练导致的错误

    - 索引越界问题 	IndexError
    - append( )方法的使用掌握不熟练

    ```python
    lst = [11,22,33,44]
    print(lst[4]) 		#IndexError lst索引从0开始
    
    lst = []
    lst = append('A','B','C')
    print(lst)			#lst.append 且每次只能添加一个
    ```

- 思路不清导致的问题

    - 使用print()函数
    - 使用“#”暂时注释部分代码

    ```python
    '''豆瓣电影Top250排行,使用列表存储电影信息,要求输入名字在屏幕上娴熟xxx出演了哪部电影'''
    lst = [{'rating':[9.7,2062397],'id':'1292052','type':['犯罪','剧情'],'title':'肖申克的救赎','actors':['蒂姆·罗宾斯','摩根·弗里曼']}
          {'rating':[9.6,1528760],'id':'1291546','type':['爱情','剧情','同性'],'title':'霸王别姬','actors':['张国荣','张丰毅','巩俐','葛优']}
          {'rating':[9.5,1559181],'id':'1292720','type':['剧情','爱情'],'title':'阿甘正传','actors':['汤姆·汉克斯','罗宾·怀特']}
          ]
    
    name = input('请输入你要查询的演员:')
    for item in lst:			#遍历列表,得到一个{},item是一个又一个的字典
        act_lst = item['actors']
        for actor in act_lst:
            if name in actor:
                print(name,'出演了：',item['title'])
                
        '''for movie in item:		#遍历字典,得到movie	是一个字典中的key
            actors = movie['actors']       
            if name in actors:
                print(name + '出演了:' + movie)'''
                
    ```

    第一层for循环遍历列表可以得到每一部电影，而每一部电影又是一个字典，只需要根据key在字典中取值即可。根据演员的键actors取出学员的列表，使用判断name在列表中是否存在，最后根据电影名称的键title取出电影的名称，进行输出。

- 被动掉坑：程序代码逻辑没有错，只是因为用户错误操作或者一些“例外情况”而导致的程序崩溃。

    ```python
    '''输入两个整数并进行除法运算'''
    a = input('请输入第一个整数：')
    a = int(a)
    b = input('请输入第二个整数：')
    b = int(b)
    result = a/b
    print('结果为：',result)
    ```

## 2. 异常处理机制

### （1）try...except结构、try...except...except结构

```python
try:
    n1 = int(input('请输入第一个整数：'))
    n2 = int('请输入第二个整数：')
    result = n1/n2
    print('结果为：',result)
except ZeroDivisionError:
    print('对不起，除数不允许为0')
except ValueError:
    print('只能输入数字串')
except BaseException as e:		#except从子类到父类，最后可以增加BaseException
    print(e)
print('程序结束')
    
```

### （2）try...except...else结构

如果try块中没有抛出异常，则执行else块，如果try中抛出异常，则执行except块。

```python
try:
    a = int(input('请输入第一个整数：'))
	b = int(input('请输入第二个整数：'))
	result = a / b
except BaseException as e:
    print('出错了',e)
else:
    print('计算结果为：',result)
```

### （3）try...except...else...finally结构

finally块无论是否发生异常都会被执行，能常用来释放try块中申请的资源。

```python
try:
    a = int(input('请输入第一个整数：'))
	b = int(input('请输入第二个整数：'))
	result = a / b
except BaseException as e:
    print('出错了',e)
else:
    print('计算结果为：',result)
finally:
    print('谢谢您的使用')
```

### （4）traceback模块

使用traceback模块打印异常处理信息，存储log日志。

```python
#print(10/0)

import traceback
try:
    print('------------------')
    print(1/0)
except:
    traceback.print_exc()
```

## 3. Python常见的异常类型

| 序号 |     异常类型      |              描述              |
| :--: | :---------------: | :----------------------------: |
|  1   | ZeroDivisionError | 除（或取模）零（所有数据类型） |
|  2   |    IndexError     |   序列中没有此索引（index）    |
|  3   |     KeyError      |        映射中没有这个键        |
|  4   |     NameError     | 未声明/初始化对象（没有属性）  |
|  5   |    SyntaxError    |         Python语法错误         |
|  6   |    ValueError     |         传入无效的参数         |

```python
'''ZeroDivisionError'''
print(10/0)
'''IndexError'''
lst = [11,22,33,44]
print(lst[4])
'''KeyError'''
dic = {'name':'张三','age':20}
print(dic['gender'])
'''NameError'''
print(num)
'''SyntaxError'''
int a = 20
'''ValueError'''
a = int('hello')
```

## 4. PyCharm的调试模式

```python
i = 1
while i <= 10:		#设置断点进行调试
    print(i)	
    i += 1
```

# 十三、找对象不积极，思想有问题

## 1. 两大编程思想

<table >
    <tr>
        <td style="text-align:center"> </td>
        <td style="text-align:center">面向过程</td>
        <td style="text-align:center">面向对象</td>
    </tr>
    <tr>
        <td> 区别 </td>
        <td>事物比较简单，可以用线性的思维去解决</td>
        <td>事物比较复杂，使用简单的线性思维无法解决</td>
    </tr>
    <tr>  
        <td>共同点</td>       
        <th colspan="2">面向过程和面向对象都是解决实际问题的一种思维方式
        </th>     
    </tr> 
     <tr>  
        <td></td>       
        <th colspan="2">二者相辅相成，并不是对立的；解决复杂问题，通过面向对象方式便于我们从宏观上把握事物之间复杂的关系、方便我们分析整个系统；具体到微观操作，仍然使用面向过程方式来处理。
        </th>     
    </tr>  
</table>

## 2. 类和对象的创建

**类**是多个类似事物组成的群体的统称。能够帮助我们快速理解和判断事物的性质。

**对象：**不同数据类型属于不同的类，像100、99、520都是int类之下包含的相似的不同个例，这些个例专业术语称为实例或者对象。

### （1）类的创建

```python
class Student:
    pass

'''Student类名由一个或多个单词组成，每个单词的首字母大写，其余小写'''
#Python中一切皆对象，Student是对象吗？内存由开空间吗？
print(id(Student))
print(type(Student))
print(Student)
```

**类的组成：**

- 类属性
- 实例方法
- 静态方法
- 类方法

```python
class Student:
    native_pace = '吉林'		#直接写在类里的变量，称为类属性
    def __init__(self,name,age):
        self.name = name	#self,name称为实体属性，进行了一个赋值的操作，将局部变量name的值赋给实体属性
        self.age = age
   
	#实例方法
    def eat(self):
        print('学生在吃饭...')
    #静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')
    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')
        
'''在类之外定义的称为函数，在类之内定义的称为方法
def drink();		#函数
	print('喝水')
'''
```

### （2）对象的创建

> 对象的创建又称为类的实例化：实例名 = 类名（）

```python
class Student:
    native_pace = '吉林'		#直接写在类里的变量，称为类属性
    def __init__(self,name,age):
        self.name = name	#self,name称为实体属性，进行了一个赋值的操作，将局部变量name的值赋给实体属性
        self.age = age
   
	#实例方法
    def eat(self):
        print('学生在吃饭...')
    #静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')
    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')
        
'''在类之外定义的称为函数，在类之内定义的称为方法
def drink();		#函数
	print('喝水')
'''

#创建Student类的对象
stu1 = Student('张三'，20)
stu1.eat()			#对象名.方法名()
print(stu1.name)
print(stu1.age)
print('---------------------------')
print(id(stu1))
print(type(stu1))
print(stu1)
print('---------------------------')
print(id(Student))
print(type(Student))
print(Student)
print('--------------------------')
Student.eat(stu1)		#类名.方法名(类的对象)		与stu1.eat()一样，都是调用Student中的eat方法
```

## 3. 类属性、类方法、静态方法

- **类属性：**类中方法外的变量称为类属性，被该类的所有对象所共享。
- **类方法：**使用@classmethod修饰的方法，使用类名直接访问的方法。
- **静态方法：**使用@staticmethod修饰的方法，使用类名直接访问的方法。

```python
class Student:
    native_pace = '吉林'		#直接写在类里的变量，称为类属性
    def __init__(self,name,age):		#初始化方法
        self.name = name	#self,name称为实体属性，进行了一个赋值的操作，将局部变量name的值赋给实体属性
        self.age = age
   
	#实例方法
    def eat(self):
        print('学生在吃饭...')
        
    #静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')
        
    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')

        
print('------------类属性的使用方法---------------')      
print(Student.native_pace)
stu1 = Student('张三',20)
stu2 = Student('李四',30)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace = '天津'
print(stu1.native_pace)
print(stu2.native_pace)
print('------------类方法的使用方式--------------')
Student.cm()
print('-----------静态方法的使用方式----------------')
Student.method()
```

## 4. 动态绑定属性和方法

> Python是动态语言，在创建对象后，可以动态地绑定属性和方法。

```python
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(self.name + '在吃饭')
        
stu1 = Student('张三',20)
stu2 = Student('李四',30)
print(id(stu1))
print(id(stu2))
print('---------只给李四添加一个性别---------------')
stu2.gender = '女'
print(stu1.name,stu1.age)		#如果添加stu1.gender会抛出AttributeError
print(stu2.name,stu2.age,stu2.gender)

print('-------------------------')
stu1.eat()
stu2.eat()

def show():
    print('定义在类之外地，称为函数')
stu1.show = show
stu1.show
#stu2.show		因为stu2并没有绑定show方法
```

# 十四 、接着找对象

**面向对象的三大特征：**

- 封装：提高程序的安全性。（1）将数据（属性）和行为（方法）包装到类对象中，在方法内部对属性进行操作，在类对象的外部调用方法。这样，无需关心方法内部的具体实现细节，从而隔离了复杂度；（2）在Python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前边使用两个“__”；
- 继承：提高代码的复用性；
- 多态：提高程序的可扩展性和可维护性。

## 1. 封装

```python
class Car:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print('汽车已启动...')
        
car = Car('宝马X5')
car.start()
print(car,brand)
```

```python
class Student:
    def __init__(self,name,age):
        self.name = name	
        self.__age = age 	#年龄age不希望在类的外部被使用，所以加了两个“_”
    def show(self):
        print(self.name,self.__age)

stu = Student('张三',20)
stu.show()
#在类的外部使用name与age
print(stu.name)
#print(stu.__age)
print(dir(stu))
print(stu._Student__age)	#在类的外部可以通过	_Student__age	进行访问
```

## 2. 继承

**继承的特点：**如果一个类没有继承任何类，则默认继承object；Python支持多继承；定义子类时，必须在其构造函数中调用父类的构造函数。

```python
#语法结构
class 子类类名(父类1，父类2...):
    pass
```

```python
class Person(object):		#Person继承object类
    def __init__(self,anme,age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no = stu_no
        
class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear = teachofyear
       
stu = Student('张三',20,'1001')
teacher = Teacher('李四'，34，10)

stu.info()
teacher.info()
```

```python
class A(object):
    pass
class B(object):
    pass
class C(A,B):		#Python支持多继承
    pass
```

## 3. 方法重写

- 如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其（方法体）进行重新编写。
- 子类重写后的方法中可以通过super().xxx()调用父类中被重写的方法。

```python
class Person(object):		#Person继承object类
    def __init__(self,anme,age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no = stu_no
    def info(self):
        super().info()
        print(self.stu_no)
        
class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear = teachofyear
    def info(self):
        super().info()
        print('教龄',self.teachofyear)
       
stu = Student('张三',20,'1001')
teacher = Teacher('李四'，34，10)

stu.info()
teacher.info()
```

## 4. object类

- object类是所有类的父类，因此所有类都有object类的属性和方法。
- 内置函数dir()可以查看指定对象所有属性。
- Object有一个\_str\_()方法，用于返回一个对于“对象的描述”，对应于内置函数str()经常用于print()方法，帮助我们查看对象的信息，所以我们经常会对\_str_()进行重写。

```python
class Student:
   def __init__(self,name,age):
    self.name = name
    self.age = age
   def __str__(self):
    return '我的名字是{0}，今年{1}岁。'.format(self.name,self,age)
stu = Student('张三',20)
print(dir(stu))
print(stu)		#默认调用__str__()方法
print(type(stu))
```

## 5. 多态

简单地说，多态就是“具有多种形态”，它指的是：即便不知道一个变量所引用地对象到底是什么类型，仍然可以通过这个变量调用方法，在运行过程中根据变量所用对象的类型，动态决定调用哪个对象中的方法。

```python
class Animal(object):
    def eat(self):
        print('动物会吃')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头...')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼...')
        
class Person:
    def eat(self):
        print('人吃五谷杂粮')
        
#定义一个函数
def fun(obj):
    obj.eat()
#开始调用函数
fun(Cat())
fun(Dog())
fun(Animal())
print('-----------------------')
fun(Person())
```

**静态语言和动态语言关于多态的区别：**

- 静态语言实现多态的三个必要条件：继承，方法重写，父类引用指向子类对象，例如Java。
- 动态语言的多态崇尚“鸭子类型”。当看到一只鸟走起来像鸭子、游泳起来像鸭子，那么这只鸟就可以被称为鸭子。在鸭子类型中，不需要关心对象是什么类型，到底是不是鸭子，只关心对象的行为。

## 6. 特殊方法和特殊属性

<table>
    <tr>
        <td > &nbsp </td>
        <td style="text-align:center">  名称  </td>
        <td style="text-align:center">  描述  </td>
    </tr>
    <tr>
        <td style="text-align:center"> 特殊属性 </td>
        <td style="text-align:center">__dict()__</td>
        <td >获得类对象或者实例对象所绑定的所有属性和方法的字典</td>
    </tr>
    <tr>       
        <th style="text-align:center" rowspan="4"> 特殊方法 </th>
        <td style="text-align:center">__len__()</td>
        <td >通过重写__len__()方法，让内置函数len()的参数可以是自定义类型</td>
    </tr> 
     <tr>  
        <td style="text-align:center">__add__()</td> 
        <td >通过重写__add__()方法，可以使用自定义对象具有“+”功能</td>
    </tr>  
    <tr>  
        <td style="text-align:center">__new__()</td> 
        <td >用于创建对象</td>
    </tr> 
    <tr>  
        <td style="text-align:center">__init__()</td> 
        <td >对创建的对象进行初始化</td>
    </tr> 
</table>

```python
'''特殊属性'''
print(dir(object))
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age
class D(A):
    pass
#创建C类的对象
x = C('Jack',20)			#x是C类型的一个实例对象
print(x.__dict__)			#实例对象的属性字典
print(C.__dict__)
print('-------------------------')
print(x.__class__)			#输出对象所属的类
print(C.__bases__)			#输出C类的父类类型的元素
print(C.__base__)			#输出类的基类
print(C.__mro__)			#类的层次结构
print(A.__subclasses__())	#输出A的子类
```

```python
'''特殊方法'''
a = 20
b = 100
c = a+b			#两个int类型的对象相加操作
d = a.__add__(b)
print(c)
print(d)

class Student:
    def __init__(self,name):
        self.name = name
    def __add__(self,other):
        return self.name + other.name
    def __len__(self):
        return len(self.name)
stu1 = Student('Jack')
stu2 = Student('李四')

s = stu1 + stu2			#实现了两个对象的加法运算（因为在Student类中，编写了__add__(）特殊的方法
print(s)
s = stu1.__add__(stu2)
print(s)

print('----------------------------')
lst = [11,22,33,44]
print(len(lst))
print(lst.__len__())
print(len(stu1))
```

```python
'''__new__()和__init__()'''
class Person(object):
    
    def __new__(cls,*args,**kwargs):			#9360
        print('__new__()被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象的id值为{0}'.format(id(obj)))				#7104
        return obj
	def __init__(self,name,age):
        print('__init__被调用了，self的id值为：{0}'.format(id(self)))			#7104
        self.name = name
        self.age = age
        
print('object这个类对象的id为：{0}'.format(id(object)))		#3232
print('Person这个类对象的id为：{0}'.format(id(Person)))		#9360

#创建Person类的实例对象
p1 = Person('张三',20)
print('p1这个Person类的实例对象的id为：{0}'.format(id(p1)))		#7104
```

## 7. 类的浅拷贝与深拷贝

**变量的赋值操作：**只是形成两个变量，实际上还是指向同一个对象。

**浅拷贝：**Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝。因此，源对象与拷贝对象会引用同一个子对象。

**深拷贝：**使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同。

```python
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk
        
#(1)变量的赋值
cpu1 = CPU()
cpu2 = cpu1
print(cpu1,id(cpu1))
print(cpu2,id(cpu2))
#(2)类的浅拷贝
print('-------------------')
disk = Disk()		#创建一个硬盘类的对象
computer = Computer(cpu1,disk)	#创建一个计算机类的对象
#浅拷贝
import copy
computer2 = copy.copy(computer)
print(disk)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)
print('---------------------')
#深拷贝
computer3 = copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)
```

![image-20210210175002816](../PythonProjects/Typora_image/image-20210210175002816.png)

# 十五、百宝箱

## 1. 什么叫模块？

**模块（modules）：**

- 一个模块中可以包含N多个函数
- 在Python中一个扩展名为 .py 的文件就是一个模块
- 使用模块的好处
    - 方便其他程序和脚本的导入并使用
    - 避免函数名和变量名的冲突
    - 提高代码的可维护性
    - 提高代码的可重用性

```python
def fun():
    pass
def fun2():
    pass
class Student:
    native_place = '吉林'		#类属性
    def eat(self):
        pass
    @classmethod
    def cm(cls):
        pass
    @staticmethod
    def sm():
        pass
    

a = 10 
b = 20 
print(a,b)
```

## 2. 自定义模块

> 导入模块
>
> import			模块名称			[as 别名]
>
> from		模块名称		import		函数/变量/类

```python
import math
print(id(math))
print(type(math))
print(dir(math))

from math import pi
from math import pow
print(pi)
print(pow(2,3))
```

```python
#自定义模块
def add(a,b):
    return a+b
def div(a,b):
    return a/b
#如何导入自定义模块
'''pycharm右键MarkDirectory as SourcesRoot'''
```

## 3. 以主程序的形式执行

在每个模块的定义中都包括一个记录模块名称的变量\_name\_，程序可以检查该变量，以确定他们在哪个模块执行，如果一个模块不是被导入到其他程序中执行，那么它可能在解释器的顶端模块中执行。顶端模块的\_name\_变量的值为\_main\_

```python
def add(a,b):
    return a+b

if __name__ == '__main__':
    print(add(10,20))		#只有当点击运行calc2模块时才会执行运算
```

```python
import calc2
print(calc2.add(100,200))
```

## 4. Python中的包

**包**是一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下。

**作用：**代码规范；避免模块名称冲突

**包与目录的区别：**包含\_\_int\_\_.py文件的目录叫作包；目录里通常不包含\_\_int\_\_.py文件

```python
#单击右键，创建-Python Package

import package
import calc
#使用import导入时只能跟包名和模块名

from package import modelA
from package.modelA import a
#使用from...import可以导入包，模块，函数变量等
```

## 5. Python中常见的内置模块

|  模块名  |                             描述                             |
| :------: | :----------------------------------------------------------: |
|   sys    |            与Python解释器及其环境操作相关的标准库            |
|   time   |               提供与时间相关的各种函数的标准库               |
|    os    |              提供了访问操作系统服务功能的标准库              |
| calendar |               提供与日期相关的各种函数的标准库               |
|  urllib  |            用于读取来自网上（服务器）的数据标准库            |
|   json   |               用于使用JSON序列化和反序列化对象               |
|    re    |            用于在字符串中执行正则表达式匹配和替换            |
|   math   |                 提供标准算术运算函数的标准库                 |
| decimal  | 用于进行精确控制运算精度、有效数位和四舍五入操作的十进制运算 |
| logging  |  提供了灵活的记录事件、错误、警告和调试信息等日志信息的功能  |

```python
import sys
import time
import urllib.request
import math

print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print(time.time())
print(time.localtime(time.time()))

print(urllib.request.urlopen('http://www.baidu.com').read())

print(math.pi)
```

## 6. 第三方模块的安装及使用

```
#DOS
pip install schedule
python
import schedule
```

```python
import schedule
import time

def job():
    print('哈哈-----')
    
schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
```

# 十六、大宝藏

## 1. 编码格式介绍

**常见的字符编码格式：**

- Python的解释器使用的是Unicode（内存）
- .py文件咋磁盘上使用UTF-8存储（外存）

![image-20210215103231516](../PythonProjects/Typora_image/image-20210215103231516.png)



## 2. 文件的读写原理

- 文件的读写俗称“IO操作”

> Python操作文件 	→	打开或新建文件夹	→	读写文件	→	关闭资源

## 3. 文件读写操作

![image-20210216142431378](../PythonProjects/Typora_image/image-20210216142431378.png)

```python
file = open('a.txt','r')
print(file.readlines())		#结果是一个list
file.close()
```

| 打开模式 |                             描述                             |
| :------: | :----------------------------------------------------------: |
|    r     |         只读模式打开文件，文件指针将会放在文件的开头         |
|    w     | 只写模式打开文件，如果文件不存在则创建；如果文件存在，则覆盖原有内容，指针放在文件开头 |
|    a     | 追加模式打开文件，如果文件不存在则创建，文件指针在文件开头；如果文件存在，则在文件末尾追加内容，文件指针在原文件末尾 |
|    b     | 二进制方式打开文件，不能单独使用，需要与其他模式一起使用，rb或者wb |
|    +     |  读写模式打开文件，不能单独使用，需要与其他模式一起使用，a+  |

```python
file = open('b.txt','w')
file.write('Python')
file.close()

file = open('b.txt','a')
file.write('Python')
file.close()
```

```python
src_file = open('logo.png','rb')
target_file = open('copylogo.png','wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()
```

## 4. 文件对象常用的方法

|        方法名         |                             说明                             |
| :-------------------: | :----------------------------------------------------------: |
|     read([size])      | 从文件中读取size个字节或字符的内容返回，若省略[size]，则读取到文件末尾，一次读取文件所有内容 |
|      readline()       |                   从文本文件中读取一行内容                   |
|      readlines()      | 把文本文件中每一行都作为独立的字符串对象，并将这些对象放入列表返回 |
|      write(str)       |                   将字符串str内容写入文件                    |
|  writelines(s_list)   |         将字符串列表s_list写入文本文件，不添加换行符         |
| seek(offset[,whence]) | 把文件指针移动到新的位置，offset表示相对whence的位置；offset为正往结束方向移动，为负往开始方向移动。whence不同的值代表不同含义：0从文件头开始计算，1从当前位置开始计算；2从文件末尾开始计算 |
|        tell()         |                    返回文件指针的当前位置                    |
|        flush()        |             把缓冲区的内容写入文件，但不关闭文件             |
|        close()        |  把缓冲区的内容写入文件，同时关闭文件，释放文件对象相关资源  |

```python
file = open('a.txt','r')
print(file.read(2))
print(file.readline())
print(file.readlines())
file.close()

file = open('c.txt','a')
file.write('hello')
lst = ['java','go','python']
file.writelines(lst)
file.close()

file = open('c.txt','r')
file.seek(2)	#一个中文两个字节
print(file.read())
print(file.tell())
file.close()

file = open('c.txt','a')
file.write('hello')
file.flush()
file.write('world')
file.close()
```

## 5. with语句（上下文管理器）

- with语句可以自动管理上下文资源，不论什么原因跳出with块，都能确保文件正确的关闭，以此来达到释放资源的目的。

```python
print(type(open('a.txt','r')))
with open('a.txt','r') as file:
    print(file.read())

'''MyContentMgr实现了特殊方法__enter__(),__exit__()称为该类对象遵守了上下文管理器协议。
该类对象的实例对象，称为上下文管理器

MyContentMgr()'''
class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        print('exit方法被调用执行了')
        
    def show(self):
        print('show方法被调用执行了')
with MyContentMgr() as file:
    file.show()
```

```python
#文件的复制
with open('logo.png','rb') as src_file:
    with open('copy2logo.png','wb') as target_file:
        target_file.write(src_file.read())
```

## 6. 目录操作

### （1）os模块

- os模块是Python内置的与操作系统功能和文件系统相关的模块，该模块中的语句的执行结果通常与操作系统有关，在不同的操作系统上运行，得到的结果可能不一样。

- os模块与os.path模块用于对目录或文件进行操作。

```python
#os模块与操作系统相关的一个模块
import os
os.system('notepad.exe')
os.system('calc.exe')
#直接调用可执行文件
os.startfile('D:\\YesPlayMusic\\YesPlayMusic.exe')
```

|              函数               |              说明              |
| :-----------------------------: | :----------------------------: |
|            getcwd()             |       返回当前的工作目录       |
|            listdir()            | 返回指定路径下的文件和目录信息 |
|       mkdir(path[,mode])        |            创建目录            |
| makedirs(path1/path2...[,mode]) |          创建多级目录          |
|           rmdir(path)           |            删除目录            |
|   removedirs(path1/path2...)    |          删除多级目录          |
|           chdir(path)           |    将path设置成当前工作目录    |

```python
import os
print(os.getcwd())

os.listdir('../chap15')			#办公自动化经常使用
print(lst)

os.mkdir('newdir2')
os.makedirs('A/B/C')
os.rmdir('newdir2')
os.removedirs('A/B/C')

os.chdir('F:\\desktop\\chap14')
print(os.getcwd())
```

### （2）os.path模块

|      函数       |                            说明                             |
| :-------------: | :---------------------------------------------------------: |
|  abspath(path)  |                用于获取文件或目录的绝对路径                 |
|  exists(path)   | 用于判断文件或目录是否存在，如果存在返回True，否则返回False |
| join(path,name) |               将目录与目录或者文件名拼接起来                |
|   splitext()    |                     分离文件名和扩展名                      |
| basename(path)  |                   从一个目录中提取文件名                    |
|  dirname(path)  |           从一个路径中提取文件路径，不包括文件名            |
|   isdir(path)   |                     用于判断是否为路径                      |

```python
import os.path
print(os.path.abspath('demo13.py'))
print(os.path.exists('demo13.py'),os.path.exists('demo18.py'))
print(os.path.join('E:\\Python','demo13.py'))
print(os.path.split('E:\\vippython\\chap15\\demo13.py'))
print(os.path.splitext('demo13.py'))
print(os.path.basename('E:\\vippython\\chap15\\demo13.py'))
print(os.path.dirname('E:\\vippython\\chap15\\demo13.py'))
print(os.path.isdir('E:\\vippython\\chap15\\demo13.py'))
```

```python
'''列出指定目录下的所有py文件'''
import os
path = os.getcwd()
lst = os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)
```

```python
#chap15-->newdir-->sub-->遍历所有文件walk
import os
path = os.getcwd()
lst_files = os.walk(path)
for dirpath,dirname,filename in lst_files:
    print(dirname)
    print(dirpath)
    print(filename)
    print('--------------------------')
    for dir in dirname:
        print(os.path.join(dirpath,dir))
        
    for file in filename:
        print(os.path.join(dirpath,file))
    print('+++++++++++++++++++++++++')
```

![image-20210216174510594](../PythonProjects/Typora_image/image-20210216174510594.png)

# 十七、学生信息管理系统

## 1. 需求分析

**学生管理系统应具备的功能：**

- 添加学生及成绩信息
- 将学生信息保存到文件中
- 修改和删除学生信息
- 查询学生信息
- 根据学生成绩进行排序
- 统计学生的总分

## 2. 系统设计

**七大模块：**

- 录入学生信息模块
- 查找学生信息模块
- 删除学生信息模块
- 修改学生信息模块
- 学生成绩排名模块
- 统计学生总人数模块
- 显示全部学生信息模块

![image-20210216180215185](../PythonProjects/Typora_image/image-20210216180215185.png)

![image-20210219105757447](../PythonProjects/Typora_image/image-20210219105757447.png)

## 3. 系统开发必备

- **系统开发环境**
    - 操作环境：Win10
    - Python解释器版本：Python3
    - 开发环境：PyCharm
    - Python内置模块：os，re

- **项目目录结构**

    studentsys	-->	students.txt	&	stusystem.py

## 4. 主函数设计

- 系统主界面运行效果图
- 主函数的业务流程

| 编号 |               功能               |
| :--: | :------------------------------: |
|  0   |             退出系统             |
|  1   |  录入学生信息，调用insert()函数  |
|  2   |  查找学生信息，调用search()函数  |
|  3   |  删除学生信息，调用delete()函数  |
|  4   |  修改学生信息，调用modify()函数  |
|  5   |  对学生成绩排序，调用sort()函数  |
|  6   | 统计学生总人数，调用total()函数  |
|  7   | 显示所有学生信息，调用show()函数 |

```python
filename = 'student.txt'
import os
def main():
    while True:
        menu()
        choice = int(input('请选择：\n'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice == 0:
                answer = input('您确定退出系统吗？y/n \n')
                if answer == 'y' or if answer == 'Y':
                    print('谢谢您的使用！')
                    break
                else:
                    continue
            if choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
def menu():
    print('======================学生信息管理系统===================')
    print('-----------------------功能菜单-----------------------')
    print('\t\t\t\t\t\t 1.录入学生信息')
    print('\t\t\t\t\t\t 2.查找学生信息')
    print('\t\t\t\t\t\t 3.删除学生信息')
    print('\t\t\t\t\t\t 4.修改学生信息')
    print('\t\t\t\t\t\t 5.排序')
    print('\t\t\t\t\t\t 6.统计学生总人数')
    print('\t\t\t\t\t\t 7.显示所有学生信息')
    print('\t\t\t\t\t\t 0.退出系统')
    print('------------------------------------------------------')
    
def insert():	#(1)
    pass
def search():	#(4)
    pass
def delete():	#(2)
    pass
def modify():	#(3)
    pass
def sort():		#(7)
    pass
def total():	#(5)
    pass
def show():		#(6)
    pass

if __name__ == '__main__':
    main()
```

## 5. 学生信息维护模块设计

### （1）录入学生信息

- **实现录入学生信息模块：**从控制台录入学生信息，并保存到磁盘文件中。
- save(student)函数，用于将学生信息保存到文件
- insert()函数，用于录入学生信息

```python
#(1)
def insert():
    student_list = []
    while True:
        id = input('请输入ID（如1001）：')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break
        try:
            English = int(input('请输入英语成绩：'))
            Python = int(input('请输入Python成绩：'))
            Java = int(input('请输入Java成绩'))
        except:
            print('输入无效，不是整数类型，请重新输入。')
            continue
        #将录入的学生信息保存到字典中
        student = {'id':id,'name':name,'English':English,'Python':Python,'Java':Java}
        #将学生信息添加到列表中
        student_list.append(student)
        answer = input('是否继续添加？y/n \n')
        if answer == 'y':
            continue
        else:
            break
    #调用save()函数
    save(student_list)
    print('学生信息录入完毕！')

def save(lst):
    try:
        stu_txt = open(filename,'a',encoding = 'utf-8')
    except:
        stu_txt = open(filename,'w',encoding = 'utf-8')
        for item in lst:
            stu_txt.write(str(item) + '\n')
        stu_txt.close()
```

### （2）删除学生信息

- **实现删除学生信息功能：**从控制台录入学生ID，到磁盘文件中找到对应的学生信息，并将其删除。

```python
#(2)
def delete():
    while True:
        student_id = input('请输入要删除的学生的ID：')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename,'r',encoding = 'utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old =[]
            flag = Fasle		#标记是否删除
            if student_old:
                with open(filename,'w',encoding = 'utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d = dict(eval(item))	#将字符串转成字典
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到ID为{student_id}的学生信息')
                else:
                    print('无学生信息')
                    break
                show()		#删除之后要重新显示所有学生信息
                answer = input('是否继续删除？y/n \n')
                if answer == 'y':
                    continue
                else:
                    break
```

### （3）修改学生信息

- **实现修改学生信息功能：**从控制台录入学生ID，到磁盘文件中找到对应的学生信息，将其进行修改。

```python
def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding = 'utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('请输入要修改的学生的ID：\n')
    with open(filename,'w',encoding = 'utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('找到学生信息，可以修改他（她）的相关信息了！')
                while True:
                    try:
                        d['name'] = input('请输入姓名：\n')
                        d['English'] = input('请输入英语成绩：\n')
                        d['Python'] = input('请输入Python成绩：\n')
                        d['Java'] = input('请输入Java成绩：\n')
                    except:
                        print('您的输入有误，请重新输入！')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功！')
            else:
                wfile.write(str(d) + '\n')
        answer = input('是否继续修改其他学生信息？y/n \n')
        if answer == 'y':
            modify()
```

### （4）查找学生信息

- **实现查询学生信息功能：**从控制台录入学生ID或姓名，到磁盘文件中找到对应的学生信息。

```python
def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按ID查找请输入1，按姓名查找请输入2：\n')
            if mode = '1':
                id = input('请输入学生ID:\n')
            elif mode = '2':
                name = input('请输入学生姓名:\n')
            else:
                print('您的输入有误，请重新输入：\n')
                search()
            with open(filename,'r',encoding = 'utf-8') as  rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
             #显示查询结果
            show_student(student_query)
            #清空列表
            student_query.clear()
            answer = input('是否要继续查询？y/n \n')
            if answer == 'y':
                continue
            else:
                break
        else:
            print('暂未保存学生信息！')
            return
def show_student(lst):
    if len(lst) == 0:
        print('没有查询到学生信息，无数据显示！')
        return
    #定义标题的显示格式
    format_title = '{:^6 \t {:^12} \t {:^8} \t {:^10} \t {:^10} \t {:^8}}'
    print(format_title.format('ID','姓名','英语成绩','Python成绩','Java成绩','总成绩'))
    #定义内容的显示格式
    format_data = '{:^6 \t {:^12} \t {:^8} \t {:^8} \t {:^8} \t {:^8}}'
    for item in lst:
        print(format_data.format(item.get('id')),item.get('name'),item.get('English'),item.get('Python'),item.get('Java'),int(item.get('English'))+int(item.get('Python'))+int(item.get('Java'))  )
```

### （5）统计学生总人数

- **实现统计学生总人数：**统计学生信息文件中保存的学生信息个数。

```python
def total():
    if os.path.exists(filename):
        with open(filename.'r',encoding = 'utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生。')
    else:
        print('还没有录入学生信息。')
```

### （6）显示所有学生信息

- **实现显示所有学生信息功能：**将学生信息文件中保存的全部学生信息获取并显示。

```python
def show():
    student_lst =[]
    if os.path.exists(filename):		#判断文件是否存在
        with open(filename,'r',encoding ='utf-8') as rfile:		#打开文件
            students = rfile.readlines()		#读取全部数据
            for item in students:
                student_lst,append(eval(item))
            if student_lst:
                show_student(student_lst)		#调用显示学生信息的方法
    else:
        print('暂未保存数据')  
```

### （7）排序学生成绩

- **实现按学生成绩排序功能：**主要对学生信息按英语成绩，Python成绩，Java成绩，总成绩进行升序或者降序排序。

```python
def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding ='utf-8') as rfile:
            student_list = rfile.readlines()
        student_new = []
        for item in stuednt_list:
            d = dict(eval(item))
            student_new,append(d)
    else:
        return
    asc_or_desc = input('请选择 \n (0.升序；\n (1.降序')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('您的输入有误，请重新输入。')
        sort()
    mode = input('请选择排序方式 \n (1.按英语成绩排序; \n (2.按Python成绩排序; \n (3.按Java语言成绩排序; \n (0.按总成绩排序.')
    if mode == '1':
        student_new.sort(key = lambda x:int(x['English']),reverse = asc_or_desc_bool)
    elif mode == '2':
        student_new.sort(key = lambda x:int(x['Python']),reverse = asc_or_desc_bool)
    elif mode == '3':
        student_new.sort(key = lambda x:int(x['Java']),reverse = asc_or_desc_bool)
    elif mode == '0':
        student_new.sort(key = lambda x: int(x['English']) + int(x['Python']) + int(x['Java']),reverse = asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入！')
        sort()
    show_student(student_new)		#显示排序结果
```

## 6. 项目打包

- **安装第三方模块：**（1）在线安装方式	pip install PyInstaller；（2）执行打包操作

# 十八、案例实操

## 1. 案例一

### （1）向文件输出“奋斗成就更好的你”

```python
# Task1 使用print方式进行输出
fp = open('F:/test.txt','w')
print('奋斗成就更好的你',file = fp)
fp.close()

# Task1 使用文件读写操作
with open('F:/test1.txt','w') as file:
    file.write('奋斗成就更好的你')
```

### （2）输出北京的天气预报

```python
print('星期日','今天')
print('--------------------')
print('08时','11时','14时','17时','20时','23时')
print('0℃ ','6℃ ','10℃','4℃ ','1℃ ','0℃ ')
print('--------------------')
print('明 天 ','2/23','2/11℃')
print('星期二','2/24','0/9℃')
print('星期三','2/25','-2/8℃')
print('星期四','2/26','-3/6℃')
print('星期五','2/27','-2/7℃')
print('星期六','2/28','-1/11℃')
```

### （3）机票购买界面

```python
print('✈国内 \t ♜国际.港澳台 \t ↘发现低价')
print('------------------------')
print('航班类型：⊙单程	⊙往返	⊙多程（含缺口城）')
print('出发城市：北京')
print('到达城市：长春')
print('出发日期：2020-3-8')
print('返回日期：yyyy-MM-dd')
print('------------------------')
print('\t\t ☐带儿童  ☐带婴儿')
print('\t\t\t__________')
print('\t\t\t___搜索___')
```

### （4）北京地铁1号线运行图

```python
print('地铁1\t\t\t四惠东→苹果园')
print('\t\t首车：05:05')
print('\t\t末车：23:30\t\t票价：起步价：2元')
print('------------------------------------')
print('  1\t\t  3\t  5\t  7\t\t  9\t\t  11\t\t  12\t\t 14\t\t 16\t\t 18\t\t 20\t\t')
print('   ⇌\t\t ⇌\t\t ⇌\t\t ⇌\t\t ⇌\t\t ⇌\t\t ⇌\t\t ⇌\t\t ⇌\t\t ⇌\t\t')
print('四惠东\t大望路\t永安里\t东单\t天安门东\t西单\t复兴门\t木樨地\t公主坟\t五棵松\t八宝山')
```

## 2. 案例二

### （1）输出杨老师出版的图书信息

```python
#1
print('►→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→◄')
print('▷       《Java程序设计教程》   ◁')
print('► 出版社：西安电子科技大学出版社 ◄')
print('▷     出版时间：2019-02-02     ◁')
print('►        定  价：56.8          ◄')
print('▷→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→◁')

#2
book_name = 'Java程序设计教程'
publish = '西安电子科技大学出版社'
pub_date = '2019-02-02'
price = 56.8
print('▶➝➝➝➝➝➝➝➝➝➝➝➝➝➝➝➝➝◀')
print('▷\t\t 《',book_name,'》 \t\t ◁')
print('▷\t出版社：',publish,'\t ◁')
print('▷\t出版时间：',pub_date,'\t\t\t ◁')
print('▷\t定 价：',price,'\t\t\t\t ◁')
print('▷➝➝➝➝➝➝➝➝➝➝➝➝➝➝➝➝➝◁')
```

### （2）输出《红楼梦》中的金陵十二钗前五位

```python
#1 变量的赋值
name1 = '林黛玉'
name2 = '薛宝钗'
name3 = '贾元春'
name4 = '贾探春'
name5 = '史湘云'
print('①\t' + name1)
print('②\t' + name2)
print('③\t' + name3)
print('④\t' + name4)
print('⑤\t' + name5)
#2 列表
lst_name = ['林黛玉','薛宝钗','贾元春','贾探春','史湘云']
lst_sig = ['①','②','③','④','⑤']
for i in range(5):
    print(lst_sig[i],lst_name[i])

#3字典
d = {'①':'林黛玉','②':'薛宝钗','③':'贾元春','④':'贾探春','⑤':'史湘云'}
for key in d:
    print('key,d[key]')
print('zip-----------------')
for s,name in zip(lst_sig,lst_name):
    print(s,name)
```

### （3）输出图书音像勋章

```python
print('\033[0;35m\t\t图书音像勋章\033[m')
print('\033[0;35m-----------------------\033[m')
print('\033[0;32m❀图书音像勋章\t\t✪专享活动 \033[m')
print('\033[0;34m❤专属优惠\t\t\t☎优惠提醒 \033[m')
print('\033[0;35m-----------------------\033[m')
```

### （4）输出你的身体指标

```python
height = 170
weight = 50.5
bmi = weight / (height+weight)
print('您的身高是：',height)
#print('您的身高是：' + str(height))
print('您的体重是：' + str(weight))
print('您的BMI是：' + str(bmi))
print('您的BMI的指数是：' '{:0.2f}'.format(bmi)
```

## 3. 案例三

### （1）将指定的十进制数转换二进制、八进制、十六进制

```python
def fun():
	num = int(input('请输入一个十进制的整数：'))		#str转换成int类型
#使用个数可变的位置参数
	print(num,'的二进制数为：',bin(num))
#使用+作为连接符，注意符号左右均为str类型
	print(str(num) + '的二进制数为：' + 	bin(num))
#格式化字符串
	print('%s的二进制数为：%s' %  (num,bin(num)))
#格式化字符串
	print('{0}的二进制数为：{1}'.format(num,bin(num)))
#格式化字符串
	print(f'{num}的二进制数为：{bin(num)}')
	print('---------------------------')
	print(f'{num}的八进制数为：{oct(num)}')
	print(f'{num}的十六进制数为：{hex(num)}')

if __name__ == '__main__':
    while True:
    	try:
        	fun()
        	break
    	except:
        	print('只能输入整数！程序出错，请重新输入')
```

### （2）为自己手机充值

```python
print('用户手机账户原有话费金额为：\033[0;35m 8元 \033[m')
money = int(input('请输入用户的充值金额：'))
money += 8
print('当前的余额为：\033[0;32m ',money,'元 \033[m')
```

### （3）计算能量的消耗

```python
num = int(input('请输入您当天行走的步数：'))
calorie = num *28
print(f'您今天一共消耗了卡路里{calorie}，即{calorie/1000}千卡')
```

### （4）预测未来子女的身高

```python
father_height = float(input('请输入父亲的身高：'))
mother_height = float(input('请输入母亲的身高：'))
son_height = (father_height + mother_height)*0.54
print('预测子女的身高为：{}cm'.format(son_height))
```

## 4. 案例四

### （1）支付密码的验证

```python
pwd = input('支付宝支付密码：')
if pwd.isdigit():
    print('支付数据合法')
else:
    print('支付数字不合法，支付密码只能是数字')

print('---------------------------')
s = '支付数据合法' if pwd.isdigit() else '支付数字不合法，支付密码只能是数字'
```

### （2）模拟QQ账号登录

```python
qq = input('请输入您的QQ号：')
pwd = input('请输入您的密码：')
if qq == '296626472'  and pwd == '123':
    print('登陆成功')
else:
    print('账号或者密码不正确')
```

### （3）商品价格大竞猜

```python
import random
price = random.randint(1000,1500)
print('今日竞猜的商品为小米扫地机器人，价格在[1000-1500]之间：')
guess = int(input())
if guess > price:
    print('大了')
elif guess < price:
    print('小了')
else:
    print('猜对了')
print('真实价格为：',price)
```

### （4）根据星座查看运势

```python
d = {'白羊座':'1','金牛座':'2','双子座':'3','巨蟹座':'4','狮子座':'5'}
star = input('请输入您的星座查看近来的运势：')
#print(d[star])
print(d.get(star))
```

## 5. 案例五

### （1）循环输出26个字母对应的ASCII码值

```python
x = 97    #a的ASCII为97
for _ in range(1,27):
    print(chr(x),'--->',x)
    x += 1
    
print('---------------')
x = 97
while x < 123:
    print(chr(x),'---->',x)
    x += 1
```

### （2）模拟用户登录

```python
for i in range(1,4):
    user_name = input('请输入用户名：')
    user_pwd = input('请输入密码：')
    if user_name == 'admin' and user_pwd == '8888':
        print('登陆成功')
        break
    else:
        print('用户名或密码不正确！')
        if i < 3:
            print(f'您还有{3-i}次机会！')
else:
    print('对不起，三次均输入错误，请联系后台管理员！')
```

### （3）猜数游戏

```python
import random
rand = random.randint(1,100)
for i in range(1,11):
    num = int(input('在我心中有个数1-100，请你猜一猜。'))
    if num < rand:
        print('小了')
    elif num > rand:
        print('大了')
    else:
        print('恭喜你猜对了')
        break
print(f'您一共猜了{i}次')
if i < 3:
    print('真聪明')
elif i <= 7:
    print('还凑合')
else:
    print('天哪，找杨老师学习二分算法')
```

### （4）计算100-999之间的水仙花数

```python
import math
for i in range(100,1000):
    if math.pow((i % 10),3) + math.pow((i//10%10),3) + math.pow(i // 100,3) == i:
        print(i)
```

## 6. 案例六

### （1）“千年虫”我来了

```python
year = [82,89,88,86,85,00,99]
print('原列表：',year)
for index,value in enumerate(year):
    #print(index,value)
    if str(value) != '0':
        year[index] = int('19' + str(value))
    else:
        year[index] = int('200' + str(value))

print('修改之后的列表为：',year)
year.sort()
print('排序之后的列表为：',year)
```

### （2）京东购物流程

```python
lst = []
for i in range(0,5):
    goods = input('请输入商品的名称进入商品的入库，每次只能输入一个商品：\n')
    lst.append(goods)
for item in lst:
    print(item)
    
cart = []
while True:
    num = input('请输入要购买的商品编号：')
    for item in lst:
        if item.find(num) != -1:
            cart.append(item)
            break		#退出for循环
        if num == 'q':
            break		#退出while循环
print('您购物车里已经选好的商品为：')
'''for m in cart:
    print(m)'''
for j in range(len(cart)-1,-1,-1):
    print(cart[j])
```

## 7. 案例七

### （1）根据星座测试性格特点

```python
constellation = ['白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座','摩羯座','水瓶座','双鱼座']
nature = ['积极乐观','固执内向','圆滑世故','多愁善感','迷之自信','精明计较','犹豫不决','阴暗消极','放荡不羁','务实本分','作天作地','安于现状']

#将两个列表转成集合
a = zip(constellation,nature)
d = dict(zip(constellation,nature))
for item in a:
    print(item)
print(d)
key = input('请输入您的星座名称：')
flag = True
for item in d:
    if key == item:
        flag = True
        print(key,'的性格特点为：',d.get(key))
        break
    else:
        #print('您输入的星座有误')
        flag = False

if not flag:
    print('您输入的星座有误')
```

### （2）模拟12306火车票订票下单

```python
dict_ticket = {
    'G1569':['北京南-天津南','18:05','18:39','00:34'],
    'G1567':['北京南-天津南','18:15','18:49','00:34'],
    'G8917':['北京南-天津西','18:20','19:19','00:59'],
    'G203 ':['北京南-天津南','18:35','19:09','00:34']
}
print('车次\t\t出发站\t\t到达站\t\t出发时间\t\t\t到达时间\t\t\t历时时长')
for item in dict_ticket:
    print(item,end = '   ')
    for i in dict_ticket[item]:
        print(i,end='\t\t\t')
    print()		#换行
#输入要购买的车次    
train_no = input('请输入购买的车次：')
persons = input('请输入乘车人。如果是多人请使用逗号分隔')
s = f'您已购买了{train_no}次列车，'
s_info = dict_ticket[train_no]		#获取车次详细信息
s += s_info[0] + ' ' + s_info[1] + ' 开。'
print(f'{s}请{persons}尽快取走纸质车票。【铁路客服】')
```

## 8. 案例八

### （1）我的咖啡馆你做主

```python
coffee_name = ('蓝山','卡布奇诺','拿铁','皇家咖啡','女王咖啡','美丽与哀愁')
print('您好！欢迎光临小喵咖啡屋。')
print('本店经营的咖啡有：')
for index,item in enumerate(coffee_name):
    print(index+ +1 ,'.',item,end=' ')
    
index = int(input('\n请输入您喜欢的咖啡编号：'))
if 0 <= index <= len(coffee_name):
    print(f'您的咖啡[{coffee_name[index -1]}]好了，请您慢用')
```

### （2）显示2019年中超联赛前五名排行

```python
socres = (('广州恒大',72),('北京国安',70),('上海上港',66),('江苏苏宁',53),('山东鲁能',51))
for index,item in enumerate(scores):
    print(index +1,'.',end=' ')
    for score in item:
        print(score,end =' ')
    print()
```

### （3）模拟手机通讯录

```python
phones = set()		#创建一个空集合，集合元素没有顺序
for i in range(5):
    info = input(f'请输入第{i+1}个朋友的姓名和手机号码：')
    phones.add(info)
for item in phones:
    print(item)
```

## 9. 案例九

### （1）统计字符串中出现指定字符的次数

```python
def get_count(s,ch):
    count = 0
    for item in s:
        if ch.upper() == item or ch.lower() == item:
            count += 1
    return count

if __name__ == '__main__':
    s = 'hellopython,hellojava,hellogo'
    ch = input('请输入要统计的字符：')
    count = get_count(s,ch)
    print(f'{ch}在{s}中出现的次数为：{count}')
```

### （2）格式化输出商品的名称和单价

```python
def show(lst):
    for item in lst:
    	for i in item:
       	 print(i,end ='\t\t')
    print()
lst = [
    ['01','电风扇','美的',500],
    ['02','洗衣机','TCL',1000],
    ['03','微波炉','老板',400],
]
print('编号\t\t\t名称\t\t\t品牌\t\t\t单价')
show(lst)
print('----------格式化---------------')
for item in lst:
    item[0] = '0000' + item[0]
    item[3] = '￥{:.2f}'.format(item[3])
show(lst)    
```

## 10. 案例十

### （1）Mini计算器

```python
def calc(a,b,op):
    if op == '+':
        return add(a,b)
    elif op == '-':
        return sub(a,b)
    elif op == '*':
        return mul(a,b)
    elif op == '/':
        if b != 0:
            return div(a,b)
        else:
            return '除数不能为0'
        
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a/b

if __name__ == '__main__':
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    op = input('请输入运算符：')
    print(calc(a,b,op))
```

### （2）猜数游戏

```python
import random
def guess(num,guess_num):
    if num = guess_num:
        return 0
    elif guess_num > num:
        return 1
    else:
        return -1
    
num = random.randint(1,100)
for i in range(10):
    guess_num = int(input('我心里有个1-100的整数，请你猜一猜：'))
    result = guess(num,guess_num)
    if result == 0:
        print('猜对了')
        break
    elif result > 0:
        print('大了')
    else:
        print('小了')
else:
    print('真笨，10次都没猜中！') 
```

## 11. 案例十一

### （1）编写程序输入学员成绩

```python
try:
	score = int(input('请输入分数：'))
	if 0 <= score <= 100:
   	 	print('分数为：',score)
	else:
   	 	raise Exception('分数不正确')
except Exception as e:
    print(e)
```

### （2）编写程序，判断三个参数能否构成三角形

```python
def is_triangle(a,b,c):
    if a<0 or b<0 or c<0:
        raise Exception('三条边不能有负数')				#手动抛出异常对象
    
    #判断是否构成三角形
    if a+b>c and a+c>b and b+c>a:
        print(f'三角形的边长为a={a},b={b},c={c}')
    else:
        raise Exception(f'a={a},b={b},c={c}，不能构成三角形')
        
if __name__ == '__main__':
    try:
        a = int(input('请输入第一条边：'))
        b = int(input('请输入第二条边：'))
        c = int(input('请输入第三条边：'))
        is_triangle(a,b,c)
    except Exception as e:
        print(e)
```

## 12. 案例十二

### （1）定义一个圆的类来计算面积和周长

```python
import math
class Circle(object):
    def __init__(self,r):
        self.r = r
        
    def get_area(self):
        return math.pi * math.pow(self.r,2)
    def get_perimeter(self):
        return 2*math.pi*self.r
    
if __name__ == '__main__':
    r = int(input('请输入圆的半径：'))
    c = Circle(r)
    print(f'圆的面积为：{c.get_area()}')
    print(f'圆的周长为：{c.get_perimeter()})
          
  	print('圆的面积为：{:.2f}'.format(c.get_area()))
  	print('圆的周长为：{:.2f}'.format(c.get_perimeter())) 
```

### （2）定义学生类录入5个学生信息存储到列表中

```python
class Student(object):
    def __init__(self,stu_name,stu_age_,stu_gender,stu_score):
        self.stu_name = stu_name
        self.stu_age = stu_age
        self.stu_gender = stu_gender
        self.stu_score = stu_score
        
    def show(self):
        print(self.stu_name,self.stu_age,self.stu_gender,self.stu_score)
        
if __name__ == '__main__':
    print('请输入五位学员的信息：(姓名#年龄#性别#成绩)')
    lst = []
    for i in range(0,5):
        s = input(f'请输入第{i+1}位学员的信息和成绩：')
        s_lst = s.split('#')
        #print(s_lst)
        #创建学生对象
        stu = Student(s_lst[0],int(s_lst[1]),s_lst[2],float(s_lst[3]))
        lst.append(stu)
    #遍历列表
    for item in lst:
        item.show()
```

## 13. 案例十三

### （1）编写程序实现乐手弹奏乐器

```python
class Instrument():
    def make_sound(self):
        pass
    
class Erhu(Instrument):
    def make_sound(self):
        print('二胡在演奏')
class Piano(Instrument):
    def make_sound(self):
        print('钢琴在演奏')
class Violin(Instrument):
    def make_sound(self):
        print('小提琴在演奏')

def play(instrument):
    instrument.make_sound()

class Bird():
    def make_sound(self):
        print('小鸟在唱歌')
        
if __name__ == '__main__':
    play(Erhu())
    play(Piano())
    play(Violin())
```

### （2）请使用面向对象的思想，设计自定义类，描述出租车和家用轿车的信息

```python
class Car(object):
    def __init__(self,type,no):
        self.type = type
        self.no = no
    def start(self):
        pass
    def stop(self):
        pass
    
class Taxi(Car):
    def __init__(self,type,no,company):
        super().__init__(type,no)
        self.company = company
    def start(self):
        print(’乘客您好！)
        print(f'我是{self.company}出租车公司的，我的车牌是{self.no}，请问您要去哪里？')
    def stop(self):
        print('目的地到了，请您付款下车，欢迎再次乘坐。')
        
class FamilyCar(Car):
    def __init__(self,type,no,name):
        super().__init__(type,no)
        self.name = name
    def stop(self):
        print('目的地到了，我们去玩吧')
    def start(self):
        print(f'我是{self.name}，我的汽车我做主')
        
if __name__ == '__main__':
    taxi = Taxi('上海大众','京A9765','长城')
    taxi.start()
    taxi.stop()
    print('-'* 30)
    familycar = FamilyCar('广汽丰田','京B88888','武大郎')
    familycar.start()
    familycar.stop()
    
```

## 14. 案例十四

### （1）模拟高铁售票系统

```python
import prettytable as pt

#显示座席
def show_ticket(row_num):
    tb = pt.PrettyTable()
    tb.field_names = ['行号','座位1','座位2','座位3','座位4','座位5']
    for i in range(row_num):
        lst = [f'第{i+1}行','有票','有票','有票','有票','有票']
        tb.add_row(lst)
    print(tb)
#订票
def order_ticket(row_num,row,column):
    tb = pt.PrettyTable()
    tb.field_names = ['行号','座位1','座位2','座位3','座位4','座位5']
    for i in range(row_num):
        if int(row) == i+1:
            lst = [f'第{i+1}行','有票','有票','有票','有票','有票']
            lst[int(column)] = '已售'
            tb.add_row(lst)
        else:
            lst = [f'第{i+1}行','有票','有票','有票','有票','有票']
            tb.add_row(lst)

if __name__ == '__main__':
    row_num = 13
    show_ticket(row_num)
    choose_num = input('请输入选择的座位，如13,5表示13排5号座位')
    #英文逗号处分隔行与列
    try:
       row,column = choose_num.split(',') 
    except:
        print('输入格式有误，如13排5号座位，应该位13,5')
    order_ticket(row_num,row,column)
```

### （2）推算几天后的日期

```python
import datetime
def inputdate():    
    indate = input('请输入开始日期：{20200202}后按回车')
    indate = indate.strip()
    datestr = indate[0:4] + '-' + indate[4:6] + '-' +indate[6:]
    return datetime.datetime.strptime(datestr,'%Y-%m-%d')

if __name__ == '__main__':
    print('--------------推算几天后的日期---------------------')
    sdate = inputdate()
    in_num = int(input('请输入间隔天数：'))
    fdate = sdate + datetime.timedelta(days = in_num)
    print('您推算的日期是：' + str(fdate))
    print('您推算的日期是：' + str(fdate).split(' ')[0])
```

## 15. 案例十五

### （1）记录用户的登录日志

```python
import time
def show_info():
    print('输入提示数字，执行相应的操作：0.退出  1.查看登录日志')
    
#记录日志
def write_logininfo(username):
    with open('log.txt','a') as file:
        s = f'用户名{username}，登录时间：{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))}'
        file.write(s)
        file.write('\n')

#读取日志
def read_logininfo():
    with open('log.txt','r') as file:
        while True:
            line = file.readlin()
            if line == '':
                break
            else:
               print(line,end = '') 
                        
if __name__ == '__main__':
    username = input('请输入用户名：')
    pwd = input('请输入密码：')
    if 'admin' == username and 'admin' == pwd:
        print('登录成功！')
        write_logininfo(username)
        show_info()
        num = int(input('请输入操作数字'))
        while True:
            if num == 0:
                print('退出成功')
                break
            elif num == 1:
                print('查看登录日志')
                read_logininfo()
                num = int(input('输入操作数字：'))
            else:
                print('您输入的数字有误')
                show_info()
                num = int(input('输入操作数字：'))
    else:
        print('对不起，用户名和密码不正确！')
    
    print(time.time())
    print(time.localtime(time.time()))
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
```

### （2）模拟淘宝客服的自动回复

```python
'''replay.txt文档
订单|如果您有任何订单问题，可以登录淘宝账号，点击“我的订单”，查看订单详情
物流|如果您有任何物流问题，可以登录淘宝账号，点击“我的订单”，查看商品系统
账户|如果您有任何账号问题，可以联系淘宝客服，电话：XXXX-XXXXXX
支付|如果您有任何支付问题，可以联系支付宝客服，QQ：XXXXXXXXX
'''
def find_answer(question):
    with open('replay.txt','r',encoding = 'gbk') as file:
        while True:
            line = file.readline()
            if not line:		#if line ==''到文件末尾退出
                break
            #字符串的分隔
            keyword = line.split('|')[0]
            reply = line.split('|')[1]
            if keyword in question:
                return reply
    return False

if __name__ == '__main__':
    question = input('Hi，您好，小蜜在此等主任很久了，有什么烦恼快和小蜜说吧')
    while True:
        if question == 'bye':
            break
        #开始在文件中查找
        replay = find_answer(question)
        if not replay:		#如果回复的是False，not False则为True
            question = input('小蜜不知道你在说什么，您可以问一些关于订单、物流、账户、支付等问题（退出请输入bye）')
        else:
            print(replay)
            question = input('小主，您还可以问一些关于订单、物流、账户、支付等问题（退出请输入bye')
    print('小主再见')
```

