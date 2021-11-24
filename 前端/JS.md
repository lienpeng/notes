js一般放在header标签中
或者单独的.js文件，通过<script src = ""></script>引用

数据类型
1. Number
123;0.456;-99;NaN(无法计算);Infinity(无限大)
% 取余
Ox 前缀的十六进制
2. 字符串 '' ""
多行字符串使用``
var name = "lee";
var message = 'hello,${name}'
字符串是不可变的，如果对字符串的某个索引赋值，不会有任何错误，但是，也没有任何效果：
var s = 'Test';
s[0] = 'X';
alert(s); // s仍然为'Test'
常用方法：length toUpperCase toLowerCase indexOf substring
3. 布尔值 true false
'==='会比较数据类型，强比较
NaN === NaN //false,NaN与所有Number都不相等
isNaN(NaN)//true 唯一判断是不是NaN的方法
浮点数计算误差问题，导致1/3和（1-2/3）不相等，只能通过差的绝对值判断

4. null 表示空，大多数情况下，我们都应该用null。undefined仅仅在判断函数参数是否传递的情况下有用。
5. 数组
[1，2，3] 或者 new Array(1,2,3)创建
6. 对象
var person = {}
7. 变量
var 语句不是全局变量，范围限制在申明的函数体里面。
变量名是大小写英文、数字、$和_的组合
