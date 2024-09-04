class Settings(object):
	"""docstring for Settings"""
	def __init__(self):
		super(Settings, self).__init__()
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		self.ship_speed_factor = 1.5
		# 子弹设置
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60 ,60
		self.bullets_allowed = 3
		