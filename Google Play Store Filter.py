# Google Play Store Data Filter
# Authored by Matthew Steuerer, Nikhil Sankepalli, and Seth Curry
# October 7th, 2020
# Demonstrates the use of Lists is Python with 2018 Google Play Store Data
# Data Source URL: https://www.kaggle.com/lava18/google-play-store-apps

# User inputs their criteria and the program needs to find all records that match

import csv

<<<<<<< HEAD
=======

# Class to represent an app object and all its properties (columns) from the data source


class GoogleApp:
    def __init__(self, app, category, rating, reviews, size, installs, type, price, contentRating, genres, lastUpdated,
                 currentVer, androidVer):
        self.app = app
        self.category = category
        self.rating = rating
        self.reviews = reviews
        self.size = size
        self.installs = installs
        self.type = type
        self.price = price
        self.contentRating = contentRating
        self.genres = genres
        self.lastUpdated = lastUpdated
        self.currentVer = currentVer
        self.androidVer = androidVer

    # String Representation of Google App Object (How its displayed once its printed)
    def __str__(self):
        appString = self.app + " " + self.category + " " + self.rating + " " + self.reviews + " "
        appString = appString + " " + self.size + " " + self.installs + " " + self.type + " "
        appString = appString + " " + self.price + " " + self.contentRating + " " + self.genres + " "
        appString = appString + " " + self.lastUpdated + " " + self.currentVer + " " + self.androidVer
        return appString

>>>>>>> parent of 8a95aa2... Scrap Object Approach
# Our list object which will hold the entire data source for processing
appList = []

# Use a reader object to read from csv file data source
with open('googleplaystore.csv') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=',')
    i = 0
    for row in readCSV:
        # Note: needed to edit data source as one row had two columns that were null and reader object threw errors
        # For each row in the file, make an object and append it to the list of items
<<<<<<< HEAD
        listFormOfApp = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                         row[11], row[12]]
        print(listFormOfApp)
        appList.append(listFormOfApp)


# Display function that only serves to format menu selection
def displayColumns():
    print("1. App Name \t 2. Category \t 3. Rating (1-5) \t 4. # of Reviews \t 5. Size (in MB) 6. # of Installs \n")
    print("7. Type (Paid or Free) \t 8. Price (don't enter $ sign) \t 9. Content Rating \t 10. Genres \t 11. Last "
          "Updated Date \n")
    print("12. Current Version (Only checks major versions, not minor) \t 13. Android Version (minimum Android OS "
          "required, also only checks major version \n")
=======
        appList.append(
            GoogleApp(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                      row[12]))
        # The first object in the list is the column headings, and could be ignored
        # just used for debugging print(appList[0])
>>>>>>> parent of 8a95aa2... Scrap Object Approach

        # just used for debugging i = i + 1

<<<<<<< HEAD
def searchOneTerm(columnInput1, searchList, searchedTerm1):  # the input1 here is the column to search
    length = len(searchList)
    index1 = 0
    totalMatchingRows = 0
    while index1 < length:  # go through the entire list; remember that users input will be 1 higher
        checkApp = appList[i]
        print(checkApp[input1])
        # print(type(checkApp[input1]))
        if searchedTerm1 in checkApp[columnInput1 - 1]:
            print(checkApp)
            totalMatchingRows = totalMatchingRows + 1
        # input 1 is the column, or row[input1] from when the objects were made but now they correspond to
        # variables... input1 could still be the column, we could have the data arranged as a multi dimensional list?
        # a list of lists that are just strings of the input; then we do if list[i].[input1] == searchterm and
        # abandon object approach, just makes things complicated ;

        index1 = index1 + 1

    print("Total apps matching your search: " + str(totalMatchingRows))


def searchTwoTerms(columnInput1, columnInput2, searchList, searchedTerm1,
                   searchedTerm2):  # the input1 here is the column to search
    length = len(searchList)
    index1 = 0
    totalMatchingRows = 0
    while index1 < length:  # go through the entire list; remember that users input will be 1 higher
        checkApp = appList[i]
        if searchedTerm1 in checkApp[columnInput1 - 1] and searchedTerm2 in checkApp[columnInput2 - 1]:
            print(checkApp)
            totalMatchingRows = totalMatchingRows + 1

        index1 = index1 + 1

    print("Total apps matching your search: " + str(totalMatchingRows))


