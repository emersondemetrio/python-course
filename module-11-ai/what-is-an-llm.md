# What is an LLM

> **In one sentence:** A **large language model** (LLM) is a program trained on a huge amount of text that, given some text, predicts what text should come next.

## Why it matters

Tools like Claude and ChatGPT are LLMs. They can summarize, translate, suggest ideas and write code. But they also make mistakes in ways that are very different from normal programs. If you understand what is happening inside, even roughly, you will use them well and know when not to trust them.

## Analogy

Imagine someone who has read millions of books, websites, recipes and conversations, and became extremely good at one game: "continue this text". If you write "The best way to keep basil fresh is", they continue with a very plausible sentence.

Most of the time, the plausible answer is also the correct one, because the books they read were mostly right. But sometimes they continue with something that **sounds** right and is not. They are not lying: they never "looked it up". They just continued the text in the most likely way.

## The idea, step by step

### Predicting the next piece of text

During **training**, the model reads an enormous amount of text and adjusts millions (or billions) of internal numbers so that it gets better at guessing the next word. After training, those numbers are fixed. When you send it a message, it:

1. Reads all the text you sent.
2. Predicts the next small piece of text.
3. Adds that piece to the text and predicts the next one.
4. Repeats until it decides the answer is complete.

That is why answers appear word by word in chat apps: the model really is producing them one piece at a time.

Here is a very tiny "language model" in plain Python. It counts which word comes after each word in some sentences, and then always picks the most common next word. Real LLMs are vastly more sophisticated, but the core idea (learn from text, predict what comes next) is the same:

```python
text = "the cat sat on the mat the cat ate the fish the cat sat on the sofa"
words = text.split()

next_words = {}
for i in range(len(words) - 1):
    current = words[i]
    following = words[i + 1]
    if current not in next_words:
        next_words[current] = {}
    next_words[current][following] = next_words[current].get(following, 0) + 1

print(next_words["the"])
print(next_words["cat"])

def most_likely_after(word):
    options = next_words[word]
    return max(options, key=options.get)

sentence = ["the"]
for _ in range(4):
    sentence.append(most_likely_after(sentence[-1]))
print(" ".join(sentence))
```

Output:

```text
{'cat': 3, 'mat': 1, 'fish': 1, 'sofa': 1}
{'sat': 2, 'ate': 1}
the cat sat on the
```

It never "understood" cats. It only learned that "cat" often comes after "the". An LLM learns much richer patterns (grammar, facts, styles, reasoning steps), but it is still learning patterns from text.

### Tokens: how the model sees text

Models do not read letters or whole words. They read **tokens**: small chunks of text. A token can be a whole short word (`cat`), part of a longer word (`un` + `believ` + `able`), a space or a punctuation mark.

A rough rule for English: **1 token is about 4 characters, or about three quarters of a word**. Portuguese and other languages often use a few more tokens for the same idea.

Tokens matter for two reasons:

- **Cost:** providers charge per token, both for what you send (input) and for what the model writes (output).
- **Limits:** each model can only handle a certain number of tokens at once, called the **context window**. It is large (often hundreds of thousands of tokens), but not infinite.

You can make a rough estimate with Python:

```python
def estimate_tokens(text):
    return round(len(text) / 4)

prompt = "Suggest three easy dinner recipes using rice, eggs and spinach."
print(len(prompt), "characters")
print("About", estimate_tokens(prompt), "tokens")
```

Output:

```text
63 characters
About 16 tokens
```

This is only an estimate. The provider's dashboard shows the exact count for every call.

### What LLMs are good at

- Writing and rewriting text: summaries, emails, simpler explanations.
- Turning messy text into structure: "here is a note, give me the date, the name and the amount as JSON".
- Generating ideas and suggestions.
- Explaining things, including code and error messages.
- Translating between languages.

### What LLMs are bad at

- **Exact facts they were not given.** They may invent names, dates, links or book titles. This is called a **hallucination**: a confident answer that is false.
- **Exact math on big numbers.** They predict text that looks like a result. For math, use Python.
- **Recent events.** The model only knows what was in its training text, which stops at a certain date (its **knowledge cutoff**).
- **Being the same every time.** The same question can get slightly different answers. Programs usually need predictable behavior.

The practical rule: **use the model for language and ideas, use normal code for facts, math and rules.**

### It does not know your data

The model has never seen your files, your database or your notes. If you ask "which of my plants need water?", it cannot know. You must **send the data inside the message**, for example: "Here are my plants and when I last watered each one: ... Which ones need water?"

This is the most important idea for the rest of this module: your Python program reads your data, turns it into text, and puts it in the prompt.

### It does not remember between calls

Each API call is independent. The model does not remember your previous call unless you send the previous messages again. Chat apps look like they remember because they resend the whole conversation every time (which is also why long conversations cost more).

### Cost

Providers publish a price per **million tokens**, with input usually cheaper than output. Small, fast models are much cheaper than large ones. As an example with made-up but realistic numbers:

```python
price_input_per_million = 1.00   # dollars
price_output_per_million = 5.00  # dollars

input_tokens = 800
output_tokens = 300

cost = (input_tokens / 1_000_000) * price_input_per_million + (output_tokens / 1_000_000) * price_output_per_million
print(f"One call: ${cost:.4f}")
print(f"1000 calls: ${cost * 1000:.2f}")
```

Output:

```text
One call: $0.0023
1000 calls: $2.30
```

