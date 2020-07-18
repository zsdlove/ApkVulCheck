# -- coding:utf-8 --

import requests
import random
import multiprocessing
from multiprocessing import Pool, cpu_count
import time
from lxml import etree
try:
    from pyecharts import Pie
    from pyecharts import Bar
    from pyecharts import Page
except:
    pass
'''
爬取应用商店里的apk信息
多进程全局变量无法进行同步，因为每一个子进程中都会有一个变量的拷贝，互不影响，多线程倒是可以利用锁来控制一下，所以这里就不进行计数了。
'''
class apkinfoCrawler:
    def __init__(self):
        self.apkinfo = {
            "apkname": "default",
            "developer": "default",
            "classify": "default",
            "apksize": "default",
            "updatetime": "default",
            "permissionList": "default",
            "history": "default",
            "downloads": "default"
        }

    '''
    爬取小米商店的信息
    权限要求在应用商城中的权限和实际的权限进行比对
    '''
    def Micrawler(self,packageName):

        try:
            url="http://app.mi.com/details?id=%s&ref=search"%packageName
            data=requests.get(url).content
            selector = etree.HTML(data)
            apkname = selector.xpath("/html/body/div[@class='main']/div[@class='container cf']/div[@class='app-intro cf']/div[@class='app-info']/div[@class='intro-titles']/h3/text()")[0]
            developer = selector.xpath("/html/body/div[@class='main']/div[@class='container cf']/div[@class='app-intro cf']/div[@class='app-info']/div[@class='intro-titles']/p[1]/text()")[0]
            classify = selector.xpath("/html/body/div[@class='main']/div[@class='container cf']/div[@class='app-intro cf']/div[@class='app-info']/div[@class='intro-titles']/p[@class='special-font action']/text()")[0]
            apksize = selector.xpath("/html/body/div/div/div/div/div/ul[@class=' cf']/li[2]/text()")[0]
            updatetime = selector.xpath("/html/body/div/div/div/div/div/ul[@class=' cf']/li[6]/text()")[0]
            permissionList=selector.xpath("/html/body/div/div/div/div/div/ul[@class='second-ul']/li/text()")
            self.apkinfo={
                "apkname":apkname,
                "developer":developer,
                "classify":classify,
                "apksize":apksize,
                "updatetime":updatetime,
                "permissionList":permissionList,
                "from":u"小米应用商城"
            }
            return self.apkinfo
        except:
            return self.apkinfo
        return self.apkinfo

    '''
    爬取豌豆荚apk信息
    多了历史版本和下载量
    '''
    def wdjcrawler(self,packageName):
        print("=====开始爬取apk信息======")
        try:
            url="https://www.wandoujia.com/search?key=%s&source=index"%packageName
            #get apkinfourl
            data=requests.get(url).content
            selector=etree.HTML(data)
            nexturl=selector.xpath("/html/body/div/div/div/ul/li/a[@class='detail-check-btn']/@href")[0]

            #get apkinfo
            data2=requests.get(nexturl).content
            selector2=etree.HTML(data2)
            apkname=selector2.xpath("/html/body/div/div/div/div/div[@class='app-info']/p[@class='app-name']/span[@class='title']/text()")[0]
            updatetime=selector2.xpath("/html/body/div/div/div/div/div/span/span[@class='update-time']/text()")[0].split(":")[1]
            downloads=selector2.xpath("/html/body/div/div/div/div/div/div/span[@class='item install']/i/text()")[0]
            apksize=selector2.xpath("/html/body/div/div/div/div/div/dl[@class='infos-list']/dd[1]/text()")[0]
            classify=selector2.xpath("/html/body/div/div/div/div/div/dl/dd[@class='tag-box']/a[1]/text()")[0]
            permissionList=selector2.xpath("/html/body/div/div/div/div/div/dl/dd/div/ul/li[*]/span[@class='perms']/text()")
            developer=selector2.xpath("/html/body/div/div/div/div/div/dl/dd[6]/span[@class='dev-sites']/text()")[0]

            #get history information
            hisurl=nexturl+"/history"
            data3=requests.get(hisurl).content
            selector3=etree.HTML(data3)
            history=selector3.xpath("/html/body/div/div/div/div/div/ul[@class='old-version-list']/li[*]/a[1]/p/text()")
            self.apkinfo={
                "apkname":apkname,
                "developer":developer,
                "classify":classify,
                "apksize":apksize,
                "updatetime":updatetime,
                "permissionList":permissionList,
                "history":history,
                "downloads":downloads,
                "from":u"豌豆荚"
            }
            return self.apkinfo
        except:
            return self.apkinfo
        finally:
            return self.apkinfo
        return self.apkinfo





    def appDownload(self):

        try:
            url="http://app.mi.com"
            applist=[]
            for i in range(36,42):
                listurl = url + "/topList?page=%d"%i
                data=requests.get(listurl).content
                selector = etree.HTML(data)
                result= selector.xpath("/html/body/div/div/div/div/ul[@class='applist']/li[*]/a/@href")
                for app in result:
                    applist.append(url+app)
            downurllist=[]
            for appurl in applist:
                try:
                    data2=requests.get(appurl).content
                    selector2=etree.HTML(data2)
                    downloadurl=url+selector2.xpath("/html/body/div/div/div/div/div/div/a[@class='download']/@href")[0]
                    downurllist.append(downloadurl)
                    #print(downloadurl)
                except:
                    pass
            return downurllist
        except:
            pass
