from twilio.twiml.voice_response import VoiceResponse
#from contacts.models import Contact

@app.route("/", methods=['GET', 'POST'])
def incoming_call():

    from_number = request.values.get('From', None)

    resp = VoiceResponse()
    resp.say("Hey there")
    #resp.play()
    g = Gather(numDigits=1, action="/handle-key", method="POST")
    g.say("To give me a call, press 1. Press any other key to start over.")
    resp.append(g)

    return str(resp)

@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():
    """Handle key press from a user."""

    # Get the digit pressed by the user
    digit_pressed = request.values.get('Digits', None)
    if digit_pressed == "1":
        resp = VoiceResponse()

        resp.dial("+15166407250")
        # If the dial fails:
        resp.say("The call failed, or the remote party hung up. Goodbye.")

        return str(resp)

    # If the caller pressed anything but 1, redirect them to the homepage.
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
