def  f(phone_number) :
   return phone_number[:3] + '-' + phone_number[3:6] + '-' + phone_number[6:]

if __name__ == "__main__":
   print(f("123456789"))