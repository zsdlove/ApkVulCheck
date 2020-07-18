# -- coding:utf-8 --
'''
Coded by zsdlove
This is a toolt to help android app developers to check the flaws in their sourcecode 
'''
import os
import datetime
from plugin.manifestAnalysis import componentcheck
from plugin.mobileSDKAnalysis import mobileSDKAnalysis
from plugin.apkInfoCrawler import apkinfoCrawler
from plugin.permissionAnalyzer import permissionAnalyzer
from config import *
import json
import hashlib
import platform
from plugin.shellDetector import shellDetector
from plugin.fastanalyze import fastAnalyze
import click
import random
import zipfile
import json2html
def handleResult(func):
	'''
	处理apk检测结果
	'''
	def wrapper(*args,**kwargs):
		ret=func(*args,**kwargs)
		if ret[1]=="json":
			with open("./report/{}.json".format(ret[4]),"w")as f:
				f.write(json.dumps(ret[0], indent=2))
		elif ret[1]=="html":
			html_content = '''
			<!DOCTYPE html>
			<html lang="zh-cn">
			<head>
			<title>ApkVulCheck-{}-风险检测报告</title>
			<meta charset="utf-8" />	
			</head>
			<body>
			<h1 style="text-align:center">ApkVulCheck-{}-风险检测报告</h1>
			<hr />
			{}
			<div>2020 ApkVulCheck,inc.</div>
			</body>
			'''
			with open("./report/{}.html".format(ret[4]), "w")as f:
				f.write(html_content.format(ret[4],ret[4],json2html.json2html.convert(ret[0])))
		else:
			with open("./report/{}.json".format(ret[4]),"w")as f:
				f.write(json.dumps(ret[0], indent=2))

		with open(ret[2],"w")as f:
			f.write(json.dumps(ret[0], indent=2))

		print(ret[0])
		print("[Reporter] - generate result successfully.")
	return wrapper

def provide_env():
	if platform.system()=="Windows":
		print("不支持windows,请自行修复路径问题.")
		exit(0)

	'''
	准备缓存文件
	'''
	if not os.path.exists("/tmp/hades/result/"):
		if os.path.exists("/tmp/hades/"):
			os.mkdir("/tmp/hades/result")
		else:
			os.mkdir("/tmp/hades/")
			os.mkdir("/tmp/hades/result/")

