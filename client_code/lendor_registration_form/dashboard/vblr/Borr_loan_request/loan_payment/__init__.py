'''from ._anvil_designer import loan_paymentTemplate
from anvil import *

class loan_payment(loan_paymentTemplate):
    def __init__(self, selected_row, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.label_3.text = f"{selected_row['loan_id']}"
        self.selected_row = selected_row  # Make selected_row an instance variable

    def link_1_click(self, **event_args):
        """This method is called when the link is clicked"""
        pass

    def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.button_2.text = f"Pay {self.selected_row['loan_id']}"
        # Additional code for handling the button click if needed
        pass'''


from ._anvil_designer import loan_paymentTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..... import lender_main_module as main_form_module




class loan_payment(loan_paymentTemplate):
    def __init__(self, selected_row, **properties):
        self.user_id = main_form_module.userId
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.label_3.text = f"{selected_row['loan_id']}"
        self.selected_row = selected_row  # Make selected_row an instance variable

    def link_1_click(self, **event_args):
        """This method is called when the link is clicked"""
        pass

    def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        # Set the text of button_2
        self.button_2.text = f"Pay {self.selected_row['loan_id']}"
        
        
        # Store selected row data in loan_disbursement table
        try:
            app_tables.loan_disbursement.add_row(
                loan_id=self.selected_row['loan_id'],
                # Add other columns and their values as needed
                # Example: column_name=value
            )
        except Exception as e:
            # Handle any errors that may occur while adding the row
            print(f"Error adding row to loan_disbursement table: {e}")

        # Additional code for handling the button click if needed
        pass

