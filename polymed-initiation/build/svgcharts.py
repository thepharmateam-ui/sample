"""Inline-SVG charts for the Polymed report.

Follows the dataviz method: fixed categorical order (CSS vars --s1..--s8), thin bars (<=24px) with a
4px rounded data-end and a square baseline, 2px surface gaps between stacked segments, hairline solid
grid, selective direct labels, legend for >=2 series, text in ink tokens (never series colour),
per-mark hover tips (data-tip + <title>) and a table-view twin rendered by the caller.
All colours are CSS custom properties, so light/dark themes switch without re-rendering.
"""
from html import escape
import math

W = 760  # viewBox width


def nice_ticks(vmax, vmin=0.0, n=5):
    """Clean axis ticks covering [vmin, vmax]."""
    span = vmax - vmin
    if span <= 0:
        span = abs(vmax) or 1.0
    raw = span / n
    mag = 10 ** math.floor(math.log10(raw))
    for m in (1, 2, 2.5, 5, 10):
        step = m * mag
        if span / step <= n:
            break
    lo = math.floor(vmin / step) * step
    hi = math.ceil(vmax / step) * step
    ticks, t = [], lo
    while t <= hi + step * 1e-6:
        ticks.append(round(t, 10))
        t += step
    return ticks


def fmt_tick(v, dec=None):
    if dec is None:
        dec = 0 if abs(v - round(v)) < 1e-9 else (1 if abs(v * 10 - round(v * 10)) < 1e-9 else 2)
    return f"{v:,.{dec}f}"


def _bar_path_v(x, y_top, w, y_base, r=4):
    """Vertical bar: rounded top (data end), square baseline. Handles negative bars (rounded bottom)."""
    h = y_base - y_top
    if abs(h) < 0.5:
        return ""
    if h > 0:
        r = min(r, h, w / 2)
        return (f"M{x:.2f},{y_base:.2f}V{y_top + r:.2f}Q{x:.2f},{y_top:.2f} {x + r:.2f},{y_top:.2f}"
                f"H{x + w - r:.2f}Q{x + w:.2f},{y_top:.2f} {x + w:.2f},{y_top + r:.2f}V{y_base:.2f}Z")
    # negative: base above, data end below
    y_end = y_top
    y0 = y_base
    r = min(r, y_end - y0 if y_end > y0 else -h, w / 2)
    return (f"M{x:.2f},{y0:.2f}V{y_end - r:.2f}Q{x:.2f},{y_end:.2f} {x + r:.2f},{y_end:.2f}"
            f"H{x + w - r:.2f}Q{x + w:.2f},{y_end:.2f} {x + w:.2f},{y_end - r:.2f}V{y0:.2f}Z")


def _rect_path(x, y, w, h):
    if h <= 0.3 or w <= 0.3:
        return ""
    return f"M{x:.2f},{y:.2f}h{w:.2f}v{h:.2f}h{-w:.2f}Z"


def _bar_path_h(x_base, y, x_end, h, r=4):
    """Horizontal bar: square at baseline (left), rounded data end (right)."""
    w = x_end - x_base
    if w < 0.5:
        return ""
    r = min(r, w, h / 2)
    return (f"M{x_base:.2f},{y:.2f}H{x_end - r:.2f}Q{x_end:.2f},{y:.2f} {x_end:.2f},{y + r:.2f}"
            f"V{y + h - r:.2f}Q{x_end:.2f},{y + h:.2f} {x_end - r:.2f},{y + h:.2f}H{x_base:.2f}Z")


def legend_html(names, kind="rect"):
    items = []
    for i, n in enumerate(names):
        sw = (f'<svg width="14" height="10" aria-hidden="true"><rect x="0" y="1" width="14" height="8" rx="2" fill="var(--s{i % 8 + 1})"/></svg>'
              if kind == "rect" else
              f'<svg width="16" height="10" aria-hidden="true"><line x1="0" y1="5" x2="16" y2="5" stroke="var(--s{i % 8 + 1})" stroke-width="2.5" stroke-linecap="round"/></svg>')
        items.append(f'<span class="lg-item">{sw}<span>{escape(n)}</span></span>')
    return f'<div class="legend">{"".join(items)}</div>'


