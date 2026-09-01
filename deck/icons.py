# -*- coding: utf-8 -*-
"""Stroke icon set. 24x24, currentColor, so icons take the surrounding text colour
and can never render dark-on-dark the way an emoji glyph can."""

_P = {
 # channels
 "web":      '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a15 15 0 0 1 0 18a15 15 0 0 1 0-18"/>',
 "email":    '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5 12 13l8.5-6.5"/>',
 "search":   '<circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.4 15.4 21 21"/>',
 "chat":     '<path d="M20 4H4a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h3v4l4.5-4H20a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1Z"/>',
 "whatsapp": '<path d="M3.5 20.5 5 16a8 8 0 1 1 3 3l-4.5 1.5Z"/><path d="M9 9.5c0 3 2.5 5.5 5.5 5.5"/>',
 "bell":     '<path d="M18 15V10a6 6 0 1 0-12 0v5l-2 2.5h16L18 15Z"/><path d="M10 20a2 2 0 0 0 4 0"/>',
 "story":    '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="8.5" cy="9.5" r="1.8"/><path d="m3.5 17 5-5 4.5 4.5 3-2.5 4.5 4"/>',
 "phone":    '<rect x="6.5" y="2.5" width="11" height="19" rx="2.5"/><path d="M10.5 18.6h3"/>',
 "sms":      '<path d="M21 5H3v11h4v4l4.5-4H21V5Z"/><path d="M8 10.5h.01M12 10.5h.01M16 10.5h.01"/>',
 # products and objects
 "headset":  '<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="2.5" y="13" width="4" height="6" rx="1.6"/><rect x="17.5" y="13" width="4" height="6" rx="1.6"/><path d="M20 19v.5a2.5 2.5 0 0 1-2.5 2.5H13"/>',
 "wrench":   '<path d="M15.5 3.5a5 5 0 0 0-5.9 6.4L3 16.5 6.5 20l6.6-6.6a5 5 0 0 0 6.4-5.9L16.8 10 14 7.2l1.5-3.7Z"/>',
 "cart":     '<path d="M2.5 3.5h2.6l2.4 11h10l2.4-8H6.5"/><circle cx="9.5" cy="19" r="1.6"/><circle cx="17.5" cy="19" r="1.6"/>',
 "bag":      '<path d="M4.5 8h15l-1.3 12.5H5.8L4.5 8Z"/><path d="M8.5 8V6a3.5 3.5 0 0 1 7 0v2"/>',
 "beauty":   '<rect x="8.5" y="10" width="7" height="11" rx="1.4"/><path d="M10.5 10V5.2a1.5 1.5 0 0 1 3 0V10"/><path d="M8.5 13.5h7"/>',
 "plane":    '<path d="M21.5 15.6v-2.2l-8.2-4.6V3.9a1.4 1.4 0 0 0-2.8 0v4.9L2.3 13.4v2.2l8.2-2.6v3.7l-2.4 1.7v1.7l3.8-1 3.8 1v-1.7l-2.4-1.7V13l8.2 2.6Z"/>',
 "car":      '<path d="M3.5 16v-3.2L6 7.5h12l2.5 5.3V16"/><path d="M2.5 16h19"/><circle cx="7.5" cy="17.5" r="1.8"/><circle cx="16.5" cy="17.5" r="1.8"/>',
 "bank":     '<path d="M3 10 12 4l9 6"/><path d="M4.5 10v8m5-8v8m5-8v8m5-8v8"/><path d="M2.5 20.5h19"/>',
 "antenna":  '<path d="M12 13v8"/><path d="M8 21h8"/><circle cx="12" cy="10" r="2.2"/><path d="M7.6 5.6a6.2 6.2 0 0 0 0 8.8M16.4 5.6a6.2 6.2 0 0 1 0 8.8"/>',
 "tag":      '<path d="M11 3H3v8l10 10 8-8L11 3Z"/><circle cx="7" cy="7" r="1.4"/>',
 "wallet":   '<rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18"/><circle cx="17" cy="14.5" r="1.3"/>',
 "chart":    '<path d="M3.5 20.5h17"/><path d="m5 15 4.5-5 3.5 3.5L20 6"/><path d="M20 10.5V6h-4.5"/>',
 "clock":    '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.2V12l3.2 2"/>',
 "id":       '<rect x="2.5" y="5" width="19" height="14" rx="2"/><circle cx="8.5" cy="11" r="2.2"/><path d="M4.8 16.2a4 4 0 0 1 7.4 0M15 10h4M15 14h3"/>',
 "click":    '<path d="M6 3.5v3M3.5 6h3M17 3.5v2M15.5 4.5h3"/><path d="m10 9 9 4.2-3.9 1.4-1.4 3.9L10 9Z"/>',
 "user":     '<circle cx="12" cy="8" r="3.8"/><path d="M4.5 20.5a7.5 7.5 0 0 1 15 0"/>',
 "key":      '<circle cx="7.5" cy="15" r="4"/><path d="m10.4 12.1 8-8M16 6.5l2.2 2.2M18.4 4.1l2.2 2.2"/>',
 "lock":     '<rect x="4.5" y="10" width="15" height="10.5" rx="2"/><path d="M8 10V7.5a4 4 0 0 1 8 0V10"/>',
 "handshake":'<path d="m2.5 12 3.5-3.5 4 1 2-1 2 1 4-1L21.5 12"/><path d="m6 8.5 4 5 2.5-1.5L15 14l3-5.5"/>',
 "building": '<rect x="4" y="3.5" width="16" height="17" rx="1.5"/><path d="M8 8h2m4 0h2M8 12h2m4 0h2M8 16h2m4 0h2"/>',
 "robot":    '<rect x="4" y="7.5" width="16" height="12" rx="3"/><circle cx="9" cy="13" r="1.4"/><circle cx="15" cy="13" r="1.4"/><path d="M12 7.5V4M9.5 4h5"/>',
 "target":   '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r=".9" fill="currentColor" stroke="none"/>',
}

def icon(name, size=24, sw=1.5):
    p = _P.get(name)
    if p is None:
        raise KeyError(f"no icon {name!r}; have {sorted(_P)}")
    return (f'<svg class="ico" viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" '
            f'stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true">{p}</svg>')

NAMES = sorted(_P)
