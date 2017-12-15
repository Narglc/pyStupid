
### Jupyter Notebook 的使用

**命令行模式**与**代码模式**   **切换**

+ Esc   命令行模式
+ Enter  编辑模式

**Markdown**与**Code**

+ y  code
+ m  markdown

**代码运行**

+ Ctrl+Enter  只在当前cell运行
+ Shift+Enter  运行并插入下一个cell
 
**新建一个cell**

+ b   在下方插入一个cell
+ a   在上方插入一个cell

**复制 粘贴Cell**

* c       复制选中的cell
* v       在下方粘贴
* shift+v   在上方粘贴

**删除Cell**

+ x       删除选中cell
+ dd      删除当前cell

***
### Markdown的使用

###### 标题标志：

一级标题
====
二级标题
------
或使用#号标志表示1-6级标题


**粗体**   两个\* 或  两个\_      
__Bold__

*斜体*    单个\* 或  单个\_    
_Italic_

~~delete~~   两个\~  

### 超链接
http://www.baidu.com  <br/>
**行内式**  [百度](http://www.baidu.com)  
**参考式**   引用的文段[百度][1]  
以下链接可以放到文章末尾 
[1]:http://www.baidu.com


###### 列表
有序列表：   
1. 苹果  
2. 香蕉  
4. 菠萝  

例外：   
1989\. 不采用列表的格式原样打印出。

无序列表：  +-\*    
* aaa  
* bbb  
* ccc  

###### 引用
>这是一级引用
>>这是二级引用
>>>这是三级引用

###### 表格  
|姓名|性别|年龄|  
|-|-|-|    
|nar|M|66|    

> 当然也可以使用HTML中的表格语言来组成表格。



***
#### Jupyter的各种快捷键

执行当前cell，并自动跳到下一个cell：Shift Enter

执行当前cell，执行后不自动调转到下一个cell：Ctrl-Enter

是当前的cell进入编辑模式：Enter

退出当前cell的编辑模式：Esc

删除当前的cell：双D

为当前的cell加入line number：单L

将当前的cell转化为具有一级标题的maskdown：单1

将当前的cell转化为具有二级标题的maskdown：单2

将当前的cell转化为具有三级标题的maskdown：单3

为一行或者多行添加/取消注释：Crtl /

撤销对某个cell的删除：z

浏览器的各个Tab之间切换：Crtl PgUp和Crtl PgDn

快速跳转到首个cell：Crtl Home

快速跳转到最后一个cell：Crtl End

### 将本地的.py文件load到jupyter的一个cell中

%load test.py  #test.py是当前路径下的一个python文件

### Jupyter运行python文件

%run file.py



***
**HTML语言的使用**

Lovely Kid
<img src="kid.jpg">

**尝试在Markdown模式下使用LaTeX输入公式：**  
使用$将公式包起来，  
当使用:    

* 单个$号时，公式居左   
* 两个$号时，公式居中

Use $$ if you want your math to appear in a single line, e.g.,    **想让公式单独占一行**

$$a = b + c$$ (line break after the equation)

If you don't need a line break after the math, use single dollar sign $, e.g.,  **想让公式插入到某一行中**

$a = b + c$   (no line break after the equation)

$$x^2$$
$$E=mc^2 \
y_1=x_1+x_2^2
$$

$\sqrt{3x-1}+(1+x)^2$

$$ P(A \mid B) = \frac{P(B \mid A) , P(A)}{P(B)} $$

$$f(x_1,x_x,\ldots,x_n) = x_1^2 + x_2^2 + \cdots + x_n^2 $$


```python
from IPython.display import display, Math, Latex
display(Math(r'F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx'))b
```


$$F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx$$


$$c = \sqrt{a^2 + b^2}$$

$$\left. \frac{du}{dx} \right|_{x=0}.$$

#### Magic Fuction：


```python
!python --version
```

    Python 2.7.10
    


```python
!python stupid_BeautifulSoup.py
```

         Hello World     This is link1     This is link2  
    <a class="link" href="#">This is link1</a>
    [<a class="link" href="#">This is link1</a>, <a class="link" href="# link2">This is link2</a>]
    


```python
%run stupid_BeautifulSoup.py
```

         Hello World     This is link1     This is link2  
    <a class="link" href="#">This is link1</a>
    [<a class="link" href="#">This is link1</a>, <a class="link" href="# link2">This is link2</a>]
    


```python
current_path = %pwd
print current_path
```

    F:\Jupyter Notebook
    


```python
# %load stupid_BeautifulSoup.py
from bs4 import BeautifulSoup
html_sample = '\
<html> \
  <body> \
    <h1 id="title">Hello World</h1> \
    <a href="#" class="link">This is link1</a> \
    <a href="# link2" class="link">This is link2</a>\
  <body>\
<html>'

soup = BeautifulSoup(html_sample,"html5lib")
print soup.text                     #不含tab的内容
# print '====='
# print soup.contents                 #全部内容
print soup.select('a')[0]
print soup.select('.link')            #class  :   .link
# print soup.select('#title')           #id :   #title
# print ""

```

         Hello World     This is link1     This is link2  
    <a class="link" href="#">This is link1</a>
    [<a class="link" href="#">This is link1</a>, <a class="link" href="# link2">This is link2</a>]
    


