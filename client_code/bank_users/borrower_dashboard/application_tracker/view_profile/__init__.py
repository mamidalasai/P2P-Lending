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
    def __init__(self, selected_row, **properties):
        # self.user_id=main_form_module.userId
        # self.user_id=1000
        self.init_components(**properties)
    def button_1_copy_click(self, **event_args):
      open_form('bank_users.borrower_dashboard')

    def button_1_click(self, **event_args):
     """This method is called when the button is clicked"""
     open_form('bank_users.borrower_dashboard.application_tracker')

        # Any code you write here will run before the form opens.
     self.loan_id_label.text = f"{selected_row['loan_id']}"
     try:
       app_tables.user_profile.get(coustmer_id=str)
            user_request = app_tables.us.get(coustmer_id=str(selected_row['coustmer_id']))
            if user_request is not None:
                # Assuming 'bank_acc_details' is a valid column name in the 'borrower' table
                bank_acc_details = user_request['bank_acc_details']
                borrower_approve_date_time = user_request['borrower_approve_date_time']
                self.label_member_since.text = f"{borrower_approve_date_time}"
                self.label_bank_acc_details.text = f"{bank_acc_details}"
