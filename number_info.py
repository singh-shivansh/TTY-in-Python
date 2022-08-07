import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder, carrier

num = str(input('Phone Number(with Country Code): ')).strip(' ')
phoneNumber = phonenumbers.parse(num)
timeZone = timezone.time_zones_for_number(phoneNumber)
Carrier = carrier.name_for_number(phoneNumber, 'en')
Region = geocoder.description_for_number(phoneNumber, 'en')

print(phoneNumber)
print(timeZone)
print(Carrier)
print(Region)
print("Valid Mobile Number:",phonenumbers.is_valid_number(phoneNumber))
print("Checking possibility of Number:",phonenumbers.is_possible_number(phoneNumber))