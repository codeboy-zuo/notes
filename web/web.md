```html
<!-- 基本框架 -->

<!DOCTYPE html>		<!-- 声明为HTML5文档  html不分大小写 -->
<html>
    <head>		<!-- 头部元素  可以添加在头部区域的元素标签为<title>, <style>, <meta>, <link>, <script>, <noscript> 和 <base>-->
        <meta charset='utf-8'>
        <title>网站页面标题</title>
        <base href="http://www.runoob.com/images/" target="_blank">	    <!-- <base>定义了所有链接的URL -->
        <style type="text/css">
        body {background-color: rgb(188, 195, 192);}
        h1 {color: red;}
        p {color: blue;}
        </style>        <!-- <style>定义了HTML文档的样式文件 -->
    </head>
    <body>			<!-- 可见的页面内容，即用来显示给用户 -->	
        <h1>第一个标题</h1>
        <p>第一个段落</p>
        <hr>   		<!-- 绘制分割线 -->
        <p>第二个段落</p>
        <p style="background-color:blueviolet;margin-left:20px;">这是一个有背景颜色的段落,左边距为20</p>
        <a href="http://www.baidu.com">这是一个连接,使用了href属性</a><br/>      <!-- html链接  通过<a>来定义 -->
        <a href="http://www.baidu.com" target="_top">点击这里跳转</a><br/>       <!-- 跳出框架 直指百度-->
        <a href="http://www.baidu.com" style="text-decoration:none;">这是一个没有下划线的百度链接</a>
        <br/>        <!-- 换行 -->
        <img src="D:\Desktop\微信开发\樱花.jpg" width="144" height="144"/><br/>      <!-- html图像  通过img来定义 -->
        <b>加粗文本</b><br/>     <!-- bold 粗体-->
        <i>斜体文本</i><br/>     <!-- italic 斜体-->
        <em>定义着重文本</em>
        <code>电脑自动输出</code><br/>
        <sub>下标</sub>和<sup>上标</sup><br/>
        <script>    
            document.write("hello world!")
        </script>   <!--定义了客户端脚本-->
    </body>
</html>

```

[菜鸟教程]: https://www.runoob.com/html/html-quicklist.html

```html
<!--表单-->

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>创建表单</title>
    </head>
    <body>
        
        <form action="">
            First name: <input type="text" name="firstname"><br/>   <!-- 文本域用 type="text"-->
            Last  name: <input type="text" name="lastname"><br/>

            Username:<input type="text" name="user"><br/>
            Password:<input type="password" name="password">    <!-- 密码字段用 type="password"-->
            <input type="submit" value="submit"><br/>       <!-- 创建提交按钮(submit button)-->

            <input type="radio" name="sex" value="male">Male<br/>   <!-- 单选按钮(Radio Buttons) -->
            <input type="radio" name="sex" value="female">Female<br/>

            <input type="checkbox" name="vehicle" value="bike">Bike<br/>  <!-- 复选框(Checkboxes)-->
            <input type="checkbox" name="vehicle" value="bus">Bus<br/>
            <input type="button" value="提交"><br>      <!-- 创建按钮(button)-->
        </form>
        <button type="button" onclick="alert('hello word!')">点击这里</button>  <!-- 创建按钮(button)-->
    </body>
</html>

```

```html
<!--定位页面的具体位置
# 包含了一个位置信息，默认的锚是#top 也就是网页的上端。
在页面很长的时候会使用 # 来定位页面的具体位置，格式为：# + id-->
<a href="#pos">点我定位到指定位置!</a><br>
<a href="#top">点我定位到顶部!</a>
<br>
...
<br>
<p id="pos">尾部定位点</p>
```

