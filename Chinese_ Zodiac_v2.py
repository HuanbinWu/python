#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author:HuanBing
#记录生肖，根据用户输入的年份判断生肖
chinese_zodiac="猴雞狗豬鼠牛虎兔龍蛇馬羊"
#print (chinese_zodiac[0:4])
#print (chinese_zodiac[-1])
# year=int(input('请用户输入出生年份'))
# if (chinese_zodiac[year%12]=='狗'):
#      print ('狗年的运势')
# for cz in chinese_zodiac:
#     print (cz)
# for i in range(1,13):
#     print(i)
# for year in range(2000,2019):
#     print('%s 年的生肖是 %s' %(year,chinese_zodiac[year%12]))
import  time
num=5
while True:
    num = num+1
    if num==10:
       continue
    print(num)
    time.sleep(1)
