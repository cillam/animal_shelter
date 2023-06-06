# -*- coding: utf-8 -*-
"""
Created on Wed May 24 09:47:57 2023

@author: Priscilla Miller and Jason Vou
"""
import matplotlib.pyplot as plt
from numpy import average

MONTHS = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul",
          8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}


# Plot monthly outcomes/intakes and intake averages
def monthly_in_out(count, year, category):
    labels = [MONTHS[x] for x in count.index.values]
    plt.figure(figsize=(6, 4))
    plt.style.use('seaborn-v0_8-colorblind')
    b = plt.bar(count.index.values, count, width=0.6)
    plt.bar_label(b)
    plt.title(f"Number of {category} per Month ({year})", size=16,
              weight="bold")
    plt.ylabel(f"{category}")
    plt.xlabel("Month")
    plt.xticks(count.index.values, labels)
    plt.show()


# Plot outcome and animal type pie charts
def type_pie_chart(types, title):
    types_counts = types.to_numpy()
    types_formatted = [x.title() for x in types.index.values]

    fig, ax = plt.subplots(figsize=(6, 3))
    wedges, texts, autotexts = ax.pie(types_counts,
                                      autopct=lambda pct: "{:.2f}%".format(pct)
                                      if (pct > 5) else None,
                                      startangle=180,
                                      colors=("goldenrod", "turquoise",
                                              "mediumslateblue", "lightblue",
                                              "steelblue", "olive", "grey"),
                                      textprops=dict(color="black"))

    ax.legend(wedges, types_formatted,
              loc="upper left",
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=12)
    ax.set_title(f"{title}", size=16, weight="bold")

    plt.show()


# Converts age in days to years
def convertAgeToYears(age):
    return age/365.24


# Requests user input for a specific year
def requestIntakeDateYearInput():
    year = input("Enter a year between 2013 and 2023 to view number of "
                 "intakes per month: ")
    while not year.isnumeric() or int(year) > 2023 or int(year) < 2013:
        print("Invalid input")
        year = input("Enter a year between 2013 and 2023 to view number of "
                     "intakes per month: ")
    return year


# Requests user input for a specific year
def requestOutcomeDateYearInput(string):
    year = input(f"Enter a year between 2014 and 2023 to view {string}: ")
    while not year.isnumeric() or int(year) > 2023 or int(year) < 2014:
        print("Invalid input")
        year = input(f"Enter a year between 2014 and 2023 to view {string}: ")
    return year


# Forecasts average for each month left in 2023
def forecast_2023(a_list):
    i = len(a_list)
    while i < 13:
        a_list.append(round(average(a_list[i-3:i])))
        i += 1
    return sum(a_list)
