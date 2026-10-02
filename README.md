# Public Tax Disclosures and Investor Perceptions: oTree experiment

oTree code for the experiments in the paper on public tax disclosures and investor perceptions (Contemporary Accounting Research). The code runs on oTree 6.0.15 with Python 3.14.

## Session configurations

Each study in the paper is one session configuration in `settings.py`.

| Session config | Study | App |
|---|---|---|
| `publictax_normal` | Main experiment, 11% ETR | `publictax_button` |
| `publictax_extreme` | Supplemental experiment 1, 1% ETR | `publictax_button` |
| `publictax_normal_cbc` | Supplemental experiment 2, CbC setting | `publictax_button` |
| `publictax_no_btn` | Supplemental experiment 3, no button | `publictax` |
| `publictax_disclaimer` | Supplemental experiment 4, disclaimer | `publictax_button_disclaimer` |
| `publictax_aggressive` | Supplemental experiment 5, aggressiveness | `publictax_aggressive` |
| `publictax_equalnumbers` | Supplemental experiment 6, equal numbers | `publictax_equalnumbers` |

All apps load their images from `publictax/static/publictax/`. The app `publictax_equalnumbers` also uses its own images in `publictax_equalnumbers/static/`. Keep the `publictax` folder even if you run only one of the other studies.

## Run it on your computer

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
otree devserver
```

Then open http://localhost:8000 and pick a session under "Demo".

## Test it

Each app has bots in `tests.py` that walk one participant through every page. Run them per session config:

```bash
otree test publictax_normal
```

Run this for each of the seven session configs above.
