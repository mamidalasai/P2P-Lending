from ._anvil_designer import user_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..user_form import user_module
from ..borrower_rgistration_form import borrower_main_form_module
from ..main_form import main_form_module

class user_form(user_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.email = main_form_module.email
    email=self.email
    self.name = user_module.get_name(email)
    self.user_id =  user_module.find_user_id(email)
    
    self.email = email
    if main_form_module.alert_mes(main_form_module.flag):
      print("user login")
    else:
      print("user login")

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
     alert("Logged out sucessfully")
     anvil.users.logout()
     open_form('bank_users.main_form')

  def home_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("bank_users.user_form1")

  def borrower_button_click(self, **event_args):
    userid = self.user_id
    user_data=app_tables.user_profile.get(coustmer_id=userid)
    if user_data:
      actual_count=user_data['form_count']
      print(actual_count)
      if actual_count==0:
        open_form('borrower_registration_form.star_1_borrower_registration_form_begin',user_id=userid)
      elif actual_count==1:
        open_form('borrower_registration_form.star_1_borrower_registration_form_begin_2',user_id=userid)
      elif actual_count==2:
        open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3',user_id=userid)
      elif actual_count==3:
        open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3a_1',user_id=userid)
      elif actual_count==4:
        open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3a',user_id=userid)
      elif actual_count==5:
        open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3c',user_id=userid)
        
    else:
     open_form('borrower_registration_form.star_1_borrower_registration_form_begin',user_id=userid)
     print(actual_count)
      
  def lendor_button_click(self, **event_args):
    userid = self.user_id
    open_form('lendor_registration_form.Lender_reg_form_1',user_id=userid)

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.grid_panel_3.visible = True
    self.grid_panel_3_copy_1.visible = False

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""

    self.grid_panel_3.visible = False
    self.grid_panel_3_copy_1.visible = True

    
  
    

  
