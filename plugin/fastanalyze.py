# -- coding:utf-8 --
import re
fastmoderules={
    u'Landroid/telephony/TelephonyManager;->getDeviceId()Ljava/lang/String;':u'获取设备ID信息',
	u'Landroid/content/pm/PackageManager;->getInstalledApplications(I)Ljava/util/List;':u'获取已经安装的应用程序信息',
	u'Landroid/test/mock/MockPackageManager;->getInstalledApplications(I)Ljava/util/List;':u'获取已经安装的应用程序信息',
	u'Landroid/telephony/CellIdentityGsm;->getLac()I':u'获取位置区域码',
	u'Landroid/telephony/CellIdentityWcdma;->getLac()I':u'获取位置区域码',
	u'Landroid/telephony/NeighboringCellInfo;->getLac()I':u'获取位置区域码',
	u'Landroid/telephony/gsm/GsmCellLocation;->getLac()I':u'获取位置区域码',
	u'Landroid/provider/Browser;->getAllVisitedUrls(Landroid/content/ContentResolver;)Landroid/database/Cursor;':u'获取所有的浏览器浏览记录信息',
	u'Landroid/content/pm/PackageManager;->getInstalledPackages(I)Ljava/util/List;':u'获取已安装的包信息',
	u'Landroid/test/mock/MockPackageManager;->getInstalledPackages(I)Ljava/util/List;':u'获取已安装的包信息',
	u'Landroid/telephony/CellIdentityGsm;->getCid()I':u'获取基站编号',
	u'Landroid/telephony/CellIdentityWcdma;->getCid()I':u'获取基站编号',
	u'Landroid/telephony/NeighboringCellInfo;->getCid()I':u'基站编号',
	u'Landroid/telephony/gsm/GsmCellLocation;->getCid()I':u'基站编号',
	u'Landroid/net/wifi/WifiInfo;->getSSID()Ljava/lang/String;':u'获取手机SSID',
	u'Landroid/net/IpPrefix;->getAddress()Ljava/net/InetAddress;':u'获取ip地址',
	u'Landroid/net/LinkAddress;->getAddress()Ljava/net/InetAddress;':u'获取InetAddress信息',
	u'Landroid/net/wifi/WifiManager;->getWifiState()I':u'获取wifi状态信息',
	u'Landroid/accounts/AccountManager;->getAccounts()[Landroid/accounts/Account;':u'获取谷歌账户信息',
	u'Landroid/provider/Browser;->getAllBookmarks(Landroid/content/ContentResolver;)Landroid/database/Cursor;':u'获取浏览器所有标签页的信息',
	u'Landroid/widget/RemoteViews;->getPackage()Ljava/lang/String;':u'获取远程应用的包信息',
	u'Landroid/app/WallpaperInfo;->toString()Ljava/lang/String;':u'获取背景信息',
	u'Landroid/app/admin/DeviceAdminInfo;->toString()Ljava/lang/String;':u'获取设备管理员信息',
	u'Landroid/app/job/JobInfo;->toString()Ljava/lang/String;':u'获取作业信息',
	u'Landroid/telephony/TelephonyManager;->getLine1Number()Ljava/lang/String;':u'获取电话号码信息',
	u'Landroid/location/LocationManager;->getLastKnownLocation(Ljava/lang/String;)Landroid/location/Location;':u'获取地理位置信息',
	u'Landroid/telephony/TelephonyManager;->getSimSerialNumber()Ljava/lang/String;':u'获取sim卡序列号信息',
    u'Landroid/app/ActivityManager;->getRunningTasks':u'获取正在运行中的任务信息',
    u'Landroid.app.ActivityManager;->getRunningAppProcesses':u'获取正在运行的应用程序',
    u'Landroid.telephony.TelephonyManager;->listen':u'监听电话',
    u'Landroid.telephony.TelephonyManager;->getCellLocation':u'获取电话',
    u'Landroid.telephony.TelephonyManager;->getSubscriberId':u'获取基站位置信息',
    u'Landroid.telephony.TelephonyManager;->getVoiceMailAlphaTag':u'返回语音邮件号码',
    u'Landroid.telephony.TelephonyManager;->isNetworkRoaming':u'返回手机是否处于漫游状态',
    u'Landroid.telephony.TelephonyManager;->getPhoneType':u'获取电话类型',
    u'Landroid.telephony.TelephonyManager;->getNetworkOperator':u'SIM卡运营商国家代码和运营商网络代码',
    u'Landroid.telephony.TelephonyManager;->getNetworkOperatorName':u'返回移动网络运营商的名字(SPN)',
    u'Landroid.telephony.TelephonyManager;->getSimOperator':u'返回移动网络运营商的名字(SPN)',
    u'Ldalvik/system/DexClassLoader;-><init>(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/ClassLoader;)V':u'外部动态加载DEX检测',
    u'Landroid/provider/Settings$Secure;->getString':u'获取android ID',
    u'Landroid/telephony/SmsManager;->getDefault()Landroid/telephony/SmsManager;':u'发送短信',
    u'Landroid/telephony/SmsManager;->sendDataMessage(Ljava/lang/String; Ljava/lang/String; S [B Landroid/app/PendingIntent; Landroid/app/PendingIntent;)V':u'发送短信',
    u'Landroid/telephony/SmsManager;->sendMultipartTextMessage(Ljava/lang/String; Ljava/lang/String; Ljava/util/ArrayList; Ljava/util/ArrayList; Ljava/util/ArrayList;)V':u'发送短信',
    u'Landroid/telephony/SmsManager;->sendTextMessage(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)V':u'发送短信',
    u'Linvoke-virtual {v1}, Ljava/io/File;->delete()Z':u'删除文件',
    u'Liget-object v2, v0, Landroid/content/pm/PackageInfo;->signatures:[Landroid/content/pm/Signature;':u'获取singature',
    u'Linvoke-virtual {v1, v2}, Ljava/lang/Runtime;->exec(Ljava/lang/String;)Ljava/lang/Process;':u'运行命令',
    u'Landroid.app.ActivityManager/killBackgroundProcesses':u'杀死后端进程',
    u'Landroid.app.ActivityManager/forceStopPackage':u'强制结束包',
    u'Landroid.hardware.Camera/takepicture':u'拍照',
    u'Landroid.app.ApplicationPackageManager;->installPackage':u'安装应用',
    u'Landroid.app.ApplicationPackageManager/deletePackage':u'删除应用',
}

