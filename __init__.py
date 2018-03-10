# Copyright 2017, Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import pyjokes
import requests
from adapt.intent import IntentBuilder
from mycroft.skills.core import intent_handler
from random import choice
from mycroft_jarbas_utils.skills.auto_translatable import AutotranslatableSkill

joke_types = ['chuck', 'neutral', 'dad']


class UniversalJokingSkill(AutotranslatableSkill):
    def __init__(self):
        super(UniversalJokingSkill, self).__init__()

    def get_intro_message(self):
        name = "jokes"
        return "you installed universal " + name + " skill, you should " \
               "also blacklist the official " + name + \
               " skill to avoid potential problems"

    def speak_joke(self, category):
        if category == "dad":
            url = "https://icanhazdadjoke.com/"
            headers = {'Accept': 'text/plain'}
            r = requests.get(url, headers=headers)
            txt = r.text.encode('ascii', errors='ignore')
            replacements = (',', '-', '!', '?', '.')
            for f in replacements:
                txt = txt.replace(f, '|')
            data = txt.split("|")
            for temp in data:
                self.speak(temp)
        else:
            self.speak(pyjokes.get_joke(category=category))

    @intent_handler(IntentBuilder("JokingIntent").require("Joke"))
    def handle_general_joke(self, message):
        selected = choice(joke_types)
        self.speak_joke(selected)

    @intent_handler(IntentBuilder("ChuckJokeIntent").require("Joke")
                    .require("Chuck"))
    def handle_chuck_joke(self, message):
        self.speak_joke('chuck')

    @intent_handler(IntentBuilder("NeutralJokeIntent").require("Joke")
                    .require("Neutral"))
    def handle_neutral_joke(self, message):
        self.speak_joke('neutral')

    @intent_handler(IntentBuilder("AdultJokeIntent").require("Joke")
                    .require("Adult"))
    def handle_adult_joke(self, message):
        self.speak_joke('adult')

    @intent_handler(IntentBuilder("DadJokeIntent").require("Joke")
                    .require("Dad"))
    def handle_adult_joke(self, message):
        self.speak_joke('dad')


def create_skill():
    return UniversalJokingSkill()
