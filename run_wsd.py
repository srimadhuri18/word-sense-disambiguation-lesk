from src.wsd_lesk import word_sense_disambiguation


def main():

    sentences = [
        "I deposited money in the bank",
        "The river bank was very steep",
        "He sat on the bank of the river"
    ]

    ambiguous_word = "bank"

    for sentence in sentences:

        print("\nSentence:", sentence)

        sense = word_sense_disambiguation(sentence, ambiguous_word)

        if sense:
            print("Predicted Sense:", sense.name())
            print("Definition:", sense.definition())
            print("Example:", sense.examples())
        else:
            print("No sense found.")


if __name__ == "__main__":
    main()