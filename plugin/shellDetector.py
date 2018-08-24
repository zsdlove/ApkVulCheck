import zipfile
'''
first,get namelist from apk
second,matching the features
thrid,julging for the shellType
so easy~~
by zsdlove
2018/8/24 Morning
'''
shellfeatures={
	"libchaosvmp.so":"娜迦",
	"libddog.so":"娜迦",
	"libfdog.so":"娜迦",
	"libedog.so":"娜迦企业版",
	"libexec.so":"爱加密",
	"libexecmain.so":"爱加密",
	"ijiami.dat":"爱加密",
	"ijiami.ajm":"爱加密企业版",
	"libsecexe.so":"梆梆免费版",
	"libsecmain.so":"梆梆免费版",
	"libSecShell.so":"梆梆免费版",
	"libDexHelper.so":"梆梆企业版",
	"libDexHelper-x86.so":"梆梆企业版",
	"libprotectClass.so":"360",
	"libjiagu.so":"360",
	"libjiagu_art.so":"360",
	"libjiagu_x86.so":"360",
	"libegis.so":"通付盾",
	"libNSaferOnly.so":"通付盾",
	"libnqshield.so":"网秦",
	"libbaiduprotect.so":"百度",
	"aliprotect.dat":"阿里聚安全",
	"libsgmain.so":"阿里聚安全",
	"libsgsecuritybody.so":"阿里聚安全",
	"libmobisec.so":"阿里聚安全",
	"libtup.so":"腾讯",
	"libexec.so":"腾讯",
	"libshell.so":"腾讯",
	"mix.dex":"腾讯",
	"lib/armeabi/mix.dex":"腾讯",
	"lib/armeabi/mixz.dex":"腾讯",
	"libtosprotection.armeabi.so":"腾讯御安全",
	"libtosprotection.armeabi-v7a.so":"腾讯御安全",
	"libtosprotection.x86.so":"腾讯御安全",
	"libnesec.so":"网易易盾",
	"libAPKProtect.so":"APKProtect",
	"libkwscmm.so":"几维安全",
	"libkwscr.so":"几维安全",
	"libkwslinker.so":"几维安全",
	"libx3g.so":"顶像科技",
	"libapssec.so":"盛大",
	"librsprotect.so":"瑞星"
}
def shellDetector(apkpath):
	shellType=""
	shellsign=""
	flag=True
	zipfiles=zipfile.ZipFile(apkpath)
	nameList=zipfiles.namelist()
	for fileName in nameList:
		for shell in shellfeatures.keys():
			if shell in fileName:
				flag=True
				shellType=shellfeatures[shell]
				shellsign=shell
				break
			else:
				flag=False
	if flag==True:
		print("经检测，该apk使用了"+shellType+"进行加固")
if __name__ == '__main__':
	shellDetector("test.apk")