def column_chart(cats, series, unit="", stacked=False, dec=1, height=300, label_last=True, label_all=False,
                 totals=False, colors=None):
    """Vertical columns. series: [{'name','values':[float|None],'tips':[str]}]."""
    n_c, n_s = len(cats), len(series)
    colors = colors or [f"var(--s{i % 8 + 1})" for i in range(n_s)]
    pad_l, pad_r, pad_t, pad_b = 46, 12, 22, 34
    ph = height - pad_t - pad_b
    pw = W - pad_l - pad_r
    if stacked:
        pos = [sum(max(0, s["values"][j] or 0) for s in series) for j in range(n_c)]
        neg = [sum(min(0, s["values"][j] or 0) for s in series) for j in range(n_c)]
        vmax, vmin = max(pos + [0]), min(neg + [0])
    else:
        vals = [v for s in series for v in s["values"] if v is not None]
        vmax, vmin = max(vals + [0]), min(vals + [0])
    ticks = nice_ticks(vmax * 1.08 if vmax > 0 else vmax, vmin * 1.08 if vmin < 0 else 0)
    t0, t1 = ticks[0], ticks[-1]
    sy = lambda v: pad_t + ph - (v - t0) / (t1 - t0) * ph
    band = pw / n_c
    out = [f'<svg viewBox="0 0 {W} {height}" class="chart" role="img" preserveAspectRatio="xMidYMid meet">']
    for t in ticks:
        y = sy(t)
        cls = "base" if abs(t) < 1e-12 else "grid"
        out.append(f'<line class="{cls}" x1="{pad_l}" x2="{W - pad_r}" y1="{y:.2f}" y2="{y:.2f}"/>')
        out.append(f'<text class="tick" x="{pad_l - 6}" y="{y + 4:.2f}" text-anchor="end">{fmt_tick(t)}</text>')
    if unit:
        out.append(f'<text class="unit" x="{pad_l - 6}" y="{pad_t - 9}" text-anchor="end">{escape(unit)}</text>')
    y0 = sy(0)
    for j, c in enumerate(cats):
        cx = pad_l + band * j
        out.append(f'<text class="tick" x="{cx + band / 2:.2f}" y="{height - pad_b + 18}" text-anchor="middle">{escape(str(c))}</text>')
        if stacked:
            bw = min(24, band * 0.56)
            bw = min(bw, 24) if n_c > 12 else bw
            x = cx + (band - bw) / 2
            acc_p, acc_n = 0.0, 0.0
            top_idx = max([i for i, s in enumerate(series) if (s["values"][j] or 0) > 0] or [-1])
            for i, s in enumerate(series):
                v = s["values"][j]
                if v is None or v == 0:
                    continue
                if v > 0:
                    yb, yt = sy(acc_p), sy(acc_p + v)
                    acc_p += v
                    # 2px surface gap: shave 1px each side except at baseline
                    gap_b = 1.0 if acc_p - v > 0 else 0.0
                    path = (_bar_path_v(x, yt + (0 if i == top_idx else 1.0), bw, yb - gap_b)
                            if i == top_idx else _rect_path(x, yt + 1.0, bw, (yb - gap_b) - (yt + 1.0)))
                else:
                    yb, yt = sy(acc_n), sy(acc_n + v)
                    acc_n += v
                    path = _rect_path(x, yb + 1.0, bw, yt - yb - 1.0)
                tip = s.get("tips", [None] * n_c)[j] or f"{c} · {s['name']}: {fmt_tick(v, dec)}"
                out.append(f'<path d="{path}" fill="{colors[i]}" class="mark" data-tip="{escape(tip)}"><title>{escape(tip)}</title></path>')
            if totals:
                tot = sum((s["values"][j] or 0) for s in series)
                out.append(f'<text class="val" x="{x + bw / 2:.2f}" y="{sy(acc_p) - 6:.2f}" text-anchor="middle">{fmt_tick(tot, dec)}</text>')
        else:
            gw = band * 0.72
            bw = min(24, gw / n_s - 2)
            gx = cx + (band - (bw * n_s + 2 * (n_s - 1))) / 2
            for i, s in enumerate(series):
                v = s["values"][j]
                if v is None:
                    continue
                x = gx + i * (bw + 2)
                path = _bar_path_v(x, sy(v), bw, y0) if v >= 0 else _bar_path_v(x, sy(v), bw, y0)
                tip = s.get("tips", [None] * n_c)[j] or f"{c} · {s['name']}: {fmt_tick(v, dec)}"
                out.append(f'<path d="{path}" fill="{colors[i]}" class="mark" data-tip="{escape(tip)}"><title>{escape(tip)}</title></path>')
                show = label_all or (label_last and j == n_c - 1)
                if show:
                    ty = sy(v) - 6 if v >= 0 else sy(v) + 14
                    out.append(f'<text class="val" x="{x + bw / 2:.2f}" y="{ty:.2f}" text-anchor="middle">{fmt_tick(v, dec)}</text>')
    out.append("</svg>")
    leg = legend_html([s["name"] for s in series]) if n_s >= 2 else ""
    return leg + "".join(out)


