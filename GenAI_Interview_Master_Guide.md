# GenAI Engineering Interview Deep-Dive: Questions & Answers

This guide covers core Generative AI concepts, RAG, Agents, and Production Engineering, designed for high-impact interview preparation.

---

## ⚙️ 1. Core GenAI Understanding (The Must-Answers)

### 1. What problem does #Generative #AI solve that traditional #ML cannot?
Traditional ML is primarily **discriminative**—it excels at classification, regression, and pattern recognition (e.g., "Is this email spam?"). Generative AI learns the underlying distribution of data to **create new samples** (text, images, code). It moves from "what is this?" to "create something like this."

### 2. How does an #LLM generate the next token?
1. **Embedding**: Input text is converted into high-dimensional vectors.
2. **Self-Attention**: The transformer architecture weighs the importance of surrounding tokens to understand context.
3. **Probability Distribution**: The model generates a score for every possible word in its vocabulary.
4. **Sampling**: A token is selected based on these probabilities (influenced by strategies like Top-P, Top-K, or Greedy Search).

### 3. What causes #hallucinations in #LLMs?
*   **Data Noise**: Training on conflicting or incorrect data.
*   **Probabilistic Nature**: The model optimizes for *fluency* (what sounds right) rather than *factuality*.
*   **Knowledge Cutoff**: The model lacks information on events after its training finished.
*   **Over-generalization**: Attempting to force a connection between unrelated concepts.

### 4. Why can’t #LLMs be trusted with factual data by default?
LLMs are statistical prediction engines, not databases. They don't have a concept of "truth." They predict the most likely sequence of tokens, which can result in confident-sounding but entirely fabricated "facts."

### 5. What is the difference between **training**, **#fine-tuning**, and **inference**?
*   **Training (Pre-training)**: Teaching a model from scratch on massive datasets (trillions of tokens). Very expensive.
*   **Fine-tuning**: Taking a pre-trained model and training it further on a smaller, specific dataset (e.g., medical journals) to adapt its style or domain knowledge.
*   **Inference**: The process of using a trained model to generate an output for a specific input.

### 6. Why does temperature affect output quality?
Temperature controls the "randomness." 
*   **Low Temp (0.1 - 0.3)**: Makes the model deterministic; it almost always picks the most likely token (good for code/facts).
*   **High Temp (0.7 - 1.2)**: Flattens the probability curve, allowing less likely tokens to be picked (good for creative writing).

### 7. What are context windows and why do they matter?
The context window is the maximum number of tokens a model can process in one "go" (input + output). If a document or conversation exceeds this limit, the model "forgets" the earliest parts, leading to lost context and errors.

---

## 🛠️ 2. LLM #API & Backend #Engineering

### 8. How do you design an API that safely interacts with an LLM?
*   **Input Sanitization**: Block prompt injection attacks.
*   **Rate Limiting**: Throttling to prevent API budget exhaustion.
*   **PII Filtering**: Ensure users don't send sensitive personal data.
*   **Monitoring**: Tracking latency, token usage, and hallucination rates.

### 9. How do you handle retries and partial failures in LLM calls?
Use **Exponential Backoff** for retries. For batch processing, handle partial failures by returning partial results to the user with "retry" tokens, or use a queue-based system (like Celery or BullMQ) to ensure message persistence.

### 10. How do you protect API keys in production?
Never hardcode them. Use **Secret Managers** (AWS Secrets Manager, GCP Secret Manager, Vault) and rotate them periodically. Use environment variables in transient compute environments.

### 11. How do you manage rate limits from LLM providers?
Implement a **Token Bucket** or **Leaky Bucket** algorithm on the backend. Use a distributed cache like Redis to track usage across multiple server instances and queue requests when limits are hit.

### 12. How do you reduce token usage and cost?
*   **Model Tiering**: Use cheaper models (e.g., GPT-4o-mini) for simple tasks and "expensive" ones only for complex reasoning.
*   **Caching**: Cache common prompt responses in Redis.
*   **Prompt Compression**: Removing redundant words or using "summarized" history.

### 13. What is structured output and why is it important?
Structured output (e.g., JSON mode) forces the LLM to return data in a specific format. It is crucial for **programmatic consumption**, allowing backend code to parse the response (e.g., into a database) without regex or brittle string parsing.

