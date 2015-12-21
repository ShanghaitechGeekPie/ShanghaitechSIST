from django import template
from classytags.arguments import (Argument, MultiValueArgument,
                                  MultiKeywordArgument)
from classytags.core import Options, Tag
from cms.templatetags.cms_tags import ShowPlaceholderById
from django.core.exceptions import ImproperlyConfigured

register = template.Library()

class ShowPlaceholderByIdwithAS(ShowPlaceholderById):
    options = Options(
        Argument('placeholder_name'),
        Argument('reverse_id'),
        Argument('lang', required=False, default=None),
        Argument('site', required=False, default=None),
        'as',
        Argument('varname', required=False, resolve=False),
    )

    def __init__(self, parser, tokens, **kwargs):
        super().__init__(parser, tokens)
        if len(self.options.breakpoints) < 1:
            raise ImproperlyConfigured(
                "AsTag subclasses require at least one breakpoint."
            )
        last_breakpoint = self.options.options[self.options.breakpoints[-1]]
        optscount = len(last_breakpoint)
        if optscount != 1:
            raise ImproperlyConfigured(
                "The last breakpoint of AsTag subclasses require exactly one "
                "argument, got %s instead." % optscount
            )
        self.varname_name = last_breakpoint[-1].name

    def get_kwargs(self, context, placeholder_name, reverse_id, lang, site, varname):
        return super().get_kwargs(context, placeholder_name, reverse_id, lang, site)

    def render_tag(self, context, **kwargs):
        """
        INTERNAL!

        Gets the context and data to render.
        """
        print(kwargs)
        value = super().render_tag(context, **kwargs)
        varname = kwargs.pop(self.varname_name)
        print(varname)
        if varname:
            context[varname] = value
            return ''
        else:
            return value

register.tag('show_placeholder_as', ShowPlaceholderByIdwithAS)
