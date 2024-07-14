import random

temperatures = [random.randint(26, 40) for _ in range(7)]
days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
even_temperatures_days = [days_of_the_week[i] for i, temp in enumerate(temperatures) if temp % 2 == 0]
good_days_count = len(even_temperatures_days)
highest_temp = max(temperatures)
highest_temp_day = days_of_the_week[temperatures.index(highest_temp)]
lowest_temp = min(temperatures)
lowest_temp_day = days_of_the_week[temperatures.index(lowest_temp)]
average_temp = sum(temperatures) / len(temperatures)
above_avg = [(days_of_the_week[i], temp) for i, temp in enumerate(temperatures) if temp > average_temp]

print("Temperatures for the week:", temperatures)
print("Good days for Shelly:", even_temperatures_days)
print("Number of good days for Shelly:", good_days_count)
print("The highest temperature was on", highest_temp_day, "with", highest_temp, "degrees.")
print("The lowest temperature was on", lowest_temp_day, "with", lowest_temp, "degrees.")
print("The average temperature was:", round(average_temp, 2))
print("Days with temperatures above the average:", above_avg)