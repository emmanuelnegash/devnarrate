# DevNarrate

**AI-powered engineering intelligence system that converts repository changes into structured insights and adaptive narratives.**

DevNarrate is an event-driven, multi-agent AI system that analyzes Git repository changes, extracts architectural and engineering insights, and generates structured knowledge artifacts — including professional narratives such as LinkedIn-ready drafts.

It transforms commits into intelligence.

---

## 🚀 Vision

Modern development teams generate enormous engineering knowledge through commits, pull requests, and architectural decisions — but most of it is never captured in a structured or reusable way.

DevNarrate bridges that gap by:

- Understanding repository changes
- Extracting architectural patterns and trade-offs
- Building longitudinal engineering memory
- Generating adaptive content across audiences
- Creating a structured knowledge layer over source control activity

---

## 🧠 Core Concepts

DevNarrate is built around modern AI engineering principles:

- Event-driven architecture
- Clean Architecture (domain isolation)
- Multi-agent orchestration
- Retrieval-augmented reasoning (RAG)
- Persistent semantic memory
- Evaluation-aware generation
- Asynchronous processing

This is not a simple prompt wrapper — it is a structured AI reasoning system.

---

## 🏗 Architecture Overview

DevNarrate is built as an event-driven, asynchronous AI system that converts repository changes into structured engineering intelligence.

### System Design Diagram

```text
                ┌──────────────────────┐
                │      GitHub Repo     │
                └──────────┬───────────┘
                           │ Push Event
                           ▼
                ┌──────────────────────┐
                │    GitHub Webhook    │
                └──────────┬───────────┘
                           ▼
                ┌──────────────────────┐
                │  Ingestion API       │
                │  (FastAPI)           │
                └──────────┬───────────┘
                           ▼
                ┌──────────────────────┐
                │   Event Store (DB)   │
                └──────────┬───────────┘
                           ▼
                ┌──────────────────────┐
                │   Redis Job Queue    │
                └──────────┬───────────┘
                           ▼
                ┌──────────────────────┐
                │    Worker Process    │
                └──────────┬───────────┘
                           ▼
                ┌──────────────────────┐
                │    Diff Processor    │
                └──────────┬───────────┘
                           ▼
                ┌──────────────────────┐
                │ LangGraph Orchestrator│
                └──────────┬───────────┘
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
 ┌─────────────┐   ┌─────────────┐   ┌────────────────┐
 │ Classifier  │   │  Insight    │   │ Memory (Vector)│
 │   Agent     │   │   Agent     │   │  pgvector      │
 └─────────────┘   └─────────────┘   └────────────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Audience Adapter     │
                └──────────┬───────────┘
                           ▼
                ┌──────────────────────┐
                │ Evaluation Agent     │
                └──────────┬───────────┘
                           ▼
                ┌──────────────────────┐
                │ PostgreSQL Storage   │
                └──────────┬───────────┘
                           ▼
                ┌──────────────────────┐
                │   API / Dashboard    │
                └──────────────────────┘


The architecture emphasizes separation of concerns, scalability, and reliability through a layered design.

### 1. Event Ingestion Layer

Repository push events are received via GitHub webhooks.

The ingestion service (FastAPI):

- Validates webhook signatures
- Extracts commit metadata
- Persists event records
- Enqueues background processing jobs

AI execution is deliberately decoupled from the ingestion layer to ensure responsiveness and fault isolation.

---

### 2. Asynchronous Processing Layer

A Redis-backed job queue manages background tasks.

This layer:

- Isolates AI workloads from API latency
- Enables retry and failure handling
- Supports horizontal scaling
- Prevents webhook timeouts

Workers consume queued jobs and initiate the intelligence pipeline.

---

### 3. Diff Processing Layer

The worker retrieves the full commit diff using the GitHub API and performs structured preprocessing:

- Normalization of diff data
- Filtering of non-semantic changes
- Extraction of impacted modules and metadata
- Construction of a structured `ChangeContext`

This preprocessing ensures the AI system operates on structured, high-signal inputs rather than raw code.

---

### 4. Multi-Agent Orchestration Layer

DevNarrate employs a graph-based agent orchestration engine (LangGraph) to enable structured, multi-step reasoning.

The agent pipeline includes:

- **Classification Agent** — Determines change type and scope.
- **Insight Agent** — Extracts architectural patterns, trade-offs, and scaling implications.
- **Memory Agent** — Retrieves semantically similar historical insights.
- **Adapter Agent** — Transforms structured insight into audience-specific narratives.
- **Evaluation Agent** — Performs quality scoring and optional regeneration.

This design avoids single-prompt generation and instead enforces controlled reasoning stages.

---

### 5. Persistence & Memory Layer

PostgreSQL serves as the primary data store for:

- Commit metadata
- Structured insights
- Generated content
- Evaluation results

Semantic memory is implemented using vector embeddings (pgvector), enabling retrieval-augmented reasoning across historical data.

---

### 6. Output & Interface Layer

Generated artifacts are exposed through API endpoints and dashboard interfaces, supporting review, regeneration, and long-term insight tracking.

---

## Architectural Characteristics

- Event-driven ingestion
- Asynchronous AI execution
- Layered separation of concerns
- Graph-based multi-agent reasoning
- Retrieval-augmented generation (RAG)
- Persistent semantic memory
- Scalable, SaaS-ready foundation




---

## 🤖 Multi-Agent Pipeline

DevNarrate uses a structured agent workflow:

1. **Change Classifier Agent**
   - Identifies change type (feature, refactor, optimization, etc.)

2. **Insight Extraction Agent**
   - Extracts architectural patterns
   - Identifies trade-offs
   - Surfaces scaling implications
   - Derives engineering principles

3. **Memory Retrieval Agent**
   - Retrieves similar past insights
   - Avoids repetition
   - Builds narrative continuity

4. **Audience Adapter Agent**
   - Transforms insights into:
     - LinkedIn professional posts
     - Technical deep dives
     - Internal summaries

5. **Evaluation Agent**
   - Self-critiques generated output
   - Scores clarity and depth
   - Regenerates if below quality threshold

---

## 🧩 Tech Stack

| Layer | Technology |
|--------|------------|
| Backend | Python + FastAPI |
| Agent Orchestration | LangGraph |
| LLM | OpenAI / Anthropic |
| Database | PostgreSQL |
| Vector Memory | pgvector |
| Queue | Redis |
| Deployment | Docker |

---

## 📦 Project Structure

DevNarrate follows Clean Architecture principles:

- `domain/` — Pure business logic
- `application/` — Use cases
- `infrastructure/` — External systems (LLM, DB, GitHub, Queue)
- `interfaces/` — API layer
- `agents/` — Agent definitions

This structure ensures scalability, testability, and infrastructure isolation.

---

## 🎯 Current Phase

Phase 1 — Single-user, single-repo system:

- GitHub webhook integration
- Diff parsing
- Multi-agent reasoning
- Vector memory
- LinkedIn draft generation
- Evaluation loop
- Async processing

Future phases will introduce:

- GitHub App integration
- Multi-tenant SaaS architecture
- Knowledge graph layer
- Engineering analytics dashboard
- Team collaboration features

---

## 🔐 Security & Design Principles

- Webhook signature validation
- Async processing to prevent blocking
- No persistent raw code storage
- Structured memory isolation
- Cost-aware AI execution

---

## 📌 Why DevNarrate Exists

Code tells a story.
DevNarrate ensures that story is understood, structured, and shareable.

---

## 📜 License

MIT License
```
