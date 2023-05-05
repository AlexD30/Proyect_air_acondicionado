# Generated by Django 4.0.4 on 2023-04-02 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = False

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('idBanco', models.AutoField(primary_key=False, serialize=False, verbose_name='Id de banco')),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('idComuna', models.AutoField(primary_key=False, serialize=False, verbose_name='Id de comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.AutoField(primary_key=False, serialize=False, verbose_name='Id de region')),
            ],
        ),
        migrations.CreateModel(
            name='DueñoEstacionamiento',
            fields=[
                ('idDueno', models.AutoField(primary_key=False, serialize=False, verbose_name='Id de dueño')),
                ('nombreUsuario', models.CharField(blank=False, max_length=50, null=False, verbose_name='Nombre de usuario')),
                ('p_apellido', models.CharField(max_length=50, verbose_name='Primer apellido')),
                ('s_apellido', models.CharField(max_length=50, verbose_name='Segundo apellido')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion')),
                ('nombreCalle', models.CharField(max_length=50, verbose_name='Nombre calle')),
                ('cuentaBancaria', models.CharField(max_length=50, verbose_name='Cuenta bancaria')),
                ('correo', models.CharField(max_length=50, verbose_name='Correo')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
                ('comuna', models.ForeignKey(blank=False, null=False, on_delete=django.db.models.deletion.CASCADE, to='core.comuna')),
                ('region', models.ForeignKey(blank=False, null=False, on_delete=django.db.models.deletion.CASCADE, to='core.region')),
            ],
        ),
        migrations.CreateModel(
            name='ClienteArrendador',
            fields=[
                ('idArrendador', models.AutoField(primary_key=False, serialize=False, verbose_name='Id de dueño')),
                ('nombreUsuario', models.CharField(blank=False, max_length=50, null=False, verbose_name='Nombre de usuario')),
                ('p_apellidos', models.CharField(max_length=50, verbose_name='Primer apellido')),
                ('s_apellido', models.CharField(max_length=50, verbose_name='Segundo apellido')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion')),
                ('tarjetaCredito', models.CharField(max_length=50, verbose_name='Cuenta bancaria')),
                ('patente', models.CharField(max_length=50, verbose_name='Nombre calle')),
                ('marca', models.CharField(max_length=50, verbose_name='Nombre calle')),
                ('modelo', models.CharField(max_length=50, verbose_name='Nombre calle')),
                ('anio', models.IntegerField(verbose_name='Nombre calle')),
                ('correo', models.CharField(max_length=50, verbose_name='Correo')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
                ('banco', models.ForeignKey(blank=False, null=False, on_delete=django.db.models.deletion.CASCADE, to='core.banco')),
                ('comuna', models.ForeignKey(blank=False, null=False, on_delete=django.db.models.deletion.CASCADE, to='core.comuna')),
                ('region', models.ForeignKey(blank=False, null=False, on_delete=django.db.models.deletion.CASCADE, to='core.region')),
            ],
        ),
    ]
