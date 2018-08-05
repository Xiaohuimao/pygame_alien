#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pygame
from bullet import Bullet
from alien import Alien
def check_keydown_events(event,ai_settings,screen,ship,bullets):
	#������Ӧ
	if event.key==pygame.K_RIGHT:
		ship.moving_right=True
	elif event.key==pygame.K_LEFT:
		ship.moving_left=True
	elif event.key==pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key==pygame.K_q:
		sys.exit()
def check_keyup_events(event,ship):
	if event.key==pygame.K_RIGHT:
		ship.moving_right=False
	elif event.key==pygame.K_LEFT:
		ship.moving_left=False
def check_events(ai_settings,screen,ship,bullets):
	#��Ӧ����������¼�
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type==pygame.KEYUP:
			check_keyup_events(event,ship)
def fire_bullet(ai_settings,screen,ship,bullets):
	#�����û�дﵽ���ƣ��ͷ���һ���ӵ�
	#����һ���ӵ���������������bullets��
	if len(bullets)<ai_settings.bullets_allowed:
			new_bullet=Bullet(ai_settings,screen,ship)
			bullets.add(new_bullet)
def update_screen(ai_setting,screen,ship,aliens,bullets):
	#������Ļ�ϵ�ͼ�񣬲��л�������Ļ
	screen.fill(ai_setting.bg_color)
	#�ڷɴ��������˺����ػ������ӵ�
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	#draw()�Ա������drawʱ��pygame�Զ����Ʊ����ÿ��Ԫ��
	aliens.draw(screen)
	#��������Ƶ���Ļ�ɼ�
	pygame.display.flip()
def update_bullets(bullets):
	#�����ӵ���λ�ã���ɾ������ʧ���ӵ�
	#�����ӵ���λ��
	bullets.update()
	#ɾ������ʧ���ӵ�
	#��forѭ���У���Ӧ���б�������ɾ����Ŀ
	for bullet in bullets.copy():
		if bullet.rect.bottom<=0:
			bullets.remove(bullet)
def get_number_aliens_x(ai_settings,alien_width):
	#����ÿ�п����ɶ���������
	available_space_x=ai_settings.screen_width-2*alien_width
	number_aliens_x=int(available_space_x/(2*alien_width))
	return number_aliens_x
def create_alien(ai_settings,screen,aliens,alien_number):
	#����һ�������˲�������ڵ�ǰ��
	alien=Alien(ai_settings,screen)
	alien_width=alien.rect.width
	alien.x=alien_width+2*alien_width*alien_number
	alien.rect.x=alien.x
	aliens.add(alien)
def create_fleet(ai_settings,screen,aliens):
	#����������Ⱥ
	#����һ�������ˣ�������ÿ�п������ɶ��ٸ�������
	alien=Alien(ai_settings,screen)
	number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
	#������һ��������
	for alien_number in range(number_aliens_x):
		#����һ�������˲�������뵱ǰ��
		create_alien(ai_settings,screen,aliens,alien_number)
	
