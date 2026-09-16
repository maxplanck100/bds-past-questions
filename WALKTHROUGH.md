# Walkthrough: From Raw PDF to Structured Question Bank

This document describes the end-to-end process for turning a scanned,
multi-subject past-paper PDF into a clean, organized Markdown question
bank. Follow these steps in order for every new year or subject added
to this repo.

---

## Step 1 — Split the source PDF by subject

Before sending anything to an LLM, split the combined PDF (e.g., an
83-page scan spanning all subjects) into one file per subject.

**Tools (pick one):**
- [iLovePDF – Split PDF](ilovepdf.com/split_pdf) — preferred
- [PDFlyer](pdflyer.netlify.app/tools/split) — fallback

Split manually by subject boundary (identify page ranges by skimming
headers), not by fixed page count. Save each output as:
`raw-pdfs/year-<N>/<subject>.pdf`

Why split first: sending one 83-page mixed-subject PDF to a model
produces inconsistent segmentation and higher OCR error rates than
sending one clean, single-subject file at a time.

---

## Step 2 — Run OCR extraction

Use the prompt template in [`reusable-query.md`](./reusable-query.md)
with any model (Claude, GPT, Gemini, Qwen, DeepSeek, Kimi, Grok, etc.).
Upload one subject PDF per session — do not batch multiple subjects
into one call.

This step is **extraction only**: OCR, cleanup, and year-wise
segmentation. No analysis, no answers, no cheatsheets. Keeping this
stage narrow avoids the model summarizing instead of transcribing.

Output: one Markdown file per subject → `extracted/year-<N>/<subject>.md`

---

## Step 3 — Verify extraction

Before committing, spot-check the output against the source PDF:
- Every question present, none merged or dropped
- Year labels correct
- `[UNCLEAR]` tags present wherever a scan was genuinely illegible

Commit only after this check passes.

---

## Step 4 — Answers (later stage)

Once extraction is verified across all subjects for a year, assign the
answer-writing task per subject. Output goes to
`answers/year-<N>/<subject>.md`, mirroring the question numbering
exactly so the two files stay cross-referenceable.

---

## Step 5 — Frequency and prediction analysis

Only after questions (and ideally answers) exist for multiple years,
run the analysis pass per subject:

- Top 10 recurring topics, with occurrence counts
- Top 10 topics most likely to reappear, with a confidence % each
- One representative sample question per top topic

Output: `analysis/year-<N>/<subject>_top_topics.md`

This stage depends on Step 2 being done identically across all years —
inconsistent extraction format will corrupt the topic counts.

---

## Step 6 — Cheatsheet appendix

Final stage. For each flagged high-probability topic from Step 5,
produce a short revision cheatsheet.

Output: `appendix/year-<N>/<subject>_cheatsheet.md`

---

## Order matters

Do not skip ahead. Each stage assumes the prior one is complete and
verified:

`raw-pdfs → extracted → answers → analysis → appendix`

Running analysis on unverified extractions, or writing cheatsheets
before topic frequency is established, produces output that has to be
redone once errors surface upstream.
