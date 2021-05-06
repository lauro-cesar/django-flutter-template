from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class MoviesConfig(AppConfig):
	name = 'movies'
	verbose_name=_('Movies')

	def ready(self):
		import movies.signals
