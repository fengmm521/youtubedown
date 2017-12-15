#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-09 22:36:40
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os,sys
from pytube import YouTube

# print sys.path.append('/usr/local/Cellar')

reload(sys)
sys.setdefaultencoding( "utf-8" )


#获取脚本路径
def cur_file_dir():
    pathx = sys.argv[0]
    tmppath,_file = os.path.split(pathx)
    if cmp(tmppath,'') == 0:
        tmppath = sys.path[0]
    #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(tmppath):
        return tmppath
    elif os.path.isfile(tmppath):
        return os.path.dirname(tmppath)
    
#获取父目录
def GetParentPath(strPath):
    if not strPath:
        return None;
    lsPath = os.path.split(strPath);
    if lsPath[1]:
        return lsPath[0];
    lsPath = os.path.split(lsPath[0]);
    return lsPath[0];

#获取目录下的所有类型文件
def getAllExtFile(pth,fromatx = ".mp4"):
    jsondir = pth
    jsonfilelist = []
    for root, _dirs, files in os.walk(jsondir):
        for filex in files:          
            #print filex
            name,text = os.path.splitext(filex)
            if cmp(text,fromatx) == 0:
                jsonArr = []
                rootdir = pth
                dirx = root[len(rootdir):]
                pathName = dirx +os.sep + filex
                jsonArr.append(pathName)
                (newPath,_name) = os.path.split(pathName)
                jsonArr.append(newPath)
                jsonArr.append(name)
                jsonfilelist.append(jsonArr)
            elif fromatx == ".*" :
                jsonArr = []
                rootdir = pth
                dirx = root[len(rootdir):]
                pathName = dirx +os.sep + filex
                jsonArr.append(pathName)
                (newPath,_name) = os.path.split(pathName)
                jsonArr.append(newPath)
                jsonArr.append(name)
                jsonfilelist.append(jsonArr)
    return jsonfilelist


    # def filter(
    #         self, fps=None, res=None, resolution=None, mime_type=None,
    #         type=None, subtype=None, file_extension=None, abr=None,
    #         bitrate=None, video_codec=None, audio_codec=None,
    #         only_audio=None, only_video=None,
    #         progressive=None, adaptive=None,
    #         custom_filter_functions=None,
    # ):


# <Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2">
# <Stream: itag="43" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp8.0" acodec="vorbis">
# <Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2">
# <Stream: itag="36" mime_type="video/3gpp" res="240p" fps="30fps" vcodec="mp4v.20.3" acodec="mp4a.40.2">
# <Stream: itag="17" mime_type="video/3gpp" res="144p" fps="30fps" vcodec="mp4v.20.3" acodec="mp4a.40.2">
# <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028">
# <Stream: itag="248" mime_type="video/webm" res="1080p" fps="30fps" vcodec="vp9">
# <Stream: itag="136" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.4d401f">
# <Stream: itag="247" mime_type="video/webm" res="720p" fps="30fps" vcodec="vp9">
# <Stream: itag="135" mime_type="video/mp4" res="480p" fps="30fps" vcodec="avc1.4d401e">
# <Stream: itag="244" mime_type="video/webm" res="480p" fps="30fps" vcodec="vp9">
# <Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e">
# <Stream: itag="243" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp9">
# <Stream: itag="133" mime_type="video/mp4" res="240p" fps="30fps" vcodec="avc1.4d4015">
# <Stream: itag="242" mime_type="video/webm" res="240p" fps="30fps" vcodec="vp9">
# <Stream: itag="160" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.4d400c">
# <Stream: itag="278" mime_type="video/webm" res="144p" fps="30fps" vcodec="vp9">
# <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2">
# <Stream: itag="171" mime_type="audio/webm" abr="128kbps" acodec="vorbis">
# <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus">
# <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus">
# <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus">

def makeMoive(ptitle,videoType = '1080p',outpth = 'out'):

    if not os.path.exists('tmp'):
        os.mkdir('tmp')

    if (not os.path.exists('out')) and outpth == 'out':
        os.mkdir('out')
        
    # savename = ptitle.replace('"','').replace("'","").replace('“','').replace('”', '').replace('’', '')
    cmd = u'/usr/local/bin/ffmpeg -i "%s/video.mp4" -i "audio/audio.mp4" -vcodec copy -acodec copy "tmp/output.mp4"'%(videoType)
    print cmd
    os.system(cmd)

    cmd = 'mv "tmp/output.mp4" "%s/%s.mp4"'%(outpth,ptitle)
    print cmd
    os.system(cmd)

    if os.path.exists('tmp/output.mp4'):
        os.remove('tmp/output.mp4')

        

def isHeaveMp4File(title,savepth):
    fs = getAllExtFile(savepth)
    for f in fs:
        if f[2].find(title) != -1:
            return True
    return False


def isHeaveMp4FileInMTVDir(title):
    fs = getAllExtFile('/Volumes/mage/moive/mtv')
    for f in fs:
        if f[2].find(title) != -1:
            return True
    return False

