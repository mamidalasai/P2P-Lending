import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_lendor_frist_form(name,gender,city,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['full_name'] = name
    row[0]['gender'] = gender
    row[0]['city'] = city
    
@anvil.server.callable
def add_lendor_second_form(investment,mobile,email,photo,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['investment'] = investment
    row[0]['mobile'] = mobile
    row[0]['mail_id'] = email
    row[0]['user_photo'] = photo

@anvil.server.callable
def add_lendor_third_form(about,alerts,term,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['about'] = about
    row[0]['alerts'] = alerts
    row[0]['terms'] = term


@anvil.server.callable
def add_lendor_four_form(qualification,pannumber,identity,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['qualification'] = qualification
    row[0]['identity_proof'] = identity
    row[0]['pan_number'] = pannumber

@anvil.server.callable
def add_lendor_five_form(martial,spouse_profession,spouse_number,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['martial_status'] = martial
    row[0]['spouse_profession'] = spouse_profession
    row[0]['spouse_number'] = spouse_number

@anvil.server.callable
def add_lendor_six_form(address_type,house_no,building_name,street,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['address_type'] = address_type
    row[0]['house_no'] = house_no
    row[0]['building_name'] = building_name
    row[0]['street'] = street


@anvil.server.callable
def add_lendor_seven_form(landmark,city,state,pincode,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['landmark'] = landmark
    row[0]['city'] = city
    row[0]['state'] = state
    row[0]['pincode'] = pincode
    
@anvil.server.callable
def add_lendor_eight_form(investment,lending_period,lending_individual,lending_institutinal,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    #row[0]['lending_type'] = lending_type
    row[0]['lending_period'] = lending_period
    row[0]['investment'] = investment
    row[0]['lending_individual'] =lending_individual
    row[0]['lending_institutional'] = lending_institutinal
    
    
       
  
