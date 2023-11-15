from ._anvil_designer import Lender_reg_form_1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_form_1(Lender_reg_form_1Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    name = self.text_box_1.text
    gender = self.drop_down_1_copy_1.selected_value
    city = self.text_box_2.text
    user_id = self.userId
    

    if not name or not gender or not city:
     Notification("Please fill all fields").show()
    else:
      anvil.server.call('add_lendor_frist_form',name,gender,city,user_id)
      open_form('lendor_registration_form.Lender_reg_form_2',user_id = user_id)
      self.clear_inputs()
  def clear_inputs(self):
    self.text_box_1.text = ''
    self.drop_down_1_copy_1.selected_value = ''
    self.text_box_2.text = ''

  def button_1_click(self, **event_args):
    open_form('bank_users.user_form')
    """This method is called when the button is clicked"""

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("bank_users.user_form")
    
      
     
    
