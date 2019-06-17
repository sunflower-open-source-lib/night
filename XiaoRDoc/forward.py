#coding:utf-8
import os
import time
import RPi.GPIO as GPIO

#######################################
#############�ź����Ŷ���##############
#######################################
GPIO.setmode(GPIO.BCM)

########��������ӿڶ���#################
ENA = 13	#//L298ʹ��A
ENB = 20	#//L298ʹ��B
IN1 = 19	#//����ӿ�1
IN2 = 16	#//����ӿ�2
IN3 = 21	#//����ӿ�3
IN4 = 26	#//����ӿ�4


#########�����ʼ��ΪLOW##########
GPIO.setup(ENA,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ENB,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)

#########������ǰ������##########
def Motor_Forward():
	print 'motor forward'
	GPIO.output(ENA,True)
	GPIO.output(ENB,True)
	GPIO.output(IN1,True)
	GPIO.output(IN2,False)
	GPIO.output(IN3,True)
	GPIO.output(IN4,False)
#########������ǰ������##########
def Motor_Stop():
	print 'motor stop'
	GPIO.output(ENA,True)
	GPIO.output(ENB,True)
	GPIO.output(IN1,False)
	GPIO.output(IN2,False)
	GPIO.output(IN3,False)
	GPIO.output(IN4,False)
	
while True:
	Motor_Forward()
	time.sleep(1)
	Motor_Stop()
	time.sleep(1)