# Generated by Django 3.2.4 on 2022-11-22 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('image', models.ImageField(blank=True, default='profileimagess/profile-avatar.png', upload_to='profileimages/')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'OTHER')], max_length=1)),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
