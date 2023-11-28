from ._anvil_designer import loan_disbursedTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class loan_disbursed(loan_disbursedTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.loan = tables.app_tables.loan_details.search()
    self.lender = tables.app_tables.lender.search()
    self.user_profile = tables.app_tables.user_profile.search()

    self.id = []
    self.type = []
    self.account = []
  
    self.result = []
    for i in self.user_profile:
      self.id.append(i['college_id'])
      self.type.append(i['usertype'])
      self.account.append(i['account_number'])

    b_type = []
    l_type = []
    for i in self.type:
      if i == "borrower":
        b_type.append(i)
      elif i == 'lender':
        l_type.append(i)
    
    for i in self.id:
      if i in self.id:
        b = self.id.count(i)
        if b == 1:
          self.result.append(i)

    a = -1
    self.result1 = []
    for i in self.account:
      a+=1
      if b
    
    
          

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.loan_management')
