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
| **Voice AI**<br><code>Speech&#8209;to&#8209;Speech</code> <code>Twilio&nbsp;PSTN</code> <code>Latency&nbsp;SLOs</code> <code>Eval&#8209;Gated&nbsp;CI</code> <code>Observability</code> | [realtime-voice-agent-turn-taking-stack](https://github.com/jameswniu/realtime-voice-agent-turn-taking-stack) | A production voice agent on a real phone number: SLOs met over its lifetime, incidents postmortemed, releases gated by a 61-case suite | Support, scheduling, and anyone shipping voice agents |
| **Reinforcement Learning**<br><code>Multi&#8209;Agent&nbsp;RL</code> <code>PPO</code> <code>PyTorch</code> <code>FastAPI</code> | [multi-agent-rl-mapf-drone-navigation](https://github.com/jameswniu/multi-agent-rl-mapf-drone-navigation) | Many drones planning conflict free paths at once, in real time | Robotics, drone, and simulation teams |
| **LLM Evaluation**<br><code>Prompt&nbsp;Engineering</code> <code>Self&#8209;Hosted&nbsp;Llama</code> <code>Ablation&nbsp;Benchmarks</code> <code>Statistical&nbsp;Analysis</code> | [self-hosted-llm-evals-lab](https://github.com/jameswniu/self-hosted-llm-evals-lab) | Knowing which prompt strategy actually wins, by statistics instead of vibes | ML platform and LLM eval teams |
| **Qualitative Research**<br><code>Thematic&nbsp;Analysis</code> <code>Claude&nbsp;+&nbsp;GPT&nbsp;APIs</code> <code>Codebook&#8209;Free&nbsp;Coding</code> <code>Quote&nbsp;Verification</code> | [customer-survey-qualitative-thematic-analysis](https://github.com/jameswniu/customer-survey-qualitative-thematic-analysis) | Thousands of open ended survey answers nobody has time to read | Research, insights, and product teams |
| **MCP Servers**<br><code>Model&nbsp;Context&nbsp;Protocol</code> <code>Tool&nbsp;Design</code> <code>OAuth&nbsp;2.1</code> <code>Self&#8209;Hosted&nbsp;Atlassian</code> | [onprem-prod-bitbucket-atlassian-mcp](https://github.com/jameswniu/onprem-prod-bitbucket-atlassian-mcp) | AI agents that cannot reach self-hosted Bitbucket, Jira, or Confluence | Enterprise platform and developer experience teams |
| **Clinical NLP**<br><code>Structured&nbsp;Extraction</code> <code>Golden&#8209;Dataset&nbsp;Evals</code> <code>Semantic&nbsp;Matching</code> <code>Abstention</code> <code>Eval&#8209;Gated&nbsp;CI</code> | [nlp-clinical-trial-eligibility-screening](https://github.com/jameswniu/nlp-clinical-trial-eligibility-screening) | Screening patients against trial protocols with evidence-cited verdicts that abstain instead of guessing | Clinical research, health data, and applied NLP teams |

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

- **Languages:** Python, TypeScript, Go, SQL, Bash, JavaScript
- **LLMs & agents:** Multi-agent systems, agentic AI, LLM orchestration, LangGraph, Model Context Protocol (MCP), MCP servers, agent-to-agent (A2A), tool design and function calling, retrieval-augmented generation (RAG), prompt engineering
- **LLM evaluation & guardrails:** LLM evaluation, LLM-as-a-judge, eval-gated CI, guardrails, ablation studies, golden-dataset benchmarks, regression testing, determinism checks, load testing, self-consistency, chain-of-thought, statistical analysis (Wilson confidence intervals), reproducibility
- **Natural language processing:** NLP, structured extraction, text classification, text clustering, semantic matching, thematic analysis, qualitative coding, abstention
- **Information retrieval & search:** Information retrieval (IR), vector search, semantic search, embeddings, reranking, approximate nearest neighbor (ANN) search, vector databases (Turbopuffer, FAISS), relevance engineering
- **Voice & speech:** Conversational AI, voice AI, real-time speech-to-speech, automatic speech recognition (ASR), text-to-speech (TTS), turn-taking, voice cloning, Twilio, PSTN, WebSocket, ElevenLabs
- **Reinforcement learning & robotics:** Reinforcement learning (RL), multi-agent RL (MARL), Proximal Policy Optimization (PPO), PyTorch, multi-agent path finding (MAPF), path planning, swarm robotics, UAV and drones, Gymnasium
- **Computer vision & generative media:** Computer vision, multimodal AI, monocular depth estimation, background matting, light-field 3D, text-to-video, video generation, generative AI
- **MLOps & platform:** MLOps, FastAPI, Docker, Kubernetes, Helm, CI/CD, GitHub Actions, Cloudflare Workers, Prometheus and Grafana, observability, pytest
- **Security & integrations:** OAuth 2.1, Auth0, JWT, audit logging, Atlassian (Bitbucket, Jira, Confluence), WhatsApp, REST and webhook APIs
- **Data & privacy:** PII redaction, prompt-injection defense, synthetic data, data privacy, AI safety, reproducible research
- **Models & APIs:** Claude (Anthropic), GPT (OpenAI), GPT-4o-mini, Llama, Ollama, Voyage AI, ElevenLabs, sentence-transformers

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