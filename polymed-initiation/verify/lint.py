"""House-style and scope lint for the Polymed report drafts (draft/*.md, draft/companion/*.md).

Errors fail the build; warnings are for review. Chart JSON blocks and {{tokens}} are ignored.
Usage: python3 verify/lint.py [--strict]
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

ERR = [
    (r"—", "em dash (use en dash – or restructure)"),
    (r"\d\s*–\s*\d", "en dash inside a numeric range (ranges take a hyphen: 6-7%)"),
    (r"\bcrores?\b|\bRs\.?\s?cr\b|\b\d+\s?cr\b|\blakhs?\b", "crore/lakh (use Rs. mn / Rs. bn)"),
    (r"₹|\bINR\s?\d", "rupee symbol/INR (use Rs.)"),
    (r"\bRs\s\d", "'Rs ' without period (use 'Rs. ')"),
    (r"\bQ[1-4]\s?FY\d{2}\b", "quarter format (use 1QFY27)"),
    (r"\bFY20\d{2}\b", "FY2027 format (use FY27)"),
    (r"\bYoY\b|\bQoQ\b|\bY-o-Y\b|\byear-on-year\b", "use yoy / qoq"),
    (r"\bbasis points\b", "use bps"),
    (r"\bcagr\b", "use uppercase CAGR"),
    (r"\bMiddle East\b", "use West Asia"),
    (r"\bdelve|\bpivotal\b|\bpoised to\b|\bunderscor(e|es|ed|ing)\b|\bcrucial\b|\btransformative\b|\btestament to\b|\bgame-changing\b",
     "banned vocabulary"),
    (r"\bleverag(es|ing|ed)\b|\bto leverage\b", "leverage as a verb"),
    (r"\bIt'?s worth noting\b|\bImportantly,|\bThat said,|\bIn conclusion\b|^Overall,", "throat-clearing opener"),
    (r"\btarget price\b|\bTP\b|\b(BUY|SELL|ADD|REDUCE)\b|\bFY2[6-9]E\b|\bFY3\dE\b|\bP/E\b|\bEV/EBITDA\b|\bDCF\b",
     "scope guard: valuation/rating/forecast language (business + industry only)"),
]
WARN = [
    (r"\brobust\b", "robust: keep only if quantified"),
    (r"\bnavigat(e|es|ing)\b", "navigate (metaphorical?)"),
    (r"\bserves as\b|\bstands as\b", "AI-tell construction"),
    (r"\bmillion\b|\bbillion\b", "use mn/bn"),
    (r"\b(color|favor|behavior|neighbor|honor|harbor)\w*", "American spelling (-our)"),
    (r"\bcent(er|ers)\b", "American spelling (centre)"),
    (r"\banalyz(e|es|ed|ing)\b", "American spelling (analyse)"),
    (r"\bdialyzer", "spelling: dialyser (Oxford) unless an official name"),
    (r"\bvaluation\b|\bmultiple(s)?\b|\bre-?rating\b", "scope check: valuation language?"),
    (r"\bwe (estimate|expect|forecast|project)\b", "scope check: forward estimate?"),
    (r"\*\*[^*\n]{3,}\*\*", "bold inside prose (house style avoids bold-facing key phrases)"),
]
ISE_OK = {"advise", "comprise", "enterprise", "exercise", "franchise", "otherwise", "premise", "promise", "revise",
          "supervise", "surprise", "compromise", "disguise", "expertise", "merchandise", "raise", "rise", "wise",
          "noise", "arise", "apprise", "chastise", "despise", "devise", "improvise", "incise", "precise", "concise",
          "praise", "poise", "cruise", "bruise", "guise", "likewise", "clockwise", "demise", "excise", "treatise",
          "reprise", "paradise", "circumcise", "televise", "anise", "valise", "turquoise", "tortoise", "porpoise",
          "noise", "chemise", "coarse", "premises", "exercises", "enterprises", "franchises", "promises", "raises",
          "rises", "arises", "revises", "surprises", "supervises", "advises", "comprises", "compromises", "expertise"}
ISE_RE = re.compile(r"\b([a-z]+is(e|es|ed|ing|ation|ations))\b")


def strip_blocks(t):
    t = re.sub(r"^:::\s*chart.*?^:::\s*$", "", t, flags=re.S | re.M)
    t = re.sub(r"\{\{[^}]+\}\}", "0", t)
    t = re.sub(r"\[\[[^\]]+\]\]", "", t)
    t = re.sub(r'(title|note|src_extra)="[^"]*"', lambda m: m.group(0), t)
    return t


def main():
    strict = "--strict" in sys.argv
    files = sorted(glob.glob("draft/*.md")) + sorted(glob.glob("draft/companion/*.md"))
    n_err = n_warn = 0
    for f in files:
        raw = open(f).read()
        t = strip_blocks(raw)
        for ln, line in enumerate(t.splitlines(), 1):
            if line.strip().startswith("<!--") or "lint-ok" in line:
                continue
            for pat, msg in ERR:
                for m in re.finditer(pat, line, flags=re.M):
                    # allow official names that contain flagged words
                    ctx = line[max(0, m.start() - 40): m.end() + 40]
                    if msg.startswith("scope guard") and re.search(r"credit rating|rating agenc|CRISIL|AA-|A1\+", ctx):
                        continue
                    print(f"ERROR {f}:{ln}: {msg}: …{ctx.strip()}…")
                    n_err += 1
            for pat, msg in WARN:
                for m in re.finditer(pat, line):
                    ctx = line[max(0, m.start() - 30): m.end() + 30]
                    if msg.startswith("scope check") and re.search(r"credit|acquisition|EV |enterprise value|deal", ctx, re.I):
                        continue
                    print(f"warn  {f}:{ln}: {msg}: …{ctx.strip()}…")
                    n_warn += 1
            for m in ISE_RE.finditer(line.lower()):
                w = m.group(1)
                base = re.sub(r"(es|ed|ing|ation|ations)$", "e", w) if not w.endswith("ise") else w
                if w in ISE_OK or base in ISE_OK or any(w.startswith(x) for x in ("exercis", "enterpris", "franchis", "premis", "promis", "revis", "supervis", "surpris", "advis", "compris", "compromis", "expertis", "rais", "aris", "devis", "precis", "concis", "wis", "nois", "prais")):
                    continue
                print(f"warn  {f}:{ln}: -ise spelling (Oxford -ize?): {w}")
                n_warn += 1
    print(f"\nlint: {n_err} errors, {n_warn} warnings across {len(files)} files")
    sys.exit(1 if (n_err and strict) else 0)


if __name__ == "__main__":
    main()
