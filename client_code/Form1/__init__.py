from ._anvil_designer import Form1Template
from anvil import *
from ..MovieEdit import MovieEdit


class Form1(Form1Template):
    def __init__(self, **properties):
        self.item = {
            'movie_name': 'Back to the Future',
            'year': 1985,
            'director': 'Robert Zemeckis',
            'summary': 'Doc Brown invents a nuclear powered time machine, which Marty McFly '
                       'then uses to nearly erase himself from existence.'
        }
        
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def edit_button_click(self, **event_args):
      editing_form = MovieEdit(item=self.item)
      alert(content=editing_form, large=True)
      self.refresh_data_bindings()
