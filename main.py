import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = 'abc@gmail.com'
PASSWORD = 'abcdefghijkl'

data = {
    'name': ['jelly', 'belly'],
    'email': ['jelly@gmail.com', 'belly@yahoo.com'],
    'year': [1982, 1987],
    'month': [9, 6],
    'day': [9, 6],
}
df = pandas.DataFrame(data)
# details = df.to_csv('birthdays.csv', mode='a', index=False, header=False)
birthday_data = pandas.read_csv("birthdays.csv")
# print(birthday_data)

birthday_date_list = birthday_data['day']
# print(birthday_date_list.to_list())

birthday_month_list = birthday_data['month']
# print(birthday_month_list.to_list())

birthday_email_list = birthday_data['email']
# print(birthday_email_list.to_list())

birthday_name_list = birthday_data['name']
# print(birthday_name_list.to_list())

current_day = dt.datetime.now()
today_date = current_day.day
today_month = current_day.month

# birthday_day_row = birthday_data[birthday_data['day'] == today_date]
index = -1
for date in birthday_date_list:
    if date != today_date:
        index += 1
# print(index)

random_number = random.randint(1, 3)
# print(random_number)
with open(f"./letter_templates/letter_{random_number}.txt") as letter:
    letter_data = letter.read()
    # print(str(letter_data))
    named_letter = letter_data.replace("[NAME]", birthday_name_list[index])
    print(named_letter)

if birthday_date_list[index] == today_date:
    if birthday_month_list[index] == today_month:

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, to_addrs=birthday_email_list[index],
                msg=f"Subject:Happy Birthday!\n\n{named_letter}"
            )
