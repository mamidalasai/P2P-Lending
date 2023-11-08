from ._anvil_designer import Lender_reg_form_7Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_form_7(Lender_reg_form_7Template):
  def __init__(self, user_id,**properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    landmark = self.text_box_1.text
    city = self.text_box_2.text
    state = self.text_box_3.text
    pincode = self.text_box_4.text
    user_id = self.userId
    anvil.server.call('add_lendor_seven_form',landmark,city,state,pincode,user_id)
    
    open_form('lendor_registration_form.Lender_reg_form_8',user_id = user_id)
    """This method is called when the button is clicked"""

  def button_1_click(self, **event_args):
    open_form('lendor_registration_form.Lender_reg_form_6')
    """This method is called when the button is clicked"""

  def text_box_4_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
    
