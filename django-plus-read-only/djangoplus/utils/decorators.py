"""TODO: These should be commented"""
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext

# Thanks to Yuri Baburov
def page(template=None, context=None, **decorator_args):
    def _wrapper(fn):
        def _innerWrapper(request, *args, **kw):
            context_dict = decorator_args.copy()
            g = fn(request, *args, **kw)
            if issubclass(type(g), HttpResponse): 
                return g
            if not hasattr(g, 'next'):  #Is this a generator?  Otherwise make it a tuple!
                g = (g,)
            for i in g:
                if issubclass(type(i), HttpResponse):
                    return i
                if type(i) == type(()):
                    context_dict[i[0]] = i[1]
                else:
                    context_dict.update(i)
            template_name = context_dict.get("template", template)
            context_instance = context_dict.get("context", context)
            if not context_instance:
                context_instance = RequestContext(request, context_dict)
            return render_to_response(template_name, context_dict, context_instance)
            
        return _innerWrapper
    return _wrapper
