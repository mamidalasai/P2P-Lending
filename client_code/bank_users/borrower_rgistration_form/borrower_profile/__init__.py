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
    user_id=get_current_userid()
    # Any code you write here will run before the form opens.
    user_profile=anvil.server.call('get_user_profile',user_id)
    self.full_name_label.text=user_profile['full_name']
    self.email_id_label.text=user_profile['email_user']
    self.mobile_no_label.text=user_profile['mobile']
    self.date_of_birth_label.text=user_profile['date_of_birth']
    self.city_label.text=user_profile['city']
    self.pan_no_label.text=user_profile['pan_number']
    self.aadhaar_no_label.text=user_profile['aadhaar_no']
    self.gender_label.text=user_profile['gender']
    self.mother_tounge_label.text=user_profile['mouther_tounge']
    self.marrital_status_label.text=user_profile['marital_status']
    self.user_type_label.text=user_profile['usertype']
  def button_1_click(self, **event_args):
    open_form('bank_users.borrower_rgistration_form.boorrower_edit_profile')

  def button_1_copy_click(self, **event_args):
    open_form('bank_users.borrower_rgistration_form')
