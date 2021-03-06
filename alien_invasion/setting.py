#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Setting():
	#存储《外星人入侵》的所有设置的类
	def __init__(self):
		#初始化游戏的设置
		#屏幕设置
		self.screen_width=1200
		self.screen_height=600
		self.bg_color=(230,230,230)
		#飞船的设置(centerx只能储存整数值)
		self.ship_speed_factor=1.5
		#子弹设置
		self.bullet_speed_factor=3#速度
		self.bullet_width=3#宽
		self.bullet_height=15#高
		self.bullet_color=60,60,60#颜色
		self.bullets_allowed=3#允许同时出现在屏幕的最大子弹数
		#外星人设置
		self.alien_speed_factor=1#左右移动速度
		self.fleet_drop_speed=10#上下移动速度
		#fleet_direction为1表示向右移，为-1表示向左移
		self.fleet_direction=1
		
	
