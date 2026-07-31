# James W. Niu

**Sr. Staff AI/ML Engineer and Architect, 10+ years. I build multi-agent systems that ship, and I measure them before I believe them.**

Working software with receipts: every project below runs, and the claims in each README are
backed by evals, probes, or logged runs rather than vibes.

## 1. Featured: AI filmmaking governed by multimodal evals

**[3d-filmmaking-ads-multimodal-evals](https://github.com/jameswniu/3d-filmmaking-ads-multimodal-evals)**

An AI filmmaking pipeline for advertising-grade avatar video: multimodal evals govern a
cloned voice, a consistent generated character, and light-field 3D output. Taste is
captured as labels, compiled into thresholds, and enforced by gates that block bad output
before it spends money. 13 probes, 4 guards, measured vendor costs, and the measurements
that falsified my own claims.

## 2 to 6: Production AI on real problems

Ranked by priority. The pinned row below shows six at a glance.

| # | Project | What it proves |
| --- | --- | --- |
| 2 | [research_doc_extraction_rag_agent](https://github.com/jameswniu/research_doc_extraction_rag_agent) | Dual-model production pipeline that turns messy survey responses into clean research insights: Claude Opus extracts themes and assigns participants, GPT writes executive summaries, temperatures tuned per stage |
| 3 | [multi-agent-rl-mapf-drone-navigation](https://github.com/jameswniu/multi-agent-rl-mapf-drone-navigation) | Real-time multi-agent drone flight: PPO reinforcement learning for pathfinding and coordination, served behind a FastAPI backend |
| 4 | [nlp-clinical-trial-eligibility-screening](https://github.com/jameswniu/nlp-clinical-trial-eligibility-screening) | Patient-vs-protocol eligibility screening over structured data and clinical notes: semantic analysis, confidence scoring, Dockerized deployment |
| 5 | [self-hosted-llm-evals-lab](https://github.com/jameswniu/self-hosted-llm-evals-lab) | Systematic prompt ablation on self-hosted Llama via lm-evaluation-harness: baseline vs CoT vs few-shot vs self-consistency, with Wilson confidence intervals |
| 6 | [vector-rerank-candidate-search-pipeline](https://github.com/jameswniu/vector-rerank-candidate-search-pipeline) | Three-stage candidate search over a vector database: Voyage-3 retrieval, hard-criteria filtering, then GPT-4o-mini reranking |
## Principles I work by

1. **Chat output is not evidence.** The database write, the rendered file, and the logged
   artifact size are the evidence.
2. **Degrade loudly, never silently.** Every fallback is logged; a green checkmark over an
   empty artifact is the worst bug in agentic systems.
3. **Spend where the artifact is judged.** Flagship models on deliverables, fast models on
   hot paths; cost per accepted deliverable beats cost per token.

## Contact

[LinkedIn](https://www.linkedin.com/in/jameswnarch/) | [+1 (917) 355-7504](https://wa.me/19173557504)
