# -*- coding: utf-8 -*-
"""This module contains general-purpose dialogue states not specific to the medication reconciliation task
"""

from .root import app

@app.handle(default=True)
@app.handle(intent='unsupported')
def default(request, responder):
    """
    When the user asks an unrelated question, convey the lack of understanding for the requested information and prompt to return to medication management.
    """
    response = ["Sorry, not sure what you meant there."]
    responder.reply(response)

@app.handle(intent='greet')
def greet(request, responder):
    try:
        responder.slots['name'] = request.context['name']
        prefix = 'Hello, {name}.'
    except KeyError:
        prefix = 'Hello. '
    message = '' #TODO: write greeting message
    response = prefix + message
    responder.reply(response)

@app.handle(intent='exit')
def exit(request, responder):
    """
    When the user ends a conversation, clear the dialogue frame and say goodbye.
    """
    responder.frame = {}

    # Respond with a random selection
    responder.reply(['Bye!', 'Goodbye!', 'Have a nice day!'])

@app.handle(intent='help')
def help(request, responder):
    """
    When the user asks for help, provide some sample prompts they can try.
    """
    prompts = ['this is an example placeholder prompt'] #TODO: fill in prompts
    responder.reply(prompts)
    responder.listen()

@app.handle(intent='start_over')
def start_over(request, responder):
    """
    When the user wants to start over, clear the dialogue frame and reply for the next request.
    """
    # Clear the dialogue frame and respond with a variation of the welcome message.
    responder.frame = {}
    replies = ["Let's start over. I'm here to help you update your medication record. Could you tell me what medications you're currently taking, their dose, and how frequently you take them?"]
    responder.reply(replies)
    responder.listen()