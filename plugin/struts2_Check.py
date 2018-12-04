'''
input parameter
struts version
output
get the vullist by the version of the struts
					by zsdlove 
to get the new flaws info,you can visit the following site:
http://struts.apache.org/releases
'''
struts_vul_info={}
def struts_Check(struts_version):
	file=open("struts.txt",'r')
	struts_data=file.readlines()
	for line in struts_data:
		version=line.split(";")[0]
		vullist=line.split(";")[-1]
		#print(version)
		#print(vullist)
		struts_vul_info[version]=vullist
	print("struts版本号:"+struts_version+"\t\n漏洞信息："+struts_vul_info[struts_version])
		
struts_Check("Struts 2.5.10.1")