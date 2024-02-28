from django.db import models

# Create your models here.

# class Country(models.Model):
#     country_choices = (("India", "India"),)
#     country = models.CharField(choices=country_choices, max_length=255, null=False, blank=True)

# class State(models.Model):
#     state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
#     state = models.CharField(choices=state_choices, max_length=255, null=False, blank=True)
#     country_id = models.ForeignKey(Country, null=False, on_delete=models.CASCADE)

# class City(models.Model):
#     city_choices = (('Pune','Pune'), ('Mumbai','Mumbai'), ('Nagpur', 'Nagpur'))
#     city = models.CharField(choices=city_choices, max_length=255, null=False, blank=True)
#     state_id = models.ForeignKey(State, null=False, on_delete=models.CASCADE)

class FacultyDetail(models.Model):
    #state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
    state_choices = (("Maharashtra", "Maharashtra"), ("Bihar", "Bihar"),)
    city_choices = (('Pune','Pune'), ('Mumbai','Mumbai'), ('Nagpur', 'Nagpur'), ('Gaya','Gaya'), ('Patna','Patna'), ('Nalanda', 'Nalanda'),)
    name = models.CharField(max_length=255)
    mobile = models.CharField(unique=True, max_length=10)
    email = models.EmailField(unique=True, max_length=255)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(choices=state_choices, max_length=50)
    city = models.CharField(choices=city_choices, max_length=50)
    locality = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    courses = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/Faculty_Photo', max_length=255, null=True, default='media/Faculty_Photo/person.jpg')

