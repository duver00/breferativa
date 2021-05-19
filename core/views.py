from itertools import product

from django.http import request
from django.shortcuts import render, redirect
from .models import Fichas, Autores, MateriasPrimas, Yacimientos, Provincias, Refauto, Refmat, Refyac, Refpro
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse


# Create your views here.

class InventarioList(ListView):
    template_name = 'busqueda_navbar.html'
    context_object_name = 'fichas'

    def get_queryset(self):
        return Refauto.objects.prefetch_related('inventario__refpro__codpro').order_by('inventario').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['materias'] = Refmat.objects.prefetch_related('codmat__refmat_set__codyac').order_by('inventario')
        context['autores'] = Autores.objects.all().order_by('desaut')
        context['provincia'] = Provincias.objects.all().order_by('provincia').defer('cubanorte')
        context['mprima'] = MateriasPrimas.objects.all().only('desmat').order_by('desmat')
        return context


def buscar_inventario(request):
    global prima1
    autores = Autores.objects.all().order_by('desaut')
    provincias = Provincias.objects.all().order_by('provincia').defer('cubanorte')
    mprima = MateriasPrimas.objects.all().only('desmat').order_by('desmat')
    count_total = Fichas.objects.all().count()
    if request.method == "GET":
        chk = request.GET.get("chk")
        if request.GET.get('inventario'):
            ficha = request.GET.get('inventario')
            ficha_resultado = Refauto.objects.all().filter(inventario=ficha)
            mprima1 = Refmat.objects.all().filter(inventario__in=ficha_resultado)
            prov1 = Refpro.objects.all().filter(inventario__refauto__in=ficha_resultado)
            return render(request, "resultados_list.html", {'ficha_resultado': ficha_resultado, 'materias': mprima1,
                                                            'autores': autores, 'provincia': provincias,
                                                            'mprima': mprima, 'prov1': prov1})

        elif chk and request.GET.get('autor', None) and request.GET.get('prima', None) and request.GET.get('province',
                                                                                                           None):
            autor_list = request.GET.get('autor')
            province_list = request.GET.get('province')
            materia_list = request.GET.get('prima')
            autorpv = Autores.objects.all().get(codaut__exact=autor_list)
            qficha = Fichas.objects.all().prefetch_related('refauto__codaut__refauto_set', 'refpro__codpro__refpro_set',
                                                           'refyac').filter(refauto__codaut__exact=autor_list,
                                                                            refpro__codpro__codpro__exact=province_list)
            qmateria = Refmat.objects.all().filter(inventario__in=qficha, codmat=materia_list)
            paginator = Paginator(qficha, 25)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            parametros = request.GET.copy()
            count = qmateria.count()
            return render(request, 'all_filters.html', {'qficha': qficha, 'qmateria': qmateria, 'autores': autores,
                                                        'provincia': provincias, 'mprima': mprima, 'autorpv': autorpv,
                                                        'page_obj': page_obj,'parametros': parametros,'count':count, 'total':count_total  })

        elif chk and request.GET.get('autor', None) and request.GET.get('prima', None):
            autor_list = request.GET.get('autor')
            materia_list = request.GET.get('prima')
            autorpv = Autores.objects.all().get(codaut__exact=autor_list)
            qficha = Fichas.objects.all().prefetch_related('refauto__codaut__refauto_set', 'refpro__codpro__refpro_set',
                                                           'refyac').filter(refauto__codaut__exact=autor_list)
            qmateria = Refmat.objects.all().filter(inventario__in=qficha, codmat=materia_list)
            mp = []
            for inv in qmateria.all():
                mp.append(inv.inventario)
            qficha = Fichas.objects.all().prefetch_related('refauto__codaut__refauto_set', 'refpro__codpro__refpro_set',
                                                           'refyac').filter(
                refauto__codaut__exact=autor_list, inventario__in=mp)
            paginator = Paginator(qficha, 25)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            parametros = request.GET.copy()
            count = qmateria.count()
            return render(request, 'prima_autor.html', {'qficha': qficha, 'qmateria': qmateria, 'autores': autores,
                                                        'provincia': provincias, 'mprima': mprima, 'autorpv': autorpv,
                                                        'parametros': parametros, 'count':count, 'total':count_total, 'page_obj':page_obj})

        elif chk and request.GET.get('autor', None) and request.GET.get('province', None):
            autor_list = request.GET.get('autor')
            province_list = request.GET.get('province')
            autorpv = Autores.objects.all().get(codaut__exact=autor_list)
            qficha = Fichas.objects.all().prefetch_related('refauto__codaut__refauto_set', 'refpro__codpro__refpro_set',
                                                           'refyac').filter(refauto__codaut__exact=autor_list,
                                                                            refpro__codpro__codpro__exact=province_list)
            mprima1 = Refmat.objects.all().filter(inventario__in=qficha)
            paginator = Paginator(qficha, 25)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            parametros = request.GET.copy()
            count = qficha.count()
            return render(request, 'provincia_autor.html',
                          {'qficha': qficha, 'autores': autores, 'provincia': provincias,
                           'mprima': mprima, 'autorpv': autorpv, 'materias': mprima1,'page_obj': page_obj,
                           'parametros': parametros, 'count':count, 'total': count_total})

        elif chk and request.GET.get('autor', None):
            autor_list = request.GET.get('autor')
            autorpv = Autores.objects.all().get(codaut__exact=autor_list)
            qficha = Fichas.objects.all().prefetch_related('refauto__codaut__refauto_set', 'refpro__codpro__refpro_set',
                                                           'refyac').filter(refauto__codaut__exact=autor_list)
            mprima1 = Refmat.objects.all().filter(inventario__in=qficha)
            paginator = Paginator(qficha, 25)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            parametros = request.GET.copy()
            count = qficha.count()
            return render(request, 'autor.html', {'qficha': qficha, 'autores': autores, 'provincia': provincias,
                                                  'mprima': mprima, 'autorpv': autorpv, 'materias': mprima1,
                                                  'page_obj': page_obj, 'parametros': parametros,'count':count, 'total':count_total })

        elif chk and request.GET.get('prima', None) and request.GET.get('province', None):
            materia_list = request.GET.get('prima')
            province_list = request.GET.get('province')
            provinciapv = Provincias.objects.get(codpro__exact=province_list)
            qficha1 = Fichas.objects.all().prefetch_related('refauto__codaut__refauto_set','refpro__codpro__refpro_set',
                                                            'refyac').filter(
                refpro__codpro__codpro__exact=province_list)
            qmateria = Refmat.objects.all().filter(inventario__in=qficha1, codmat=materia_list)
            mp = []
            for inv in qmateria.all():
                mp.append(inv.inventario)
            qficha = Fichas.objects.all().prefetch_related('refauto__codaut__refauto_set','refpro__codpro__refpro_set',
                                                            'refyac').filter(
                refpro__codpro__codpro__exact=province_list, inventario__in=mp)
            paginator = Paginator(qficha,25)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            parametros = request.GET.copy()
            count = qficha.count()
            return render(request, 'provincia_prima.html', { 'qmateria': qmateria, 'autores': autores,
                                                            'provincia': provincias, 'mprima': mprima,
                                                            'page_obj': page_obj, 'parametros': parametros, 'count':count,
                                                             'total': count_total, 'provinciapv':provinciapv})

        elif chk and request.GET.get('province', None):
            province_list = request.GET.get('province')
            qficha = Fichas.objects.all().prefetch_related('refauto__codaut__refauto_set',
                                                           'refpro__codpro__refpro_set').filter(
                refpro__codpro__codpro__exact=province_list)
            mprima1 = Refmat.objects.all().filter(inventario__in=qficha)
            paginator = Paginator(qficha, 25)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            parametros = request.GET.copy()
            count = qficha.count()
            return render(request, 'provincia.html', {'autores': autores, 'provincia': provincias,
                                                      'mprima': mprima, 'materias': mprima1, 'page_obj': page_obj,
                                                      'parametros': parametros, 'provinciab':province_list, 'count':count,
                                                      'total':count_total})

        elif chk and request.GET.get('prima', None):
            materia_list = request.GET.get('prima')
            materia = Refmat.objects.all().filter(codmat=materia_list)
            mp = []
            for inv in materia.all():
                mp.append(inv.inventario)
            qficha = Fichas.objects.all().prefetch_related('refauto__codaut__refauto_set', 'refpro__codpro__refpro_set').filter(inventario__in=mp)
            paginatormp = Paginator(qficha, 25)
            page_number = request.GET.get('page')
            page_mp = paginatormp.get_page(page_number)
            parametros = request.GET.copy()
            count = qficha.count()
            prov1 = Refpro.objects.all().filter(inventario__inventario__in=qficha)
            return render(request, 'prima.html', {'autores': autores, 'provincia': provincias,
                                                      'mprima': mprima,'page_mp':page_mp, 'parametros': parametros,
                                                  'materia_list': materia_list, 'materia': materia,'count':count, 'total':count_total,
                                                  'prov1':prov1})
        else:
            return redirect('/')
    else:
        return render(request, "index.html")
