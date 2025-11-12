# 🤙 BRUTALIST CONTENT GUIDE
## How to Use Your Legendary Content Elements

Version 15 introduces comprehensive brutalist styling for all your newsletter and post content. Here's how to use every element:

---

## 📦 SECTION DIVIDERS

**What it does:** Creates a rainbow-colored horizontal bar using all your brand colors

**How to use in Ghost:**
```html
---
```

Just use a standard markdown horizontal rule (three dashes). It will render as a chunky 20px bar with:
- Hot Pink → Sky Blue → Sunshine Yellow → Purple → Lime gradient
- 4px black borders top and bottom
- 4px drop shadow

**Works in:** Web posts ✅ | Email ✅

---

## 🗣️ QUOTE BLOCKS

**What it does:** Massive brutalist quotes with hot pink background

**How to use in Ghost:**
```markdown
> Your inspiring quote here. This will render with maximum impact!
```

**Styling:**
- Hot pink background (`#FF1493`)
- 4px black border all around
- 6px drop shadow
- Giant quotation mark watermark
- Bold, heavy weight text

**Works in:** Web posts ✅ | Email ✅

---

## 📅 CALENDAR BULLET POINTS

**What it does:** Special list items perfect for event dates and schedules

**How to use in Ghost:**
```html
<ul class="calendar-list">
  <li><strong>MON, DEC 16</strong> - Holiday Market at Grand Park (Free!)</li>
  <li><strong>TUE, DEC 17</strong> - Live Jazz at The Blue Whale (8pm)</li>
  <li><strong>WED, DEC 18</strong> - Taco Tuesday Tour starts in Boyle Heights</li>
</ul>
```

**Styling:**
- 📅 emoji automatically added to each item
- Date in strong = Sunshine yellow badge with black border
- 4px bordered boxes for each event
- 4px drop shadow

**Pro tip:** First `<strong>` tag in each list item becomes the date badge!

**Works in:** Web posts ✅ | Email ⚠️ (simplified)

---

## 🎪 EVENT CARDS

**What it does:** Full-featured brutalist event cards with metadata

**How to use in Ghost HTML:**
```html
<div class="event-card">
  <div class="event-card-title">Echo Park Rising Festival</div>
  <div class="event-card-meta">
    <span class="event-card-meta-item">📅 SAT, JAN 20</span>
    <span class="event-card-meta-item">🕐 2PM - 10PM</span>
    <span class="event-card-meta-item">📍 Echo Park</span>
    <span class="event-card-meta-item">💵 $25</span>
  </div>
  <div class="event-card-description">
    The biggest local music festival returns! 50+ bands across 10 venues.
    Support local LA artists while discovering your new favorite band.
  </div>
</div>
```

**Styling:**
- Cream background with 4px borders
- 8px drop shadow (lifts on hover!)
- Each meta item gets different color (lime → blue → yellow → pink)
- Uppercase title with thick underline

**Works in:** Web posts ✅ | Email ❌ (use calendar list instead)

---

## 🍟 IMAGE CAPTIONS (for EATS posts!)

**What it does:** Chunky brutalist caption boxes attached to images

**How to use in Ghost:**
```html
<figure>
  <img src="your-taco-photo.jpg" alt="Best al pastor in LA">
  <figcaption>Leo's Tacos Truck - $3.50 per taco, cash only. Open till 3am. 📍 Venice & La Brea</figcaption>
</figure>
```

**Styling:**
- Image gets 4px black border (no bottom border)
- Caption box attached seamlessly below
- Sunshine yellow background
- 4px black border continuation
- 4px drop shadow
- Bold, readable text

**Perfect for:** Eats posts, photo essays, food tours

**Works in:** Web posts ✅ | Email ✅

---

## 🎬 MEDIA EMBEDS (YouTube, GIFs)

**What it does:** Frames videos and embeds with thick borders

**How to use in Ghost:**

Just paste a YouTube URL in the editor, Ghost will auto-embed it. Or use HTML:

```html
<iframe width="560" height="315"
  src="https://www.youtube.com/embed/VIDEO_ID"
  frameborder="0" allowfullscreen>
</iframe>
```

**Styling:**
- 4px black border around entire embed
- 6px drop shadow
- Centered on page
- Responsive width

**Works in:** Web posts ✅ | Email ⚠️ (some clients block iframes)

---

## 💡 CALLOUT BOXES

**What it does:** Highlight important info with colored boxes

**How to use in Ghost HTML:**
```html
<div class="callout-box">
  <strong>PRO TIP:</strong> Get there before 6pm for half-price happy hour!
</div>

<!-- Color variants -->
<div class="callout-box pink">Hot pink background</div>
<div class="callout-box blue">Sky blue background</div>
<div class="callout-box yellow">Sunshine yellow background</div>
<div class="callout-box purple">Purple background (white text)</div>
```

