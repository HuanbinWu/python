#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author:HuanBing
#星座的确定
chinese_zodiac="猴雞狗豬鼠牛虎兔龍蛇馬羊"
zodiac_name=(u'摩羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',
             u'巨蟹座',u'狮子座',u'处女座',u'天秤座',u'天蝎座',u'射手座')
zodiac_days=((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),
             (7,23),(8,23),(9,23),(10,23),(11,23),(12,23))

cz_num={}
for i in chinese_zodiac:
    cz_num[i]=0
# z_num={}
# for i in zodiac_name:
#     z_num[i]= 0
z_num={i:0 for i in zodiac_name }
while True:
    #用户输入月份和日期
    year = int(input('请输入年份'))
    month=int(input('请输入月份'))
    day=int(input('请输入日期'))

    n=0
    while zodiac_days[n] <(month,day):
        if month == 12 and day > 23:
            break
        n+=1
    # 出生生肖和星座
    print(zodiac_name[n])
    print('%s 年的生肖%s'% (year,chinese_zodiac[year%12]))
    cz_num[chinese_zodiac[year%12]]+=1
    z_num[zodiac_name[n]]+=1
    #生肖和星座的统计信息
    for each_key in cz_num.keys():
        print ('生肖%s 有 %d 个' %(each_key,cz_num[each_key]))
    for each_key in z_num.keys():
         print ('星座 %s 有 %d 个'  %(each_key,z_num[each_key]))