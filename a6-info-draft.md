# BERT and Attention

## BERT 

### McCormick (2020)

- BERT stands for **Bidirectional Encoder Representations** from **Transformers**
- method of pretraining **language representations** used to create models for NLP practitioners
- two possibilities:
	- can use BERT models to **extract HQ language features**
	- can **fine-tune** these models on a **specific task** with your **own data** to make **good predictions**
- **BERT** gives **context-specific features**. To understand this we need to go to the original BERT paper.

### BERT Paper 

- Current techniques restrict the power of pre-trained representations, esp. for fine-tuning approaches.
- Standard language models are **unidirectional**
	- OpenAI's GPT: authors use a left-to-right architecture, every token can only attend to **previous** tokens in the Transformer's **self-attention** layer
	- these restrictions are bad for sentence level tasks, where you need context from both directions. 

- **Bidirectional Encoder Representations from Transformers** (BERT) alleviates unidirectionality problems using a **masked language model** (MLM), which is a **pre-training objective** based on the **Cloze** task
	- The MLM will randomly **mask** (hide) some of the tokens from the input
	- the pre-training objective: predict the **original vocab id** of the **masked word** based **only on its context**
	- the MLM objective enables the representation to **fuse the left and right context**, unlike the left-to-right pretrainer.
- Also uses a **next sentence prediction** task, jointly trains text-pair representations.

- BERT is the first **fine-tuning based representation model** that gets SOTA performance on both many **sentence-level** and **token-level** tasks

## Attention


- This is the introduction to Attention
- Include Attn. stuff here