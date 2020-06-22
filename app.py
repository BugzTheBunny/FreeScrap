import flask
import json
import app_properties
from models_jobs.model_linkedin import get_linkedin_jobs
from models_jobs.model_mploy import get_mploy_jobs
from models_education.model_udemy import get_udemy_courses
from models_education.model_campus_gov import get_campus_courses
app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return app_properties.hello_world


@app.route(f'/mploy', methods=['GET'])
def mploy_jobs():
    search_query = flask.request.args.get('search')
    if search_query != '' and search_query is not None:
        return json.dumps(get_mploy_jobs(search_query, app_properties.max_data_size), ensure_ascii=False)
    else:
        return app_properties.sorry_message


@app.route(f'/linkedin-jobs', methods=['GET'])
def linkedin_jobs():
    search_query = flask.request.args.get('search')
    if search_query != '' and search_query is not None:
        return json.dumps(get_linkedin_jobs(search_query, app_properties.max_data_size), ensure_ascii=False)
    else:
        return app_properties.sorry_message


@app.route(f'/udemy', methods=['GET'])
def udemy_courses():
    search_query = flask.request.args.get('search')
    if search_query != '' and search_query is not None:
        return json.dumps(get_udemy_courses(search_query), ensure_ascii=True)
    else:
        return app_properties.sorry_message

@app.route(f'/campus', methods=['GET'])
def campus_il_courses():
    search_query = flask.request.args.get('search')
    if search_query != '' and search_query is not None:
        return json.dumps(get_campus_courses(search_query), ensure_ascii=False)
    else:
        return app_properties.sorry_message


if __name__ == '__main__':
    app.run(debug=True)
