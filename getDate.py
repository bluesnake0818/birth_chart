
from datetime import date

from datetime import datetime

datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

GAN = ["GAP", "EUL", "BYU", "JUN", "MUU", "KII", "KYU", "SHI", "YIM", "KYE"]
JI = ["RAT", "OXX", "TIG", "RAB", "DRA", "SNA", "HOR", "GOA", "MON", "ROO", "DOG", "PIG"]

day_gan_idx = 0
day_ji_idx = 0

def getDate (year, month, day, hour):
  d1 = date(1987,6,25)
  d2 = date(year, month, day)
  diff = abs(d1 - d2).days

  if(diff % 60) == 0: 
    day_gan_idx = 1
    day_ji_idx = 5
  elif(diff % 60) == 1: 
    day_gan_idx = 2
    day_ji_idx = 6
  elif(diff % 60) == 2: 
    day_gan_idx = 3
    day_ji_idx = 7
  elif(diff % 60) == 3: 
    day_gan_idx = 4
    day_ji_idx = 8
  elif(diff % 60) == 4: 
    day_gan_idx = 5
    day_ji_idx = 9
  elif(diff % 60) == 5: 
    day_gan_idx = 6
    day_ji_idx = 10
  elif(diff % 60) == 6: 
    day_gan_idx = 7
    day_ji_idx = 11
  elif(diff % 60) == 7: 
    day_gan_idx = 8
    day_ji_idx = 0
  elif(diff % 60) == 8: 
    day_gan_idx = 9
    day_ji_idx = 1
  elif(diff % 60) == 9: 
    day_gan_idx = 0
    day_ji_idx = 2
  elif(diff % 60) == 10: 
    day_gan_idx = 1
    day_ji_idx = 3
  elif(diff % 60) == 11: 
    day_gan_idx = 2
    day_ji_idx = 4
  elif(diff % 60) == 12: 
    day_gan_idx = 3
    day_ji_idx = 5
  elif(diff % 60) == 13: 
    day_gan_idx = 4
    day_ji_idx = 6
  elif(diff % 60) == 14: 
    day_gan_idx = 5
    day_ji_idx = 7
  elif(diff % 60) == 15: 
    day_gan_idx = 6
    day_ji_idx = 8
  elif(diff % 60) == 16: 
    day_gan_idx = 7
    day_ji_idx = 9
  elif(diff % 60) == 17: 
    day_gan_idx = 8
    day_ji_idx = 10
  elif(diff % 60) == 18: 
    day_gan_idx = 9
    day_ji_idx = 11
  elif(diff % 60) == 19: 
    day_gan_idx = 0
    day_ji_idx = 0
  elif(diff % 60) == 20: 
    day_gan_idx = 1
    day_ji_idx = 1
  elif(diff % 60) == 21: 
    day_gan_idx = 2
    day_ji_idx = 2
  elif(diff % 60) == 22: 
    day_gan_idx = 3
    day_ji_idx = 3
  elif(diff % 60) == 23: 
    day_gan_idx = 4
    day_ji_idx = 4
  elif(diff % 60) == 24: 
    day_gan_idx = 5
    day_ji_idx = 5
  elif(diff % 60) == 25: 
    day_gan_idx = 6
    day_ji_idx = 6
  elif(diff % 60) == 26: 
    day_gan_idx = 7
    day_ji_idx = 7
  elif(diff % 60) == 27: 
    day_gan_idx = 8
    day_ji_idx = 8
  elif(diff % 60) == 28: 
    day_gan_idx = 9
    day_ji_idx = 9
  elif(diff % 60) == 29: 
    day_gan_idx = 0
    day_ji_idx = 10
  elif(diff % 60) == 30: 
    day_gan_idx = 1
    day_ji_idx = 11
  elif(diff % 60) == 31: 
    day_gan_idx = 2
    day_ji_idx = 0
  elif(diff % 60) == 32: 
    day_gan_idx = 3
    day_ji_idx = 1
  elif(diff % 60) == 33: 
    day_gan_idx = 4
    day_ji_idx = 2
  elif(diff % 60) == 34: 
    day_gan_idx = 5
    day_ji_idx = 3
  elif(diff % 60) == 35: 
    day_gan_idx = 6
    day_ji_idx = 4
  elif(diff % 60) == 36: 
    day_gan_idx = 7
    day_ji_idx = 5
  elif(diff % 60) == 37: 
    day_gan_idx = 8
    day_ji_idx = 6
  elif(diff % 60) == 38: 
    day_gan_idx = 9
    day_ji_idx = 7
  elif(diff % 60) == 39: 
    day_gan_idx = 0
    day_ji_idx = 8
  elif(diff % 60) == 40: 
    day_gan_idx = 1
    day_ji_idx = 9
  elif(diff % 60) == 41: 
    day_gan_idx = 2
    day_ji_idx = 10
  elif(diff % 60) == 42: 
    day_gan_idx = 3
    day_ji_idx = 11
  elif(diff % 60) == 43: 
    day_gan_idx = 4
    day_ji_idx = 0
  elif(diff % 60) == 44: 
    day_gan_idx = 5
    day_ji_idx = 1
  elif(diff % 60) == 45: 
    day_gan_idx = 6
    day_ji_idx = 2
  elif(diff % 60) == 46: 
    day_gan_idx = 7
    day_ji_idx = 3
  elif(diff % 60) == 47: 
    day_gan_idx = 8
    day_ji_idx = 4
  elif(diff % 60) == 48: 
    day_gan_idx = 9
    day_ji_idx = 5
  elif(diff % 60) == 49: 
    day_gan_idx = 0
    day_ji_idx = 6
  elif(diff % 60) == 50: 
    day_gan_idx = 1
    day_ji_idx = 7
  elif(diff % 60) == 51: 
    day_gan_idx = 2
    day_ji_idx = 8
  elif(diff % 60) == 52: 
    day_gan_idx = 3
    day_ji_idx = 9
  elif(diff % 60) == 53: 
    day_gan_idx = 4
    day_ji_idx = 10
  elif(diff % 60) == 54: 
    day_gan_idx = 5
    day_ji_idx = 11
  elif(diff % 60) == 55: 
    day_gan_idx = 6
    day_ji_idx = 0
  elif(diff % 60) == 56: 
    day_gan_idx = 7
    day_ji_idx = 1
  elif(diff % 60) == 57: 
    day_gan_idx = 8
    day_ji_idx = 2
  elif(diff % 60) == 58: 
    day_gan_idx = 9
    day_ji_idx = 3
  else: #if(diff % 60) == 59: 
    day_gan_idx = 0
    day_ji_idx = 4
  
  if(hour >= 23):
    day_gan_idx += 1 
    day_ji_idx += 1

  return [GAN[day_gan_idx], JI[day_ji_idx]]

print(getDate(1987,6,30,23))


  # if(diff % 60) == 0: 
  #   day_gan_idx = 0
  #   day_ji_idx = 0

  # input 과 기준점과의 차이를 day count로 저장하고, 거기서 %60를 한담에, 그거에 따라서 day_gan_idx, day_ji_idx를 정함

  # hour == 23 이면 day_gan_idx += 1, day_ji_idx += 1



  # def days_between(d1, d2):
  #   d1 = datetime.strptime(d1, "%Y-%m-%d")
  #   d2 = datetime.strptime(d2, "%Y-%m-%d")
  #   return abs((d2 - d1).days)