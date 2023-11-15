from ._anvil_designer import Lender_reg_individual_form_1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_individual_form_1(Lender_reg_individual_form_1Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    emp_type = self.drop_down_1.selected_value
    org_type = self.drop_down_2.selected_value
    company_name = self.text_box_1.text
    user_id = self.userId
    if not emp_type or not org_type or not company_name:
      Notification("please fill the required fields ").show()
    else:
      anvil.server.call('add_lendor_individual_form_1', company_name,org_type,emp_type,user_id)
    open_form('lendor_registration_form.Lender_reg_individual_form_2',user_id=self.userId)



  
  def button_1_click(self, **event_args):
    open_form('lendor_registration_form.Lender_reg_form_8',user_id=self.userId)

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass
   
    
