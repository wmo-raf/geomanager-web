# Generated by Django 4.2.7 on 2023-12-04 08:36

from django.db import migrations, models
import django.db.models.deletion
import home.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailcache.cache
import wagtailmetadata.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('banner_title', models.CharField(max_length=255, verbose_name='Banner Title')),
                ('banner_subtitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Banner Subtitle')),
                ('intro_text', wagtail.fields.RichTextField(blank=True, help_text='Introduction section description', null=True, verbose_name='Introduction text')),
                ('info_blocks', wagtail.fields.StreamField([('info', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Section title', label='Section Title', max_length=100)), ('text', wagtail.blocks.RichTextBlock(features=['bold', 'li', 'ul'], help_text='Section description', label='Section Text')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))], label='Info'))], blank=True, null=True, use_json_field=True, verbose_name='Info Section')),
                ('feature_blocks', wagtail.fields.StreamField([('feature', wagtail.blocks.StructBlock([('icon', wagtail.blocks.CharBlock(label='Icon', max_length=100)), ('title', wagtail.blocks.CharBlock(label='Title', max_length=100)), ('description', wagtail.blocks.CharBlock(label='Description', max_length=150))], label='Feature'))], blank=True, null=True, use_json_field=True, verbose_name='Features')),
                ('dataset_blocks', wagtail.fields.StreamField([('category', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title', max_length=100)), ('tag', wagtail.blocks.ChoiceBlock(choices=home.blocks.get_dataset_categories, label='Select Category'))], label='Dataset Category'))], blank=True, null=True, use_json_field=True, verbose_name='Available Datasets')),
                ('banner_image', models.ForeignKey(blank=True, help_text='A high quality banner image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Banner Image')),
                ('intro_image', models.ForeignKey(blank=True, help_text='A high quality image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Introduction Image')),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Search image')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailmetadata.models.WagtailImageMetadataMixin, wagtailcache.cache.WagtailCacheMixin, 'wagtailcore.page', models.Model),
        ),
    ]
