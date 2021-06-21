# 密碼重試程式
# password = 'a123456'
# 使用者可重複輸入密碼
# 最多三次
# 如果正確 就印出 "登入成功"
# 如果不正確就印出 "密碼錯誤! 還有__幾次機會"

password = 'a123456'
c = 3 # 剩餘機會
while c > 0:
	q = input('請輸入密碼:') 
	if q == password:
		print('登入成功!')
		break 
	else:
		c = c - 1
		print('密碼錯誤!還有',c ,'次機會')