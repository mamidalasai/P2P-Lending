from ._anvil_designer import new_loan_requestTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class new_loan_request(new_loan_requestTemplate):
  def __init__(self, **properties):
    #self.userId=user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def  loan(self, min_amount, max_amount): 
    all_requests = app_tables.loan_details.search()

    if all_requests:
            most_recent_request = None

            for request in all_requests:
                if most_recent_request is None or request['timestamp'] > most_recent_request['timestamp']:
                    most_recent_request = request

            self.customer_id = most_recent_request['customer_id']
    user_request = app_tables.loan_details.get(customer_id=self.customer_id)
    max_amount = user_request['max_amount']
    self.max_amount.text=f"{max_amount}"
    # Any code you write here will run before the form opens.
    min_amount = self.min_amount.text  # Convert the string to a float
    max_amount = self.max_amount.text  # Convert the string to a float
    tenure = self.tenure.selected_value

    anvil.server.call('add_loan_details', min_amount, max_amount, tenure)
   
  def button_1_copy_click(self, **event_args):
    if self.check_box_1.checked:
     open_form('bank_users.borrower_rgistration_form.new_loan_request.loan_type') 
    else:
      alert('Please select Terms and Conditions')
    def button_1_click(self, **event_args):
      open_form('bank_users.borrower_rgistration_form')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    alert('Agreements, Privacy Policy and Applicant should accept following:Please note that any information concealed (as what we ask for), would be construed as illegitimate action on your part and an intentional attempt to hide material information which if found in future, would attract necessary action (s) at your sole cost. Hence, request to be truthful to your best knowledge while sharing your details)')

   # max_amount = self.max_amount
    #min_amount = self.min_amount.text
    #tenure = self.tenure.selected_value
    #anvil.server.call('add_user_profile', min_amount, tenure, max_amount)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form')
