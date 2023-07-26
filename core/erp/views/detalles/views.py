from django.shortcuts import render

from core.erp.models import *


def ver_productos(request, id):
    template_name = 'detalles/view.html'
    productos = Product.objects.filter(active=True, id=id)
    categorias = Category.objects.filter(active=True)

    context = {"productos": productos, "categorias": categorias}
    return render(request, template_name, context)


def view_general(request):
    template_name = 'detalles/view_total.html'
    pr = Product.objects.filter(active=True)
    categorias = Category.objects.filter(active=True)
    total = []
    for c in categorias:
        productos = Product.objects.filter(active=True, cate=c.id)
        # TENGO TODOS LOS PROD PARA LA CAT DE ARRIBA
        listado = []
        for pro in productos:
            item = {
                'producto': {
                    'id': pro.id,
                    'name': pro.name,
                    'get_image': pro.get_image,
                    'desc': pro.desc,
                    'pvp': pro.pvp,
                    'cate': pro.cate,
                }
            }
            listado.append(item)
        item1 = {
            'categ': {
                'cat': c.name,
                'cat_prod': listado
            }
        }
        # Supuestamente aqui tengo los item1
        # las categorias como categ dentro de los item
        # y dentro la categoria y un listado de sus productos
        if len(listado) != 0:
            total.append(item1)

    context = {'total_cat_pro': total, 'categorias': categorias}
    return render(request, template_name, context)
