from ._anvil_designer import Lender_reg_form_2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_form_2(Lender_reg_form_2Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  

  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('lendor_registration_form.Lender_reg_form_1',user_id=user_id)

  def button_2_click(self, **event_args):
    #investment=self.drop_down_1.selected_value
    mobile = self.text_box_1.text
    email = self.text_box_2.text
    photo = self.file_loader_1.file
    user_id = self.userId
    if not mobile or not email or not photo :
      Notification("Please fill all the fields").show()
    else:
      anvil.server.call('add_lendor_second_form',mobile,email,photo,user_id)
      open_form('lendor_registration_form.Lender_reg_form_3',user_id = user_id)


  
  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("bank_users.user_form")
    
    
