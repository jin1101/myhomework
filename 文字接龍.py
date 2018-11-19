print('五次失敗就會退出遊戲')
x=input('請輸入一個字串:')
errorCount=0
while errorCount < 5:
	y=input('請輸入-'+x[-1]+'-開始字串:')
	if y[0] !=x[-1]:
		errorCount+=1
		print('輸入錯誤,累積錯誤次數='+str(errorCount))
	else:
		x=x+'-'+y
		print('上一個字串是'+x)
