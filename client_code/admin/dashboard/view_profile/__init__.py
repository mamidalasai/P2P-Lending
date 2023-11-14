from ._anvil_designer import view_profileTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

class view_profile(view_profileTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.user_profile.search()

    self.id_list = []
    self.name_list = []
    self.status_list = []
    self.gender_list = []
    self.age_list = []
    self.dob_list = []
    self.aadhar_list = []
    self.pan_list = []
    self.city_list = []
    self.email_user_list = []
    self.last_confirm_list = []
    self.mobile_check_list = []
    self.mother_tongue_list = []
    self.mother_status_list = []
    self.date_marrige_list = []
    self.space_name_list = []
    self.about_list = []
    self.alets_list = []
    self.terms_list = []
    self.mail_id_list = []
    self.qualification_list = []
    self.address_type_list = []
    self.street_list = []
    self.build_name_list = []
    self.house_no_list = []
    self.landmark_list = []
    self.pincode_list = []
    self.state_list = []
    self.spouse_number_list = []
    self.company_name_list = []
    self.company_adress_list = []
    self.proffic_list = []
    self.user_type_list = []
    self.approve_list = []
    self.mobile_list = []

    a = -1
    for i in self.data:
      a+=1
      self.id_list.append(i['coustmer_id'])
      self.name_list.append(i['full_name'])
      self.status_list.append(i['profile_status'])
      self.gender_list.append(i['gender'])
      self.age_list.append(i['user_age'])
      self.dob_list.append(i['date_of_birth'])
      self.aadhar_list.append(i['aadhaar_no'])
      self.pan_list.append(i['pan_number'])
      self.city_list.append(i['city'])
      self.email_user_list.append(i['email_user'])
      self.last_confirm_list.append(i['last_confirm'])
      self.mobile_check_list.append(i['mobile_check'])
      self.mother_status_list.append(i['marital_status'])
      self.mother_tongue_list.append(i['mouther_tounge'])
      self.date_marrige_list.append(i['Date_mariage'])
      self.space_name_list.append(i['spouse_name'])
      self.about_list.append(i['about'])
      self.alets_list.append(i['alerts'])
      self.terms_list.append(i['terms'])
      self.mail_id_list.append(i['mail_id'])
      self.qualification_list.append(i['qualification'])
      self.address_type_list.append(i['address_type'])
      self.street_list.append(i['street'])
      self.build_name_list.append(i['building_name'])
      self.house_no_list.append(i['house_no'])
      self.landmark_list.append(i['house_landmark'])
      self.pincode_list.append(i['pincode'])
      self.state_list.append(i['state'])
      self.spouse_number_list.append(i['spouse_mobile'])
      self.company_name_list.append(i['spouse_company_name'])
      self.company_adress_list.append(i['spouse_company_address'])
      self.proffic_list.append(i['spouse_profficen'])
      self.user_type_list.append(i['usertype'])
      self.approve_list.append(i['registration_approve'])
      self.mobile_list.append(i['mobile'])

    print(self.company_adress_list)
    if a == -1:
      alert("No Data Available Here!!")
    else:
      self.label_3.text = self.id_list[-1]
      self.label_8.text = self.name_list[-1]
      self.label_9.text = bool(self.status_list[-1])
      self.label_39.text= self.gender_list[-1]
      self.label_40.text = int(self.age_list[-1])
      self.label_41.text = self.dob_list[-1]
      self.label_44.text = self.mobile_list[-1]
      self.label_45.text = self.aadhar_list[-1]
      self.label_46.text = self.pan_list[-1]
      self.label_47.text = self.city_list[-1]
      self.label_48.text = self.email_user_list[-1]
      self.label_49.text = bool(self.last_confirm_list[-1])
      self.label_50.text = self.mobile_check_list[-1]
      self.label_51.text = self.mother_tongue_list[-1]
      self.label_52.text = self.mother_status_list[-1]
      self.label_53.text = self.date_marrige_list[-1]
      self.label_54.text = self.space_name_list[-1]
      self.label_61.text = self.about_list[-1]
      self.label_63.text = bool(self.alets_list[-1])
      self.label_72.text = bool(self.terms_list[-1])
      self.label_69.text = self.qualification_list[-1]
      self.label_62.text = self.address_type_list[-1]
      self.label_71.text = self.street_list[-1]
      self.label_64.text = self.build_name_list[-1]
      self.label_66.text = self.house_no_list[-1]
      self.label_65.text = self.landmark_list[-1]
      self.label_68.text = self.pincode_list[-1]
      self.label_70.text = self.state_list[-1]
      self.label_55.text = self.spouse_number_list[-1]
      self.label_56.text = self.company_name_list[-1]
      self.label_57.text = self.company_adress_list[-1]
      self.label_58.text =  self.proffic_list[-1]
      self.label_59.text = self.user_type_list[-1]
      self.label_60.text = bool(self.approve_list [-1])

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.view_profile.edit_form')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.view_profile.update_form')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard')
