

import  urllib2


url = 'http://mobile.cfda.gov.cn/datasearch/QueryList?pageIndex=1&pageSize=1&tableId=26'
html = urllib2.urlopen(url).read()
print html.decode("gbk").encode("utf-8")