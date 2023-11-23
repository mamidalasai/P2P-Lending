from ._anvil_designer import star_1_borrower_registration_form_beginTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime,timedelta
import re
class star_1_borrower_registration_form_begin(star_1_borrower_registration_form_beginTemplate):
    def __init__(self, user_id, **properties):
        self.userId = user_id
        self.init_components(**properties)
        
        # Any code you write here will run before the form opens.

    def home_borrower_registration_form_click(self, **event_args):
        open_form('bank_users.user_form')

    def next_butto_for_step_2_click(self, **event_args):
        full_name = self.borrower_full_name_test.text
        gender = self.gender_dd.selected_value
        dob = self.borrower_date_of_birth_date_picker.date
        user_id = self.userId
        
        # Clear previous error messages
        self.full_name_label.text = ''
        self.dob_label.text = ''

        # Validate full name
        if not re.match(r'^[A-Za-z\s]+$', full_name):
            self.full_name_label.text = 'Enter a valid full name'
          
        elif not dob or dob > datetime.now().date():
            self.dob_label.text = 'Enter a valid date of birth'

        # Validate age (must be 18 or older)
        elif datetime.now().date() - dob < timedelta(days=365 * 18):
            self.dob_label.text = 'You must be at least 18 years old'
        elif not full_name or not gender:
            Notification('Please fill all details').show()
        else:
            anvil.server.call('add_borrower_step1', full_name, gender, dob, user_id)
            Notification("Step 1 form fill up submitted successfully")
            open_form('borrower_registration_form.star_1_borrower_registration_form_begin_2', user_id=user_id)
           

    def borrower_full_name_test_change(self, **event_args):
        # This event is triggered when the text in the full name text box changes.
        # Check the format and hide the error label if the format is correct.
        full_name = self.borrower_full_name_test.text
        if re.match(r'^[A-Za-z\s]+$', full_name):
            self.full_name_label.text = ''
    
    def borrower_date_of_birth_date_picker_change(self, **event_args):
        # This event is triggered when the date in the date picker changes.
        # Check if the date is valid and hide the error label if it is correct.
        dob = self.borrower_date_of_birth_date_picker.date
        if not dob or dob > datetime.now().date():
            self.dob_label.text = ''
