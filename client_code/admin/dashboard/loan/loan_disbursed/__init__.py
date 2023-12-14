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
    self.b = []
    self.l = []
    self.result1 = []
    
    for i in self.type:
      if i == "borrower":
        self.b.append(self.type.index(i))
      elif i == 'lender':
        self.l.append(self.type.index(i))

    c = -1
    for i in self.account:
      c += 1
      if i != None:
        b = self.account.count(i)
        if b > 1:
          self.result1.append(self.id[c])
        print(b)

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

    self.main_result = []
    for i in self.result:
      if i in self.result1:
        self.main_result.append(i)
    print(self.result)
    print(self.result1)
    print(self.main_result)

    self.data = tables.app_tables.loan_details.search()

    a = -1
    self.list_1 = []
    self.list_2 = []
    self.list_3 = []
    self.list_4 = []
    
    
    for i in self.data:
      a+=1
      self.list_1.append(i['loan_id'])
      self.list_2.append(i['coustmer_id'])
      self.list_3.append(i['full_name'])
      self.list_4.append(i['loan_updated_status'])
    print(a)

    self.result_3 = []
    self.index = []
    if a == -1:
      alert("No Data Available Here!")
    else:
      b = -1
      for i in self.list_2:
        b+=1
        if (i in self.main_result) and (self.list_4[b] == "approved"):
          self.index.append(b)
          
      print(self.index)
      for i in self.index:
        self.result_3.append({'loan_id' : self.list_1[i], 'coustmer_id' : self.list_2[i], 'full_name' : self.list_3[i], 'loan_updated_status' : self.list_4[i]})

      self.repeating_panel_1.items = self.result_3

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.loan_management')