def downloadWithURL(pURL = 'https://www.youtube.com/watch?v=cmSbXsFE3l8',outpth = 'out'):
    yt = YouTube(pURL)
    alllist = yt.streams.all()
    # for x in alllist:
        # print x

    p1080 = yt.streams.filter(res='1080p', file_extension='mp4').first()
    p720 = yt.streams.filter(res='720p', file_extension='mp4').first()
    p480 = yt.streams.filter(res='480p', file_extension='mp4').first()
    p360 = yt.streams.filter(res='360p', file_extension='mp4').first()
    p240 = yt.streams.filter(res='240p', file_extension='mp4').first()
    p144 = yt.streams.filter(res='144p', file_extension='mp4').first()


    abr128k = yt.streams.filter(abr="128kbps", file_extension='mp4').first()

    # print p1080.player_config['args']['title'].encode('utf-8')
    # print abr128k.player_config['args']['title'].encode('utf-8')
    title = ''
    audiopth = ''

    if abr128k:
        # abr128k.player_config['args']['title'] = abr128k.player_config['args']['title'].encode('utf-8')
        # 
        if not os.path.exists('audio'):
            os.mkdir('audio')

        
        audiopth = 'audio/audio.mp4'

        title = abr128k.player_config['args']['title'].encode('utf-8')

        if isHeaveMp4File(title, outpth):
            print '(%s) title is heave in %s'%(title,outpth)
            return
        if isHeaveMp4FileInMTVDir(title):
            print '(%s) title is heave in MTV dir(/Volumes/mage/moive/mtv)'%(title)
            return

        try:
            abr128k.player_config['args']['title'] = 'audio'

            print 'title:',title

            print 'start downloading audio 128k...'

            abr128k.download('audio')

        except Exception as e:

            print 'download 128 erro,and redownload with other mp4 type'

            abr128k = yt.streams.filter(mime_type="audio/mp4", file_extension='mp4').first()

            abr128k.player_config['args']['title'] = 'audio'

            print 'start downloading audio other mp4 type ...'

            abr128k.download('audio')
        
        
    videopth = ''
    if p1080:
        if not os.path.exists('1080p'):
            os.mkdir('1080p')
        print 'start downloading video 1080p...'
        
        title +='_1080p'

        p1080.player_config['args']['title'] = 'video'

        videopth = '1080p/video.mp4'

        p1080.download('1080p')

        makeMoive(title,'1080p',outpth)

    elif p720:
        if not os.path.exists('720p'):
            os.mkdir('720p')
        print 'start downloading video 720p...'

        title +='_720p'

        p720.player_config['args']['title'] = 'video'

        videopth = '720p/video.mp4'

        p720.download('720p')
        
        makeMoive(title,'720p',outpth)
    elif p480:
        if not os.path.exists('480p'):
            os.mkdir('480p')
        print 'start downloading video 480p...'

        title +='_480p'

        p480.player_config['args']['title'] = 'video'

        videopth = '480p/video.mp4'

        p480.download('480p')
        
        makeMoive(title,'480p',outpth)
    elif p360:
        if not os.path.exists('360p'):
            os.mkdir('360p')
        print 'start downloading video 360p...'

        title +='_360p'

        p360.player_config['args']['title'] = 'video'

        videopth = '360p/video.mp4'

        p360.download('360p')
        
        makeMoive(title,'360p',outpth)
    elif p240:
        if not os.path.exists('240p'):
            os.mkdir('240p')
        print 'start downloading video 240p...'

        title +='_240p'

        p240.player_config['args']['title'] = 'video'

        videopth = '240p/video.mp4'

        p240.download('240p')
        
        makeMoive(title,'240p',outpth)
    elif p144:
        if not os.path.exists('144p'):
            os.mkdir('144p')
        print 'start downloading video 144p...'

        title +='_144p'

        p144.player_config['args']['title'] = 'video'

        videopth = '144p/video.mp4'

        p144.download('144p')
        
        makeMoive(title,'144p',outpth)
    else:
        print 'not video'

    print audiopth
    print videopth

    if os.path.exists(audiopth):
        os.remove(audiopth)
    if os.path.exists(videopth):
        os.remove(videopth)


#下载一个文件中的所有视频,每一个视频地址一行
def downLoadWithList(turlsFilePth,outpth = 'out'):
    if not os.path.exists(turlsFilePth):
        print '下载视频地址列表文件错误.查看是否存在文件:%s'%(turlsFilePth)
        return
    f = open(turlsFilePth,'r')
    lines = f.readlines()
    f.close()

    turls = []
    for l in lines:
        ltmp = l.replace('\r','')
        ltmp = ltmp.replace('\n','')
        if len(ltmp) > 10 and (ltmp[:7] == 'http://' or ltmp[:8]) == 'https://':
            print ltmp
            turls.append(ltmp)
    count = len(turls)
    downcount = 0
    for u in turls:
        downcount += 1
        print 'strat downloading %d/%d'%(downcount,count)
        print u
        downloadWithURL(u,outpth)

def main(args):
    turl = ''
    if len(args) == 2 :
        turl = args[1]
        print turl
        if turl[:7] == 'http://' or turl[:8] == 'https://':
            downloadWithURL(turl)
        elif turl[-4:] == '.txt':
            downLoadWithList(turl)
        
    elif len(args) == 3:
        turl = args[1]
        outpth = args[2]
        print turl
        print outpth
        if turl[:7] == 'http://' or turl[:8] == 'https://':
            downloadWithURL(turl,outpth)
        elif turl[-4:] == '.txt':
            downLoadWithList(turl,outpth)
    else:
        print "未输入要下载的视频URL地址,参考下边样式输入参数来下载:\n"
        print 'python youtubedownload.py 要下载的视频地址'
        print '或者:'
        print 'python youtubedownload.py 要下载的视频地址 输出的视频目录'

if __name__ == '__main__':
    main(sys.argv)
    # downloadWithURL()
    # makeMoive(u'Anna Kendrick - Cups (Pitch Perfect’s “When I’m Gone”)','1080p','out')
    
