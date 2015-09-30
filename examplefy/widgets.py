import django.forms
from django.forms.utils import flatatt
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.encoding import force_text
from itertools import chain
from models import Topic, Concept

class ExamplfySelect(django.forms.Select):

    def __init__(self, model, placeholder="", attrs=None, choices=()):
        super(ExamplfySelect, self).__init__(attrs)
        self.placeholder=placeholder
        self.model=model

    def render(self, name, value, attrs=None, choices=()):

        dropdown_attrs = { # hardcoded for now
            'class': 'dropdown-menu',
            'role': 'menu',
        }

        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        output = [format_html('<button id="%s_button"{}>' % self.model, flatatt(final_attrs))]
        options = self.render_options(choices, [value])
        output.append(self.placeholder)
        output.append('</button>')
        output.append(format_html('<ul id="%s_dropdown"{}>' % self.model, flatatt(dropdown_attrs)))
        if options:
            output.append(options)
        output.append('</ul>')
        return mark_safe('\n'.join(output))

    def render_option(self, selected_choices, option_value, option_label):
        return '<li class="%s_list_element" id=%s><a>%s</a></li>' % (self.model, option_label, option_label)

    def render_options(self, choices, selected_choices):
        if self.model == "concept":
            return None

        # Normalize to strings.
        selected_choices = set(force_text(v) for v in selected_choices)
        output = []
        for option_value, option_label in chain(self.choices, choices):
            if isinstance(option_label, (list, tuple)):
                output.append(format_html('<optgroup label="{}">', force_text(option_value)))
                for option in option_label:
                    output.append(self.render_option(selected_choices, *option))
                output.append('</optgroup>')
            else:
                if option_label == "---------": continue
                output.append(self.render_option(selected_choices, option_value, option_label))
        return '\n'.join(output)

    def value_from_datadict(self, data, files, name):
        if self.model == "topic":
            return Topic.objects.get(name=data["topic"])
        if self.model == "concept":
            return Concept.objects.get(name=data["concept"])
        raise BaseException("Widget cannot get value")


    def _media(self):
        return django.forms.Media(js=('js/jquery.js', 'js/select_widget.js'))
    media = property(_media)
