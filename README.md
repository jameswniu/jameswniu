# James W. Niu

**Sr. Staff AI/ML Engineer, 10+ years. I build multi-agent systems that ship, and I measure them before I believe them.**

**Built work, with receipts.** Every project below runs, and every claim traces to an eval,
a probe, or a logged run. The receipts that proved me wrong are here too.

A wrong number in a dashboard fails loudly. A generative system fails **plausibly**: a mouth
trailing the audio by four frames, a cited statistic with nothing behind it. Those are
invisible to a type check, obvious to a person, and different again tomorrow. So I capture
human judgment as labels, compile it into thresholds, and wire it into gates that can refuse
to spend.

| If you want | Go to |
| --- | --- |
| One project, read deeply | [The featured harness](#featured-three-hard-problems-in-ai-video---solved-in-one-loop) |
| Range across problems | [The table of six](#six-more-production-ai-on-real-problems) |
| How I work | [Principles I work by](#principles-i-work-by) |

## Featured: Three hard problems in AI video - Solved in one loop

**[autonomous-ads-pipeline-multimodal-evals](https://github.com/jameswniu/autonomous-ads-pipeline-multimodal-evals)**

`7 steps, 4 guards, 10 probes` · `10 of 10 named gating thresholds derived from labelled exemplars` · `48 exemplars graded by hand, 42 calibration scenes` · `28 ad versions across 4 engines` · `10 spec ads for real products`

Three problems the field has not settled, and one loop that does all three. A multi-agent system I run in production shot thirty-eight ads with nobody watching, against metered video engines, and it could only spend when its own checks said yes.

1. It shoots with no director. Boards, prompts, engine calls, re-rolls and delivery ran unattended, and every request landed in an append-only ledger.
2. It grades pixels, audio and timing instead of text, against 48 exemplars I labelled by hand. The grading splits three ways.
   - Process evals check that every step ran and its gate fired before money moved.
   - Outcome evals check that every claim on screen matches the product's own live page.
   - Quality evals score taste against the golden set, re-derived for each audience.
3. It routes each brief to the engine that wins that audience. Four engines shot the same five briefs and no single engine won all five, so the winners table picks per brief, the way Perplexity picks a model per question, here for video.

The evals overruled me, too. Ten scoring models I built were thrown out in one day for disagreeing with the human labels, and a lip-sync check that shipped backwards was caught doubling the error it was built to remove.

## Six more: Production AI on real problems

Ranked by priority, one per repository, nothing listed twice.

| Focus | Project | What it solves | Who benefits |
| --- | --- | --- | --- |
| **Voice AI**<br><code>Speech&#8209;to&#8209;Speech</code> <code>Twilio&nbsp;PSTN</code> <code>WebSocket</code> <code>ElevenLabs</code> <code>LLM&nbsp;Failover</code> <code>Latency&nbsp;SLOs</code> <code>Eval&#8209;Gated&nbsp;CI</code> <code>Observability</code> | [realtime-voice-agent-turn-taking-stack](https://github.com/jameswniu/realtime-voice-agent-turn-taking-stack) | A production voice agent on a real phone number: SLOs met over its lifetime, incidents postmortemed, releases gated by a 61-case suite | Support, scheduling, and anyone shipping voice agents |
| **Reinforcement Learning**<br><code>Multi&#8209;Agent&nbsp;RL</code> <code>PPO</code> <code>PyTorch</code> <code>Gymnasium</code> <code>MAPF</code> <code>FastAPI</code> <code>Docker</code> | [multi-agent-rl-mapf-drone-navigation](https://github.com/jameswniu/multi-agent-rl-mapf-drone-navigation) | Many drones planning conflict free paths at once, in real time | Robotics, drone, and simulation teams |
| **LLM Evaluation**<br><code>Prompt&nbsp;Engineering</code> <code>Llama&nbsp;3.1&nbsp;8B</code> <code>lm&#8209;eval&#8209;harness</code> <code>Ollama</code> <code>Ablation&nbsp;Benchmarks</code> <code>Wilson&nbsp;CI</code> <code>Load&nbsp;Testing</code> | [self-hosted-llm-evals-lab](https://github.com/jameswniu/self-hosted-llm-evals-lab) | Knowing which prompt strategy actually wins, by statistics instead of vibes | ML platform and LLM eval teams |
| **Fine-Tuning**<br><code>DistilBERT</code> <code>Hugging&nbsp;Face</code> <code>PyTorch</code> <code>ONNX&nbsp;int8</code> <code>LLM&#8209;as&#8209;Judge</code> <code>FastAPI</code> <code>Docker</code> | [fine-tuning-turn-detection-model](https://github.com/jameswniu/fine-tuning-turn-detection-model) | Knowing whether the caller is done talking before the agent speaks: 58 ms p95 on CPU, zero false interruptions on a frozen human gold set | Voice AI, conversational AI, and applied ML teams |
| **MCP Servers**<br><code>Model&nbsp;Context&nbsp;Protocol</code> <code>FastMCP</code> <code>OAuth&nbsp;2.1</code> <code>Auth0</code> <code>Self&#8209;Hosted&nbsp;Atlassian</code> <code>Docker</code> <code>Audit&nbsp;Logging</code> | [onprem-prod-bitbucket-atlassian-mcp](https://github.com/jameswniu/onprem-prod-bitbucket-atlassian-mcp) | AI agents that cannot reach self-hosted Bitbucket, Jira, or Confluence | Enterprise platform and developer experience teams |
| **Computer Vision**<br><code>OpenCV</code> <code>CNN</code> <code>PyTorch</code> <code>ONNX&nbsp;int8</code> <code>Image&nbsp;Preprocessing</code> <code>Object&nbsp;Detection</code> <code>FastAPI</code> <code>Docker</code> <code>Human&#8209;in&#8209;the&#8209;Loop</code> <code>Pytest&nbsp;Gates</code> <code>GitHub&nbsp;Actions</code> | [synthetic-image-recognition-cnn-harness](https://github.com/jameswniu/synthetic-image-recognition-cnn-harness) | Reading checkboxes off scanned forms where a misread box becomes a wrong decision, with the uncertain ones queued to a person | Document processing, real estate, and applied computer vision teams |

## Two things I learned by being wrong

1. **Passing tests say nothing about what you never thought to test.** Every check passed while the presenter's dark top vanished into a black background and a floating head shipped, because nobody had written that question down. Now every suite I build carries [a written list of what it does not measure](https://github.com/jameswniu/autonomous-ads-pipeline-multimodal-evals#where-the-claims-stop).
2. **A success message is not a result.** Every agent reported success while the files it handed over were empty, because each one looked for the others at an address that only works on one machine. Now every handoff verifies the address and every file reports its size, so an empty one cannot pass as done.

## Principles I work by

1. **Chat output is not evidence.** The database write, the rendered file, and the logged
   artifact size are the evidence.
2. **Degrade loudly, never silently.** Every fallback is logged; a green checkmark over an
   empty artifact is the worst bug in agentic systems.
3. **Spend where the artifact is judged.** Flagship models on deliverables, fast models on
   hot paths; cost per accepted deliverable beats cost per token.

## Skills

- **Languages:** Python, SQL, TypeScript, JavaScript, Go, Bash
- **Full-stack & web:** React, Node.js, TypeScript, Vite, HTML/CSS, responsive web apps, streaming chat UIs
- **APIs, RPC & streaming:** REST, FastAPI, gRPC, WebSockets, Server-Sent Events (SSE), streaming APIs, webhooks, OAuth 2.1
- **LLMs & agents:** Agentic AI, multi-agent systems in production, LangGraph, LangChain, Model Context Protocol (MCP), tool and function calling, prompt and context engineering, OpenAI API, Anthropic Claude API
- **Search, retrieval & RAG:** RAG, vector search, semantic and hybrid search, embeddings, reranking, approximate nearest neighbor (ANN), vector databases (FAISS, Turbopuffer), relevance engineering
- **NLP:** Information extraction, text classification, semantic matching, thematic and qualitative analysis
- **Evaluation & guardrails:** Evaluation engineering, LLM-as-a-judge, golden datasets, groundedness and hallucination evals, multimodal evals, process, outcome and quality evals, eval-gated CI, guardrails, output validation, prompt-injection testing, PII handling, A/B testing, ablation studies, statistical analysis
- **Observability & tracing:** Langfuse, LangSmith, Datadog, Prometheus, Grafana, distributed tracing, structured logging, metrics and alerting, LLM observability
- **Voice & speech:** Conversational AI, voice AI, ASR, TTS, turn detection, voice cloning (ElevenLabs), Twilio, PSTN telephony
- **Video & creative AI:** Text-to-video and video generation, avatar video (HeyGen), ffmpeg, ad tech, creative testing
- **Machine learning:** PyTorch, deep learning, fine-tuning (Hugging Face, DistilBERT), computer vision (OpenCV, MediaPipe, CNNs), reinforcement learning (multi-agent RL, PPO), ONNX int8 quantization, generative AI
- **Infra & MLOps:** MLOps, LLMOps, Docker, Kubernetes, Helm, CI/CD (GitHub Actions, Harness), AWS (EKS), Azure, self-hosted LLM serving (Ollama), PostgreSQL, Snowflake
- **Models:** Claude (Anthropic), GPT (OpenAI), Llama, Voyage AI

## Open to work

**Sr. Staff / Principal AI engineering: agentic systems, LLM evals, and the guardrails that
make them safe to run unattended.** San Francisco, or remote.

Role titles I map to: Staff AI Engineer, Principal AI Engineer, Applied AI Engineer, Machine Learning Engineer, AI/ML Engineer, Forward Deployed Engineer (FDE).

**The fastest way to evaluate me is to not take my word for it.** No accounts, no API keys,
no GPU. Needs `python3` and `ffmpeg`:

```
git clone https://github.com/jameswniu/autonomous-ads-pipeline-multimodal-evals
cd autonomous-ads-pipeline-multimodal-evals && pip install -r requirements.txt
python3 evals/derive.py
```

It prints every gating threshold in that harness beside the labelled pass and the labelled
reject that bracket it, recomputes the shipped exemplars rather than reciting them, and exits
nonzero if any constant has drifted outside its own evidence.

Hiring, or want the walkthrough:
[LinkedIn](https://www.linkedin.com/in/jameswnarch/) | [jameswnarch@gmail.com](mailto:jameswnarch@gmail.com)