
GAN = ["GAP", "EUL", "BYU", "JUN", "MUU", "KII", "KYU", "SHI", "YIM", "KYE"]
JI = ["RAT", "OXX", "TIG", "RAB", "DRA", "SNA", "HOR", "GOA", "MON", "ROO", "DOG", "PIG"]

month_gan_idx = 0
month_ji_idx = 0

def getMonth (year_gan, month, date, hour):
  if(month % 12) == 0: 
    if(year_gan == 'GAP' or year_gan == 'KII'):
      month_gan_idx = 2
      month_ji_idx = 2
      month_gan = 'BYU'
      month_ji = 'TIG'
      if(date <= 2):
        month_gan_idx -= 1
        month_ji_idx -= 1
        month_gan = 'EUL'
        month_ji = 'OXX'
      if(date == 3):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
          month_gan = 'EUL'
          month_ji = 'OXX'
    elif(year_gan == 'EUL' or year_gan == 'KYU'): 
      
    elif(year_gan == 'BYU' or year_gan == 'SHI'): 
    elif(year_gan == 'JUN' or year_gan == 'YIM'): 
    else: # If (year_gan == 'MUU' or year_gan == 'KYE')


  month_gan_idx = GAN.index(month_gan)
  month_ji_idx = JI.index(month_ji)

  # print(month_gan_idx)
  # print(month_ji_idx)
  if(month == 1): 
    month_gan_idx -= 1
    month_ji_idx -= 1

  if(month == 2):
    if(date <= 2):
      month_gan_idx -= 1
      month_ji_idx -= 1
    if(date == 3):
      if(hour < 23):
        month_gan_idx -= 1
        month_ji_idx -= 1

  return [GAN[month_gan_idx], JI[month_ji_idx]]

print(getmonth(1988, 2, 3, 22))