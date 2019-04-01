# -- coding:utf-8 --
'''
Coded by zsdlove
This is a toolt to help android app developers to check the flaws in their sourcecode 
'''

import os
import sys
import xml.dom.minidom
import re
import zipfile
import random
import getopt
import shutil
sys.path.append('plugin')
from WebviewHideAPI_Check import WebviewHideAPI_Check

class cmdreceiver:
	def __init__(self):
		self.output=''
		self.target=''
	#
	#get cmd args
	def handlecmdargs(self):
		opts, args = getopt.getopt(sys.argv[1:], "h:t:o:", ["help", "output","target"])
		for opt,val in opts:
			if opt in ('-h','--help'):
				usage()
			elif opt in ('-o','--output'):
				self.output=val
			elif opt in ('-t','--target'):
				self.target=val
			else:
				print("default mode")

	def receive(self):
		self.handlecmdargs()

	def doapkcpy(self):
		copypath=os.getcwd()+"\workspace\\apk\\"+str(random.randrange(1000,9999))+".apk"
		shutil.copyfile(self.gettarget(),copypath)
		print("拷贝成功")
	def getoutput(self):
		return self.output

	def gettarget(self):
		return self.target
		
	def getapkname(self):
		return self.target.split('\\')[-1]
		

#generate report
class apkvulreporter:
	def __init__(self,resultfile,resultinfo):
		self.resultfile=resultfile
		self.resultinfo=resultinfo
	def generate(self):
		self.resultfile.write("<h2>白盒扫描漏洞报告</h2>")
		for vul in self.resultinfo.keys():
			self.resultfile.write("<div id='menu'><h3><a href=#"+vul+">"+vul+"漏洞</a></h3>")
		for vul in self.resultinfo.keys():
			self.resultfile.write("<div id="+vul+"><h3>"+vul+"漏洞</h3><a href='#menu'><h3>  返回漏洞目录</h3><a>")
			count=0
			for vulitem in self.resultinfo[vul]:
				count=count+1
				print("[+]找到疑似"+vul+"漏洞点！")
				print("代码是："+vulitem["linecode"].strip())
				print("行数："+vulitem["line"])
				print("路径："+vulitem["path"])
				self.resultfile.write("<h4>第"+str(count)+"处漏洞点</h4>")
				self.resultfile.write("<p>代码是："+vulitem["linecode"].strip()+"</p>")
				self.resultfile.write("<p>行数："+vulitem["line"]+"</p>")
				self.resultfile.write("<p>路径："+vulitem["path"]+"</p>")
				self.resultfile.write("</div>")
	
#manifest.xml resolve and check
class componentcheck:
	def __init__(self,apkname):
		self.manifest_path="workspace/result/"+apkname+"/AndroidManifest_resolved.xml"
	#
	#获得apk包名
	#
	def getPackageName(self,root):
		packageName=root.getAttribute('package')
		return packageName
		
	#
	#获得应用运行权限
	#
	def getUsesPermission(self,node):
		if node.nodeName == "uses-permission":
			print("申请的权限名为："+node.getAttribute('android:name'))
		return node.getAttribute('android:name')

	#
	#获得应用自定义权限：权限名，保护级别
	#
	def getPermission(self,node):
		if node.nodeName == "permission":
			print("自定义权限名："+node.getAttribute('android:name'))
			print("保护级别为："+node.getAttribute('android:protectionLevel'))
		return node.getAttribute('android:name')
	#
	#判断应用是否可被调试
	#
	def isapkdebugable(self,node):
		if node.getAttribute('android:debuggable')=="true":
			print("应用可被调试！")
		else:
			print("应用不可被调试->安全")
		
	#
	#备份漏洞backup
	#		
	def buckupflaw(self,node):
		if node.getAttribute('android:allowBackup')=="true":
			print("存在任意数据备份漏洞")
		else:
			print("不存在任意数据备份漏洞")
			
	#
	#解析application标签,检查bakup备份
	#
	def applicationtab(self,node):
		if node.nodeName == "application":
			self.buckupflaw(node)
			self.isapkdebugable(node)
			for cn in node.childNodes:
					if cn.nodeName!="#text":
						self.decompile_service(cn)
						self.decompile_activity(cn)
						self.decompile_receiver(cn)
						self.decompile_provider(cn)
					else:
						pass
						
		else:
			pass
	#
	#解析xml文件并检测manifest中的不当设置
	#
	def android_manifest_check(self):
		#try:
			dom = xml.dom.minidom.parse(self.manifest_path)
			print("xml读取成功")
			root = dom.documentElement
			packageName=self.getPackageName(root)
			print("apk包名是："+packageName)
			nodelist=root.childNodes
			for node in nodelist:
				if node.nodeName!="#text":
					self.getUsesPermission(node)#usespermission
					self.getPermission(node)#permission
					self.applicationtab(node)#解析application标签
		#except:
		#	pass	
	def run(self):
		self.android_manifest_check()

	#
	#解析activity,cn是节点
	#
	def decompile_activity(self,cn):
		if cn.nodeName=="activity":
			print("exported:"+cn.getAttribute("android:exported"))
			if cn.getAttribute("android:exported")=="true":
				print("activity组件导出,存在风险")
			else:
				print("activity组件安全")
		else:
			pass
		return cn.getAttribute("android:exported")
		
	#
	#解析service
	#
	def decompile_service(self,cn):
		if cn.nodeName=="service":
			print("exported:"+cn.getAttribute("android:exported"))
			if cn.getAttribute("android:exported")=="true":
				print("service组件导出,存在风险")
			else:
				print("service组件安全")
		else:
			pass
		return cn.getAttribute("android:exported")
		
	#
	#解析receiver
	#
	def decompile_receiver(self,cn):
		if cn.nodeName=="receiver":
			print("exported:"+cn.getAttribute("android:exported"))
			if cn.getAttribute("android:exported")=="true":
				print("receiver组件导出,存在风险")
			else:
				print("receiver组件安全")
		else:
			pass
		return cn.getAttribute("android:exported")
		
	#
	#解析provider
	#
	def decompile_provider(self,cn):
		if cn.nodeName=="provider":
			print("exported:"+cn.getAttribute("android:exported"))
			if cn.getAttribute("android:exported")=="true":
				print("provider组件导出,存在风险")
			else:
				print("provider组件安全")
		else:
			pass
		return cn.getAttribute("android:exported")

