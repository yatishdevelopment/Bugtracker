# Generated by Django 3.0.8 on 2020-08-02 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_type', models.PositiveSmallIntegerField(choices=[(1, 'feature'), (2, 'bug')])),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='bugapp.User')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='bugapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_name', models.CharField(max_length=200)),
                ('issue_descr', models.CharField(max_length=500)),
                ('assignee', models.CharField(max_length=20)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'new'), (2, 'in progress'), (3, 'on hold'), (4, 'closed')])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bugapp.User', verbose_name='issues')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='bugapp.User')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bugapp.Project', verbose_name='issues')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='bugapp.User')),
            ],
        ),
    ]
