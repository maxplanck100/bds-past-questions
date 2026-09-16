# BDS 1st Year — Biochemistry: Topic Frequency & Exam Prediction Analysis

Based on 11 available Kathmandu University BDS I Biochemistry papers (2015–2021),
extracted in `extracted/year-1/biochemistry.md`. Counting method: each **topic** is
counted once per **paper** in which it appears (regardless of how many sub-questions
within that paper touch it), so a topic's count is out of 11 possible papers.
Confidence percentages for future-exam prediction are qualitative estimates derived
from historical frequency plus a recency weighting (heavier weight given to the five
most recent papers: Oct/Nov 2021, Aug/Sep 2021, Mar/Apr 2021, Feb/Mar 2020, Dec
2018/Jan 2019) — they are informed pattern-based estimates, not statistical
guarantees, and should not replace full syllabus coverage.

---

## Top 10 Recurring Topics (by historical frequency, 2015–2021)

| Rank | Topic | Papers appeared in | Frequency |
|------|-------|---------------------|-----------|
| 1 | Oxidative Phosphorylation / ETC / Chemiosmotic Theory | 10 of 11 | 91% |
| 2 | Lipoprotein Metabolism (chylomicron, VLDL, LDL, HDL, atherosclerosis) | 9 of 11 | 82% |
| 3 | Enzyme Kinetics & Inhibition (coenzyme, isoenzyme, Km, competitive/non-competitive) | 9 of 11 | 82% |
| 4 | Iron Metabolism (absorption, transport, storage, hepcidin, deficiency) | 7 of 11 | 64% |
| 5 | Free Radicals & Antioxidants | 7 of 11 | 64% |
| 6 | Protein Structure (primary–quaternary organisation) | 7 of 11 | 64% |
| 7 | Neurotransmitters & Catecholamine Synthesis | 7 of 11 | 64% |
| 8 | TCA (Krebs) Cycle | 6 of 11 | 55% |
| 9 | Cardiac Markers | 6 of 11 | 55% |
| 10 | Heme Synthesis & Porphyria | 6 of 11 | 55% |

**Just outside the top 10:** Ketone Bodies (5/11), Carbohydrate Classification (5/11),
Lipids/Phospholipids general (5/11), Glycolysis steps/RBC (5/11), Hemoglobinopathies —
sickle cell & thalassemia (4/11), Vitamins (4/11).

---

## Top 10 Topics Most Likely for the Next Exam (with confidence %)

Ranked by combining overall frequency with presence in the most recent papers.

| Rank | Topic | Confidence | Basis |
|------|-------|-----------|-------|
| 1 | Oxidative Phosphorylation / ETC / Chemiosmotic Theory | **90%** | Present in 4 of last 5 papers; historically the single most consistent topic (10/11 overall) |
| 2 | Ketone Bodies (synthesis, utilisation, triggering conditions) | **85%** | Present in 4 of last 5 papers; rising presence in 2018–2021 set |
| 3 | Glycolysis (irreversible steps, RBC-specific, rate-limiting enzymes) | **85%** | Present in 4 of last 5 papers; a near-guaranteed Section B short-note or main question |
| 4 | Lipoprotein Metabolism (VLDL/HDL/LDL/chylomicron/atherosclerosis) | **85%** | Present in 4 of last 5 papers; 9/11 overall, KU's most-tested applied topic |
| 5 | TCA Cycle (steps, amphibolic nature) | **80%** | Present in 3 of last 5 papers; consistently paired with oxidative phosphorylation |
| 6 | Free Radicals & Antioxidants | **75%** | Present in 3 of last 5 papers; recurring short-note staple |
| 7 | Cardiac Markers | **70%** | Present in 3 of last 5 papers; clinically-oriented, favoured for BDS applied questions |
| 8 | Enzyme Kinetics & Inhibition | **70%** | High overall frequency (9/11) despite a dip in the most recent two papers |
| 9 | Neurotransmitters & Catecholamine Synthesis | **65%** | Present in 3 of last 5 papers; broad topic covering ACh, dopamine, myasthenia, OP poisoning |
| 10 | Iron Metabolism | **60%** | Appeared in the most recent paper (Oct/Nov 2021); historically strong (7/11) but skipped several recent years |

---

## Sample Question Type per Top Topic

**1. Oxidative Phosphorylation / ETC**
> "List the components of electron transport chain. Explain the chemiosmotic theory." *(2021)*

**2. Ketone Bodies**
> "What are ketone bodies? Name the physiological and pathological conditions in which synthesis of ketone bodies are increased." *(2021)*

**3. Glycolysis**
> "Write down the irreversible steps of glycolysis. Add a note on rapaport leubering cycle and its significance." *(2021)*

**4. Lipoprotein Metabolism**
> "What are apo-lipoproteins? Classify lipoproteins. Illustrate the metabolic cycle of chylomicrons." *(2020)*

**5. TCA Cycle**
> "Write down the steps of TCA cycle. Explain why it is called the common terminal metabolic pathway." *(2021)*

**6. Free Radicals & Antioxidants**
> "Write short notes on: Anti-oxidants and their role in biological systems." *(2020)*

**7. Cardiac Markers**
> "Write short notes on: Cardiac markers and their role in diagnosis of Myocardial infarction." *(2020)*

**8. Enzyme Kinetics & Inhibition**
> "Define enzyme, coenzyme, and isoenzyme. Explain factors that affect enzymes activity." *(2021)*

**9. Neurotransmitters & Catecholamine Synthesis**
> "Define neurotransmitter, write down the criteria to be considering a substance as neurotransmitters and classify them." *(2021)*

**10. Iron Metabolism**
> "Discuss diagrammatically the absorption of non-heme iron, its transport and storage. How does hepcidin regulate iron absorption?" *(2021)*

---

## Notes and limitations

- This dataset covers 11 papers spanning 2015–2021; no papers from 2022–2026 were
  available for extraction at the time of this analysis. If newer papers surface,
  re-run this analysis — pattern strength should improve with more recent data points.
- "BDS I (old course)" and "BDS I (new course)" papers from 2016 were counted as two
  separate data points since they represent different exam structures (35 vs 25 marks
  per section), which may slightly inflate frequency for topics common to both.
- Confidence percentages are directional study-prioritisation aids, not a substitute
  for complete syllabus coverage — several one-off topics (e.g., nucleotide salvage
  pathway, cardiac muscle calcium handling, mineral metabolism) have appeared exactly
  once and could reappear without warning.
