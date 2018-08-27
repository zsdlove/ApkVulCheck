'''
WebviewHideAPI_Check
for detecting webview hidden api flaw
if the target class contains 
  removeJavascriptInterface
  "searchBoxJavaBridge_"
  "accessibility"
  "accessibilityTraversal"
may be it is a potential webview flaw
				by zsdlove 
				2018/8/27
'''
import re
def WebviewHideAPI_Check(lines):
	m1=re.match(r'.*'+'removeJavascriptInterface'+'.*',lines)
	m2=re.match(r'.*'+'searchBoxJavaBridge_'+'.*',lines)
	m3=re.match(r'.*'+'accessibility'+'.*',lines)
	m4=re.match(r'.*'+'accessibilityTraversal'+'.*',lines)
	if m1 and m2 and m3 and m4:
		print("it is not a webview hidden api flaw")
		return False
	else :
		print("is potential webview hidden api flaw")
		return True