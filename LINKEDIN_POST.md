Safe to Send · Ep 14 — The word "forgot" in your incident report

Week 2 retro, with a different angle. Here's a synthetic incident report, written the way many of them really are:

"The operator forgot to check the send time." Contributing factor: "human error under Black Friday volume."

I built a small linter for postmortems. It flags blame language ("forgot", "careless", "should have", "human error") and every action item without an owner and a due date.

On this report it flagged three things. The interesting part is what happened when I rewrote them:

"The operator forgot to check the send time"
→ "The scheduler showed UTC with no local-time preview"

Same facts. The first version produces a reprimand. The second produces a fix that protects every market next year.

The tool also calculates time to detect (22 min) and time to contain (12 min). By then, 38% of the audience had the email.

Repo: https://github.com/sghatge/safe-to-send-14-blameless-postmortem

#SafeToSend #Postmortem #MarketingOps #LearnInPublic
