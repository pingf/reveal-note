from jinja2 import Template
if __name__ == '__main__':
    template = Template('Hello {{ name }}!')
    r = template.render(name='John Doe')
    print(r)
