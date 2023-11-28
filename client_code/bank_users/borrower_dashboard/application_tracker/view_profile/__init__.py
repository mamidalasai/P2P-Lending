from ._anvil_designer import view_profileTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import borrower_main_form_module as main_form_module

class view_profile(view_profileTemplate):
    def __init__(self, selected_row, **properties):
        self.init_components(**properties)

        # Display loan details
        self.loan_id_label.text = f"{selected_row['loan_id']}"
        self.loan_amount_label.text=f"{selected_row['total_repayment_amount']}"
        
        # Try to get user profile details
        try:
            user_request = app_tables.user_profile.get(coustmer_id=selected_row['coustmer_id'])
            if user_request is not None:
                # Assuming 'bank_acc_details' is a valid column name in the 'borrower' table
                full_name = user_request['full_name']
                email_id=user_request['email_user']
               # borrower_approve_date_time = user_request['borrower_approve_date_time']
                self.full_name_label.text = f"{full_name}"
                
        except Exception as e:
            print(f"Error fetching user profile details: {e}")

    def button_1_copy_click(self, **event_args):
        open_form('bank_users.borrower_dashboard')

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard.application_tracker')
