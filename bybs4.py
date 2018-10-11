
import time              
import re
import urllib   
from bs4 import BeautifulSoup
import urllib.request
import xlwt #EXCEL操作


wbk=xlwt.Workbook()
sheet = wbk.add_sheet('sheet 1')
# indexing is zero based, row then column
sheet.write(0,0,'标题')
sheet.write(0,1,'作者')
sheet.write(0,2,'摘要')


#主函数
if __name__ == '__main__':
    num = 0
    for page in range(1135,1304):
 
        #url = "http://search.cnki.net/Search.aspx?q=python&rank=relevant&cluster=all&val=&p=0"
        url = "http://jcip.cipsc.org.cn/CN/volumn/volumn_"+str(page)+"_abs.shtml"
        content = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(content,"html.parser")
    
        #定位论文摘要
        wz_tab = soup.find_all("table",bgcolor="#f4f4f4")
        for tab in wz_tab:
            num = num+1
            #标题
            title = tab.find("b")
            sheet.write(num,0,title.get_text())
            print(title.get_text())
            #作者
            for idx1, tr in enumerate(tab.find_all('tr')):
                if idx1 == 1:
                    for idx2, td in enumerate(tr.find_all('td')):
                        if idx2 == 2:
                            sheet.write(num,1,td.get_text())
                            print(td.get_text())
            #摘要
                if idx1 == 2:
                    for idx2, td in enumerate(tr.find_all('td')):
                        if idx2 == 2:
                            sheet.write(num,2,td.get_text())
                            print(td.get_text())

wbk.save('S://master//实验室//爬虫//test.xls') 