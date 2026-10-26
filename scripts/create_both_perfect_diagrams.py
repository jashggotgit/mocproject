import math

def create_style1_alveare(filename):
    # Image 1 Clone: 1400 x 780
    svg = []
    svg.append('<?xml version="1.0" encoding="UTF-8" standalone="no"?>')
    svg.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 780" width="1400" height="780">')
    svg.append('<defs>')
    svg.append('  <marker id="arrow" markerWidth="9" markerHeight="9" refX="7" refY="3.5" orient="auto">')
    svg.append('    <path d="M 0 0 L 7 3.5 L 0 7 Z" fill="#000000"/>')
    svg.append('  </marker>')
    svg.append('</defs>')
    svg.append('<rect width="1400" height="780" fill="#FFFFFF"/>')

    R = 24  # Circle radius matching Image 1

    # Node positions carefully spaced to avoid ANY text overlap
    # Row 1: y = 110
    # Q0: 90, Q1: 220, Q2: 350, Q3: 480, Q5: 640, Q6: 780, Q7: 920
    # Column 1 (x = 640): Q5 (110), Q8 (250), Q9 (390), Q12 (530), Q18 (670)
    # Red node: Q10 (920, 270)
    # Middle row loop (y = 530):
    # Q16m (260), Q13a (380), Q11 (500), Q12 (640), Q13b (790)
    # Bottom row (y = 670):
    # Q14 (120), Q15 (260), Q16b (390), Q17 (520), Q18 (650), Q19 (790), Q20 (930)

    nodes = {
        "Q0": (90, 110, "blue", "start_state"),
        "Q1": (220, 110, "white", ""),
        "Q2": (350, 110, "white", ""),
        "Q3": (480, 110, "white", ""),
        "Q5": (640, 110, "white", ""),
        "Q6": (780, 110, "white", ""),
        "Q7": (920, 110, "white", ""),
        
        "Q8": (640, 250, "white", ""),
        "Q10": (920, 270, "red", ""),
        "Q9": (640, 390, "white", ""),
        
        # Middle row
        "Q16m": (260, 530, "white", ""),
        "Q13a": (380, 530, "white", ""),
        "Q11": (500, 530, "white", ""),
        "Q12": (640, 530, "white", ""),
        "Q13b": (790, 530, "white", ""),
        
        # Bottom row
        "Q14": (120, 670, "white", ""),
        "Q15": (260, 670, "white", ""),
        "Q16b": (390, 670, "white", ""),
        "Q17": (520, 670, "white", ""),
        "Q18": (650, 670, "white", ""),
        "Q19": (790, 670, "white", ""),
        "Q20": (930, 670, "green", "")
    }

    def draw_node(nid, x, y, ntype, label=""):
        display_id = nid.rstrip('abm')
        if ntype == "blue":
            svg.append(f'  <circle cx="{x}" cy="{y}" r="{R}" fill="#4A90E2" stroke="#000000" stroke-width="2.2"/>')
            svg.append(f'  <text x="{x}" y="{y+5}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{display_id}</text>')
            # Start arrow
            svg.append(f'  <line x1="{x-55}" y1="{y}" x2="{x-R}" y2="{y}" stroke="#000000" stroke-width="1.8" marker-end="url(#arrow)"/>')
            svg.append(f'  <text x="{x}" y="{y+38}" font-family="Arial, sans-serif" font-size="11" fill="#000000" text-anchor="middle">{label}</text>')
        elif ntype == "red":
            svg.append(f'  <circle cx="{x}" cy="{y}" r="{R}" fill="#E06666" stroke="#000000" stroke-width="2.2"/>')
            svg.append(f'  <text x="{x}" y="{y+5}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#000000" text-anchor="middle">{display_id}</text>')
        elif ntype == "green":
            svg.append(f'  <circle cx="{x}" cy="{y}" r="{R+5}" fill="#6AA84F" stroke="#000000" stroke-width="2.2"/>')
            svg.append(f'  <circle cx="{x}" cy="{y}" r="{R-2}" fill="#6AA84F" stroke="#000000" stroke-width="1.6"/>')
            svg.append(f'  <text x="{x}" y="{y+5}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#000000" text-anchor="middle">{display_id}</text>')
        else:
            svg.append(f'  <circle cx="{x}" cy="{y}" r="{R}" fill="#FFFFFF" stroke="#000000" stroke-width="2.2"/>')
            svg.append(f'  <text x="{x}" y="{y+5}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#000000" text-anchor="middle">{display_id}</text>')

    def draw_edge(x1, y1, x2, y2, label="", label_pos="top"):
        dx = x2 - x1
        dy = y2 - y1
        dist = math.sqrt(dx*dx + dy*dy)
        if dist == 0: return
        ux = dx / dist
        uy = dy / dist
        sx = x1 + ux * R
        sy = y1 + uy * R
        ex = x2 - ux * R
        ey = y2 - uy * R
        svg.append(f'  <line x1="{sx}" y1="{sy}" x2="{ex}" y2="{ey}" stroke="#000000" stroke-width="1.8" marker-end="url(#arrow)"/>')
        if not label: return
        mx = (sx + ex) / 2
        my = (sy + ey) / 2
        if label_pos == "top":
            svg.append(f'  <text x="{mx}" y="{my-6}" font-family="Arial, sans-serif" font-size="11" fill="#000000" text-anchor="middle">{label}</text>')
        elif label_pos == "bottom":
            svg.append(f'  <text x="{mx}" y="{my+15}" font-family="Arial, sans-serif" font-size="11" fill="#000000" text-anchor="middle">{label}</text>')
        elif label_pos == "left":
            svg.append(f'  <text x="{mx-8}" y="{my+4}" font-family="Arial, sans-serif" font-size="11" fill="#000000" text-anchor="end">{label}</text>')
        elif label_pos == "right":
            svg.append(f'  <text x="{mx+8}" y="{my+4}" font-family="Arial, sans-serif" font-size="11" fill="#000000" text-anchor="start">{label}</text>')

    # --- ROW 1: Compiler Pipeline ---
    draw_edge(90, 110, 220, 110, "load_regex", "top")
    draw_edge(220, 110, 350, 110, "tokenize", "top")
    draw_edge(350, 110, 480, 110, "build_ast", "top")
    draw_edge(480, 110, 640, 110, "optimize_ast", "top")
    draw_edge(640, 110, 780, 110, "emit_binary", "top")
    draw_edge(780, 110, 920, 110, "load_bram", "top")

    # --- VERTICAL LADDER & ERROR EDGES ---
    # Q7 -> Q10 (mismatch_detected)
    draw_edge(920, 110, 920, 270, "mismatch_detected", "left")

    # Q5 -> Q8 (stream_ready)
    draw_edge(640, 110, 640, 250, "stream_ready", "right")

    # Q8 -> Q10 (mismatch_detected)
    draw_edge(640, 250, 920, 270, "mismatch_detected", "top")

    # Q8 -> Q9 (fetch_3way)
    draw_edge(640, 250, 640, 390, "fetch_3way", "right")

    # Q9 -> Q10 (error_detected)
    svg.append('  <path d="M 664 390 L 870 390 L 912 294" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arrow)"/>')
    svg.append('  <text x="780" y="382" font-family="Arial, sans-serif" font-size="11" fill="#000000" text-anchor="middle">mismatch_detected</text>')

    # Q9 -> Q12 (dispatch_vcu)
    draw_edge(640, 390, 640, 530, "dispatch_vcu", "right")

    # Q10 (Red) -> Q5 (Outer Rollback Feedback Loop)
    svg.append('  <path d="M 920 246 L 920 45 L 640 45 L 640 86" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arrow)"/>')
    svg.append('  <text x="780" y="38" font-family="Arial, sans-serif" font-size="11" fill="#000000" text-anchor="middle">single_cycle_rollback</text>')
    svg.append('  <text x="940" y="160" font-family="Arial, sans-serif" font-size="11" fill="#000000" text-anchor="start" transform="rotate(-90 940 160)">pop_stack_restore</text>')

    # Q10 -> Q13b (send_query / test_alternative)
    svg.append('  <path d="M 920 294 L 920 470 L 790 470 L 790 506" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arrow)"/>')
    svg.append('  <text x="855" y="462" font-family="Arial, sans-serif" font-size="11" fill="#000000" text-anchor="middle">test_alt_branch</text>')

    # --- MIDDLE ROW (Refinement & Linking) ---
    draw_edge(260, 530, 380, 530, "retry_token", "top")
    draw_edge(380, 530, 500, 530, "save_checkpoint", "top")
    draw_edge(500, 530, 640, 530, "speculate_greedy", "top")
    draw_edge(640, 530, 790, 530, "request_alt", "top")

    # Q16m -> Q15 (Vertical Down)
    draw_edge(260, 530, 260, 670, "")

    # Q12 -> Q18 (accept_token / Vertical Down)
    draw_edge(640, 530, 650, 670, "accept_token", "right")

    # --- BOTTOM ROW: Streaming & Match Resolution ---
    draw_edge(120, 670, 260, 670, "slide_window", "top")
    draw_edge(260, 670, 390, 670, "realign_buffer", "top")
    draw_edge(390, 670, 520, 670, "next_byte", "top")
    draw_edge(520, 670, 650, 670, "check_bounds", "top")
    draw_edge(650, 670, 790, 670, "check_eop", "top")
    draw_edge(790, 670, 930, 670, "emit_offsets", "top")

    # Draw all nodes on top
    for nid, (x, y, ntype, label) in nodes.items():
        draw_node(nid, x, y, ntype, label)

    svg.append('</svg>')
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Generated clean Style 1 ALVEARE diagram: {filename}")


