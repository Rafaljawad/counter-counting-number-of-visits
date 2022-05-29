from flask import Flask,render_template,redirect,request,session
app=Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
# Have the root route render a template that displays the number of times the client has visited this site. Refresh the page several times to ensure the counter is working
#set each the num and counter to 0 to start at value zero
#for this root route will display the html with its content so, when we refresh the page the counter styays count.
@app.route('/')
def show_content():
    session['number']=0
    session['count2']=0
    if 'count' not in session:
        session['count']=0
    else:
        session['count']+=1
    return render_template('index.html')

# SENSEI BONUS: Add a form that allows the user to specify the increment of the counter and have the counter increment accordingly
# by ading this route so the counter will count once the count button hit.
@app.route('/count')
def count_up():
    if 'count' in session:
        session['count']+=1
    else:
        session['count']=0
    return render_template('index.html')

# NINJA BONUS: Add a +2 button underneath the counter and a new route that will increment the counter by 2
@app.route('/count_two')
def count_two_up():
    session['count2']+=2
    return render_template('index.html')



# SENSEI BONUS: Add a form that allows the user to specify the increment of the counter and have the counter increment accordingly
@app.route('/add_by_user',methods=['POST'])
def increment():
    session['number']+=int(request.form['number'])
    return render_template('index.html')

# NINJA BONUS: Add a Reset button to reset the counter
@app.route('/destroy_session')
def clear_seesion():
    session.clear()
    return redirect('/')



if __name__=="__main__": 
    app.run(debug=True)  