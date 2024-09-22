## 文件名

```
1：文档类型
	d：目录    
	-：文件    
	l：链接文档
	b：装置文件里面的可供存储的接口设备（可随机存取装置）
	c：装置文件里面的串行端口设备:键盘、鼠标等一次性读取装置
	
	数字类型改变权限：
	【-rwxrwxrwx】9个权限三个三个一组  
	各权限分数 r：4   w：2   x：1   如上为 777
	注：w 权限可以让使用者删除、更新、新建文件和目录
	
2：/usr/share/doc/       存放一些说明文件

3：/etc/shadow     保存用户password信息
	format：用户名：加密密码：最后一次修改时间：最小修改时间间隔：密码有效期：密码需要变更前的警告天数：密码过期后的宽限时间：账号失效时间：保留字段        注：时间是从1970.1.1开始计算

4：常见目录及说明
/etc/：几乎系统的所有配置文件案均在此，尤其 passwd,shadow
/boot：开机配置文件，也是预设摆放核心vmlinuz的地方
/usr/bin, /bin：一般执行档摆放的地方
/usr/sbin,/sbin：系统管理员常用指令集
/dev：摆放所有系统装置文件的目录
/var/log：摆放系统注册表文件的地方
/run：CentOS7以后才有，将经常变动的项目(每次开机都不同，如程序的PID)移动到内存暂存，所以/run并不占实际磁盘容量
```

## 常用命令

1. 文件操作

   ```
   sync：将数据同步写入硬盘中，常用在即将关机时输入保存数据
   
   mkdir：创建目录
   touch：新建文件
   mv：移动文件或目录
   cp：复制文件或目录
   rm：删除文件或目录
   zip：压缩文件
   unzip：解压文件
   
   ./file_name  执行shell脚本文件
   
   文件查看命令：
   
       cat：查看文件内容（第一行开始）   
       tac：从最后一行开始显示内容
       nl：显示的时候，顺便输出行号
       more：一页一页显示文件内容
       less：与more类似，可以往前翻页
       head：查看文件开头内容
       tail：查看文件结尾内容
       od：以二进制的方式读取文件内容
       
   grep、sed、awk：灵活查找和处理文件内容
   
   ```

2. 查看系统信息

   ```
   ps -aux  查看进程及资源占用
   top		查看实时进程及资源占用情况
   ps		查看进程信息
   free	查看内存占用情况
   df		查看磁盘占用情况
   netstat	查看网络状态信息
   ```

3. 用户权限

   ```
   useradd：添加用户
   userdel：删除用户
   
   chgrp：改变文件所属群组
   chown：改变文件拥有者
   chomd：改变文件权限
   
   chattr：添加文件隐藏属性    如 chattr +i 导致文件无法删除改名写入等等
   lsattr：显示文件隐藏属性
   ```

4. 其它

   ```
   1、od：可以将date file或者是binary file的内容读出
   	例如：将passwd这几个字符的ASCLL打印出来  输入命令 echo passwd | od -t oCc 即可
   
   2、umask：可修改touch创建文件以及mkdir创建目录时的默认权限
   	例如：输入umask   得到0002 表示创建的文件默认权限为-rw-rw-r--  目录权限为drwxrwxr-x
   		修改默认权限例如： umask 0022     则文件权限为-rw-r--r--  目录权限为drwxr-xr-x
   	注：只看后面三个数如022 代表user没有拿掉任何权限，group和other拿掉了2即（w）
   		文件默认没有x权限，目录默认有x
   ```

## Linux服务器

### 端口开放

1. 开启防火墙

   ```
   systemctl start firewalld
   ```

2. 开放指定端口

   ```
   firewall-cmd --zone=public --add-port=4000/tcp --permanent
   
   或者直接：ufw allow 8000/tcp (适用Ubuntu/Debian等)
   ```

3. 重启防火墙

   ```
   firewall-cmd --reload
   ```

4. 查看端口号

   ```
   # 查看当前所有tcp端口
   netstat -ntlp
   
   # 查看4000端口使用情况
   netstat -ntulp | grep 4000
   ```

### 查看域名解析所使用的服务器

```
# 安装blind9-dnsutils
sudo apt update
sudo apt install bind9-dnsutils
nslookup domain.com ## 也可直接在Windows的cmd输入此命令查看
```

