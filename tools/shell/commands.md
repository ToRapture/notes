## grep
`$ grep -irn 'main' .`
`$ grep -irl 'main' .`

  -i 忽略字符大小写的差别
  
  -v 反转查找
  
  -n 在显示符合范本样式的那一列之前，标示出该列的编号
  
  -R/-r 此参数的效果和指定"-d recurse"参数相同
  
  -w 只显示全字符合的列
  
  -l 列出文件内容符合指定的范本样式的文件名称
  
  -L 列出文件内容不符合指定的范本样式的文件名称
  
  -a 不要忽略二进制数据
  
  -c 计算符合范本样式的列数
  
  -e <范本样式> 指定字符串作为查找文件内容的范本样式
  
  -h 在显示符合范本样式的那一列之前，不标示该列所属的文件名称
  
  -H 在显示符合范本样式的那一列之前，标示该列的文件名称
  
  -o 只输出文件中匹配到的部分
  
  -A <显示列数> 除了显示符合范本样式的那一行之外，并显示该行之后的内容
  
  -B <显示列数> 除了显示符合范本样式的那一行之外，并显示该行之前的内容
  
  -C <显示列数>或-<显示列数>  除了显示符合范本样式的那一列之外，并显示该列之前后的内容

## find
`$ find . -maxdepth 3 -name "[A-Z]*"`
在当前目录中递归查找文件名以一个大写字母开头的文件

## sed
`$ sed -n '5,10p' filename`
只查看文件的第5行到第10行

## tail
`$ tail -f app.log`
循环读取app.log的更新

## source
`$ source file_name`
在当前bash环境下读取并执行file_name中的命令

## sort
  -n 依照数值的大小排序
  
  -f 排序时，将小写字母视为大写字母
  
  -r 以相反的顺序来排序
  
  -M 将前面3个字母依照月份的缩写进行排序
  
  -b 忽略每行前面开始出的空格字符
  
  -c 检查文件是否已经按照顺序排序
  
  -d 排序时，处理英文字母、数字及空格字符外，忽略其他的字符
  

```
$ cat aqours
27015
114115
2333 very small
Start Dash
さようなら！
who are you

$ sort aqours
114115
2333 very small
27015
Start Dash
who are you
さようなら！

$ sort -n aqours
Start Dash
who are you
さようなら！
2333 very small
27015
114115

$ sort -nr aqours
114115
27015
2333 very small
さようなら！
who are you
Start Dash

$ cat aqours
hello
WORLD
$ sort aqours
WORLD
hello
$ sort -f aqours
hello
WORLD

$ sort -c aqours 2>/dev/null; echo "exit code: $?"
exit code: 1
$ sort aqours | sort -c 2>/dev/null; echo "exit code: $?"
exit code: 0
$ sort aqours | sort -cr 2>/dev/null; echo "exit code: $?"
exit code: 1
$ sort -r aqours | sort -cr 2>/dev/null; echo "exit code: $?"
exit code: 0

$ cat aqours
February
January
April
March
$ sort -M aqours
January
February
March
April
```

## crontab
```
$ crontab -l
crontab: no crontab for torapture
$ echo "* * * * * ls ~ > ~/crontab_test" | crontab
$ crontab -l
* * * * * ls ~ > ~/crontab_test
$ sleep 60
$ ls | grep crontab_test
crontab_test
$ cat crontab_test
Applications
Codes
Desktop
Documents
Downloads
Files
Games
Library
Movies
Music
Pictures
Public
Tools
Virtual
Work
crontab_test

$ crontab -r && crontab -l
crontab: no crontab for torapture
```

## tmux
```
$ tmux
$ tmux a
[^b $ {session-name}] 重命名当前会话
[^b s] 选择会话列表
[^b d] detach 当前会话
$ tmux a -t {session-name}
[^b %] 左右平分
[^b "] 上下平分
[^b z] 最大化当前窗格
[^b q] 显示所有窗格的序号
```
