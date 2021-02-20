import bots


def checker(x):
  # while True:
    # x = input().lower()

    if "wiki" in x.lower():
      src_qr = x.replace("wiki ","")
      print("WikiBot has joined the chat!")
      # print(bots.WikiBot(src_qr))
      return bots.WikiBot(src_qr)
      

    elif "tempcheck" in x.lower():
      loca = x.replace("tempcheck ","")
      print("TempChecker has joined the chat!")
      return bots.TempCheck(loca)

    elif "ask: " in x.lower(): 
      ask = x.replace("ask: ","")
      # print("wolf")
      return bots.Wolfram(ask)

    else:
      return False
  
# print(checker("tempcheck Jaipur"))