# Word Sense Disambiguation using Lesk Algorithm

## Project Overview

This project implements **Word Sense Disambiguation (WSD)** using the **Lesk Algorithm**, a classical Natural Language Processing technique used to determine the correct meaning of an ambiguous word based on its context in a sentence.

Many words in natural language have multiple meanings. For example, the word **"bank"** can refer to a financial institution or the side of a river. Word Sense Disambiguation helps identify the correct meaning automatically by analyzing the surrounding words in the sentence.

This project uses **NLTK** and **WordNet**, a large lexical database of English, to determine the most appropriate meaning (sense) of ambiguous words.

---

## Objectives

The main objectives of this project are:

* Understand lexical ambiguity in natural language
* Implement the Lesk algorithm for word sense disambiguation
* Utilize WordNet to retrieve word meanings and examples
* Analyze how context influences the interpretation of words
* Demonstrate a basic Natural Language Processing pipeline

---

## Technologies Used

* Python
* Natural Language Toolkit (NLTK)
* WordNet Lexical Database
* Tokenization Techniques
* Git & GitHub

---

## Key Concepts

### Word Sense Disambiguation (WSD)

Word Sense Disambiguation is the task of determining the correct meaning of a word based on its context within a sentence.

Example:

Sentence 1:

```
I deposited money in the bank.
```

Sentence 2:

```
The fisherman sat on the bank of the river.
```

The word **"bank"** has different meanings depending on the context.

---

### Lesk Algorithm

The **Lesk Algorithm** resolves ambiguity by comparing the words in a sentence with dictionary definitions of possible meanings and selecting the meaning with the highest overlap.

Steps of the algorithm:

1. Tokenize the input sentence
2. Retrieve possible meanings (synsets) from WordNet
3. Compare the context words with definitions
4. Select the sense with the maximum overlap

---

## Project Structure

```
word-sense-disambiguation-lesk
│
├── src
│   └── wsd_lesk.py
│
├── run_wsd.py
├── requirements.txt
└── README.md
```

### Folder Description

**src/**
Contains the core implementation of the Word Sense Disambiguation algorithm.

**run_wsd.py**
Main script used to test the algorithm with example sentences.

**requirements.txt**
Lists Python dependencies required to run the project.

---

## Installation

Clone the repository:

```
git clone https://github.com/srimadhuri18/word-sense-disambiguation-lesk.git
```

Navigate to the project directory:

```
cd word-sense-disambiguation-lesk
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Project

Execute the main script:

```
python run_wsd.py
```

The program will:

1. Tokenize the input sentence
2. Apply the Lesk algorithm
3. Identify the most appropriate meaning of the ambiguous word
4. Display the predicted sense and definition

---

## Example Output

Input Sentence:

```
I deposited money in the bank
```

Output:

```
Predicted Sense: bank.n.09
Definition: a financial institution that accepts deposits and channels the money into lending activities
Example: he cashed a check at the bank
```

Another example:

```
Sentence: The fisherman sat on the bank of the river
Predicted Sense: bank.n.01
Definition: sloping land beside a body of water
```

---

## Skills Demonstrated

This project demonstrates practical experience in:

* Natural Language Processing
* Word Sense Disambiguation
* Context-based semantic analysis
* Python for NLP
* Using lexical databases such as WordNet
* Implementing classic NLP algorithms

---

## Possible Improvements

Future improvements could include:

* Implementing advanced WSD methods using machine learning
* Applying transformer-based models such as BERT for contextual disambiguation
* Creating a web interface for interactive sentence analysis
* Evaluating the algorithm on benchmark NLP datasets

---



