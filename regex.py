import re

pattern = 'g....o'
test_string = 'giulio is giulio studying.'

result = re.match(pattern, test_string)
# will return a match only if occurred at the beginning of string
print("1", result)
input(".match() done - continue with .search()")
print()


result = re.search(pattern, test_string)
# will return a match if occurred somewhere in the string
print("2", result)
input(".search() done - continue with .findall()")
print()


result = re.findall(pattern, test_string)
# returns all matches and stores it into a list
print("3", result)
input(".findall() done - continue with .finditer()")
print()


result = re.finditer(pattern, test_string)
# returns all matches and stores it into a list - including exact index
print("4", result)
input("press enter to show all of the objects of .finditer() result")
print()


for match in result:
    print(match)