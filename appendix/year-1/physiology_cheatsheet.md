# BDS 1st Year — Physiology Quick Revision Cheatsheet
*Based on Kathmandu University Past Questions (2015–2022)*

This cheatsheet distills the most frequently tested physiological concepts, ionic mechanisms, cardiovascular cycles, and hematological pathways from the extracted past papers. Use it for rapid review before your exams.

---

## 1. General Physiology & Membrane Transport

### Homeostasis & Feedback Loops
* **Homeostasis:** Maintenance of a stable, dynamic internal environment (extracellular fluid / *milieu intérieur*) essential for cellular function (Claude Bernard, Walter Cannon).
* **Negative Feedback:** The primary homeostatic mechanism. A deviation in a controlled variable triggers a response that opposes/reverses the initial change back to set-point.
  * *Components:* Sensor / Receptor → Afferent pathway → Control Center (Hypothalamus/Medulla) → Efferent pathway → Effector.
  * *Examples:* Arterial blood pressure (baroreceptor reflex), blood glucose regulation (insulin/glucagon), core body temperature regulation.
* **Positive Feedback:** The effector response amplifies or reinforces the initial disturbance away from the set-point until a definitive endpoint is achieved.
  * *Examples:* Parturition (Ferguson reflex: oxytocin release on cervical stretch), Blood coagulation cascade (thrombin activates upstream factors), Action potential generation (Hodgkin cycle: depolarization increases $Na^+$ conductance which causes further depolarization).

### Transport Across Cell Membranes
* **Passive Transport (No Direct Energy Required):**
  * *Simple Diffusion:* Down electrochemical gradient through lipid bilayer (O₂, CO₂, steroid hormones) or water channels/aquaporins.
  * *Facilitated Diffusion:* Carrier-mediated transport down gradient without energy; exhibits saturation kinetics ($V_{max}$) and specificity (e.g. GLUT-4 in muscle/adipose, GLUT-2 in liver).
* **Active Transport (Requires Energy, Against Gradient):**
  * **Primary Active Transport:** Hydrolysis of ATP directly powers the carrier pump.
    * **$Na^+/K^+$ ATPase Pump:** Pumps **$3\ Na^+$ ions OUT** and **$2\ K^+$ ions IN** for every ATP hydrolyzed.
    * *Significance:* Maintains resting membrane potential (electrogenic), regulates intracellular osmotic volume (prevents cell swelling/lysis), and generates the transmembrane $Na^+$ gradient that drives secondary active transport.
    * *Other primary pumps:* $Ca^{2+}$-ATPase (SERCA in sarcoplasmic reticulum), $H^+/K^+$ ATPase (gastric parietal cells).
  * **Secondary Active Transport:** Uses the potential energy stored in an ionic concentration gradient (usually $Na^+$) previously created by primary active transport.
    * *Cotransport (Symport):* Both solute and $Na^+$ move in the **same direction** across the membrane (e.g. **SGLT-1** $Na^+$-glucose cotransporter and $Na^+$-amino acid transporters in intestinal enterocytes and renal proximal tubules).
    * *Countertransport (Antiport):* Solute and $Na^+$ move in **opposite directions** (e.g. $Na^+/Ca^{2+}$ exchanger in myocardium, $Na^+/H^+$ antiporter in renal tubules).

---

## 2. Nerve, Muscle & Neurophysiology

### Action Potential in Excitable Tissues
* **Resting Membrane Potential (RMP):**
  * Typical values: Nerve = **-70 mV**; Skeletal muscle = **-90 mV**.
  * Primarily determined by the high resting permeability of **$K^+$ leak channels** (close to $K^+$ equilibrium potential of -90 mV) and maintained by the $Na^+/K^+$ pump.
* **Phases of Action Potential:**
  1. *Depolarization:* Stimulus depolarizes membrane to threshold (~ -55 mV) → explosive opening of **voltage-gated $Na^+$ channels** (activation m-gates open) → massive $Na^+$ influx → membrane potential overshoots to **+35 mV**.
  2. *Repolarization:* At peak, $Na^+$ channels inactivate (h-gates close) and slow **voltage-gated $K^+$ channels** open fully → rapid $K^+$ efflux restores internal negativity.
  3. *After-Hyperpolarization (Positive After-Potential):* Voltage-gated $K^+$ channels are slow to close, causing excessive $K^+$ efflux toward -90 mV before settling back to RMP.
