# Presentation Deck: ALVEARE — A Full-Stack Domain-Specific Framework for Regular Expressions

**Paper Reference:** Filippo Carloni, Davide Conficconi, Emanuele Del Sozzo, and Marco D. Santambrogio. *"ALVEARE: A Full-Stack Domain-Specific Framework for Regular Expressions"*, IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD).

**File Locations:**
- **PowerPoint Presentation (.pptx):** [ALVEARE_Research_Paper_Presentation.pptx](file:///c:/Users/Jashith%20Masand/Desktop/CN/ALVEARE_Research_Paper_Presentation.pptx)
- **High-Resolution PDF Export (.pdf):** [ALVEARE_Research_Paper_Presentation.pdf](file:///c:/Users/Jashith%20Masand/Desktop/CN/ALVEARE_Research_Paper_Presentation.pdf)
- **Simple State Diagram (Style 1 - Image 1 Match):** [alveare_simple_state_diagram.svg](file:///c:/Users/Jashith%20Masand/Desktop/CN/alveare_simple_state_diagram.svg)
- **Phased Swimlane State Diagram (Style 2 - Image 2 Match):** [alveare_phased_state_diagram.svg](file:///c:/Users/Jashith%20Masand/Desktop/CN/alveare_phased_state_diagram.svg)
- **Full Microarchitecture State Diagram (Detailed):** [alveare_state_diagram.svg](file:///c:/Users/Jashith%20Masand/Desktop/CN/alveare_state_diagram.svg)
- **Interactive Dual Diagram Viewer (.html):** [view_state_diagrams.html](file:///c:/Users/Jashith%20Masand/Desktop/CN/view_state_diagrams.html)
- **Slide Image Previews (1080p PNG):** [slides_img/](file:///c:/Users/Jashith%20Masand/Desktop/CN/slides_img/)

---

## Slide-by-Slide Outline & Structure

### Slide 1: Title Slide
- **Category Badge:** `RESEARCH PAPER PRESENTATION • HARDWARE/SOFTWARE CO-DESIGN`
- **Title:** ALVEARE: A Full-Stack Domain-Specific Framework for Regular Expressions
- **Subtitle:** Overcoming the Efficiency vs. Flexibility Trade-off in Regex Matching with a Tailored 43-bit RISC ISA, Speculative DSA, and Optimizing Compiler
- **Authors:** Filippo Carloni • Davide Conficconi • Emanuele Del Sozzo • Marco D. Santambrogio
- **Affiliation:** NECSTLab, Dipartimento di Elettronica, Informazione e Bioingegneria, Politecnico di Milano
- **Venue:** IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD)
- **Tags:** `Domain-Specific Architecture` • `Custom 43-bit RISC ISA` • `Speculative Microarchitecture` • `FLEX/BISON Compiler` • `FPGA Acceleration`

---

### Slide 2: 1. Topic Overview
- **Subtitle:** *First, understand the computational problem the paper is trying to solve.*
- **Card 1 — Regular Expressions (REs):**
  - Foundational pattern-matching language across modern computing systems.
  - Computer Security: Deep Packet Inspection (Snort, Zeek) and Antivirus scanning (ClamAV).
  - Personalized Medicine: Scanning genomic databases for DNA/RNA motifs and protein sequences.
  - Big Data & Logs: Real-time telemetry filtering and high-speed data ingestion.
- **Card 2 — The Hardware Bottleneck:**
  - Branch Divergence: Quantifiers (`*`, `+`, `?`), repetitions `{m,n}`, and alternations `(a|b)` force constant backtracking.
  - Memory Bound: DFA representations suffer from exponential state explosion, overwhelming CPU caches.
  - CPU/GPU Penalties: General-purpose cores stall on serialization and memory latency at 100+ Gbps line rates.
- **Card 3 — Domain-Specific Co-Design:**
  - Treating Regular Expressions as a first-class Domain-Specific Language (DSL).
  - Tailored 43-bit ISA: Purpose-built instructions handling character matching, ranges, and quantifiers.
  - Speculative Microarchitecture: Hardware-managed speculation stack eliminates CPU software backtracking.
  - Lightweight Compiler: Shifts structural complexity to compile-time software, keeping hardware lean and fast.
- **Bottom Callout:** *Why it matters: Software engines (RE2, Hyperscan) are flexible but energy-intensive, while conventional hardware accelerators (ASICs/FPGAs) are fast but restricted to simple patterns. ALVEARE bridges this gap by uniting software flexibility with custom hardware efficiency.*

---

### Slide 3: 2. Research Gap – Identified in the Paper
- **Subtitle:** *What existing regular expression workflows and hardware accelerators were missing.*
- **Point 1 — Efficiency vs. Flexibility Dilemma:** Software engines (RE2, PCRE) support broad operators but run slowly with high power; hardware accelerators (ASICs) are rigid and support only trivial subsets.
- **Point 2 — Strict Data Dependencies & Backtracking:** Complex operators like greedy/lazy quantifiers and alternations induce severe branch divergence, causing massive pipeline stalls on CPUs and GPUs.
- **Point 3 — Absence of Tailored RE ISAs:** General-purpose instruction sets (x86, ARM) require dozens of generic ALU cycles to process a single character set, range match, or repetition count.
- **Point 4 — Automata Memory & State Explosion:** Converting modern REs into Deterministic Finite Automata (DFAs) leads to exponential state space explosion; NFA alternatives require complex interconnects.
- **Point 5 — Line-Rate Energy Inefficiency:** Running 100+ Gbps network security inspection on server CPUs or SmartNIC DPUs consumes prohibitive amounts of energy and induces thermal throttling.
- **Synthesis Callout:** *Research gap: A unified full-stack framework combining high-level regex expressiveness, fast compilation, and speculative line-rate hardware execution without exponential state explosion.*

---

### Slide 4: 3. Problem Statement
- **Subtitle:** *The core research question and architectural trade-off addressed by the authors.*
- **Core Question:** *How can regular expression matching overcome the efficiency vs. flexibility trade-off to provide high throughput and energy efficiency while preserving full support for complex, real-world regex operators?*
- **Traditional Workflows:**
  - Path A (General-Purpose Software: RE2, PCRE, Hyperscan): High operator flexibility, but CPU/GPU thread divergence stalls throughput; DFAs cause memory explosion; NFAs require costly pointer chasing.
  - Path B (Fixed Hardware Accelerators / Rigid ASICs): High throughput, but restricted to simple character matches; modifying expressions requires full FPGA/ASIC resynthesis.
  - *Risk:* Severe trade-off between operator support and line-rate performance.
- **Proposed ALVEARE Workflow:**
  - 1. DSL Treatment: Treat regular expressions as a domain-specific language.
  - 2. Ad-hoc Compiler: Parse and optimize ASTs, emitting 43-bit RISC code in $O(N)$.
  - 3. Speculative Microarchitecture: Single-cycle hardware rollback via on-chip stack.
  - 4. Scalable DSA: Multi-core execution scaling from 1 to 10+ cores on FPGA.
  - *Advantage:* Full operator flexibility with custom silicon speed & efficiency.
- **Objective:** *Shift structural complexity from hardware to software, creating a lightweight speculative DSA that achieves up to 34x speedup and 57x energy savings while retaining broad operator support.*

---

### Slide 5: 4. Methods Used in the Paper
- **Subtitle:** *A full-stack hardware-software co-design spanning benchmarks, compiler, ISA, and microarchitecture.*
- **Method 1 — Benchmark Operator Analysis:** Quantitatively analyzed 6 benchmark suites (ANMLZoo: Snort, PowerEN, Protomata; Brill, ClamAV, Dotstar) to profile real-world operator frequencies.
- **Method 2 — 43-bit RISC-based RE ISA:** Custom 43-bit instruction set with 3 classes: Control (branches/loops), Base (single char/wildcard), and Complex (classes, ranges, quantifiers).
- **Method 3 — Speculative Microarchitecture:** Speculation engine with on-chip Speculation Stack that checkpoints states, handling greedy/lazy backtracking without CPU intervention.
- **Method 4 — 3 Decode Units & Vector Compute:** Parallel front-end featuring 3 decode units dispatching instructions simultaneously to Vector Compute Units (VCUs) for multi-character evaluations.
- **Method 5 — Ad-Hoc Optimizing C Compiler:** Written in C (FLEX/BISON). Translates ASTs into optimized 43-bit machine code with linear $O(N)$ time and space complexity, eliminating state explosion.
- **Method 6 — Multi-Core FPGA Prototyping:** Synthesized in VHDL on an Avnet Ultra96v2 FPGA (Xilinx ZU3EG MPSoC) at 300 MHz, linearly scaling from 1 to 10 independent cores.
- **Co-Design Principle:** *Lifting structural complexity to the compiler keeps the hardware core lightweight and fast, enabling multi-core scalability on low-cost FPGA silicon.*

---

### Slide 6: 5. Input to the Proposed Method
- **Subtitle:** *What information and datasets enter the ALVEARE framework?*
- **Input A — Regular Expression Rules:** PCRE/POSIX syntax; character classes `[a-z]`, bounded repetitions `{m,n}`, greedy & lazy quantifiers (`*`, `+`, `?`); 200 randomly selected patterns each from Snort, Protomata, and PowerEN.
- **Input B — Target Data Streams:** Raw unstructured byte streams; 1 MB benchmark payload files; chunked into 16 KB blocks matching on-chip memory buffers.
- **Input C — Architecture Config:** 1 to 10 processing cores active on FPGA; hardware constraints (max reference width of four 8-bit chars, counters 0 to 62); speculation stack depth limits.
- **Concrete Mini-Example:**
  - Input RE: `"/api/v[0-9]{1,2}/[a-z]+(\\.json|\\.xml)"`
  - Target Stream: 16 KB network packet payload arriving from an Ethernet interface into FPGA BRAM buffers.
  - Hardware Target: 4-core ALVEARE deployment running at 300 MHz on Xilinx Zynq UltraScale+ MPSoC.

---

### Slide 7: 6. Output of the Proposed Method
- **Subtitle:** *The framework produces optimized machine code, precise match telemetry, and high energy efficiency.*
- **Output 1 — Compiled 43-bit Machine Code:** Compact RISC-based binary instructions directly loadable into the processor's on-chip instruction memory, completely avoiding DFA state explosion.
- **Output 2 — Exact Match Flags & Offsets:** Real-time boolean match signals accompanied by exact start and end byte coordinates of matching patterns within the streaming input buffer.
- **Output 3 — Line-Rate Acceleration Metrics:** Demonstrated execution speedup of up to 34x over CPU/DPU software solutions (RE2 on ARM A53, NVIDIA BlueField-2) and 356x faster than GPU implementations.
- **Output 4 — Ultra-Low Energy Dissipation:** Significant energy efficiency improvement of up to 57x (Joules per processed MB) compared to server CPUs, GPUs, and embedded SoC matchers.
- **Output 5 — Multi-Core Scale-Out Telemetry:** Comprehensive hardware metrics including total execution clock cycles, speculation stack peak depth, and core-by-core utilization across 1 to 10 cores.
- **Deliverable Highlight:** *Real-time pattern detection at 300 MHz with deterministic memory consumption, instant sub-millisecond compilation, and zero state explosion.*

---

### Slide 8: 7. Steps Involved in the Proposed Method
- **Subtitle:** *The end-to-end flow from high-level regular expression to hardware match detection.*
- **Step 1:** Parse RE Syntax (FLEX lexer & BISON parser convert PCRE expressions into an AST).
- **Step 2:** Optimize AST (AST simplification, merging character ranges and pruning redundant sub-expressions).
- **Step 3:** Emit 43-bit Binary (C compiler generates custom RISC machine code in linear time & space $O(N)$).
- **Step 4:** Load Instructions (Binary program loaded into FPGA on-chip instruction memory BRAM).
- **Step 5:** Stream Target Data (16 KB payload chunks streamed into hardware input buffers via AXI interfaces).
- **Step 6:** 3-Way Decode (3 Decode Units dispatch instructions in parallel to Vector Compute Units).
- **Step 7:** Speculative Match (Speculation Stack checkpoints states during quantifiers/alternations; auto-backtracks on mismatch).
- **Step 8:** Report Match Results (Hardware asserts match flag, outputs start/end byte offsets, and advances stream).
- **Mechanism Deep-Dives:**
  - *Hardware Backtracking Mechanism:* When a speculative branch fails, the core restores previous character pointers and state in a single clock cycle directly from the Speculation Stack, eliminating software interrupt latency.
  - *Linear-Time Compilation Pipeline:* Unlike DFAs which suffer catastrophic exponential memory growth during compilation, ALVEARE compiles in $O(N)$ linear time and space, enabling fast dynamic rule loading at runtime.

---

### Slide 9: Evaluation: What Did the Authors Find?
- **Subtitle:** *Benchmarking against state-of-the-art CPU, GPU, DPU, and server engines on ANMLZoo.*
- **Benchmark Comparison Table:**

| System / Engine | Speedup vs Baseline | Energy Efficiency Gain | Compilation Time | Operator Support |
| :--- | :---: | :---: | :---: | :--- |
| **ALVEARE (1-10 Cores @ 300MHz, FPGA)** | **Up to 34x faster** | **17x – 57x higher** | **Sub-millisecond (Linear)** | **Broad (Classes, Quantifiers, Bounds)** |
| Google RE2 (ARM Cortex-A53 SoC) | 1.0x (Baseline CPU) | 1.0x (Baseline) | Fast (Software AST) | Broad PCRE/POSIX |
| NVIDIA BlueField-2 DPU (Data Center) | 0.8x – 1.8x | 2.1x – 3.4x | Moderate | Broad PCRE/POSIX |
| GPU-based Matchers (NVIDIA CUDA) | 0.05x – 0.1x (356x Slower) | Poor (High Wattage) | High (Kernel compilation) | Restricted (Severe divergence) |
| Intel Hyperscan (Intel Xeon Server) | Competitive Throughput | 15x – 25x Worse Power | High (Heavy DFA/NFA build) | Restricted complex quantifiers |

- **Key Findings:**
  - Up to 34x Speedup over embedded CPUs and DPU SmartNICs, scaling linearly with core count.
  - At least 356x Faster than GPUs: Eliminates thread serialization caused by warp divergence.
  - 17x to 57x Energy Gain: Consumes a fraction of the power of Xeon servers and DPUs.
  - Zero State Explosion: Compiles rulesets instantly without memory explosion.
- **Architectural Limitations:**
  - Reference holds a maximum of four 8-bit characters; repetition counters limited to 0–62.
  - Large rulesets require time-multiplexing across FPGA reconfiguration.
  - Single comparator active after partial match.
  - Pathological nested expressions can trigger algorithmic ReDoS collapse without compiler guardrails.

---

### Slide 10: Conclusion and Key Takeaways
- **Subtitle:** *What should the audience remember about the ALVEARE framework?*
- **Research Contribution:** Proposed the first full-stack domain-specific framework for regular expressions; introduced a tailored 43-bit RISC ISA; built a speculative microarchitecture with on-chip stack; implemented a linear-time C compiler.
- **Practical Value:** Resolves the dilemma between software flexibility and ASIC rigidity; delivers up to 34x speedup and 57x energy savings; unlocks line-rate deep packet inspection (Snort) and genomics at low power; linear $O(N)$ compile time eliminates DFA memory blowup.
- **Critical Limitations:** Reference width fixed at four 8-bit characters; counters capped at 0–62; large rulesets require dynamic FPGA time-multiplexing; susceptible to algorithmic ReDoS on nested quantifiers.
- **One-Sentence Summary:** *ALVEARE proves that treating Regular Expressions as a domain-specific language paired with a custom 43-bit RISC ISA, a speculative microarchitecture, and an optimizing compiler delivers line-rate matching and up to 57x energy efficiency without sacrificing operator flexibility.*

---

### Slide 11: Quick Explanation / Speaker Notes
- **Q1: What is a Domain-Specific Architecture (DSA) in this context?**
  - *A:* A DSA is hardware customized specifically for a narrow domain—in this case, regular expression primitives (character classes, ranges, repetition counters) rather than general-purpose math. It avoids instruction decoding overhead and directly evaluates regex tokens in silicon.
- **Q2: Why do CPUs and GPUs struggle with regular expression matching?**
  - *A:* Regular expressions contain non-deterministic branches (greedy quantifiers, alternations). When a match fails, the engine must backtrack. On GPUs, this creates severe thread warp divergence where parallel lanes serialize. On CPUs, it causes cache thrashing and branch mispredictions.
- **Q3: How does ALVEARE's speculative microarchitecture avoid performance collapse?**
  - *A:* ALVEARE speculates that greedy paths succeed while pushing alternative checkpoints onto an on-chip Speculation Stack. If a character mismatch occurs, the controller pops the previous state in a single clock cycle, avoiding costly software interrupt routines or DFA state explosions.
- **Q4: Why does lifting complexity to the compiler help the hardware?**
  - *A:* Compilers can analyze ASTs, merge character ranges, and eliminate dead branches ahead of time in software. This keeps the hardware core tiny (fitting up to 10+ cores on a budget FPGA) and allows compilation in linear time $O(N)$, unlike DFAs which experience exponential graph explosions.
- **Suggested Closing Remark:** *“ALVEARE demonstrates that by treating regular expressions as a domain-specific programming language, we can achieve custom-silicon speeds and up to 57x energy efficiency while retaining the rich operator expressiveness required by modern cybersecurity and bioinformatics.”*
