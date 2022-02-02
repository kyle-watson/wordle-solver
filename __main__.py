# Read, trim, and combine files
allowed = (open("allowed.txt","r").readlines())
allowed = [w.strip() for w in allowed]
answers = (open("answers.txt","r").readlines())
answers = [w.strip() for w in answers]
words = list(set(allowed + answers))

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

        #   Get feedback from user:
        feedback = ""
        while True:
            print(f"Guess: {best_guess}")
            print("Please enter the result: ")
            safe_to_break = True
            feedback = str(input())
            if len(feedback) != 5:
                print("Result is not the proper length, must be 5 characters")
                safe_to_break = False
                continue
            for char in feedback:
                if char != 'g' and char != 'y' and char != 'b':
                    print(f"Result has illegal character: {char}, result must only contain either g, y or b, ex:bggyy for black, green, green, yellow, yellow")
                    safe_to_break = False
                    continue
            if safe_to_break:
                break

        # Evaluate feedback
        if feedback == 'ggggg':
            print("\N{Large Green Square}"*5 + "   " + best_guess)
            break
        for i, color in enumerate(feedback):
                if color == 'g':
                    # Green, remove all that do not have a green char in this slot
                    words = [word for word in words if word[i] == best_guess[i]]
                    print("\N{Large Green Square}", end='')
                elif color == 'y':
                    # Yellow, remove all words that do not have this letter and remove all words where this letter is in this slot
                    words = [word for word in words if best_guess[i] in word and word[i] != best_guess[i]]
                    print("\N{Large Yellow Square}", end='')
                elif color == 'b':
                    # Black, remove all words that contain this letter
                    words = [word for word in words if best_guess[i] not in word]
                    print("\N{Black Large Square}", end='')
                else:
                    print(f"Fatal illegal char {color}")
                    exit()

        print("   " + best_guess)