* **Refractory Periods:**
  * *Absolute Refractory Period (ARP):* From firing level until 1/3 of repolarization. Voltage-gated $Na^+$ channels are either open or in inactivated state. **No stimulus, however strong, can elicit a second action potential.** Limits maximum firing frequency.
  * *Relative Refractory Period (RRP):* From end of ARP until return to RMP. Some $Na^+$ channels have reset to resting closed state, but $K^+$ conductance remains elevated. **A suprathreshold (stronger than normal) stimulus can trigger an action potential** with reduced amplitude.

### Synaptic Transmission & Neuromuscular Junction
* **Synapse:** Functional junction between two neurons or between an excitable neuron and effector cell.
* **Events of Synaptic Transmission:**
  1. Action potential arrives at presynaptic axon terminal.
  2. Voltage-gated $Ca^{2+}$ channels open → **$Ca^{2+}$ influx** into terminal.
  3. $Ca^{2+}$ activates synaptotagmin and SNARE proteins, causing exocytosis of neurotransmitter (e.g., Acetylcholine) into the synaptic cleft.
  4. Neurotransmitter diffuses across cleft (20–40 nm) and binds specific postsynaptic receptors.
  5. *Excitatory Postsynaptic Potential (EPSP):* Opening of ligand-gated $Na^+$/cation channels → local depolarization.
  6. *Inhibitory Postsynaptic Potential (IPSP):* Opening of ligand-gated $Cl^-$ or $K^+$ channels → local hyperpolarization.
  7. Termination: Reuptake into presynaptic terminal or enzymatic breakdown (e.g. Acetylcholinesterase).
* **Neuromuscular Junction (NMJ):**
  * Synapse between somatic motor neuron and skeletal muscle motor end plate.
  * Neurotransmitter: **Acetylcholine (ACh)** acting on nicotinic ACh receptors ($N_M$).
  * Produces an **End Plate Potential (EPP)**, an obligate local depolarizing potential that invariably triggers a muscle action potential.
* **Myasthenia Gravis:**
  * Autoimmune disorder where autoantibodies attack and block/destroy post-synaptic **nicotinic ACh receptors ($N_M$)** at the NMJ.
  * *Features:* Progressive muscular weakness that worsens with repetitive activity and improves with rest (ptosis, diplopia, difficulty chewing and swallowing).
  * *Diagnosis & Treatment:* Tensilon (Edrophonium) test; treated with anticholinesterases (Neostigmine, Pyridostigmine) and immunosuppressants.

### Autonomic Nervous System (ANS)
* **Sympathetic vs. Parasympathetic Functional Differences:**
  * *Heart:* Sympathetic increases heart rate (positive chronotropy via $\beta_1$) and increases contractility (positive inotropy); Parasympathetic decreases heart rate (negative chronotropy via $M_2$ muscarinic receptors via vagus nerve), minimal effect on ventricular contractility.
  * *Urinary Bladder:* Sympathetic relaxes detrusor muscle ($\beta_2/\beta_3$) and contracts internal urethral sphincter ($\alpha_1$) to promote **urine storage**; Parasympathetic contracts detrusor ($M_3$) and relaxes internal sphincter to promote **micturition**.
  * *Pupil:* Sympathetic causes pupillary dilation (**mydriasis** via $\alpha_1$ on pupillary dilator muscle); Parasympathetic causes pupillary constriction (**miosis** via $M_3$ on sphincter pupillae).
  * *Bronchi:* Sympathetic causes bronchodilation ($\beta_2$); Parasympathetic causes bronchoconstriction ($M_3$) and increases secretions.

---

## 3. Blood, Hematology & Hemostasis

