1. 超文本概念
   - 纯文本 只能保存文本内容
   - 超【超链接】文本标记【标签】语言

2. 主体标签/元素
   - html标签 根标签 有且只有一个
     - head 内容不会展示在网页中
       - title 浏览器标题栏，搜索引擎在检索页面时，会首先检索title标签
       - meta `<meta chaset="utf-8">`
         1. 字符集 charset 编码和解码采用的规则
            - ASCII 7位 128个字符
            - GB2312 【国标】
            - GBK 
            - UTF-8 【万国码】
     - body
3. 注释 `<!--  这是注释 -->`
4. 文档说明 doctype
   - 用来告诉浏览区当前网页的版本
   - `<!doctype html>` 【html不区分大小写】
5. 标签属性
   - 结构  属性值:"属性值"
6. 实体【转义字符】
   - 语法 &实体名字;
   - 多个连续的空格会被认为是一个空格 可以使用`&nbsp;`来代替 
 - `&lt;` `&gt;`
7. 标签
- meta
  - charset
  - name 指定数据的名称
  - content 指定数据的内容
    - 常用数据 keywords 表示网站的关键字
    - description 用于网站描述 在搜索引擎的结果中展示
    - 网页重定向 `<meta http-equiv="refresh" content="3; url=http://example.com">`
- 标题标签 h 6级标题
  - 标识文件的重要程度 给搜索引擎检索用，一般网页中h1最好只有一个
  - 块级标签
  - hgroup标签用于标题组
- 段落 p 块级标签
- em 用于语气的加重 斜体
- strong 表示重要
- br 换行
1. 技巧 
   - 离线文档查询 zeal
   - vscode插件 live server