<div align="center">

<img src="assets/portfolio/repo-card.svg" width="520" alt="safe-to-send-14-blameless-postmortem bespoke project visual">

**SAFE TO SEND · GOVERNED AI ENGINEERING SERIES · SAFE TO SEND 14 BLAMELESS POSTMORTEM**

[GitHub Profile](https://github.com/sghatge) · [Portfolio](https://sghatge.github.io/adobe-campaign-v8-governance/)

</div>

---

# safe-to-send-14 · Blameless Postmortem Kit

![Safe to Send, Episode 14](docs/episode.png)

**Safe to Send · Episode 14** — Week 2 retrospective of a 28-day learn-in-public series on governing AI in CRM operations.

> Blame the person and the next mistake gets hidden. Blame the system and it gets fixed.

## The real-world scenario

A Greek Black Friday email goes out at 23:30 local time with English price formatting. The first draft of the incident report says "the operator forgot to check the send time" and lists "human error" as a cause. Everyone nods. Nothing about the scheduler changes, and next year it happens again in another market.

## The use case

Write the incident as a timeline. This tool turns it into a postmortem, calculates time to detect and time to contain, and lints it:

- **blame language** ("forgot", "careless", "should have", "human error") is flagged with the sentence it appears in
- **action items** without an owner and a due date are flagged

## Run it

```bash
python postmortem.py examples/gr_late_send.json
```

## Real example output (lint section)

```
## Lint
- blame language "forgot" in: ... The operator forgot to check the send time.
- blame language "Human error" in: Human error under Black Friday volume
- action without owner or due date: Review Black Friday staffing
```

The rendered postmortem also shows **time to detect: 22 min** and **time to contain: 12 min**: by the time anyone noticed, 38% of the audience had the email.

## Rewrite it blamelessly

"The operator forgot to check the send time" becomes "The scheduler showed UTC with no local-time preview". Same facts. One version produces a reprimand, the other produces a fix.

MIT · [Sangram Ghatge](https://www.linkedin.com/in/sangram-g-2369705b) · #SafeToSend


---

## Portfolio integration & safe use

This repository is part of the **Safe to Send** 28-episode engineering series on governed AI for CRM and marketing operations.

- [Series index and episode map](https://github.com/sghatge/safe-to-send-21-series-map)
- [Complete portfolio](https://github.com/sghatge/sghatge)
- [OPSFORGE Build Lab](https://sghatge.streamlit.app/) — portfolio overview; this repository remains independently usable without the Build Lab.

**Safe-use boundary:** use the supplied examples and synthetic data for evaluation. Review the implementation, dependencies and tests before adapting it. Do not connect it to a production CRM, customer dataset or activation endpoint without a separate security, privacy and change-control review. No production integration or deployment is implied by this repository.
