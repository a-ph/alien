import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# 创建play 按钮
	play_button = Button(ai_settings, screen, "Play")

	# 创建一个用于存储游戏统计信息的实例，并创建记分牌
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)

	# 创建一艘飞船, 一个子弹编组和一个外星人编组
	ship = Ship(ai_settings, screen)
	# 创建一个用于存储子弹的编组
	bullets = Group()

	# set bgcolor
	bg_color = (230, 230, 230)

	aliens = Group()
	#创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# start game
	while True:
		# observe keybord mose event
		gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, 
 bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()