from ._anvil_designer import loan_paymentTemplate
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
        pass
