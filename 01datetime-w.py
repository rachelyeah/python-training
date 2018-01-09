import time
import datetime
import pytz
from datetime import tzinfo, timezone


#将时间戳转换成  年 月 日
timeStamp = 123456789
form1 = time.localtime(123456789)
form2 = time.strftime("%Y年%m月%d日", form1)
print(1, form2)


#算出utc时间并在utc时间上加上2
form3 = datetime.datetime.utcnow()
print(2, form3)
form4 = form3 + datetime.timedelta(hours=2)
print(3, form4)





#将2017-07-18转换成2017年07月18日
form5 = time.strptime('2017-07-18', "%Y-%m-%d")
form6 = time.strftime("%Y年%m月%d日", form5)
print(5, form6)



#用Asia/Shanghai时间求出本地时间
form8 = datetime.datetime.now()
form9 = time.mktime(form8.timetuple())
print(4, form9)
form11 = datetime.datetime.utcfromtimestamp(form9)
form10 = datetime.datetime.fromtimestamp(form9, pytz.timezone('Asia/Shanghai'))
print(8, form11)
print(7, form10)