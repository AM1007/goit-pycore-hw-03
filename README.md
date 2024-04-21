## Working with dates, hours, and expanding functionality to work with rows.

### Task 1

Create a function called `get_days_from_today(date)` that returns the number of days between a given date and the current date.

#### Task requirements:

1. The function takes one parameter: `date`, which is a string representing a date in the format `YYYY-MM-DD` (e.g., `2020-10-09`).
2. The function returns an integer indicating the number of days from the specified date to the current date. If the specified date is later than the current one, the result will be negative.
3. Calculations should only consider days, disregarding time (hours, minutes, seconds).
4. To handle dates, you should utilize Python's `datetime` module.

#### Implementation recommendations:

1. Begin by importing the `datetime` module.
2. Convert the date string in the `YYYY-MM-DD` format to a `datetime` object.
3. Obtain the current date using `datetime.today()`.
4. Compute the difference between the current date and the specified date.
5. Return the difference in days as an integer.

#### Example:

If today is May 5, 2021, a call to `get_days_from_today("2021-10-09")` should return `157` because October 9, 2021 is 157 days later than May 5, 2021.

---

### Task 2

To win the main prize in the lottery, you must correctly match a specific number of numbers on your lottery ticket with the numbers drawn randomly within a predetermined range during the next draw. For instance, you may need to guess six numbers from a range of 1 to 49 or five numbers from 1 to 36, and so on.

You need to create a function called `get_numbers_ticket(lower_bound, upper_bound, quantity)` to generate a set of unique random numbers for such lotteries. This function should return a random set of numbers within the specified parameters, ensuring that all numbers in the set are unique.

#### Task requirements:

1. Function parameters:

- `min` - the minimum possible number in the set (at least 1).
- `max` - the maximum possible number in the set (no more than 1000).
- `quantity` - the number of numbers to be selected (a value between lower_bound and upper_bound).

1. The function generates the specified number of unique numbers within the specified range.
2. The function returns a list of randomly selected, sorted numbers. These numbers must be unique within the set. If the parameters fall outside the specified limits, the function returns an empty list.

#### Implementation recommendations:

1. Check that the input parameters meet the specified limits.
2. Utilize the `random` module for generating random numbers.
3. Employ an array or another mechanism to guarantee uniqueness of numbers.
4. Keep in mind that the get_numbers_ticket function yields a sorted list of unique numbers.

#### Example:

Let's say you need to select 6 unique numbers for a lottery ticket, with each number falling between 1 and 49. You can employ your function like this:

```python
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

```

This code invokes the function `get_numbers_ticket` with parameters `min=1`, `max=49`, and `quantity=6`. The outcome will be a list of 6 randomly selected, unique, and sorted numbers, such as `[4, 15, 23, 28, 37, 45]`. Each invocation of the function will yield a distinct set of numbers.

---

### Task 3

Your company runs an active SMS marketing campaign. To facilitate this, you gather customer phone numbers from a database. However, you frequently encounter numbers written in various formats. For instance:

```python
"    +38(050)123-32-34"
"     0503451234"
"(050)8889900"
"38050-111-22-22"
"38050 111 22 11   "
```

Your mailing service operates optimally when phone numbers are in the correct format. Hence, you require a function to automatically normalize phone numbers, stripping away any extra characters and adding the international country code if necessary.

Create a function called `normalize_phone(phone_number)` that normalizes phone numbers to a standard format, leaving only numbers and the leading `'+'` sign. The function takes one argument `'-'` a string with a phone number in any format and converts it to the standard format, leaving only numbers and the `'+'` symbol. If the number does not contain an international code, the function automatically adds the code `'+38' (for Ukraine)`. This ensures that all numbers are suitable for sending SMS.

#### Implementation recommendations:

1. Use the `re` module for regular expressions to remove unnecessary characters.
2. Check if the number starts with `'+'` and correct the prefix as instructed.
3. Remove all characters except digits and `'+'` from the phone number.
4. Don't forget to return the normalized phone number from the function.

#### Usage Example:

```python
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
```

As a result, you'll receive a list of numbers in a standard format, suitable for SMS use.

```
#Normalized Phone Numbers for SMS Sending:
['+380671234567', '+380952345678', '+380441234567',
'+380501234567', '+380501233234', '+380503451234',
'+380508889900', '+380501112222', '+380501112211']
```

### Task 4

Within your organization, you're tasked with coordinating birthday greetings for colleagues. To simplify this task, you need to develop a `get_upcoming_birthdays` function to identify colleagues deserving of congratulations. The function should yield a list of individuals whose birthdays fall within the next 7 days, including the current day.

You have a list of `users` at your disposal, each element of which contains information about the user's name and birthday. Since colleagues' birthdays may fall on the weekend, your function should also take this into account and move the greeting date to the next working day if necessary.

#### Implementation recommendations:

1. The function parameter `users` is a list of dictionaries, where each dictionary contains the keys `name` (user name, string) and `birthday` (birthday, string in the format 'year.month.date').
2. The function should determine whose birthdays are 7 days ahead including the current day. If the birthday falls on a weekend, the date of the greeting is moved to the following Monday.
3. The function returns a list of dictionaries, where each dictionary contains information about the user (`name` key) and congratulation date (`congratulation_date` key, whose data is in the string format 'year.month.date').

#### Implementation recommendations:

1. Suppose you have received a list of `users`, where each dictionary contains `name` (user name) and `birthday` (date of birth in the string format `year.month.date`). You must convert birthdates from strings to `datetime` objects. Convert a date of birth from a string to a `datetime` object - `datetime.strptime(user["birthday"], "%Y.%m.%d").date()`. Since only the date is needed (no time), use `.date()` to get just the date.
2. Determine the current system date using `datetime.today().date()`.
3. Go through the list of `users` and analyze the dates of birth of each user (`for user in users:`).
4. Check whether the birthday has already passed this year (`if birthday_this_year < today`). If so, consider a date for next year.
5. Find the difference between the birthday and the current day to determine the birthdays for the next week.
6. Check if the birthday falls on a weekend. If so, move the greeting date to next Monday.
7. Create a data structure that will store the username and the corresponding greeting date if the birthday occurs within the next week.
8. Output the collected data in the form of a list of dictionaries with usernames and dates of greetings.

#### Example:

Suppose you have a list of users:

```python
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
```

Using the `get_upcoming_birthdays` function:

```python
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
```

If today `2024.01.22` the result can be:

```python
[
    {'name': 'John Doe', 'congratulation_date': '2024.01.23'},
    {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
]
```

This list contains information about who and when to wish a happy birthday.