class apkAnalysis():
	'''
	apk静态分析
	'''

	def __init__(self):
		self.result={}
		provide_env()

	def getAndroidManifest(self,apkpath,outputpath):
		'''
		获取manifest.xml
		'''
		try:
				zipfiles=zipfile.ZipFile(apkpath)
				a=zipfiles.read('AndroidManifest.xml')
				if a !='':
					apkdir=outputpath
					if not os.path.exists(apkdir):
						os.makedirs(apkdir)
					dexfile=open('{}/AndroidManifest.xml'.format(outputpath),'wb')
					dexfile.write(a)
				else:
					logging.error('- [error] function getAndroidManifest(apkname) 找不到AndroidManifest.xml文件！')
		except:
			logging.error('- [error] function getAndroidManifest(apkname) 找不到AndroidManifest.xml文件！')

	def decompile_AndroidManifest(self,apkpath,outputpath):
		'''
		解析manifest.xml
		'''
		try:
			if not os.path.exists(apkpath):
				os.makedirs(apkpath)
			self.getAndroidManifest(apkpath, outputpath)  # 获取apk中的AndroidManifest.xml文件
			cmd="java -jar lib/AXMLPrinter2.jar {}/AndroidManifest.xml > {}/AndroidManifest_resolved.xml".format(outputpath,outputpath)
			os.system(cmd)
			logging.info("[init] - Decode the AndroidManifest.xml file Successfully！")
			print("[init] - Decode the AndroidManifest.xml file Successfully！")
		except:
			logging.info("- [init] - Can't Decode the AndroidMnifest.xml file.")
			print("- [init] - Can't Decode the AndroidMnifest.xml file.")

	def decompiledex(self, apkpath, outputPath):
		'''
		@param apkpath path of malware_test.
		@param outputpath path of result file.
		反编译dex文件
		'''
		try:
			cmd="java -jar lib/baksmali.jar %s -o %s"%(apkpath,outputPath)
			print("outputpath=>%s"%outputPath)
			os.system(cmd)
			logging.info("[init] - Decompile the dex file Successfully.")
			print("[init] - Decompile the dex file Successfully.")
		except:
			logging.info("[init] - Can't decompile the dex file.")
			print("[init] - Can't decompile the dex file.")


	@handleResult
	def fastScanEngine(self,task):
		'''
		快速分析apk
		:param task:
		:return:
		'''
		stattime=str(datetime.datetime.now())[:19]
		provide_env()
		filepath=task.get("taskpath")
		taskname=filepath.split('/')[-1].split('.')[0]
		outputPath='/tmp/hades/result/%s'%taskname+str(random.randint(10000,99999))
		resultpath="{}/result.json".format(outputPath)

		self.decompile_AndroidManifest(filepath,outputPath)
		self.decompiledex(filepath,outputPath)

		cptcheck=componentcheck(outputPath)#component analysis
		cptcheck.run()
		activityEntryList,serviceEntryList= cptcheck.activityPathList,cptcheck.servicePathList
		providerEntryList,broadcastEntryList,packageName,version=cptcheck.providerPathList,cptcheck.broadcastPathList,cptcheck.packageName,cptcheck.version
		totalEntryList=activityEntryList+serviceEntryList+providerEntryList+broadcastEntryList

		msa=mobileSDKAnalysis()
		nastySDKList,Advertisement,thirdpartPayAPI,otherSDKs=msa.analysis(totalEntryList)

		aic=apkinfoCrawler()
		crawlresult=aic.Micrawler(packageName)
		if crawlresult.get("developer")=="default":
			crawlresult=aic.Micrawler(packageName)
		developer=crawlresult.get('developer')
		classify=crawlresult.get('classify')
		apkname=os.popen("lib/aapt2 dump badging %s |grep application-label:" % filepath).read().replace("\n","").split(":")[1].replace("'","")
		donwloads=crawlresult.get('downloads')
		history=crawlresult.get('history')
		apkfrom=crawlresult.get('from')
		'''
		权限检查
		'''
		pA=permissionAnalyzer()
		dangerous_permissions=pA.analysis(cptcheck.permissionList)

		apksize=os.path.getsize(filepath)
		def gethash(file):
			m,s1,s256= hashlib.md5(),hashlib.sha1(),hashlib.sha256()
			with open(file, 'rb') as f:
				for line in f:
					m.update(line)
					s1.update(line)
					s256.update(line)
			return m.hexdigest(),s1.hexdigest(),s256.hexdigest()
		md5str, shastr, sha256str = gethash(filepath)
		'''
		壳校验
		'''
		sd=shellDetector()
		isShelled,shellType=sd.shellDetector(filepath)

		'''
		开始快速模式扫描
		'''
		ipv4_s, ipv6_s, senAPI_s, pathlist, urlslist, emaillist, flaws_s = [], [], [], [], [], [],[]

		pathlist=[os.path.join(root, file)
					       for root,dirs,files in os.walk(outputPath)
								for file in files
					  					if os.path.splitext(file)[1] == '.smali' ]

		pathlist=[path
					  	for path in pathlist
							if "com/google" not in path and "android/" not in path and "androidx" not in path]

		for path in pathlist:
				try:
					print("[*]ananlysis %s"%path)
					sensitiveAPI,ipv4,ipv6,urls,emails,flaws=fastAnalyze(path).analyze()

					if len(ipv4)>0:[ipv4_s.append(ip) for ip in ipv4]

					if len(ipv6)>0:[ipv6_s.append(ip) for ip in ipv6]

					if len(sensitiveAPI)>0:senAPI_s.append(sensitiveAPI)

					if len(urls)>0:[urlslist.append(url) for url in urls]

					if len(emails)>0:[emaillist.append(email)for email in emails]

					if len(flaws)>0:flaws_s.append(flaws)
				except:
					pass

		self.result = {
			"Advertisement": Advertisement,
			"thirdpartPayAPI": thirdpartPayAPI,
			"nastySDKs": nastySDKList,
			"otherSDKs": otherSDKs,
			"packageName": packageName,
			"version": version,
			"size": str(apksize / 1048576) + "MB" if apksize > 1048576 else str(apksize / 1024) + "KB",
			"from": apkfrom,
			"time": str(datetime.datetime.now()),
			"md5": md5str,
			"sha1": shastr,
			"sha256": sha256str,
			"permission": dangerous_permissions,
			'activity': activityEntryList,
			'service': serviceEntryList,
			'provider': providerEntryList,
			'receiver': broadcastEntryList,
			"developer": developer,
			"classify": classify,
			"apkname": apkname,
			"shelltype": shellType,
			"donwloads": donwloads,
			"history": history,
			"taskid": task.get("taskid"),
			"target": filepath,
			"starttime": stattime,
			"endtime": str(datetime.datetime.now())[:19],
			"ipv4":ipv4_s,
			"ipv6":ipv6_s,
			"sensitiveAPI":senAPI_s,
			"urls":urlslist,
			"emails":emaillist,
			"flaws":flaws_s,
		}


		return self.result,task.get("output"),resultpath,task.get('taskid'),apkname

def gentaskid(taskpath):
	'''
	生成taskid
	'''
	m=hashlib.md5()
	m.update(taskpath.encode("utf-8"))
	return m.hexdigest()+str(random.randint(10000,99999))

def path_validate(filepath):
	'''
	路径校验
	:param filepath:
	:return:
	'''
	return True if filepath.endswith(".apk") and ".." not in filepath else False

@click.command()
@click.option("--taskpath",default="test/3436test1.apk",help='please input the apk path')
@click.option("--output",default="undefined",help='please input the path of the output')
def startprocess(**kwargs):

	apkAnalysis().fastScanEngine({
			"taskpath":kwargs.get("taskpath"),
			"taskid":gentaskid(kwargs.get("taskpath")),
			"output":kwargs.get("output")
		}
	)


if __name__ == '__main__':
	startprocess()