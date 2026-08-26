from .db import create_database
from .templates import create_deftemplates, fill_form, check_tempchoice
from .organize_ext import organize_on_ext

def main():
	create_database()
	templates = create_deftemplates()
	answers = fill_form(templates)
	check_tempchoice(answers, templates)
	organize_on_ext(templates[answers["template_select"]], answers)

if __name__ == "__main__":
	main()