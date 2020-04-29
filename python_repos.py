import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

responce_dict = r.json()

print("Total repositories: ", responce_dict['total_count'])

repo_dicts = responce_dict['items']
#print("Repositories returned: ", len(repo_dicts))
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    description = repo_dict['description']
    if not description:
        description = "No description provided."
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url']
        }
    plot_dicts.append(plot_dict)

my_style = LS(base_style=LCS)
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
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

#repo_dict = repo_dicts[0]
#print("\nKeys:", len(repo_dict))
#for key in sorted(repo_dict.keys()):
 #   print(key)
#for repo_dict in repo_dicts:
 #   print("\nSelected information about each repository:")
  #  print('Name: ', repo_dict['name'])
   # print('Owner: ', repo_dict['owner']['login'])
    #print('Stars: ', repo_dict['stargazers_count'])
    #print('Repository: ', repo_dict['html_url'])
    #print('Created: ', repo_dict['created_at'])
    #print('Updated: ', repo_dict['updated_at'])
    #print('Description: ', repo_dict['description'])