### Erythropoiesis
* **Definition & Site:** Process of formation of mature RBCs. In adults: red bone marrow of flat and irregular bones (sternum, vertebrae, ribs, pelvis, skull).
* **Stages of Differentiation:**
  1. *Pluripotent Hematopoietic Stem Cell (PHSC)* → CFU-GEMM → BFU-E → CFU-E.
  2. *Proerythroblast:* Large cell (15–20 $\mu$m), basophilic cytoplasm, large nucleus with 2–3 nucleoli.
  3. *Early Normoblast (Basophilic):* Nucleoli disappear, chromatin condenses.
  4. *Intermediate Normoblast (Polychromatic):* **Hemoglobin synthesis begins**; cytoplasm stains dual (basophilic RNA + acidophilic hemoglobin).
  5. *Late Normoblast (Orthochromatic):* Cytoplasm predominantly pink (acidophilic); **nucleus becomes pyknotic and is extruded** from the cell.
  6. *Reticulocyte:* Immature, non-nucleated RBC containing remnants of ribosomal RNA network (stains with vital stains: New Methylene Blue / Brilliant Cresyl Blue). Normal count: 0.5–1.5%.
  7. *Mature Erythrocyte:* Biconcave, non-nucleated disc (7.2 $\mu$m diameter), lifespan = **120 days**.
* **Regulation of Erythropoiesis:**
  * **Erythropoietin (EPO):** Glycoprotein hormone secreted primarily by renal peritubular interstitial cells (85%) in response to **tissue hypoxia**. Stimulates proliferation and differentiation of CFU-E into proerythroblasts.
  * *Nutritional Factors:* Vitamin B12 and Folic acid (essential for DNA synthesis and nuclear maturation; deficiency causes Megaloblastic Anemia), Iron (essential for heme synthesis; deficiency causes Microcytic Hypochromic Anemia), Proteins/amino acids, Copper, Cobalt.

### Blood Groups & Rh Incompatibility
* **ABO System:** Based on presence or absence of agglutinogens (antigens A and B) on RBC membranes and agglutinins (antibodies anti-A and anti-B) in plasma.
  * **Landsteiner's Law:**
    1. If an agglutinogen is present on the RBC membrane, the corresponding agglutinin must be absent from the plasma.
    2. If an agglutinogen is absent from the RBC membrane, the corresponding agglutinin must be present in the plasma. *(Note: Part 2 applies only to ABO, not to the Rh system).*
  * *Group A:* Antigen A, Anti-B antibody.
  * *Group B:* Antigen B, Anti-A antibody.
  * *Group AB:* Both Antigens A & B, Neither antibody (**Universal Recipient**).
  * *Group O:* Neither antigen, Both Anti-A & Anti-B antibodies (**Universal Donor**).
* **Rh System & Erythroblastosis Fetalis (Hemolytic Disease of the Newborn):**
  * Rh-positive individuals possess the **D antigen** on RBCs; Rh-negative individuals lack it. Anti-D antibodies are not naturally present; they develop only after exposure to Rh+ RBCs.
  * *Mechanism:* Rh-negative mother carries an Rh-positive fetus (father is Rh-positive). During delivery, fetomaternal hemorrhage allows fetal Rh+ RBCs to enter maternal circulation, stimulating production of maternal **anti-D antibodies (IgG)**.
  * In subsequent Rh-positive pregnancies, maternal IgG anti-D antibodies freely cross the placenta and bind to fetal Rh+ RBCs, triggering complement-mediated extravascular hemolysis.
  * *Consequences:* Severe hemolytic anemia, jaundice, hepatosplenomegaly, **Kernicterus** (unconjugated bilirubin crosses immature blood-brain barrier causing basal ganglia damage), and **Hydrops Fetalis** (severe intrauterine heart failure and generalized edema).
  * *Prevention:* Administer **anti-D immunoglobulin (RhoGAM)** to the Rh-negative mother at 28 weeks of gestation and within 72 hours of delivery of an Rh-positive child to neutralize circulating fetal RBCs before maternal sensitization occurs.

