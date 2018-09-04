# def getCount(inputStr):
#     num_vowels = 0
    
    
#     return num_vowels

print ("Input a string and it will return the number of vowels!")
inputString = input("")

def check_vowels(inputString):
  vowels = "AaeEeIiOoUu"
  checkedVowels = [each for each in inputString if each in vowels]
  return (len(checkedVowels))

print("Number of vowels: {}".format(check_vowels(inputString)))