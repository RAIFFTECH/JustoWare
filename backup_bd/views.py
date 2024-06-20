from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
# from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Backup
import subprocess
from Justo_proy import settings


def backup_database(request):
    # Nombre del archivo de copia de seguridad
    backup_filename = f"backup_{timezone.now().strftime('%Y-%m-%d_%H-%M-%S')}.sql"

    # Ruta completa al archivo de copia de seguridad
    backup_path = f"{settings.BASE_DIR}/{backup_filename}"

    # Comando mysqldump
    db_user = settings.DATABASES['default']['USER']
    db_password = settings.DATABASES['default']['PASSWORD']
    db_name = settings.DATABASES['default']['NAME']
    command = f"mysqldump -u {db_user} -p{db_password} {db_name} > {backup_path}"

    # Ejecutar el comando mysqldump
    subprocess.run(command, shell=True)

    # Registrar la copia de seguridad en la base de datos
    backup = Backup(filename=(backup_filename), usuario="TEFA")
    backup.save()

    return HttpResponse(f"Copia de seguridad creada correctamente: {backup_filename}")



def restore_backup(request):
    if request.method == 'POST':
        # Nombre del archivo de copia de seguridad enviado desde el formulario
        backup_filename = request.POST.get('backup_filename', None)

        if backup_filename:
            # Ruta completa al archivo de copia de seguridad
            backup_path = f"{settings.BASE_DIR}/{backup_filename}"
                        
            # Comando mysql para restaurar la base de datos
            db_user = settings.DATABASES['default']['USER']
            db_password = settings.DATABASES['default']['PASSWORD']
            db_name = settings.DATABASES['default']['NAME']
            command = f"mysql -u {db_user} -p{db_password} {db_name} < {backup_path}"

            # Ejecutar el comando mysql
            subprocess.run(command, shell=True)

            return HttpResponse("La restauración de la copia de seguridad se ha completado correctamente.")
        else:
            return HttpResponse("No se ha proporcionado un nombre de archivo de copia de seguridad.")
    else:
        backups = Backup.objects.all()
        return render(request, 'restore_backup.html', {'backups': backups})
