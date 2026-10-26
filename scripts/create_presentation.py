import collections.abc
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck(filename="ALVEARE_Research_Paper_Presentation.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_slide_layout = prs.slide_layouts[6]

    # Color Palette - Professional Modern Academic Tech
    BG_COLOR = RGBColor(248, 250, 252)        # Slate 50
    CARD_BG = RGBColor(255, 255, 255)         # Pure White
    CARD_BORDER = RGBColor(226, 232, 240)     # Slate 200
    NAVY = RGBColor(15, 23, 42)               # Slate 900
    BLUE_ACCENT = RGBColor(29, 78, 216)       # Blue 700
    CYAN_ACCENT = RGBColor(2, 132, 199)       # Sky 600
    TEXT_MUTED = RGBColor(100, 116, 139)      # Slate 500
    TEXT_BODY = RGBColor(51, 65, 85)          # Slate 700
    BADGE_BG = RGBColor(239, 246, 255)        # Blue 50
    BADGE_BORDER = RGBColor(191, 219, 254)    # Blue 200
    HIGHLIGHT_BG = RGBColor(241, 245, 249)    # Slate 100
    CALLOUT_BG = RGBColor(238, 242, 255)      # Indigo 50
    CALLOUT_BORDER = RGBColor(199, 210, 254)  # Indigo 200

    def add_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()
        return bg

    def add_card(slide, left, top, width, height, fill_color=CARD_BG, border_color=CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = fill_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1)
        else:
            card.line.fill.background()
        return card

    def add_para(tf, text, font_size=10.5, bold=False, color=TEXT_BODY, space_before=0, space_after=0, align=PP_ALIGN.LEFT):
        if len(tf.paragraphs) == 1 and len(tf.paragraphs[0].text) == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.alignment = align
        if space_before > 0:
            p.space_before = Pt(space_before)
        if space_after > 0:
            p.space_after = Pt(space_after)
        run = p.add_run()
        run.text = text
        run.font.name = "Segoe UI"
        run.font.size = Pt(font_size)
        run.font.bold = bold
        run.font.color.rgb = color
        return p

    def add_header(slide, title_text, subtitle_text, slide_num):
        # Header title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.73), Inches(0.55))
        tf = title_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        add_para(tf, title_text, font_size=22, bold=True, color=NAVY)

        # Subtitle
        sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.98), Inches(11.73), Inches(0.35))
        tf_sub = sub_box.text_frame
        tf_sub.word_wrap = True
        tf_sub.margin_left = tf_sub.margin_top = tf_sub.margin_right = tf_sub.margin_bottom = 0
        add_para(tf_sub, subtitle_text, font_size=13, bold=False, color=TEXT_MUTED)

        # Footer
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(10.5), Inches(0.3))
        tf_f = footer_box.text_frame
        tf_f.margin_left = tf_f.margin_top = tf_f.margin_right = tf_f.margin_bottom = 0
        add_para(tf_f, "Research paper analysis • ALVEARE: A Full-Stack Domain-Specific Framework for Regular Expressions", font_size=9.5, color=TEXT_MUTED)

        # Page Number
        num_box = slide.shapes.add_textbox(Inches(12.0), Inches(7.05), Inches(0.5), Inches(0.3))
        tf_n = num_box.text_frame
        tf_n.margin_left = tf_n.margin_top = tf_n.margin_right = tf_n.margin_bottom = 0
        add_para(tf_n, str(slide_num), font_size=10, bold=True, color=TEXT_MUTED, align=PP_ALIGN.RIGHT)

    def set_speaker_notes(slide, notes_text):
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = notes_text

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_slide_layout)
    add_bg(s1)

    top_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.12))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = BLUE_ACCENT
    top_bar.line.fill.background()

    # Category Pill
    pill = add_card(s1, Inches(1.0), Inches(0.85), Inches(5.8), Inches(0.38), fill_color=BADGE_BG, border_color=BADGE_BORDER)
    tb_pill = s1.shapes.add_textbox(Inches(1.15), Inches(0.9), Inches(5.5), Inches(0.3))
    tf_p = tb_pill.text_frame
    tf_p.margin_left = tf_p.margin_top = tf_p.margin_right = tf_p.margin_bottom = 0
    add_para(tf_p, "RESEARCH PAPER PRESENTATION • HARDWARE/SOFTWARE CO-DESIGN", font_size=10, bold=True, color=BLUE_ACCENT)

    # Main Title
    tb_title = s1.shapes.add_textbox(Inches(1.0), Inches(1.45), Inches(11.33), Inches(1.4))
    tf_t = tb_title.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
    add_para(tf_t, "ALVEARE: A Full-Stack Domain-Specific\nFramework for Regular Expressions", font_size=32, bold=True, color=NAVY)

    # Subtitle
    tb_sub = s1.shapes.add_textbox(Inches(1.0), Inches(3.05), Inches(11.33), Inches(0.75))
    tf_s = tb_sub.text_frame
    tf_s.word_wrap = True
    tf_s.margin_left = tf_s.margin_top = tf_s.margin_right = tf_s.margin_bottom = 0
    add_para(tf_s, "Overcoming the Efficiency vs. Flexibility Trade-off in Regex Matching\nwith a Tailored 43-bit RISC ISA, Speculative DSA, and Optimizing Compiler", font_size=15, bold=False, color=TEXT_BODY)

    # Authors Card
    add_card(s1, Inches(1.0), Inches(4.05), Inches(11.33), Inches(1.75), fill_color=CARD_BG, border_color=CARD_BORDER)

    tb_auth = s1.shapes.add_textbox(Inches(1.3), Inches(4.25), Inches(10.7), Inches(0.35))
    tf_a = tb_auth.text_frame
    tf_a.margin_left = tf_a.margin_top = tf_a.margin_right = tf_a.margin_bottom = 0
    add_para(tf_a, "Authors: Filippo Carloni • Davide Conficconi • Emanuele Del Sozzo • Marco D. Santambrogio", font_size=13.5, bold=True, color=NAVY)

    tb_affil = s1.shapes.add_textbox(Inches(1.3), Inches(4.68), Inches(10.7), Inches(0.35))
    tf_af = tb_affil.text_frame
    tf_af.margin_left = tf_af.margin_top = tf_af.margin_right = tf_af.margin_bottom = 0
    add_para(tf_af, "Affiliation: NECSTLab, Dipartimento di Elettronica, Informazione e Bioingegneria, Politecnico di Milano", font_size=11.5, color=TEXT_MUTED)

    tb_venue = s1.shapes.add_textbox(Inches(1.3), Inches(5.1), Inches(10.7), Inches(0.35))
    tf_v = tb_venue.text_frame
    tf_v.margin_left = tf_v.margin_top = tf_v.margin_right = tf_v.margin_bottom = 0
    add_para(tf_v, "Venue: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD)", font_size=11.5, bold=True, color=BLUE_ACCENT)

    # Tags Row
    tags = ["Domain-Specific Architecture", "Custom 43-bit RISC ISA", "Speculative Microarchitecture", "FLEX/BISON Compiler", "FPGA Acceleration"]
    tx = Inches(1.0)
    for tag in tags:
        tw = Inches(2.15)
        add_card(s1, tx, Inches(6.05), tw, Inches(0.36), fill_color=HIGHLIGHT_BG, border_color=CARD_BORDER)
        tb_t = s1.shapes.add_textbox(tx, Inches(6.11), tw, Inches(0.28))
        tf_tag = tb_t.text_frame
        tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
        add_para(tf_tag, tag, font_size=9.5, bold=True, color=TEXT_BODY, align=PP_ALIGN.CENTER)
        tx += tw + Inches(0.14)

    # Footer
    tb_foot = s1.shapes.add_textbox(Inches(1.0), Inches(6.8), Inches(10.5), Inches(0.3))
    tf_f1 = tb_foot.text_frame
    tf_f1.margin_left = tf_f1.margin_top = tf_f1.margin_right = tf_f1.margin_bottom = 0
    add_para(tf_f1, "Research paper analysis • Based on published IEEE TCAD work", font_size=9.5, color=TEXT_MUTED)

    num_box = s1.shapes.add_textbox(Inches(12.0), Inches(6.8), Inches(0.5), Inches(0.3))
    tf_n = num_box.text_frame
    tf_n.margin_left = tf_n.margin_top = tf_n.margin_right = tf_n.margin_bottom = 0
    add_para(tf_n, "1", font_size=10, bold=True, color=TEXT_MUTED, align=PP_ALIGN.RIGHT)

    set_speaker_notes(s1, "Good morning/afternoon everyone. Today I am presenting 'ALVEARE: A Full-Stack Domain-Specific Framework for Regular Expressions', published in IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD) by researchers from Politecnico di Milano. Regular expressions are fundamental across network security, cloud telemetry, and bioinformatics, but they represent a massive computational bottleneck for modern hardware. This paper proposes a full-stack hardware-software co-design to resolve the efficiency vs flexibility dilemma.")

    # =========================================================================
    # SLIDE 2: 1. TOPIC OVERVIEW
    # =========================================================================
    s2 = prs.slides.add_slide(blank_slide_layout)
    add_bg(s2)
    add_header(s2, "1. Topic overview", "First, understand the computational problem the paper is trying to solve.", 2)

    card_w = Inches(3.64)
    card_h = Inches(4.0)
    tops = Inches(1.5)

    # Card 1: What are Regular Expressions?
    add_card(s2, Inches(0.8), tops, card_w, card_h)
    b1 = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), tops, card_w, Inches(0.08))
    b1.fill.solid()
    b1.fill.fore_color.rgb = BLUE_ACCENT
    b1.line.fill.background()

    tb = s2.shapes.add_textbox(Inches(1.05), Inches(1.75), card_w - Inches(0.5), card_h - Inches(0.4))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    add_para(tf, "Regular Expressions (REs)", font_size=16, bold=True, color=NAVY, space_after=8)
    add_para(tf, "Foundational pattern-matching language across modern computing systems:", font_size=11, color=TEXT_BODY, space_after=8)
    add_para(tf, "• Computer Security: Deep Packet Inspection (Snort, Zeek) and Antivirus scanning (ClamAV).\n• Personalized Medicine: Scanning genomic databases for DNA/RNA motifs and protein sequences.\n• Big Data & Logs: Real-time telemetry filtering and high-speed data ingestion.", font_size=10.5, color=TEXT_MUTED)

    # Card 2: The Core Challenge
    add_card(s2, Inches(4.84), tops, card_w, card_h)
    b2 = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(4.84), tops, card_w, Inches(0.08))
    b2.fill.solid()
    b2.fill.fore_color.rgb = CYAN_ACCENT
    b2.line.fill.background()

    tb = s2.shapes.add_textbox(Inches(5.09), Inches(1.75), card_w - Inches(0.5), card_h - Inches(0.4))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    add_para(tf, "The Hardware Bottleneck", font_size=16, bold=True, color=NAVY, space_after=8)
    add_para(tf, "Strict data dependencies and massive computational complexity:", font_size=11, color=TEXT_BODY, space_after=8)
    add_para(tf, "• Branch Divergence: Quantifiers (*, +, ?), repetitions {m,n}, and alternations (a|b) force constant backtracking.\n• Memory Bound: DFA representations suffer from exponential state explosion, overwhelming CPU caches.\n• CPU/GPU Penalties: General-purpose cores stall on serialization and memory latency at 100+ Gbps line rates.", font_size=10.5, color=TEXT_MUTED)

    # Card 3: The ALVEARE Solution
    add_card(s2, Inches(8.88), tops, card_w, card_h)
    b3 = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(8.88), tops, card_w, Inches(0.08))
    b3.fill.solid()
    b3.fill.fore_color.rgb = NAVY
    b3.line.fill.background()

    tb = s2.shapes.add_textbox(Inches(9.13), Inches(1.75), card_w - Inches(0.5), card_h - Inches(0.4))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    add_para(tf, "Domain-Specific Co-Design", font_size=16, bold=True, color=NAVY, space_after=8)
    add_para(tf, "Treating Regular Expressions as a first-class Domain-Specific Language (DSL):", font_size=11, color=TEXT_BODY, space_after=8)
    add_para(tf, "• Tailored 43-bit ISA: Purpose-built instructions handling character matching, ranges, and quantifiers.\n• Speculative Microarchitecture: Hardware-managed speculation stack eliminates CPU software backtracking.\n• Lightweight Compiler: Shifts structural complexity to compile-time software, keeping hardware lean and fast.", font_size=10.5, color=TEXT_MUTED)

    # Bottom Callout Box
    add_card(s2, Inches(0.8), Inches(5.75), Inches(11.73), Inches(1.05), fill_color=CALLOUT_BG, border_color=CALLOUT_BORDER)
    tb_c = s2.shapes.add_textbox(Inches(1.05), Inches(5.85), Inches(11.23), Inches(0.85))
    tf_c = tb_c.text_frame
    tf_c.word_wrap = True
    tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0
    add_para(tf_c, "Why it matters: Software engines (RE2, Hyperscan) are flexible but energy-intensive, while conventional hardware accelerators (ASICs/FPGAs) are fast but restricted to simple patterns. ALVEARE bridges this gap by uniting software flexibility with custom hardware efficiency.", font_size=11.5, bold=False, color=NAVY)

    set_speaker_notes(s2, "To understand ALVEARE, we first look at the landscape of regex matching. Modern applications require scanning incoming traffic at line rates (100 Gbps+) for thousands of complex patterns. Software engines running on general-purpose CPUs or GPUs suffer from branch divergence, cache thrashing, and high energy usage. Conversely, ASIC accelerators are hardwired and only support basic character matching. ALVEARE breaks this trade-off by treating regular expressions as a DSL with dedicated hardware primitives.")

    # =========================================================================
    # SLIDE 3: 2. RESEARCH GAP IDENTIFIED
    # =========================================================================
    s3 = prs.slides.add_slide(blank_slide_layout)
    add_bg(s3)
    add_header(s3, "2. Research Gap \u2013 Identified in the paper", "What existing regular expression workflows and hardware accelerators were missing.", 3)

    gaps = [
        ("1", "Efficiency vs. Flexibility Dilemma", "Software engines (RE2, PCRE) support broad operators but run slowly with high power; hardware accelerators (ASICs) are rigid and support only trivial subsets."),
        ("2", "Strict Data Dependencies & Backtracking", "Complex operators like greedy/lazy quantifiers and alternations induce severe branch divergence, causing massive pipeline stalls on CPUs and GPUs."),
        ("3", "Absence of Tailored RE ISAs", "General-purpose instruction sets (x86, ARM) require dozens of generic ALU cycles to process a single character set, range match, or repetition count."),
        ("4", "Automata Memory & State Explosion", "Converting modern REs into Deterministic Finite Automata (DFAs) leads to exponential state space explosion; NFA alternatives require complex interconnects."),
        ("5", "Line-Rate Energy Inefficiency", "Running 100+ Gbps network security inspection on server CPUs or SmartNIC DPUs consumes prohibitive amounts of energy and induces thermal throttling.")
    ]

    card_y = Inches(1.45)
    card_h = Inches(0.85)
    gap_spacing = Inches(0.96)

    for i, (num, title, desc) in enumerate(gaps):
        y = card_y + i * gap_spacing
        add_card(s3, Inches(0.8), y, Inches(11.73), card_h)

        nb = add_card(s3, Inches(0.95), y + Inches(0.15), Inches(0.55), Inches(0.55), fill_color=BADGE_BG, border_color=BADGE_BORDER)
        tb_num = s3.shapes.add_textbox(Inches(0.95), y + Inches(0.2), Inches(0.55), Inches(0.45))
        tf_n = tb_num.text_frame
        tf_n.margin_left = tf_n.margin_top = tf_n.margin_right = tf_n.margin_bottom = 0
        add_para(tf_n, num, font_size=16, bold=True, color=BLUE_ACCENT, align=PP_ALIGN.CENTER)

        tb_t = s3.shapes.add_textbox(Inches(1.65), y + Inches(0.12), Inches(10.6), Inches(0.65))
        tf_t = tb_t.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        add_para(tf_t, title, font_size=13, bold=True, color=NAVY, space_after=3)
        add_para(tf_t, desc, font_size=10.5, color=TEXT_BODY)

    add_card(s3, Inches(0.8), Inches(6.32), Inches(11.73), Inches(0.58), fill_color=CALLOUT_BG, border_color=CALLOUT_BORDER)
    tb_rg = s3.shapes.add_textbox(Inches(1.0), Inches(6.38), Inches(11.3), Inches(0.45))
    tf_rg = tb_rg.text_frame
    tf_rg.word_wrap = True
    tf_rg.margin_left = tf_rg.margin_top = tf_rg.margin_right = tf_rg.margin_bottom = 0
    add_para(tf_rg, "Research gap: A unified full-stack framework combining high-level regex expressiveness, fast compilation, and speculative line-rate hardware execution without exponential state explosion.", font_size=10.5, bold=True, color=NAVY)

    set_speaker_notes(s3, "Here we highlight the 5 key research gaps identified by the authors. Existing architectures force an unacceptable compromise: either you sacrifice throughput and energy efficiency with software engines, or you sacrifice operator expressiveness with fixed hardware accelerators. Moreover, converting complex regular expressions with bounded repetitions or lookarounds into DFAs causes exponential memory explosion. ALVEARE targets this gap directly.")

    # =========================================================================
    # SLIDE 4: 3. PROBLEM STATEMENT
    # =========================================================================
    s4 = prs.slides.add_slide(blank_slide_layout)
    add_bg(s4)
    add_header(s4, "3. Problem Statement", "The core research question and architectural trade-off addressed by the authors.", 4)

    # Core Problem Banner
    add_card(s4, Inches(0.8), Inches(1.45), Inches(11.73), Inches(0.95), fill_color=NAVY)
    tb_prob = s4.shapes.add_textbox(Inches(1.1), Inches(1.55), Inches(11.1), Inches(0.75))
    tf_p = tb_prob.text_frame
    tf_p.word_wrap = True
    tf_p.margin_left = tf_p.margin_top = tf_p.margin_right = tf_p.margin_bottom = 0
    add_para(tf_p, "Core Question: How can regular expression matching overcome the efficiency vs. flexibility trade-off to provide high throughput and energy efficiency while preserving full support for complex, real-world regex operators?", font_size=13.5, bold=True, color=RGBColor(255, 255, 255))

    col_w = Inches(5.72)
    col_h = Inches(3.45)
    col_y = Inches(2.55)

    # Traditional Workflow
    add_card(s4, Inches(0.8), col_y, col_w, col_h)
    bar_trad = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), col_y, col_w, Inches(0.08))
    bar_trad.fill.solid()
    bar_trad.fill.fore_color.rgb = RGBColor(239, 68, 68)
    bar_trad.line.fill.background()

    tb_t = s4.shapes.add_textbox(Inches(1.05), col_y + Inches(0.18), col_w - Inches(0.5), col_h - Inches(0.3))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
    add_para(tf_t, "Traditional Workflows", font_size=15, bold=True, color=NAVY, space_after=6)
    add_para(tf_t, "Path A: General-Purpose Software (RE2, PCRE, Hyperscan)\n• High operator flexibility, but CPU/GPU thread divergence stalls throughput.\n• DFAs cause memory explosion; NFAs require costly pointer chasing.", font_size=10, color=TEXT_BODY, space_after=8)
    add_para(tf_t, "Path B: Fixed Hardware Accelerators (Rigid ASICs)\n• High throughput, but restricted to simple character matches.\n• Inflexible: modifying expressions requires full FPGA/ASIC resynthesis.", font_size=10, color=TEXT_BODY, space_after=8)
    add_para(tf_t, "Risk: Severe trade-off between operator support and line-rate performance.", font_size=10, bold=True, color=RGBColor(185, 28, 28))

    # Proposed Workflow (ALVEARE)
    add_card(s4, Inches(6.81), col_y, col_w, col_h)
    bar_prop = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.81), col_y, col_w, Inches(0.08))
    bar_prop.fill.solid()
    bar_prop.fill.fore_color.rgb = BLUE_ACCENT
    bar_prop.line.fill.background()

    tb_pr = s4.shapes.add_textbox(Inches(7.06), col_y + Inches(0.18), col_w - Inches(0.5), col_h - Inches(0.3))
    tf_pr = tb_pr.text_frame
    tf_pr.word_wrap = True
    tf_pr.margin_left = tf_pr.margin_top = tf_pr.margin_right = tf_pr.margin_bottom = 0
    add_para(tf_pr, "Proposed ALVEARE Workflow", font_size=15, bold=True, color=NAVY, space_after=6)
    add_para(tf_pr, "1. DSL Treatment: Treat regular expressions as a domain-specific language.\n2. Ad-hoc Compiler: Parse and optimize ASTs, emitting 43-bit RISC code in O(N).\n3. Speculative Microarchitecture: Single-cycle hardware rollback via on-chip stack.\n4. Scalable DSA: Multi-core execution scaling from 1 to 10+ cores on FPGA.", font_size=10, color=TEXT_BODY, space_after=10)
    add_para(tf_pr, "Advantage: Full operator flexibility with custom silicon speed & efficiency.", font_size=10, bold=True, color=BLUE_ACCENT)

    # Bottom Objective Box
    add_card(s4, Inches(0.8), Inches(6.18), Inches(11.73), Inches(0.72), fill_color=CALLOUT_BG, border_color=CALLOUT_BORDER)
    tb_ob = s4.shapes.add_textbox(Inches(1.0), Inches(6.26), Inches(11.3), Inches(0.55))
    tf_ob = tb_ob.text_frame
    tf_ob.word_wrap = True
    tf_ob.margin_left = tf_ob.margin_top = tf_ob.margin_right = tf_ob.margin_bottom = 0
    add_para(tf_ob, "Objective: Shift structural complexity from hardware to software, creating a lightweight speculative DSA that achieves up to 34x speedup and 57x energy savings while retaining broad operator support.", font_size=11, bold=True, color=NAVY)

    set_speaker_notes(s4, "The core problem statement contrasts traditional workflows against ALVEARE. Traditional workflows make you choose between software flexibility or ASIC performance. ALVEARE proposes a third way: an ad-hoc compiler compiles regexes into a specialized 43-bit RISC instruction stream, while a speculative hardware engine executes instructions with dedicated hardware backtracking. This shifts structural complexity to software and keeps the hardware tiny and scalable.")

    # =========================================================================
    # SLIDE 5: 4. METHODS USED IN THE PAPER
    # =========================================================================
    s5 = prs.slides.add_slide(blank_slide_layout)
    add_bg(s5)
    add_header(s5, "4. Methods used in the paper to implement the research gap", "A full-stack hardware-software co-design spanning benchmarks, compiler, ISA, and microarchitecture.", 5)

    methods = [
        ("Benchmark Operator Analysis", "Quantitatively analyzed 6 benchmark suites (ANMLZoo: Snort, PowerEN, Protomata; Brill, ClamAV, Dotstar) to profile real-world operator frequencies."),
        ("43-bit RISC-based RE ISA", "Custom 43-bit instruction set with 3 classes: Control (branches/loops), Base (single char/wildcard), and Complex (classes, ranges, quantifiers)."),
        ("Speculative Microarchitecture", "Speculation engine with on-chip Speculation Stack that checkpoints states, handling greedy/lazy backtracking without CPU intervention."),
        ("3 Decode Units & Vector Compute", "Parallel front-end featuring 3 decode units dispatching instructions simultaneously to Vector Compute Units (VCUs) for multi-character evaluations."),
        ("Ad-Hoc Optimizing C Compiler", "Written in C (FLEX/BISON). Translates ASTs into optimized 43-bit machine code with linear O(N) time and space complexity, eliminating state explosion."),
        ("Multi-Core FPGA Prototyping", "Synthesized in VHDL on an Avnet Ultra96v2 FPGA (Xilinx ZU3EG MPSoC) at 300 MHz, linearly scaling from 1 to 10 independent cores.")
    ]

    card_w = Inches(3.64)
    card_h = Inches(2.1)
    xs = [Inches(0.8), Inches(4.84), Inches(8.88)]
    ys = [Inches(1.5), Inches(3.85)]

    for idx, (title, desc) in enumerate(methods):
        x = xs[idx % 3]
        y = ys[idx // 3]

        add_card(s5, x, y, card_w, card_h)

        ind = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, card_w, Inches(0.06))
        ind.fill.solid()
        ind.fill.fore_color.rgb = BLUE_ACCENT if idx % 2 == 0 else CYAN_ACCENT
        ind.line.fill.background()

        tb = s5.shapes.add_textbox(x + Inches(0.2), y + Inches(0.15), card_w - Inches(0.4), card_h - Inches(0.25))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        add_para(tf, title, font_size=12.5, bold=True, color=NAVY, space_after=6)
        add_para(tf, desc, font_size=9.5, color=TEXT_BODY)

    add_card(s5, Inches(0.8), Inches(6.18), Inches(11.73), Inches(0.72), fill_color=HIGHLIGHT_BG, border_color=CARD_BORDER)
    tb_imp = s5.shapes.add_textbox(Inches(1.0), Inches(6.26), Inches(11.3), Inches(0.55))
    tf_imp = tb_imp.text_frame
    tf_imp.word_wrap = True
    tf_imp.margin_left = tf_imp.margin_top = tf_imp.margin_right = tf_imp.margin_bottom = 0
    add_para(tf_imp, "Hardware-Software Co-Design Principle: Lifting structural complexity to the compiler keeps the hardware core lightweight and fast, enabling multi-core scalability on low-cost FPGA silicon.", font_size=10.5, bold=True, color=NAVY)

    set_speaker_notes(s5, "Here are the six pillars of the methodology. First, the authors performed a quantitative analysis across 6 benchmark suites from ANMLZoo to determine which operators are actually used in practice. Second, they defined a 43-bit RISC ISA divided into Control, Base, and Complex operations. Third, they designed a speculative microarchitecture with an on-chip Speculation Stack for zero-latency rollback. Fourth, they built 3 decode units coupled with Vector Compute Units. Fifth, they wrote an ad-hoc C compiler that operates in linear time O(N). Finally, they prototyped everything on an FPGA running at 300 MHz across 1 to 10 cores.")

    # =========================================================================
    # SLIDE 6: 5. INPUT TO THE PROPOSED METHOD
    # =========================================================================
    s6 = prs.slides.add_slide(blank_slide_layout)
    add_bg(s6)
    add_header(s6, "5. Input to the proposed method", "What information and datasets enter the ALVEARE framework?", 6)

    col_w = Inches(3.64)
    col_h = Inches(3.25)
    tops = Inches(1.5)

    # Input A
    add_card(s6, Inches(0.8), tops, col_w, col_h)
    add_card(s6, Inches(1.0), tops + Inches(0.18), Inches(1.2), Inches(0.32), fill_color=BADGE_BG, border_color=BADGE_BORDER)
    tb = s6.shapes.add_textbox(Inches(1.0), tops + Inches(0.22), Inches(1.2), Inches(0.28))
    tf = tb.text_frame
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    add_para(tf, "Input A", font_size=10.5, bold=True, color=BLUE_ACCENT, align=PP_ALIGN.CENTER)

    tb_a = s6.shapes.add_textbox(Inches(1.0), tops + Inches(0.6), col_w - Inches(0.4), col_h - Inches(0.7))
    tf_a = tb_a.text_frame
    tf_a.word_wrap = True
    tf_a.margin_left = tf_a.margin_top = tf_a.margin_right = tf_a.margin_bottom = 0
    add_para(tf_a, "Regular Expression Rules", font_size=14, bold=True, color=NAVY, space_after=6)
    add_para(tf_a, "• Syntax: PCRE/POSIX regular expression rulesets.\n• Complex Operators: Character classes [a-z], sets, bounds {m,n}, greedy & lazy quantifiers (*, +, ?).\n• Benchmark Rules: 200 randomly selected patterns each from Snort, Protomata, and PowerEN.", font_size=10, color=TEXT_BODY)

    # Input B
    add_card(s6, Inches(4.84), tops, col_w, col_h)
    add_card(s6, Inches(5.04), tops + Inches(0.18), Inches(1.2), Inches(0.32), fill_color=BADGE_BG, border_color=BADGE_BORDER)
    tb = s6.shapes.add_textbox(Inches(5.04), tops + Inches(0.22), Inches(1.2), Inches(0.28))
    tf = tb.text_frame
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    add_para(tf, "Input B", font_size=10.5, bold=True, color=BLUE_ACCENT, align=PP_ALIGN.CENTER)

    tb_b = s6.shapes.add_textbox(Inches(5.04), tops + Inches(0.6), col_w - Inches(0.4), col_h - Inches(0.7))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = 0
    add_para(tf_b, "Target Data Streams", font_size=14, bold=True, color=NAVY, space_after=6)
    add_para(tf_b, "• Streaming Data: Raw unstructured byte streams inspected in real time.\n• Standardized Input: 1 MB benchmark payload files per test suite.\n• Block Chunking: Processed in 16 KB chunks matching on-chip memory buffers.", font_size=10, color=TEXT_BODY)

    # Input C
    add_card(s6, Inches(8.88), tops, col_w, col_h)
    add_card(s6, Inches(9.08), tops + Inches(0.18), Inches(1.2), Inches(0.32), fill_color=BADGE_BG, border_color=BADGE_BORDER)
    tb = s6.shapes.add_textbox(Inches(9.08), tops + Inches(0.22), Inches(1.2), Inches(0.28))
    tf = tb.text_frame
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    add_para(tf, "Input C", font_size=10.5, bold=True, color=BLUE_ACCENT, align=PP_ALIGN.CENTER)

    tb_c = s6.shapes.add_textbox(Inches(9.08), tops + Inches(0.6), col_w - Inches(0.4), col_h - Inches(0.7))
    tf_c = tb_c.text_frame
    tf_c.word_wrap = True
    tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0
    add_para(tf_c, "Architecture Config", font_size=14, bold=True, color=NAVY, space_after=6)
    add_para(tf_c, "• Hardware Allocation: 1 to 10 processing cores active on FPGA.\n• Hardware Constraints: Max reference width (four 8-bit chars) and counters (0 to 62).\n• Speculation Parameters: Stack depth configuring speculation limits and rollback.", font_size=10, color=TEXT_BODY)

    # Mini Example Box
    add_card(s6, Inches(0.8), Inches(4.95), Inches(11.73), Inches(1.85), fill_color=HIGHLIGHT_BG, border_color=CARD_BORDER)
    tb_ex = s6.shapes.add_textbox(Inches(1.05), Inches(5.1), Inches(11.23), Inches(1.55))
    tf_ex = tb_ex.text_frame
    tf_ex.word_wrap = True
    tf_ex.margin_left = tf_ex.margin_top = tf_ex.margin_right = tf_ex.margin_bottom = 0
    add_para(tf_ex, "Concrete Mini-Example:", font_size=12.5, bold=True, color=NAVY, space_after=4)
    add_para(tf_ex, "• Input RE: \"/api/v[0-9]{1,2}/[a-z]+(\\.json|\\.xml)\" (combines character classes, bounded repetition, alternation, and quantifiers)\n• Target Stream: 16 KB network packet payload arriving from an Ethernet interface into FPGA BRAM buffers.\n• Hardware Target: 4-core ALVEARE deployment running at 300 MHz on Xilinx Zynq UltraScale+ MPSoC.", font_size=10.5, color=TEXT_BODY)

    set_speaker_notes(s6, "Slide 6 defines the three inputs entering the ALVEARE framework: Input A is the regular expression ruleset containing complex features like character classes and quantifiers. Input B is the target data stream—in this paper, 1 MB files chunked into 16 KB blocks. Input C represents architectural configuration, including core count (1 to 10 cores) and speculation stack depth. The concrete example at the bottom demonstrates an API routing regex pattern being scanned across network payload packets.")

    # =========================================================================
    # SLIDE 7: 6. OUTPUT OF THE PROPOSED METHOD
    # =========================================================================
    s7 = prs.slides.add_slide(blank_slide_layout)
    add_bg(s7)
    add_header(s7, "6. Output of the proposed method", "The framework produces optimized machine code, precise match telemetry, and high energy efficiency.", 7)

    outputs = [
        ("1", "Compiled 43-bit Machine Code", "Compact RISC-based binary instructions directly loadable into the processor's on-chip instruction memory, completely avoiding DFA state explosion."),
        ("2", "Exact Match Flags & Offsets", "Real-time boolean match signals accompanied by exact start and end byte coordinates of matching patterns within the streaming input buffer."),
        ("3", "Line-Rate Acceleration Metrics", "Demonstrated execution speedup of up to 34x over CPU/DPU software solutions (RE2 on ARM A53, NVIDIA BlueField-2) and 356x faster than GPU implementations."),
        ("4", "Ultra-Low Energy Dissipation", "Significant energy efficiency improvement of up to 57x (Joules per processed MB) compared to server CPUs, GPUs, and embedded SoC matchers."),
        ("5", "Multi-Core Scale-Out Telemetry", "Comprehensive hardware metrics including total execution clock cycles, speculation stack peak depth, and core-by-core utilization across 1 to 10 cores.")
    ]

    card_y = Inches(1.45)
    card_h = Inches(0.85)
    gap_spacing = Inches(0.96)

    for i, (num, title, desc) in enumerate(outputs):
        y = card_y + i * gap_spacing
        add_card(s7, Inches(0.8), y, Inches(11.73), card_h)

        nb = add_card(s7, Inches(0.95), y + Inches(0.15), Inches(0.55), Inches(0.55), fill_color=BADGE_BG, border_color=BADGE_BORDER)
        tb_num = s7.shapes.add_textbox(Inches(0.95), y + Inches(0.2), Inches(0.55), Inches(0.45))
        tf_n = tb_num.text_frame
        tf_n.margin_left = tf_n.margin_top = tf_n.margin_right = tf_n.margin_bottom = 0
        add_para(tf_n, num, font_size=16, bold=True, color=BLUE_ACCENT, align=PP_ALIGN.CENTER)

        tb_t = s7.shapes.add_textbox(Inches(1.65), y + Inches(0.12), Inches(10.6), Inches(0.65))
        tf_t = tb_t.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        add_para(tf_t, title, font_size=13, bold=True, color=NAVY, space_after=3)
        add_para(tf_t, desc, font_size=10.5, color=TEXT_BODY)

    add_card(s7, Inches(0.8), Inches(6.32), Inches(11.73), Inches(0.58), fill_color=CALLOUT_BG, border_color=CALLOUT_BORDER)
    tb_out = s7.shapes.add_textbox(Inches(1.0), Inches(6.38), Inches(11.3), Inches(0.45))
    tf_out = tb_out.text_frame
    tf_out.word_wrap = True
    tf_out.margin_left = tf_out.margin_top = tf_out.margin_right = tf_out.margin_bottom = 0
    add_para(tf_out, "Output Highlights: Real-time pattern detection at 300 MHz with deterministic memory consumption, instant sub-millisecond compilation, and zero state explosion.", font_size=10.5, bold=True, color=NAVY)

    set_speaker_notes(s7, "The output of ALVEARE is far richer than just a boolean match flag. It provides compact 43-bit binary code generated in linear time, exact byte offset coordinates for matched strings, up to 34x speedup over ARM and DPU processors, up to 57x higher energy efficiency, and full multi-core performance telemetry. This provides both high-speed matching and deep diagnostic visibility.")

    # =========================================================================
    # SLIDE 8: 7. STEPS INVOLVED IN THE PROPOSED METHOD
    # =========================================================================
    s8 = prs.slides.add_slide(blank_slide_layout)
    add_bg(s8)
    add_header(s8, "7. Steps involved in the proposed method to convert given input into output", "The end-to-end flow from high-level regular expression to hardware match detection.", 8)

    steps = [
        ("1", "Parse RE Syntax", "FLEX lexer & BISON parser convert PCRE expressions into an Abstract Syntax Tree (AST)."),
        ("2", "Optimize AST", "AST simplification, merging character ranges and pruning redundant sub-expressions."),
        ("3", "Emit 43-bit Binary", "C compiler generates custom RISC machine code in linear time & space O(N)."),
        ("4", "Load Instructions", "Binary program loaded into FPGA on-chip instruction memory (BRAM)."),
        ("5", "Stream Target Data", "16 KB payload chunks streamed into hardware input buffers via AXI interfaces."),
        ("6", "3-Way Decode", "3 Decode Units dispatch instructions in parallel to Vector Compute Units (VCUs)."),
        ("7", "Speculative Match", "Speculation Stack checkpoints states during quantifiers/alternations; auto-backtracks on mismatch."),
        ("8", "Report Match Results", "Hardware asserts match flag, outputs start/end byte offsets, and advances stream.")
    ]

    card_w = Inches(2.72)
    card_h = Inches(1.8)
    xs = [Inches(0.8), Inches(3.79), Inches(6.78), Inches(9.77)]
    ys = [Inches(1.45), Inches(3.45)]

    for idx, (num, title, desc) in enumerate(steps):
        x = xs[idx % 4]
        y = ys[idx // 4]

        add_card(s8, x, y, card_w, card_h)

        add_card(s8, x + Inches(0.12), y + Inches(0.12), Inches(0.38), Inches(0.38), fill_color=BADGE_BG, border_color=BADGE_BORDER)
        tb_num = s8.shapes.add_textbox(x + Inches(0.12), y + Inches(0.15), Inches(0.38), Inches(0.32))
        tf_n = tb_num.text_frame
        tf_n.margin_left = tf_n.margin_top = tf_n.margin_right = tf_n.margin_bottom = 0
        add_para(tf_n, num, font_size=12, bold=True, color=BLUE_ACCENT, align=PP_ALIGN.CENTER)

        tb_t = s8.shapes.add_textbox(x + Inches(0.58), y + Inches(0.12), card_w - Inches(0.7), card_h - Inches(0.2))
        tf_t = tb_t.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        add_para(tf_t, title, font_size=11.5, bold=True, color=NAVY, space_after=3)
        add_para(tf_t, desc, font_size=9.5, color=TEXT_BODY)

    add_card(s8, Inches(0.8), Inches(5.45), Inches(5.72), Inches(1.35), fill_color=CALLOUT_BG, border_color=CALLOUT_BORDER)
    tb_c1 = s8.shapes.add_textbox(Inches(1.0), Inches(5.55), Inches(5.3), Inches(1.15))
    tf_c1 = tb_c1.text_frame
    tf_c1.word_wrap = True
    tf_c1.margin_left = tf_c1.margin_top = tf_c1.margin_right = tf_c1.margin_bottom = 0
    add_para(tf_c1, "Hardware Backtracking Mechanism:", font_size=11, bold=True, color=NAVY, space_after=3)
    add_para(tf_c1, "When a speculative branch fails, the core restores previous character pointers and state in a single clock cycle directly from the Speculation Stack, eliminating software interrupt latency.", font_size=9.5, color=TEXT_BODY)

    add_card(s8, Inches(6.81), Inches(5.45), Inches(5.72), Inches(1.35), fill_color=HIGHLIGHT_BG, border_color=CARD_BORDER)
    tb_c2 = s8.shapes.add_textbox(Inches(7.01), Inches(5.55), Inches(5.3), Inches(1.15))
    tf_c2 = tb_c2.text_frame
    tf_c2.word_wrap = True
    tf_c2.margin_left = tf_c2.margin_top = tf_c2.margin_right = tf_c2.margin_bottom = 0
    add_para(tf_c2, "Linear-Time Compilation Pipeline:", font_size=11, bold=True, color=NAVY, space_after=3)
    add_para(tf_c2, "Unlike DFAs which suffer catastrophic exponential memory growth during compilation, ALVEARE compiles in O(N) linear time and space, enabling fast dynamic rule loading at runtime.", font_size=9.5, color=TEXT_BODY)

    set_speaker_notes(s8, "This slide maps out the complete 8-step pipeline converting regular expressions and streaming text into match results. Steps 1 through 3 execute in the custom C compiler: parsing with FLEX/BISON, optimizing the AST, and generating 43-bit binary instructions in linear time. Steps 4 through 8 execute on the FPGA hardware: instructions and data are loaded, 3 decode units dispatch instructions to vector compute units, and the speculation stack manages rollbacks in hardware. The entire pipeline operates with zero CPU runtime overhead.")

    # =========================================================================
    # SLIDE 9: EVALUATION: WHAT DID THE AUTHORS FIND?
    # =========================================================================
    s9 = prs.slides.add_slide(blank_slide_layout)
    add_bg(s9)
    add_header(s9, "Evaluation: what did the authors find?", "Benchmarking against state-of-the-art CPU, GPU, DPU, and server engines on ANMLZoo.", 9)

    rows = 6
    cols = 5
    table_shape = s9.shapes.add_table(rows, cols, Inches(0.8), Inches(1.45), Inches(11.73), Inches(2.7))
    table = table_shape.table

    table.columns[0].width = Inches(3.2)
    table.columns[1].width = Inches(2.1)
    table.columns[2].width = Inches(2.2)
    table.columns[3].width = Inches(2.1)
    table.columns[4].width = Inches(2.13)

    headers = ["System / Engine", "Speedup vs Baseline", "Energy Efficiency Gain", "Compilation Time", "Operator Support"]
    table_data = [
        ["ALVEARE (1-10 Cores @ 300MHz, FPGA)", "Up to 34x faster", "17x \u2013 57x higher", "Sub-millisecond (Linear)", "Broad (Classes, Quantifiers, Bounds)"],
        ["Google RE2 (ARM Cortex-A53 SoC)", "1.0x (Baseline CPU)", "1.0x (Baseline)", "Fast (Software AST)", "Broad PCRE/POSIX"],
        ["NVIDIA BlueField-2 DPU (Data Center)", "0.8x \u2013 1.8x", "2.1x \u2013 3.4x", "Moderate", "Broad PCRE/POSIX"],
        ["GPU-based Matchers (NVIDIA CUDA)", "0.05x \u2013 0.1x (356x Slower)", "Poor (High Wattage)", "High (Kernel compilation)", "Restricted (Severe divergence)"],
        ["Intel Hyperscan (Intel Xeon Server)", "Competitive Throughput", "15x \u2013 25x Worse Power", "High (Heavy DFA/NFA build)", "Restricted complex quantifiers"]
    ]

    for col_idx, header in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.text = header
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY
        for p in cell.text_frame.paragraphs:
            p.font.name = "Segoe UI"
            p.font.size = Pt(11)
            p.font.bold = True
            p.font.color.rgb = RGBColor(255, 255, 255)
            p.alignment = PP_ALIGN.CENTER if col_idx > 0 else PP_ALIGN.LEFT

    for row_idx, row_values in enumerate(table_data):
        for col_idx, val in enumerate(row_values):
            cell = table.cell(row_idx + 1, col_idx)
            cell.text = val
            cell.fill.solid()
            if row_idx == 0:
                cell.fill.fore_color.rgb = BADGE_BG
            elif row_idx % 2 == 1:
                cell.fill.fore_color.rgb = CARD_BG
            else:
                cell.fill.fore_color.rgb = HIGHLIGHT_BG
            for p in cell.text_frame.paragraphs:
                p.font.name = "Segoe UI"
                p.font.size = Pt(10)
                if row_idx == 0:
                    p.font.bold = True
                    p.font.color.rgb = BLUE_ACCENT if col_idx > 0 else NAVY
                else:
                    p.font.color.rgb = TEXT_BODY
                p.alignment = PP_ALIGN.CENTER if col_idx > 0 else PP_ALIGN.LEFT

    add_card(s9, Inches(0.8), Inches(4.35), Inches(5.72), Inches(2.45), fill_color=CALLOUT_BG, border_color=CALLOUT_BORDER)
    tb_int = s9.shapes.add_textbox(Inches(1.05), Inches(4.45), Inches(5.2), Inches(2.25))
    tf_int = tb_int.text_frame
    tf_int.word_wrap = True
    tf_int.margin_left = tf_int.margin_top = tf_int.margin_right = tf_int.margin_bottom = 0
    add_para(tf_int, "Key Experimental Findings:", font_size=12.5, bold=True, color=NAVY, space_after=4)
    add_para(tf_int, "• Up to 34x Speedup: Over embedded CPUs and DPU SmartNICs, scaling linearly with core count.\n• At least 356x Faster than GPUs: Eliminates thread serialization caused by warp divergence.\n• 17x to 57x Energy Gain: Consumes a fraction of the power of Xeon servers and DPUs.\n• Zero State Explosion: Compiles rulesets instantly without memory explosion.", font_size=10, color=TEXT_BODY)

    add_card(s9, Inches(6.81), Inches(4.35), Inches(5.72), Inches(2.45), fill_color=HIGHLIGHT_BG, border_color=CARD_BORDER)
    tb_lim = s9.shapes.add_textbox(Inches(7.06), Inches(4.45), Inches(5.2), Inches(2.25))
    tf_lim = tb_lim.text_frame
    tf_lim.word_wrap = True
    tf_lim.margin_left = tf_lim.margin_top = tf_lim.margin_right = tf_lim.margin_bottom = 0
    add_para(tf_lim, "Identified Architectural Limitations:", font_size=12.5, bold=True, color=NAVY, space_after=4)
    add_para(tf_lim, "• Hardware Boundaries: Reference holds a maximum of four 8-bit characters; repetition counters limited to 0\u201362.\n• Deep Rulesets: Huge rulesets require time-multiplexing across FPGA reconfiguration.\n• Single Comparator Active: Only one comparator active after partial match.\n• ReDoS Vulnerability: Pathological nested expressions can trigger algorithmic backtracking collapse without compiler guardrails.", font_size=10, color=TEXT_BODY)

    set_speaker_notes(s9, "Turning to experimental results: The authors benchmarked ALVEARE using ANMLZoo workloads (Snort, PowerEN, Protomata) following the YARB methodology. ALVEARE delivers up to 34x speedup and 17x to 57x energy efficiency gains over ARM Cortex-A53 and NVIDIA BlueField-2 DPUs. It is at least 356x faster than GPUs, which struggle catastrophically with warp serialization during backtracking. Compared to Intel Hyperscan on server Xeons, ALVEARE achieves competitive throughput while requiring far less power and compiling in linear time. The authors also candidly document architectural limitations: 4-character references, counters limited to 62, and ReDoS vulnerability.")

    # =========================================================================
    # SLIDE 10: CONCLUSION AND KEY TAKEAWAYS
    # =========================================================================
    s10 = prs.slides.add_slide(blank_slide_layout)
    add_bg(s10)
    add_header(s10, "Conclusion and key takeaway", "What should the audience remember about the ALVEARE framework?", 10)

    card_w = Inches(3.64)
    card_h = Inches(3.0)
    tops = Inches(1.5)

    # Card 1: Research Contribution
    add_card(s10, Inches(0.8), tops, card_w, card_h)
    tb = s10.shapes.add_textbox(Inches(1.05), tops + Inches(0.18), card_w - Inches(0.5), card_h - Inches(0.3))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    add_para(tf, "Research Contribution", font_size=15, bold=True, color=NAVY, space_after=6)
    add_para(tf, "• Proposed the first full-stack domain-specific framework for regular expressions.\n• Introduced a tailored 43-bit RISC ISA supporting base and complex operators.\n• Implemented a speculative microarchitecture with on-chip stack.\n• Built an ad-hoc linear-time optimizing compiler in C.", font_size=10, color=TEXT_BODY)

    # Card 2: Practical Engineering Value
    add_card(s10, Inches(4.84), tops, card_w, card_h)
    tb = s10.shapes.add_textbox(Inches(5.09), tops + Inches(0.18), card_w - Inches(0.5), card_h - Inches(0.3))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    add_para(tf, "Practical Value", font_size=15, bold=True, color=NAVY, space_after=6)
    add_para(tf, "• Resolves the dilemma between software flexibility and ASIC rigidity.\n• Delivers up to 34x speedup and 57x energy savings over CPU/DPU engines.\n• Unlocks line-rate deep packet inspection (Snort) and genomics at low power.\n• Linear O(N) compile time eliminates DFA memory blowup.", font_size=10, color=TEXT_BODY)

    # Card 3: Limitations & Future Work
    add_card(s10, Inches(8.88), tops, card_w, card_h)
    tb = s10.shapes.add_textbox(Inches(9.13), tops + Inches(0.18), card_w - Inches(0.5), card_h - Inches(0.3))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    add_para(tf, "Critical Limitations", font_size=15, bold=True, color=NAVY, space_after=6)
    add_para(tf, "• Reference width fixed at four 8-bit characters; counters capped at 0\u201362.\n• Very large rulesets require dynamic FPGA time-multiplexing.\n• Susceptible to algorithmic ReDoS if expressions have catastrophic nested quantifiers.\n• Future work: wider counters and compiler-level ReDoS guardrails.", font_size=10, color=TEXT_BODY)

    # One Sentence Summary Box
    add_card(s10, Inches(0.8), Inches(4.75), Inches(11.73), Inches(1.3), fill_color=CALLOUT_BG, border_color=CALLOUT_BORDER)
    tb_sum = s10.shapes.add_textbox(Inches(1.05), Inches(4.88), Inches(11.23), Inches(1.05))
    tf_sum = tb_sum.text_frame
    tf_sum.word_wrap = True
    tf_sum.margin_left = tf_sum.margin_top = tf_sum.margin_right = tf_sum.margin_bottom = 0
    add_para(tf_sum, "One-Sentence Summary:", font_size=11.5, bold=True, color=NAVY, space_after=4)
    add_para(tf_sum, "ALVEARE proves that treating Regular Expressions as a domain-specific language paired with a custom 43-bit RISC ISA, a speculative microarchitecture, and an optimizing compiler delivers line-rate matching and up to 57x energy efficiency without sacrificing operator flexibility.", font_size=11, color=TEXT_BODY)

    # Source Attribution Box (Concise & well fitted)
    tb_src = s10.shapes.add_textbox(Inches(0.8), Inches(6.25), Inches(11.73), Inches(0.4))
    tf_src = tb_src.text_frame
    tf_src.word_wrap = True
    tf_src.margin_left = tf_src.margin_top = tf_src.margin_right = tf_src.margin_bottom = 0
    add_para(tf_src, "Source: Carloni et al., \"ALVEARE: A Full-Stack Domain-Specific Framework for Regular Expressions\", IEEE Transactions on Computer-Aided Design (TCAD).", font_size=9.5, color=TEXT_MUTED)

    set_speaker_notes(s10, "In conclusion, ALVEARE represents a major milestone in domain-specific acceleration for regular expressions. By treating regexes as a DSL, the authors successfully combined the best of both worlds: software-like operator expressiveness with hardware-grade speed and efficiency. The one-sentence takeaway to remember is that co-designing an ISA and compiler with a speculative microarchitecture is the key to solving line-rate pattern matching bottlenecks.")

    # =========================================================================
    # SLIDE 11: QUICK EXPLANATION / SPEAKER NOTES
    # =========================================================================
    s11 = prs.slides.add_slide(blank_slide_layout)
    add_bg(s11)
    add_header(s11, "Quick explanation / speaker notes", "Use these concise explanations and talking points while delivering your presentation.", 11)

    notes = [
        ("What is a Domain-Specific Architecture (DSA) in this context?",
         "A DSA is hardware customized specifically for a narrow domain—in this case, regular expression primitives (character classes, ranges, repetition counters) rather than general-purpose math. It avoids instruction decoding overhead and directly evaluates regex tokens in silicon."),

        ("Why do CPUs and GPUs struggle with regular expression matching?",
         "Regular expressions contain non-deterministic branches (greedy quantifiers, alternations). When a match fails, the engine must backtrack. On GPUs, this creates severe thread warp divergence where parallel lanes serialize. On CPUs, it causes cache thrashing and branch mispredictions."),

        ("How does ALVEARE's speculative microarchitecture avoid performance collapse?",
         "ALVEARE speculates that greedy paths succeed while pushing alternative checkpoints onto an on-chip Speculation Stack. If a character mismatch occurs, the controller pops the previous state in a single clock cycle, avoiding costly software interrupt routines or DFA state explosions."),

        ("Why does lifting complexity to the compiler help the hardware?",
         "Compilers can analyze ASTs, merge character ranges, and eliminate dead branches ahead of time in software. This keeps the hardware core tiny (fitting up to 10+ cores on a budget FPGA) and allows compilation in linear time O(N), unlike DFAs which experience exponential graph explosions.")
    ]

    card_y = Inches(1.45)
    card_h = Inches(1.05)
    note_spacing = Inches(1.15)

    for i, (q, a) in enumerate(notes):
        y = card_y + i * note_spacing
        add_card(s11, Inches(0.8), y, Inches(11.73), card_h)

        tb = s11.shapes.add_textbox(Inches(1.05), y + Inches(0.12), Inches(11.23), card_h - Inches(0.2))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        add_para(tf, q, font_size=12.5, bold=True, color=BLUE_ACCENT, space_after=3)
        add_para(tf, a, font_size=10.5, color=TEXT_BODY)

    add_card(s11, Inches(0.8), Inches(6.15), Inches(11.73), Inches(0.75), fill_color=CALLOUT_BG, border_color=CALLOUT_BORDER)
    tb_sc = s11.shapes.add_textbox(Inches(1.05), Inches(6.25), Inches(11.23), Inches(0.55))
    tf_sc = tb_sc.text_frame
    tf_sc.word_wrap = True
    tf_sc.margin_left = tf_sc.margin_top = tf_sc.margin_right = tf_sc.margin_bottom = 0
    add_para(tf_sc, "Suggested Closing Remark:", font_size=11, bold=True, color=NAVY, space_after=2)
    add_para(tf_sc, "\"ALVEARE demonstrates that by treating regular expressions as a domain-specific programming language, we can achieve custom-silicon speeds and up to 57x energy efficiency while retaining the rich operator expressiveness required by modern cybersecurity and bioinformatics.\"", font_size=10.5, color=TEXT_BODY)

    set_speaker_notes(s11, "This final slide provides quick Q&A reference cards for the presentation Q&A session. Key concepts covered include what a DSA is, why GPUs diverge on regex matching, how the speculation stack works, and why linear-time compilation prevents DFA explosion. The suggested closing remark provides an impactful concluding statement.")

    prs.save(filename)
    print(f"Presentation successfully created and saved to {filename}")

if __name__ == "__main__":
    create_deck("c:/Users/Jashith Masand/Desktop/CN/ALVEARE_Research_Paper_Presentation.pptx")
