#-*-coding:utf-8-*-

class mobileSDKAnalysis():
    def __init__(self):
        self.nastySDK={
	        "com.shunwang.service.alarm":u"顺网恶意SDK",
	        "com.karumi.dexter.DexterActivity":u"Android动态权限申请",
            "com.github.dfqin.grantor.PermissionActivity":u"Android动态权限申请",
            "com.yanzhenjie.permission.PermissionActivity":u"Android动态权限申请",
            "pub.devrel.easypermissions.AppSettingsDialogHolderActivity":u"Android动态权限申请",
            "com.igexin.sdk.GActivity": u"个推开机自启动组件",
            "com.yy.pushsvc.impl.KeepAliveActivity":u"个推开机唤醒组件",
}
        self.Advertisement={
            "com.pad.android_independent_video_sdk.view.IndependentVideoActivity":u"多盟广告平台",
            "com.qq.e.ads.ADActivity":u"腾讯广告联盟",
            "com.qq.e.comm.DownloadService":u"腾讯广告联盟",
            "com.baidu.mobads.AppActivity":u"百度广告联盟",
            "com.xiaomi.gamecenter.sdk.ui.MiActivity":u"小米移动广告联盟",
            "com.xiaomi.gamecenter.sdk.ui.PayListActivity":u"小米移动广告联盟",
            "com.xiaomi.hy.dj.HyDjActivity":u"小米移动广告联盟",
            "com.xiaomi.gamecenter.push.GamePushService":u"小米移动广告联盟",
            "com.xiaomi.gamecenter.push.OnClickReceiver":u"小米移动广告联盟",
            "com.xiaomi.gamecenter.sdk.utils.MiFileProvider":u"小米移动广告联盟",
            "com.xiaomi.gamecenter.sdk.ui.fault.ViewFaultNoticeActivity":u"小米移动广告联盟",
            "com.xiaomi.gamecenter.sdk.ui.notice.NoticeActivity":u"小米移动广告联盟",
            "com.xiaomi.push.service.XMPushService":u"小米消息推送",
            "com.xiaomi.push.service.XMJobService":u"小米消息推送",
            "com.xiaomi.mipush.sdk.PushMessageHandler":u"小米消息推送",
            "com.xiaomi.mipush.sdk.MessageHandleService":u"小米消息推送",
            "com.xiaomi.push.service.receivers.NetworkStatusReceiver":u"小米消息推送",
            "com.xiaomi.push.service.receivers.PingReceiver":u"小米消息推送",
            "com.xiaomi.assemble.control.HmsPushReceiver":u"小米消息推送",
            "com.xiaomi.assemble.control.DistributeActivity":u"小米消息推送",
            "com.xiaomi.assemble.control.COSPushMessageService":u"小米消息推送",
            "com.qq.e.comm.DownloadService": u"腾讯广告联盟",
            "com.qq.e.ads.ADActivity": u"腾讯广告联盟",
            "com.taobao.accs.ChannelService$KernelService":u"淘宝推送",
            "com.taobao.accs.internal.AccsJobService":u"淘宝推送",
            "com.taobao.accs.ServiceReceiver":u"淘宝推送",
            "com.taobao.accs.data.MsgDistributeService":u"淘宝推送",
            "com.taobao.agoo.AgooCommondReceiver":u"淘宝推送",
            "com.alipay.pushsdk.thirdparty.hw.HuaWeiPushReceiver":u"支付宝推送",
            "com.mob.MobProvider":u"MobTech推送",
            "com.meizu.cloud.pushsdk.SystemReceiver":u"魅族推送",
            "com.meizu.cloud.pushsdk.NotificationService":u"魅族推送",
            "com.yy.pushsvc.thirdparty.PushVivoPushReceiver":u"个推消息推送",
            "com.yy.pushsvc.thirdparty.PushMeizuPushReceiver":u"个推消息推送",
            "com.yy.pushsvc.services.PushOppoMsgService":u"个推消息推送",
            "com.yy.pushsvc.services.PushGTIntentService":u"个推消息推送",
            "com.yy.pushsvc.services.GeTuiService":u"个推消息推送",
            "com.igexin.sdk.PushActivity":u"个推消息推送",
            "com.igexin.sdk.PushService":u"个推消息推送",
            "com.yy.pushsvc.impl.PushOppoActivity":u"个推消息推送",
            "com.yy.pushsvc.thirdparty.PushHuaweiPushReceiver":u"个推消息推送",
            "com.yy.pushsvc.JobSchedulerService":u"个推消息推送",
            "com.huawei.hms.update.provider.UpdateProvider":u"华为消息推送",
            "com.huawei.hms.support.api.push.PushEventReceiver":u"华为消息推送",
            "com.huawei.android.pushagent.PushBootReceiver":u"华为消息推送",
            "com.huawei.hms.activity.BridgeActivity":u"华为消息推送",
            "com.huawei.push.service.receivers.HWPushMessageHandler":u"华为消息推送",
            "com.huawei.hms.support.api.push.service.HmsMsgService":u"华为消息推送",
            "com.huawei.updatesdk.service.deamon.download.DownloadService":u"华为消息推送",
            "com.huawei.android.hms.agent.common.HMSAgentActivity":u"华为消息推送",
            "com.umeng.message.provider.MessageProvider":u"友盟消息推送",
            "com.umeng.message.UmengMessageIntentReceiverService":u"友盟消息推送",
            "com.umeng.message.UmengDownloadResourceService":u"友盟消息推送",
            "com.umeng.message.UmengMessageCallbackHandlerService":u"友盟消息推送",
            "com.umeng.message.NotificationProxyBroadcastReceiver":u"友盟消息推送",
            "com.umeng.message.XiaomiIntentService":u"友盟消息推送",
            "com.umeng.message.UmengIntentService":u"友盟消息推送",
            "cn.jpush.android.service.PluginVivoMessageReceiver":u"极光消息推送",
            "cn.jpush.android.service.PluginMeizuPlatformsReceiver":u"极光消息推送",
            "cn.jpush.android.service.PluginHuaweiPlatformsReceiver":u"极光消息推送",
            "cn.jpush.android.service.PluginXiaomiPlatformsReceiver":u"极光消息推送",
            "cn.jiguang.user.service.action":u"极光消息推送",
            "com.netease.nimlib.service.ResponseService":u"网易云消息推送",
            "com.netease.nimlib.mixpush.mz.MZPushReceiver":u"网易云消息推送",
            "com.netease.nimlib.ipc.NIMContentProvider":u"网易云消息推送",
            "com.netease.nimlib.service.ResponseReceiver":u"网易云消息推送",
            "com.netease.nimlib.service.NimReceiver":u"网易云消息推送",
            "com.netease.nimlib.job.NIMJobService":u"网易云消息推送",
            "com.netease.nimlib.job.NIMJobService":u"网易云消息推送",
            "com.netease.nimlib.service.NimService":u"网易云消息推送",
            "com.vivo.push.sdk.LinkProxyClientActivity":u"vivo消息推送",
            "com.vivo.push.sdk.service.CommandClientService":u"vivo消息推送",
}
        self.thirdpartPayAPI={
	        "com.alipay.sdk.app.H5PayActivity":u"支付宝支付接口",
	        "com.unionpay.uppay.PayActivity":u"银联支付接口",
	        "com.jdpaysdk.author.browser.BrowserActivity":u"银联支付接口",
}
        self.otherSDKs={
            "com.baidu.location.f":u"定位,百度地图API接口",
            "com.tencent.qalsdk.service.QalService":u"通讯,腾讯云通信API接口",
            "com.tencent.qalsdk.service.QalAssistServices":u"通讯,腾讯云通信API",
            "com.tencent.qalsdk.QALBroadcastReceiver":u"通讯,腾讯云通信API",
            "com.tencent.qalsdk.core.NetConnInfoCenter":u"通讯,腾讯云通信API",
            "com.tencent.tauth.AuthActivity":u"第三方登陆,腾讯登入授权API",
            "com.tencent.tinker.lib.service.TinkerPatchForeService":u"腾讯热更新API",
            "com.tencent.tinker.lib.service.DefaultTinkerResultService":u"腾讯热更新API",
            "com.tencent.tinker.loader.hotplug.ActivityStubs$SIStub_02_T":u"腾讯热更新API",
            "com.tencent.connect.common.AssistActivity":u"腾讯热更新API",
            "com.tencent.tinker.lib.service.TinkerPatchService":u"腾讯热更新API",
            "com.tencent.tinker.lib.service.TinkerPatchService$InnerService":u"腾讯热更新API",
            "com.tencent.av.screen.MediaProjectionPermissionCheckActivity":u"腾讯API,弹窗并请求屏幕录制/截屏权限",
            "tinker.sample.android.service.SampleResultServic":u"Android热修复",
            "com.google.ar.core.InstallActivity":u"Google AR设备API",
            "com.google.ar.core.min_apk_version":u"Google AR设备API",
        }

    def analysis(self,activityList):
        nastySDK={}#恶意sdk
        Advertisement={}#广告sdk
        thirdpartPayAPI={}#第三方支付sdk
        otherSDKs={}#其他一些工具sdk
        for activity in activityList:
            for key,value in self.nastySDK.items():
                if key==activity:
                    nastySDK[key]=value
            for key,value in self.Advertisement.items():
                if key==activity:
                    Advertisement[key]=value
            for key,value in self.thirdpartPayAPI.items():
                if key==activity:
                    thirdpartPayAPI[key]=value
            for key,value in self.otherSDKs.items():
                if key==activity:
                    otherSDKs[key]=value
        return nastySDK,Advertisement,thirdpartPayAPI,otherSDKs
if __name__ == '__main__':
    activitList=[
        'com.pad.android_independent_video_sdk.view.IndependentVideoActivity',
        'com.alipay.sdk.app.H5PayActivity',
        'com.karumi.dexter.DexterActivity',
        'com.xiaomi.hy.dj.HyDjActivity'
    ]
    msa=mobileSDKAnalysis()
    print(msa.analysis(activitList))