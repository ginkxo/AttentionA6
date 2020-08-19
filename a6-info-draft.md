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
- Improvement on ELMo, whose contextual representation of each token is simply the concatenation of left-to-right and right-to-left representations. Feature-based and not deeply bidirectional.

#### Phases

- Pre-training: model trained on unlabeled data over different pre-training tasks.
- Fine-tuning: BERT model initialized with pretrained params, and all params are fine-tuned via labeled data from downstream tasks
	- each downstream task has **separate fine-tune models** despite all being initialized with same pre-trained params.

#### Model Architecture

- **multi-layer bidirectional Transformer encoder**
	- The Annotated Transformer: http://nlp.seas.harvard.edu/2018/04/03/attention.html
- L (layers, number of Transformer blocks), H (hidden size), A (number of self-attention heads)
- **BERTBase** (L=12, H=768, A=12, Total Params=110M, same size as GPT)
- **BERTLarge** (L=24, H=1024, A=16, Total Params=340M (~ 3x))

#### Input/Output Representations

- To let BERT handle a variety of downstream tasks, the **input representation** can **unambiguously represent both single sentences and sentence pairs**, in a **token sequence**.
	- **sentence** : any contiguous text sequence
	- **sequence** : our actual input token sequence to BERT; can be 1 sentences or 2 sentences packed together (e.g. in Question Answering (Question, Answer) inputs).
- WordPiece embeddings w/ 30,000 token vocab.
- First token of every sequence is always a [CLS] classification token.
- The **final hidden state corresponding to [CLS]** is used as the **aggregate sequence representation for classification tasks**.
- 



## Attention


- This is the introduction to Attention
- Include Attn. stuff here