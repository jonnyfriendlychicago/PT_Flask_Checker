# the next two lines always need to be atop this server.py file 
from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# all the @ stuff below will (later) be moved into separate files.  These will be replaced with controller import lines. 

defaultValidationMsg = "The URL you typed looks awesome, and so does this checkerboard... right?!?"
defaultValStyle = "affirmativeValStyle"

@app.route('/')          
def welcome():
    return render_template("index.html", horizDispCount = 1, vertDispCount = 1, color1 = "red", color2 = "black", displayValMsg = defaultValidationMsg, displayValStyle = defaultValStyle)

@app.route('/<int:hNum>/')
def horiz(hNum):
    return render_template("index.html", horizDispCount=hNum, vertDispCount = 1, color1 = "red", color2 = "black", displayValMsg = defaultValidationMsg, displayValStyle = defaultValStyle)

@app.route('/<int:hNum>/<int:vNum>/')
def both(hNum, vNum):
    return render_template("index.html", horizDispCount=hNum, vertDispCount = vNum, color1 = "red", color2 = "black", displayValMsg = defaultValidationMsg, displayValStyle = defaultValStyle)

@app.route('/<int:hNum>/<int:vNum>/<string:incomingColor1>/<string:incomingColor2>/')
def colorsAlso(hNum, vNum, incomingColor1, incomingColor2):
    acceptableColors = ["blue", "green", "red", "black"]
    if incomingColor1 == incomingColor2: 
        color1 = "red" 
        color2 = "black"
        validationMsg = "You provided the same color for both colors variables, which won't create a checkerboard.  Red/black combination displayed instead."
        validationStyle = "negativeValStyle"
    elif incomingColor1 in acceptableColors and incomingColor2 in acceptableColors: 
        color1 = incomingColor1 
        color2 = incomingColor2
        validationMsg = defaultValidationMsg
        validationStyle = defaultValStyle
    else: 
        color1 = "red" 
        color2 = "black"
        validationMsg = "One or both of your submitted colors is not supported.  Red/black combination displayed instead."
        validationStyle = "negativeValStyle"
    return render_template("index.html", horizDispCount=hNum, vertDispCount = vNum, displayColor1 = color1, displayColor2 = color2, displayValMsg = validationMsg, displayValStyle = validationStyle)

"""DON'T TOUCH BELOW :-) below always needs to be at the bottom of the script, yes!"""
# below is stuff you oughta have, per TA Cameron Smith, from Coding Dojo: 

@app.route('/', defaults={'cookies': ''})
@app.route('/<path:cookies>')
def catch_all(cookies):
    return 'Sorry! No response here. Try url again.'

# below is flask boiler plate; exclude it and stuff won't work    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

