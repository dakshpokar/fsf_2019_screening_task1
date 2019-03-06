# Generated by Django 2.1 on 2019-03-06 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TM', '0005_teams_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipToTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='belongs_to',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TM.Teams'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membershiptotask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TM.Task'),
        ),
        migrations.AddField(
            model_name='task',
            name='assigned_members',
            field=models.ManyToManyField(related_name='memberOfTask', through='TM.MembershipToTask', to=settings.AUTH_USER_MODEL),
        ),
    ]
