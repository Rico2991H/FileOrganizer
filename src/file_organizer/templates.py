import questionary
import sqlite3
from .db import insert_template, insert_temp_rule, get_template_names, get_template, delete_all_templates

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
		try:
			name[questionary.text("Choose an extension").ask()] = questionary.text("Choose a destination.").ask()
			add = questionary.confirm("Add another one ?").ask()
		except sqlite3.IntegriyError:
			print(f"⚠️  That template name already exists. Try a different name.")
	print("Created new template")
	return name

def fill_form(templates):
	answers = {
		"folder_name": questionary.path("What folder would you like to organize (e.g. downloads)?").ask(),
		"template_choice": questionary.confirm("Would you like to choose a template?").ask(),
	}
	if answers["template_choice"]:
		template_names = get_template_names()
		answers["template_select"] = questionary.select(
			"Which template do you want to use?",
			choices = [row[0] for row in template_names]).ask()
		templates[answers["template_select"]] = get_template(answers["template_select"]) # might need to store this in answers or return it for later use
	else:
		if questionary.confirm("Would you like to create a template?").ask():
			template_name = questionary.text("What is the name of your template ?").ask()
			templates[template_name] = create_template(template_name)
			answers["template_select"] = template_name
	return answers


	

def save_templates(templates):
	for template_name, rules in templates.items():
			try:
				lastrowid = insert_template(template_name)
				for extension, destination in rules.items():
					insert_temp_rule(lastrowid, extension, destination)
			except:
				print(f"⚠️  Skipped '{template_name}' — already exists.")
				continue

def show_templates():
	template = {

	}
	template_names = get_template_names()
	answer = questionary.select(
			"Which template do you want to see?",
			choices = [row[0] for row in template_names]).ask()
	template["template_select"] = get_template(answer)
	#print(template["template_select"])
	for selected in template:
		for ext in template[selected]:
			print(f"extension:", ext, "- destination", template[selected][ext])
		
