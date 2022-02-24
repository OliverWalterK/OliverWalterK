import scraper2

bot = scraper2.Scraper('https://ftx.com/markets')

bot.find_all_links()
bot.valid_links()