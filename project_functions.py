# -*- coding: utf-8 -*-
"""
Created on Wed May 24 09:47:57 2023

@author: Priscilla Miller
"""
import matplotlib.pyplot as plt
from numpy import arange

MONTHS = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul",
          8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}


# Plot monthly outcomes/intakes and intake average
def monthly_in_out(count, year, category):
    labels = [MONTHS[x] for x in count.index.values]
    plt.figure(figsize=(8, 6))
    plt.style.use('seaborn-v0_8-colorblind')
    b = plt.bar(count.index.values, count, width=0.6)
    plt.bar_label(b)
    plt.title(f"Number of {category} per Month ({year})")
    plt.ylabel(f"{category}")
    plt.xlabel("Month")
    plt.xticks(count.index.values, labels)
    plt.show()
    plt.close(plt.gcf())


# this function will be updated to plot monthly average against adoption average
def monthly_in_out_grouped(count1, count2, year):
    months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
              "Oct", "Nov", "Dec")
    categories = {
        "Intakes": count1,
        "Outcomes": count2,
        }

    x = arange(len(months))
    width = 0.4
    multiplier = 0

    plt.figure(figsize=(12, 6))
    plt.style.use('seaborn-v0_8-colorblind')
    ax = plt.subplot()

    for category, count in categories.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, count, width, label=category)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    ax.set_ylabel("Intake/Outcome Count")
    ax.set_title(f"Number of Intakes/Outcomes per Month ({year})")
    ax.set_xticks(x + width, months)
    ax.legend(ncols=3)

    plt.show()
