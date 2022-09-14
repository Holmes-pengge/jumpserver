# Generated by Django 3.2.14 on 2022-08-11 07:11
import assets.models.platform
import django.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0102_auto_20220803_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='platform',
            field=models.ForeignKey(default=assets.models.platform.Platform.default, on_delete=django.db.models.deletion.PROTECT, related_name='assets', to='assets.platform', verbose_name='Platform'),
        ),
        migrations.RemoveField(
            model_name='asset',
            name='_protocols',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='admin_user',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='number',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='public_ip',
        ),
        migrations.AlterModelOptions(
            name='asset',
            options={'ordering': ['name'], 'permissions': [('refresh_assethardwareinfo', 'Can refresh asset hardware info'), ('test_assetconnectivity', 'Can test asset connectivity'), ('push_assetsystemuser', 'Can push system user to asset'), ('match_asset', 'Can match asset'), ('add_assettonode', 'Add asset to node'), ('move_assettonode', 'Move asset to node')], 'verbose_name': 'Asset'},
        ),
        migrations.RenameField(
            model_name='asset',
            old_name='hostname',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='asset',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='asset',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='asset',
            name='updated_by',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Updated by'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='created_by',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by'),
        ),
    ]
