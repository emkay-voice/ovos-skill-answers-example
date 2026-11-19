"""Your own answers: the questions and answers in locale/<language>/answers.list.

Ask "where are the spare keys?" and the skill answers "In the blue bowl in
the hall." – or anything else you write in answers.list, one line each:

    question | answer

There are no intents here. This is a common query skill: when someone asks
a question, OpenVoiceOS asks every common query skill whether it knows the
answer and how sure it is (match_common_query), and speaks the best one –
yours, Wikipedia's, or another skill's. A question that is almost like one of
yours still finds it ("where did we put the spare keys").

Try changing: the questions and answers (any number of lines), how alike a
question must be (ALIKE), or what happens when your answer is picked
(answered: it shows the answer on the screen).
"""
from difflib import SequenceMatcher

from ovos_workshop.decorators import common_query
from ovos_workshop.skills import OVOSSkill

ALIKE = 0.75   # how alike a question must be to one in answers.list, 0..1


def words(text):
    """A sentence as plain lower-case words: "Where're the keys?" -> "where re the keys"."""
    return " ".join("".join(c if c.isalnum() else " " for c in (text or "").lower()).split())


def alike(a, b):
    """How alike two questions are, 0..1."""
    return SequenceMatcher(None, words(a), words(b)).ratio()


class AnswersSkill(OVOSSkill):

    def answers(self, lang):
        """[(question, answer)] from answers.list in that language."""
        path = self.find_resource("answers.list", lang=lang)
        out = []
        for line in open(path, encoding="utf-8") if path else []:
            if "|" in line and not line.startswith("#"):
                question, answer = line.split("|", 1)
                out.append((question.strip(), answer.strip()))
        return out

    def answered(self, phrase, answer, lang):
        """Our answer was the one picked: show it on the screen too."""
        self.gui.show_text(answer, title=phrase, override_idle=15)

    @common_query(callback=answered)
    def match_common_query(self, phrase, lang):
        """Asked by OpenVoiceOS for every question: (our answer, how sure 0..1), or None."""
        best, score = None, 0.0
        for question, answer in self.answers(lang):
            s = alike(phrase, question)
            if s > score:
                best, score = answer, s
        if score < ALIKE:
            return None
        return best, min(score, 0.95)
