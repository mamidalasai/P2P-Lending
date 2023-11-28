from ._anvil_designer import view_profileTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import borrower_main_form_module as main_form_module

class view_profile(view_profileTemplate):
  def __init__(self, **properties):
    self.user_id=main_form_module.userId
    #self.user_id=1000
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    user_profile=app_tables.user_profile.get(coustmer_id=self.user_id)
    if user_profile:

      self.full_name_label.text=user_profile['full_name']
      self.email_id_label.text=user_profile['email_user']
      self.mobile_no_label.text=user_profile['mobile']
      self.city_label.text=user_profile['city']
      self.gender_label.text=user_profile['gender']
      user_profile=app_tables.loan_details.get(coustmer_id=self.user_id)
      if user_profile:
        self.label_4.text=user_profile['loan_updated_status']

  def button_1_copy_click(self, **event_args):
    open_form('bank_users.borrower_dashboard')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_dashboard.application_tracker')
