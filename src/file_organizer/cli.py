import questionary

from .db import create_database, delete_all_templates
from .templates import create_deftemplates, fill_form, save_templates, create_template, show_templates
from .organize_ext import organize_on_ext

def show_menu(templates):
	choice = questionary.select(
		"What would you like to do?",
		choices=["Create template", "Organize files", "View templates", "Exit"]
	).ask()
	if choice == "Organize files":
		answers = fill_form(templates)
		organize_on_ext(templates[answers["template_select"]], answers)
		save_templates(templates)
		show_menu(templates)
	elif choice == "Create template":
		template_name = questionary.text("What is the name of your template ?").ask()
		templates[template_name] = create_template(template_name)
		save_templates(templates)
		show_menu(templates)
	elif choice == "View templates":
		show_templates()
		show_menu(templates)
	elif choice == "Exit":
		save_templates(templates)

def main():
	if not create_database():
		templates = create_deftemplates()
	else:
		templates = {

		}
	show_menu(templates)
	#if choice == "Organize files":
	#	answers = fill_form(templates)
	#	show_menu()
	#elif choice == "Create template":
	#	template_name = questionary.text("What is the name of your template ?").ask()
	#	templates[template_name] = create_template(template_name)
	#	show_menu()
	#elif choice == "View templates":
	#	show_menu()
	#elif choice == "Exit":
	#	save_templates(templates)
	#	return


if __name__ == "__main__":
	main()