'''
粗糙的apk潜在漏洞匹配-_-||
'''
flawsSink={
    'AnyFileReadAndWrite':{
        'flawsname':u'任意文件读写漏洞',
        'desc':u'''
SharedPreferences是Android平台上一个轻量级的存储类，用来保存应用的一些常用配置，比如Activity状态，Activity暂停时，将此activity的状态保存到SharedPereferences中；当Activity重载，系统回调方法onSaveInstanceState时，再从SharedPreferences中将值取出。
关键函数getsharedpreferences(string name,int mode)
操作数等级有：
Context.mode_private表示该文件为私有，只能在应用内被访问；
Context.MODE_WORLD_READABLE 其他应用可读
Context.MODE_WORLD_WRITEABLE 其他应用可写
Context.MODE_WORLD_READABLE + Context.MODE_WORLD_WRITEABLE其他应用可读写
危害：Shared Preferences文件没有使用正确的创建模式，导致可被其他应用访问，并执行读写操作，可能会导致敏感信息的泄漏。
    ''',
        'suggest':u'''
1、避免使用MODE_WORLD_READABLE和MODE_WORLD_WRITEABLE模式创建内部存储文件
2、避免把密码等敏感数据信息明文存放在内部存储文件中        
        ''',
        'item':[u'openFileOutput(Ljava/lang/String;I)Ljava/io/FileOutputStream;']},
    'HardCode':{
        'flawsname':u'密钥硬编码漏洞',
        'desc':u'''
应用程序在加解密时，使用硬编码在程序中的密钥，攻击者通过反编译拿到密钥可以轻易解密APP通信数据     
        ''',
        'suggest':u'''
避免使用MODE_WORLD_READABLE和MODE_WORLD_WRITEABLE模式创建数据库(Database)        
        ''',
        'item':[u'Ljavax/crypto/spec/SecretKeySpec;->']},
    'tcDanialOfService':{
        'flawsname':u'强制类型转换本地拒绝服务漏洞',
        'desc':u'''
getSerializableExtra(String name)  返回Serializable
getStringExtra(String name)  返回String
导出的组件没有对getSerializableExtra()等获取到的数据进行类型判断而进行强制类型转换，从而导致类型转换异常而导致应用崩溃
        ''',
        'suggest':u'''
1、不必要导出的组件，建议显示设置组件的“android:exported”属性为false
2、在做强制类型转换时，要先进行类型判断并使用try catch，防止异常数据导致强制转换抛出异常        
        ''',
        'item':[u'Landroid/content/Intent;->get.+Extra']},
    'DanialOfServiceConponents':{
        'flawsname':u'系统组件本地拒绝服务漏洞',
        'desc':u'''
getAction()  返回String
getSerializableExtra(String name)  返回Serializable
getStringExtra(String name)  返回String
导出的组件在处理Intent附加数据的时候，没有进行异常捕获，攻击者可通过向应用发送空数据、异常或畸形数据等，导致应用程序崩溃。        
        ''',
        'suggest':u'''
1、不必要导出的组件，建议显示设置组件的“android:exported”属性为false
2、在使用Intent获取附加数据时，使用try catch进行异常捕获和处理，防止抛出异常引发崩溃        
        ''',
        'item':[u'Landroid/content/Intent;->get(?:Action|.+Extra)']},
    'IntentSchemaURL':{
        'flawsname':u'Intent Schema URL漏洞',
        'desc':u'''
如果浏览器支持Intent Scheme Uri语法，如果过滤不当，那么恶意用户可能通过浏览器js代码进行一些恶意行为，比如盗取cookie等。如果使用了Intent.parseUri函数，获取的intent必须严格过滤，intent至少包含addCategory(“android.intent.category.BROWSABLE”)，setComponent(null)，setSelector(null)3个策略     
        ''',
        'suggest':u'''
        Intent intent=Intent.parseUri(uri);
        intent.addCategory(android.intent.category.BROWSABLE);
        intent.setComponent(null);
        intent.setSelector(null);
        context.startActivityIfNeeded(intent,-1);
        ''',
        'item':[u'Landroid/content/Intent;->parseUri']},
    'ContentProviderSQLInjection':{
        'flawsname':u'Content Provider组件本地SQL注入漏洞',
        'desc':u'''
关键函数query(Uri uri, String[ ] projection, String selection, String[ ] selectionArgs, String sortOrder)。
Content Provider是存储和获取数据提供统一的接口,可以在不同的应用程序之间共享数据,Android已经为常见的一些数据提供了默认的ContentProvider。
危害：暴露的Provider组件，如果在query()中使用拼接字符串组成SQL语句的形式去查询数据库，容易发生SQL注入攻击。        
        ''',
        'suggest':u'''
1、不必要导出的Provider组件，建议显示设置组件的“android:exported”属性为false
2、使用selectionArgs进行参数化查询
        ''',
        'item':[u'.super Landroid/content/ContentProvider;']},
    'CodeDynamicLoading':{
        'flawsname':u'代码动态加载安全检测',
        'desc':u'''
DexClassLoader(String dexPath, String optimizedDirectory, String librarySearchPath, ClassLoader parent)
PathClassLoader(String dexPath, String librarySearchPath, ClassLoader parent)
函数作用用于加载apk，dex或jar等文件。
危害：
使用DexClassLoader或PathClassLoader动态加载dex文件、apk文件、jar文件时，如果这些文件存储在可被其他应用读写的目录中(比如sdcard)，同时没有对外部加载的文件进行完整性校验，导致应用可能会被恶意代码注入并执行。
        ''',
        'suggest':u'''
1、将所需要动态加载的文件放置在apk内部，或应用私有目录中
2、如果应用必须要把所加载的文件放置在可被其他应用读写的目录中(比如sdcard)，建议对不可信的加载源进行完整性校验和白名单处理，以保证不被恶意代码注入        
        ''',
        'item':[u'Ldalvik/system/DexClassLoader->init']},
    'CertificateWeakCheck':{
        'flawsname':u'证书弱校验',
        'desc':u'''
自定义实现的X509TrustManager子类中，未对服务器端证书做验证，默认接受任意服务端证书，会存在安全风险，可能会导致恶意程序利用中间人攻击绕过证书校验        
        ''',
        'suggest':u'''
利用X509TrustManager子类中的checkServerTrusted函数，校验服务器端证书的合法性        
        ''',
        'item':[u'.implements Ljavax/net/ssl/X509TrustManager;']},
    'HostnameWeakVerifier':{
        'flawsname':u'主机名弱校验',
        'desc':u'''
客户端根据服务器证书内编码的主机名验证URL内的主机名。以确保客户端连接到了真正的服务器，而不是中间人。
漏洞的成因是客户端自定义实现了HostnameVerifier接口，其中的verify函数没有做好校验，默认接受任意域名，导致了中间人攻击。        
        ''',
        'suggest':u'''
利用HostnameVerifier子类中的verify函数，校验服务器主机名的合法性        
        ''',
        'item':[u'.implements Ljavax/net/ssl/HostnameVerifier;']},
    'HTTPSsensitivedatahijack':{
        'flawsname':u'HTTPS敏感数据劫持漏洞',
        'desc':u'''
Android APP在HTTPS通信中，使用ALLOW_ALL_HOSTNAME_VERIFIER，表示允许和所有的HOST建立SSL通信，这会存在中间人攻击的风险，最终导致敏感信息可能会被劫持，以及其他形式的攻击        
        ''',
        'suggest':u'''
验证策略改成严格模式，即把ALLOW_ALL_HOSTNAME_VERIFIER改成STRICT_HOSTNAME_VERIFIER        
        ''',
        'item':[u';->setHostnameVerifier']},
    'UnsafeHash':{
        'flawsname':u'Hash算法不安全',
        'desc':u'''
使用不安全的Hash算法(MD5/SHA-1)加密信息，存在被破解的风险
如何检测：
1. 调用MessageDigest类的getInstance方法
【1】对应到smali语句的特征
       invoke-static {v1}, Ljava/security/MessageDigest;->
            getInstance(Ljava/lang/String;)Ljava/security/MessageDigest;
2. 寄存器赋值的判断
     const-string v1, MD5
     const-string v1, SHA-1    
        ''',
        'suggest':u'''
建议使用SHA-256等安全性更高的Hash算法        
        ''',
        'item':[u'Ljava/security/MessageDigest;->getInstance']},
    'AESWeakSecret':{
        'flawsname':u'AES弱加密',
        'desc':u'''使用AES/DES/DESede加密算法时，如果使用ECB模式，容易受到攻击风险，造成信息泄露。''',
        'suggest':u'''
使用AES/DES/DESede加密算法时，应显示指定使用CBC或CFB加密模式        
        ''',
        'item':[u'Ljavax/crypto/Cipher;->getInstance']},
    'UnsafeLocat':{
        'flawsname':u'Locat泄露隐私信息',
        'desc':u'''
在APP的开发过程中，为了方便调试，通常会使用log函数输出一些信息，这会让攻击者更加容易了解APP内部结构，方便破解和攻击，甚至有可能直接获取到有价值的隐私敏感信息。        
        ''',
        'suggest':u'''
为了APP的错误采集，异常反馈，必要的日志还是要被输出的，建议使用ProGuard等工具在APP的发行版本(release)中自动删除Log.d()和Log.v()对应的代码       
        ''',
        'item':[u'Landroid/util/Log;->d']},
    'LogLeakRisk':{
        'flawsname':u'日志泄漏风险',
        'desc':u'''
使用System.out.print和System.out.println输出打印日志信息，容易泄漏敏感信息
        ''',
        'suggest':u'''
建议删除所有使用System.out.print和System.out.println输出打印日志信息的代码        
        ''',
        'item':[u'Ljava/io/PrintStream;->print']},
    'PendingIntentMisuseRisk':{
        'flawsname':u'PendingIntent误用风险',
        'desc':u'''
使用PendingIntent的时候，如果使用了一个空Intent，会导致恶意用户劫持修改Intent的内容
        ''',
        'suggest':u'''
1、禁止使用一个空Intent去构造PendingIntent
2、构造PendingIntent的Intent一定要设置ComponentName或者action        
        ''',
        'item':[u'Landroid/app/PendingIntent;->getActivity']},
    'InetentImplicitCall':{
        'flawsname':u'Intent隐式调用',
        'desc':u'''
隐式intent没有明确指明哪些接收方有权限接收，恶意程序指定action标识后，可以获取intent内容，导致数据泄露，intent劫持，仿冒，钓鱼应用等风险。        
        ''',
        'suggest':u'''
1、建议使用显示调用方式发送Intent
2、使用Intent.setPackage、Intent.setComponent、Intent.setClassName、Intent.setClass、new Intent(context,Receivered.class)中任一种方法明确指定目标接收方，显式调用intent        
        ''',
        'item':[u'Landroid/content/Intent;->setAction']},
    'AnyDatabaseReadAndWrite':{
        'flawsname':u'数据库文件任意读写',
        'desc':u'''
数据库(Database)文件没有使用正确的创建模式，导致可被其他应用访问，并执行读写操作，可能会导致敏感信息的泄漏        
        ''',
        'suggest':u'''
避免使用MODE_WORLD_READABLE和MODE_WORLD_WRITEABLE模式创建数据库(Database)        
        ''',
        'item':[u'Landroid/database/sqlite/SQLiteDatabase;']},
    'WebviewHideAPI':{
        'flawsname':u'WebView系统隐藏接口漏洞检测',
        'desc':u'''
android webview组件包含3个隐藏的系统接口：searchBoxJavaBridge_, accessibilityTraversal以及accessibility，恶意程序可以利用它们实现远程代码执行        
        ''',
        'suggest':u'''
对于APP开发者，如果使用了WebView，那么使用WebView.removeJavascriptInterface(String name) API，显示的移除searchBoxJavaBridge_、accessibility、accessibilityTraversal这三个接口        
        ''',
        'item':[u'searchBoxJavaBridge_']},
    'WebviewIgnoreSSLcer':{
        'flawsname':u'WebView忽略SSL证书错误检测',
        'desc':u'''
Android WebView组件加载网页发生证书认证错误时，会调用WebViewClient类的onReceivedSslError方法，如果该方法实现调用了handler.proceed()来忽略该证书错误，则会受到中间人攻击的威胁，可能导致隐私泄露。        
        ''',
        'suggest':u'''
1、不调用android.webkit.SslErrorHandler的proceed方法
2、当发生证书认证错误时，采用默认的处理方法SslErrorHandler.cancel()，停止加载问题页面        
        ''',
        'item':[u'Landroid/webkit/SslErrorHandler;->proceed']},
    'WebviewSecretPlaintextStorage':{
        'flawsname':u'WebView明文存储密码',
        'desc':u'''
在使用WebView的过程中忽略了WebView setSavePassword，当用户选择保存在WebView中输入的用户名和密码，则会被明文保存到应用数据目录的databases/webview.db中。如果手机被root就可以获取明文保存的密码，造成用户的个人敏感数据泄露。        
        ''',
        'suggest':u'''
使用WebView.getSettings().setSavePassword(false)来禁止保存密码        
        ''',
        'item':[u'Landroid/webkit/WebSettings;->setSavePassword']},
    'AnySharedPreferencesReadAndWrite':{
        'flawsname':u'SharedPreferences任意读写',
        'desc':u'''
SharedPreferences是Android平台上一个轻量级的存储类，用来保存应用的一些常用配置，比如Activity状态，Activity暂停时，将此activity的状态保存到SharedPereferences中；当Activity重载，系统回调方法onSaveInstanceState时，再从SharedPreferences中将值取出。
关键函数getsharedpreferences(string name,int mode)        
        ''',
        'suggest':u'''
1、避免使用MODE_WORLD_READABLE和MODE_WORLD_WRITEABLE模式创建Shared Preferences文件
2、避免把密码等敏感数据信息明文存放在Shared Preferences文件中        
        ''',
        'item':[u';->getSharedPreferences(Ljava/lang/String;I)Landroid/content/SharedPreferences;']},
    'UnsafeRandomCode':{
        'flawsname':u'随机数使用不安全',
        'desc':u'''
生成的随机数具有确定性，存在被破解的风险        
        ''',
        'suggest':u'''
1、不使用setSeed方法
2、使用/dev/urandom或者/dev/random来初始化伪随机数生成器        
        ''',
        'item':[u'Ljava/security/SecureRandom;->setSeed']},
}
class fastAnalyze(object):
    def __init__(self,classpath):
        self.result={}
        self.classpath=classpath
        self.classbytecode=self.readclassfile(self.classpath)
        self.ipv4=set()
        self.ipv6=set()
        self.urls=set()
        self.emails=set()
        self.flawresult={}
    '''
    读取类字节码文件
    '''
    def readclassfile(self,classpath):
        file=open(classpath,"rb")
        return file.readlines()

    '''
    快速的发现apk中潜在的漏洞
    '''
    def checkFlaws(self,linestr):
        for key,val in flawsSink.items:
            for sink in val.get('items'):
                if sink in linestr:
                    pass


    '''
    分析每一个类文件中的ipv4信息
    '''
    def getallIP(self,linestr):
        result = re.findall(
            r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", linestr)
        if result:
            return result
        else:
            result=[]
        return result

    '''
    分析每一个类文件中的ipv6信息
    '''
    def getallipv6(self,linestr):
        # 匹配是否满足IPv6格式要求,请注意例子里大小写不敏感
        result = re.findall(r"(?<![:.\w])(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}(?![:.\w])", linestr, re.I)
        if result:
            return result
        else:
            result=[]
        return  result

    '''
    获取url信息
    '''
    def geturl(self,linestr):
        result=re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',linestr)
        res=[url for url in result if "\"" not in url and ")" not in url and "(" not in url and ";" not in url and "+" not in url and ";" not in url]
        res=[url.replace("\\","") for url in res]
        if res:
            return res
        else:
            res=[]
        return res

    def getemail(self,linestr):
        result=re.findall(r'[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}',linestr)
        if result:
            return result
        else:
            result=[]
        return result
    '''
    针对每一个类文件进行分析
    '''
    def analyze(self):
        count,lincount,c=0,0,0
        for linestr in self.classbytecode:
            lincount += 1
            for sensitiveapi in fastmoderules:
                if sensitiveapi in  str(linestr):
                    self.result.setdefault(str(count),{})
                    self.result[str(count)]["sensitiveAPI"]=sensitiveapi
                    self.result[str(count)]["desc"]=fastmoderules.get(sensitiveapi)
                    self.result[str(count)]["linecount"]=str(lincount)
                    self.result[str(count)]["path"]=self.classpath
                    count+=1
                    break

            for key,val in flawsSink.items():
                flag=False
                for sink in val.get("item"):
                    if sink in str(linestr):
                        flag=True
                        self.flawresult.setdefault(str(c),{})
                        self.flawresult[str(c)]["flawsName"]=val.get("flawsname")
                        self.flawresult[str(c)]["desc"]=val.get("desc")
                        self.flawresult[str(c)]["suggest"]=val.get("suggest")
                        self.flawresult[str(c)]["linecount"]=str(lincount)
                        self.flawresult[str(c)]["path"]=self.classpath
                        c += 1
                        break
                if flag==True:
                    break

            ipinfo=self.getallIP(str(linestr))
            ipv6info=self.getallipv6(str(linestr))
            urlinfo=self.geturl(str(linestr))
            emailinfo=self.getemail(str(linestr))
            if len(ipinfo)>0:
                for ip in ipinfo:
                    self.ipv4.add(ip)
            elif len(ipv6info)>0:
                for ip in ipv6info:
                    self.ipv6.add(ip)
            elif len(urlinfo)>0:
                for url in urlinfo:
                    self.urls.add(url)
            elif len(emailinfo)>0:
                for email in emailinfo:
                    self.emails.add(email)
        lincount+=1
        return self.result,self.ipv4,self.ipv6,self.urls,self.emails,self.flawresult
if __name__ == '__main__':
    fa=fastAnalyze(classpath="test.smali")
    fa.analyze()
