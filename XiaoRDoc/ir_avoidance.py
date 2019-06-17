#coding:utf-8
#Python中声明文件编码的注释，编码格式指定为utf-8
import time					#导入time库，可使用时间函数。
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)	##信号引脚模式定义，使用.BCM模式
LED = 10				##LED0的IO口定义
Sign = 11				##输入信号管脚定义

GPIO.setwarnings(False)
GPIO.setup(LED,GPIO.OUT,initial=GPIO.HIGH)##led初始化为高电平，此时灯熄灭（灌电流模式）
GPIO.setup(Sign,GPIO.IN,pull_up_down=GPIO.PUD_UP)##Sign初始化输入,并内部拉高

def	do_action():		##使用def定义函数，可在其他地方调用此函数。未调用不执行。
	if GPIO.input(Sign) == False:
		GPIO.output(LED,False)	#红外避障传感器被触发，把LED管脚的电平拉低，LED灯亮起
	else:
		GPIO.output(LED,True)	#红外避障传感器未被触发，把LED管脚的电平拉高，LED灯熄灭
	
while True:		#循环函数
	do_action()
'''
整个程序功能为：
	如果红外避障传感器被触发，那么主板上的LED灯亮起，否则熄灭
	程序结束
'''