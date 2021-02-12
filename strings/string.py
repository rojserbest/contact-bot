import os
import json


class Strings:
    def __init__(self):
        languages = {}

        for f in os.listdir("strings"):
            if f.endswith(".json"):
                languages[f[:-5]
                          ] = json.loads(open(f"strings/{f}", "r").read())

        self.languages = languages

    def get_string(self, string, language):
        try:
            return self.languages[language][string]
        except:
            return self.languages["en"][string]

    def get_languages(self):
        result = {}

        for language in self.languages:
            result[language] = self.languages[language]["name"]

        return result


strings = Strings()
