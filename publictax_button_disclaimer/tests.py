from otree.api import Bot, Submission

from . import *


def valid_value(name):
    # One valid answer per form field, taken from the field definition in __init__.py.
    props = getattr(Player, name).form_props
    if props.get('choices'):
        return props['choices'][0][0]
    if name.startswith('check_'):
        return 1
    if 'min' in props and 'max' in props:
        return (props['min'] + props['max']) // 2 + 1
    if props.get('widget') is widgets.CheckboxInput:
        return True
    return 'test'


class PlayerBot(Bot):
    def play_round(self):
        # Some Thank pages show this session field; give it a test value.
        self.session.prolific_completion_url = 'BOTTEST'
        # Walk every page except the last (Thank), which has no Next button.
        for page in page_sequence[:-1]:
            if hasattr(page, 'get_form_fields'):
                fields = page.get_form_fields(self.player)
            else:
                fields = getattr(page, 'form_fields', [])
            data = {f: valid_value(f) for f in fields if f != 'timer_id'}
            # check_html=False: the check_* fields are hidden inputs that the
            # page script fills when a participant moves a slider.
            yield Submission(page, data, check_html=False)
        assert self.player.completion_code
