import anvil.email
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
    row[0]['form_count']=0

@anvil.server.callable
def add_borrower_3a1_form(street_adress_1,street_address_2,city,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['street_adress_1'] = street_adress_1
    row[0]['street_address_2'] = street_address_2
    row[0]['city'] = city    
    row[0]['form_count']=3
@anvil.server.callable
def add_borrower_step2(mobile_no,user_photo,alternate_email,user_id):
  row=app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['mobile']=mobile_no
    row[0]['user_photo']=user_photo
    row[0]['another_email']= alternate_email
    row[0]['form_count']=1



@anvil.server.callable
def add_borrower_step3(aadhar,aadhar_card,pan,pan_card,user_id):
  row=app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['aadhaar_no']=aadhar
    row[0]['aadhaar_photo']=aadhar_card
    row[0]['pan_number']=pan
    row[0]['pan_photo']=pan_card
    row[0]['form_count']=2


@anvil.server.callable
def add_borrower_step3a(father_name,father_age,mother_name,mother_age,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['father_name'] = father_name
    row[0]['father_age'] = father_age
    row[0]['mother_name'] = mother_name
    row[0]['mother_age'] = mother_age
    row[0]['form_count']=4

@anvil.server.callable
def add_borrower_step3c(status_of_user,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['profficen'] = status_of_user
    row[0]['form_count']=5


@anvil.server.callable
def add_borrower_step4(marital_status,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['marital_status']=marital_status
    row[0]['form_count']=6

@anvil.server.callable
def add_borrower_student(college_name,college_id,college_proof,college_address,user_id):
  row=app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['college_name']=college_name
    row[0]['college_id']=college_id
    row[0]['college_address']=college_address
    row[0]['college_proof']=college_proof
    
    
@anvil.server.callable
def add_borrower_step4a(spouse_name,marrege_date,spouse_mobile_no,user_id):
  row=app_tables.user_profile.search(coustmer_id=user_id)
  if row:
   row[0]['spouse_name']=spouse_name
   row[0]['Date_mariage']=marrege_date
   row[0]['spouse_mobile']=spouse_mobile_no

@anvil.server.callable
def add_borrower_step5(spouse_company_name,spouse_company_address,spouse_profficen,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['spouse_company_name']=spouse_company_name
    row[0]['spouse_company_address']=spouse_company_address
    row[0]['spouse_designation']=spouse_profficen

@anvil.server.callable
def add_borrower_spouse(annual_ctc,office_number,user_id):
  row=app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['spouse_annual_ctc']=annual_ctc
    row[0]['spouse_office_number']=office_number

@anvil.server.callable
def add_borrower_step7(home_loan,other_loan,live_loan,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['running_Home_Loan'] = home_loan
    row[0]['running_or_live loans']= live_loan
    row[0]['other_loan']=other_loan
    row[0]['form_count']=7
@anvil.server.callable
def add_borrower_step8(account_name, account_type,account_number,bank_name, user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['account_name'] = account_name
    row[0]['account_type'] = account_type
    row[0]['account_number'] = account_number
    row[0]['select_bank'] = bank_name  
    row[0]['form_count']=8

@anvil.server.callable
def add_borrower_step9(ifsc,salary_type,select_bank,net_bank, user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['ifsc_code'] = ifsc
    row[0]['salary_type'] = salary_type
    row[0]['select_bank'] = select_bank
    row[0]['net_bank'] = net_bank
    row[0]['usertype'] = 'borrower'
    row[0]['last_confirm'] = True
    row[0]['form_count']=9

# the borrower registration form end hear do not change any code ---#






@anvil.server.callable
def add_loan_details(min_amount, tenure,max_amount,user_id):
  row=app_tables.loan_details.search(coustmer_id=user_id)
  if row:
    row[0]['max_amount']=max_amount
    row[0]['max_amount']=min_amount
    row[0]['tenure']=tenure
    row[0]['timestamp']=datetime.now()
