# coding:utf-8
import urllib
import urllib2
import re
class MaoYan:
    def crawl(self):
        urls = ['http://piaofang.maoyan.com/dayoffice?date=2016-12-15&cnt=10',
                'http://piaofang.maoyan.com/dayoffice?date=2016-12-14&cnt=10',
                'http://piaofang.maoyan.com/dayoffice?date=2016-12-13&cnt=10',
                'http://piaofang.maoyan.com/dayoffice?date=2016-12-12&cnt=10',
                'http://piaofang.maoyan.com/dayoffice?date=2016-12-11&cnt=10']
        for url in urls:
            date = url.replace('http://piaofang.maoyan.com/dayoffice?date=','').replace('&cnt=10','')
            request = urllib2.Request(url)
            request.add_header('Host','piaofang.maoyan.com')
            request.add_header('Referer', url.replace('dayoffice',''))
            request.add_header('Uid','9b0e57b0f889ec0eefbde184d4ea6674bcb762db')
            request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0')
            request.add_header('X-Requested-With', 'XMLHttpRequest')
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            content = content.replace('\\n','').replace('\\','')
            infos = content.split('<li class=\'c1\'>')
            print '----------------------'+date+'票房--------------------'
            for index in range(len(infos)):
               if index>0:
                    info = infos[index]
                    pattern = re.compile('<b>(.*?)</b>.*?<br><em>(.*?)</em><em style="margin-left: .1rem">(.*?)</em>.*?</li>.*?'+
                                         '<li class="c2 ">.*?<b>(.*?)</b><br/>.*?</li>.*?<li class="c3 ">(.*?)</li>.*?<li class="c4 ">(.*?)</li>'+
                                         '.*?<li class="c5 ">.*?<span style="margin-right:-.1rem">(.*?)</span>',re.S)
                    items = re.findall(pattern, info)
                    for item in items:
                        print item[0]+'\t'+item[1]+'\t'+item[2]+'\t'+item[3]+'\t'+item[4].strip()+'\t'+item[5].strip()+'\t'+item[6].strip()
m = MaoYan()
m.crawl()