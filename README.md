# Spoken Dialogue System for Rx Medications (sds4rx)

This application uses the [Mindmeld](www.mindmeld.com) framework to build a conversational agent that inquires and collects information about a patient's medication record. The use case for this application is _medication reconciliation_, which is the process of creating an accurate record of a patient's current medication regimen.

This agent aims to accomplish the following tasks:

- Collect medication brand, primary ingredients, dosage, and frequency from natural language
- Inquire user for missing information about their medications
- Cross check information with [RxNorm](https://www.nlm.nih.gov/research/umls/rxnorm/index.html), a database of standardized perscription drug information maintained by the US Library of Medicine

This application is currently under development.


## NLP Model Hiearchy

The `medication` domain is to support the following intents:

- `add_medication` — Patient reports a series of new medications that are to be added to their record.
- `update_record` — Agent interviews patient about medications on their existing record and updates it as needed.
- `start_over`  — Clears information from the current conversation and goes back to the start message.

The `general` domain is to support the following intents:

- `greet` — Begins the interaction. Greet the patient and inform them about the agent's functionality.
- `exit` — Ends the current interaction and say goodbye to the patient.
- `help` — State the agent's functionality and recomend several actions they can take in case the patient gets stuck.
- `unsupported` — Patient has inquired for information outside the scope of the agent's knowledge.


## File structure

- `medication_history_examples` — Examples of medication reconciliation dialogue from [Vanderbilt University Medical Center's training videos](https://www.youtube.com/watch?v=8az0PV3WXZk).
- `sds4rx` — Mindmeld application
  - `data` — JSON knowledge base of all known medications
  - `domains` — Contains annotated example queries for all intents, sorted by domain.
  - `entities` — Contains training data for entity resolution.
  - `scripts` — custom Python scripts used to generate data in the three folders described previously.
    - `rxnorm.py` — Collects data from RxNorm API
    - `kb_generatory.py` — Generates a JSON knowledge base given a list of ingredients using information from RxNorm.
    - `entity_generator.py` — Generates entity mapping files given a JSON knowledge base.
    - `frequencies_gen.py` — Generates natural language phrases for describing frequencies.

## Current Status & Limitations

- This application's knowledge base is limited to the 50 most perscribed medications in the US [(Fuentes, 2018)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6025009/).
- Representative training data is currently being generated to train the NLP classifiers. (related [Mindmeld documentation](https://www.mindmeld.com/docs/quickstart/06_generate_representative_training_data.html))


## Future Work

- Include a knowledge base component that directly interfaces with the RxNorm API instead of a locally-stored database.
