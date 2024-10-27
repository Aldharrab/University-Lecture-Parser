'''
HTML TO CSS CONVERTER FOR DATA SCRAPED OFF THE UBT COURSE DATABASE

Imports both the regular expressions package (default package, no pip install needed) and Beautifulsoup (pip install bs4 or sudo apt get python3-bs4)
Main function is to parse throught HTML provided publicly by the UBT website and turns it into a table that can be used by Microsoft excel or Access.
'''


import re
from bs4 import BeautifulSoup


with open("HTML Parser/CourseList.html") as courseList:
    soup = BeautifulSoup(courseList, "html.parser")
    
def ParseFile():
    try:
        with open('HTML Parser/CourseList.html', 'r') as file:
            print("List.html FOUND")
    except FileNotFoundError:
        print("Please provide the CourseList.html File") 
    try:
        with open('HTML Parser/CourseList.csv', 'r') as file:
            print("Please delete The CourseList.csv file so a new one can be created")
    except FileNotFoundError:
        OutputFile = open("HTML Parser/CourseList.csv", "a+")
        OutputFile.write("Course Number,Title,Unit,Section,Instructor,Time,Days,Building,Room,Status,Gender,Study Type\n")
        courses = soup.find_all("tr")
        for course in courses:
            entries = course.find_all("td")
            i=0
            if (entries!= []):

                for entry in entries:
                    OutputFile.write(re.sub(r'<.+?>', '', str(entry)).strip().replace("&amp;","&"))
                    OutputFile.write(',')


                OutputFile.write("\n")
        OutputFile.close()
        print("parsing Complete")
    return



'''
UBT Courselist HTML to CSV converter.
'''
def main():
   #Create Output File
   ParseFile()

   
if __name__ == "__main__":
    main()