def download(url):
    try:
        print(u"开始下载=>%s"%url)
        res=requests.get(url,stream=True,timeout=6)
        filename=str(random.randint(1000000,9999999))
        f=open("/Volumes/Samsung_T5/zsdlove/malware_test/"+filename+".malware_test",'wb')
        apksize=res.headers['Content-Length']
        count=0
        size=float(5120)
        data=float(0)
        for chunk in res.iter_content(chunk_size=5120):
            if chunk:
                data=data+size
                if data/float(apksize)>0.05:
                    data=float(0)
                    count=count+1
                    time.sleep(0.1)
                    print("[*]task"+str(random.randint(1000000,9999999))+" "+count*"#"+str(float(count)/float(20)*100)+"%")
                f.write(chunk)
        print("[*]成功下载一个apk!")
    except:
        pass
import os
import json

'''
广告sdk使用情况分析,哪些广告sdk使用量最多
'''
def analyzead(bigresultdict):
    print("广告sdk使用情况分析,哪些广告sdk使用量最多")
    permissiontypelist={}
    permissioncountdict={}
    for key,value in bigresultdict.items():
        permissiondict=value.get('Advertisement')
        for k,v in permissiondict.items():
            if k not in permissiontypelist.keys():
                permissiontypelist[k]=v
                permissioncountdict[k]=1
            else:
                permissioncountdict[k]+=1
    permissioncountdict=sorted(permissioncountdict.items(),key=lambda item:item[1])
    permissioncountdict.reverse()
    finalresult={}
    for i in permissioncountdict[0:10]:
        print(i[0],i[1],permissiontypelist.get(i[0]))
        finalresult[permissiontypelist.get(i[0])]=i[1]
    return finalresult

'''
哪些应用使用广告sdk最多
'''
def analyzead2(bigresultdict):
    print("哪些应用使用广告sdk最多")
    perdict={}
    for key,result in bigresultdict.items():
        try:
            permissiondict=result.get('Advertisement')
            perlen=len(permissiondict.keys())
            perdict[result.get('packageName')]=perlen
        except:
            pass
    l=perdict.values()
    l.sort()
    perdict=sorted(perdict.items(),key=lambda item:item[1])
    perdict.reverse()
    finalresult={}
    for i in perdict[0:10]:
        print(i[0],i[1],bigresultdict.get(i[0]).get('apkname'),bigresultdict.get(i[0]).get('classify'))
        finalresult[bigresultdict.get(i[0]).get('apkname')]=i[1]
    return finalresult