### 14. How do you validate LLM responses before using them?
Use schema validation libraries like **Pydantic (Python)** or **Zod (TS)**. For logic validation, use a second "Judge" LLM to check if the output meets specific criteria.

### 15. How do you stream LLM responses to #frontend?
Use **Server-Sent Events (SSE)**. This allows the server to push chunks of the response as they are generated, improving the user's "time to first token" (perceived speed).

---

## 🧩 3. #Prompt Engineering (#Engineering Perspective)

### 16. Difference between zero-shot, few-shot, and chain-of-thought?
*   **Zero-shot**: "Translate this to French: [text]"
*   **Few-shot**: Giving 2-3 examples of inputs and outputs in the prompt.
*   **CoT**: Explicitly asking the model to "Think step-by-step" to improve logical reasoning.

### 17. Why can prompts be considered contracts?
Because downstream systems depend on the model outputting a specific structure or tone. If you change a prompt, you "break the contract," potentially causing the parser to fail or the UI to render incorrectly.

### 18. How do you version prompts in production?
Treat them like code. Use a **Prompt Management System** (like LangSmith, Portkey, or Git-based registries) to track which version of a prompt was used for every API call.

### 19. When would you prefer prompts over fine-tuning?
Prefer prompts for **90% of use cases**. They are faster to iterate on, cheaper, and often more flexible. Use fine-tuning only when you need very specific *formatting*, *tone*, or *latency* improvements that prompts can't provide.

### 20. How do you debug a failing prompt?
*   **Isolation**: Test individual components of the prompt separately.
*   **Logit Bias Analysis**: Look at which tokens the model almost picked.
*   **Negatives**: Tell the model what it *must not* do.
*   **Simplification**: Reduce the instruction complexity until it works, then add layers back.

---

## 📚 4. #RAG (Retrieval Augmented Generation)

### 21. Why is RAG needed when LLMs are already trained?
RAG allows LLMs to access **outside knowledge** (private docs, recent news) that wasn't in their training data, significantly reducing hallucinations by grounding answers in provided facts.

### 22. Explain the complete #RAG #pipeline end-to-end.
1. **Load**: Import documents.
2. **Chunk**: Break docs into smaller pieces.
3. **Embed**: Turn chunks into vectors.
4. **Store**: Save vectors in a Vector DB.
5. **Retrieve**: Find the most relevant chunks for a user query.
6. **Augment**: Stuff the chunks into the prompt.
7. **Generate**: LLM answers using the provided context.

### 23. How do you decide #chunk size?
It’s a trade-off. 
*   **Small (200-500 tokens)**: High precision, less "noise," but may lose the bigger picture.
*   **Large (1000+ tokens)**: Better context, but context windows might fill up with irrelevant info.

### 24. How do embeddings work?
They convert text into a vector of numbers in a high-dimensional space. "Dog" and "Puppy" will have vectors that are numerically "close" to each other, allowing for semantic search instead of just keyword matching.

### 25. Vector DB vs traditional #DB — why?
Traditional DBs (SQL) search for exact matches (`WHERE name='John'`). Vector DBs search for **similarity** (`FIND words similar to 'happy'`), which is essential for handling unstructured data and semantic meaning.

### 26. How do you reduce hallucinations in RAG?
*   **Strict Prompting**: "Answer only using the provided context. If not found, say I don't know."
*   **Citations**: Force the model to cite the specific chunk ID.
*   **Re-ranking**: Double-check the relevance of retrieved chunks before sending them to the LLM.

### 27. How do you handle stale or outdated documents?
Use **Incremental Indexing**. Track document IDs and timestamps; when a file changes, delete the old embeddings and re-embed the new content.

### 28. How do you secure sensitive data in RAG?
Implement **Metadata Filtering**. Store user IDs/Roles in the metadata of the vector. When querying, only retrieve chunks where `user_role` matches the current user.

### 29. How do you test RAG quality?
Use the **RAGAS** framework or similar, focusing on:
*   **Faithfulness**: Is the answer derived solely from context?
*   **Answer Relevance**: Does it actually address the user's prompt?
*   **Context Precision**: How relevant were the retrieved chunks?