One call is almost free. A loop that calls the model thousands of times is not. Always check the current prices on your provider's website, and set a spending limit in your account.

### Privacy

Whatever you put in a prompt is sent to the provider's servers. Before sending data, ask:

- Is this personal information about someone (names, phone numbers, health, money)?
- Would the owner of this data be comfortable with it leaving my computer?

Send only what the model needs. Read your provider's data policy. Never send passwords or API keys in a prompt.

## Common mistakes

### Trusting a fact without checking

If an answer includes a specific fact (a date, a price, a quote, a link), treat it as a **suggestion to verify**, not as truth. Ask for sources and check them yourself.

### Asking the model to do math your program can do

<!-- no-verify -->
```python
prompt = "What is the total of 1847.35 + 922.10 + 3310.75?"
```

The model might get it right, or might not. Python always gets it right, for free:

```python
print(round(1847.35 + 922.10 + 3310.75, 2))
```

Output:

```text
6080.2
```

### Expecting it to know your data

Asking "what did I buy last week?" will get an invented answer or a polite "I don't know". Send the data in the prompt.

## Exercises

### Predict the output

#### Exercise 1: Counting next words

Using the tiny model idea from this file, what does this print?

<!-- no-verify -->
```python
words = "I like tea I like coffee I love tea".split()

after_i = {}
for i in range(len(words) - 1):
    if words[i] == "I":
        nxt = words[i + 1]
        after_i[nxt] = after_i.get(nxt, 0) + 1

print(after_i)
```

<details>
<summary>Show answer</summary>

```python
words = "I like tea I like coffee I love tea".split()

after_i = {}
for i in range(len(words) - 1):
    if words[i] == "I":
        nxt = words[i + 1]
        after_i[nxt] = after_i.get(nxt, 0) + 1

print(after_i)
```

Output:

```text
{'like': 2, 'love': 1}
```

After "I", the word "like" appears twice and "love" once. A model trained on this text would most often continue "I" with "like".

</details>

### Fix the bug

#### Exercise 2: The wrong job for AI

A program needs to know whether an order of 3 items at 12.50 each is above 30. The current code sends the question to an LLM. Rewrite it so it does not need AI at all.

<!-- no-verify -->
```python
prompt = "An order has 3 items at 12.50 each. Is the total above 30? Answer yes or no."
answer = ask_llm(prompt)
```

<details>
<summary>Show answer</summary>

```python
quantity = 3
price = 12.50
total = quantity * price

if total > 30:
    print(f"Yes, the total is {total}")
else:
    print(f"No, the total is {total}")
```

Output:

```text
Yes, the total is 37.5
```

Math and fixed rules belong in normal code: it is exact, instant and free.

</details>

### Write it

#### Exercise 3: Cost calculator

Write a function `call_cost(input_tokens, output_tokens, input_price, output_price)` where the prices are in dollars per million tokens. It returns the cost of one call. Print the cost of a call with 2000 input tokens and 500 output tokens, with prices 1.00 and 5.00, formatted with 4 decimal places.

<details>
<summary>Show answer</summary>

```python
def call_cost(input_tokens, output_tokens, input_price, output_price):
    return input_tokens / 1_000_000 * input_price + output_tokens / 1_000_000 * output_price

cost = call_cost(2000, 500, 1.00, 5.00)
print(f"${cost:.4f}")
```

Output:

```text
$0.0045
```

The underscore in `1_000_000` is just to make the number easier to read. Python ignores it.

</details>

#### Exercise 4: Rules or AI?

For each feature, decide: plain Python rules, or an LLM? Write your reason in one sentence.

1. Warn when a plant has not been watered for more than 7 days.
2. Write a friendly birthday message for a customer.
3. Calculate the total of a shopping list.
4. Turn a messy note ("dinner w/ Ana fri 8pm at Lume") into a calendar event with date, time and place.
5. Sort books by publication year.

<details>
<summary>Show answer</summary>

1. **Rules.** It is a fixed comparison of dates, exact and free.
2. **LLM.** Creative, varied text is what models do well.
3. **Rules.** It is math.
4. **LLM.** Messy human language into structure is a great use, but check the result before saving it.
5. **Rules.** Sorting is exact; Python's `sorted` does it perfectly.

</details>

## Review

#### Review 1: Most common item (module 6)

Write a function `most_common(items)` that returns the item that appears most often in a list. (You saw a trick for this in this file.)

<details>
<summary>Show answer</summary>

```python
def most_common(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return max(counts, key=counts.get)

print(most_common(["tea", "coffee", "tea", "water", "tea"]))
```

Output:

```text
tea
```

`max(counts, key=counts.get)` looks at every key and picks the one with the biggest value.

</details>

#### Review 2: Formatting money (module 1)

Print `Total: $6.50` using an f-string, from the variable `total = 6.5`.

<details>
<summary>Show answer</summary>

```python
total = 6.5
print(f"Total: ${total:.2f}")
```

Output:

```text
Total: $6.50
```

`:.2f` means "show as a decimal number with 2 digits after the point".

</details>

## Recap

- An LLM is trained on lots of text and produces answers by predicting the next piece of text, one piece at a time.
- It reads and writes **tokens** (about 4 characters each in English); you pay per token.
- It can **hallucinate**: sound sure and be wrong. Check facts, and use normal code for math and rules.
- It does not know your data and does not remember previous calls: send what it needs in each prompt.
- Everything in a prompt leaves your computer. Send only what is necessary.

**Next:** [Calling an LLM](calling-an-llm.md)
