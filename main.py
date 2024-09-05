import random
import os

ace="""
◜¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯◝
| A             |
|               |
|       ♥       |
|               |
|               |
|             A |
◟_______________◞
"""
king="""
◜¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯◝
| K             |
|      ^^^      |
|      (.)      |
|       |       |
|      / \      |
|             K |
◟_______________◞
"""
queen="""
◜¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯◝
| Q             |
|      /^\      |
|      (.)      |
|       |       |
|      / \      |
|             Q |
◟_______________◞
"""
jack="""
◜¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯◝
| J             |
|       _       |
|      (.)      |
|       |       |
|      / \      |
|             J |
◟_______________◞
"""
c10="""
◜¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯◝
| 10            |
|    ♥     ♥    |
|    ♥  ♥  ♥    |
|    ♥  ♥  ♥    |
|    ♥     ♥    |
|            10 |
◟_______________◞
"""
c9="""
◜¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯◝
| 9             |
|    ♥     ♥    |
|    ♥  ♥  ♥    |
|    ♥     ♥    |
|    ♥     ♥    |
|            9  |
◟_______________◞
"""
c8="""
◜¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯◝
| 8             |
|    ♥          |
|    ♥  ♥  ♥    |
|    ♥  ♥  ♥    |
|          ♥    |
|            8  |
◟_______________◞
"""
c7="""
◜¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯◝
| 7             |
|    ♥     ♥    |
|    ♥  ♥  ♥    |
|    ♥     ♥    |
|               |
|            7  |
◟_______________◞
"""
c6="""
◜¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯◝
| 6             |
|    ♥     ♥    |
|    ♥     ♥    |
|    ♥     ♥    |
|               |
|            6  |
◟_______________◞
"""
c5="""
◜¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯◝
| 5             |
|    ♥     ♥    |
|       ♥       |
|    ♥     ♥    |
|               |
|            5  |
◟_______________◞
"""
c4="""
◜¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯◝
| 4             |
|    ♥     ♥    |
|               |
|    ♥     ♥    |
|               |
|            4  |
◟_______________◞
"""
c3="""
◜¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯◝
| 3             |
|       ♥       |
|       ♥       |
|       ♥       |
|               |
|            3  |
◟_______________◞
"""
c2="""
◜¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯◝
| 2             |
|       ♥       |
|               |
|       ♥       |
|               |
|            2  |
◟_______________◞
"""

BLACK  = "\033[30m"
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
PURPLE = "\033[35m"
CYAN   = "\033[36m"
WHITE  = "\033[37m"
RESET  = "\033[0m"

cards=[ace,ace,ace,ace,c2,c2,c2,c2,c3,c3,c3,c3,c4,c5,c6,c7,c8,c9,c10,jack,queen,king]
card_len=len(cards)-1
bot_cards=[]
player_cards=[]
player_card="NO_CARD"
bot_card="NO_CARD"

def draw_player():
  global cards
  return cards[random.randint(min(cards), max(cards))]

def draw_bot():
  global cards
  return cards[random.randint(min(cards), max(cards))]

while True:
  player_card=draw_player()
  bot_card=draw_bot()

  if bot_card>player_card:
    print(RED+"Bot Wins"+RESET)
    cards.remove(player_card)
    cards.remove(bot_card)
    bot_cards.append(player_card)
    bot_cards.append(bot_card)
  else:
    print(GREEN+"Player Wins"+RESET)
    cards.remove(player_card)
    cards.remove(bot_card)
    player_cards.append(player_card)
    player_cards.append(bot_card)
  print(RED+bot_card+RESET)
  print(player_card)

  wait=input("Press enter to continue")
  os.system('clear')