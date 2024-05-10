from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.text_box_1.text
    weight = int(self.text_box_2.text)
    address = self.text_box_3.text
    mobileNo = int(self.text_box_4.text)
    personaltraining  = self.check_box_1.checked
    anvil.server.call('submit', name=name, weight=weight, address=address, mobileNo = mobileNo, personaltraining =personaltraining)
    Notification("Your response has been recorded").show()

  def text_box_4_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
