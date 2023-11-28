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
      self.id.append(i['coustmer_id'])
      self.type.append(i['usertype'])
      self.account.append(i['account_number'])

    self.b_type = []
    self.l_type = []
    for i in self.type:
      if i == "borrower":
        self.b_type.append(self.type.index(i))
      elif i == 'lender':
        self.l_type.append(self.type.index(i))
        
    self.b = []
    self.l = []
    

    a = -1
    for i in self.id:
      if i in self.id:
        b = self.id.count(i)
        a += 1
        if b == 1:
          self.result.append(self.id[a])

    self.index = []
    for i in self.result:
      self.index.append(self.id.index(i))
    a = -1
    self.result1 = []
    for i in self.index:
      if (self.type[i] == 'borrower') and (self.type[i] == 'lender'):
        pass
    

    print(self.result)
    print(self.result1)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.loan_management')
