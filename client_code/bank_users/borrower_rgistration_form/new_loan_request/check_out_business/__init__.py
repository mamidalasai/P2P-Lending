from ._anvil_designer import check_out_businessTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import borrower_main_form_module

class check_out_business(check_out_businessTemplate):
  def __init__(self, **properties):
     #self.user_id=main_form_module.userId
    self.user_id=1000
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.names = ' Business loan '
    user_request = app_tables.product_borrower.get(names=self.names)

    if user_request:
            interest_rate = user_request['interest_rate']
            self.int_rate.text = f"Interest rate : {interest_rate} %"
    else:
            self.int_rate.text = "Interest rate not found."

    all_requests = app_tables.loan_details.search()

    if all_requests:
            most_recent_request = None

            for request in all_requests:
                if most_recent_request is None or request['timestamp'] > most_recent_request['timestamp']:
                    most_recent_request = request

            self.customer_id = most_recent_request['coustmer_id']
            min_amount = most_recent_request['min_amount']
            tenure = most_recent_request['tenure']
            max_amount = most_recent_request['max_amount']

            min_amount = float(min_amount)  # Convert to float
            tenure = float(tenure)  # Convert to float
            max_amount = float(max_amount)

            total_repayment = min_amount + (min_amount * (interest_rate / 100) * tenure)
            self.trp_amount.text = f"Total Repayment Amount : {total_repayment}"

            P = float(total_repayment)
            r = float(interest_rate) / 12 / 100
            n = int(tenure)

            emi = P * r * (1 + r)**n / ((1 + r)**n - 1)
            processing_fee = min_amount * tenure * (interest_rate / 100)
            self.pro_fee.text = f"Processing fee : {processing_fee}"

            self.emi_details.text = f"EMI Details: {emi:.2f}"
    else:
            self.trp_amount.text = "No user profile data available."

    # Any code you write here will run before the form opens.

  def submit_click(self, **event_args):
    alert('your data was submitted')
    open_form('bank_users.borrower_rgistration_form')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form.new_loan_request.business_loan')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form')

 