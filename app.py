from flask import Flask
import utils

app = Flask(__name__)


@app.route("/")
def page_index():
    f = utils.get_all()
    return f


@app.route("/candidates/<int:x>")
def page_candidate(x):
    f = utils.get_by_pk(x)
    url = f["picture"]
    d = f'<img src="({url})">\n'
    d += '\n'
    d += '<pre>\n'
    d += f'''
        {f["name"]}\n
        {f["position"]}\n
        {f["skills"]}\n
        '''
    d += '</pre>'
    return d


@app.route("/skills/<skill>")
def page_candidate_skills(skill):
    f = utils.get_by_skill(skill)
    d = '<pre>\n'
    for i in f:
        d += f'''
            {i["name"]}\n
            {i["position"]}\n
            {i["skills"]}\n
        '''
    d += '</pre>'
    return d


app.run()