def searchThreeTerms(columnInput1, columnInput2, columnInput3, searchList, searchedTerm1, searchedTerm2,
                     searchedTerm3):  # the input1 here is the column to search
    length = len(searchList)
    index1 = 0
    totalMatchingRows = 0
    while index1 < length:  # go through the entire list; remember that users input will be 1 higher
        checkApp = appList[i]
        if searchedTerm1 in checkApp[columnInput1 - 1] and searchedTerm2 in checkApp[columnInput2 - 1] and searchedTerm3 in \
                checkApp[columnInput3 - 1]:
            print(checkApp)
            totalMatchingRows = totalMatchingRows + 1

        index1 = index1 + 1

    print("Total apps matching your search: " + str(totalMatchingRows))


=======
# No more needs to be done to load the source
# Now just need to offer a menu with search options for user;
# Different options depending on which column they want to search on
>>>>>>> parent of 8a95aa2... Scrap Object Approach
# Requirements state user must be able to search by up to three values (Need to check up to 3 columns)
# Ask user how many search values they will enter (up to three allowed)
# Have a switch statement depending on which columns user would like to search by
# Have the switch run in a loop with an exit command

# First, prompt and ask user how many key values they will search for

print("Welcome to the Google Play Store Filter!")
print("This program allows you to select up to three search terms to find matching Google Apps")
print("Note: You will be prompted to select how many fields you'd like to search by first.")
print("Then, you will be prompted for your search term. Enter the term, followed by enter with no unnecessary white "
      "spaces.")

exitCondition = False  # exit condition to terminate menu loop
while not exitCondition:
    numberOfSearchTerms = int(input("Would you like to use 1, 2, or 3 search terms? Please type the number and press "
                                    "enter. Enter 4 to exit the program."))
    if numberOfSearchTerms == 1:
        # offer all columns and let user pick one to search on
        # then search the entire list at that columns index and return all that match
<<<<<<< HEAD
        displayColumns()
        input1 = int(input("Which column above would you like to search on? \n"))
        searchTerm1 = input("What term do you wish to search for? \n")
        print(input1)
        print(searchTerm1)
        # searchOneTerm function
        searchOneTerm(input1, appList, searchTerm1)
    elif numberOfSearchTerms == 2:
        displayColumns()
        input1 = int(input("Select the first column you would like to search on: \n"))
        input2 = int(input("Select the second column you would like to search on: \n"))
        searchTerm1 = input("What is the first term you wish to search for? \n")
        searchTerm2 = input("What is the second term you wish to search for? \n")
        searchTwoTerms(input1, input2, appList, searchTerm1, searchTerm2)
    elif numberOfSearchTerms == 3:
        displayColumns()
        input1 = int(input("Select the first column you would like to search on: \n"))
        input2 = int(input("Select the second column you would like to search on: \n"))
        input3 = int(input("Select the third column you would like to search on: \n"))
        searchTerm1 = input("What is the first term you wish to search for? \n")
        searchTerm2 = input("What is the second term you wish to search for? \n")
        searchTerm3 = input("What is the third term you wish to search for? \n")
        searchThreeTerms(input1, input2, input3, appList, searchTerm1, searchTerm2, searchTerm3)
=======
        # display columns function
        input1 = input("Which column above would you like to search on?")
        # searchOneTerm function
    elif numberOfSearchTerms == 2:
        # display columns function
        input1 = input("Select the first column you would like to search on: ")
        input2 = input("Select the second column you would like to search on: ")
        # searchTwoTerms(input1, input2)function
    elif numberOfSearchTerms == 3:
        # display columns function
        input1 = input("Select the first column you would like to search on: ")
        input2 = input("Select the second column you would like to search on: ")
        input3 = input("Select the third column you would like to search on: ")
        # searchThreeTerms(input1, input2, input3) function
>>>>>>> parent of 8a95aa2... Scrap Object Approach
    elif numberOfSearchTerms == 4:
        exitCondition = True


