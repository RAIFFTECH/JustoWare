from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import COMPROBANTES

@receiver(post_save, sender=COMPROBANTES)
def asignar_numero_COMPROBANTES(sender, instance, created, **kwargs):
    if created and instance.numero is None:
        # Solo si el objeto HECHO_ECONO es recién creado y el número aún no ha sido asignado
        ultimo_numero = COMPROBANTES.objects.filter(docto_conta=instance.docto_conta).order_by('-numero').first()
        nuevo_numero = ultimo_numero.numero + 5 if ultimo_numero else 1
        instance.numero = nuevo_numero
        instance.save()