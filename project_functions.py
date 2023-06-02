# -*- coding: utf-8 -*-
"""
Created on Wed May 24 09:47:57 2023

@author: Priscilla Miller
"""
import matplotlib.pyplot as plt

MONTHS = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul",
          8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}


# Plot monthly outcomes/intakes and intake average
def monthly_in_out(count, year, category):
    labels = [MONTHS[x] for x in count.index.values]
    plt.figure(figsize=(8, 6))
    plt.style.use('seaborn-v0_8-colorblind')
    b = plt.bar(count.index.values, count, width=0.6)
    plt.bar_label(b)
    plt.title(f"Number of {category} per Month ({year})", size=20,
              weight="bold")
    plt.ylabel(f"{category}")
    plt.xlabel("Month")
    plt.xticks(count.index.values, labels)
    plt.show()
    plt.close(plt.gcf())


# Plot outcome and animal type pie charts
def type_pie_chart(types, title):
    types_counts = types.to_numpy()
    types_formatted = [x.title() for x in types.index.values]

    fig, ax = plt.subplots(figsize=(10, 7))
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
    ax.set_title(f"{title}", size=20, weight="bold")

    plt.show()
    plt.close(plt.gcf())

def convertAgeToYears(age):
    return age/365.24

def convertDaysInShelterToYears(days):
    return days/365.24

def requestIntakeDateYearInput(df):
    year = input("Enter a year between 2013 and 2023 to view number of "
             "intakes per month: ")
    while not year.isnumeric() or int(year) > 2023 or int(year) < 2013:
        print("Invalid input")
        year = input("Enter a year between 2013 and 2023 to view number of "
                    "intakes per month: ")
    df_in_date = df[df["Intake Date"].dt.strftime("%Y") == f"{year}"]
    return year, df_in_date

def requestOuttakeDateYearInput(df):
    year = input("Enter a year between 2014 and 2023 to view number of "
             "outcomes per month: ")
    while not year.isnumeric() or int(year) > 2023 or int(year) < 2014:
        print("Invalid input")
        year = input("Enter a year between 2014 and 2023 to view number of "
                 "outcomes per month: ")
    df_out_date = df[df["Outcome Date"].dt.strftime("%Y") == f"{year}"]
    return year, df_out_date