'''
分析样本中的加壳情况，并对各个加壳类型进行统计
'''
def analyzeshell(bigresultdict):
    print("分析样本中的加壳情况，并对各个加壳类型进行统计")
    shelltypelist=[]
    shelltypecountdict={}
    for key,singledict in bigresultdict.items():
        shelltype=singledict['shellType']
        if shelltype not in shelltypelist:
            shelltypelist.append(shelltype)
            shelltypecountdict[shelltype]=1
        else:
            shelltypecountdict[shelltype]+=1
    finalresult={}
    for key,value in shelltypecountdict.items():
        print(key,value,str(float(value)/float(len(bigresultdict.keys()))*100)+"%")
        finalresult[key]=value
    return finalresult
'''
统计样本类型&数量&占比
'''
def analyzeclassify(bigresultdict):
    print("统计样本类型数量")
    classifylist=[]
    classifycountdict={}
    for key,singledict in bigresultdict.items():

        classify=singledict['classify']
        if classify not in classifylist:
            classifylist.append(classify)
            classifycountdict[classify]=1
        else:
            classifycountdict[classify]+=1
    finalresult={}
    for key,value in classifycountdict.items():
        print(key,value,str(float(value)/float(len(bigresultdict.keys()))*100)+"%")
        finalresult[key]=value
    return finalresult
'''
分析哪些应用使用权限最多
'''
def analyzepermission(bigresultdict):
    print("分析哪些应用使用权限最多")
    perdict={}
    for key,result in bigresultdict.items():
        permissiondict=result.get('permission')
        perlen=len(permissiondict.keys())
        perdict[result.get('packageName')]=perlen
    l=perdict.values()
    l.sort()
    print(u"最多拥有权限个数:%s"%max(l))
    print(u"平均拥有权限个数:%d"%(sum(l)/len(l)))
    perdict=sorted(perdict.items(),key=lambda item:item[1])
    perdict.reverse()
    finalresult={}
    for i in perdict[0:10]:
        print(i[0],i[1],bigresultdict.get(i[0]).get('apkname'),bigresultdict.get(i[0]).get('classify'))
        finalresult[bigresultdict.get(i[0]).get('apkname')]=i[1]
    return finalresult
'''
分析使用量最多的权限
'''
def analyzepermission2(bigresultdict):
    print("分析使用量最多的权限")
    permissiontypelist={}
    permissioncountdict={}
    for key,value in bigresultdict.items():
        permissiondict=value.get('permission')
        for k,v in permissiondict.items():
            if k not in permissiontypelist.keys():
                permissiontypelist[k]=v
                permissioncountdict[k]=1
            else:
                permissioncountdict[k]+=1
    permissioncountdict=sorted(permissioncountdict.items(),key=lambda item:item[1])
    permissioncountdict.reverse()
    finalresult={}
    for i in permissioncountdict:
        print(i[0],i[1],permissiontypelist.get(i[0])[1])
        finalresult[permissiontypelist.get(i[0])[1]]=i[1]
    return finalresult
'''
分析恶意sdk使用，哪些apk使用了恶意sdk
'''
def analyzenastysdk(bigresultdict):
    print("分析恶意sdk使用，哪些apk使用了恶意sdk")
    perdict={}
    for key,result in bigresultdict.items():
        permissiondict=result.get('nastySDKs')
        perlen=len(permissiondict.keys())
        perdict[result.get('packageName')]=perlen
    l=perdict.values()
    l.sort()
    perdict=sorted(perdict.items(),key=lambda item:item[1])
    perdict.reverse()
    finalresult={}
    for i in perdict[0:10]:
        print(i[0],i[1],bigresultdict.get(i[0]).get('apkname'),bigresultdict.get(i[0]).get('classify'))
        finalresult[bigresultdict.get(i[0]).get('apkname')]=i[1]
    return finalresult

'''
分析哪些恶意sdk使用得最多
'''
def analyzenastysdk2(bigresultdict):
    print("分析哪些恶意sdk使用得最多")
    permissiontypelist={}
    permissioncountdict={}
    for key,value in bigresultdict.items():
        permissiondict=value.get('nastySDKs')
        for k,v in permissiondict.items():
            if k not in permissiontypelist.keys():
                permissiontypelist[k]=v
                permissioncountdict[k]=1
            else:
                permissioncountdict[k]+=1
    permissioncountdict=sorted(permissioncountdict.items(),key=lambda item:item[1])
    permissioncountdict.reverse()
    finalresult={}
    for i in permissioncountdict[0:10]:
        print(i[0],i[1],permissiontypelist.get(i[0]))
        finalresult[permissiontypelist.get(i[0])]=i[1]
    return finalresult
