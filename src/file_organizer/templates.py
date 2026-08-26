import questionary
from .db import insert_template, insert_temp_rule, get_template_names

def create_deftemplates():
	templates = {
		"MPD" : {
			".pdf" : "Documents/pdfs",
			".pptx" : "Documents/Powerpoints",
			".docx" : "Documents/docs",
			".xlsx" : "Documents/excel",
			".jpeg" : "Pictures/jpeg",
			".jpg" : "Pictures/jpg",
			".png" : "Pictures",
			".mp3" : "Music/mp3",
			}}
	return templates

def create_template(name):
	add = True
	name = {
		"template_name" : name
	}
	while add:
		name[questionary.select("Choose an extension.").ask()] =  questionary.text("Choose a destination.").ask()
		add = questionary.confirm("Add another one ?")
	return name

def fill_form():
	answers = {
		"folder_name": questionary.path("What folder would you like to organize ?").ask(),
		"template_choice": questionary.confirm("Would you like to choose a template ?").ask(),
	}
	return answers
	
def check_tempchoice(answers, templates):
	if answers["template_choice"]:
		template_names = get_template_names()
		answers["template_select"] = questionary.select(
			"Which template do you want to use?",
			choices = [row[0] for row in template_names]).ask()
	else:
		template_name = questionary.text("What is the name of your template ?").ask()
		templates[template_name] = create_template(template_name)


	

def save_templates(templates):
	for template_name, rules in templates.items():
			lastrowid = insert_template(template_name)
			for extension, destination in rules.items():
				insert_temp_rule(lastrowid, extension, destination)