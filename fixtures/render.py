#!/usr/bin/env python3
"""Odologic fixture renderer.

Reads a fixture JSON and renders the shared trace-view HTML (document panel,
judgment stack with trace-to-floor, side ledger inspector). Used by both UI
variant sketches so the logic-trace presentation stays identical while layout
experiments vary.

Usage: render.py <fixture.json> <out.html> [--inner] > embedding
"""
import json
import sys
from pathlib import Path

STATUS_ORDER = ["theorem", "observation", "assumption", "contested", "defeated", "unaudited"]
STATUS_COLORS = {
    "theorem": "#1F6F54",
    "observation": "#1D5F8A",
    "assumption": "#8A6A1F",
    "contested": "#6A3FA0",
    "defeated": "#A03030",
    "unaudited": "#666666",
}
VERBS = {
    "theorem": "holds as theorem",
    "observation": "holds as observation",
    "assumption": "held as assumption",
    "contested": "contested",
    "defeated": "defeated",
    "unaudited": "unaudited",
}


def esc(s):
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def status_chip(status):
    c = STATUS_COLORS.get(status, "#666")
    return f'<span class="chip" style="background:{c}">{esc(status)}</span>'


def cert_row(c, jid):
    ok = c.get("suffices")
    badge = "suffices" if ok else "insufficient"
    bcls = "ok" if ok else "no"
    return (
        f'<div class="cert">'
        f'<div class="cert-head"><span class="cert-id">{esc(c["id"])}</span>'
        f'<span class="cert-type">{esc(c["type"])}</span>'
        f'<span class="badge {bcls}">{badge}</span></div>'
        f'<div class="cert-summary">{esc(c["summary"])}</div>'
        f'<div class="cert-detail">{esc(c["detail"])}</div>'
        f"</div>"
    )


def trace_block(j, certs, defs, deps, floors):
    """Render the per-judgment trace to the floor."""
    lines = []
    cert = certs.get(j.get("certificate"))
    dlist = [defs[d] for d in j.get("defeats", []) if d in defs]
    dep_ids = deps.get(j["id"], [])
    out = []
    out.append(f'<section class="jrow" id="{esc(j["id"])}" data-status="{esc(j["status"])}">')
    out.append(f'<div class="jhead"><span class="jid">{esc(j["id"])}</span>'
               f'{status_chip(j["status"])}'
               f'<span class="jtype">{esc(j.get("type", ""))}</span></div>')
    out.append(f'<div class="jclaim">{esc(j["claim"])}</div>')
    out.append(f'<div class="jverdict">{esc(j["verdict_line"])}</div>')
    # evidence panel
    out.append('<div class="epanel"><div class="etitle">Evidence</div>')
    if cert:
        out.append(cert_row(cert, j["id"]))
    else:
        out.append('<div class="cert none">no certificate attached</div>')
    out.append("</div>")
    # floor trace
    out.append('<div class="epanel"><div class="etitle">Trace to floor</div>')
    if j["status"] == "theorem":
        out.append(f'<div class="trace-line floor">FLOOR · {esc(j["claim"])}</div>')
        for d in dep_ids:
            dj = floors.get(d)
            if dj:
                out.append(f'<div class="trace-line floor">floor · {esc(dj["claim"])}</div>')
    else:
        if j["status"] == "defeated":
            out.append(f'<div class="trace-line bad">{esc(j["id"])} · {esc(VERBS.get(j["status"], j["status"]))} · no path to floor</div>')
        else:
            out.append(f'<div class="trace-line">{"&nbsp;"*2}{esc(j["id"])} · {esc(VERBS.get(j["status"], j["status"]))}</div>')
            for d in dep_ids:
                dj = floors.get(d)
                if dj:
                    out.append(f'<div class="trace-line floor">{"&nbsp;"*4}└ floor · {esc(dj["claim"])}</div>')
    out.append("</div>")
    # defeats
    if dlist:
        out.append('<div class="epanel"><div class="etitle">Defeats</div>')
        for d in dlist:
            out.append(
                f'<div class="drow"><span class="dtype">{esc(d["type"])}</span>'
                f'<span class="dtarget">→ {esc(d["target"])}</span></div>'
                f'<div class="dclaim">{esc(d["claim"])}</div>'
                f'<div class="ddetail">{esc(d["detail"])}</div>'
            )
        out.append("</div>")
    out.append("</section>")
    return "\n".join(out)


