# number bias sim

simulates human number selection with common biases for analysis

![image](./__project_image__/tenor.gif)

---

## 💡 overview

simulates human number selection with common biases and analyses which numbers are "safe" (>= 5 from the mean). i got the idea randomly one day and for some reason decided to simulate instead of just using real-world data, so results may not reflect reality as biases are honestly kind of arbitrary... regardless, it was a fun experiment that i did out of pure curiosity, and i learned new things :)

---

## ⚙️ features

- simulates 100 numbers selected from 1 to 100 inclusive per trial (10000 trials) according to human biases
- identifies "safe" numbers (>= 5 from the mean) in each trial
- computes selection counts, safe counts, and probability of being safe
- generates plots for:
  - frequency of numbers selected vs numbers safe
  - probability of being safe given selection
  - distribution of trial means
- uses moving averages to highlight trends

---

## 🧰 requirements

install with:

```bash
pip install -r requirements.txt
```

---

## 🚀 how to use

```bash
python main.py
```
