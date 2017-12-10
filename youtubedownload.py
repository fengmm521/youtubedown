#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-09 22:36:40
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os,sys
from pytube import YouTube

reload(sys)
sys.setdefaultencoding( "utf-8" )
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
    cmd = '/usr/local/bin/ffmpeg ffmpeg -i "%s/%s.mp4" -i "audio/%s.mp4" -vcodec copy -acodec copy "%s/%s.mp4"'%(videoType,ptitle,ptitle,outpth,ptitle)
    print cmd
    os.system(cmd)

def downloadWithURL(pURL = 'https://www.youtube.com/watch?v=cmSbXsFE3l8',outpth = 'out'):
    yt = YouTube(pURL)
    alllist = yt.streams.all()
    # for x in alllist:
        # print x
    p1080 = yt.streams.filter(res='1080p', file_extension='mp4').first()
    p720 = yt.streams.filter(res='720p', file_extension='mp4').first()
    abr128k = yt.streams.filter(abr="128kbps", file_extension='mp4').first()
    # print p1080.player_config['args']['title'].encode('utf-8')
    # print abr128k.player_config['args']['title'].encode('utf-8')
    title = ''
    audiopth = ''
    if abr128k:
        # abr128k.player_config['args']['title'] = abr128k.player_config['args']['title'].encode('utf-8')
        abr128k.download('audio')
        audiopth = 'audio/' + abr128k.player_config['args']['title'].encode('utf-8')

    videopth = ''
    if p1080:
        print p1080
        # p1080.player_config['args']['title'] = p1080.player_config['args']['title'].encode('utf-8')
        p1080.download('1080p')
        
        videopth = '1080p/' + p1080.player_config['args']['title'].encode('utf-8')

        title = ''

        makeMoive(p1080.player_config['args']['title'],'1080p',outpth)

    elif p720:
        # p720.player_config['args']['title'] = p1080.player_config['args']['title'].encode('utf-8')
        p720.download('720p')

        videopth = '720p/' + p720.player_config['args']['title'].encode('utf-8')

        makeMoive(p720.player_config['args']['title'].encode('utf-8'),'720p',outpth)

    os.remove(audiopth)
    os.remove(videopth)

def main(args):
    turl = ''
    if len(args) == 2 :
        turl = args[1]
        print turl
        downloadWithURL(turl)
    elif len(args) == 3:
        turl = args[1]
        outpth = args[2]
        print turl
        print outpth
        downloadWithURL(turl,outpth)
    else:
        print "未输入要下载的视频URL地址,参考下边样式输入参数来下载:\n"
        print 'python youtubedownload.py 要下载的视频地址'
        print '或者:'
        print 'python youtubedownload.py 要下载的视频地址 输出的视频目录'

if __name__ == '__main__':
    main(sys.argv)
    # downloadWithURL()
    
