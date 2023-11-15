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

  # next page form 2 
  def button_2_click(self, **event_args):
    name = self.text_box_1.text
    gender = self.drop_down_1_copy_1.selected_value
    date_of_birth = self.date_picker_1.date
    user_id = self.userId
    if not name or not gender or not date_of_birth:
      Notification("please fill all required fields")
    else:
      anvil.server.call('add_lendor_frist_form',name,gender,date_of_birth,user_id)
      open_form('lendor_registration_form.Lender_reg_form_2',user_id=user_id)

    
  def button_1_click(self, **event_args):
    open_form('bank_users.user_form')

  def button_3_click(self, **event_args):
    open_form("bank_users.user_form")
    
      
     
    
