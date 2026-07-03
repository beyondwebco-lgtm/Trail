import re
import os

with open("index.html", "r") as f:
    index_content = f.read()

# We need to insert the other sections right after the closing </section> of home.
home_section_end = index_content.find("</section>") + 10

def get_section(filename, section_id):
    with open(filename, "r") as f:
        content = f.read()
    match = re.search(f'(<section id="{section_id}".*?</section>)', content, re.DOTALL)
    return match.group(1) if match else ""

sections = []
sections.append(get_section("ingredients.html", "ingredients"))
sections.append(get_section("taste.html", "taste"))
sections.append(get_section("eco.html", "eco"))
sections.append(get_section("reviews.html", "reviews"))
sections.append(get_section("contact.html", "shop"))

# Combine
new_content = index_content[:home_section_end] + "\n\n" + "\n\n".join(sections) + index_content[home_section_end:]

# Update nav links in the new combined content
nav_replacements = [
    ('href="index.html"', 'href="#home"'),
    ('href="ingredients.html"', 'href="#ingredients"'),
    ('href="taste.html"', 'href="#taste"'),
    ('href="eco.html"', 'href="#eco"'),
    ('href="reviews.html"', 'href="#reviews"'),
    ('href="contact.html"', 'href="#shop"')
]

for old, new in nav_replacements:
    new_content = new_content.replace(old, new)

with open("index.html", "w") as f:
    f.write(new_content)

# Clean up
os.remove("ingredients.html")
os.remove("taste.html")
os.remove("eco.html")
os.remove("reviews.html")
os.remove("contact.html")
