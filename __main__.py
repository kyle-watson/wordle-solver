
answer = "tater"
alphabet = 'abcdefghijklmnopqrstuvwxyz'


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
    #   4) Remove all words with black letters
    #   5) Remove all words that do not have yellow letters
    #   6) Remove all words with yellow letters in guessed slot
    #   Repeat
    
    #   1) Make a dictonary of letters and the number of times they appear in the word list
    #       (do not count double letters within words when scoring letters)
    letter_scores = score_letters
    print(f"Letter Scores: {letter_scores}")

    #   2) Score each word by summing each letter's score in dictionary
    #       (also do not count double letters within words towards a words score)
    best_guess = find_best_guess(words, letter_scores)

    #   3) Evaluate the word with the highest score
    