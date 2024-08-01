import string


def uniqueMorseRepresentations(words):
      alphabet = list(string.ascii_lowercase)
      
      dot_dash_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

      dict_alpha_dashes = {alphabet[i]:dot_dash_list[i] for i in  range(len(alphabet))}
      return len(set(["".join([dict_alpha_dashes[j] for j in i]) for i in words]))

words = ["gin","zen","gig","msg"]
print(uniqueMorseRepresentations(words))
words = ["a"]
print(uniqueMorseRepresentations(words))
