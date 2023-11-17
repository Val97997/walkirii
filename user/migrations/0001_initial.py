# Generated by Django 4.2 on 2023-05-25 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudonym', models.CharField(blank=True, default='', max_length=50)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='MALE', help_text='Required', max_length=6)),
                ('twitter', models.CharField(blank=True, default='', max_length=100)),
                ('instagram', models.CharField(blank=True, default='', max_length=100)),
                ('linkedin', models.CharField(blank=True, default='', max_length=100)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text='Required', max_length=128, region=None)),
                ('youtube', models.CharField(blank=True, default='', max_length=100)),
                ('language', models.CharField(choices=[('aa', 'Afar'), ('ab', 'Abkhazian'), ('af', 'Afrikaans'), ('ak', 'Akan'), ('am', 'Amharic'), ('ar', 'Arabic'), ('an', 'Aragonese'), ('as', 'Assamese'), ('av', 'Avaric'), ('ae', 'Avestan'), ('ay', 'Aymara'), ('az', 'Azerbaijani'), ('ba', 'Bashkir'), ('bm', 'Bambara'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('bi', 'Bislama'), ('bo', 'Tibetan'), ('bs', 'Bosnian'), ('br', 'Breton'), ('bg', 'Bulgarian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('ch', 'Chamorro'), ('ce', 'Chechen'), ('cu', 'Church Slavic'), ('cv', 'Chuvash'), ('kw', 'Cornish'), ('co', 'Corsican'), ('cr', 'Cree'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('dv', 'Dhivehi'), ('dz', 'Dzongkha'), ('el', 'Modern Greek (1453-)'), ('en', 'English'), ('eo', 'Esperanto'), ('et', 'Estonian'), ('eu', 'Basque'), ('ee', 'Ewe'), ('fo', 'Faroese'), ('fa', 'Persian'), ('fj', 'Fijian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Western Frisian'), ('ff', 'Fulah'), ('gd', 'Scottish Gaelic'), ('ga', 'Irish'), ('gl', 'Galician'), ('gv', 'Manx'), ('gn', 'Guarani'), ('gu', 'Gujarati'), ('ht', 'Haitian'), ('ha', 'Hausa'), ('sh', 'Serbo-Croatian'), ('he', 'Hebrew'), ('hz', 'Herero'), ('hi', 'Hindi'), ('ho', 'Hiri Motu'), ('hr', 'Croatian'), ('hu', 'Hungarian'), ('hy', 'Armenian'), ('ig', 'Igbo'), ('io', 'Ido'), ('ii', 'Sichuan Yi'), ('iu', 'Inuktitut'), ('ie', 'Interlingue'), ('ia', 'Interlingua (International Auxiliary Language Association)'), ('id', 'Indonesian'), ('ik', 'Inupiaq'), ('is', 'Icelandic'), ('it', 'Italian'), ('jv', 'Javanese'), ('ja', 'Japanese'), ('kl', 'Kalaallisut'), ('kn', 'Kannada'), ('ks', 'Kashmiri'), ('ka', 'Georgian'), ('kr', 'Kanuri'), ('kk', 'Kazakh'), ('km', 'Central Khmer'), ('ki', 'Kikuyu'), ('rw', 'Kinyarwanda'), ('ky', 'Kirghiz'), ('kv', 'Komi'), ('kg', 'Kongo'), ('ko', 'Korean'), ('kj', 'Kuanyama'), ('ku', 'Kurdish'), ('lo', 'Lao'), ('la', 'Latin'), ('lv', 'Latvian'), ('li', 'Limburgan'), ('ln', 'Lingala'), ('lt', 'Lithuanian'), ('lb', 'Luxembourgish'), ('lu', 'Luba-Katanga'), ('lg', 'Ganda'), ('mh', 'Marshallese'), ('ml', 'Malayalam'), ('mr', 'Marathi'), ('mk', 'Macedonian'), ('mg', 'Malagasy'), ('mt', 'Maltese'), ('mn', 'Mongolian'), ('mi', 'Maori'), ('ms', 'Malay (macrolanguage)'), ('my', 'Burmese'), ('na', 'Nauru'), ('nv', 'Navajo'), ('nr', 'South Ndebele'), ('nd', 'North Ndebele'), ('ng', 'Ndonga'), ('ne', 'Nepali (macrolanguage)'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('nb', 'Norwegian Bokmål'), ('no', 'Norwegian'), ('ny', 'Nyanja'), ('oc', 'Occitan (post 1500)'), ('oj', 'Ojibwa'), ('or', 'Oriya (macrolanguage)'), ('om', 'Oromo'), ('os', 'Ossetian'), ('pa', 'Panjabi'), ('pi', 'Pali'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('ps', 'Pushto'), ('qu', 'Quechua'), ('rm', 'Romansh'), ('ro', 'Romanian'), ('rn', 'Rundi'), ('ru', 'Russian'), ('sg', 'Sango'), ('sa', 'Sanskrit'), ('si', 'Sinhala'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('se', 'Northern Sami'), ('sm', 'Samoan'), ('sn', 'Shona'), ('sd', 'Sindhi'), ('so', 'Somali'), ('st', 'Southern Sotho'), ('es', 'Spanish'), ('sq', 'Albanian'), ('sc', 'Sardinian'), ('sr', 'Serbian'), ('ss', 'Swati'), ('su', 'Sundanese'), ('sw', 'Swahili (macrolanguage)'), ('sv', 'Swedish'), ('ty', 'Tahitian'), ('ta', 'Tamil'), ('tt', 'Tatar'), ('te', 'Telugu'), ('tg', 'Tajik'), ('tl', 'Tagalog'), ('th', 'Thai'), ('ti', 'Tigrinya'), ('to', 'Tonga (Tonga Islands)'), ('tn', 'Tswana'), ('ts', 'Tsonga'), ('tk', 'Turkmen'), ('tr', 'Turkish'), ('tw', 'Twi'), ('ug', 'Uighur'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('ve', 'Venda'), ('vi', 'Vietnamese'), ('vo', 'Volapük'), ('wa', 'Walloon'), ('wo', 'Wolof'), ('xh', 'Xhosa'), ('yi', 'Yiddish'), ('yo', 'Yoruba'), ('za', 'Zhuang'), ('zh', 'Chinese'), ('zu', 'Zulu')], help_text='Required', max_length=2)),
                ('secondlanguage', models.CharField(blank=True, choices=[('aa', 'Afar'), ('ab', 'Abkhazian'), ('af', 'Afrikaans'), ('ak', 'Akan'), ('am', 'Amharic'), ('ar', 'Arabic'), ('an', 'Aragonese'), ('as', 'Assamese'), ('av', 'Avaric'), ('ae', 'Avestan'), ('ay', 'Aymara'), ('az', 'Azerbaijani'), ('ba', 'Bashkir'), ('bm', 'Bambara'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('bi', 'Bislama'), ('bo', 'Tibetan'), ('bs', 'Bosnian'), ('br', 'Breton'), ('bg', 'Bulgarian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('ch', 'Chamorro'), ('ce', 'Chechen'), ('cu', 'Church Slavic'), ('cv', 'Chuvash'), ('kw', 'Cornish'), ('co', 'Corsican'), ('cr', 'Cree'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('dv', 'Dhivehi'), ('dz', 'Dzongkha'), ('el', 'Modern Greek (1453-)'), ('en', 'English'), ('eo', 'Esperanto'), ('et', 'Estonian'), ('eu', 'Basque'), ('ee', 'Ewe'), ('fo', 'Faroese'), ('fa', 'Persian'), ('fj', 'Fijian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Western Frisian'), ('ff', 'Fulah'), ('gd', 'Scottish Gaelic'), ('ga', 'Irish'), ('gl', 'Galician'), ('gv', 'Manx'), ('gn', 'Guarani'), ('gu', 'Gujarati'), ('ht', 'Haitian'), ('ha', 'Hausa'), ('sh', 'Serbo-Croatian'), ('he', 'Hebrew'), ('hz', 'Herero'), ('hi', 'Hindi'), ('ho', 'Hiri Motu'), ('hr', 'Croatian'), ('hu', 'Hungarian'), ('hy', 'Armenian'), ('ig', 'Igbo'), ('io', 'Ido'), ('ii', 'Sichuan Yi'), ('iu', 'Inuktitut'), ('ie', 'Interlingue'), ('ia', 'Interlingua (International Auxiliary Language Association)'), ('id', 'Indonesian'), ('ik', 'Inupiaq'), ('is', 'Icelandic'), ('it', 'Italian'), ('jv', 'Javanese'), ('ja', 'Japanese'), ('kl', 'Kalaallisut'), ('kn', 'Kannada'), ('ks', 'Kashmiri'), ('ka', 'Georgian'), ('kr', 'Kanuri'), ('kk', 'Kazakh'), ('km', 'Central Khmer'), ('ki', 'Kikuyu'), ('rw', 'Kinyarwanda'), ('ky', 'Kirghiz'), ('kv', 'Komi'), ('kg', 'Kongo'), ('ko', 'Korean'), ('kj', 'Kuanyama'), ('ku', 'Kurdish'), ('lo', 'Lao'), ('la', 'Latin'), ('lv', 'Latvian'), ('li', 'Limburgan'), ('ln', 'Lingala'), ('lt', 'Lithuanian'), ('lb', 'Luxembourgish'), ('lu', 'Luba-Katanga'), ('lg', 'Ganda'), ('mh', 'Marshallese'), ('ml', 'Malayalam'), ('mr', 'Marathi'), ('mk', 'Macedonian'), ('mg', 'Malagasy'), ('mt', 'Maltese'), ('mn', 'Mongolian'), ('mi', 'Maori'), ('ms', 'Malay (macrolanguage)'), ('my', 'Burmese'), ('na', 'Nauru'), ('nv', 'Navajo'), ('nr', 'South Ndebele'), ('nd', 'North Ndebele'), ('ng', 'Ndonga'), ('ne', 'Nepali (macrolanguage)'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('nb', 'Norwegian Bokmål'), ('no', 'Norwegian'), ('ny', 'Nyanja'), ('oc', 'Occitan (post 1500)'), ('oj', 'Ojibwa'), ('or', 'Oriya (macrolanguage)'), ('om', 'Oromo'), ('os', 'Ossetian'), ('pa', 'Panjabi'), ('pi', 'Pali'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('ps', 'Pushto'), ('qu', 'Quechua'), ('rm', 'Romansh'), ('ro', 'Romanian'), ('rn', 'Rundi'), ('ru', 'Russian'), ('sg', 'Sango'), ('sa', 'Sanskrit'), ('si', 'Sinhala'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('se', 'Northern Sami'), ('sm', 'Samoan'), ('sn', 'Shona'), ('sd', 'Sindhi'), ('so', 'Somali'), ('st', 'Southern Sotho'), ('es', 'Spanish'), ('sq', 'Albanian'), ('sc', 'Sardinian'), ('sr', 'Serbian'), ('ss', 'Swati'), ('su', 'Sundanese'), ('sw', 'Swahili (macrolanguage)'), ('sv', 'Swedish'), ('ty', 'Tahitian'), ('ta', 'Tamil'), ('tt', 'Tatar'), ('te', 'Telugu'), ('tg', 'Tajik'), ('tl', 'Tagalog'), ('th', 'Thai'), ('ti', 'Tigrinya'), ('to', 'Tonga (Tonga Islands)'), ('tn', 'Tswana'), ('ts', 'Tsonga'), ('tk', 'Turkmen'), ('tr', 'Turkish'), ('tw', 'Twi'), ('ug', 'Uighur'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('ve', 'Venda'), ('vi', 'Vietnamese'), ('vo', 'Volapük'), ('wa', 'Walloon'), ('wo', 'Wolof'), ('xh', 'Xhosa'), ('yi', 'Yiddish'), ('yo', 'Yoruba'), ('za', 'Zhuang'), ('zh', 'Chinese'), ('zu', 'Zulu')], help_text='Optional', max_length=2, verbose_name='Second Language')),
                ('location', models.CharField(help_text='Required', max_length=50)),
                ('avatar', models.ImageField(default='media/avatar.jpg', upload_to=user.models.user_directory_path)),
                ('birthday', models.DateField(null=True, verbose_name='Birthday')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]