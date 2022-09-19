# Generated by Django 4.0.6 on 2022-07-25 18:49

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('tanks', 'Танки'), ('healers', 'Хилы'), ('damagers', 'ДД'), ('merchants', 'Торговцы'), ('guildmasters', 'Гилдмастеры'), ('questgivers', 'Квестгиверы'), ('blacksmiths', 'Кузнецы'), ('tanners', 'Кожевники'), ('potionmakers', 'Зельевары'), ('spellmasters', 'Мастера заклинаний')], default='tanks', max_length=12)),
                ('title', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('media', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ad',
                'verbose_name_plural': 'Ads',
                'ordering': ('-dateCreation',),
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreation', models.DateTimeField(auto_now_add=True, verbose_name='Date Creation')),
                ('text', models.TextField(verbose_name='Text')),
                ('status_remove', models.BooleanField(default=False, verbose_name='Отклик - отклонен')),
                ('status_add', models.BooleanField(default=False, verbose_name='Отклик - принят')),
                ('replyAd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Advertisement.advertisement')),
                ('replyUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reply',
                'verbose_name_plural': 'Replys',
                'ordering': ('-dateCreation',),
            },
        ),
    ]
