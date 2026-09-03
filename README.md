# James W. Niu

**Sr. Staff AI/ML Engineer, 10+ years. I build multi-agent systems that ship, and I measure them before I believe them.**

**Built work, with receipts.** Every project below runs, and every claim traces to an eval,
a probe, or a logged run. The receipts that proved me wrong are here too.

A wrong number in a dashboard fails loudly. A generative system fails **plausibly**: a mouth
trailing the audio by four frames, a cited statistic with nothing behind it. Those are
invisible to a type check, obvious to a person, and different again tomorrow. So I capture
human judgment as labels, compile it into thresholds, and wire it into gates that can refuse
to spend.

| if you want | go to |
| --- | --- |
| one project, read deeply | [the featured pipeline](#featured-ai-filmmaking-governed-by-multimodal-evals) |
| range across problems | [the table of six](#six-more-production-ai-on-real-problems) |
| how I work | [principles I work by](#principles-i-work-by) |

## Featured: AI filmmaking governed by multimodal evals

**[3d-filmmaking-ads-multimodal-evals](https://github.com/jameswniu/3d-filmmaking-ads-multimodal-evals)**

`13 probes` · `16 of 16 gating thresholds derived from labelled exemplars` · `4 guards, 3 of which fail open and say so` · `1 credit per scheduled render` · `77 views per frame`

An AI filmmaking pipeline for advertising-grade avatar video: multimodal evals govern a
cloned voice, a consistent generated character, and light-field 3D output. Taste is
captured as labels, compiled into thresholds, and enforced by gates that block bad output
before it spends money.

It runs on a schedule, against metered vendor APIs, with nobody awake. That is the design
constraint: an unattended pipeline cannot be corrected mid flight, so every gate fires before
the credit is spent, and anything short of a clean success pages loudly instead of passing
quietly.

**The repo publishes the measurements that falsified my own claims**, including two failures
the shipped render still does not pass, and a speedup whose number held while the explanation
I wrote for it turned out to be wrong.

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

**A suite only covers what someone thought to measure.** Eleven probes scored the face, the
motion and the timing in a rendered frame. None asked whether the subject was visible against
the background. A dark top on a black matte separated by 22 levels of luma where the face
separated by 134, so the torso dissolved and the render shipped a floating head. Every probe
passed. The gap was not a bug in any of them; it was a question nobody had written down.

**Three green checkmarks over two empty files.** In a multi-agent system every step reported
success and both artifacts persisted empty. The agent cards advertised localhost, correct on
one machine and wrong across a container network, so discovery kept succeeding while delivery
failed silently. The client now rebases the address and logs that it did, and every artifact
writes its byte size.

## Principles I work by

1. **Chat output is not evidence.** The database write, the rendered file, and the logged
   artifact size are the evidence.
2. **Degrade loudly, never silently.** Every fallback is logged; a green checkmark over an
   empty artifact is the worst bug in agentic systems.
3. **Spend where the artifact is judged.** Flagship models on deliverables, fast models on
   hot paths; cost per accepted deliverable beats cost per token.

## Skills

- **Languages:** Python, TypeScript, JavaScript, Go, SQL, Bash
- **Full-stack & web:** React, Vite, Node.js, HTML/CSS, responsive UIs
- **APIs, RPC & streaming:** FastAPI, REST, gRPC, JSON-RPC, WebSockets, Server-Sent Events (SSE), streaming, webhooks
- **LLMs & agents:** Multi-agent systems, agentic AI, LangGraph, LangChain, Model Context Protocol (MCP), tool design, prompt engineering
- **Search, retrieval & RAG:** RAG, vector search, semantic search, hybrid search, embeddings, reranking, approximate nearest neighbor (ANN), vector databases (Turbopuffer, FAISS), relevance engineering
- **NLP:** Structured extraction, thematic analysis, text classification, semantic matching, qualitative coding
- **Evaluation & guardrails:** LLM-as-a-judge, eval-gated CI, guardrails, ablation studies, statistical analysis
- **Observability & tracing:** Prometheus, Grafana, Langfuse, LangSmith, distributed tracing, structured logging, metrics, alerting
- **Voice & speech:** Conversational AI, voice AI, ASR, TTS, Twilio, PSTN
- **Machine learning:** Reinforcement learning, multi-agent RL, PPO, PyTorch, computer vision, generative AI
- **Infra & MLOps:** MLOps, Docker, Kubernetes, Helm, CI/CD, cloud deployment
- **Models:** Claude (Anthropic), GPT (OpenAI), Llama, Voyage AI

## Open to work

**Sr. Staff / Principal AI engineering: agentic systems, LLM evals, and the guardrails that
make them safe to run unattended.** San Francisco, or remote.

Role titles I map to: Staff AI Engineer, Principal AI Engineer, Applied AI Engineer, Machine Learning Engineer, AI/ML Engineer, Forward Deployed Engineer (FDE).

**The fastest way to evaluate me is to not take my word for it.** No accounts, no API keys,
no GPU. Needs `python3` and `ffmpeg`:

```
git clone https://github.com/jameswniu/3d-filmmaking-ads-multimodal-evals
cd 3d-filmmaking-ads-multimodal-evals && pip install -r requirements.txt
python3 evals/derive.py
```

It prints every gating threshold in that pipeline beside the labelled pass and the labelled
reject that bracket it, recomputes the shipped exemplars rather than reciting them, and exits
nonzero if any constant has drifted outside its own evidence.

Hiring, or want the walkthrough:
[LinkedIn](https://www.linkedin.com/in/jameswnarch/) | [+1 (917) 355-7504](https://wa.me/19173557504)