#apkvulcheck main engine
class apkvulcheck:
	def __init__(self):
		self.resultinfo={}
		self.apknamelist=getapkFileName()
		self.output=''
	#
	#获取manifest.xml文件
	#			
	def getAndroidManifest(self,apkname):
		apkfilelist=getApkFilePath()
		print('py文件目录'+os.getcwd())
		for apkfilepath in apkfilelist:
			try:
				zipfiles=zipfile.ZipFile(apkfilepath)
				a=zipfiles.read('AndroidManifest.xml')
				if a !='':
					#apkname=apkfilepath.split('.')[0].split('\\')[-1]
					print('apk文件名'+apkname)
					apkdir=os.getcwd()+'\\workspace\\result\\'+apkname
					print(apkdir)
					if not os.path.exists(apkdir):
						os.makedirs(apkdir)
					dexfile=open('workspace/result/'+apkname+'/AndroidManifest.xml','wb')
					dexfile.write(a)
					print('获取AndroidManifest.xml文件成功')
				else:
					print('找不到AndroidManifest.xml文件！')
			except:
				continue
		

	def decompiledex(self,apkname):
		path=os.getcwd()+'//workspace//result//'
		self.getdexfile(apkname)#处理apk文件
		cmd="java -jar lib/baksmali.jar -o workspace/result/"+apkname+" workspace/result/"+apkname+"/classes.dex"
		os.system(cmd)
		print('dex文件反编译成功')
		
	def VulScanEngine(self,apkname):
		resultfile=''
		resultfile2=''
		apkresultpath=os.getcwd()+'//report//'+apkname
		os.makedirs(apkresultpath)
		if self.output!="":
			resultfile=open(self.output,"w+")
			resultfile2=open(apkresultpath+"//_result.txt",'w+')
		else:
			resultfile=open(apkresultpath+"//_result.html",'w+')
			resultfile2=open(apkresultpath+"//_result.txt",'w+')
		features=getFeatureFromXml()
		print("开始进dex反编译")
		self.decompiledex(apkname)
		print("开始进行AndroidManifest.xml反编译")
		self.decompile_AndroidManifest(apkname)
		#解析并检测manifest.xml文件
		cptcheck=componentcheck(apkname)
		cptcheck.run()
		print("开始进行安卓漏洞静态扫描")
		path='./workspace/result/'+apkname
		for root,dirs,files,in os.walk(path):
				for file in files:
					if os.path.splitext(file)[1] == '.smali':
						refs={}
						#print(os.path.join(root,file))
						filepath=os.path.join(root,file)
						className=os.path.splitext(file)[0]
						print("开始扫描类文件："+filepath)
						f=open(filepath,'rb')
						lines=f.readlines()
						lineslen=len(lines)
						className=os.path.splitext(file)[0]
						try:
							while lineslen>0:
									lineslen=lineslen-1
									linecode=lines[lineslen]
									linecode=str(linecode,encoding="utf-8")	
									for vulname in features.keys():
										if vulname not in self.resultinfo.keys():
											self.resultinfo[vulname]=[]
										for feature in features[vulname]['item']:
											m=re.match(r'.*'+feature+'.*',linecode)
											if m:
													print("[+]找到疑似"+vulname+"漏洞点，地址是："+filepath)
													#if vulCheckEngine(vulname,lines):
													vulinfo={}
													vulinfo["path"]=filepath
													vulinfo["linecode"]=linecode
													vulinfo["line"]=str(lineslen)
													self.resultinfo[vulname].append(vulinfo)
													resultfile2.write("[+]checked:"+vulname+" 地址："+filepath+"行数："+str(lineslen)+"\n")
											else:
												pass
										
						except:
							pass
		#生成报告
		reporter=apkvulreporter(resultfile,self.resultinfo)
		reporter.generate()
		input("按任意键结束");
	#
	#获得dex文件
	#
	def getdexfile(self,apkname):
		apkfilelist=getApkFilePath()
		print('py文件目录'+os.getcwd())
		for apkfilepath in apkfilelist:
			try:
				zipfiles=zipfile.ZipFile(apkfilepath)
				a=zipfiles.read('classes.dex')
				if a !='':
					#apkfileName=apkfilepath.split('.')[0].split('\\')[-1]
					print('apk文件名'+apkname)
					apkdir=os.getcwd()+'\\workspace\\result\\'+apkname
					os.makedirs(apkdir)
					dexfile=open('workspace/result/'+apkname+'/classes.dex','wb')
					dexfile.write(a)
					print('获取classes.dex文件成功')
				else:
					print('找不到classes.dex文件！')
			except:
				continue
			
	#
	#对androidManifest.xml进行反编译，获得明文文件
	#

	def decompile_AndroidManifest(self,apkname):
		path=os.getcwd()+'//workspace//result//'
		self.getAndroidManifest(apkname)#获取apk中的AndroidManifest.xml文件
		cmd="java -jar lib/AXMLPrinter2.jar workspace/result/"+apkname+"/AndroidManifest.xml > "+" workspace/result/"+apkname+"/AndroidManifest_resolved.xml"
		print("打印cmd"+cmd)
		os.system(cmd)
		print('AndroidManifest.xml反编译成功！')
			
		
	def run(self):
		cmdrec=cmdreceiver()
		cmdrec.receive()
		if cmdrec.gettarget()!="":
			cmdrec.doapkcpy()
			if cmdrec.getoutput!="":
				self.output=cmdrec.getoutput()
			self.VulScanEngine(cmdrec.getapkname())
		else:
			for apkname in self.apknamelist:
				apkname=apkname+str(random.randrange(1000,9999))
				self.VulScanEngine(apkname)		
