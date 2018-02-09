# Weekly Switch Sales

[View the list of on-sale games here!](https://gist.github.com/bargeruns/616e5358220cfbae0daf3e2b169e9d8b)

I wrote this Python script to make it easier to find out which Nintendo Switch games go on sale each week. Nintendo's website can be _painfully_ slow to navigate, and it requires (IMO) too many steps to see Switch-specific sales. I decided this would be a good time to dust off and brush up on a few skills, specifically:

- Python
- Git + SSH on my remote [Linode server](https://www.linode.com/?r=0e7c841f5fca7598ff7fa3a60bf708f736e870f8)
- Linux server management
- Cron

## How does it work?

The `scraper.py` script gets the latest on-sale Switch games from Nintendo's website as JSON. This gets parsed into a list of Markdown links, and then sent via HTTP PATCH to a Github Gist, so people can check the list. The script is then cloned onto my [Linode](https://www.linode.com/?r=0e7c841f5fca7598ff7fa3a60bf708f736e870f8) machine, where I setup a cron task to run the script every Monday to get the latest sales. 

## DIY

Feel free to clone this repo and make it your own. Below are a few steps you'll need to take.

### 1. Setup a free Twilio account
The script uses Twilio to send an SMS notification. [Check out the Twilio docs for Python](https://www.twilio.com/docs/libraries/python) to learn more about the integration, and then sign up for a free Twilio account so you can send yourself an SMS when the script completes or fails.

### 2. Install Python Modules
`cd` into this repo on your machine, and run `$ pip install -r requirements.txt`

### 3. Setup Environment Variables
If you examine `settings.py`, you'll see the list of environment variables you'll need to make the script work. Put these into a new file, `.env` in the root of the project.

You'll need:

- Your Twilio API token and from_ phone number
- The phone number where you want to receive notifications
- A Github OAuth token with the rights to create Gists under your Github account
- A Github Gist where you can post the updated list

Fill out the appropriate variables and save your `.env`.

### 4. Run the script!

Fire away! `cd` into this repo and run `$ python scraper.py`. You should get an SMS when the script completes. Check your console for any errors.

## (Optional) Setup a Cron task

If you want this to all start happening _for_ you, you'll need to get the script running on an automated basis using cron. I encourage you to learn about cron on your own, but let me give you the points you'll need to get started:

1. You'll need a server to host this stuff on! I highly recommend [Linode](https://www.linode.com/?r=0e7c841f5fca7598ff7fa3a60bf708f736e870f8), they have great documentation and make it really easy to get your very own private, hosted Linux server setup and running!
2. You'll need to create an executable bash script to run the `scraper.py` script. This script needs to live in `/etc/cron.weekly` (for weekly execution), or `/etc/cron.daily` for daily, etc.
3. You'll need to edit your `crontab` file to run your weekly/daily/hourly/whatever cron jobs.

If you can get all of this working, you'll feel like a god and, even better - you'll never miss another great deal on a Nintendo Switch game!!!
