# Generated by Django 4.2.7 on 2024-04-02 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ratings', '0003_account_model_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating_model',
            name='movie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='Ratings.movie_model'),
        ),
        migrations.AlterField(
            model_name='rating_model',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='Ratings.account_model'),
        ),
    ]