### Hemostasis & Coagulation
* **Hemostasis:** Arrest of bleeding following vascular injury. Involves three sequential phases:
  1. **Vascular Spasm:** Immediate reflex vasoconstriction of injured vessel triggered by local myogenic spasm, nociceptor reflexes, and endothelin/serotonin.
  2. **Platelet Plug Formation (Primary Hemostasis):**
     * *Adhesion:* Platelet membrane GP Ib receptors bind to subendothelial collagen via **von Willebrand Factor (vWF)**.
     * *Activation & Secretion:* Platelets change shape (pseudopodia) and release granule contents: **ADP** (aggregating agent), **Thromboxane $A_2$ ($TXA_2$)** (vasoconstrictor and aggregator), and serotonin.
     * *Aggregation:* ADP and $TXA_2$ activate GP IIb/IIIa receptors on adjacent platelets, crosslinking platelets via **fibrinogen** to form an unstable primary hemostatic plug.
  3. **Blood Coagulation (Secondary Hemostasis):**
     * *Extrinsic Pathway:* Initiated by tissue damage releasing **Tissue Factor (Factor III / Thromboplastin)**. Tissue Factor + Factor VIIa + $Ca^{2+}$ activates Factor X to Xa. Rapid (seconds).
     * *Intrinsic Pathway:* Initiated by contact activation when Factor XII contacts negatively charged subendothelial collagen. XIIa → XIa → IXa. Factor IXa + Factor VIIIa + $Ca^{2+} +$ Platelet factor 3 activate Factor X to Xa. Slower (minutes).
     * *Common Pathway:* Factor Xa combines with Factor Va, $Ca^{2+}$, and phospholipids to form the **Prothrombinase Complex**, which cleaves **Prothrombin (Factor II) into Thrombin (Factor IIa)**.
     * Thrombin converts soluble **Fibrinogen (Factor I) into insoluble Fibrin monomers**, which polymerize into loose fibrin polymers.
     * **Factor XIIIa** (Fibrin-Stabilizing Factor, activated by thrombin) crosslinks fibrin polymers into a tough, stable clot meshwork.

### Plasma Proteins
* **Total Concentration:** 6.0–8.0 g/dL (Albumin: 3.5–5.0 g/dL, Globulins: 2.0–3.5 g/dL, Fibrinogen: 0.2–0.4 g/dL). Normal A:G ratio = **1.2:1 to 1.7:1**.
* **Major Functions:**
  1. *Colloid Osmotic (Oncotic) Pressure:* Contributes ~25 mmHg of effective osmotic pressure. **Albumin generates 70–80%** of total oncotic pressure due to its high concentration and low molecular weight (69 kDa). Prevents fluid extravasation and interstitial edema.
  2. *Transport Function:* Albumin transports unconjugated bilirubin, free fatty acids, calcium, hormones, and drugs (sulfonamides, penicillin). Globulins transport iron (Transferrin), copper (Ceruloplasmin), and thyroid hormones (TBG).
  3. *Immunity:* Gamma-globulins act as circulating antibodies / immunoglobulins (IgG, IgM, IgA, IgE, IgD) produced by plasma cells.
  4. *Coagulation & Fibrinolysis:* Fibrinogen and prothrombin are essential for blood clot formation.
  5. *Buffering Capacity:* Plasma proteins provide ~15% of the total buffering power of blood via imidazole groups of histidine residues.

---

## 4. Cardiovascular Physiology

### The Cardiac Cycle
* **Duration:** At resting heart rate of 75 beats/min, one complete cycle lasts **0.8 seconds**.
* **Ventricular Events Breakdown (0.8 s total):**
  * **Ventricular Systole (0.3 s):**
    1. *Isovolumetric Contraction (0.05 s):* Ventricles contract with all valves closed (AV valves snap shut; semilunar valves not yet open). Ventricular volume remains constant while intraventricular pressure spikes steeply. Produces the **First Heart Sound ($S_1$)**.
    2. *Rapid Ejection (0.10 s):* Ventricular pressure exceeds aortic/pulmonary pressure (~80 mmHg in left ventricle) → semilunar valves open → 2/3 of stroke volume ejected rapidly into aorta.
    3. *Reduced Ejection (0.15 s):* Ventricular repolarization begins (T wave); rate of ejection slows down.
  * **Ventricular Diastole (0.5 s):**
    1. *Isovolumetric Relaxation (0.08 s):* Ventricles relax with all valves closed. Pressure plummets below aortic pressure → semilunar valves close. Produces the **Second Heart Sound ($S_2$)**.
    2. *Rapid Inflow / Rapid Filling (0.11 s):* Ventricular pressure drops below atrial pressure → AV valves open → rapid rush of blood from atria into ventricles (accounts for 70% of ventricular filling). Can produce physiological third heart sound ($S_3$) in children.
    3. *Diastasis / Reduced Filling (0.22 s):* Slow passive filling as venous blood flows continuously into ventricles.
    4. *Atrial Systole (0.10 s):* Atria contract ("atrial kick"), completing the remaining 20–30% of ventricular filling. Produces the fourth heart sound ($S_4$, pathological in ventricular stiffness).
