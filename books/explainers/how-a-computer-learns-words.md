# How a Computer Learns Words
*A Simple Story About Large Language Models, with "Or" as Our Guide*

---

## 1. Story Time

Everything starts with a giant pile of words.

To train an AI like ChatGPT, people gather a massive collection of writing from websites, books, articles, games, and even code. Nobody labels which sentences are true, logical, or well-written. It's just a huge set of examples of how humans actually talk and write.

Before you ever type a word into the chat, the AI has seen that word millions of times. But the computer doesn't really see letters the way you do. It turns every bit of text into a sequence of *pieces* that it can handle.

### Sidebar: How We Chop Up the Words (BPE)

Before the AI can put pins on its "meaning map," it needs to decide what counts as a *piece* of text. That's where *Byte Pair Encoding* (BPE) comes in.

You can picture BPE like this:

- Start by splitting everything into single letters.
- Look for the most common pairs of letters that sit next to each other, like "th," "er," "or," "ing."
- When a pair appears a lot, glue it together and treat it as one new piece.
- Keep repeating: find frequent pairs, glue them into bigger pieces, until you have a good set of word-pieces.

These pieces (called *subwords*) might be whole words for common things ("the," "and") or chunks for rarer words ("comput" + "er," "un" + "break" + "able").

The word "or" usually becomes its own piece because it's common. That piece is what the AI will later turn into numbers and learn about.

---

Back to the story. Once BPE has chopped text into pieces, the AI gives each piece a pin on a giant "meaning map." At the start, every pin is placed randomly. The pin for "or" sits in an arbitrary spot, no closer to "and" than to "banana."

The AI's first job is *next-word guessing*. It sees part of a sentence and tries to guess what comes next. For "Do you want cake ___ ice cream?", it might guess "or." At the beginning it's wrong constantly. Each time it guesses, it measures how far off it was, then nudges its internal numbers a tiny bit to do better next time.

This is like a chef tasting soup: too salty, add water; too bland, add spice. The "tasting" is comparing the guess to the right answer. The "tweaking" is adjusting the recipe. Over millions of tastes, the recipe improves—and the pin for "or" migrates across the map toward a neighborhood where it helps the AI make good guesses.

Here's what's interesting: as training proceeds, "or" doesn't just land anywhere useful. It drifts toward *other choice-words*. The pin for "or" ends up near "either," "alternatively," and "whether"—words that show up in similar sentence patterns. Meanwhile, "and" lands in a different neighborhood, near words of combination and addition. The map develops structure because similar contexts pull similar words toward similar locations.

Inside the AI, there's also something like reading with a flashlight in the dark. For each word-piece, the AI shines a "spotlight" on other pieces in the sentence that matter most. When it looks at "or," it learns to shine more light on the words around it that go with choices and contrasts—"either," the options on both sides, words like "instead" or "rather"—and less light on irrelevant words. The flashlight doesn't follow fixed rules; it learns *where* to shine by the same guess-and-adjust process. Different sentences teach it different shining patterns, and over time, patterns that help prediction get reinforced.

After this massive guessing phase, there's a second step called *Reinforcement Learning from Human Feedback* (RLHF). Now people look at the AI's answers and rate them: this one is helpful, that one is confusing, this one is kind, that one is rude. The AI keeps approaches that get good ratings and drops ones that don't.

RLHF mostly shapes *how* the AI talks—its tone, politeness, safety, and formatting. It doesn't fundamentally change what the AI knows about words like "or." The base model already handles "or" correctly in most contexts before RLHF; the fine-tuning teaches the model to be helpful and clear when *offering* choices, not what choices *are*.

By the end of training, when you type "or," the AI pulls up the pin for "or" on its map and runs it through all its learned patterns. It often *sounds* like it understands "or" as a logical choice between things. But it's following patterns in numbers that worked well in the past, not reasoning about logic the way a person does.

---

## 2. Technical Time

Now the same story, aligned with actual architecture.

### Step 0: Tokenization with BPE

Pipeline start: *raw text → BPE tokenizer → token IDs*.

BPE begins with a base alphabet (often bytes or characters). It repeatedly finds the most frequent adjacent symbol pair and merges it into a new symbol, building a vocabulary of subword units. Once trained, the BPE vocabulary and merge rules segment any new text into a sequence of subword tokens.

This gives you a fixed-size *subword vocabulary* (often tens of thousands of tokens) and a way to represent any string as a sequence of known tokens with no true out-of-vocabulary words.

For our running example, "or" is common enough to appear as a single BPE token, corresponding to one embedding row and one token ID.

### Tokens and Embeddings

Next pipeline step: *token IDs → embeddings*.

Each BPE token ID indexes into an *embedding matrix*. The selected row is the token's *embedding vector*—a point in a high-dimensional vector space.

The "meaning map" metaphor corresponds to this vector space. Each word-piece is a point. Nearby points correspond to tokens used in similar contexts. Initially, all embeddings (including "or") are random and are updated via gradient descent during pretraining.

As training proceeds, tokens that appear in similar distributional contexts migrate toward similar regions of embedding space. "Or" ends up geometrically closer to "either," "alternatively," and "whether" than to "and," "plus," or "also." This isn't programmed; it emerges from the statistics of co-occurrence and predictive utility.

### Transformer Layers and Attention

The sequence of embeddings feeds into a stack of *transformer layers*. Each layer contains multi-head self-attention (which computes context-dependent weighted sums of other token representations) and feed-forward networks (which apply learned nonlinear transformations).

Self-attention is the "flashlight." For each position, the model computes queries, keys, and values and uses scaled dot-product attention to produce weights—how much each token should attend to others. The query, key, and value projection matrices are *learned parameters*, updated during training. The flashlight learns where to shine; it doesn't follow fixed rules.