def hbar_chart(cats, series, unit="", stacked=False, dec=1, row_h=30, label=True, share=False, colors=None,
               label_w=190):
    """Horizontal bars; share=True draws 100% stacked bars (values are shares in %)."""
    n_c, n_s = len(cats), len(series)
    colors = colors or [f"var(--s{i % 8 + 1})" for i in range(n_s)]
    pad_l, pad_r, pad_t, pad_b = label_w, 56, 24, 26
    height = pad_t + pad_b + row_h * n_c
    pw = W - pad_l - pad_r
    if share:
        vmax = 100.0
    elif stacked:
        vmax = max(sum(max(0, s["values"][j] or 0) for s in series) for j in range(n_c))
    else:
        vmax = max(v for s in series for v in s["values"] if v is not None)
    ticks = nice_ticks(vmax if share else vmax * 1.05, 0)
    t1 = ticks[-1]
    sx = lambda v: pad_l + v / t1 * pw
    out = [f'<svg viewBox="0 0 {W} {height}" class="chart" role="img" preserveAspectRatio="xMidYMid meet">']
    for t in ticks:
        x = sx(t)
        cls = "base" if t == 0 else "grid"
        out.append(f'<line class="{cls}" x1="{x:.2f}" x2="{x:.2f}" y1="{pad_t}" y2="{height - pad_b}"/>')
        out.append(f'<text class="tick" x="{x:.2f}" y="{height - pad_b + 16}" text-anchor="middle">{fmt_tick(t)}</text>')
    if unit and not share:
        out.append(f'<text class="unit" x="{W - pad_r}" y="{pad_t - 8}" text-anchor="end">{escape(unit)}</text>')
    for j, c in enumerate(cats):
        y = pad_t + row_h * j
        bh = min(18, row_h * 0.6)
        by = y + (row_h - bh) / 2
        out.append(f'<text class="cat" x="{pad_l - 8}" y="{by + bh / 2 + 4:.2f}" text-anchor="end">{escape(str(c))}</text>')
        if stacked or share:
            acc = 0.0
            last = max([i for i, s in enumerate(series) if (s["values"][j] or 0) > 0] or [-1])
            for i, s in enumerate(series):
                v = s["values"][j]
                if not v:
                    continue
                x0, x1 = sx(acc) + (1 if acc > 0 else 0), sx(acc + v) - (0 if i == last else 1)
                acc += v
                path = _bar_path_h(x0, by, x1, bh) if i == last else _rect_path(x0, by, x1 - x0, bh)
                tip = s.get("tips", [None] * n_c)[j] or f"{c} · {s['name']}: {fmt_tick(v, dec)}{'%' if share else ''}"
                out.append(f'<path d="{path}" fill="{colors[i]}" class="mark" data-tip="{escape(tip)}"><title>{escape(tip)}</title></path>')
                if share and (x1 - x0) > 34:
                    out.append(f'<text class="inlbl on{i % 8 + 1}" x="{(x0 + x1) / 2:.2f}" y="{by + bh / 2 + 4:.2f}" text-anchor="middle">{fmt_tick(v, 0)}%</text>')
        else:
            for i, s in enumerate(series):
                v = s["values"][j]
                if v is None:
                    continue
                sub_h = bh / n_s
                yy = by + i * sub_h
                path = _bar_path_h(sx(0), yy + (1 if n_s > 1 else 0), sx(v), sub_h - (2 if n_s > 1 else 0))
                tip = s.get("tips", [None] * n_c)[j] or f"{c} · {s['name']}: {fmt_tick(v, dec)}"
                out.append(f'<path d="{path}" fill="{colors[i]}" class="mark" data-tip="{escape(tip)}"><title>{escape(tip)}</title></path>')
                if label:
                    out.append(f'<text class="val" x="{sx(v) + 5:.2f}" y="{yy + sub_h / 2 + 4:.2f}" text-anchor="start">{fmt_tick(v, dec)}</text>')
    out.append("</svg>")
    leg = legend_html([s["name"] for s in series]) if n_s >= 2 else ""
    return leg + "".join(out)


