answer = "sills"


def score_letters(words):
    letter_scores = {}
    for word in words:
        # Foreach unique character...
        for char in set(word):
            try:
                letter_scores[char] += 1
            except KeyError:
                # If the character isn't in the dictionary, update dictionary
                letter_scores.update({char: 1})

    return letter_scores

def find_best_guess(words, letter_scores):
    # Finds the word with the highest score
    best_guess = words[0]
    best_score = -1

    for word in words:
        score = 0
        for char in set(word):
            score += letter_scores[char]
        if score > best_score:
            best_guess = word
            best_score = score

    return best_guess

def find_worst_guess(words, letter_scores):
    # Finds the word with the lowest score
    worst_guess = words[0]
    worst_score = 9999999999

    for word in words:
        score = 0
        for char in set(word):
            score += letter_scores[char]
        if score < worst_score:
            worst_guess = word
            worst_score = score

    return worst_guess

if __name__ == "__main__":


    # Read file
    words = (open("allowed.txt","r").readlines())

    # Trim '\n' off end of each word
    words = [w.strip() for w in words]

    # Greedy approach:
    #   1) Make a dictonary of letters and the number of times they appear in the word list
    #       (do not count double letters within words when scoring letters)
    #   2) Score each word by summing each letter's score in dictionary
    #       (also do not count double letters within words towards a words score)
    #   3) Evaluate the word with the highest score
    #       Remove all words with black letters
    #       Remove all words that do not have yellow letters
    #       Remove all words with yellow letters in guessed slot
    #   Repeat until solved

    for _ in range(20):
        #   1) Make a dictonary of letters and the number of times they appear in the word list
        #       (do not count double letters within words when scoring letters)
        letter_scores = score_letters(words)

        #   2) Score each word by summing each letter's score in dictionary
        #       (also do not count double letters within words towards a words score)
        best_guess = find_best_guess(words, letter_scores)

        #   3) Evaluate the word with the highest score
        if best_guess == answer:
            print("\N{Large Green Square}"*5 + "   " + best_guess)
            break
        for i, (char, char_ans) in enumerate(zip(best_guess, answer)):
            if char == char_ans:
                # Green, remove all that do not have a green char in this slot
                words = [word for word in words if word[i] == char]
                print("\N{Large Green Square}", end='')
            elif char in answer:
                # Yellow, remove all words that do not have this letter and remove all words where this letter is in this slot
                words = [word for word in words if char in word and word[i] != char]
                print("\N{Large Yellow Square}", end='')
                pass
            else:
                # Black, remove all words that contain this letter
                words = [word for word in words if char not in word]
                print("\N{Black Large Square}", end='')
                pass
            
        print("   " + best_guess)
