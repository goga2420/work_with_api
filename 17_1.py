import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:Java&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

repo_dicts = response_dict['items']

my_style = LS('#333366', base_style=LCS)
my_style.tittle_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred JavaScript Projects on GitHub'

chart_data = []
names = []
for repo_dict in repo_dicts:
    repo_chart_data = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['name'],
        'xlink': repo_dict['html_url']
    }
    chart_data.append(repo_chart_data)
    names.append(repo_dict['name'])

chart.add('Some value', chart_data)
chart.x_labels = names
chart.render_to_file('java_repos.svg')
