#coding:utf-8
#Python中声明文件编码的注释，编码格式指定为utf-8
import time					#导入time库，可使用时间函数。
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)	##信号引脚模式定义，使用.BCM模式
Sign = 11				##信号输出的IO口定义

GPIO.setwarnings(False)
GPIO.setup(Sign,GPIO.OUT,initial=GPIO.LOW)##Sign初始化为低电平

def	do_action():		##定义功能函数，在其他地方调用此函数。未调用不执行。
	GPIO.output(Sign,True)##把电平拉高，蜂鸣器模块发出声音
	time.sleep(1)##延迟1秒
	GPIO.output(Sign,False)##把电平拉低，，蜂鸣器模块停止发出声音
	time.sleep(1)
	
for i in range(1,5):		#调用rang（）循环函数，功能类似 for（i =1;i<5;i++ ）执行4遍
	do_action()
'''
整个程序功能为：
	接在驱动板上IO11位置的蜂鸣器发出滴声，持续1秒，然后停止发声，再持续1秒
	持续循环4遍
'''