from pathlib import Path
import sys
import subprocess

def compile_latex(tex_file):
    tex_path = Path(tex_file).resolve()
    workdir = tex_path.parent
    tex_name = tex_path.name

    print("Compiling LaTeX → PDF...")

    try:
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", tex_name],
            cwd=workdir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
    except FileNotFoundError:
        print("Error: pdflatex not found. Is LaTeX installed?")
        sys.exit(1)

    if result.returncode != 0:
        print("LaTeX compilation failed:\n")
        print(result.stdout)
        print(result.stderr)
        sys.exit(1)

    print("PDF generated successfully.")


# -----------------------------
# Data containers
# -----------------------------
contact = []
education = []
experience = []
projects = []

# -----------------------------
# CLI argument
# -----------------------------
if len(sys.argv) < 2:
    print("Usage: python3 render.py <cv.md>")
    sys.exit(1)

input_file = sys.argv[1]

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# -----------------------------
# Parser state
# -----------------------------
current_section = None
current_subsection = None
userName = None


def flush_subsection():
    global current_subsection
    if not current_subsection:
        return

    if current_section == "Education":
        education.append(current_subsection)
    elif current_section == "Experience":
        experience.append(current_subsection)
    elif current_section == "Projects":
        projects.append(current_subsection)

    current_subsection = None


# -----------------------------
# Markdown parsing
# -----------------------------
for line in lines:
    line = line.strip()
    if not line:
        continue

    # Title
    if line.startswith("# "):
        userName = line[2:].strip()
        continue

    # Section
    if line.startswith("## "):
        flush_subsection()
        current_section = line[3:].strip()
        continue

    # Contact information
    if current_section == "Contact Information" and line.startswith("- "):
        key, value = line[2:].split(":", 1)
        contact.append({key.strip(): value.strip()})
        continue

    # Subsection
    if line.startswith("### "):
        flush_subsection()
        current_subsection = {
            "title_org": line[4:].strip(),
            "bullets": []
        }
        continue

    # Date
    if line.startswith("> ") and current_subsection:
        current_subsection["date"] = line[2:].strip()
        continue

    # Bullet
    if line.startswith("- ") and current_subsection:
        current_subsection["bullets"].append(line[2:].strip())
        continue


flush_subsection()

print("Markdown file read. Creating the CV.")

# -----------------------------
# Header generation
# -----------------------------
latex_header = ""
latex_header += f"\\fontsize{{25 pt}}{{25 pt}}\\selectfont {userName}\n"
latex_header += "\n\\vspace{5 pt}\n"
latex_header += "\\normalsize\n"

contacts_len = len(contact)

for i, info in enumerate(contact):
    for key, value in info.items():
        if key == "Email":
            latex_header += (
                f"\\mbox{{\\hrefWithoutArrow{{mailto:{value}}}{{\\texttt{{{value}}}}}}}%\n"
            )
        elif key == "Phone":
            latex_header += (
                f"\\mbox{{\\hrefWithoutArrow{{tel:{value}}}{{{value}}}}}%\n"
            )
        elif key == "LinkedIn":
            latex_header += (
                f"\\mbox{{\\hrefWithoutArrow{{{value}}}{{\\texttt{{LinkedIn}}}}}}%\n"
            )
        elif key == "GitHub":
            latex_header += (
                f"\\mbox{{\\hrefWithoutArrow{{{value}}}{{\\texttt{{GitHub}}}}}}%\n"
            )
        else:
            latex_header += (
                f"\\mbox{{\\hrefWithoutArrow{{{value}}}{{\\texttt{{{key}}}}}}}%\n"
            )

        if i < contacts_len - 1:
            latex_header += "\\kern 5.0 pt%\n"
            latex_header += "\\AND%\n"
            latex_header += "\\kern 5.0 pt%\n"

print("Header created.")

# -----------------------------
# Education
# -----------------------------
latex_education = ""

