youtube down
==========

#一个下载mtv的工具

##pytube库安装

首先使用pip安装pytube库.
pip install pytube --user
可参考:
https://pypi.python.org/pypi/pytube/

##音视频文件合并
下载高清的1080p视频时是没有声音的，可以使用ffmpeg工具的下边方法把音视频合并为一个文件：
```
ffmpeg -i 视频路径 -i 音频路径 -vcodec copy -acodec copy 合成后输出的路径
```
其中输出和输入文件编码格式由上边各种路径文件后缀来确定文件格式
音视频转码以及合成参考：
http://blog.csdn.net/jinzheng069/article/details/9252653