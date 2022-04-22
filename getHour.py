GAN = ["GAP", "EUL", "BYU", "JUN", "MUU", "KII", "KYU", "SHI", "YIM", "KYE"]
JI = ["RAT", "OXX", "TIG", "RAB", "DRA", "SNA", "HOR", "GOA", "MON", "ROO", "DOG", "PIG"]


hour_gan_idx = 0
hour_ji_idx = 0

# hour in 24 hour format
def getHour (day_gan, hour):
  if(day_gan == "GAP" or day_gan == "KII"):
    if(hour == 23 or hour == 0):
      hour_gan_idx = 0
      hour_ji_idx = 0
    elif(hour == 1 or hour == 2):
      hour_gan_idx = 1
      hour_ji_idx = 1
    elif(hour == 3 or hour == 4):
      hour_gan_idx = 2
      hour_ji_idx = 2
    elif(hour == 5 or hour == 6):
      hour_gan_idx = 3
      hour_ji_idx = 3
    elif(hour == 7 or hour == 8):
      hour_gan_idx = 4
      hour_ji_idx = 4
    elif(hour == 9 or hour == 10):
      hour_gan_idx = 5
      hour_ji_idx = 5
    elif(hour == 11 or hour == 12):
      hour_gan_idx = 6
      hour_ji_idx = 6
    elif(hour == 13 or hour == 14):
      hour_gan_idx = 7
      hour_ji_idx = 7
    elif(hour == 15 or hour == 16):
      hour_gan_idx = 8
      hour_ji_idx = 8
    elif(hour == 17 or hour == 18):
      hour_gan_idx = 9
      hour_ji_idx = 9
    elif(hour == 19 or hour == 20):
      hour_gan_idx = 0
      hour_ji_idx = 10
    else: #if(hour == 21 or hour == 22):
      hour_gan_idx = 1
      hour_ji_idx = 11

  elif(day_gan == "EUL" or day_gan == "KYU"):
    if(hour == 23 or hour == 0):
      hour_gan_idx = 2
      hour_ji_idx = 0
    elif(hour == 1 or hour == 2):
      hour_gan_idx = 3
      hour_ji_idx = 1
    elif(hour == 3 or hour == 4):
      hour_gan_idx = 4
      hour_ji_idx = 2
    elif(hour == 5 or hour == 6):
      hour_gan_idx = 5
      hour_ji_idx = 3
    elif(hour == 7 or hour == 8):
      hour_gan_idx = 6
      hour_ji_idx = 4
    elif(hour == 9 or hour == 10):
      hour_gan_idx = 7
      hour_ji_idx = 5
    elif(hour == 11 or hour == 12):
      hour_gan_idx = 8
      hour_ji_idx = 6
    elif(hour == 13 or hour == 14):
      hour_gan_idx = 9
      hour_ji_idx = 7
    elif(hour == 15 or hour == 16):
      hour_gan_idx = 0
      hour_ji_idx = 8
    elif(hour == 17 or hour == 18):
      hour_gan_idx = 1
      hour_ji_idx = 9
    elif(hour == 19 or hour == 20):
      hour_gan_idx = 2
      hour_ji_idx = 10
    else: #if(hour == 21 or hour == 22):
      hour_gan_idx = 3
      hour_ji_idx = 11

  elif(day_gan == "BYU" or day_gan == "SHI"):
    if(hour == 23 or hour == 0):
      hour_gan_idx = 4
      hour_ji_idx = 0    
    elif(hour == 1 or hour == 2):
      hour_gan_idx = 5
      hour_ji_idx = 1
    elif(hour == 3 or hour == 4):
      hour_gan_idx = 6
      hour_ji_idx = 2
    elif(hour == 5 or hour == 6):
      hour_gan_idx = 7
      hour_ji_idx = 3
    elif(hour == 7 or hour == 8):
      hour_gan_idx = 8
      hour_ji_idx = 4
    elif(hour == 9 or hour == 10):
      hour_gan_idx = 9
      hour_ji_idx = 5
    elif(hour == 11 or hour == 12):
      hour_gan_idx = 0
      hour_ji_idx = 6
    elif(hour == 13 or hour == 14):
      hour_gan_idx = 1
      hour_ji_idx = 7
    elif(hour == 15 or hour == 16):
      hour_gan_idx = 2
      hour_ji_idx = 8
    elif(hour == 17 or hour == 18):
      hour_gan_idx = 3
      hour_ji_idx = 9
    elif(hour == 19 or hour == 20):
      hour_gan_idx = 4
      hour_ji_idx = 10
    else: #if(hour == 21 or hour == 22):
      hour_gan_idx = 5
      hour_ji_idx = 11

  elif(day_gan == "JUN" or day_gan == "YIM"):
    if(hour == 23 or hour == 0):
      hour_gan_idx = 6
      hour_ji_idx = 0
    elif(hour == 1 or hour == 2):
      hour_gan_idx = 7
      hour_ji_idx = 1
    elif(hour == 3 or hour == 4):
      hour_gan_idx = 8
      hour_ji_idx = 2
    elif(hour == 5 or hour == 6):
      hour_gan_idx = 9
      hour_ji_idx = 3
    elif(hour == 7 or hour == 8):
      hour_gan_idx = 0
      hour_ji_idx = 4
    elif(hour == 9 or hour == 10):
      hour_gan_idx = 1
      hour_ji_idx = 5
    elif(hour == 11 or hour == 12):
      hour_gan_idx = 2
      hour_ji_idx = 6
    elif(hour == 13 or hour == 14):
      hour_gan_idx = 3
      hour_ji_idx = 7
    elif(hour == 15 or hour == 16):
      hour_gan_idx = 4
      hour_ji_idx = 8
    elif(hour == 17 or hour == 18):
      hour_gan_idx = 5
      hour_ji_idx = 9
    elif(hour == 19 or hour == 20):
      hour_gan_idx = 6
      hour_ji_idx = 10
    else: #if(hour == 21 or hour == 22):
      hour_gan_idx = 7
      hour_ji_idx = 11

  else: #if(day_gan == "MUU" or day_gan == "KYE"):
    if(hour == 23 or hour == 0):
      hour_gan_idx = 8
      hour_ji_idx = 0
    elif(hour == 1 or hour == 2):
      hour_gan_idx = 9
      hour_ji_idx = 1
    elif(hour == 3 or hour == 4):
      hour_gan_idx = 0
      hour_ji_idx = 2
    elif(hour == 5 or hour == 6):
      hour_gan_idx = 1
      hour_ji_idx = 3
    elif(hour == 7 or hour == 8):
      hour_gan_idx = 2
      hour_ji_idx = 4
    elif(hour == 9 or hour == 10):
      hour_gan_idx = 3
      hour_ji_idx = 5
    elif(hour == 11 or hour == 12):
      hour_gan_idx = 4
      hour_ji_idx = 6
    elif(hour == 13 or hour == 14):
      hour_gan_idx = 5
      hour_ji_idx = 7
    elif(hour == 15 or hour == 16):
      hour_gan_idx = 6
      hour_ji_idx = 8
    elif(hour == 17 or hour == 18):
      hour_gan_idx = 7
      hour_ji_idx = 9
    elif(hour == 19 or hour == 20):
      hour_gan_idx = 8
      hour_ji_idx = 10
    else: #if(hour == 21 or hour == 22):
      hour_gan_idx = 9
      hour_ji_idx = 11

  return [GAN[hour_gan_idx], JI[hour_ji_idx]]

print(getHour("EUL", 7))