**Styling:**
- 💡 emoji badge floats above box
- Default: lime green background
- 4px borders + 6px shadow
- Available in all 5 brand colors

**Use for:** Pro tips, warnings, special announcements, CTAs

**Works in:** Web posts ✅ | Email ❌ (use blockquote instead)

---

## 📝 HEADINGS

**H2 - Section Headers:**
```markdown
## This Week in LA
```
- Centered, uppercase
- Thick black underline (6px)
- Font weight 900
- 2rem size

**H3 - Subsection Headers:**
```markdown
### Arts & Culture
```
- Purple left border (8px thick)
- Uppercase
- Font weight 900
- Left-aligned with padding

**H4 - Small Headers:**
```markdown
#### Quick Notes
```
- Uppercase, bold
- No special borders
- Smaller size

**Works in:** Web posts ✅ | Email ✅

---

## ✨ TEXT HIGHLIGHTS

**Bold/Strong Text:**
```markdown
This is **highlighted text** with subtle yellow background
```

**Styling:**
- Font weight 900
- Subtle yellow highlight (30% opacity)
- 2px padding

**Use for:** Emphasis, key phrases, dates, prices

**Works in:** Web posts ✅ | Email ✅

---

## 📋 REGULAR LISTS

**Bullet lists get brutalist treatment automatically:**

```markdown
- First item
- Second item
- Third item
```

**Styling:**
- Purple square bullets (▪)
- Larger bullet size
- Custom spacing
- No default list styling

**Works in:** Web posts ✅ | Email ✅

---

## 🎨 COLOR SYSTEM REFERENCE

All elements use your 5-color brutalist palette:

- **Hot Pink:** `#FF1493` - Quote blocks, event meta items
- **Sky Blue:** `#00D4FF` - Event meta items, links
- **Sunshine Yellow:** `#FFE66D` - Captions, date badges, highlights
- **Purple:** `#8B5CF6` - H3 borders, bullets, header backgrounds
- **Lime:** `#EBF99A` - Callout boxes, event meta items, footer accents

Plus:
- **Cream Background:** `#FFF8E7` - Page background (warm, easy on eyes)
- **Pure Black:** `#000000` - All borders, text, shadows

---

## 📧 EMAIL VS WEB

| Element | Web Posts | Email |
|---------|-----------|-------|
| Section Dividers (HR) | ✅ Full rainbow | ✅ Full rainbow |
| Quote Blocks | ✅ Pink + shadow | ✅ Pink + border |
| Calendar Lists | ✅ Full styling | ⚠️ Simplified |
| Event Cards | ✅ Full interactive | ❌ Use calendar list |
| Image Captions | ✅ Full styling | ✅ Full styling |
| Media Embeds | ✅ Full styling | ⚠️ Client dependent |
| Callout Boxes | ✅ Full styling | ❌ Use blockquote |
| Headings | ✅ Full styling | ✅ Full styling |
| Text Highlights | ✅ Full styling | ✅ Full styling |

---

## 💡 PRO TIPS

1. **Mix colors for visual rhythm:** Alternate between different callout box colors in long posts
2. **Use calendar lists for events:** Even non-calendar events look great in this format
3. **Caption every food photo:** Makes eats posts way more useful
4. **Break up long content with HRs:** Rainbow dividers = visual refresh
5. **Event cards for featured events:** Full cards for main events, calendar lists for quick schedules
6. **Test emails before sending:** Some email clients have quirks

---

## 🚀 QUICK START EXAMPLES

**Newsletter Structure:**
```markdown
## This Week's Hottest Events

---

<ul class="calendar-list">
  <li><strong>FRI, JAN 12</strong> - Night Market at Smorgasburg</li>
  <li><strong>SAT, JAN 13</strong> - Arts District Gallery Crawl</li>
</ul>

---

## Featured: Taco Crawl in Boyle Heights

> "The best tacos in LA aren't in restaurants—they're from trucks and family-run spots that have been perfecting their recipes for decades."

<figure>
  <img src="tacos.jpg" alt="Al pastor tacos">
  <figcaption>Tacos La Azteca - $2.50 each, cash only 📍 César Chávez & Soto</figcaption>
</figure>

---

### Pro Tips for Taco Tourists

- Bring cash (most don't take cards)
- Go before 8pm for freshest ingredients
- Try the agua fresca (horchata is 🔥)
```

---

## 🤙 THAT'S IT!

You now have a complete brutalist content system that works across web and email. Every element uses your brand colors, maintains the chunky aesthetic, and makes content more engaging.

Questions? Check the CSS in `assets/css/screen.css` (lines 1131-1475) for all styling details.