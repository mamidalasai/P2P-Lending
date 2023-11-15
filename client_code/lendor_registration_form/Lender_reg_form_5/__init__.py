from ._anvil_designer import Lender_reg_form_5Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_form_5(Lender_reg_form_5Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    martial = self.drop_down_1.selected_value
    spouse_profession = self.text_box_1.text
    spouse_number = self.text_box_2.text
    user_id = self.userId
    if not martial or not spouse_profession or not spouse_number:
      Notification("Please fill all the fields")
    else:
     anvil.server.call('add_lendor_five_form',martial,spouse_profession,spouse_number,user_id)
     open_form('lendor_registration_form.Lender_reg_form_6',user_id = user_id)
    """This method is called when the button is clicked"""

  def button_1_click(self, **event_args):
     user_id = self.userId
     open_form('lendor_registration_form.Lender_reg_form_4',user_id=user_id)
     """This method is called when the button is clicked"""

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("bank_users.user_form")
    
