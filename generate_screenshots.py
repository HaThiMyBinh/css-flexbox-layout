import os
from PIL import Image, ImageDraw, ImageFont

def get_font(name, size):
    try:
        path = os.path.join("C:/Windows/Fonts", name)
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    except Exception:
        pass
    return ImageFont.load_default()

font_title = get_font("segoeuib.ttf", 22)
font_h2 = get_font("segoeuib.ttf", 16)
font_body = get_font("segoeui.ttf", 13)
font_body_b = get_font("segoeuib.ttf", 13)
font_small = get_font("segoeui.ttf", 11)
font_tab = get_font("segoeui.ttf", 12)
font_badge = get_font("segoeuib.ttf", 11)

def draw_browser_frame(draw, width, height, title, url):
    draw.rectangle([0, 0, width, 70], fill="#e2e8f0")
    draw.ellipse([14, 12, 24, 22], fill="#ef4444")
    draw.ellipse([30, 12, 40, 22], fill="#f59e0b")
    draw.ellipse([46, 12, 56, 22], fill="#10b981")

    draw.rounded_rectangle([68, 6, 320, 36], radius=5, fill="#ffffff")
    draw.text((82, 12), title, fill="#1e293b", font=font_tab)

    draw.rectangle([0, 36, width, 70], fill="#ffffff")
    draw.line([0, 36, width, 36], fill="#cbd5e1", width=1)
    draw.line([0, 70, width, 70], fill="#e2e8f0", width=1)

    draw.polygon([(14, 53), (20, 48), (20, 58)], fill="#64748b")
    draw.polygon([(34, 53), (28, 48), (28, 58)], fill="#64748b")

    draw.rounded_rectangle([50, 41, width - 15, 65], radius=11, fill="#f1f5f9", outline="#cbd5e1", width=1)
    draw.text((65, 45), url, fill="#475569", font=font_small)

def draw_mobile_frame(draw, x, y, width, height):
    draw.rounded_rectangle([x, y, x + width, y + height], radius=28, fill="#1e293b", outline="#334155", width=3)
    screen_x = x + 10
    screen_y = y + 10
    screen_w = width - 20
    screen_h = height - 20
    draw.rounded_rectangle([screen_x, screen_y, screen_x + screen_w, screen_y + screen_h], radius=20, fill="#ffffff")

    notch_w = 90
    notch_h = 18
    notch_x = screen_x + (screen_w - notch_w) // 2
    draw.rounded_rectangle([notch_x, screen_y + 6, notch_x + notch_w, screen_y + 6 + notch_h], radius=9, fill="#0f172a")

    return screen_x, screen_y + 30, screen_w, screen_h - 35

