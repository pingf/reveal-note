from jinja2 import Template
from jinja2 import Environment, PackageLoader
if __name__ == '__main__':
    env = Environment(loader=PackageLoader('test_pack', 'templates'))
    template = env.get_template('template.html')
    r = template.render(name='Jesse')
    generate = 'generate.html'
    f = open(generate, 'w')
    f.write(r)
    f.close()
    print(r)
