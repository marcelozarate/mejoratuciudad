from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from vecinosapp.models import Aviso
from vecinosapp.forms import AvisoForm
from django.forms.util import ErrorList
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils import timezone
# Create your views here.


def home(request):
    return TemplateResponse(request, 'home.html',)


def add_aviso(request):
    if request.method == 'POST':
            form = AvisoForm(request.POST, request.FILES, auto_id=False,
            error_class=DivErrorList)
            if form.is_valid():
                aviso = form.save(commit=False)
                aviso.fecha = timezone.now()
                aviso.latitud = 0
                aviso.longitud = 0
                aviso.resuelto = False
                aviso.save()
                return HttpResponseRedirect(reverse('home'))
    else:
        form = AvisoForm()
    return TemplateResponse(request,
             'add_aviso.html', {'form': form, })


@login_required
def list_avisos(request, orderby=None, ordertype=None):
    if "mensaje" in request.session:
        mensaje = request.session["mensaje"]
        del request.session["mensaje"]
    else:
        mensaje = ""
    try:
        avisos = Aviso.objects.all().order_by('id')
    except avisos.DoesNotExist:
            return render_to_response('list_avisos.html',
            {'aviso': avisos,
                "mensaje": mensaje}, context_instance=RequestContext(request))
    return render_to_response('list_avisos.html', {'aviso': avisos,
        "mensaje": mensaje}, context_instance=RequestContext(request))


def list_problemas(request, orderby=None, ordertype=None):
    if "mensaje" in request.session:
        mensaje = request.session["mensaje"]
        del request.session["mensaje"]
    else:
        mensaje = ""
    try:
        resueltos = Aviso.objects.filter(resuelto=True).order_by('id')
        noresueltos = Aviso.objects.filter(resuelto=False).order_by('id')
    except resueltos.DoesNotExist or noresueltos.DoesNotExist:
            return render_to_response('list_problemas.html',
            {'resuelto': resueltos, 'noresueltos': noresueltos,
                "mensaje": mensaje}, context_instance=RequestContext(request))
    return render_to_response('list_problemas.html',
        {'resuelto': resueltos, 'noresuelto': noresueltos, "mensaje": mensaje},
        context_instance=RequestContext(request))


@login_required
def resolver(request, aviso_id):
    aviso = get_object_or_404(Aviso, id=aviso_id)
    aviso.resuelto = True
    aviso.save()
    request.session["mensaje"] = """El aviso
    con id """ + aviso_id + """ ha sido resuelto exitosamente"""
    return HttpResponseRedirect(reverse('list-avisos'))


class DivErrorList(ErrorList):
    def __unicode__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return u''
#        return u'<div class="alert alert-error"><strong>&iexcl;Error!</strong>
#%s</div>' % ''.join([u'<div class="error">%s</div>' % e for e in self])
        error_list = ''.join(
            [u'<div class="error">{0}</div>'.format(e) for e in self])
        return (
            u'<div class="alert alert-error">'
            u'<strong>&iexcl;Error!</strong>{0}</div>'
        ).format(error_list)