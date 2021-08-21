from venmo_api import Client
from dotenv import load_dotenv
from notifiers import get_notifier
from datetime import datetime

from utils import get_env, env_vars, get_month, Venmo, Telegram

def main(now):
  """
  The main function which initiates the script.
  """

  load_dotenv()  # take environment variables from .env.
  actualVars = []
  for var in env_vars:
    actualVars.append(get_env(var))

  access_token, chat_id, bot_token, k_friend_id, s_friend_id, t_friend_id = actualVars

  month = get_month(now)
  venmo = Venmo(access_token)
  telegram = Telegram(bot_token, chat_id)

  friends =[
    {
      "name": "Kirk",
      "id": k_friend_id,
    },
    {
      "name": "Santiago",
      "id": s_friend_id,
    },
    {
      "name": "Tabitha",
      "id": t_friend_id,
    },
  ]

  successfulRequests = []
  expectedRequests = len(friends)

  # Request Set 1
  for friend in friends[:2]:
    name = friend["name"]
    id = friend["id"]
    description = "Ziply internet bill for the month of " + month
    amount = 13.33
    message = f"""Good news old sport!

I have successfully requested money from {name}.

— Efron 🤵🏻‍♂️
    """
    success = venmo.request_money(id, amount, description, telegram.send_message(message))
    if success:
      successfulRequests.append(success)

  # Request Set 2
  for friend in friends[2:3]:
    name = friend["name"]
    id = friend["id"]
    description = "Spotify for the month of " + month
    amount = 7.14
    message = f"""Good news old sport!

I have successfully requested money from {name}.

— Efron 🤵🏻‍♂️
    """
    success = venmo.request_money(id, amount, description, telegram.send_message(message))
    if success:
      successfulRequests.append(success)

  if len(successfulRequests) == expectedRequests:
    print("✅ Ran script successfully and sent " + str(expectedRequests) + " Venmo requests.")
  else:
    print("❌ Something went wrong. Only sent " + str(len(successfulRequests)) + "/" + str(expectedRequests) + " venmo requests.")

now = datetime.now()
main(now)
