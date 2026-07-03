import re

with open("index.html", "r") as f:
    content = f.read()

# Remove style and script tags content, replace with links
content = re.sub(r'<style>.*?</style>', '<link rel="stylesheet" href="style.css">', content, flags=re.DOTALL)
content = re.sub(r'<script>\s*const modelViewer.*?</script>', '<script src="script.js"></script>', content, flags=re.DOTALL)

# Update nav links in the header and footer
nav_replacements = [
    ('href="#home"', 'href="index.html"'),
    ('href="#ingredients"', 'href="ingredients.html"'),
    ('href="#taste"', 'href="taste.html"'),
    ('href="#eco"', 'href="eco.html"'),
    ('href="#reviews"', 'href="reviews.html"'),
    ('href="#shop"', 'href="contact.html"')
]

# We also need to extract sections.
# Sections are <section id="..."></section>
sections = {
    'home': re.search(r'(<section id="home".*?</section>)', content, re.DOTALL).group(1),
    'ingredients': re.search(r'(<section id="ingredients".*?</section>)', content, re.DOTALL).group(1),
    'taste': re.search(r'(<section id="taste".*?</section>)', content, re.DOTALL).group(1),
    'eco': re.search(r'(<section id="eco".*?</section>)', content, re.DOTALL).group(1),
    'reviews': re.search(r'(<section id="reviews".*?</section>)', content, re.DOTALL).group(1),
    'shop': re.search(r'(<section id="shop".*?</section>)', content, re.DOTALL).group(1)
}

# The header part (from <body> up to <main>)
header_part = re.search(r'(<body.*?)<main>', content, re.DOTALL).group(1) + '<main>'
for old, new in nav_replacements:
    header_part = header_part.replace(old, new)

# The footer part (from </main> to </html>)
footer_part = '</main>' + re.search(r'</main>(.*)', content, re.DOTALL).group(1)
for old, new in nav_replacements:
    footer_part = footer_part.replace(old, new)

# Write index.html
with open("index.html", "w") as f:
    f.write(content.split('<body')[0] + header_part.replace('href="index.html" class="nav-item"', 'href="index.html" class="nav-item active"') + "\n" + sections['home'] + "\n" + footer_part)

# Function to write other pages
def write_page(filename, section_key, nav_active_class_old, nav_active_class_new):
    head_and_body = content.split('<body')[0] + header_part
    # Update active class in nav
    head_and_body = re.sub(r'class="nav-item active"', 'class="nav-item"', head_and_body)
    head_and_body = head_and_body.replace(nav_active_class_old, nav_active_class_new)
    
    # We might not want bubbles overlapping content heavily, but for now we keep it
    html = head_and_body + "\n" + sections[section_key] + "\n" + footer_part
    with open(filename, "w") as f:
        f.write(html)

write_page("ingredients.html", "ingredients", 'href="ingredients.html" class="nav-item"', 'href="ingredients.html" class="nav-item active"')
write_page("taste.html", "taste", 'href="taste.html" class="nav-item"', 'href="taste.html" class="nav-item active"')
write_page("eco.html", "eco", 'href="eco.html" class="nav-item"', 'href="eco.html" class="nav-item active"')
write_page("reviews.html", "reviews", 'href="reviews.html" class="nav-item"', 'href="reviews.html" class="nav-item active"')
write_page("contact.html", "shop", 'href="contact.html" class="nav-item"', 'href="contact.html" class="nav-item active"') # Note: Shop uses contact button for now
