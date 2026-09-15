# Reusable Query: OCR Extraction Prompt

Copy this prompt as-is when uploading a per-subject past-paper PDF to
any model (Claude, GPT, Gemini, Qwen, DeepSeek, Kimi, Grok, etc.).
Upload one subject at a time.

---

I'm uploading a scanned PDF of BDS 1st Year past question papers (KU,
Bachelor level) for **[SUBJECT NAME]**, spanning available years from
2015 onward, including older papers where available. 
Extract and organize every question from every available year 
without missing, skipping, merging, or omitting any paper or question.

**Task — OCR and extraction only, no analysis yet:**

1. OCR the full PDF into clean, accurate text.
2. Strip headers, footers, page numbers, and scan artifacts; correct
   OCR misreads.
3. Segment the text into individual, standalone questions, preserving
   original numbering (Q1, 1a/1b, Group A/B) where present.
4. Organize by year, most recent first.
5. Output as a single Markdown file: `## <Year>` headers, numbered
   questions underneath, verbatim.

Extract everything — do not summarize, paraphrase, or skip questions.
If a scan is illegible, flag it with `[UNCLEAR: <best guess>]` rather
than guessing silently. Deliver only the `.md` file for this pass.

*(Appendix cheatsheets and high-probability/repeat-question analysis
are separate follow-up tasks — not part of this request.)*
