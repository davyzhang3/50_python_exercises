class HourTooLowError(Exception): pass
class HourTooHighError(Exception): pass

RATES = {
    'Chico': 0.5,
    'Groucho': 0.7,
    'Harpo': 0.5,
    'Zeppo': 0.4
}

def time_percentage(hour):
    return hour / 24 

def calculate_tax(amount, state, hour):
    if hour < 0:
        raise HourTooLowError(f'Hour of {hour} is < 0')
    if hour >= 24:
        raise HourTooHighError(f'Hour of {hour} is >= 24')
    return amount + (amount * RATES[state] * time_percentage(hour))


print(calculate_tax(500, 'Harpo', 12))