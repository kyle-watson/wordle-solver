# wordle-solver
My attempt at an efficient wordle solver.

Word lists taken from https://gist.github.com/cfreshman/dec102adb5e60a8299857cbf78f6cf57.

Uses greedy approach where it scores each letter by how often it appears in the word list (not counting doubles). The it scores each word by summing the scores of its letters (again, not counting doubles.) Then it takes user input as feedback, modifies the word list appropriatley by removing all words that contain a black letter, removing all words that do not have a yellow letter, removing all words that have a yellow letter in that yellow letters slot, and removing all words that do not have a green letter in that green letter's slot.
