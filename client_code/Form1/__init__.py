from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..MovieEdit import MovieEdit

class Form1(Form1Template):
    def __init__(self, **properties):
        # self.item = {
        #     'movie_name': 'Back to the Future',
        #     'year': 1985,
        #     'director': 'Robert Zemeckis',
        #     'summary': 'Doc Brown invents a nuclear powered time machine, which Marty McFly '
        #                'then uses to nearly erase himself from existence.'
        # }
        self.item = app_tables.movies.search()[0]
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def edit_button_click(self, **event_args):
      item = dict(self.item)
      editing_form = MovieEdit(item=item)
      alert(content=editing_form, large=True)
      anvil.server.call('update_movie', item)
      self.item = app_tables.movies.search()[0]
      self.refresh_data_bindings()