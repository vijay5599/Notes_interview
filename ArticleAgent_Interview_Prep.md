# ArticleAgent Interview Prep

## Project Explanation

ArticleAgent is an AI-powered content automation platform I built to generate high-quality, SEO-friendly articles at scale. The main goal was to solve common problems with AI writing tools such as weak structure, factual errors, robotic tone, and poor long-form coherence.

On the frontend, I used React.js with Tailwind CSS and Material UI to build a responsive dashboard. Users can configure inputs like tone, industry, target word count, and humanization level. I also built a real-time editor so users can review and refine content easily.

On the backend, I used FastAPI for high-performance async APIs. I used PostgreSQL for storing users, projects, and generated content. Authentication is handled with JWT.

The core strength of the project is the multi-stage AI pipeline.

First, a Planner Agent creates a structured JSON outline for the article. This keeps long-form content organized and ensures all key topics are covered.

Next, a Research Agent gathers supporting information and context. This helps reduce hallucinations and improves factual grounding.

Then, section generation happens in parallel using Python asyncio. Each article section is generated independently, which reduces response time and allows large articles without context window issues.

After that, augmentation agents suggest charts, visuals, infographics, and images to improve engagement.

Finally, a Humanization and Validation layer rewrites the content to sound more natural and checks whether the output matches user instructions like tone, word count, and format.

For model orchestration, I used LiteLLM, which lets the system switch between providers like GPT-4o, Claude, and Gemini based on task needs, cost, or availability.

For monitoring, I integrated Langfuse to track prompts, token usage, latency, failures, and costs.

For deployment, I containerized the full stack using Docker and deployed it on a Linux VM. I also set up GitLab CI/CD pipelines for automated testing and deployment.

This project gave me hands-on experience in scalable backend systems, async processing, multi-model AI orchestration, prompt pipelines, DevOps, and building production-grade AI products.

---

## Challenge Faced and How I Solved It

One challenge I faced while developing ArticleAgent was high article generation time, especially during peak usage hours. Users experienced delays, and sometimes requests timed out, which affected the overall experience.

My goal was to identify the bottlenecks and improve performance on both the backend and frontend so the platform could scale smoothly.

I started by profiling the backend and found that external AI API calls were being handled synchronously, which caused blocking during concurrent traffic. I refactored those services using FastAPI's async/await patterns and improved concurrency handling.

On the frontend, I optimized rendering by lazy loading heavy components like the editor, and used React.memo and useCallback to reduce unnecessary re-renders. I also added skeleton loaders and progress states to improve perceived performance.

As a result, article generation time improved by around 40%, responsiveness became much better under load, and users had a smoother experience.

---

## LiteLLM — How to Explain It in an Interview

### One-Line Answer

LiteLLM is a Python library that acts as a unified interface over multiple LLM providers — GPT-4o, Claude, Gemini — so your code does not need to change when you switch models.

---

### 30-Second Explanation (Say This in the Interview)

> "For model orchestration, I used a library called LiteLLM. It provides a single `completion()` call that works across providers like OpenAI, Anthropic, and Google. I just pass a model name — for example `gpt-4o` or `claude-3-opus` — and LiteLLM handles the API differences underneath. This was useful because different stages of the pipeline had different needs. Some tasks needed Claude's long-context handling, others needed GPT-4o's instruction following. LiteLLM let me route each task to the right model without rewriting integration code every time."

---

### Follow-up Questions & Answers

**Q: Why not just call OpenAI directly?**

> I could have, but hardcoding the OpenAI SDK would have locked me into one provider. LiteLLM gave me flexibility from day one. If GPT-4o had an outage or became too expensive, I could switch to Claude or Gemini just by changing the model name string — no code refactoring needed.

---

**Q: What exactly is LiteLLM?**

> It is a Python library that wraps multiple LLM provider SDKs behind one consistent interface. You call `completion()` with a model name and a messages list — the same format as OpenAI's API — and LiteLLM routes it to the correct provider and handles authentication, request formatting, and response parsing internally.

---

**Q: Did you actually use multiple models or just one?**

> Both. By default most requests went to GPT-4o. But for tasks like long research summaries that exceed GPT-4o's effective context, I routed those to Claude because of its larger context window. LiteLLM made that routing easy to configure without duplicating API integration code for each provider.

---

### Key Point to Remember

Mentioning LiteLLM shows you thought about **provider flexibility**, **cost control**, and **production reliability** — not just "call the AI API and hope it works." That signals senior-level thinking. Keep the explanation short and let the interviewer ask follow-ups.
