import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup
import markdown2

def generate_microblog():
    # Open index.html file
    file_path = filedialog.askopenfilename(title="Select index.html file", filetypes=(("HTML files", "*.html"),))
    if not file_path:
        return

    with open(file_path, 'r') as file:
        html_content = file.read()

    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find template div
    template_div = soup.find('div', id='template')
    if not template_div:
        display_message("Template div not found.")
        return

    # Create post div with markdown content
    post_content = post_entry.get("1.0", tk.END)
    post_html = markdown2.markdown(post_content)
    post_div = soup.new_tag("div", id="box")
    post_div.append(BeautifulSoup(post_html, 'html.parser'))

    # Insert post div after template div
    template_div.insert_after(post_div)

    # Save modified HTML with custom formatting
    with open(file_path, 'w') as file:
        file.write(custom_prettify(soup))

    display_message("Microblog post added successfully to " + file_path)

def custom_prettify(soup):
    pretty_html = soup.prettify()
    pretty_html = pretty_html.replace("    ", "\t")  # Replace spaces with tabs
    # Remove line breaks for specific elements
    elements_no_line_breaks = ['p', 'li', 'ul', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    for element in elements_no_line_breaks:
        pretty_html = pretty_html.replace("\n<" + element, "<" + element)
    return pretty_html

def display_message(message):
    message_label.config(text=message)

# GUI setup
root = tk.Tk()
root.title("Microblog Generator")

post_label = tk.Label(root, text="Enter your post (in markdown):")
post_label.pack()

post_entry = tk.Text(root, height=5, width=50)
post_entry.pack()

generate_button = tk.Button(root, text="Generate Microblog Post", command=generate_microblog)
generate_button.pack()

message_label = tk.Label(root, text="")
message_label.pack()

root.mainloop()
