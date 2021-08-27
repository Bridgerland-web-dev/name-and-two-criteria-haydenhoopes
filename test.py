import codecs
from bs4 import BeautifulSoup


f=codecs.open("index.html", "r")
soup = BeautifulSoup(f.read(), 'html.parser')

fullName = soup.find(id="name").text

# Test 1: First and last name are present
assert len(fullName.split(" ")) >= 2, "Please include your full name"


allCriteria = soup.find_all(class_="criteria")

# Test 2: Are there more than one criteria?
assert len(allCriteria) >= 2, "There need to be at least 2 criteria"
