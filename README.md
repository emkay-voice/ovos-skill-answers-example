# Your own answers

Ask **"where are the spare keys?"** and the skill answers *"In the blue bowl in
the hall."* – or anything else you write in `answers.list`, one line each,
`question | answer` – in all twelve of [Emkay](https://emkay.ai)'s languages.

**👉 The friendly guide: <https://dev.emkay.ai>**

## What it shows

- **Common query, no intents:** when someone asks a question, OpenVoiceOS asks
  every *common query* skill whether it knows the answer and how sure it is,
  and speaks the best one – yours, Wikipedia's or another skill's. Your part
  is one method: `@common_query` on `match_common_query(phrase, lang)`, which
  returns `(answer, how sure 0..1)` or `None`.
- **Almost the same question:** `alike()` compares the question with yours
  (Python's own `difflib`), so "where did we put the spare keys" finds it too.
- **When your answer is picked:** the `callback` (`answered`) runs – here it
  shows the answer on the screen.
- **Your own data per language:** `locale/<language>/answers.list`.

## Try changing

- the questions and answers – your house, your club, your class;
- `ALIKE` – how alike a question must be (lower: more questions find yours,
  and more wrong ones);
- what `answered` does – speak more, show a picture, start something.

## A working skill, and a template

This is a complete OpenVoiceOS skill – install it and it works – and an
example to start your own from: *Use this template* on GitHub, or
*Emkay: New skill* in VS Code ([Emkay Dev](https://dev.emkay.ai)), which
gives it your own names. Made for [Emkay](https://emkay.ai), it runs on any
OpenVoiceOS.

## Try it

- **Emkay Dev (VS Code):** *Emkay: Run the skill in Emkay* (Ctrl+Alt+E) opens
  Emkay next to your code and loads the skill; type under Emkay to talk to it.
  Every save loads it again. *Emkay: Test the skill* sends the golden
  utterances and shows ✓ / ✗ in the Testing view. Emkay's menu →
  *Guardian* → *What's happening?* shows which skill took a sentence, and why.
- **ovos-tui-client (Codespaces, Dev Container):** run `ovos-tui` in the
  terminal, type to talk, `Ctrl+P` → *Test* runs the same golden utterances
  against a full OpenVoiceOS.
- **pytest:** `pytest -q` – no OpenVoiceOS needed.

When you make a repository from this template ("Use this template"), a
small workflow renames the skill after your repository and then removes
itself.

## Show it, on your own Emkay, and into the store

To show it in [See my skill](https://dev.emkay.ai/#gallery) on dev.emkay.ai –
ready or not – add the topic `emkay-skill` to the repository (the ⚙ next to
*About*). Remove the topic, or make the repository private, to take it away.

*Emkay: Send to my Emkay* shows a QR code that installs this skill from
GitHub on the Emkay you scan it with. To get it into the
[Emkay store](https://store.emkay.ai): topics `ovos` and `openvoiceos` on the
repository, a release on GitHub (`publish.yml` puts it on PyPI), and the
store's nightly test does the rest – <https://dev.emkay.ai/#store>.

More on writing skills:
[the OpenVoiceOS technical manual](https://openvoiceos.github.io/ovos-technical-manual/).
