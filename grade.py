#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Nov 2019
# This program says what percentage per grade

def marks(grade):
    # process

    marks = None
    if grade == "4+" or grade == "A+":
        marks = "97%"
    elif grade == "4" or grade == "A":
        marks = "90%"
    elif grade == "4-" or grade == "A-":
        marks = "83%"
    elif grade == "3+" or grade == "B+":
        marks = "78%"
    elif grade == "3" or grade == "B":
        marks = "74%"
    elif grade == "3-" or grade == "B-":
        marks = "71%"
    elif grade == "2+" or grade == "C+":
        marks = "68%"
    elif grade == "2" or grade == "C":
        marks = "64%"
    elif grade == "2-" or grade == "C-":
        marks = "61%"
    elif grade == "1+" or grade == "D+":
        marks = "58%"
    elif grade == "1" or grade == "D":
        marks = "54%"
    elif grade == "1-" or grade == "D-":
        marks = "51%"
    elif grade == "0+" or grade == "R+":
        marks = "46%"
    elif grade == "0" or grade == "R":
        marks = "36%"
    elif grade == "0-" or grade == "R-":
        marks = "26%"
    elif grade == "N/E" or grade == "n/e":
        marks = "No Evidence"

    else:
        marks = ("Sorry Invalid Mark")

    return marks


def main():
    # output

    grade = input("Please Enter A Mark In Level Format (ex: 4+): ")
    level = marks(grade)
    print(level)


if __name__ == "__main__":
    main()
