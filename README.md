# 🐱 Hidden Bias Steganography

> *"What if a neural network was secretly whispering something to you this whole time?"*

This project started specifically as a CTF challenge, then ended up becoming a full experiment. I'm just a cat, no degree — just playing with curiosity.

Hide secret messages **inside a neural network's bias values**. The model still runs perfectly... but it's carrying a hidden message no one can see just by looking at it. nyaa~

![Status](https://img.shields.io/badge/status-ongoing-yellow)
![Python](https://img.shields.io/badge/python-3.x-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)

---

## 🐾 What Even Is This?

This project is about two ideas mashed together:

**Steganography** — hiding a secret message inside something that looks totally normal. Like writing in invisible ink, or hiding a note inside a regular-looking book.

**Neural Networks** — programs that learn from data. They're made of layers of tiny math units called **neurons**. Each neuron has two types of numbers:
- **Weights** — control how strongly it listens to each input
- **Biases** — a small personal offset that helps it make decisions

Nobody usually looks at the raw bias values directly. So what if we *replaced them* with our secret message?

That's exactly what this does. 🐱

---

## 🔑 How It Works

### Encoding — Hiding the Message

```
Secret message:  "Cats are cute"
                      ↓
Convert each character to its ASCII number
                      ↓
C=67  a=97  t=116  s=115  ' '=32  a=97  r=114  e=101 ...
                      ↓
Replace the bias values of the neural network with these numbers
                      ↓
Save the model  →  model_with_hidden_message.h5
```

The model file looks completely normal from the outside. It still has the same structure, same layer names, and the weights are untouched. Only the biases changed — and they changed to numbers that *happen* to spell out a message.

### Decoding — Finding the Message

```
Load the model
      ↓
Read the bias values from all Dense layers
      ↓
Round each value to the nearest integer
      ↓
Keep only values in range 0–255 (valid ASCII range)
      ↓
Convert each number back to a character
      ↓
Read the secret! 🐾
```

### Why Does float32 Work Here?

Neural network weights are stored as `float32` numbers (decimals like `0.023` or `-1.47`). But small integers like `67` (letter 'C') are represented **exactly** in float32 — no precision lost. So when we save `67.0` into a bias and load it back, we get `67.0` back. Round it → `67` → `chr(67)` → `'C'`. Perfect recovery every time.

---

## 🎯 Use Cases

### 1. CTF (Capture The Flag) Challenges

Give someone a `.h5` model file as a challenge. They have to figure out that the secret flag is hidden inside the bias values. The model is the puzzle!

The old version (`code/`) has an example with a real CTF-style flag:
```
halal{AI41AI_fjuwdh9f83_P41}
```
...repeated and packed into 513 bias neurons across all layers of a food classifier model. nyaa~

### 2. Neural Network Watermarking

Want to prove an AI model is yours if someone steals it? Before releasing your model, embed your name, a unique ID, or a signature into the bias values. If someone copies your model and claims it's theirs, you can prove ownership by reading back the hidden watermark.

This is a real research direction — sometimes called **model fingerprinting**.

---

## 📁 Project Structure

```
HiddenBiasSteganography/
│
├── code/
│   ├── make.ipynb          ← Old version: embed a CTF flag into a food classifier
│   ├── solve.ipynb         ← Old version: extract and decode the hidden flag
│   ├── test.py             ← Quick script to inspect all bias values in a model
│   │
│   └── new/
│       ├── make.ipynb      ← New version: clean encoder (recommended to start here!)
│       └── solve.ipynb     ← New version: clean decoder
│
├── FormalDocumentation/
│   ├── HiddenBiasSteganography.ipynb  ← Full documented notebook (start here for research!)
│   └── Model/
│       └── model_with_hidden_message.h5  ← Generated when you run the notebook
│
├── model/
│   ├── model_makanan.h5              ← Original food classifier model
│   └── model_with_hidden_message.h5  ← Model with "Cats are cute" embedded
├── TODO.md                                                     ← Research to-do list
└── README.md
```

---

## 🛠️ Requirements

```bash
pip install tensorflow numpy
```

- Python 3.8+
- TensorFlow 2.x
- NumPy

---

## 🚀 Quick Start

**Recommended:** Open `FormalDocumentation/HiddenBiasSteganography.ipynb` — it has the full pipeline (train → encode → save → decode) in one place with explanations at every step.

If you just want the bare code, use `code/new/`:

### Step 1 — Encode a message

Open `code/new/make.ipynb`. Change the message on this line:

```python
message = "Cats are cute"   # ← your secret goes here!
```

Run all cells. It will:
1. Train a simple neural network (student grade predictor — dummy data)
2. Replace the first `len(message)` bias values in the hidden layer with ASCII codes
3. Save the model as `model_with_hidden_message.h5`

```
✅ Model saved as 'model_with_hidden_message.h5'
Secret message: 'Cats are cute' → ASCII: [67, 97, 116, 115, 32, 97, 114, 101, 32, 99, 117, 116, 101]
```

### Step 2 — Decode the message

Open `code/new/solve.ipynb` and run all cells.

```
🔓 Extracted message: 'Cats are cute'
```

---

## 📏 Capacity — How Long Can the Message Be?

The message length is limited by the number of neurons in the hidden layer (each neuron holds one character in its bias).

| Hidden Layer Size | Max Message Length |
|---|---|
| `Dense(13)` | 13 characters |
| `Dense(64)` | 64 characters |
| `Dense(128)` | 128 characters |
| `Dense(512)` | 512 characters |

**Need more space?** Spread the message across multiple layers! The old version (`code/make.ipynb`) shows how to fill 513 biases across all 6 Dense layers of a deeper model.

---

## ⚠️ Limitations (Being Honest nyaa~)

- **It's obvious if you look directly.** The bias values are completely replaced with integers like `67`, `97`, `116`... A careful reverse-engineer inspecting the model would notice these aren't normal trained bias values (which are usually small decimals, not round integers).

- **Accuracy changes.** We're overwriting the *learned* bias values, so the model's prediction accuracy will be different after embedding. For CTF this is fine — you design the model for hiding, not performance. For real watermarking on a model you depend on, this needs a more careful approach.

- **Keras/TensorFlow `.h5` only (for now).** PyTorch or ONNX models would need their own implementation.

- **No encryption.** The message is just raw ASCII. Anyone who knows to check the biases can read it. Adding encryption on top of this would make it much more secure.

---

## 🔭 Future Work

- [ ] Test on diverse image classification datasets
- [ ] Compare with float32 LSB steganography — encode into the mantissa bits of weights instead of full replacement (subtler, statistically harder to detect)
- [ ] Review training-time watermarking (Uchida et al.) as a proper baseline comparison for the fingerprinting use case
- [ ] Add optional encryption layer before embedding
- [ ] Support PyTorch `.pt`/`.pth` checkpoint format
- [ ] Write formal paper draft (expand experiments + results + conclusion)
- [ ] Submit to arXiv or IEEE student conference?

---

## 📄 Research Paper (Draft)

[Embedding Data inside Neural Network Bias Model: A Steganographic Approach Using Keras Models](https://docs.google.com/document/d/1vsu8nVY4sbXoxn7RPkzEEE4EDIov3tByuHGk2LePxNg/edit?tab=t.0)

*(I don't know how to write a paper nyaa~ 😭)*

---

## 🐱 About

Made by a cat-boy researcher who thinks neural networks deserve to have secrets too.

```
  /\_____/\
 (  ^ ω ^  )   ₊˚ "psst... check the biases"
  >  🐾  <
```

> *"The best hiding spot is somewhere nobody thinks to look."*