def create_style2_alveare(filename):
    # Image 2 Clone: 1400 x 850
    # 4 swimlanes with spacious layout, clean non-overlapping labels, self loops
    svg = []
    svg.append('<?xml version="1.0" encoding="UTF-8" standalone="no"?>')
    svg.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 850" width="1400" height="850">')
    svg.append('<defs>')
    svg.append('  <marker id="arrow" markerWidth="9" markerHeight="9" refX="7" refY="3.5" orient="auto">')
    svg.append('    <path d="M 0 0 L 7 3.5 L 0 7 Z" fill="#000000"/>')
    svg.append('  </marker>')
    svg.append('  <marker id="arrowRed" markerWidth="9" markerHeight="9" refX="7" refY="3.5" orient="auto">')
    svg.append('    <path d="M 0 0 L 7 3.5 L 0 7 Z" fill="#EA4335"/>')
    svg.append('  </marker>')
    svg.append('</defs>')
    svg.append('<rect width="1400" height="850" fill="#FFFFFF"/>')

    # Main Header
    svg.append('  <text x="700" y="38" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="#000000" text-anchor="middle">ALVEARE: Domain-Specific Execution State Machine (Corrected DFA)</text>')

    row_data = [
        {
            "title": "Front-End Lexing, Parsing &amp; Compiler Optimization (C Software)",
            "y": 60, "height": 165,
            "nodes": [
                ("Q0", "Idle / Load\nRegex", "blue", 130),
                ("Q1", "FLEX Lexer\nTokenization", "white", 350),
                ("Q2", "BISON AST\nGeneration", "white", 570),
                ("Q3", "AST Optimize\n&amp; Pruning", "white", 790),
                ("Q4", "Linear 43-bit\nISA Codegen", "white", 1010),
                ("Q5", "BRAM Binary\nLoader", "white", 1230)
            ],
            "edges": [
                (0, 1, "load_regex"),
                (1, 2, "tokenize"),
                (2, 3, "build_ast"),
                (3, 4, "optimize_ast"),
                (4, 5, "emit_binary")
            ]
        },
        {
            "title": "Instruction Fetch, 3-Way Decode &amp; Vector Compute (Hardware Core)",
            "y": 255, "height": 165,
            "nodes": [
                ("Q5", "BRAM Binary\nLoader", "white", 130),
                ("Q6", "16 KB Stream\nIngestion", "white", 370),
                ("Q7", "3-Way Parallel\nFetch/Decode", "white", 610),
                ("Q8", "Vector Compute\nUnit (VCU)", "white", 850),
                ("Q9", "Branch Detector\n(*, +, ?, |)", "white", 1090)
            ],
            "edges": [
                (0, 1, "stream_chunk"),
                (1, 2, "fetch_3way"),
                (2, 3, "dispatch_vcu"),
                (3, 4, "check_operator")
            ]
        },
        {
            "title": "Speculative Execution, Stack Push &amp; Backtracking Loop",
            "y": 450, "height": 165,
            "nodes": [
                ("Q10", "Speculation\nCheckpoint", "amber", 130),
                ("Q11", "Push Stack\n(Alt PC, Ptr)", "white", 390),
                ("Q12", "Evaluate Greedy\nPrimary Path", "white", 650),
                ("Q13", "Mismatch\nDetection", "white", 910),
                ("Q14", "Single-Cycle\nStack Pop", "red", 1170)
            ],
            "edges": [
                (0, 1, "save_state"),
                (1, 2, "speculate_greedy"),
                (2, 3, "char_mismatch"),
                (3, 4, "stack_not_empty")
            ]
        },
        {
            "title": "Stream Window Progression &amp; Match Resolution",
            "y": 645, "height": 165,
            "nodes": [
                ("Q12", "Char Match\nSatisfied", "white", 130),
                ("Q15", "Advance Stream\n(stream_ptr++)", "white", 410),
                ("Q16", "Window Slide\n(SP==0, PC=0)", "white", 690),
                ("Q17", "End-of-Pattern\nVerification", "white", 970),
                ("Q18", "Match Found\n(Emit Offsets)", "green", 1230)
            ],
            "edges": [
                (0, 1, "char_ok"),
                (1, 3, "check_eop"),
                (3, 4, "pattern_complete")
            ]
        }
    ]

    r = 30  # Circle radius for swimlane nodes

    for r_idx, row in enumerate(row_data):
        ry = row["y"]
        rh = row["height"]
        
        # Swimlane background
        svg.append(f'  <g transform="translate(40, {ry})">')
        svg.append(f'    <rect width="1320" height="{rh}" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.2"/>')
        svg.append(f'    <text x="20" y="24" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#334155">{row["title"]}</text>')
        svg.append('  </g>')

        node_cy = ry + 95
        nodes = row["nodes"]

        # Straight edges with spacious placement
        for e in row["edges"]:
            i1, i2, elabel = e
            x1 = nodes[i1][3] + 40
            x2 = nodes[i2][3] + 40
            
            svg.append(f'  <line x1="{x1+r}" y1="{node_cy}" x2="{x2-r}" y2="{node_cy}" stroke="#000000" stroke-width="1.8" marker-end="url(#arrow)"/>')
            mx = (x1 + x2) / 2
            svg.append(f'  <text x="{mx}" y="{node_cy-8}" font-family="Arial, sans-serif" font-size="11" fill="#000000" text-anchor="middle">{elabel}</text>')

        # Red loop in row 2
        if r_idx == 2:
            x14 = nodes[4][3] + 40
            x12 = nodes[2][3] + 40
            svg.append(f'  <path d="M {x14} {node_cy-r} C {x14} {node_cy-60}, {x12} {node_cy-60}, {x12} {node_cy-r}" fill="none" stroke="#EA4335" stroke-width="1.8" marker-end="url(#arrowRed)"/>')
            svg.append(f'  <text x="{(x14+x12)/2}" y="{node_cy-65}" font-family="Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#EA4335" text-anchor="middle">single_cycle_rollback_to_alt_branch</text>')

        # Draw nodes with self-loops
        for idx, n in enumerate(nodes):
            nid, ntext, ntype, nx = n
            cx = nx + 40
            cy = node_cy

            # Self loop arc
            svg.append(f'  <path d="M {cx-10} {cy-r+2} C {cx-22} {cy-r-20}, {cx+22} {cy-r-20}, {cx+10} {cy-r+2}" fill="none" stroke="#475569" stroke-width="1.3" marker-end="url(#arrow)"/>')

            if ntype == "blue":
                svg.append(f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="#4A90E2" stroke="#000000" stroke-width="2.2"/>')
                # Start arrow
                svg.append(f'  <line x1="{cx-r-45}" y1="{cy}" x2="{cx-r}" y2="{cy}" stroke="#000000" stroke-width="1.8" marker-end="url(#arrow)"/>')
                svg.append(f'  <text x="{cx-r-22}" y="{cy-8}" font-family="Arial, sans-serif" font-size="10" fill="#000000" text-anchor="middle">start</text>')
                tcolor = "#FFFFFF"
            elif ntype == "red":
                svg.append(f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="#E06666" stroke="#000000" stroke-width="2.2"/>')
                tcolor = "#000000"
            elif ntype == "amber":
                svg.append(f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="#F6B26B" stroke="#000000" stroke-width="2.2"/>')
                tcolor = "#000000"
            elif ntype == "green":
                svg.append(f'  <circle cx="{cx}" cy="{cy}" r="{r+5}" fill="#6AA84F" stroke="#000000" stroke-width="2.2"/>')
                svg.append(f'  <circle cx="{cx}" cy="{cy}" r="{r-2}" fill="#6AA84F" stroke="#000000" stroke-width="1.6"/>')
                tcolor = "#000000"
            else:
                svg.append(f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="#FFFFFF" stroke="#000000" stroke-width="2"/>')
                tcolor = "#000000"

            # Node ID and text
            lines = ntext.split("\n")
            svg.append(f'  <text x="{cx}" y="{cy-6}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{tcolor}" text-anchor="middle">{nid}</text>')
            if len(lines) == 1:
                svg.append(f'  <text x="{cx}" y="{cy+10}" font-family="Arial, sans-serif" font-size="8.5" fill="{tcolor}" text-anchor="middle">{lines[0]}</text>')
            elif len(lines) >= 2:
                svg.append(f'  <text x="{cx}" y="{cy+6}" font-family="Arial, sans-serif" font-size="8" fill="{tcolor}" text-anchor="middle">{lines[0]}</text>')
                svg.append(f'  <text x="{cx}" y="{cy+16}" font-family="Arial, sans-serif" font-size="8" fill="{tcolor}" text-anchor="middle">{lines[1]}</text>')

    svg.append('</svg>')
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Generated clean Style 2 ALVEARE diagram: {filename}")

if __name__ == "__main__":
    create_style1_alveare("c:/Users/Jashith Masand/Desktop/CN/alveare_simple_clean_diagram.svg")
    create_style2_alveare("c:/Users/Jashith Masand/Desktop/CN/alveare_phased_clean_diagram.svg")
