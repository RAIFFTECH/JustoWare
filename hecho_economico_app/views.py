from django.shortcuts import render
from hecho_economico_app.forms import HechoEconoForm
from detalle_economico_app.forms import DetalleEconoForm


def maestro_detalle(request):
    if request.method == 'POST':
        hecho_econo_form = HechoEconoForm(request.POST)
        detalle_econo_form = DetalleEconoForm(request.POST)
        if hecho_econo_form.is_valid() and detalle_econo_form.is_valid():
            # Guardar el formulario maestro
            hecho_econo = hecho_econo_form.save()
            # Asociar el detalle al maestro y guardarlo
            detalle_econo = detalle_econo_form.save(commit=False)
            detalle_econo.hecho_econo = hecho_econo
            detalle_econo.save()
            return render(request, 'exito.html')
    else:
        hecho_econo_form = HechoEconoForm()
        detalle_econo_form = DetalleEconoForm()
    return render(request, 'detalles_hecho_eco.html', {'hecho_econo_form': hecho_econo_form, 'detalle_econo_form': detalle_econo_form})
