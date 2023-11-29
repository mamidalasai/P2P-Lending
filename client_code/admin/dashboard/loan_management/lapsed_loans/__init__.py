from ._anvil_designer import lapsed_loansTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, timedelta


class lapsed_loans(lapsed_loansTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.loan = tables.app_tables.loan_details.search()
    self.fourcloser = tables.app_tables.foreclosure.search()

    self.due_list = []
    self.loan_amont = []
    self.paid_amount = []

    self.id = []
    for i in self.loan:
      self.due_list.append(i['due_date'].date())
      self.loan_amont.append(i['loan_amount'])
      self.id.append(i['loan_id'])

    self.id_1 = []
    for i in self.fourcloser:
      self.paid_amount.append(i['paid_amount'])
      self.id_1.append(i['loan_id'])


    
    for i in self.id:
      if i in self.id_1:
        b = self.id_1.index(i)
        if self.loan_amont[b] == self.paid_amount[b]:
          
    
    print(self.due_list)


    