from ._anvil_designer import star_1_borrower_registration_form_begin_7Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_7(star_1_borrower_registration_form_begin_7Template):
  def __init__(self,user_id, **properties):
    self.init_components(**properties)
    self.userId = user_id


  def button_1_click(self, **event_args):
    open_form('borrower_registration_form.Form22')

  def button_2_click(self, **event_args):
    open_form('borrower_registration_form.Form24')
