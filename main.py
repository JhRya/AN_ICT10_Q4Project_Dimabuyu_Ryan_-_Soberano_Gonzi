from pyscript import display, HTML, document

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hi! I am <strong>{self.name}</strong> from {self.section}. My favorite subject is {self.favorite_subject}."

classmates_list = [
    Classmate("Luis", "10 Ruby", "ICT"),
    Classmate("Maria", "10 Emerald", "English"),    
    Classmate("Bianca", "10 Emerald", "Math"),
    Classmate("Juan", "10 Sapphire", "Social Studies"),
    Classmate("Miguel", "10 Amethyst", "Science")
]

def add_classmate(event):
    n = document.getElementById("name")
    s = document.getElementById("section")
    sub = document.getElementById("subject")
    
    if n.value and s.value and sub.value:
        classmates_list.append(Classmate(n.value, s.value, sub.value))
        n.value = s.value = sub.value = ""
        if document.getElementById("display-area").style.display == "block":
            render_list()

def render_list():
    output = document.getElementById("output-list")
    output.innerHTML = ""
    for c in classmates_list:
        display(HTML(f"<div class='intro-text'>{c.introduce()}</div>"), target="output-list", append=True)

def toggle_list(event):
    area = document.getElementById("display-area")
    btn = document.getElementById("show-btn")
    
    if area.style.display == "none":
        render_list()
        area.style.display = "block"
        btn.innerText = "Hide List"
    else:
        area.style.display = "none"
        btn.innerText = "Show List"