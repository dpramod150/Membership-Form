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
    weight = self.text_box_2.number
    address = self.text_box_3.text
    mobile_no = self.text_box_4.number
    personal_training  = self.check_box_1.checked
    anvil.server.call('submit', name=name, weight=weight, address=address, mobile_no = mobile_no, personal=personal, )
    anvil.server.anvil.Notification (message, (title""), {})
