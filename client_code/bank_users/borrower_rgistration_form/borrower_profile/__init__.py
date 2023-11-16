from ._anvil_designer import borrower_profileTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class borrower_profile(borrower_profileTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user_id=get_current_user_id()
    # Any code you write here will run before the form opens.
    user_profile=anvil.server.call('add_borrower_step1',user_id)
    self.full_name_label.text=user_profile['full_name']
  def button_1_click(self, **event_args):
    open_form('bank_users.borrower_rgistration_form.boorrower_edit_profile')

  def button_1_copy_click(self, **event_args):
    open_form('bank_users.borrower_rgistration_form')
