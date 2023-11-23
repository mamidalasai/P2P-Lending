from ._anvil_designer import forecloseTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

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
    paid_amount = monthly_installment * payment_done
    paid_amount = int(paid_amount)

    remaining_amount = min_amount - paid_amount
    remaining_amount = int(remaining_amount)

    penalty_rate = 0.03  # 3%
    penalty_amount = remaining_amount * penalty_rate
    penalty_amount = int(penalty_amount)
    total_due_amount = remaining_amount + penalty_amount
    total_due_amount = int(total_due_amount)

    self.ra_label.text = f"{remaining_amount}"
    self.tda_label.text = f"{total_due_amount}"
    self.emi_label.text = f"{emi}  (per month)"
    self.pa_label.text = f"{penalty_amount}"
    self.paid_label.text = f"{paid_amount}"
    self.paid_output.text = f"You paid {paid_amount} rs for {payment_done} months"
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form')
