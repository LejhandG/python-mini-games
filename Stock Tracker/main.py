import smtplib
from datetime import datetime, timedelta
import requests

STOCK_NEWS_API = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=STOCKNAME.BSE&outputsize=full&apikey=API_KEY"
stock_news_request = requests.get(STOCK_NEWS_API)
stock_data = stock_news_request.json()

yesterday_closing_price = stock_data["Time Series (Daily)"][(datetime.now() - timedelta(1)).strftime('%Y-%m-%d')]["4. close"]

daybefore_yesterday_closing_price = stock_data["Time Series (Daily)"][(datetime.now() - timedelta(2)).strftime('%Y-%m-%d')]["4. close"]
price_diff = abs(float(yesterday_closing_price) - float(daybefore_yesterday_closing_price))
diff_perc = (price_diff/float(daybefore_yesterday_closing_price)) * 100

NEWS_DATA = requests.get(f"https://newsapi.org/v2/everything?q=companyname&from={(datetime.now() - timedelta(2)).strftime('%Y-%m-%d')}&to={(datetime.now() - timedelta(2)).strftime('%Y-%m-%d')}&sortBy=popularity&apiKey=API_KEY").json()
email_body = (
             "Company Name: " + "\n" + \
             "Stock Name: " + "\n" + \
             f"{(datetime.now() - timedelta(2)).strftime('%Y-%m-%d')} Closing Price: {daybefore_yesterday_closing_price}" + "\n" + \
             f"{(datetime.now() - timedelta(1)).strftime('%Y-%m-%d')} Opening Price: {yesterday_closing_price}" + "\n" + \
             f"Price Change: {price_diff:.2f}" + "\n" + \
             f"Percentage Change: {diff_perc:.2f}%" + "\n\n" + \
             "Relevant News" + "\n" + \
             NEWS_DATA["articles"][0]["title"] + "\n" + \
             NEWS_DATA["articles"][0]["description"] + "\n\n" + \
             NEWS_DATA["articles"][1]["title"] + "\n" + \
             NEWS_DATA["articles"][1]["description"] + "\n\n" + \
             NEWS_DATA["articles"][2]["title"] + "\n" + \
             NEWS_DATA["articles"][2]["description"])

if diff_perc > 0:
    if daybefore_yesterday_closing_price < yesterday_closing_price:
        subject = f"COMPANY NAME: 🔺{diff_perc:.2f}%"
        body = email_body
        msg = f"Subject: {subject}\n\n{body}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="youremail@gmail.com", password="APP_PASSWORD")
            connection.sendmail(
                from_addr="youremail@gmail.com",
                to_addrs="emailtosend@gmail.com",
                msg=msg.encode('utf-8')
            )
    else:
        subject = f"COMPANY NAME: 🔻{diff_perc:.2f}%"
        body = email_body
        msg = f"Subject: {subject}\n\n{body}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="youremail@gmail.com", password="APP_PASSWORD")
            connection.sendmail(
                from_addr="youremail@gmail",
                to_addrs="emailtosend@gmail",
                msg=msg.encode('utf-8')
            )