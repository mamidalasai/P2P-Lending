from ._anvil_designer import Lender_reg_Institutional_form_5Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_Institutional_form_5(Lender_reg_Institutional_form_5Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    reg_off_add = self.text_box_1.text
    off_add_proof = self.text_box_2.text
    proof_verification = self.file_loader_1.file
    user_id = self.userId
    if not reg_off_add or not off_add_proof or not proof_verification:
      Notification("Please all the fields")
    else:
     anvil.server.call('add_lendor_institutional_form_5',reg_off_add,off_add_proof,proof_verification,user_id)
     open_form('lendor_registration_form.Lender_reg_bothdirect_bank_form_1',user_id=user_id)
    """This method is called when the button is clicked"""

  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('lendor_registration_form.Lender_reg_Institutional_form_4',user_id=user_id)
    """This method is called when the button is clicked"""

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("bank_users.user_form")
    
