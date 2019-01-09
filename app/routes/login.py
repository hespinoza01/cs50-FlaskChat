from . import routes, session, nicknames
from flask import render_template as render, request, redirect, url_for


@routes.route('/login', methods=('GET', 'POST'))
def login():
    nickerror = False
    if request.method == 'POST':
        print(request.form['nickname'])
        if request.form['nickname'] not in nicknames:
            nickname = request.form['nickname']
            session['nickname'] = nickname
            nicknames.append(nickname)
            return redirect(url_for('routes.index'))
        else:
            nickerror = True

    return render('login.html', nickerror=nickerror)
