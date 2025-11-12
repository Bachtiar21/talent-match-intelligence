# Parse AI Output
def parse_ai_output(text: str):
    sections = {
        "Key Responsibilities": [],
        "Work Inputs": [],
        "Work Outputs": [],
        "Qualifications": [],
        "Competencies": [],
    }

    current = None
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        lower = line.lower()
        if "responsibilit" in lower:
            current = "Key Responsibilities"
        elif "input" in lower:
            current = "Work Inputs"
        elif "output" in lower:
            current = "Work Outputs"
        elif "qualification" in lower:
            current = "Qualifications"
        elif "competenc" in lower:
            current = "Competencies"
        elif current:
            clean = line.lstrip("-•1234567890. ").strip()
            if clean:
                sections[current].append(clean)

    return sections
