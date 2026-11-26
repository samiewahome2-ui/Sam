# Samie Wahome | AI & Research Portfolio

**AI evaluation · Data annotation · Research quality · Robotics and systems thinking**

Based in Kenya, I am interested in building reliable AI systems through structured evaluation, evidence-based research and careful data quality review.

## Portfolio website

[View the portfolio source](index.html). Open `index.html` in a modern browser to explore the responsive portfolio, filter projects, and try the interactive AI response quality gate. No API keys or external dependencies are required.

## Selected projects

| Project | Demonstrates | Status |
|---|---|---|
| [AI response evaluation](projects/ai-evaluation/) | Rubric design, factuality, severity and review decisions | Runnable demo |
| [Research evidence register](projects/research-quality/) | Claim-to-source traceability, limitations and release gates | Template |
| [Data annotation quality](projects/data-annotation/) | Label consistency, ambiguity handling and agreement | Worked example |
| [Robotics verification](projects/robotics/) | Requirements traceability, timing and integration testing | Example test plan |

## Skills and interests

- AI output evaluation, error categorization and human oversight
- Evidence synthesis, reproducibility and uncertainty reporting
- Rubric-based labeling, quality auditing and reviewer calibration
- Robotics verification planning and sensor-data quality
- Clear, decision-ready technical documentation

## Run the evaluation demo

Requires Python 3.10+ and no external packages.

```bash
python projects/ai-evaluation/evaluate.py
python -m unittest discover -s projects/ai-evaluation -p "test_*.py"
```

## Hosting

The static portfolio is ready for GitHub Pages: select **Settings → Pages**, then deploy from the root of the `main` branch.

All examples are illustrative and use synthetic or fictional data. They do not represent client results or measured production improvements.

[GitHub profile](https://github.com/samiewahome2-ui)
