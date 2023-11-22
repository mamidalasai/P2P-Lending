from ._anvil_designer import Lender_reg_form_3eTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_form_3e(Lender_reg_form_3eTemplate):
  def __init__(self, user_id,**properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    qualification = self.drop_down_1.selected_value
    certificate = self.file_loader_1.file
    user_id = self.userId
    if not qualification or not certificate:
      Notification("Please fill all the fields")
    else:
      anvil.server.call('add_lendor_third_3e_form',qualification,certificate,user_id)
      open_form('lendor_registration_form.Lender_reg_Institutional_form_3',user_id = user_id)
    """This method is called when the button is clicked"""

  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('lendor_registration_form.Lender_reg_form_2',user_id = user_id)
    """This method is called when the button is clicked"""

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("bank_users.user_form")
