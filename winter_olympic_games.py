# pylint: disable=missing-docstring

import csv

COUNTRIES_FILEPATH = "data/dictionary.csv"
MEDALS_FILEPATH = "data/winter.csv"

def most_decorated_athlete_ever():
    """Returns who won the most winter olympic games medals (gold/silver/bronze) ever"""
    medal_dict = {}
    with open(MEDALS_FILEPATH, encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, skipinitialspace=True)
        for row in list(reader):
            if row['Athlete'] in medal_dict:
                medal_dict[row['Athlete']]+= 1
            else:
                medal_dict[row['Athlete']] = 1
        for key, value in medal_dict.items():
            if value == max(medal_dict.values()):
                return key
    return None
    #pass  # YOUR CODE HERE

def country_with_most_gold_medals(min_year, max_year):
    """Returns which country won the most gold medals between `min_year` and `max_year`"""
    medal_dict = {}
    country_abbv = {}
    with open(COUNTRIES_FILEPATH, encoding="utf8") as country:
        reader_country = csv.DictReader(country, skipinitialspace=True)
        for row in list(reader_country):
            country_abbv[row['Code']] = row['Country']

    with open(MEDALS_FILEPATH, encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, skipinitialspace=True)
        list_gold = []
        for row in list(reader):
            if row['Medal'] == 'Gold':
                list_gold.append(row)

        list_year_gold = []
        for row_year in list_gold:
            if int(row_year['Year']) in list(range(min_year, max_year + 1)):
                list_year_gold.append(row_year)

        for row_gold in list_year_gold:
            if row_gold['Country'] in medal_dict:
                medal_dict[row_gold['Country']] += 1
            else:
                medal_dict[row_gold['Country']] = 1

        for key, value in medal_dict.items():
            if value == max(medal_dict.values()):
                return country_abbv[key]
    return None
    #pass  # YOUR CODE HERE

def top_three_women_in_five_thousand_meters():
    """Returns the three women with the most 5000 meters medals(gold/silver/bronze)"""
    medal_dict = {}
    with open(MEDALS_FILEPATH, encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, skipinitialspace=True)
        list_event = []
        for row in list(reader):
            if row['Event'] == '5000M' and row['Gender'] == 'Women':
                list_event.append(row)
        for row_list_event in list_event:
            if row_list_event['Athlete'] in medal_dict:
                medal_dict[row_list_event['Athlete']]+= 1
            else:
                medal_dict[row_list_event['Athlete']] = 1

        sorted_dict = dict(sorted(medal_dict.items(), key = lambda x:x[1], reverse=True))
    return list(sorted_dict.keys())[:3]
    #pass  # YOUR CODE HERE
