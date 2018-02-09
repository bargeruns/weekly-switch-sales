import requests
import json
import datetime
import settings
from twilio.rest import Client

client = Client(settings.TWILIO_SID, settings.TWILIO_TOKEN)

page = requests.get("https://www.nintendo.com/json/content/get/filter/game?limit=40&offset=0&system=switch&sale=true")

json_response = page.json()

game_list_text = "# On Sale This Week \n" + "Updated " + datetime.date.today().isoformat() + "\n\n"

for game in json_response["games"]["game"]:
	if "sale_price" in game:
		game_list_text += "[" + game["title"] + " - $" + game["sale_price"] + "]" + "(https://www.nintendo.com/games/detail/" + game["slug"] + ")" + "\n\n"

payload = { 
	"description": "Weekly Switch Sales", 
	"files": {
		"switch_sales.md": {
			"content": game_list_text
		}
	}
}

post = requests.patch(settings.GIST_API_URL + settings.GIST_TOKEN, data = json.dumps(payload))

if post.status_code != 200:
	message = client.messages.create(
		to=settings.PHONE_NUMBER_TO,
		from_=settings.PHONE_NUMBER_FROM,
		body="Weekly Switch Sales update failed, check the logs!"
	)
else:
	message = client.messages.create(
		to=settings.PHONE_NUMBER_TO,
		from_=settings.PHONE_NUMBER_FROM,
		body="Switch Sales list updated!\n" + settings.GIST_PUBLIC_URL 
	)

