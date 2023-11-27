from ._anvil_designer import borrower_foreclosureTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class borrower_foreclosure(borrower_foreclosureTemplate):
  def __init__(self, selected_row, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_loan_id.text = f"{selected_row['loan_id']}"
    self.label_name.text = f"{selected_row['full_name']}"
    self.label_loan_amount.text = f"{selected_row['min_amount']}"
    self.label_loan_tenure.text = f"{selected_row['tenure']} Months"
    self.label_interest_rate.text = f"{selected_row['interest_rate']} %  pa"
    self.label_credit_limit.text = f"{selected_row['max_amount']}"
    self.label_tpm.text = f"{selected_row['payment_done']}"

        # Save selected_row as an instance variable for later use
    self.selected_row = selected_row
  def button_foreclose_click(self, **event_args):
    """This method is called when the button is clicked"""
    selected_row = self.selected_row

    payment_done = selected_row['payment_done']

    if payment_done > 12:
          open_form('bank_users.borrower_dashboard.borrower_foreclosure_request.borrower_foreclosure.foreclose', selected_row=selected_row)

         
    else:
          alert('You are not eligible for foreclosure! You have to pay atleast 12 months. ')

   
    
        

  def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard.borrower_foreclosure_request')

  def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard')

  

  

  

  
  

 
  

  
