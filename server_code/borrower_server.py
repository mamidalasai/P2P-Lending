import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime


@anvil.server.callable
def add_borrower_step1(full_name,gender,dob,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['full_name'] = full_name
    row[0]['gender'] = gender
    row[0]['date_of_birth'] = dob

    
    
@anvil.server.callable
def add_borrower_step2(mobile_no,user_photo,alternate_email,user_id):
  row=app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['mobile']=mobile_no
    row[0]['user_photo']=user_photo
    row[0]['another_email']= alternate_email




@anvil.server.callable
def add_borrower_step3(aadhar,aadhar_card,pan,pan_card,user_id):
  row=app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['aadhaar_no']=aadhar
    row[0]['aadhaar_photo']=aadhar_card
    row[0]['pan_number']=pan
    row[0]['pan_photo']=pan_card


@anvil.server.callable
def add_borrower_step3a(father_name,father_age,mother_name,mother_age,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['father_name'] = father_name
    row[0]['father_age'] = father_age
    row[0]['mother_name'] = mother_name
    row[0]['mother_age'] = mother_age


@anvil.server.callable
def add_borrower_step3c(status_of_user,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['designation'] = status_of_user




@anvil.server.callable
def add_borrower_step4(mother_toung,marital_status,spouse_name,marrege_date,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['mouther_tounge']=mother_toung
    row[0]['marital_status']=marital_status
    row[0]['spouse_name']=spouse_name
    row[0]['Date_mariage']=marrege_date


@anvil.server.callable
def add_borrower_step5(spouse_mobile,spouse_company_name,spouse_company_address,spouse_profficen,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['spouse_mobile']=spouse_mobile
    row[0]['spouse_company_name']=spouse_company_name
    row[0]['spouse_company_address']=spouse_company_address
    row[0]['spouse_profficen']=spouse_profficen


  

# the borrower registration form end hear do not change any code ---#




@anvil.server.callable
def add_loan_details(min_amount, tenure,max_amount,user_id):
  row=app_tables.loan_details.search(coustmer_id=user_id)
  if row:
    row[0]['max_amount']=max_amount
    row[0]['max_amount']=min_amount
    row[0]['tenure']=tenure
    row[0]['timestamp']=datetime.now()

