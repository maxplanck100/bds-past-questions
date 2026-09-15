# Contributing

This repo is a structured, community-verifiable question bank for BDS
past papers (KU). Contributions are welcome at any stage of the
pipeline described in [`WALKTHROUGH.md`](./WALKTHROUGH.md):

`raw-pdfs → extracted → answers → analysis → appendix`

---

## Ground rules

- **One subject, one file, one PR.** Don't bundle multiple subjects or
  stages into a single pull request — it makes review and rollback
  harder.
- **Don't skip stages.** Answers depend on verified extractions;
  analysis depends on verified answers. Confirm the upstream folder
  exists and is marked verified before building on top of it.
- **Preserve original numbering.** Question numbering (Q1, 1a/1b,
  Group A/B) must match the source paper exactly, across all stages.
- **No AI-generated content merged without human review.** LLM output
  (OCR, answers, analysis) is a first draft, not a final one.

---

## How to contribute

### 1. Adding a new year or subject (raw-pdfs)
- Split the source PDF by subject using iLovePDF or PDFlyer (see
  `WALKTHROUGH.md`, Step 1).
- Place under `raw-pdfs/year-<N>/<subject>.pdf`.
- Open a PR with just the PDF and a one-line note on its source (e.g.,
  "KU BDS 1st Year, scanned copy, 2015–2022").

### 2. OCR extraction
- Use the prompt in [`reusable-query.md`](./reusable-query.md)
  unmodified, one subject per model session.
- Spot-check output against the source PDF before submitting:
  - No merged, duplicated, or dropped questions
  - Year labels correct
  - Genuinely illegible scans marked `[UNCLEAR: ...]`, not guessed
- Submit to `extracted/year-<N>/<subject>.md`.

### 3. Answers
- Only open a PR here once the corresponding `extracted/` file is
  merged and verified.
- Mirror the question numbering exactly — answers must be
  cross-referenceable by number, not by position.
- Cite your source (textbook, lecture note, or reasoning) briefly
  where a question is ambiguous or contested.
- Submit to `answers/year-<N>/<subject>.md`.

### 4. Analysis (topic frequency / prediction)
- Only open a PR here once multiple years of a subject exist under
  `extracted/`.
- State your counting method (exact topic match, keyword grouping,
  etc.) at the top of the file, so others can audit the counts.
- Submit to `analysis/year-<N>/<subject>_top_topics.md`.

### 5. Appendix (cheatsheets)
- Only for topics already flagged in the corresponding `analysis/`
  file.
- Keep cheatsheets short and exam-oriented, not full chapter
  summaries.
- Submit to `appendix/year-<N>/<subject>_cheatsheet.md`.

---

## Note on agentic / computer-use models

If you're working with an agentic model capable of operating a
computer directly (browsing, splitting PDFs, running OCR, and writing
files end-to-end in one session) — such as
[Claude Fable](https://www.anthropic.com/claude/fable) or
[GPT-6 Astra](https://openai.com/index/gpt-6-astra/) — the manual
stage-by-stage workflow above exists mainly to keep *human*
contributions consistent and reviewable. You don't need to replicate
every intermediate manual step yourself — let the model handle PDF
splitting, OCR, and formatting in one pass. What still matters
regardless of how the output was produced:
- The output lands in the correct folder, following the naming
  convention.
- It's spot-checked against the source before a PR is opened.
- It's still reviewed by a human before merge — see the ground rules
  above; this doesn't change based on how efficiently the draft was
  produced.
---

## Review checklist (for maintainers)

- [ ] Correct folder and naming convention followed
- [ ] Matches numbering/structure of its upstream file (if applicable)
- [ ] No unverified stage skipped
- [ ] Disclaimer in README still applies (unverified answers labeled
      as such, no copyrighted textbook content pasted in full)

---

## Reporting errors

If you spot a wrong answer, a miscounted topic, or a missed question,
open an issue rather than editing silently — this keeps a record of
what changed and why, which matters for a study resource other
students rely on.
