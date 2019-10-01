"""
This module contains the dialogue states for the 'medication' domain
"""
from .root import app

#TODO: fill in app handles
@app.handle(intent='create_record')
def prompt_for_medication(request, responder):
    """
    Prompt user for their current list of medications
    """
    message = "I'd like to go over your medications with you to make sure our records are up-to-date. May you please tell me the medications you are currently taking, including the dosage and when you take them?"

    responder.reply(message)
    responder.listen()

def prompt_for_dosage(request, responder):
    """
    Prompt user for a medication's dosage
    """


    responder.reply(message)
    responder.listen()

def prompt_for_brand(request, responder):
    """
    Prompt for a medication's brand if they only state the ingredient
    """
    responder.reply(message)

def prompt_for_frequency(request, responder):
    """
    Prompt user for how often or when they take a particular medication
    """
    responder.reply(message)

def verify_unspoken(request, responder):
    """
    Prompt user to verify a medication they haven't mentioned but is on their record
    """
    responder.reply(message)

def verify_complete_record(request, responder):
    """
    Prompt user to verify that current medication history is accurate
    """
    responder.reply(message)

def send_ingredient(request, responder):
    """
    Provide a user with a medication's primary ingredient if they don't recognize the brand
    """
    responder.reply(message)

def send_brand(request, responder):
    """
    Provide a user with a medication's brand if they don't recognize an ingredient
    """
    responder.reply(message)