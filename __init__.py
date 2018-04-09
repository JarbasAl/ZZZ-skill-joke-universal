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
from mycroft.skills.core import intent_handler, intent_file_handler
from random import choice
from mycroft_jarbas_utils.skills.auto_translatable import AutotranslatableSkill

joke_types = ['chuck', 'neutral', 'dad']


class UniversalJokingSkill(AutotranslatableSkill):
    def __init__(self):
        super(UniversalJokingSkill, self).__init__()

    def get_intro_message(self):
        name = "jokes"
        folder = self._dir.split("/")[-1].replace("-universal", "")
        blacklisted_skills = self.config_core.get("skills", {}).get(
            "blacklisted_skills", [])
        if folder not in blacklisted_skills:
            return "you installed universal " + name + " skill, you should " \
                   "also blacklist the standard " + name + " skill to avoid " \
                   "potential problems"
        return None

    def speak_joke(self, category=None):
        if category is None:
            category = choice(joke_types)
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
        elif category in ["chuck", "neutral", "adult"]:
            self.speak(pyjokes.get_joke(category=category))
        else:
            url = "https://icanhazdadjoke.com/search?term="+category
            headers = {'Accept': 'text/plain'}
            r = requests.get(url, headers=headers)
            txt = r.text.encode('ascii', errors='ignore')
            if not txt:
                self.speak_dialog("no_joke", {"category": category})
            else:
                data = [joke for joke in txt.split(".") if joke]
                self.speak(choice(data))

    @intent_file_handler("Joke.intent")
    def handle_general_joke(self, message):
        joke_type = message.data.get("type")
        print joke_type
        self.speak_joke(joke_type)

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
    def handle_dad_joke(self, message):
        self.speak_joke('dad')


def create_skill():
    return UniversalJokingSkill()