def render(fixture_path, out_path=None, inner=False):
    data = json.loads(Path(fixture_path).read_text())
    certs = {c["id"]: c for c in data.get("certificates", [])}
    defs = {d["id"]: d for d in data.get("defeats", [])}
    deps = data.get("depends_on", {})
    floors = {j["id"]: j for j in data.get("judgments", [])}

    counts = {s: 0 for s in STATUS_ORDER}
    for j in data["judgments"]:
        counts[j["status"]] = counts.get(j["status"], 0) + 1

    rows = "\n".join(trace_block(j, certs, defs, deps, floors) for j in data["judgments"])

    # stats strip
    stats = "".join(
        f'<div class="stat"><span class="stat-n" style="color:{STATUS_COLORS[s]}">{counts[s]}</span>'
        f'<span class="stat-l">{s}</span></div>'
        for s in STATUS_ORDER if counts.get(s)
    )

    body = f"""
<main class="odologic">
  <div class="docpane">
    <div class="pane-head">
      <div class="pane-title">{esc(data.get("source_name", "source"))}</div>
      <div class="pane-sub">{esc(data.get("scenario", ""))}</div>
    </div>
    <div class="doctext">{esc(data["input_text"])}</div>
  </div>
  <div class="tracepane">
    <div class="pane-head">
      <div class="pane-title">{esc(data.get("task_line", "Judgments"))}</div>
      <div class="pane-sub">{esc(data.get("subtitle", ""))}</div>
    </div>
    <div class="stats">{stats}</div>
    <div class="jlist">{rows}</div>
  </div>
</main>
"""
    if inner:
        return body
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{esc(data.get("source_name", "Odologic"))} · Odologic</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  color: #1a1a1a; background: #f6f5f2; line-height: 1.5; }}
main.odologic {{ display: grid; grid-template-columns: 2fr 3fr; gap: 0; min-height: 100vh; }}
.docpane {{ background: #efede8; border-right: 1px solid #ddd9d0; padding: 28px 24px; }}
.tracepane {{ padding: 28px 32px; }}
.pane-head {{ margin-bottom: 14px; }}
.pane-title {{ font-weight: 650; font-size: 15px; }}
.pane-sub {{ font-size: 12.5px; color: #6b675e; margin-top: 2px; }}
.doctext {{ font-size: 15px; white-space: pre-wrap; background: #fff; border: 1px solid #e0dcd2;
  border-radius: 10px; padding: 18px 20px; margin-top: 10px; font-family: Georgia, "Times New Roman", serif; }}
.stats {{ display: flex; gap: 18px; margin-bottom: 16px; flex-wrap: wrap; }}
.stat {{ display: flex; align-items: baseline; gap: 5px; }}
.stat-n {{ font-size: 20px; font-weight: 700; }}
.stat-l {{ font-size: 11.5px; color: #6b675e; text-transform: uppercase; letter-spacing: 0.04em; }}
.jlist {{ display: flex; flex-direction: column; gap: 14px; }}
.jrow {{ background: #fff; border: 1px solid #e3dfd6; border-radius: 10px; padding: 16px 18px; }}
.jrow[data-status="defeated"] {{ border-color: #d9b8b8; background: #fdf9f9; }}
.jhead {{ display: flex; align-items: center; gap: 8px; margin-bottom: 6px; }}
.jid {{ font-family: ui-monospace, monospace; font-size: 12px; color: #6b675e; }}
.jtype {{ font-size: 11px; color: #9b968b; text-transform: uppercase; letter-spacing: 0.05em; margin-left: auto; }}
.chip {{ color: #fff; font-size: 10.5px; font-weight: 650; text-transform: uppercase;
  letter-spacing: 0.06em; border-radius: 999px; padding: 2px 9px; }}
.jclaim {{ font-size: 15.5px; font-weight: 600; margin-bottom: 4px; }}
.jverdict {{ font-size: 13px; color: #57534a; margin-bottom: 12px; }}
.epanel {{ border-top: 1px dashed #ddd9d0; padding-top: 10px; margin-top: 10px; }}
.etitle {{ font-size: 10.5px; text-transform: uppercase; letter-spacing: 0.08em; color: #9b968b; margin-bottom: 7px; }}
.cert {{ border-left: 3px solid #1F6F54; padding: 6px 10px; background: #f4f7f5; border-radius: 0 6px 6px 0; }}
.cert.none {{ border-color: #bbb; background: #f4f3f0; color: #8a8578; font-size: 13px; }}
.cert-head {{ display: flex; gap: 8px; align-items: center; margin-bottom: 3px; }}
.cert-id {{ font-family: ui-monospace, monospace; font-size: 11px; color: #57534a; }}
.cert-type {{ font-size: 11px; color: #6b675e; text-transform: uppercase; }}
.badge {{ margin-left: auto; font-size: 10px; font-weight: 650; text-transform: uppercase;
  letter-spacing: 0.05em; padding: 1px 7px; border-radius: 999px; }}
.badge.ok {{ background: #1F6F54; color: #fff; }}
.badge.no {{ background: #A03030; color: #fff; }}
.cert-summary {{ font-size: 13px; font-weight: 550; }}
.cert-detail {{ font-size: 12.5px; color: #57534a; margin-top: 2px; }}
.trace-line {{ font-size: 12.5px; padding: 3px 0 3px 8px; color: #57534a;
  font-family: ui-monospace, monospace; }}
.trace-line.floor {{ color: #1F6F54; font-weight: 600; }}
.trace-line.bad {{ color: #A03030; font-weight: 600; }}
.drow {{ display: flex; gap: 8px; align-items: baseline; margin-bottom: 2px; }}
.dtype {{ font-size: 10.5px; font-weight: 700; color: #A03030; text-transform: uppercase; letter-spacing: 0.05em; }}
.dtarget {{ font-family: ui-monospace, monospace; font-size: 11px; color: #57534a; }}
.dclaim {{ font-size: 13px; font-weight: 550; }}
.ddetail {{ font-size: 12.5px; color: #57534a; margin-bottom: 8px; }}
@media (max-width: 900px) {{
  main.odologic {{ grid-template-columns: 1fr; }}
}}
</style>
</head>
<body>
{body}
</body>
</html>
"""
    if out_path:
        Path(out_path).write_text(html)
        print(f"wrote {out_path}")
    else:
        print(html)


if __name__ == "__main__":
    inner = "--inner" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    fixture, out = args[0], (args[1] if len(args) > 1 else None)
    render(fixture, out, inner)