#
#从conf.xml文件中获取特征值
#	

def getFeatureFromXml():
	vulhub={}
	dom = xml.dom.minidom.parse('lib/conf.xml')
	root = dom.documentElement
	nodelist=root.childNodes
	for node in nodelist:
		if node.nodeName!="#text":
			#print(node.nodeName)
			vulname=node.nodeName
			for nd in node.childNodes:
				if nd.nodeName!="#text" and nd.nodeName!="desc":
					#print(nd.firstChild.data)
					feature=nd.firstChild.data
					if vulname not in vulhub.keys():
						vulhub[vulname]={}
					if 'item' not in vulhub[vulname].keys():
						vulhub[vulname]['item']=[]
					vulhub[vulname]['item'].append(feature)
				elif nd.nodeName=="desc":
					if vulname not in vulhub.keys():
						vulhub[vulname]={}
					if 'item' not in vulhub[vulname].keys():
						vulhub[vulname]['item']=[]
					vulhub[vulname]['desc']=nd.firstChild.data
				else:
					pass
	return vulhub
#
#各种漏洞进一步检测的入口
#

def vulCheckEngine(vulname,lines):
	return getModuleByVulname(vulname,lines)
	
#
#通过漏洞类型找到漏洞检测函数
#

def getModuleByVulname(vulname,lines):
	flag=eval(vulname+"_Check"+"(lines)")
	print(vulname+"detecting finished")
	return flag	

#
#usage
#	

def usage():
	print('''
Help:
	-t [apkpath]
	-o [resultpath]
	-l [apklistpath]
examples:
	python -t c:/test.apk -o c:/test.html
	''')
	
	
#
#获得apk文件名
#

def getapkFileName():
	apkfilenamelist=[]
	for root,dirs,files,in os.walk('workspace'):
			for file in files:
				if os.path.splitext(file)[1] == '.apk':
					filepath=os.path.join(root,file)
					filepath=filepath.split('.')[0].split('\\')[-1]
					apkfilenamelist.append(filepath)
	return apkfilenamelist
		

#
#从获得apk文件路径
#

def getApkFilePath():
	apkfilelist=[]
	for root,dirs,files,in os.walk('workspace'):
			for file in files:
				if os.path.splitext(file)[1] == '.apk':
					filepath=os.path.join(root,file)
					apkfilelist.append(filepath)
	return apkfilelist
	

if __name__ == '__main__':
	avc=apkvulcheck()
	avc.run()
	
