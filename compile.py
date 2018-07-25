from itertools import count
counter = count()

import yaml
conf = open("font.yaml", 'r')
conf = yaml.load(conf)

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('./'))
template = env.get_template('fontGenerator.svg.j2')
output_from_parsed_template = template.render(id=lambda:counter.__next__(),**conf)

# to save the results
with open("wizardFont.svg", "wb") as fh:
    fh.write(output_from_parsed_template.encode('utf-8'))
