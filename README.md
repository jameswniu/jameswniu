# James W. Niu

**Sr. Staff AI/ML Engineer and Architect, 10+ years. I build multi-agent systems that ship, and I measure them before I believe them.**

Working software with receipts: every project below runs, and the claims in each README are
backed by evals, probes, or logged runs rather than vibes.

## The problem I actually work on

A wrong number in a dashboard fails loudly. A generative system fails **plausibly**. A mouth
trails the audio by four frames. A cited statistic has no source behind it. A gesture lands
just after the word it belonged to. Each one is invisible to a type check, obvious to a
person, and different again in tomorrow's run.

That gap is where most agentic systems quietly break, and it gets worse the moment nobody is
watching. Scheduled jobs, unattended pipelines, and background agents have no human in the
loop to catch a plausible failure, so the only real defense is to capture human judgment
earlier and enforce it at runtime.

That thread runs through everything below. Turn taste into labels, compile labels into
thresholds, and wire thresholds into gates that can refuse to spend money. The evals are not
a report card stapled on at the end. They are the product.

## 1. Featured: AI filmmaking governed by multimodal evals

**[3d-filmmaking-ads-multimodal-evals](https://github.com/jameswniu/3d-filmmaking-ads-multimodal-evals)**

An AI filmmaking pipeline for advertising-grade avatar video: multimodal evals govern a
cloned voice, a consistent generated character, and light-field 3D output. Taste is captured
as labels, compiled into thresholds, and enforced by gates that block bad output before it
spends money. 13 probes, 4 guards, measured vendor costs, and the measurements that falsified
my own claims.

It runs on a schedule, against metered vendor APIs, with nobody awake. That constraint is the
whole design: an unattended pipeline cannot be corrected mid flight, so every gate has to fire
before the credit is spent, and anything that is not a clean success has to page loudly rather
than pass quietly.

## 2 to 6: Production AI on real problems

Ranked by priority. The pinned row below shows six: the three strongest here, plus three not listed above.

| # | Project | What it proves |
| --- | --- | --- |
| 2 | [multi-agent-rl-mapf-drone-navigation](https://github.com/jameswniu/multi-agent-rl-mapf-drone-navigation) | Real-time multi-agent drone flight: PPO reinforcement learning for pathfinding and coordination, served behind a FastAPI backend |
| 3 | [self-hosted-llm-evals-lab](https://github.com/jameswniu/self-hosted-llm-evals-lab) | Systematic prompt ablation on self-hosted Llama via lm-evaluation-harness: baseline vs CoT vs few-shot vs self-consistency, with Wilson confidence intervals |
| 4 | [questions-to-sql-intent-router](https://github.com/jameswniu/questions-to-sql-intent-router) | Plain-English questions routed to document retrieval or to SQL generated from the question and validated before it runs: 100 percent query validation, PII and prompt-injection guardrails |
| 5 | [research_doc_extraction_rag_agent](https://github.com/jameswniu/research_doc_extraction_rag_agent) | Dual-model production pipeline that turns messy survey responses into clean research insights: Claude Opus extracts themes and assigns participants, GPT writes executive summaries, temperatures tuned per stage |
| 6 | [claude-code-in-python-and-prose](https://github.com/jameswniu/claude-code-in-python-and-prose) | Architecture study of an agentic coding CLI, told twice: thirty-four prose chapters on the query loop, tool registry, hooks, sandboxing, and MCP, plus the same shapes expressed in Python |

## Three things I learned by being wrong

**A suite can score everything about a person except whether you can see her.** A generated
presenter was matted onto pure black and dressed in a black top. Her face cleared the
background by 134 levels of luma. Her torso cleared it by 22. The body dissolved, and the
render shipped a floating head. Eleven probes were scoring her face, her motion, and her
timing, and not one of them asked whether she was visible. The fix took a cream top. The
lesson was that a thorough suite can still be blind in exactly the place that matters, so I
now design probes against the failure I have not imagined yet.

**Ten scoring models, built in one day, and every one inverted against the labels.** One
lip-sync metric agreed with the human eye eight times out of eight, went in as a blocking gate
within minutes, then measured six to ten frames of swing against itself inside a single clip
and was demoted the same hour. A brightness bar set to 8.0, because one vendor's output
measured 7.9, turned out to encode "resemble that vendor" and steered six hours of decisions
while gating nothing at all. Measuring your own measurements is not overhead. It is the only
thing standing between a metric and a superstition.

**Three green checkmarks over two empty files.** In a multi-agent system, agents discovered
each other through their published cards and every step reported success. Both artifacts
persisted empty. The cards advertised localhost, which is correct on one machine and wrong
across a container network, so discovery kept succeeding while delivery silently failed. The
client now rebases the address and logs that it did, and every artifact writes its byte size
to the log, so an empty success shows up in one grep. That failure is why the first principle
below is worded the way it is.

## Principles I work by

1. **Chat output is not evidence.** The database write, the rendered file, and the logged
   artifact size are the evidence.
2. **Degrade loudly, never silently.** Every fallback is logged; a green checkmark over an
   empty artifact is the worst bug in agentic systems.
3. **Spend where the artifact is judged.** Flagship models on deliverables, fast models on
   hot paths; cost per accepted deliverable beats cost per token.

## How I work

I write the honest limitations section. Every repository here says what it does not do yet,
because a README that only lists wins tells a reviewer nothing about judgment, and the
limitations are the part a senior engineer actually reads.

I would rather ship a system that degrades in public than one that looks perfect until the
day it does not. Most of what I build runs unattended, which means the interesting engineering
is not the happy path. It is the ladder of fallbacks underneath it, each one logged, each one
cheaper than the last, and none of them pretending.

**What I am looking for:** teams putting agentic or LLM systems into production, where the
hard problems are reliability, evaluation, cost per accepted output, and the failure modes
that only surface at three in the morning with nobody watching. I am glad to own the eval
layer, the orchestration layer, or the argument about which model belongs where.

## Contact

[LinkedIn](https://www.linkedin.com/in/jameswnarch/) | [+1 (917) 355-7504](https://wa.me/19173557504)
