# Generated by Django 4.0.4 on 2022-05-04 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_category_country_video_ytchannel_ytviews_delete_car_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ytviews',
            old_name='Channel_id',
            new_name='channel_id',
        ),
        migrations.RenameField(
            model_name='ytviews',
            old_name='Comment_count',
            new_name='comment_count',
        ),
        migrations.RenameField(
            model_name='ytviews',
            old_name='Disklikes',
            new_name='dislikes',
        ),
        migrations.RenameField(
            model_name='ytviews',
            old_name='Likes',
            new_name='likes',
        ),
        migrations.RenameField(
            model_name='ytviews',
            old_name='Trending_date',
            new_name='trending_date',
        ),
        migrations.RenameField(
            model_name='ytviews',
            old_name='Video_ID',
            new_name='video_id',
        ),
        migrations.RenameField(
            model_name='ytviews',
            old_name='View_Count',
            new_name='view_count',
        ),
    ]
