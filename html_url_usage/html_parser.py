from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request


def getHTML(url):
    req=request.Request(url)
    with request.urlopen(req) as f:
        return f.read().decode('utf-8')
    print(f.read())

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser,self).__init__()
        self._events={}
        self._counter=0 #用于记录条目数量
        self._tag=''

    def handle_starttag(self,tag,attrs):
        #attrs like {{'class','event-title'}}
        if tag=='h3' and attrs and attrs[0][0]=='class' and attrs[0][1]=='event-title':
            self._tag='title'
        if tag=='time' and attrs and attrs[0][0]=='datetime':
            self._tag='datetime'
        if tag=='span' and attrs and attrs[0][0]=='class' and attrs[0][1]=='event-location':
           self._tag='location'

    def handle_data(self,data):
        if self._tag=='title':
            self._events[self._counter]={'title':data}
        if self._tag=='datetime':
            self._events[self._counter]['datetime']=data
        if self._tag=='location':
            self._events[self._counter]['location']=data
            self._counter+=1
        self._tag=''
    
    def printEvents(self):
        for k in self._events:
            print('[title]:%s [datetime]:%s [location]:%s'%(self._events[k]['title'],self._events[k]['datetime'],self._events[k]['location'])) 




if __name__=='__main__':
    parser=MyHTMLParser()
    parser.feed(getHTML('https://www.python.org/events/python-events/'))
    parser.printEvents()









        
    
