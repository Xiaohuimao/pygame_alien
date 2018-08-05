#引用pygame模块
import sys
import pygame
from setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
def run_game():
	#初始化游戏并创建一个屏幕对象
	#初始化背景设置
	pygame.init()
	ai_settings=Setting()
	#pygame.display.set_mode()用于创建一个屏幕，参数为一个元组（长，高）
	screen=pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	#pygame.display.set_caption()方法用于给屏幕命名
	pygame.display.set_caption("打爆薛琨")
	#创建一艘飞船
	ship=Ship(ai_settings,screen)
	#创建一个用于储存子弹的编组和一个外星人的编组
	bullets=Group()
	aliens=Group()
	#创建外星人群
	gf.create_fleet(ai_settings,screen ,aliens)
	#开始游戏的主循环
	while True:
		#监视键盘和鼠标事件（事件是用户玩游戏时执行的操作）
		#用户的所有事件
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullets(bullets)
		#print(len(bullets))
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)
run_game()

