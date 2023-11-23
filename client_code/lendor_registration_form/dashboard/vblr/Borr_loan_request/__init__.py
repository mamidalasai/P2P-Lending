from ._anvil_designer import Borr_loan_requestTemplate
from anvil import *
import anvil.facebook.auth
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
#from ._anvil_designer import Borr_loan_requestTemplate
from anvil import open_form

# In Borr_loan_request class

class Borr_loan_request(Borr_loan_requestTemplate):
    def __init__(self, selected_row, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Populate labels with the selected row details
        self.label_user_id.text = f"{selected_row['coustmer_id']}"
        self.label_name.text = f"{selected_row['full_name']}"
        self.label_loan_amount_applied.text = f"{selected_row['min_amount']}"
        self.label_loan_acc_number.text = f"{selected_row['loan_acc_number']}"
        self.label_beseem_score.text = f"{selected_row['beseem_score']}"
        self.label_loan_tenure.text = f"{selected_row['tenure']}"
        self.label_member_rom.text = f"{selected_row['member_rom']}"
        self.label_member_since.text = f"{selected_row['timestamp']}"
        self.label_credit_limit.text = f"{selected_row['max_amount']}"
        self.label_bank_acc_details.text =f"{selected_row['borrower_bank_acc_details']}"

    def button_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form("lendor_registration_form.dashboard.vblr")
