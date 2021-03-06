# Generated by Django 2.2.6 on 2020-05-26 16:38

import app.revisioner.managers
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import utils.mixins.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('authentication', '0003_workspace_active_sso'),
        ('definitions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.CharField(db_index=True, default=utils.mixins.models.uuid4_hex, max_length=32, editable=False, primary_key=True, unique=True)),
                ('revision_count', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Timestamp for when the run was created.')),
                ('started_at', models.DateTimeField(default=None, help_text='Timestamp for when run queued actual processing tasks.', null=True)),
                ('finished_at', models.DateTimeField(default=None, help_text='Timestamp for when run finished calculating all revisions.', null=True)),
                ('datastore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='run_history', to='definitions.Datastore')),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='run_history', to='authentication.Workspace')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RunTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_task_id', models.CharField(help_text='Task ID for Celery', max_length=512, null=True)),
                ('status', models.CharField(choices=[('SUCCESS', 'SUCCESS'), ('FAILURE', 'FAILURE'), ('PENDING', 'PENDING'), ('REVOKED', 'REVOKED')], default='PENDING', max_length=10)),
                ('started_at', models.DateTimeField(default=None, help_text='Timestamp for when the task started', null=True)),
                ('finished_at', models.DateTimeField(default=None, help_text='Timestamp for when the task finished', null=True)),
                ('storage_path', models.CharField(max_length=512, unique=True)),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='revisioner.Run')),
            ],
        ),
        migrations.CreateModel(
            name='RevisionerError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('task_fcn', models.CharField(default=None, max_length=40, null=True)),
                ('exc_type', models.CharField(default=None, max_length=40, null=True)),
                ('exc_stacktrace', models.TextField(default=None, null=True)),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='errors', to='revisioner.Run')),
                ('task', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='revisioner.RunTask')),
            ],
            options={
                'db_table': 'revisioner_error',
            },
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('revision_id', models.CharField(max_length=40, primary_key=True, serialize=False, unique=True)),
                ('resource_id', models.CharField(max_length=30, null=True)),
                ('parent_resource_id', models.CharField(max_length=30, null=True)),
                ('action', models.IntegerField(choices=[(1, 'Created'), (2, 'Modified'), (3, 'Dropped')])),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('checksum', models.CharField(max_length=32)),
                ('first_seen_on', models.DateTimeField()),
                ('applied_on', models.DateTimeField(default=None, null=True)),
                ('first_seen_run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original_revisions', to='revisioner.Run')),
                ('parent_resource_revision', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revisions', to='revisioner.Revision')),
                ('parent_resource_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType')),
                ('resource_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType')),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revisions', to='revisioner.Run')),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='authentication.Workspace')),
            ],
            managers=[
                ('objects', app.revisioner.managers.RevisionManager()),
            ],
        ),
        migrations.AddConstraint(
            model_name='revision',
            constraint=models.UniqueConstraint(fields=('workspace_id', 'checksum'), name='unique_revision_checksum'),
        ),
    ]