def line_chart(cats, series, unit="", dec=1, height=280, label_end=True, ymin=None):
    n_c, n_s = len(cats), len(series)
    pad_l, pad_r, pad_t, pad_b = 46, 70, 22, 34
    ph, pw = height - pad_t - pad_b, W - pad_l - pad_r
    vals = [v for s in series for v in s["values"] if v is not None]
    lo = min(vals) if ymin is None else ymin
    lo = min(lo, 0) if ymin is None and min(vals) < 0 else lo
    ticks = nice_ticks(max(vals) * 1.05, lo if ymin is not None else min(0, min(vals)))
    t0, t1 = ticks[0], ticks[-1]
    sy = lambda v: pad_t + ph - (v - t0) / (t1 - t0) * ph
    sx = lambda j: pad_l + (pw * j / (n_c - 1) if n_c > 1 else pw / 2)
    out = [f'<svg viewBox="0 0 {W} {height}" class="chart" role="img" preserveAspectRatio="xMidYMid meet">']
    for t in ticks:
        y = sy(t)
        out.append(f'<line class="{"base" if t == ticks[0] else "grid"}" x1="{pad_l}" x2="{W - pad_r}" y1="{y:.2f}" y2="{y:.2f}"/>')
        out.append(f'<text class="tick" x="{pad_l - 6}" y="{y + 4:.2f}" text-anchor="end">{fmt_tick(t)}</text>')
    if unit:
        out.append(f'<text class="unit" x="{pad_l - 6}" y="{pad_t - 9}" text-anchor="end">{escape(unit)}</text>')
    step = max(1, math.ceil(n_c / 12))
    for j, c in enumerate(cats):
        if j % step == 0 or j == n_c - 1:
            out.append(f'<text class="tick" x="{sx(j):.2f}" y="{height - pad_b + 18}" text-anchor="middle">{escape(str(c))}</text>')
    for i, s in enumerate(series):
        col = f"var(--s{i % 8 + 1})"
        pts = [(sx(j), sy(v)) for j, v in enumerate(s["values"]) if v is not None]
        if len(pts) > 1:
            d = "M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in pts)
            out.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>')
        for j, v in enumerate(s["values"]):
            if v is None:
                continue
            tip = s.get("tips", [None] * n_c)[j] or f"{cats[j]} · {s['name']}: {fmt_tick(v, dec)}"
            out.append(f'<circle cx="{sx(j):.2f}" cy="{sy(v):.2f}" r="4" fill="{col}" stroke="var(--surface)" stroke-width="2" class="mark" data-tip="{escape(tip)}"><title>{escape(tip)}</title></circle>')
        last = [(j, v) for j, v in enumerate(s["values"]) if v is not None][-1]
        if label_end:
            out.append(f'<text class="val" x="{sx(last[0]) + 8:.2f}" y="{sy(last[1]) + 4:.2f}">{fmt_tick(last[1], dec)}</text>')
    out.append("</svg>")
    leg = legend_html([s["name"] for s in series], kind="line") if n_s >= 2 else ""
    return leg + "".join(out)
