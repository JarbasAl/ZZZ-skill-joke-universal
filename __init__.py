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

from adapt.intent import IntentBuilder
from mycroft.skills.core import intent_handler
from random import choice
from mycroft_jarbas_utils.skills.auto_translatable import AutotranslatableSkill

joke_types = ['chuck', 'neutral']


class UniversalJokingSkill(AutotranslatableSkill):
    def __init__(self):
        super(UniversalJokingSkill, self).__init__()

    def speak_joke(self, lang, category):
        lang = "en"
        self.speak(pyjokes.get_joke(language=lang, category=category))

    @intent_handler(IntentBuilder("JokingIntent").require("Joke"))
    def handle_general_joke(self, message):
        selected = choice(joke_types)
        self.speak_joke(self.lang[:-3], selected)

    @intent_handler(IntentBuilder("ChuckJokeIntent").require("Joke")
                    .require("Chuck"))
    def handle_chuck_joke(self, message):
        self.speak_joke(self.lang[:-3], 'chuck')

    @intent_handler(IntentBuilder("NeutralJokeIntent").require("Joke")
                    .require("Neutral"))
    def handle_neutral_joke(self, message):
        self.speak_joke(self.lang[:-3], 'neutral')

    @intent_handler(IntentBuilder("AdultJokeIntent").require("Joke")
                    .require("Adult"))
    def handle_adult_joke(self, message):
        self.speak_joke(self.lang[:-3], 'adult')


def create_skill():
    return UniversalJokingSkill()
