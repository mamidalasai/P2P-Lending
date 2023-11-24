from ._anvil_designer import forecloseTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime

class foreclose(forecloseTemplate):
  def __init__(self, selected_row, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.selected_row = selected_row 
        # Any code you write here will run before the form opens.
    min_amount = selected_row['min_amount']
    payment_done = selected_row['payment_done']
    tenure = selected_row['tenure']  # Assuming tenure is given in months

        # Calculate EMI
    monthly_interest_rate = selected_row['interest_rate'] / (12 * 100)  # Assuming interest rate is in percentage
    factor = (1 + monthly_interest_rate) ** tenure  # Calculate (1 + r)^t without using pow
    emi = min_amount * monthly_interest_rate * factor / (factor - 1)
    emi = int(emi)

    monthly_installment = min_amount / tenure
    paid_amount = emi * payment_done
    paid_amount = int(paid_amount)

    remaining_amount = min_amount - monthly_installment*payment_done
    remaining_amount = int(remaining_amount)

   
    

    penalty_rate = 0.03  # 3%
    penalty_amount = remaining_amount * penalty_rate
    penalty_amount = int(penalty_amount)
    total_due_amount = remaining_amount + penalty_amount
    total_due_amount = int(total_due_amount)

    self.ra_label.text = f"{remaining_amount}"
    self.tda_label.text = f"{total_due_amount}"
    self.emi_label.text = f"{emi}"
    self.pa_label.text = f"{penalty_amount}"
    self.paid_label.text = f"{paid_amount}  ({payment_done} months)"
    self.mi_label.text = f"{monthly_installment}"
    #self.fir_label.text = f"{}"
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form.borrower_foreclosure_request.borrower_foreclosure', selected_row= self.selected_row)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    alert('Submitting a foreclosure request implies acknowledgment and acceptance of financial and legal consequences, adhering to established timelines and communication protocols.')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.f_checkbox.checked:
        # Get the reason entered by the user
        reason = self.reason_textbox.text.strip()

        if reason:
           
                app_tables.foreclosure.add_row(
                    loan_id=self.selected_row['loan_id'],
                    borrower_name=self.selected_row['full_name'],
                    remaining_amount=self.ra_label.text,
                    total_due_amount=self.tda_label.text,
                    emi_amount=self.emi_label.text,
                    paid_amount=self.paid_label.text,
                    penalty_amount=self.pa_label.text,
                    requested_on=datetime.now(),
                    reason=reason
                )

               
                alert('Foreclosure request submitted successfully! pay amount now.')
         
        else:
            alert('Please enter a reason for foreclosure.')
    else:
        alert('Please accept the Terms and Conditions.')