for i, entry in enumerate(education):
    date = entry.get("date", "")
    title = entry["title_org"]

    name, org = (title.split("|", 1) + [""])[:2]
    name = name.strip()
    org = org.strip()

    latex_education += f"\\begin{{twocolentry}}{{{date}}}\n"
    latex_education += f"\\textbf{{{name}}}, {org}\n"
    latex_education += "\\end{twocolentry}\n\n"

    if len(entry["bullets"]) > 0:
        latex_education += "\\vspace{0.10 cm}\n"
        latex_education += "\\begin{onecolentry}\n"
        latex_education += "\\begin{highlights}\n"

        for bullet in entry["bullets"]:
            if bullet.startswith("Coursework:"):
                bullet = bullet.replace("Coursework:", "\\textbf{Coursework:}")
            latex_education += f"\\item {bullet}\n"

        latex_education += "\\end{highlights}\n"
        latex_education += "\\end{onecolentry}\n"

    if i < len(education) - 1:
        latex_education += "\\vspace{0.20 cm}\n"

print("Education section created.")

# -----------------------------
# Experience
# -----------------------------
latex_experience = ""

for i, entry in enumerate(experience):
    date = entry.get("date", "")
    title = entry["title_org"]

    name, org = (title.split("|", 1) + [""])[:2]
    name = name.strip()
    org = org.strip()

    latex_experience += f"\\begin{{twocolentry}}{{{date}}}\n"
    latex_experience += f"\\textbf{{{name}}}, {org}\n"
    latex_experience += "\\end{twocolentry}\n\n"

    latex_experience += "\\vspace{0.10 cm}\n"
    latex_experience += "\\begin{onecolentry}\n"
    latex_experience += "\\begin{highlights}\n"

    for bullet in entry["bullets"]:
        latex_experience += f"\\item {bullet}\n"

    latex_experience += "\\end{highlights}\n"
    latex_experience += "\\end{onecolentry}\n"

    if i < len(experience) - 1:
        latex_experience += "\\vspace{0.10 cm}\n"

print("Experience section created.")

# -----------------------------
# Projects
# -----------------------------
latex_projects = ""

for entry in projects:
    title = entry["title_org"]
    name, short_link, link = (title.split("|", 2) + [""])[:3]
    name = name.strip()
    short_link = short_link.strip()
    link = link.strip()

    latex_projects += "\\vspace{0.10 cm}\n"

    if link:
        latex_projects += (
            f"\\begin{{twocolentry}}{{\\href{{{link}}}{{{short_link}}}}}\\textbf{{{name}}}\n"
        )
    else:
        latex_projects += f"\\begin{{twocolentry}}{{\\textbf{{{name}}}}}\n"

    latex_projects += "\\end{twocolentry}\n\n"

    latex_projects += "\\vspace{0.10 cm}\n"
    latex_projects += "\\begin{onecolentry}\n"
    latex_projects += "\\begin{highlights}\n"

    tools = entry["bullets"][-1].replace("Tools Used:", "\\textbf{Tools Used:}")
    for bullet in entry["bullets"][:-2]:
        latex_projects += f"\\item {bullet}\n"
    latex_projects += f"\\item {entry['bullets'][-2]} {tools}\n"
    latex_projects += "\\end{highlights}\n"
    latex_projects += "\\end{onecolentry}\n"

print("Projects section created.")

# -----------------------------
# Template filling
# -----------------------------
template_file = "./input/latexTemplate.tex"
output_file = "./output/output_cv.tex"

with open(template_file, "r", encoding="utf-8") as f:
    template = f.read()

template = template.replace("{{HEADER}}", latex_header)
template = template.replace("{{EDUCATION}}", latex_education)
template = template.replace("{{EXPERIENCE}}", latex_experience)
template = template.replace("{{PROJECTS}}", latex_projects)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(template)

print(f"CV LaTeX generated: {output_file}")

# Compile LaTeX to PDF 
compile_latex(output_file)