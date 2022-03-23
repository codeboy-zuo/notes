`turtle.screensize(canvwidth=None, canvheight=None, bg=None)   # 参数为画布宽、高、背景色`

`turtle.pensize(5)   	      # 设置画笔大小`
`turtle.pencolor('red')  	# 设置画笔颜色`
`turtle.speed()   		     # 设置画笔移动速度`
`turtle.title()		# 设置标题`

`turtle.forward(distance)  	# 当前画笔方向移动distance像素长度`
`turtle.backward(distance)  	# 当前画笔反方向移动distance像素长度`
`turtle.right(degree)	# 顺时针移动degree°`
`turtle.left(degree)		# 逆时针……`
`turtle.circle(100)# 画圆，半径为正(负),画笔左边(右))画圆 。参数r、弧度、内切多边形边数(steps)`
`turtle.circle(50,180)	# 半圆`
`turtle.circle(50,steps=4)	#  半径为50的圆内切四边形(正方形)`

`turtle.penup()		# 提起画笔`
`turtle.pendown()	# 放下画笔`
`turtle.goto(x,y)	# 将画笔移动到(x,y)坐标`
`turtle.fillcolor()	# 填充颜色`
`turtle.color(color1,color2)    # 设置pencolor(color1)和fillcolor(color2), 若颜色相同填一个即可`
`turtle.begin_fill()		# 开始填充`
`turtle.end_fill()		# 填充完成`
`turtle.write("text",align='center',font=("宋体",12,"normal"))	# 文本输入` 
`turtle.delay(delay=None)	# 设置或返回以ms为单位的延迟`
`turtle.hideturtle()		# 隐藏画笔  ，showturtle()显示画笔`
`turtle.mode(mode=None)# 默认为standard模式：方向东,正角度(逆); logo模式:方向北，角度顺`

`setx()		# 将当前x轴移动到指定位置`
`sety()		# 将当前y轴移动到指定位置`
`home()		# 设置当前画笔位置为原点，方向东`
`dot(r)		# 绘制指定直径和颜色的圆点`
`setheading(angle)	# 设置当前朝向为angle角度`

`turtle.done()`
`turtle.mainloop()	# 启动事件循环`
