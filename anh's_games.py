

#@title WEATHER FORECAST - Click the Play button { run: "auto" }

import datetime
import requests
def weather (city,lat,lng):
  print('In {}:'.format(city))
  dates=[datetime.date.today(), datetime.date.today() + datetime.timedelta(days=1),datetime.date.today() + datetime.timedelta(days=2)]
  time='10:00:00'
  for date in dates:
    url = "https://api.darksky.net/forecast/b35c24ac71df4b2310a9038089616f68/{},{},{}T{}".format(lat, lng, date, time)
    raw_response = requests.get(url) # get the data from the service
    response = raw_response.json() # assuming json, convert the json to a python dictionary
    max_tempF = response['daily']['data'][0]['temperatureHigh']
    min_tempF = response['daily']['data'][0]['temperatureLow']
    status=response['daily']['data'][0]['icon']
    max_tempC = (max_tempF - 32) * 0.5556
    min_tempC = (min_tempF - 32) * 0.5556
    print ('- The temperature on {} is {}-{}C. And it is a {} day'.format(date, int(min_tempC), int(max_tempC), status))

#@title Hanoi
weather('Hanoi',21.028511,105.804817)

#@title Ho Chi Minh
weather('Hochiminh',10.8231,106.6297)

#@title London
weather('London',51.5074,0.1278)

#@title Nottingham
weather('Nottingham',52.9548,1.1581)

"""**CHECK YOUR MOON PHASE**"""

#@title Click the 'Play button'
print('Please input your name')
name=str(input())
print('Please input your date of birth (year, month, day), for ex: 1996 05 28')
year,month,date=[int(i) for i in input().split()]
import pandas as pd
pd.read_csv
import datetime
from lunarcalendar import Converter, Solar, Lunar
def moon_phase():
  solar = Solar(year,month,date)
  lunar = Converter.Solar2Lunar(solar)
  if lunar.day <=1:
    phase='New Moon'
    char='Creative, Adventurous, Impulsive'
  elif lunar.day <7:
    phase='Waxing Crescent'
    char= 'Ambitious, Diligent, Risk averse'
  elif lunar.day <9:
    phase='First Quarter'
    char='Talented, Brave, Patient'
  elif lunar.day <14:
    phase='Waxing Gibbous'
    char= 'Calm, Gracious, Perfectionist'
  elif lunar.day <17:
    phase='Full Moon'
    char= 'Sensitive, Empathetic, Emotional'
  elif lunar.day <22:
    phase='Waning Gibbous'
    char='Meditative, Analytical, Judgmental'
  elif lunar.day <24:
    phase='Third Quarter'
    char='Loyal, Emotional, Sociable'
  elif lunar.day >=24:
    phase='Waning Crescent'
    char= 'Imaginative, Divergent, Lonesome'
  print ('Hi {}, your Moon phase is \033[32m {}\033[30m, and your characteristics are \033[32m {}\033[30m.'.format(name,phase,char))
moon_phase()

"""**BOMB GAME**"""

#@title Click the 'Play' button
print('To play, input the number of column & row you want (>=3 or else you could not win:))')
n=int(input())
def bomb():
    print('This is a simple bomb game. The number of column and row is {} each. There will be {} bombs in the field.\nWhenever you input a row & column number (for ex 3 4 - remember to include space between 2 numbers!), I will inform you on the bomb risk.\nIn all cases, D letter means Danger zone, X letter mean Safer zone\nIf you can survive {} times of input, you win!'.format(n,n,n*2))
    print('\nPlease choose the difficulty level. Input 1 for harder mode, which means there is only alert if you near 2 bombs and above.\n2 is for easier mode, means I will inform the number of bomb around your input area')
    m=int(input())  
    import random
    a=[['0']*n for i in range(n)]
    for col in a:
            print (' '.join(col))
    bomb_list=[]
    input_list=[]
    while len(bomb_list)<=(n-1):
        l=[[random.randint(1,n),random.randint(1,n)]]
        if l[0] not in bomb_list:
            bomb_list+=l    
    # playing part:
    if m==2:
        while len(input_list)<n*2:
            print ('Please input your row & column numbers')
            l=[int(i) for i in input().split()]
            if l[0]>n or l[1]>n or l[0]<=0 or l[1]<=0:
              print('Input out of table range')
              continue
            if l not in input_list:
                input_list+=[l]
            else:
                print('You enter the same cell. Please try again!')
                continue
            if l in bomb_list:
                print('Oops! You step on bomb. End game.')
                a[l[0]-1][l[1]-1]='\033[31mB\033[30m'
                break
            else:
                count=0
                for i in range(len(bomb_list)):
                    if abs(l[0]-bomb_list[i][0])<=1 and abs(l[1]-bomb_list[i][1])<=1:  
                        count+=1
                        a[l[0]-1][l[1]-1]='\033[33mD\033[30m'
                if count==0:
                    print('Safe zone!')
                    a[l[0]-1][l[1]-1]='\033[32mX\033[30m'
                elif count>=1:
                    print ('Watch out! You are close to {} bombs.'.format(count))
            for col in a:
                print (' '.join(col))
            print('Fighting! Only {} more times to win'.format(n*2-len(input_list)))
        for col in a:
            print (' '.join(col))
        if len(input_list)==n*2:
            print('\033[32mCongratulation! You win.\033[30m')
    if m==1:
        while len(input_list)<n*2:
            print ('Please input your row & column numbers')
            l=[int(i) for i in input().split()]
            if l[0]>n or l[1]>n or l[0]<=0 or l[1]<=0:
              print('Input out of table range')
              continue
            if l not in input_list:
                input_list+=[l]
            else:
                print('You enter the same cell. Please try again!')
                continue
            if l in bomb_list:
                print('Oops! You step on bomb. End game.')
                a[l[0]-1][l[1]-1]='\033[31mB\033[30m'
                break
            else:
                count=0
                for i in range(len(bomb_list)):
                    if abs(l[0]-bomb_list[i][0])<=1 and abs(l[1]-bomb_list[i][1])<=1:  
                        count+=1
                if count<=1:
                    print('0 or 1 bombs LOL')
                    a[l[0]-1][l[1]-1]='\033[32mX\033[30m'
                elif count>=2:
                    print ('Watch out! You are close to +2 bombs.')
                    a[l[0]-1][l[1]-1]='\033[33mD\033[30m'
            for col in a:
                print (' '.join(col))
            print('Fighting! Only {} more times to win'.format(n*2-len(input_list)))
        for col in a:
            print (' '.join(col))
        if len(input_list)==n*2:
            print('\033[32mCongratulation! You win.\033[30m')
bomb()
