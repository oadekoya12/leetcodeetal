# Deck Game

A Python-based card game simulation where players can create standard playing cards and powerful Joker cards. The game logic is simple: higher-ranked cards beat lower-ranked ones, and Jokers beat all non-Joker cards.

---

## 🎯 Features

- Create standard playing cards (Hearts, Spades, Clubs, Diamonds) with values from A to K  
- Add Joker cards (Red or Black) that beat any non-Joker  
- Compare any two cards to determine the winner  
- Includes 6 predefined unit tests to validate core game logic

---

## ⚙️ Installation & Setup

Ensure you have **Python 3.8+** installed.

Clone the repository and set up your project directory:
```bash
    mkdir deck_game
    cd deck_game
```
Create the necessary files:
``` bash
    touch game.py test_game.py
```
---

## 🚀 Usage

To run the game manually and compare cards:
```bash
    python game.py
```
### 📌 Example Input:

    Spades 3
    Hearts K

### 📤 Output:

    3 of Spades
    K of Hearts
    false

---

## 🧪 Testing

To run the test suite and verify game logic:
```bash
    python -m unittest test_game.py
```
---

## ✅ Test Cases & Expected Outcomes

| Test # | Input                         | Expected Output                            |
|--------|-------------------------------|---------------------------------------------|
| 1      | "Spades 3" "Hearts K"         | 3 of Spades<br>K of Hearts<br>false         |
| 2      | "Clubs J" "Spades A"          | J of Clubs<br>A of Spades<br>true           |
| 3      | "Hearts 10" "Diamonds 10"     | 10 of Hearts<br>10 of Diamonds<br>false     |
| 4      | "Diamonds 5" "Joker Red"      | 5 of Diamonds<br>Red Joker<br>true          |
| 5      | "Joker Red" "Joker Black"     | Red Joker<br>Black Joker<br>false           |
| 6      | "Spades 9" "Hearts 9"         | 9 of Spades<br>9 of Hearts<br>false         |

---

## 📄 License

This project is open source and free to use under the [MIT License](./LICENSE).

---
