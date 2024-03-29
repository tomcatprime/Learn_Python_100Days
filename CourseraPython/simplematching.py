import re
#always use raw string for regular expressions
result = re.search(r"aza", "plaza")
print(result)
result = re.search(r"aza", "bazaaaar")
print(result)
result = re.search(r"aza", "Buchar")
print(result)


#exercise Fill in the code to check if the text passed contains the vowels a, e and i, with exactly one occurrence of any other character in between.

def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

#match by case insensitive
print(re.search(r"p.ng", "Pangeea", re.IGNORECASE ))

#wildcards and Characters classes
# dot . matching any character

#character classes in [] brackets

print(re.search(r"[Pp]ython", "oliPythonista"))

#lower case a-z - range of characters
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search(r"[A-Z]on", "Matching amAon"))

#coursera exercise

#Fill in the code to check if the text passed contains punctuation symbols:
#commas, periods, colons, semicolons, question marks, and exclamation points.
import re
def check_punctuation (text):
  result = re.search(r"[,.:;?!]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

print(re.search(r"cat|dog", "Matching cat"))
print(re.findall(r"cat|dog", "Finding all cats and dogs"))