* **Heart Sounds Summary:**
  * **$S_1$ ("Lubb"):** Caused by the closure of AV valves (Mitral and Tricuspid) at the onset of ventricular systole. Low-pitched, soft, relatively long (0.15 s).
  * **$S_2$ ("Dubb"):** Caused by the closure of Semilunar valves (Aortic and Pulmonary) at the onset of ventricular diastole. High-pitched, sharp, short (0.12 s).

### Cardiac Output & Blood Pressure Regulation
* **Cardiac Output (CO):** Volume of blood pumped by each ventricle per minute:
  $$\text{Cardiac Output} = \text{Stroke Volume (SV)} \times \text{Heart Rate (HR)} \approx 70\ \text{mL} \times 72\ \text{bpm} \approx 5.0\ \text{L/min}$$
* **Determinants of Stroke Volume:**
  1. *Preload (End-Diastolic Volume):* Degree of myocardial stretch before contraction. Governed by **Frank-Starling Law of the Heart**: *Within physiological limits, the force of ventricular contraction is directly proportional to the initial resting length of cardiac muscle fibers.*
  2. *Afterload:* Resistance against which the ventricle must pump to eject blood (approximated by Total Peripheral Resistance and mean arterial pressure).
  3. *Contractility (Inotropic State):* Intrinsic force of contraction independent of preload, increased by sympathetic stimulation, catecholamines, and digitalis ($Ca^{2+}$ availability).
* **Blood Pressure Regulation:**
  * **Short-Term Regulation (Baroreceptor Reflex):**
    * High-pressure stretch receptors located in the **carotid sinus** (innervated by sinus nerve of Hering / CN IX) and **aortic arch** (innervated by CN X).
    * Increased arterial BP stretch receptors → increased afferent firing to the *nucleus tractus solitarius (NTS)* in the medulla.
    * NTS stimulates cardioinhibitory center (vagal parasympathetic tone ↑ → heart rate and cardiac output ↓) and inhibits the vasomotor center (sympathetic outflow ↓ → arteriolar vasodilation and venomotor tone ↓).
    * Net result: Rapid reduction of BP back to baseline within seconds.
  * **Long-Term Regulation (Renin-Angiotensin-Aldosterone System - RAAS):**
    * Decreased renal perfusion pressure or sympathetic activation stimulates juxtaglomerular (JG) cells to release **Renin**.
    * Renin converts circulating Angiotensinogen to **Angiotensin I**.
    * Angiotensin-Converting Enzyme (ACE) on pulmonary vascular endothelium converts Angiotensin I into **Angiotensin II**.
    * *Angiotensin II actions:* Potent arteriolar vasoconstrictor (increases TPR), stimulates thirst and ADH release, and stimulates adrenal cortex (zona glomerulosa) to secrete **Aldosterone**.
    * Aldosterone acts on renal late distal tubules and collecting ducts to increase $Na^+$ and water reabsorption, expanding extracellular fluid volume and restoring blood pressure.

### Electrocardiogram (ECG)
* **P wave:** Atrial depolarization (duration: 0.08–0.10 s).
* **PR Interval:** Time between onset of atrial depolarization and onset of ventricular depolarization; represents conduction delay through the **AV node** (normal: **0.12–0.20 s**). Prolonged in 1st-degree heart block.
* **QRS Complex:** Ventricular depolarization (normal duration: **< 0.10 s**). Atrial repolarization is buried within.
* **ST Segment:** Isoelectric period where ventricles remain completely depolarized (corresponds to plateau phase of ventricular action potential). Elevated in acute myocardial infarction.
* **T wave:** Ventricular repolarization (asymmetrical).

