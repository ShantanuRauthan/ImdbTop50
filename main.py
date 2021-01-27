#To Get the Top 50 IMBD Movies
#Kindly refrain  changing credits
#Make sure to clear out all the text from the IMDB.txt file everytime you run the code


from bs4 import BeautifulSoup
import requests

print('''
██╗███╗░░░███╗██████╗░██████╗░  ███████╗░█████╗░
██║████╗░████║██╔══██╗██╔══██╗  ██╔════╝██╔══██╗
██║██╔████╔██║██║░░██║██████╦╝  ██████╗░██║░░██║
██║██║╚██╔╝██║██║░░██║██╔══██╗  ╚════██╗██║░░██║
██║██║░╚═╝░██║██████╔╝██████╦╝  ██████╔╝╚█████╔╝
╚═╝╚═╝░░░░░╚═╝╚═════╝░╚═════╝░  ╚═════╝░░╚════╝░
''')
print('      [+]Author: https://github.com/ShantanuRauthan [+]\n')

print("Type y to continue")
a = input()

if (a =='y'):
  url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"
  headers = {"Accept-Language": "en-US, en;q = 0.5" }# for getting only english movie titles

  r = requests.get(url, headers,timeout = 3)

  soup = BeautifulSoup(r.text, 'html.parser')


  container = soup.find_all('div', class_='lister-item mode-advanced') #finding all div with the given class


#making a dict of all the necessary infos
  for item in container:
    tweet={
    "S No.": item.find("span", class_='lister-item-index unbold text-primary').text,
    "Movie Name": item.h3.a.text,
    "Year Released": item.find("span",class_ = "lister-item-year text-muted unbold").text,
    "Time": item.find("span",class_="runtime").text,
    "Genre": item.find("span", class_ = "genre").text,
    "Ratings": item.strong.text,
        }

    print(tweet)
    print("\n")
    
    with open ('IMDB.txt','a') as f:
      f.write(str(tweet) + "\n")
    f.close()


