
GAN = ["GAP", "EUL", "BYU", "JUN", "MUU", "KII", "KYU", "SHI", "YIM", "KYE"]
JI = ["RAT", "OXX", "TIG", "RAB", "DRA", "SNA", "HOR", "GOA", "MON", "ROO", "DOG", "PIG"]

month_gan_idx = 0
month_ji_idx = 0

def getMonth (year_gan, month, date, hour):
  #2월
  if(month % 12) == 2: 
    month_ji_idx = 2
    if(year_gan == 'GAP' or year_gan == 'KII'):
      month_gan_idx = 2
      if(date <= 2):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 3):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'EUL' or year_gan == 'KYU'): 
      month_gan_idx = 4
      if(date <= 2):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 3):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'BYU' or year_gan == 'SHI'): 
      month_gan_idx = 6
      if(date <= 2):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 3):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'JUN' or year_gan == 'YIM'): 
      month_gan_idx = 8
      if(date <= 2):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 3):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    else: # If (year_gan == 'MUU' or year_gan == 'KYE')
      month_gan_idx = 0
      if(date <= 2):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 3):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1

  #3월
  elif(month % 12) == 3: 
    month_ji_idx = 3
    if(year_gan == 'GAP' or year_gan == 'KII'):
      month_gan_idx = 3
      if(date <= 4):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 5):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'EUL' or year_gan == 'KYU'): 
      month_gan_idx = 5
      if(date <= 4):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 5):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'BYU' or year_gan == 'SHI'): 
      month_gan_idx = 7
      if(date <= 4):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 5):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'JUN' or year_gan == 'YIM'): 
      month_gan_idx = 9
      if(date <= 4):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 5):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    else: # If (year_gan == 'MUU' or year_gan == 'KYE')
      month_gan_idx = 1
      if(date <= 4):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 5):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1

  #4월
  elif(month % 12) == 4: 
    month_ji_idx = 4
    if(year_gan == 'GAP' or year_gan == 'KII'):
      month_gan_idx = 4
      if(date <= 3):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 4):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'EUL' or year_gan == 'KYU'): 
      month_gan_idx = 6
      if(date <= 3):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 4):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'BYU' or year_gan == 'SHI'): 
      month_gan_idx = 8
      if(date <= 3):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 4):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'JUN' or year_gan == 'YIM'): 
      month_gan_idx = 1
      if(date <= 3):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 4):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    else: # If (year_gan == 'MUU' or year_gan == 'KYE')
      month_gan_idx = 3
      if(date <= 3):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 4):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1

  # 5월
  elif(month % 12) == 5: 
    month_ji_idx = 5
    if(year_gan == 'GAP' or year_gan == 'KII'):
      month_gan_idx = 5
      if(date <= 3):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 4):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'EUL' or year_gan == 'KYU'): 
      month_gan_idx = 7
      if(date <= 3):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 4):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'BYU' or year_gan == 'SHI'): 
      month_gan_idx = 9
      if(date <= 3):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 4):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'JUN' or year_gan == 'YIM'): 
      month_gan_idx = 1
      if(date <= 3):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 4):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    else: # If (year_gan == 'MUU' or year_gan == 'KYE')
      month_gan_idx = 3
      if(date <= 3):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 4):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1

    # 6월
  elif(month % 12) == 6: 
    month_ji_idx = 6
    if(year_gan == 'GAP' or year_gan == 'KII'):
      month_gan_idx = 6
      if(date <= 4):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 5):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'EUL' or year_gan == 'KYU'): 
      month_gan_idx = 8
      if(date <= 4):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 5):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'BYU' or year_gan == 'SHI'): 
      month_gan_idx = 0
      if(date <= 4):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 5):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'JUN' or year_gan == 'YIM'): 
      month_gan_idx = 2
      if(date <= 4):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 5):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    else: # If (year_gan == 'MUU' or year_gan == 'KYE')
      month_gan_idx = 4
      if(date <= 4):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 5):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1




  # 7월
  elif(month % 12) == 7: 
    month_ji_idx = 7
    if(year_gan == 'GAP' or year_gan == 'KII'):
      month_gan_idx = 7
      if(date <= 5):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 6):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'EUL' or year_gan == 'KYU'): 
      month_gan_idx = 9
      if(date <= 5):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 6):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'BYU' or year_gan == 'SHI'): 
      month_gan_idx = 1
      if(date <= 5):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 6):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'JUN' or year_gan == 'YIM'): 
      month_gan_idx = 3
      if(date <= 5):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 6):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    else: # If (year_gan == 'MUU' or year_gan == 'KYE')
      month_gan_idx = 5
      if(date <= 5):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 6):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1


  # 8월
  elif(month % 12) == 8: 
    month_ji_idx = 8
    if(year_gan == 'GAP' or year_gan == 'KII'):
      month_gan_idx = 8
      if(date <= 5):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 6):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'EUL' or year_gan == 'KYU'): 
      month_gan_idx = 0
      if(date <= 5):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 6):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'BYU' or year_gan == 'SHI'): 
      month_gan_idx = 2
      if(date <= 5):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 6):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'JUN' or year_gan == 'YIM'): 
      month_gan_idx = 4
      if(date <= 5):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 6):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    else: # If (year_gan == 'MUU' or year_gan == 'KYE')
      month_gan_idx = 6
      if(date <= 5):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 6):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1




  # 9월
  elif(month % 12) == 9: 
    month_ji_idx = 9
    if(year_gan == 'GAP' or year_gan == 'KII'):
      month_gan_idx = 9
      if(date <= 6):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 7):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'EUL' or year_gan == 'KYU'): 
      month_gan_idx = 1
      if(date <= 6):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 7):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'BYU' or year_gan == 'SHI'): 
      month_gan_idx = 3
      if(date <= 6):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 7):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'JUN' or year_gan == 'YIM'): 
      month_gan_idx = 5
      if(date <= 6):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 7):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    else: # If (year_gan == 'MUU' or year_gan == 'KYE')
      month_gan_idx = 7
      if(date <= 6):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 7):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1

  # 10월
  elif(month % 12) == 10: 
    month_ji_idx = 10
    if(year_gan == 'GAP' or year_gan == 'KII'):
      month_gan_idx = 0
      if(date <= 6):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 7):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'EUL' or year_gan == 'KYU'): 
      month_gan_idx = 2
      if(date <= 6):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 7):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'BYU' or year_gan == 'SHI'): 
      month_gan_idx = 4
      if(date <= 6):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 7):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'JUN' or year_gan == 'YIM'): 
      month_gan_idx = 6
      if(date <= 6):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 7):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    else: # If (year_gan == 'MUU' or year_gan == 'KYE')
      month_gan_idx = 8
      if(date <= 6):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 7):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1





  # 11월
  elif(month % 12) == 11: 
    month_ji_idx = 11
    if(year_gan == 'GAP' or year_gan == 'KII'):
      month_gan_idx = 1
      if(date <= 5):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 6):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'EUL' or year_gan == 'KYU'): 
      month_gan_idx = 3
      if(date <= 5):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 6):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'BYU' or year_gan == 'SHI'): 
      month_gan_idx = 5
      if(date <= 5):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 6):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'JUN' or year_gan == 'YIM'): 
      month_gan_idx = 7
      if(date <= 5):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 6):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    else: # If (year_gan == 'MUU' or year_gan == 'KYE')
      month_gan_idx = 9
      if(date <= 5):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 6):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1

  # 12월
  elif(month % 12) == 0: 
    month_ji_idx = 0
    if(year_gan == 'GAP' or year_gan == 'KII'):
      month_gan_idx = 2
      if(date <= 5):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 6):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'EUL' or year_gan == 'KYU'): 
      month_gan_idx = 4
      if(date <= 5):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 6):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'BYU' or year_gan == 'SHI'): 
      month_gan_idx = 6
      if(date <= 5):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 6):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'JUN' or year_gan == 'YIM'): 
      month_gan_idx = 8
      if(date <= 5):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 6):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    else: # If (year_gan == 'MUU' or year_gan == 'KYE')
      month_gan_idx = 0
      if(date <= 5):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 6):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1


  # 1월
  elif(month % 12) == 1: 
    month_ji_idx = 1
    if(year_gan == 'GAP' or year_gan == 'KII'):
      month_gan_idx = 3
      if(date <= 3):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 4):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'EUL' or year_gan == 'KYU'): 
      month_gan_idx = 5
      if(date <= 3):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 4):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'BYU' or year_gan == 'SHI'): 
      month_gan_idx = 7
      if(date <= 3):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 4):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    elif(year_gan == 'JUN' or year_gan == 'YIM'): 
      month_gan_idx = 9
      if(date <= 3):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 4):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1
    else: # If (year_gan == 'MUU' or year_gan == 'KYE')
      month_gan_idx = 1
      if(date <= 3):
        month_gan_idx -= 1
        month_ji_idx -= 1
      if(date == 4):
        if(hour < 23):
          month_gan_idx -= 1
          month_ji_idx -= 1


  return [GAN[month_gan_idx], JI[month_ji_idx]]

print(getMonth("JUN", 6, 25, 7))