def analyze():
    biglist=[]
    for root, dirs, files, in os.walk("/Users/pony/github/hades/workspace/result/"):
        for file in files:
            if os.path.splitext(file)[1] == '.json':
                filepath = os.path.join(root, file)
                biglist.append(filepath)
    print("共分析%d个文件"%len(biglist))
    bigresultdict={}
    for filepath in biglist:
        f=open(filepath,'r')
        data=f.read()
        singledict=json.loads(data)
        bigresultdict[singledict.get('packageName')]=singledict
    shell=analyzeshell(bigresultdict)
    classify=analyzeclassify(bigresultdict)
    per1=analyzepermission(bigresultdict)
    per2=analyzepermission2(bigresultdict)
    ad=analyzead(bigresultdict)
    ad2=analyzead2(bigresultdict)
    nastysdk=analyzenastysdk(bigresultdict)
    nastysdk2=analyzenastysdk2(bigresultdict)

    pie = Pie("分析样本中的加壳情况",title_pos='center')
    bar1 = Bar("统计应用类型数量",title_pos='center')
    bar2 = Bar("分析哪些应用使用权限最多",title_pos='center')
    pie3 = Pie("分析哪些权限使用最频繁",title_pos='left')
    pie4 = Pie("分析哪些第三方广告使用量最多",title_pos='center')
    bar5 = Bar("分析哪些应用使用广告最多",title_pos='center')
    pie6 = Pie("分析哪些应用使用恶意sdk最多",title_pos='center')
    pie7 = Pie("分析哪些恶意sdk使用量最多",title_pos='center')
    pie.add(
        "apk数量",
        shell.keys(),
        shell.values(),
        is_label_show=True,
        is_more_utils=True,
        legend_pos='left',
        legend_orient='vertical'
    )
    bar1.add(
        "apk数量",
        classify.keys(),
        classify.values(),
        is_label_show=True,
        is_more_utils=True,
        legend_pos='left',
        legend_orient='vertical'
    )
    bar2.add(
        "权限数量",
        per1.keys(),
        per1.values(),
        is_label_show=True,
        is_more_utils=True,
        legend_pos='left',
        legend_orient='vertical'
    )
    pie3.add(
        "apk数量",
        per2.keys(),
        per2.values(),
        is_label_show=True,
        is_more_utils=True,
        legend_pos='bottom',
        legend_orient='vertical'
    )
    pie4.add(
        "apk数量",
        ad.keys(),
        ad.values(),
        is_label_show=True,
        is_more_utils=True,
        legend_pos='left',
        legend_orient='vertical'
    )
    bar5.add(
        "apk数量",
        ad2.keys(),
        ad2.values(),
        is_label_show=True,
        is_more_utils=True,
        legend_pos='left',
        legend_orient='vertical'
    )
    pie6.add(
        "恶意sdk数量",
        nastysdk.keys(),
        nastysdk.values(),
        is_label_show=True,
        is_more_utils=True,legend_pos='left',
        legend_orient='vertical'
    )
    pie7.add(
        "恶意sdk数量",
        nastysdk2.keys(),
        nastysdk2.values(),
        is_label_show=True,
        is_more_utils=True,
        legend_pos='left',
        legend_orient='vertical'
    )

    page=Page()
    page.add(pie)
    page.add(bar1)
    page.add(bar2)
    page.add(pie3)
    page.add(pie4)
    page.add(bar5)
    page.add(pie6)
    page.add(pie7)
    page.render("bing2.html")



if __name__ == '__main__':
    #crawler=apkinfoCrawler()
    #print crawler.Micrawler("com.job.android")
    #print crawler.wdjcrawler("cn.haoyunbang")
    analyze()
    '''
    pool = Pool(processes=cpu_count())
    urls=crawler.appDownload()
    try:
       pool.map(download,urls)
    except Exception as e:
      print e
    '''