For a phrase like "either A or B," the representation of the "or" token will often attend more strongly to "either," "A," and "B" than to irrelevant tokens, because that pattern minimizes the language-modeling loss. Different models develop different attention patterns for the same token depending on their training data and random initialization.

### Next-Token Prediction, Softmax, and Backpropagation

The pretraining objective is *causal language modeling* (next-token prediction).

Given previous tokens, the model outputs a *logit vector*: one real number for every token in the vocabulary. These raw scores are converted into a probability distribution using *softmax*, a function that exponentiates the scores and normalizes them so they sum to 1. This converts arbitrary scores into probabilities over all possible next tokens.

Training uses *cross-entropy loss* between this softmax distribution and the true next token. If the true token (say, the BPE token for "or") has low probability, the loss is high; if it has high probability, the loss is low.

This is the "chef tasting the soup" moment. Softmax is the conversion from raw scores to probabilities. The cross-entropy comparison against ground truth is the actual taste test. Using *backpropagation*, gradients of the loss are computed with respect to all parameters—flowing backward through the computational graph from loss to output layer to transformer weights to embeddings. *Gradient descent* updates parameters in the direction that reduces loss.

Over billions of updates, the embedding row for "or" moves to a location in vector space that makes "or" useful across many contexts. Attention patterns and deeper representations involving "or" are shaped to support good prediction. No explicit rule for logical disjunction is stored; usage patterns become encoded in network parameters.

### RLHF and Policy Optimization

After pretraining, the base model is fine-tuned with *Reinforcement Learning from Human Feedback* (RLHF):

1. The base model generates multiple candidate completions for prompts.
2. Human labelers rank these completions by quality (helpfulness, harmlessness, clarity).
3. A *reward model* is trained to predict these rankings.
4. The base model, treated as a policy, is updated (commonly with PPO-style reinforcement learning) to maximize this reward.

This is the "comedian and audience" phase: the policy is nudged toward responses the reward model scores highly.

RLHF shapes tone, safety, helpfulness, and response formatting. It doesn't substantially change how the model represents logical connectives. The base model already handles "or" correctly in most contexts before RLHF; fine-tuning adjusts *how the model talks about* things, not *what it knows about* basic syntax and semantics. RLHF teaches the model to be polite and clear when offering choices—not what choices are.

### Inference: Frozen Parameters, Learned Behavior

After fine-tuning, parameters are frozen. The BPE tokenizer is fixed (vocabulary plus merge rules). The embedding matrix is fixed (the "or" row is final). Transformer weights and the final output layer are fixed.

At inference:

1. Input text is tokenized with BPE into subword tokens.
2. Token IDs are mapped to embeddings.
3. Embeddings are processed through transformer layers with self-attention and feed-forward networks.
4. A final linear layer plus softmax yields a probability distribution over the next token.

The model's "logical-looking" behavior with "or" is emergent from BPE defining "or" as a consistent token, its learned embedding location, attention patterns and higher-layer representations, and RLHF-driven preference shaping of output style.

No component explicitly encodes the logic of disjunction as symbolic rules. Logic-like behavior is a statistical side effect of the training pipeline and architecture.

---

## 3. What the Model Doesn't Learn About "Or"

If statistical learning fully recovered logical structure, the model would handle "or" the way a logician does. It doesn't. Here's where the gaps show.

### Exclusive vs. Inclusive Disjunction

In classical logic, "or" is inclusive: "A or B" is true if A is true, if B is true, or if both are true. In everyday speech, "or" is often exclusive: "soup or salad" means pick one, not both.

The model defaults to inclusive-or because that's what minimizes prediction loss across diverse contexts. But it often mishandles constructions where exclusive-or is clearly intended. "You can have either the cake or the ice cream" should preclude having both, but the model doesn't reliably track this. It may offer clarifications like "Would you like both?" when the sentence structure already ruled that out.

### Negation Scope

Consider "not A or B." Does this mean "(not A) or B" or "not (A or B)"? The two readings have different truth conditions. Humans resolve this through context, prosody, and pragmatic inference. The model pattern-matches based on training distribution, which means it often gets the scope wrong when the sentence is ambiguous or when the intended reading is the less frequent one.

### Logical Entailment

A simple inference: "A or B" plus "not A" entails "B." This is disjunctive syllogism, valid in classical logic. The model doesn't reliably execute this inference. It may affirm "B" in easy cases, but it can also hedge, repeat the premises without drawing the conclusion, or get distracted by irrelevant surface features.

This isn't a matter of lacking the pattern—the training data contains countless examples of disjunctive reasoning. The issue is that the model's learned representations don't encode the *structure* of the inference. It recognizes instances but doesn't possess the rule.

### Why This Matters

The model's competence with "or" is real but shallow. It handles ordinary usage well because ordinary usage is well-represented in training. It fails at edge cases, logical inference, and disambiguation because those require structure that statistical learning doesn't reliably extract.

This is the difference between learning to talk about logic and learning logic. The model does the former. Whether any amount of scaling or architectural change could achieve the latter remains an open question.

---

## Sources

The technical details in this piece reflect standard descriptions of transformer architecture and training pipelines as documented in foundational papers and engineering reports:

- Vaswani et al. (2017), "Attention Is All You Need" (transformer architecture, self-attention mechanism)
- Sennrich et al. (2016), "Neural Machine Translation of Rare Words with Subword Units" (BPE tokenization)
- Radford et al. (2019), "Language Models are Unsupervised Multitask Learners" (GPT-2, causal language modeling)
- Ouyang et al. (2022), "Training language models to follow instructions with human feedback" (RLHF, InstructGPT)
