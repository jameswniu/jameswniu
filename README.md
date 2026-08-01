# James W. Niu

**Sr. Staff AI/ML Engineer, 10+ years. I build multi-agent systems that ship, and I measure them before I believe them.**

Working systems with receipts: every project below runs, and the claims in each README are
backed by evals, probes, or logged runs rather than vibes.

A wrong number in a dashboard fails loudly. A generative system fails **plausibly**: a mouth
trailing the audio by four frames, a cited statistic with nothing behind it. Those are
invisible to a type check, obvious to a person, and different again tomorrow. So I capture
human judgment as labels, compile it into thresholds, and wire it into gates that can refuse
to spend.

| if you want | go to |
| --- | --- |
| one project, read deeply | [the featured pipeline](#1-featured-ai-filmmaking-governed-by-multimodal-evals) |
| range across problems | [the table of five](#2-to-6-production-ai-on-real-problems) |
| how I work | [principles I work by](#principles-i-work-by) |

## 1. Featured: AI filmmaking governed by multimodal evals

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

## 2 to 6: Production AI on real problems

Ranked by priority, one per repository, nothing listed twice.

| # | Project | What it proves |
| --- | --- | --- |
| 2 | [multi-agent-rl-mapf-drone-navigation](https://github.com/jameswniu/multi-agent-rl-mapf-drone-navigation) | Real-time multi-agent drone flight: PPO reinforcement learning for pathfinding and coordination, served behind a FastAPI backend |
| 3 | [self-hosted-llm-evals-lab](https://github.com/jameswniu/self-hosted-llm-evals-lab) | Systematic prompt ablation on self-hosted Llama via lm-evaluation-harness: baseline vs CoT vs few-shot vs self-consistency, with Wilson confidence intervals |
| 4 | [questions-to-sql-intent-router](https://github.com/jameswniu/questions-to-sql-intent-router) | Plain-English questions routed to document retrieval or to SQL generated from the question and validated before it runs: 100 percent query validation, PII and prompt-injection guardrails |
| 5 | [research_doc_extraction_rag_agent](https://github.com/jameswniu/research_doc_extraction_rag_agent) | Dual-model production pipeline that turns messy survey responses into clean research insights: Claude Opus extracts themes and assigns participants, GPT writes executive summaries, temperatures tuned per stage |
| 6 | [onprem-bitbucket-jiraconfluence-mcp](https://github.com/jameswniu/onprem-bitbucket-jiraconfluence-mcp) | Self-hosted Bitbucket, Jira and Confluence have no official MCP server; this is that missing server: 56 token-lean tools over stdio or OAuth, with benchmarks showing where a hand-built MCP beats the official Cloud MCP and raw REST |

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

## Open to work

**Sr. Staff / Principal AI engineering: agentic systems, LLM evals, and the guardrails that
make them safe to run unattended.** San Francisco, or remote.

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