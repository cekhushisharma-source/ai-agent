import json

from parser import extract_text
from interrogator import InterrogatorAgent
from reasoning_engine import ReasoningEngine
from report_generator import ReportGenerator


# Load dataset
with open("dataset.json") as f:

    data = json.load(f)


# Get PDF path
pdf_path = data["pdf_path"]


# Extract text from PDF
text = extract_text(pdf_path)


# Initialize modules
interrogator = InterrogatorAgent()
reasoner = ReasoningEngine()
reporter = ReportGenerator()


# Example suspects
suspects = ["John", "Mike", "Sarah"]


# Interrogation phase
for suspect in suspects:

    questions = interrogator.ask_questions(
        suspect,
        "Fingerprint and CCTV evidence"
    )

    print(f"\nQuestions for {suspect}:")

    for q in questions:
        print("-", q)


# Investigation phase
results = reasoner.analyze(text)


# Generate report
report = reporter.generate(results)


# Print final report
print(report)