---

## 🧠 5. Advanced RAG (Senior-Level)

### 30. What is Self-RAG?
A framework where the model **critiques itself**. It outputs special tokens to decide if it needs to retrieve information, if the retrieved info is relevant, and if the final answer is actually supported.

### 31. What problem does Corrective RAG (CRAG) solve?
It handles **low-quality retrieval**. If the system detects that the retrieved documents aren't relevant to the query, it triggers an external search (like Google/Tavily) to find better information.

### 32. How does Agentic RAG differ from basic RAG?
Basic RAG is a linear pipeline. **Agentic RAG** provides the LLM with "tools" (Search, SQL, Web) and lets the LLM decide which tool to use, how many times to search, and how to verify the results.

### 33. How do you handle multi-document reasoning?
Use **Multi-Hop Retrieval**. The agent retrieves one set of docs, analyzes them, and then realizes it needs a different set of docs from another source to complete the answer.

### 34. How do you rank retrieved documents?
Use a **Cross-Encoder (Re-ranker)**. Vector search (Bi-encoders) is fast but slightly imprecise. A Re-ranker takes the top 10-20 results and does a deep semantic comparison to re-order them by actual relevance.

### 35. What happens when #retrieval fails?
The system must have a "Fallback." Either tell the user "I couldn't find relevant documents," trigger a broad web search, or route the request to a human operator.

---

## 🤖 6. #Agents & #Agentic #AI

### 36. What is an AI agent?
An AI agent is a system that uses an LLM to **autonomously** reason, plan, and take actions using tools to achieve a complex goal.

### 37. How is an agent different from a chatbot?
*   **Chatbot**: Responsive and usually follows a predefined flow.
*   **Agent**: Proactive and identifies the steps needed to solve a problem (e.g., "Book a flight" involves searching, comparing, and transacting).

### 38. What causes infinite loops in agents?
Usually, a failure in the logic-loop. The agent attempts a tool, gets an error, and instead of correcting, it tries the exact same tool again. This is mitigated by **Max Iteration** limits.

### 39. Stateless vs stateful agents?
*   **Stateless**: Every prompt is a fresh start. No memory.
*   **Stateful**: Maintains a "State" object (history, current variables, previous tool results) throughout the entire workflow.

### 40. How do agents use tools?
Through **Function Calling**. The LLM is given a JSON definition of available tools. It outputs which tool it wants to call and with what arguments. The system executes the code and feeds the result back to the LLM.

### 41. How do you manage agent memory?
*   **Short-term**: Recent conversation history (sliding window).
*   **Long-term**: Storing important facts/preferences in a Vector DB or Graph for retrieval in later sessions.

### 42. When should agents NOT be used?
When the task is **highly deterministic** (if-this-then-that), when **low latency** is required, or when the cost of a mistake is extremely high (e.g., critical medical dosing).

---

## 🔗 7. #LangChain vs #LangGraph (Production Critical)

### 43. Why do LangChain chains fail in complex workflows?
LangChain's standard "Chains" are linear. They struggle with **cycles**, **conditional logic**, and **error recovery**. If a step fails, the whole chain often breaks without a way to "go back."

### 44. How does LangGraph solve agent #orchestration?
It models the workflow as a **Graph** (nodes and edges). This allows for loops (cyclic graphs) and complex branching, giving developers precise control over the state and execution flow.

### 45. What are #nodes, #edges, and state in LangGraph?
*   **Node**: A function or an LLM that performs a task.
*   **Edge**: The connection path between nodes.
*   **State**: A shared object passed between nodes that stores the "memory" of the current execution.

### 46. How do you implement conditional routing?
By defining a function that looks at the current `state` and returns the name of the next node to visit. LangGraph uses this to decide the next edge dynamically.

### 47. How do you prevent cyclic execution?
1.  **Recursion Limit**: Set a maximum number of steps allowed.
2.  **Termination Logic**: Hardcoded conditions in the routing functions to exit if a certain state or counter is reached.

### 48. When would you still use LangChain?
For simple, one-shot pipelines, standard RAG implementation, or when you only need quick integrations with its vast library of 3rd party tool loaders.
