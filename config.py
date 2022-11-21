from app import app
from flask import render_template
import utils


@app.route('/')
def main_page():
    candidates = utils.load_candidates()
    return render_template('main_page.html', candidates=candidates)


@app.route('/candidates/<int:pk>')
def candidat_page(pk):
    candidates = {candidat['pk']: candidat for candidat in utils.load_candidates()}
    if pk in candidates:
        return render_template('candidat_page.html', candidat=candidates[pk])
    else:
        return render_template('candidat_page.html', number=pk)


@app.route('/skills/<skill>')
def skills_page(skill):
    candidates = utils.get_by_skill(skill)
    return render_template('skill_page.html', skill = skill, candidates=candidates)
