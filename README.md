## Universal Jokes
Let Mycroft brighten your day with a little humor

## Description
Brighten your day with a little humor.  This draws on the jokes collected by the [PyJokes project](https://github.com/pyjokes/pyjokes) to give you a chuckle.

The joke categories are:
* Neutral -- jokes that are safe for work, kids or your grandmother
* Adult -- nothing horrible, but be ready to cover some ears
* Chuck Norris -- jokes only a geek can love
* Dad -- jokes from https://icanhazdadjoke.com/

By default it will give you clean and/or geeky jokes, but you can ask a little adult humor if you feel that way.

_WARNING:  Laughter is not guaranteed, but eye rolls are likely._


uses and translates english jokes by default instead of relying in pyjokes
module for language support

intent vocabulary auto-translated with google

## Examples
* "Make me laugh"
* "Tell me a Chuck Norris joke"
* "Tell me a dad joke"
* "I want to hear a raunchy joke"
* "How about a neutral joke"

## LOGS

    20:51:38.386 - SKILLS - DEBUG - {"type": "recognizer_loop:utterance", "data": {"utterances": ["conta uma piada"]}, "context": null}
    20:51:38.391 - mycroft.skills.intent_service:send_metrics:244 - DEBUG - Sending metric
    20:51:38.395 - SKILLS - DEBUG - {"type": "7443995936560537690:JokingIntent", "data": {"confidence": 1.0, "target": null, "intent_type": "7443995936560537690:JokingIntent", "HEEDJJFJDGFGAFDHGJAJoke": "piada", "__tags__": [{"end_token": 2, "start_token": 2, "from_context": false, "entities": [{"confidence": 1.0, "data": [["piada", "HEEDJJFJDGFGAFDHGJAJoke"]], "key": "piada", "match": "piada"}], "key": "piada", "match": "piada"}], "utterance": "conta uma piada"}, "context": {"target": null}}
    20:51:38.420 - SKILLS - DEBUG - {"type": "mycroft.skill.handler.start", "data": {"name": "UniversalJokingSkill.handle_general_joke"}, "context": null}
    20:51:52.543 - SKILLS - DEBUG - {"type": "speak", "data": {"expect_response": false, "utterance": "Existem 10 tipos de pessoas: aqueles que entendem o binario e os que nao o fazem", "metadata": null}, "context": {"target_lang": "pt", "auto_translated": true, "target": null, "source_lang": "en"}}
    20:51:52.545 - SKILLS - DEBUG - {"type": "mycroft.skill.handler.complete", "data": {"name": "UniversalJokingSkill.handle_general_joke"}, "context": null}

## Credits
Mycroft AI

Everyone at https://github.com/pyjokes/pyjokes!

Tjoen [better-jokes](https://github.com/tjoen/skill-better-jokes/)
