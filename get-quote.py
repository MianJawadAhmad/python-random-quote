import random

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  f = open("quotes.txt", "a")
  f.write("Practice Like a Singer!")
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0, last)
  print(quotes[rnd])
  rnd = random.randint(0, last)
  print(quotes[rnd])
  rnd = random.randint(0, last)
  print(quotes[rnd])
  print(quotes[14])

if __name__== "__main__":
  primary()
