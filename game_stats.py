
class GameStats():
	"""docstring for GameStats"""
	def __init__(self, ai_settings):
		super(GameStats, self).__init__()
		self.ai_settings = ai_settings
		self.reset_stats()
		# 游戏刚启动时处于活跃状态
		self.game_active = True

	def reset_stats(self):
		"""初始化在游戏运行期间可能变化的统计信息"""
		self.ships_left = self.ai_settings.ship_limit
		