# def getCount(inputStr):
#     num_vowels = 0
    
    
#     return num_vowels


inputString = input("")

def check_vowels(inputString):
  vowels = "AaeEeIiOoUu"
  checkedVowels = [each for each in inputString if each in vowels]
  return (len(checkedVowels))

print(check_vowels(inputString))