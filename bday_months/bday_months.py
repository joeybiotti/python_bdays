import json
from collections import Counter

def load_dictionary():
    with open('bdays.json', 'r') as f:
        _bdays = dict(json.load(f))
    return _bdays

def display_months():
    dates = dict(Counter([val[:-8] for key, val in _bdays.items()]))

    nums_to_string = {
        '01' : 'Jan'
        '02' : 'Feb'
        '03' : 'March'
        '04' : 'April'
        '05' : 'May'
        '06' : 'Jun'
        '07' : 'July'
        '08' : 'Aug'
        '09' : 'Sept'
        '10' : 'Oct'
        '11' : 'Nov'
        '12' : 'Dec'
    }

    months = dict()
    for key, val in nums_to_string.items():
        months[val] = dates[key]

    return months

if __name__ == "__main__":
    bdays = load_dictionary()
    display_months(bdays)