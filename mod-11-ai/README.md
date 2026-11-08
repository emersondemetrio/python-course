# Module 11: AI

In this last module, your programs learn to ask an AI model for help. You will understand what a large language model (LLM) really is, call one from Python, and learn to write prompts that give useful, predictable answers.

The goal is not magic. By the end you will know exactly what the model receives, what it sends back, what it costs, and when a simple `if` is a better choice than AI.

## Files, in order

1. [What is an LLM](what-is-an-llm.md): what these models are, what they are good and bad at, tokens, cost and privacy.
2. [Calling an LLM](calling-an-llm.md): API keys, environment variables and your first call with the Anthropic Python SDK.
3. [Prompts](prompts.md): writing clear prompts, asking for JSON, and choosing between rules and AI.

## Before you start

- You can call an API with `requests` and read JSON (module 10).
- You can install packages in a virtual environment (module 7).
- You know `try` and `except` (module 7) and functions that `return` values (module 3).
- You will need an API key from an AI provider. Your teacher can help you create one. Calls cost a small amount of money per use, so read the cost section in the first file before you start.

## Time estimate

Plan for 3 sessions of about one hour each.

## You are ready for the final project when you can...

- [ ] Explain in your own words what an LLM does and why it can be confidently wrong.
- [ ] Explain what a token is and why a longer prompt costs more.
- [ ] Keep an API key out of your code using an environment variable or a `.env` file.
- [ ] Call an LLM from Python and print its answer.
- [ ] Build a prompt from your own data with a function.
- [ ] Ask the model for JSON and read it safely with `json.loads`.
- [ ] Decide, for a given feature, whether simple rules or an LLM is the better tool.

**Next:** [What is an LLM](what-is-an-llm.md)
