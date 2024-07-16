# Generated by Django 4.2.9 on 2024-01-10 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post2_category_remove_topic_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post2',
            name='category',
            field=models.CharField(choices=[('Rowery miejskie', 'Rowery miejskie'), ('Rowery górskie', 'Rowery górskie'), ('Rowery szosowe', 'Rowery szosowe'), ('Rowery trekkingowe', 'Rowery trekkingowe'), ('Akcesoria rowerowe', 'Akcesoria rowerowe'), ('Rowery torowe', 'Rowery torowe'), ('Wyprawy rowerowe', 'Wyprawy rowerowe'), ('Serwis i konserwacja', 'Serwis i konserwacja'), ('Porady dla początkujących', 'Porady dla początkujących'), ('Sprzęt rowerowy', 'Sprzęt rowerowy'), ('Zdrowie i kondycja', 'Zdrowie i kondycja'), ('Inne', 'Inne'), ('Dieta i suplementy', 'Dieta i suplementy')], default='Inne', max_length=127),
        ),
        migrations.AddField(
            model_name='topic',
            name='category',
            field=models.CharField(choices=[('Rowery miejskie', 'Rowery miejskie'), ('Rowery górskie', 'Rowery górskie'), ('Rowery szosowe', 'Rowery szosowe'), ('Rowery trekkingowe', 'Rowery trekkingowe'), ('Akcesoria rowerowe', 'Akcesoria rowerowe'), ('Rowery torowe', 'Rowery torowe'), ('Wyprawy rowerowe', 'Wyprawy rowerowe'), ('Serwis i konserwacja', 'Serwis i konserwacja'), ('Porady dla początkujących', 'Porady dla początkujących'), ('Sprzęt rowerowy', 'Sprzęt rowerowy'), ('Zdrowie i kondycja', 'Zdrowie i kondycja'), ('Inne', 'Inne'), ('Dieta i suplementy', 'Dieta i suplementy')], default='Inne', max_length=127),
        ),
    ]