---

## 5. Respiratory & Renal Physiology

### Mechanics of Respiration & Surfactant
* **Inspiration:** Active process. Contraction of diaphragm (flattens, accounts for 75% of thoracic volume change) and external intercostal muscles (lifts ribs in "bucket-handle" and "pump-handle" motion) → intrapleural pressure drops from -2.5 mmHg to -6 mmHg → intra-alveolar pressure drops to -1 mmHg → air flows in.
* **Expiration:** Quiet expiration is passive. Diaphragm relaxes; elastic recoil of lungs and chest wall compresses lungs → intra-alveolar pressure rises to +1 mmHg → air flows out.
* **Pulmonary Surfactant:**
  * Synthesized and secreted by **Type II alveolar epithelial cells**.
  * Primary active component: **Dipalmitoylphosphatidylcholine (DPPC)**.
  * *Function:* Greatly lowers alveolar surface tension, governed by the **Law of Laplace** ($P = 2T / r$). By lowering surface tension ($T$) proportionally more in smaller alveoli than larger ones, it prevents smaller alveoli from collapsing into larger ones (**prevents atelectasis**), stabilizes alveolar size, increases lung compliance, and prevents pulmonary capillary transudation (edema).
  * *Clinical Correlation:* Deficiency in premature infants causes **Infant Respiratory Distress Syndrome (IRDS)**.

### Lung Volumes and Capacities
* **Tidal Volume (TV):** Volume of air inspired or expired with each normal quiet breath (~**500 mL**).
* **Inspiratory Reserve Volume (IRV):** Extra volume that can be inspired above tidal volume (~**3000 mL**).
* **Expiratory Reserve Volume (ERV):** Extra volume that can be forcefully expired after tidal expiration (~**1100 mL**).
* **Residual Volume (RV):** Volume remaining in lungs even after maximal forced expiration (~**1200 mL**). *Cannot be measured by simple spirometry.*
* **Vital Capacity (VC):** Maximum volume that can be exhaled following maximal inspiration ($VC = IRV + TV + ERV \approx \mathbf{4600\ mL}$).
* **Total Lung Capacity (TLC):** Total volume in lungs after maximal inspiration ($TLC = VC + RV \approx \mathbf{5800\ mL}$).

### Renal Physiology: GFR & Countercurrent Mechanism
* **Glomerular Filtration Rate (GFR):** Volume of filtrate formed by both kidneys per minute (normal: **125 mL/min** or **180 L/day**).
  * Determined by Starling forces:
    $$\text{Net Filtration Pressure} = (P_{GC} - P_{BS}) - (\pi_{GC} - \pi_{BS})$$
    * Glomerular hydrostatic pressure ($P_{GC} \approx 60\ \text{mmHg}$) favors filtration.
    * Bowman's space pressure ($P_{BS} \approx 18\ \text{mmHg}$) and Glomerular oncotic pressure ($\pi_{GC} \approx 32\ \text{mmHg}$) oppose filtration.
* **Countercurrent Mechanism (Urine Concentration):**
  * **Countercurrent Multiplier (Loop of Henle):** Descending limb is permeable to water but impermeable to solutes (fluid becomes hypertonic up to 1200 mOsm/L at hairpin turn). Ascending thick limb actively reabsorbs $Na^+, K^+, 2Cl^-$ via NKCC2 cotransporter but is impermeable to water, creating a hyperosmotic medullary interstitium.
  * **Countercurrent Exchanger (Vasa Recta):** Hairpin capillary loops maintain the medullary osmotic gradient by passive diffusion of water and solutes without washing out the gradient.

---
> 💡 **Exam Tip for KU:** In Physiology, structured long-answer questions are scored on completeness of phases and diagrams. Always draw labeled diagrams for the **Action Potential (with voltage and millisecond scales)**, the **Cardiac Cycle (Wiggers Diagram phases)**, and flowcharts for the **Extrinsic & Intrinsic Coagulation Cascades** and **RAAS pathway**.
