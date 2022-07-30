def forecast(days):
    sunshine_count = 0
    rain_count = 0
    snow_count = 0

    for day in days:
        if day == "sunshine":
            sunshine_count += 1
        elif day == "rain":
            rain_count += 1
        elif day == "snow":
            snow_count += 1
    if (rain_count > sunshine_count and rain_count > snow_count) or (rain_count < snow_count and snow_count == sunshine_count):
        return "rain"
    elif (sunshine_count > rain_count and sunshine_count > snow_count) or (sunshine_count < rain_count and rain_count == snow_count):
        return "sunshine"
    elif (snow_count > sunshine_count and snow_count > rain_count) or (snow_count < rain_count and rain_count == sunshine_count):
        return "snow"
    elif sunshine_count == rain_count and rain_count == snow_count:
        return days[len(days) - 1]


print(forecast(["snow", "snow", "rain", "sunshine"]))
print(forecast(["rain", "rain", "snow", "snow", "sunshine", "sunshine"]))
print(forecast(["rain", "rain", "sunshine", "sunshine"]))
