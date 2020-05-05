import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightStyle as LS


from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

submission_ids = r.json()
data = []

for submission_id in submission_ids[:30]:
    submission_url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission = requests.get(submission_url).json()

    submission_data = {
        'title': submission['title'],
        'value': submission.get('descendants', 0),
        'xlink': 'http://news.ycombinator.com/item?id=' + str(submission_id)
    }
    data.append(submission_data)


data = sorted(data, key=itemgetter('value'), reverse=True)
names = [s['title'] for s in data]


my_style = LS(base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18
my_config = pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.truncate_label=15
my_config.show_y_guides=False
my_config.width=1000
chart = pygal.Bar(my_config, style = my_style)
chart.title = 'Discussion questions'
chart.x_labels = names

chart.add('', data)
chart.render_to_file('hacker-news_comments.svg')