# 1. Desktop Screenshot
def render_desktop_screenshot(out_path):
    w, h = 1000, 700
    img = Image.new("RGB", (w, h), color="#ffffff")
    draw = ImageDraw.Draw(img)

    draw_browser_frame(draw, w, h, "Flexbox Layout - Desktop View", "http://localhost:5500/index.html (Desktop > 768px)")

    # 1. Header (#333)
    hh = 75
    draw.rectangle([0, 70, w, 70 + hh], fill="#333333")
    draw.text((w // 2 - 40, 70 + 14), "Header", fill="#ffffff", font=font_title)
    draw.text((w // 2 - 130, 70 + 46), "Bố cục trang web Responsive với CSS Flexbox", fill="#bbbbbb", font=font_small)

    # 2. Navigation (#444)
    nav_y = 70 + hh
    nav_h = 42
    draw.rectangle([0, nav_y, w, nav_y + nav_h], fill="#444444")
    
    menus = [("Trang chủ", True), ("Tin tức", False), ("Dịch vụ", False), ("Giới thiệu", False), ("Liên hệ", False)]
    mx = w // 2 - 190
    for txt, is_act in menus:
        bbox = draw.textbbox((0, 0), txt, font=font_body_b if is_act else font_body)
        tw = bbox[2] - bbox[0] + 20
        if is_act:
            draw.rounded_rectangle([mx, nav_y + 6, mx + tw, nav_y + nav_h - 6], radius=4, fill="#007bff")
            draw.text((mx + 10, nav_y + 11), txt, fill="#ffffff", font=font_body_b)
        else:
            draw.text((mx + 10, nav_y + 11), txt, fill="#eeeeee", font=font_body)
        mx += tw + 10

    # Footer height
    footer_h = 55
    footer_y = h - footer_h

    # 3. Middle: .main-container (display: flex; flex: 1)
    mid_y = nav_y + nav_h
    mid_h = footer_y - mid_y

    content_w = int(w * 0.75)  # flex: 3 (75%)
    sidebar_w = w - content_w  # flex: 1 (25%)

    # Content
    draw.rectangle([0, mid_y, content_w, footer_y], fill="#ffffff")
    draw.text((30, mid_y + 24), "Main Content (flex: 3)", fill="#111111", font=font_h2)
    draw.text((30, mid_y + 54), "Khu vực hiển thị nội dung chính bài viết. Chiếm 3/4 (75%) chiều rộng.", fill="#4b5563", font=font_body)

    # Content box
    cb_y = mid_y + 88
    draw.rounded_rectangle([30, cb_y, content_w - 30, cb_y + 180], radius=6, fill="#f8fafc", outline="#cbd5e1", width=1)
    draw.rectangle([30, cb_y, 35, cb_y + 180], fill="#007bff")
    draw.text((45, cb_y + 14), "Cấu trúc Flexbox trên Desktop:", fill="#007bff", font=font_body_b)
    b_lines = [
        "• .container: display: flex; flex-direction: column; (Header → Nav → Main → Footer)",
        "• .main-container: display: flex; flex: 1; (Xếp Content và Sidebar theo hàng ngang)",
        "• .content: flex: 3; (Chiếm 3 phần chiều rộng)",
        "• .sidebar: flex: 1; (Chiếm 1 phần chiều rộng)"
    ]
    by = cb_y + 42
    for bl in b_lines:
        draw.text((45, by), bl, fill="#374151", font=font_small)
        by += 22

    # Sidebar
    draw.rectangle([content_w, mid_y, w, footer_y], fill="#f4f4f4")
    draw.line([content_w, mid_y, content_w, footer_y], fill="#e0e0e0", width=1)

    draw.text((content_w + 24, mid_y + 24), "Sidebar (flex: 1)", fill="#222222", font=font_h2)
    draw.line([content_w + 24, mid_y + 48, w - 24, mid_y + 48], fill="#dddddd", width=2)

    # Widget
    draw.rounded_rectangle([content_w + 20, mid_y + 65, w - 20, mid_y + 175], radius=6, fill="#ffffff", outline="#e2e8f0", width=1)
    draw.text((content_w + 32, mid_y + 78), "Tin tức mới:", fill="#1e293b", font=font_body_b)
    news = ["• Làm chủ Flexbox", "• Flexbox vs CSS Grid", "• Responsive Design"]
    ny = mid_y + 104
    for n in news:
        draw.text((content_w + 32, ny), n, fill="#007bff", font=font_small)
        ny += 20

    # 4. Footer (#333)
    draw.rectangle([0, footer_y, w, h], fill="#333333")
    draw.text((w // 2 - 160, footer_y + 18), "Footer (c) 2026 - CSS Flexbox Responsive Layout Practice", fill="#ffffff", font=font_body)

    img.save(out_path)
    print(f"Saved Desktop: {out_path}")

# 2. Mobile Screenshot
def render_mobile_screenshot(out_path):
    w, h = 480, 800
    img = Image.new("RGB", (w, h), color="#f8fafc")
    draw = ImageDraw.Draw(img)

    sx, sy, sw, sh = draw_mobile_frame(draw, 40, 20, w - 80, h - 40)

    # 1. Header
    m_hh = 65
    draw.rectangle([sx, sy, sx + sw, sy + m_hh], fill="#333333")
    draw.text((sx + sw // 2 - 35, sy + 14), "Header", fill="#ffffff", font=font_h2)
    draw.text((sx + sw // 2 - 75, sy + 40), "Flexbox Layout (Mobile)", fill="#bbbbbb", font=font_small)

    # 2. Nav
    nav_y = sy + m_hh
    nav_h = 36
    draw.rectangle([sx, nav_y, sx + sw, nav_y + nav_h], fill="#444444")
    draw.text((sx + 14, nav_y + 9), "[Trang chủ]  [Tin tức]  [Dịch vụ]  [Liên hệ]", fill="#eeeeee", font=font_small)

    curr_y = nav_y + nav_h

    # 3. Content
    ct_h = 240
    draw.rectangle([sx, curr_y, sx + sw, curr_y + ct_h], fill="#ffffff")
    draw.text((sx + 16, curr_y + 14), "Main Content (flex-direction: column)", fill="#111111", font=font_h2)
    draw.text((sx + 16, curr_y + 38), "Trên màn hình <= 768px, .main-container chuyển sang", fill="#4b5563", font=font_small)
    draw.text((sx + 16, curr_y + 54), "flex-direction: column để xếp dọc.", fill="#4b5563", font=font_small)

    # Code note on mobile
    mc_y = curr_y + 78
    draw.rounded_rectangle([sx + 14, mc_y, sx + sw - 14, mc_y + 145], radius=6, fill="#f8fafc", outline="#cbd5e1", width=1)
    draw.text((sx + 24, mc_y + 10), "Media Query áp dụng:", fill="#007bff", font=font_body_b)
    m_lines = [
        "@media (max-width: 768px) {",
        "  .main-container {",
        "    flex-direction: column;",
        "  }",
        "  /* Sidebar xếp xuống dưới Content */",
        "}"
    ]
    my = mc_y + 32
    for ml in m_lines:
        draw.text((sx + 24, my), ml, fill="#374151", font=font_small)
        my += 16

    curr_y += ct_h

    # 4. Sidebar (stacked under content)
    sb_h = 160
    draw.rectangle([sx, curr_y, sx + sw, curr_y + sb_h], fill="#f4f4f4")
    draw.line([sx, curr_y, sx + sw, curr_y], fill="#e0e0e0", width=1)
    draw.text((sx + 16, curr_y + 12), "Sidebar (Xếp dưới Main Content)", fill="#222222", font=font_body_b)
    draw.text((sx + 16, curr_y + 34), "• Tin tức: Làm chủ Flexbox trong 30 phút", fill="#007bff", font=font_small)
    draw.text((sx + 16, curr_y + 50), "• Tin tức: Flexbox vs CSS Grid", fill="#007bff", font=font_small)

    draw.rounded_rectangle([sx + 14, curr_y + 75, sx + sw - 14, curr_y + 145], radius=4, fill="#eef2ff", outline="#c7d2fe", width=1)
    draw.text((sx + 22, curr_y + 85), "Quảng cáo: Khóa học Frontend", fill="#4338ca", font=font_body_b)
    draw.text((sx + 22, curr_y + 105), "HTML5, CSS3, Flexbox, Responsive Web.", fill="#475569", font=font_small)

    # 5. Footer
    draw.rectangle([sx, sy + sh - 50, sx + sw, sy + sh], fill="#333333")
    draw.text((sx + sw // 2 - 80, sy + sh - 32), "Footer (c) 2026 - Flexbox Layout", fill="#ffffff", font=font_small)

    img.save(out_path)
    print(f"Saved Mobile: {out_path}")

# 3. Combined Overview
def render_combined_screenshot(out_path):
    w, h = 1100, 750
    img = Image.new("RGB", (w, h), color="#f8fafc")
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, w, 75], fill="#1e293b")
    draw.text((30, 22), "CSS Flexbox Layout: Bố cục Responsive trên Desktop & Mobile", fill="#ffffff", font=font_title)

    # Left: Desktop (660px)
    d_x, d_y, d_w, d_h = 30, 95, 660, 580
    draw.rounded_rectangle([d_x, d_y, d_x + d_w, d_y + d_h], radius=8, fill="#ffffff", outline="#cbd5e1", width=1)
    draw.rounded_rectangle([d_x + 15, d_y + 12, d_x + 130, d_y + 36], radius=12, fill="#007bff")
    draw.text((d_x + 28, d_y + 16), "DESKTOP", fill="#ffffff", font=font_badge)
    draw.text((d_x + 145, d_y + 14), "Màn hình rộng (> 768px): Content (flex: 3) + Sidebar (flex: 1)", fill="#1e293b", font=font_body_b)

    # Desktop mock
    px = d_x + 15
    pw = d_w - 30

    # Header
    draw.rounded_rectangle([px, d_y + 50, px + pw, d_y + 105], radius=4, fill="#333333")
    draw.text((px + pw // 2 - 25, d_y + 68), "Header", fill="#ffffff", font=font_h2)

    # Nav
    draw.rounded_rectangle([px, d_y + 110, px + pw, d_y + 145], radius=4, fill="#444444")
    draw.text((px + 20, d_y + 120), "Navigation: [Trang chủ]  [Tin tức]  [Dịch vụ]  [Liên hệ]", fill="#eeeeee", font=font_small)

    # Mid container
    sb_w = int(pw * 0.28)
    ct_w = pw - sb_w - 6
    mid_top = d_y + 150
    mid_bottom = d_y + 490

    # Content (flex: 3)
    draw.rounded_rectangle([px, mid_top, px + ct_w, mid_bottom], radius=4, fill="#ffffff", outline="#cbd5e1", width=1)
    draw.text((px + 16, mid_top + 16), "Main Content (flex: 3)", fill="#111111", font=font_h2)
    draw.text((px + 16, mid_top + 44), "Chiếm 75% chiều rộng hàng ngang.", fill="#4b5563", font=font_small)
    draw.text((px + 16, mid_top + 70), "display: flex; flex: 3;", fill="#007bff", font=font_body_b)

    # Sidebar (flex: 1)
    draw.rounded_rectangle([px + ct_w + 6, mid_top, px + pw, mid_bottom], radius=4, fill="#f4f4f4", outline="#cbd5e1", width=1)
    draw.text((px + ct_w + 16, mid_top + 16), "Sidebar (flex: 1)", fill="#222222", font=font_body_b)
    draw.text((px + ct_w + 16, mid_top + 40), "Chiếm 25% chiều rộng.", fill="#4b5563", font=font_small)
    draw.text((px + ct_w + 16, mid_top + 65), "• Tin mới 1", fill="#007bff", font=font_small)
    draw.text((px + ct_w + 16, mid_top + 85), "• Tin mới 2", fill="#007bff", font=font_small)

    # Footer
    draw.rounded_rectangle([px, d_y + 496, px + pw, d_y + 550], radius=4, fill="#333333")
    draw.text((px + pw // 2 - 25, d_y + 514), "Footer", fill="#ffffff", font=font_h2)

    # Right: Mobile (350px)
    m_x, m_y, m_w, m_h = 720, 95, 350, 580
    draw.rounded_rectangle([m_x, m_y, m_x + m_w, m_y + m_h], radius=8, fill="#ffffff", outline="#cbd5e1", width=1)
    draw.rounded_rectangle([m_x + 15, m_y + 12, m_x + 115, m_y + 36], radius=12, fill="#10b981")
    draw.text((m_x + 28, m_y + 16), "MOBILE", fill="#ffffff", font=font_badge)
    draw.text((m_x + 130, m_y + 14), "Xếp dọc 1 cột (<= 768px)", fill="#1e293b", font=font_body_b)

    mpx = m_x + 15
    mpw = m_w - 30

    # Header
    draw.rounded_rectangle([mpx, m_y + 50, mpx + mpw, m_y + 95], radius=4, fill="#333333")
    draw.text((mpx + mpw // 2 - 25, m_y + 64), "Header", fill="#ffffff", font=font_body_b)

    # Nav
    draw.rounded_rectangle([mpx, m_y + 100, mpx + mpw, m_y + 135], radius=4, fill="#444444")
    draw.text((mpx + 10, m_y + 110), "Navigation: [Menu di động]", fill="#eeeeee", font=font_small)

    # Content
    draw.rounded_rectangle([mpx, m_y + 140, mpx + mpw, m_y + 310], radius=4, fill="#ffffff", outline="#cbd5e1", width=1)
    draw.text((mpx + 14, m_y + 152), "Main Content", fill="#111111", font=font_body_b)
    draw.text((mpx + 14, m_y + 176), "flex-direction: column;", fill="#007bff", font=font_small)
    draw.text((mpx + 14, m_y + 196), "Nội dung chính hiển thị trước,", fill="#4b5563", font=font_small)
    draw.text((mpx + 14, m_y + 214), "chiếm trọn 100% chiều rộng.", fill="#4b5563", font=font_small)

    # Sidebar
    draw.rounded_rectangle([mpx, m_y + 316, mpx + mpw, m_y + 450], radius=4, fill="#f4f4f4", outline="#cbd5e1", width=1)
    draw.text((mpx + 14, m_y + 328), "Sidebar (Xếp xuống dưới)", fill="#222222", font=font_body_b)
    draw.text((mpx + 14, m_y + 352), "• Tin tức & Quảng cáo", fill="#007bff", font=font_small)

    # Footer
    draw.rounded_rectangle([mpx, m_y + 456, mpx + mpw, m_y + 500], radius=4, fill="#333333")
    draw.text((mpx + mpw // 2 - 20, m_y + 470), "Footer", fill="#ffffff", font=font_body_b)

    draw.text((w // 2 - 140, h - 30), "CSS Flexbox Practice • Responsive Web Layout", fill="#94a3b8", font=font_small)

    img.save(out_path)
    print(f"Saved Combined: {out_path}")

if __name__ == "__main__":
    base_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\css-flexbox-layout"
    render_desktop_screenshot(os.path.join(base_dir, "screenshot_desktop.png"))
    render_mobile_screenshot(os.path.join(base_dir, "screenshot_mobile.png"))
    render_combined_screenshot(os.path.join(base_dir, "tat_ca_giao_dien.png"))
