from ._anvil_designer import loan_typeTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class loan_type(loan_typeTemplate):
  def __init__(self, **properties):
    self.userId=user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    user_id=self.userId
  def link_1_click(self, **event_args):
    open_form('bank_users.borrower_rgistration_form.new_loan_request.k12_loan',user_id=self.userId)

  def link_2_click(self, **event_args):
    open_form('bank_users.borrower_rgistration_form.new_loan_request.business_loan',user_id=self.userId)

  def button_2_click(self, **event_args):
    open_form('bank_users.borrower_rgistration_form.new_loan_request',user_id=self.userId)

  def drop_down_1_change(self, **event_args):

    value=self.drop_down_1.selected_value 
    if value=="K-12 Educational loan":
      open_form('bank_users.borrower_rgistration_form.new_loan_request.k12_loan',user_id=self.userId)
    else:
      open_form('bank_users.borrower_rgistration_form.new_loan_request.business_loan',user_id=self.userId)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form')
  
