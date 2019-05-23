# python辅助曲谱变调
笔者最近刚刚接触民乐，深感变调之痛苦，为了可以方便的变调，遂写此脚本，可以方便的比较各调式的相关参数，并输出不同调式的曲谱。

## 使用环境
python 3.6<br>
番茄简谱 V1.0<br>
pandas 0.23.4<br>
numpy 1.13.3<br>
prettytable 0.7.2

## 使用方法
1、制作[调式对照表](https://github.com/jiangangoddog/python-assisted-tone/blob/master/tone.xlsx)，该表有效范围是C大调的超低音#2至超高音#2，足以满足大多数曲子的需求，如有特殊需要，可自行继续补充。<br>
2、打开[番茄简谱](http://jianpu99.net/),按照语法打出曲谱脚本（最麻烦的一步，目前没有发现更好的方法），注意在音符之间要打空格，将该文件命名为[music.txt](https://github.com/jiangangoddog/python-assisted-tone/blob/master/music.txt)。这里以刚刚完结的美剧《权游》插曲《卡斯特梅的雨季》为例。<br>
![番茄简谱](https://github.com/jiangangoddog/python-assisted-tone/blob/master/image/%E7%95%AA%E8%8C%84%E7%AE%80%E8%B0%B1.png)<br>
3、将打好的曲谱复制粘贴进入番茄曲谱编辑器，这一步的主要目的是利用编辑器自带的自动格式化脚本的功能补齐缺失空格，如果确认空格打全，可以省略这一步，也可以上一步偷懒不打空格，这一步自动补齐，在这一步我们可以发现，番茄简谱对于英文标点的支持并不好，这里删去了几乎所有的标点，较为遗憾。<br>
![编辑器界面](https://github.com/jiangangoddog/python-assisted-tone/blob/master/image/123.png)<br>
4、打开脚本[tone.py](https://github.com/jiangangoddog/python-assisted-tone/blob/master/tone.py)，运行，可以看到得出了各种曲调的比较表：<br>
![不同调式的比较](https://github.com/jiangangoddog/python-assisted-tone/blob/master/image/QQ%E6%88%AA%E5%9B%BE20190524001720.png)<br>
5、选择合适的目标调式运行命令<br>
```
output(final_tune='C')
```
可以输出名为[result.txt](https://github.com/jiangangoddog/python-assisted-tone/blob/master/result.txt)的曲谱脚本文件，复制到番茄简谱编辑器中，调整页面，可以输出好看的新调式的简谱。该函数只有一个参数final_tune，默认值是’C'，可选'C', '升C', 'D', '升D', 'E','F','升F', 'G', '升G', 'A', '升A', 'B'中除原调外的曲调。<br>
![The rains of castamere](https://github.com/jiangangoddog/python-assisted-tone/blob/master/image/the rains of castamere.jpg)
