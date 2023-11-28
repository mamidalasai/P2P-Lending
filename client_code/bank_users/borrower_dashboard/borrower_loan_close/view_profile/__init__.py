from ._anvil_designer import view_profileTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...import borrower_main_form_module as main_form_module

class view_profile(view_profileTemplate):
  def __init__(self,selected_row, **properties):
    #self.user_id=main_form_module.userId
    #self.user_id=1000
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
   
    # Display loan details
    self.loan_id_label.text = f"{selected_row['loan_id']}"
    self.loan_amount_label.text=f"{selected_row['total_repayment_amount']}"
    self.intrest_rate_label.text=f"{selected_row['interest_rate']}"
    self.tenure_label.text=f"{selected_row['tenure']}"
    self.date_of_apply_label.text=f"{selected_row['timestamp']}"
    self.loan_updated_status_label.text=f"{selected_row['loan_updated_status']}"
    # Try to get user profile details
    try:
        user_request = app_tables.user_profile.get(coustmer_id=selected_row['coustmer_id'])
        if user_request is not None:
        # Assuming 'bank_acc_details' is a valid column name in the 'borrower' table
          full_name = user_request['full_name']
          email_id=user_request['email_user']
          mobile=user_request['mobile'] 
          aadhar_no =user_request['aadhaar_no']
          pan_number=user_request['pan_number']
          gender=user_request['gender']
          self.full_name_label.text = f"{full_name}"
          self.email_id_label.text=f"{email_id}"
          self.mobile_no_label.text=f"{mobile}"
          self.aadhar_no_label.text=f"{aadhar_no}"
          self.pan_no_label.text=f"{pan_number}"
          self.gender_label.text=f"{gender}"
    except Exception as e:
          print(f"Error fetching user profile details: {e}")

  def button_1_copy_click(self, **event_args):
    open_form('bank_users.borrower_dashboard')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_dashboard.borrower_loan_close')
