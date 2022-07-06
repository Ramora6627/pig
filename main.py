"""
Create a function that takes a string consisting of one or more all-lowercase words separated by spaces. It should return a new string converted to "pig Latin," where each word has its first letter moved to the back and the letters "ay" are added to the end of the word. However, words starting with a vowel (a, e, i, o, or u) should not be altered.
Examples:
pig_latin("something") # should return "omethingsay"
pig_latin("awesome") # should return "awesome" (words starting with a vowel should not be altered)
pig_latin("latin is a hard language") # should return "atinlay is a ardhay anguagelay"
pig_latin("y") # should return "yay"
pig_latin("e") # should return "e"
"""

def pig_latin(sentence):
  vowels = ["a","e","i","o","u"]
  output = sentence.split()
  for i in range(len(output)):
    if output[i][0] not in vowels:
      new_word = output[i][1:] + output[i][:1] +"ay"
      output[i] = new_word
      print(output)

  x = " ".join(output) 
  print (x)
  return x


# Test cases
assert pig_latin("something") == "omethingsay"
assert pig_latin("awesome") == "awesome"
assert pig_latin("latin is a hard language") == "atinlay is a ardhay anguagelay"
assert pig_latin("y") == "yay"
assert pig_latin("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")