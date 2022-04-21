
GAN = ["GAP", "EUL", "BYU", "JUN", "MUU", "KII", "KYU", "SHI", "YIM", "KYE"]
JI = ["RAT", "OXX", "TIG", "RAB", "DRA", "SNA", "HOR", "GOA", "MON", "ROO", "DOG", "PIG"]







# print('Enter your year (yy) of birth:')
# year = input()
# print('Hello, ' + year)

# print('Enter your month (mm) of birth:')
# month = input()
# print('Hello, ' + month)

# print('Enter your date (dd) of birth:')
# date = input()
# print('Hello, ' + date)

# print('Enter your hour (hh) of birth:')
# hour = input()


# print('Enter your minute (mm) of birth:')
# minute = input()


year_gan = ''
year_ji = ''

year_gan_idx = 0
year_ji_idx = 0



def getYear (year, month, date, hour):
  if(year % 60) == 0: 
    year_gan = GAN[6]
    year_ji = JI[8]
  elif(year % 60) == 1: 
    year_gan = GAN[7]
    year_ji = JI[9]
  elif(year % 60) == 2: 
    year_gan = GAN[8]
    year_ji = JI[10]
  elif(year % 60) == 3: 
    year_gan = GAN[9]
    year_ji = JI[11]
  elif(year % 60) == 4: 
    year_gan = GAN[0]
    year_ji = JI[0]
  elif(year % 60) == 5: 
    year_gan = GAN[1]
    year_ji = JI[1]
  elif(year % 60) == 6: 
    year_gan = GAN[2]
    year_ji = JI[2]
  elif(year % 60) == 7: 
    year_gan = GAN[3]
    year_ji = JI[3]
  elif(year % 60) == 8: 
    year_gan = GAN[4]
    year_ji = JI[4]
  elif(year % 60) == 9: 
    year_gan = GAN[5]
    year_ji = JI[5]
  elif(year % 60) == 10: 
    year_gan = GAN[6]
    year_ji = JI[6]
  elif(year % 60) == 11: 
    year_gan = GAN[7]
    year_ji = JI[7]
  elif(year % 60) == 12: 
    year_gan = GAN[8]
    year_ji = JI[8]
  elif(year % 60) == 13: 
    year_gan = GAN[9]
    year_ji = JI[9]
  elif(year % 60) == 14: 
    year_gan = GAN[0]
    year_ji = JI[10]
  elif(year % 60) == 15: 
    year_gan = GAN[1]
    year_ji = JI[11]
  elif(year % 60) == 16: 
    year_gan = GAN[2]
    year_ji = JI[0]
  elif(year % 60) == 17: 
    year_gan = GAN[3]
    year_ji = JI[1]
  elif(year % 60) == 18: 
    year_gan = GAN[4]
    year_ji = JI[2]
  elif(year % 60) == 19: 
    year_gan = GAN[5]
    year_ji = JI[3]
  elif(year % 60) == 20: 
    year_gan = GAN[6]
    year_ji = JI[4]
  elif(year % 60) == 21: 
    year_gan = GAN[7]
    year_ji = JI[5]
  elif(year % 60) == 22: 
    year_gan = GAN[8]
    year_ji = JI[6]
  elif(year % 60) == 23: 
    year_gan = GAN[9]
    year_ji = JI[7]
  elif(year % 60) == 24: 
    year_gan = GAN[0]
    year_ji = JI[8]
  elif(year % 60) == 25: 
    year_gan = GAN[1]
    year_ji = JI[9]
  elif(year % 60) == 26: 
    year_gan = GAN[2]
    year_ji = JI[10]
  elif(year % 60) == 27: 
    year_gan = GAN[3]
    year_ji = JI[11]
  elif(year % 60) == 28: 
    year_gan = GAN[4]
    year_ji = JI[0]
  elif(year % 60) == 29: 
    year_gan = GAN[5]
    year_ji = JI[1]
  elif(year % 60) == 30: 
    year_gan = GAN[6]
    year_ji = JI[2]
  elif(year % 60) == 31: 
    year_gan = GAN[7]
    year_ji = JI[3]
  elif(year % 60) == 32: 
    year_gan = GAN[8]
    year_ji = JI[4]
  elif(year % 60) == 33: 
    year_gan = GAN[9]
    year_ji = JI[5]
  elif(year % 60) == 34: 
    year_gan = GAN[0]
    year_ji = JI[6]
  elif(year % 60) == 35: 
    year_gan = GAN[1]
    year_ji = JI[7]
  elif(year % 60) == 36: 
    year_gan = GAN[2]
    year_ji = JI[8]
  elif(year % 60) == 37: 
    year_gan = GAN[3]
    year_ji = JI[9]
  elif(year % 60) == 38: 
    year_gan = GAN[4]
    year_ji = JI[10]
  elif(year % 60) == 39: 
    year_gan = GAN[5]
    year_ji = JI[11]
  elif(year % 60) == 40: 
    year_gan = GAN[6]
    year_ji = JI[0]
  elif(year % 60) == 41: 
    year_gan = GAN[7]
    year_ji = JI[1]
  elif(year % 60) == 42: 
    year_gan = GAN[8]
    year_ji = JI[2]
  elif(year % 60) == 43: 
    year_gan = GAN[9]
    year_ji = JI[3]
  elif(year % 60) == 44: 
    year_gan = GAN[0]
    year_ji = JI[4]
  elif(year % 60) == 45: 
    year_gan = GAN[1]
    year_ji = JI[5]
  elif(year % 60) == 46: 
    year_gan = GAN[2]
    year_ji = JI[6]
  elif(year % 60) == 47: 
    year_gan = GAN[3]
    year_ji = JI[7]
  elif(year % 60) == 48: 
    year_gan = GAN[4]
    year_ji = JI[8]
  elif(year % 60) == 49: 
    year_gan = GAN[5]
    year_ji = JI[9]
  elif(year % 60) == 50: 
    year_gan = GAN[6]
    year_ji = JI[10]
  elif(year % 60) == 51: 
    year_gan = GAN[7]
    year_ji = JI[11]
  elif(year % 60) == 52: 
    year_gan = GAN[8]
    year_ji = JI[0]
  elif(year % 60) == 53: 
    year_gan = GAN[9]
    year_ji = JI[1]
  elif(year % 60) == 54: 
    year_gan = GAN[0]
    year_ji = JI[2]
  elif(year % 60) == 55: 
    year_gan = GAN[1]
    year_ji = JI[3]
  elif(year % 60) == 56: 
    year_gan = GAN[2]
    year_ji = JI[4]
  elif(year % 60) == 57: 
    year_gan = GAN[3]
    year_ji = JI[5]
  elif(year % 60) == 58: 
    year_gan = GAN[4]
    year_ji = JI[6]
  else: #if(year % 60) == 59 
    year_gan = GAN[5]
    year_ji = JI[7]

  year_gan_idx = GAN.index(year_gan)
  year_ji_idx = JI.index(year_ji)

  # print(year_gan_idx)
  # print(year_ji_idx)
  if(month == 1): 
    year_gan_idx -= 1
    year_ji_idx -= 1

  if(month == 2):
    if(date <= 2):
      year_gan_idx -= 1
      year_ji_idx -= 1
    if(date == 3):
      if(hour < 23):
        year_gan_idx -= 1
        year_ji_idx -= 1

  return [GAN[year_gan_idx], JI[year_ji_idx]]

print(getYear(1988, 2, 3, 22))