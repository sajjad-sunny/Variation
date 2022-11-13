import random

name = ['Cristian Romero', 'German Pezzella', 'Gonzalo Montiel', 'Juan Foyth', 'Lisandro Martinez', 'Marcos Senesi',
        'Nahuel Molina',  'Nicolas Otamendi', 'Nicolas Tagliafico', 'Angel Correa', 'Julian Alvarez', 'Lautaro Martinez',
        'Nicolas Gonzalez', 'Franco Armani', 'Geronimo Rulli', 'Juan Musso', 'Alexis Mac Allister', 'Angel Di Maria',
        'Exequiel Palacios', 'Giovani Lo Celso', 'Guido Rodriguez', 'Joaquin Correa', 'Marcos Acuna', 'Alejandro Gomez',
        'Rodrigo de Paul']

country = ['Argentina','Argentina','Argentina','Argentina','Argentina','Argentina','Argentina','Argentina','Argentina',
           'Argentina','Argentina','Argentina','Argentina','Argentina','Argentina','Argentina','Argentina','Argentina',
           'Argentina','Argentina','Argentina','Argentina','Argentina','Argentina','Argentina','Argentina']

profession = ['Argentina Football Player','Argentina Football Player','Argentina Football Player','Argentina Football Player',
              'Argentina Football Player','Argentina Football Player','Argentina Football Player','Argentina Football Player',
              'Argentina Football Player','Argentina Football Player','Argentina Football Player','Argentina Football Player',
              'Argentina Football Player','Argentina Football Player','Argentina Football Player','Argentina Football Player',
              'Argentina Football Player','Argentina Football Player','Argentina Football Player','Argentina Football Player',
              'Argentina Football Player','Argentina Football Player','Argentina Football Player','Argentina Football Player',
              'Argentina Football Player','Argentina Football Player']

nickname = ['Cuti','Pezzella','Montiel','Juan','The butcher of Amsterdam','The Gladiator','Negro, Moli','The Bianconeri',
            'The General,El Mohicano','Nicolas','Angelito','The Spider','The Bull','la bestia','Rulli','Juan','Mac',
            'angelito, fideo','Pala','Monito','Rodriguez','El Tucu','Huevo','Gomez','Lechuga']

birthplace = ['Cordoba, Argentina','Bahia Blanca, Argentina','Gonzalez Catan, Argentina','La Plata, Argentina','Gualeguay, Argentina',
              'Concordia, Argentina','Embalse, Argentina','Hurlingham, Argentina','El Talar, Argentina','Rafael Calzada, Argentina',
              'Rosario, Argentina','Calchín, Argentina','Bahía Blanca, Argentina','San Antonio, Texas','Casilda, Argentina',
              'La Plata, Argentina','San Nicolás de los Arroyos, Argentina','La Pampa, Argentina','Rosario, Argentina','Famaillá, Argentina',
              'Rosario, Argentina','Sáenz Peña, Argentina','Juan Bautista Alberdi, Argentina','Zapala, Argentina','Buenos Aires, Argentina',
              'Sarandí, Argentina']

citizen = ['Argentinian','Argentinian','Argentinian','Argentinian','Argentinian','Argentinian','Argentinian','Argentinian',
           'Argentinian','Argentinian','Argentinian','Argentinian','Argentinian','Argentinian','Argentinian','Argentinian',
           'Argentinian','Argentinian','Argentinian','Argentinian','Argentinian','Argentinian','Argentinian','Argentinian',
           'Argentinian','Argentinian']

hometown = ['Cordoba, Argentina','Bahia Blanca, Argentina','Gonzalez Catan, Argentina','La Plata, Argentina','Gualeguay, Argentina',
            'Concordia, Argentina','Embalse, Argentina','Hurlingham, Argentina','El Talar, Argentina','Rafael Calzada, Argentina',
            'Rosario, Argentina','Calchín, Argentina','Bahía Blanca, Argentina','San Antonio, Texas','Casilda, Argentina','La Plata, Argentina',
            'San Nicolás de los Arroyos, Argentina','La Pampa, Argentina','Rosario, Argentina','Famaillá, Argentina','Rosario, Argentina',
            'Sáenz Peña, Argentina','Juan Bautista Alberdi, Argentina','Zapala, Argentina','Buenos Aires, Argentina','Sarandí, Argentina']

religion = ['Christian','Christian','Christian','Christian','Christian','Christian','Christian','Christian','Christian',
            'Christian','Christian','Christian','Christian','Christian','Christian','Christian','Christian','Christian',
            'Christian','Christian','Christian','Christian','Christian','Christian','Christian','Christian']

zodiac = ['Taurus','Cancer','Capricorn','Capricorn','Capricorn','Taurus','Aries','Cancer','Aquarius','Virgo','Pisces',
          'Aquarius','Leo','Aries','Libra','Taurus','Taurus','Capricorn','Aquarius','Libra','Aries','Aries','Leo','Scorpio',
          'Aquarius','Gemini']

birthday = ['April 27, 1998','27 June 1991','1 January, 1997','January 12, 1998','18 January 1998','May 10, 1997',
            'April 6, 1998','June 24, 2000','February 12, 1988','August 31, 1992','March 9, 1995','January 31, 2000',
            'August 22, 1997','April 6, 1998','October 16, 1986','May 20, 1992','May 6, 1994','December 24, 1998',
            'February 14, 1988','October 5, 1998','April 9, 1996','April 12, 1994','August 13, 1994','October 28, 1991',
            'February 15, 1988','May 24, 1994']

age = ['24','31','24','24','24','25','24','22','34','29','27','22','25','24','35','30','28','23','34','23','26','28','28','30','34','28']

height = ['6 feet 1 inch','In Centimeters: 187 cm.','In Meters: 1.87 m.','In Feet Inches: 6 feet 2 inches','5′ 9″ ',
          '6 Feet 2 Inch','1.75 m (5 ft 9 in)','1.83 m','1.75 m','1.84 m''1.84 m','1.72 m','1.73 m','1.70 m','1.74 m',
          '1.70 m','1.89 m','1.89 m','1.91 m','1.74 m','1.78m','1.77m','1.77 m','1.85 m','1.88 m','1.72 m','1.83 m','1.78 m']

weight = ['78 kg','75 kg','70 kg','78Kg','77kg','75 kg.','70 kg','75 kg','80 kg','65 kg','74 kg','71 kg','79 kg','77 kg',
          '85 kg','84 kg.','93 kg','72 kg','75kg','67 kg','70 kg','80 kg','76 kg','72 kg.','72 kg.','68 kg.']

eye_color = ['Black','Black','Black','Brown','Brown','Black','Black','Black','Dark Brown','Brown', 'Black', 'Brown',
             'Dark Brown','Brown','Black','dark brown','black','Brown','dark brown','dark brown','blue','Black','Dark Brown',
             'Black',  'Black','Light Brown.']

hair_color = ['Black','Black','Brown','Brown','Black','Brown','Black','Brown','Black','Black', 'Brown','Brown','Dark Brown',
              'Black','Brown','Black','Brown','Light Brown','Black','Black','Dark Brown','Black','Black','Black','Black','Black']

marital_status = ['Married','Engaged','Single','Married','In a relationship','In a relationship ','Single','In a relationship ',
                  'Married','Married', 'In a relationship','Single','In a relationship','Married','Married', 'Married',
                  'Married', 'In a relationship', 'Married', 'In a relationship','In a relationship','Single','In a relationship',
                  'Married','Married','In a relationship']

affairs = ['Karen Cavaller','Agustina Bascerano','Not Found','Ariana Alonso','Muri Lopez Benitez','Valentina Pavlovsky',
           'Under Review','Sara Scaperrotta','Michele','Carolina Calvagni','Sabrina Di Marzo','Under Review','Agustina Gandolfo',
           'Kelsey Crane','Daniela Rendón','Rocio Suarez','Daniela Rendón','Cami Mayan','Jorgelina Cardoso','Sol Pérez','Magui Alcacer',
           'Under Review','Desirée Cordero Ferrer','Julia Silva','Linda Raff','Camila Homs']

father = ['Quito','Miguel Pezzella','Not Found','Not Found','Not Found','Ricardo Senesi','Will be updated soon',
          'Will be updated soon','Hernan Otamendi','Will be updated soon','Ángel Correa','Gustavo Álvarez','Karina Vanesa Gutiérrez',
          'John Gonzalez','Will be updated soon','Omar Rulli','Will be updated soon','Carlos Mac Allister','Miguel Di María',
          'Will be updated soon','Juan Pere Lo Celso','Will be updated soon','Will be updated soon','Will be updated soon',
          'Juan Manuel Gomez Fernandez','Roberto De Paul']

mother= ['Rosa','Not Found','Not Available','Not Found','Not Found','Will be updated soon','Will be updated soon',
         'Will be updated soon','Silvia Otamendi','Will be updated soon','Marcela Martínez','Will update','Mario Martínez',
         'Sylvia Mosier','Analia Rimoldi','Adriana García','Will be updated soon','Silvina Riela','Diana Hernández',
         'Will be updated soon','Sandra Lo Celso','Will be updated soon','Will be updated soon','Sara del Prado','Will be updated soon',
         'Monica De Paul']

siblings = ['Aldana','Bruno Pezzella','Not Known','Not Known','Not Known','Will be updated soon','Will be updated soon',
            'Will be updated soon','Will be updated soon','Will be updated soon','Luis Martínez','Raphael Alvarez','Jano Martínez,',
            'Alan Martínez','John Joseph Gonzalez','Will be updated soon','Will be updated soon','Will be updated soon',
            'Francis and Kevin','Evelyn Di María Hernández,Vanesa Di María Hernández','Will be updated soon','Will be updated soon',
            'Will be updated soon','Will be updated soon','Will be updated soon','Will be updated soon','Damian De Paul, Guido De Paul']

school = ['Not Found','Yet to update','Updated Soon','Updated Soon','Updated Soon','Will be updated soon','Will be updated soon',
          'Will be updated soon', 'Will be updated soon','Will be updated soon','Will be updated soon','Will be updated soon',
          'Will update','Will be updated soon','Will be updated soon','Will be updated soon','Will be updated soon','Will be updated soon',
          'Will be updated soon','Will be updated soon','Will be updated soon','Will be updated soon','Will be updated soon',
          'Will be updated soon','Will be updated soon','Will be updated soon']

college = ['Not Found','Yet to update','Not Found','Yet to update','Yet to update','Will be updated soon','Will be updated soon',
           'Will be updated soon','Will be updated soon','Will be updated soon','Will be updated soon','Will be updated soon',
           'Will be updated soon','Will be updated soon','Will be updated soon','Will be updated soon','Will be updated soon',
           'Will be updated soon','Will be updated soon','Will be updated soon','Will be updated soon','Will be updated soon',
           'Will be updated soon','Will be updated soon','Will be updated soon','Will be updated soon']

eduacational_qualification = ['Updated soon','Not Known','Not Known','Updated soon','Updated soon','Will be updated soon',
                              'Will be updated soon','Will be updated soon','Will be updated soon','Will be updated soon',
                              'Will be updated soon','Will be updated soon','Will be updated soon','Will be updated soon',
                              'Will be updated soon','Will be updated soon','Will be updated soon','Will be updated soon',
                              'Will be updated soon','Will be updated soon','Will be updated soon','Will be updated soon',
                              'Will be updated soon','Will be updated soon','Will be updated soon','Will be updated soon']

debut = ['3 June 2021 in a World Cup qualifier against Chile','Against Nigeria in 2017','Against Venezuela on 22 March, 2019',
         'Nov 17, 2018 against Mexico','22 March 2019, against Venezuela','5 June 2022 against the Estonia national team.',
         '3 June 2021 in a World Cup qualifier against Chile','November 2019','In April 2009 against Panama','In Copa America 2021',
         'On 4 September 2015 against Bolivia','3 June 2021, in a World Cup qualifier against Chile','March 27, 2018',
         'Oct 13, 2019 against Ecuador','26 June 2018 against Nigeria','Against Guatemala on 8 September 2018',
         'on 26 March 2019 in a friendly against Morocco','on 30 October 2016 against Central Córdoba','On 6 September 2008, against Paraguay.',
         '8 September 2018, against the Guatemala national football team','On 11 November 2017, against Russia','On 9 June 2017, against Brazil',
         'On 9 June 2017, against Brazil','On 15 November 2016, against Colombia','Against Singapore in 2017','Against Iraq on 11 October 2018']

known_for = ['International football player','International football player','International football player','International football player',
             'International football player','International football player','International football player','International football player',
             'International football player','International football player','International football player','International football player',
             'International football player','International football player','International football player','International football player',
             'International football player','International football player','International football player','International football player',
             'International football player','International football player','International football player','International football player',
             'International football player','International football player',]

position = ['Defender','Defender','Defender','Defender','Defender','Defender','Defender','Defender','Defender','Defender',
            'Forward','Forward','Forward','Forward','Goalkeeper','Goalkeeper','Goalkeeper','Midfielder','Midfielder','Midfielder',
            'Midfielder','Midfielder','Midfielder','Defender','Midfielder','Midfielder']

jersey = ['13','16','2','8','21','4','26','2','19','3','21','27','22','15','1','1','28','10','11','14','20','18','16','8','24','7']

current_club = ['Tottenham Hotspur','Real Betis','Sevilla','Villarreal','Manchester United','Feyenoord','Udinese','Atletico Madrid',
                'Benfica','Ajax','Atlético Madrid','Manchester City','Inter Milan','Fiorentina','River Plate','Villarreal',
                'Atalanta','Brighton & Hove Albion','Juventus','Bayer Leverkusen','Tottenham Hotspur','Betis','Inter Milan',
                'Sevilla','Sevilla','Atlético Madrid']

ex_club = ['Atletico Belgrano','Olimpo, River Plate,  Fiorentina','River Plate','Not Available','Club Urquiza,','Club Libertad,',
           'Newell\'s Old Boys, Ajax','San Lorenzo','Rosario Central','Udinese','Manchester City','Independiente','San Lorenzo',
           'River Plate','Racing Club','VfB Stuttgart','Atlético Nacional','Montpellier','Udinese','Boca Juniors','Paris Saint-Germain',
           'River Plate','Villarreal','América','Lazio','Sporting CP','Atalanta','Udinese']

net_worth = ['$5 million','$5-10M','$5-10M','$2 million','$2 million','$1M', '$1.5 Million', '$1-5 Million','$12 Million',
             '5 Million Euro','27 Million Euro','$2 million','$5 million','$2.75 million','$2 million','$1.5 Million',
             '$3 Million - $4 Million','$1.5 Million','$18 million','22.5 Million Euro','50 Million Euro',
             '$1 million – $7 million dollars','7 Million Euro','$1.5 Million','$2 million','$2 million']

controversy = ['Not found','Not found','Not Available','Not Available','Not Known','Not Known','Not Known','Not Known',
               'Not Known','Not Known','Not Known','Not Known','Not Known','Not Known','Not Known','Not Known','Not Known',
               'Not Known','Not Known','Not Known','Not Known','Not Known','Not Known''Not Known','Not Known'
               'Camila Homs and Rodrigo De Paul are going through one of the worst moments of their relationship due to the millionaire lawsuit']

social_media = ['Twitter: https://twitter.com/cutiromero2?lang=en   Instagram: https://www.instagram.com/cutiromero2/?hl=en',
'Instagram: https://www.instagram.com/germanpezzella/  twitter: https://twitter.com/Gpezze',
'Instagram: https://www.instagram.com/gonzalo_montiel29/?hl=en     Twitter: https://twitter.com/gonzamontiel29?lang=en',
'Not Available',
'Instagram: https://www.instagram.com/lisandromartinezzz/?hl=en  Twitter: https://twitter.com/lisandrmartinez',
'Twitter: https://twitter.com/senesimarcos?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor   Instagram: https://www.instagram.com/marcosenesi/?hl=en',

'Instagram: https://www.instagram.com/nehuen.perez/?hl=en   Twitter: https://twitter.com/nehuenperezz',
'Instagram: https://www.instagram.com/nicolasotamendi30       Twitter: https://twitter.com/Notamendi30',
'Twitter: https://twitter.com/nico_taglia  Instagram: https://www.instagram.com/tagliafico3/',
'Instagram: https://www.instagram.com/angelcorrea32/?hl=en   Twiter: https://twitter.com/angelcorrea32',
'Twitter: https://twitter.com/julianalvarezfc?lang=en  Instagram: https://www.instagram.com/juliaanalvarez/?hl=en',
'Twitter: https://twitter.com/lmartinez10_?lang=en  Instagram: https://www.instagram.com/lautaromartinez/?hl=en',
'Instagram: https://www.instagram.com/nicoigonzalez/?hl=en  Twitter: https://twitter.com/NicoSGonzalez',
'Instagram: https://www.instagram.com/francoarmani34/   Twitter: https://twitter.com/francoarman1?lang=en',
'Instagram: https://www.instagram.com/gerorulli/?hl=en  Twitter: https://twitter.com/gerorulli?lang=en',
'Instagram: https://www.instagram.com/juanmusso/?hl=en   Twitter: https://twitter.com/musso_juan?lang=en',
'Twitter: https://twitter.com/alemacallister?lang=en  Instagram: https://www.instagram.com/alemacallister/?hl=en',
'Twitter: https://twitter.com/oficial7dimaria?lang=en Instagram: https://www.instagram.com/angeldimariajm/?hl=en',
'Twitter: https://twitter.com/exepalacios_?lang=en Instagram: https://www.instagram.com/exepalaciosok/?hl=en',
'Twitter: https://twitter.com/locelsogiovani  Instagram: https://www.instagram.com/locelsogiovani/?hl=en',
'Instagram: https://www.instagram.com/guiido_rodriguez/?hl=en  Twitter: https://twitter.com/guido_rodriguez?lang=en',
'Instagram|: https://www.instagram.com/tucucorrea/?hl=en  Twitter: https://twitter.com/tucu_correa?lang=en',
'Twitter: https://twitter.com/acunamarcos17?lang=en  Instagram: https://www.instagram.com/marcos.acuna10/?hl=en',
'Twitter: https://twitter.com/alejo_g11  Instagram: https://www.instagram.com/alejandrog44/?hl=en',
'Twitter: https://twitter.com/rodridepaul?lang=en  Instagram: https://www.instagram.com/rodridepaul/?hl=en']

i = 0
while i > len(name):

    name = name[i]
    country = country[i]
    profession = profession[i]
    nickname = nickname[i]
    birthplace = birthplace[i]
    citizen = citizen[i]
    hometown = hometown[i]
    religion = religion[i]
    zodiac = zodiac[i]
    birthday = zodiac[i]
    age = age[i]
    height = height[i]
    weight = weight[i]
    eye_color = eye_color[i]
    hair_color = hair_color[i]
    marital_status = marital_status[i]
    affairs = affairs[i]
    father = father[i]
    mother = mother[i]
    siblings = siblings[i]
    school = school[i]
    college = college[i]
    eduacational_qualification = eduacational_qualification[i]
    debut = debut[i]
    known_for = known_for[i]
    position = position[i]
    jersey = jersey[i]
    current_club = current_club[i]
    ex_club = ex_club[i]
    net_worth = net_worth[i]
    controversy = controversy[i]
    social_media = social_media[i]

    #Introduction

    sentence_one = [
        f'{name} is an established football player who plays for {current_club} and the {country} national football team.',
        f'{name} is a well-known football player who competes for {current_club} and the {country} squad.',
        f'{name} is a seasoned pro football player who competes for {current_club} and the {country} squad.',
        f'Footballer {name} is a seasoned professional player who competes for {current_club} and {country}.',
        f'{name} is a leading footballer who now plays for {country} national team and {current_club}.',
        f'Extraordinary football player {name} plays for {current_club} and {country} National football team',
    ]

    sentence_two = [
        f'He is famous for his incredible footballing skills and abilities.',
        f'He is well-known for his exceptional football talents and abilities.',
        f'He is renowned for his extraordinary footballing skills.',
        f'He is well known for having amazing footballing ability.',
        f'He is renowned for his tremendous footballing talent.',
        f'His incredible football skills are highly renowned to everyone.',
        f'He has incredible football skills, which is highly renowned.',
        f'His outstanding football talent is well known to all.',
    ]

    sentence_three = [
        f'This article will show you all you need to know about {name} Net Worth, Salary, Age, Biography, Height, Weight, Career, Love life, and more.',
        f'Everything you need to know about Harry Maguire{name}, age, biography, height, weight, career, love life, and other details are included in this post.',
        f'Everything you need to know about {name}\'s net worth, salary, age, biography, height, weight, career, love life, and other factors are covered in this article.',
        f'This post will provide you every facts about {name} such as Age, Career, Net Worth, Salary, Biography, Physical info,  Love Life, and much more.',
        f'Through this article you will know everyting about {name} Biography, Net worth, Age, Salary, Career and more.',
        f'You will find everything about {name}\'s biography, net worth, age, salary, career, and more through this article.',
        f'You can discover everything about {name}\'s early life, including his biography, net worth, age, salary, and career, through this article.',
        f'{name}\'s age, salary, career, affairs biography, height, weight,, and other details are provided in this post.',
    ]

    sentence_four = [
        f'We hope this article is useful to everyone, especially those who don\'t know who he is.',
        f'Especially for those who don\'t know who he is, this article will be helpful to them.',
        f'We expect that this information are beneficial to everyone, to know about him.',
        f'This information will be useful to those who don\'t know who he is, especially.',
        f'This article will be beneficial to every readers, especially those who are unfamiliar with him.',
        f'Those who are unfamiliar with him, will get every information from here.',
        f'Those who are unknown with him will discover everything they need to know about {name}.',
        f'Those who are interested to know about him will find all essential data here.',
        f'Those who are courios to know about him will find all essential data here.',
    ]

    #Early Life & Biography
    sentence_five = [
        f'The real name of {name} is {name}.',
        f'{name} is {name}\'s actual name.',
        f'{name}\'s full name is {name}.',
        f'{name} is {name}\'s full name.',
        f'{name}\'s real name is {name}.',
        f'{name}\'s original name is {name}.',
        f'{name} is {name}\'s birth name.',
        f'{name} was {name}\'s original name.',
    ]

    sentence_six = [
        f'People and his relatives call him {nickname}.',
        f'His nickname is {nickname},',
        f'{nickname} is a nickname given to him by his friends and family.',
        f'{nickname} is his nick name.',
        f'He is also known as {nickname} as nickname.',
        f'He also calls by the name {nickname}.',
        f'{nickname} is another name for him.',
        f'Additionally, he also calls by the nickname {nickname}.',
    ]

    sentence_seven = [
        f'He came from a decent family.',
        f'He came from an aristocrate family.',
        f'He came from an elegant family.',
        f'He belongs to a decent family.',
        f'He belongs to an elegant family.',
        f'He comes from an gracious family',
        f'He comes from a gentle family.',
        f'He comes from a kind family.',
    ]

    sentence_eight = [
        f'{name} has grown up in {birthplace}.',
        f'{name} has raised up in {birthplace}.',
        f'In {birthplace}, {name} was raised.',
        f'{birthplace} is the birthplace of {name}.',
        f'{name} was born and grown up in {birthplace}.',
        f'{name} birthplace is {birthplace},',
    ]

    sentence_nine = [
        f'He has {citizen} citizenship and currently living in {birthplace}.',
        f'He currently resides in {birthplace}, and holds {citizen} citizenship.',
        f'He is a citizen of {country} and is presently residing in {birthplace}.',
        f'He has {citizen} nationality and presently stays in {birthplace}.',
        f'He presently lives in {birthplace}, and holds {citizen} citizenship.',
        f'He is a citizen of {country} and is presently staying in {birthplace}.',
        f'His present residence is {birthplace}, and he is an {citizen} citizen.',
    ]

    sentence_ten = [
        f'{name} follows {religion}.',
        f'{religion} is the religion of {name}.',
        f'{religion} is {name}\'s religion.',
        f'{religion} is the religion practiced by {name}.',
        f'He believes in {religion}.',
        f'He adheres to {religion}.',
        f'He is a devout {religion}.',
        f'He is believer of {religion}.',
    ]

    sentence_eleven = [
        f'This player\'s educational background is {eduacational_qualification}.',
        f'This player has a {eduacational_qualification} degree.',
        f'This player holds a {eduacational_qualification} degree.',
        f'This player has a {eduacational_qualification} level education.',
        f'This player has a {eduacational_qualification} education.',
        f'He is {eduacational_qualification} from an well known university.',
        f'He has completed his studies from university.',
    ]

    sentence_twelve = [
        f'Check out the area below for further information.',
        f'For more information, please see the section below.',
        f'For further information, see the section below.',
        f'More information will be found in the section below.',
        f'You can check the below information for more.',
        f'More information is available in the section below.',
        f'More data is provided in the section below.',
        f'More details can be found in the sections below.',
        f'Collect additional information from the below section.',
        f'To found additional information check the below section.',
    ]

    #Age and Birth

    sentence_thirteen = [
        f'What is the age of {name}?',
        f'When {name} was born?',
        f'What is {name}\'s age?',
        f'How old is {name}?',
        f'What is {name}\'s age?',
        f'What age is {name}?',
    ]

    sentence_fourteen = [
        f'The age, birthdate, and other essential details have been addressed here.',
        f'Here,age, birthday, and other necessary details have been covered.',
        'The age, birthdate, and other relevant details have been covered in this section.',
        f'This information includes the person\'s age, birthday, and other important facts.',
        f'The age, birthday, and other important data are provided here.',
        f'The age, birthday, and other important facts have been discussed here.',
        f'The age, birthdate, and other important information have been included in this section.',
        f'Age, date of birth and other important details have been mentioned here.',
    ]

    sentence_fifteen = [
        f'You may find a variety of birth-related facts in the table below also.',
        f'The table below contains a variety of birth-related information.',
        f'You can also find more birth-related information in the table below.',
        f'The table below includes a range of birth-related information.',
        f'A number of birth-related information may also be found in the table below.',
        f'The table below also includes a variety of birth-related data.',
        f'Additionally, the table below includes a number of birth-related information.',
    ]

    sentence_sixteen = [
        f'According to some sources, {name} was born on {birthday}.',
        f'{name} was born on {birthday}, according some sources.',
        f'Some sources claim that {name} was born on {birthday}.',
        f'In {birthday} he was born.',
        f'According to a few sources, {name} born on {birthday}.',
        f'On {birthday}, {name} was born.',
    ]

    sentence_seventeen = [
        f'The age of {name} is {age} old.',
        f'{name} is {age} old.',
        f'{name}\'s age is {age}.',
        f'{name} is a {age} old man.',
        f'He is {age} old.',
        f'{name} age is {age} old.',
        f'The age of {name} is {age}.',
        f'Currently, {name} is {age} old.',
    ]

    sentence_eighteen = [
        f'His birthplace is {birthplace}.',
        f'{birthplace} is the city of his birth.',
        f'{birthplace}, is where he was born.',
        f'{birthplace} is where he was born.',
        f'He was born in {birthplace}.',
        f'In {birthplace}, he was born.',
        f'In {birthplace}, he was born.',
    ]

    #Height, Weight

    sentence_nineteen = [
        f'Celebrities’ physical appearance always attracts their fans and followers.',
        f'The physical appearance of celebrities always draws the attention of their fans and followers.',
        f'The physical look of celebrities constantly attract fans and followers.',
        f'Fans and followers are always attracted to celebrities based on their physical appearance.',
        f'Fans and followers are strongly attracted bycelebrity\'s physical appearance.',
        f'Fans and followers are constantly interested in celebrities\'physical appearance.',
        f'Celebrity looks have always fascinated fans and followers.',
    ]

    sentence_twenty = [
        f'They love to know more about their favorite celebrity’s physical structure.',
        f'They are often curious in the physical appearance of their favorite celebrities.',
        f'They are fascinated by the details of the physical structure of their favorite celebrities.',
        f'They want to know more about the body structure of their favorite celebrity.',
        f'They want to know more about their favorite celebrity\'s body type.',
        f'They are curious in the physical structure of their favorite star.',
    ]

    sentence_twenty_one = [
        f'We are quite well aware of that.',
        f'We are fully aware about this.',
        f'That is something we are fully aware of.',
        f'We know that very well.',
        f'We are well aware of that.',
        f'That is known to us.',
        f'We know this very well.',
        f'We\'re quite aware of this.',
    ]

    sentence_twenty_two = [
        f'{name}\'s height is {height} and his weight is {weight}.',
        f'{name} is {height} tall and weight is {weight}.',
        f'{name} weight is {weight} and he is {height} tall.',
        f'{name} is {weight} and {height}.',
        f'{name} is approximately {weight} and {height} tall.',
        f'{name} weight is about {weight} and {height} tall.',
    ]

    sentence_twenty_three = [
        f'The weight can be updated at any moment; we have included the most recent figure below.',
        f'We have provided the most recent weight here, but it may change at any time.',
        f'The weight is possible to change at any time; the most current value is given here.',
        f'The weight may be changed at any time; the most current value is provided here.',
        f'Weights can be updated at any time. Here are the latest value.',
        f'Weights can be changed at any time; We\'ve included the most recent figure below.',
        f'Weight is possible to change at any time; the most recent number is displayed here.',
    ]

    sentence_twenty_four = [
        f'His eyes are {eye_color}, and his hair is {hair_color}.',
        f'His hair is {hair_color}, and his eyes are {eye_color}.',
        f'He has {hair_color} hair and {eye_color} eyes.',
        f'His {hair_color} hair contrasts with his {eye_color} eyes.',
        f'His has {hair_color} hair and {eye_color} eyes.',
        f'His eyes are {eye_color}, and he has {hair_color} hair.',
    ]

    sentence_twenty_five = [
        f'Check these also from the below section.',
        f'Check them out as well in the area below.',
        f'Check them out in the area below as well.',
        f'Check out these information from the area below.',
        f'Also check the next section.',
        f'Also check them out in the section below.',
        f'Additionally, look these in the section below.',
        f'Also have a look at the below information.',
    ]
    #Marital status, Love life

    sentence_twenty_six = [
        f'Who is {name} Dating and what is his marital condition?',
        f'What is {name}\'s marital status and who is he dating?',
        f'What is the marital status of {name} and who is he dating?',
        f'Here are {name}\'s  relationships as well as his current marital status.',
        f'Here you can view {name}\'s dating history and marital status.',
        f'Along with his marital status, {name}\'s dating history is shown here.',
        f'Here are {name}\'s dating history along with his current marital status.',
    ]

    sentence_twenty_seven = [
        f'People are becoming more interested in the love life and family info of celebrities.',
        f'More people are increasingly interested in the relationships and familial backgrounds of celebrities.',
        f'Celebrity families and their relationship histories are of increasing interest to the audience.',
        f'People are becoming more interested in the relationships and familial backgrounds of celebrities.',
        f' Everyone here is interested to know  about relationship and family info of celebrities.',
        f'People are interested in finding out about the relationships and families of famous people.',
        f'Everyone is curious about the relationships and families of well-known people.',
        f'Everyone is eager to find out more about the families and relationships of famous people.',
        f'About the families and relationships of famous people, everyone is interested.',
    ]

    sentence_twenty_eight = [
        f'This section is for you if you want to discover more about his family, personal life, and marital status.',
        f'If you want to know more about his family, personal life, and marital status, this section is for you.',
        f'You may find out more about his family, personal life, and marital status in this section.',
        f'If you want to get more about his family, personal life, and marital status, you should read this part.',
        f'If you want to read more about his family, personal life, and marital status, then this part is for you.',
        f'This section is where his family, personal life, and marital status are explained.',
        f'This section contains information about his family, personal life, and marital status.',
    ]

    sentence_twenty_nine = [
        f'To find out about this information, see the following table.',
        f'See the following table for further details on this information',
        f'Check out the table below for further details on this information.',
        f'See the following table for more details on this information.',
        f'View the following table to know more about this ',
        f'Check the following table to know more about this',
        f'See the table below to know more about this information',
        f'To know more about this information , see the table below.',
        f'For additional details, see the table below.',
    ]

    #Education Qualification

    sentence_thirty= [
        f'Everyone thinks that being a famous person is all about fame and fortune.',
        f'Everyone believes that fame and riches are the only two aspects of being famous.',
        f'People thinks that popularity and money are the only two aspects of being famous.',
        f'Everyone believes that being famous is all about riches and fame.',
        f'People believes that being famous is all about wealth and recognition.',
        f'Everybody believes that fame and wealth are the only two things involved in being famous.',
        f'People thinks that wealth and recognition are the only two factors involved in being famous.',
        f'People often think that fame is all about money and popularity.',
    ]

    sentence_thirty_one = [
        f'However, there’s more to it than that.',
        f'But it\'s more complicated than that.',
        f'It\'s however more complex than that.',
        f'There is more to it than that, though.',
        f'There is more to it than that, however.',
        f'It is far more complicated than that, though.',
        f'That is not all there is to it, though.',
        f'Although it\'s not the only part of it.',
    ]

    sentence_thirty_two = [
        f'To have success as a celebrity, must have a good educational background.',
        f'A strong educational foundation is necessary for success in the celebrity world.',
        f'A proper education foundation is essential for success in the entertainment industry.',
        f'Need a strong educational foundation in order to achieve success as a celebrity.',
        f'Need to have a solid academic foundation to succeed as a celebrity.',
        f'Need a good educational background in order to be successful as a celebrity.',
        f'Require a strong educational foundation to succeed as a superstar.',
        f'To succeed as a celebrity, everyone needs a strong educational foundation.',
    ]
    sentence_thirty_three = [
        f'Many people search for the academic background of their favorite celebrities. ',
        f'Many people look into the educational history of their favorite celebrities.',
        f'A lot of individuals look up the academic credentials of their favorite celebrities.',
        f'The academic history of their favorite celebrities is a popular topic of search.',
        f'Many individuals search up the academic credentials of their favorite stars.',
        f'A large number of people check the academic credentials of their favorite celebrities.',
        f'Many individuals look into the academic backgrounds of their favorite celebrities.',
        f'Several people look into the academic background of the superstars they admire.',
    ]

    sentence_thirty_four = [
        f'From here, you will know about {name} Education Qualification information.',
        f'You can read more about {name}\'s educational background from this page.',
        f'This page will inform you of {name}\'s academic qualifications.',
        f'The information of {name}\'s educational background will be gained from this.',
        f'This section will update viewers of {name}\'s educational qualifications.',
        f'The information regarding {name}\'s educational background is covered in this section.',
        f'{name} Education Qualification Information is presented in this section.',
    ]

    #Professional, Club Career

    sentence_thirty_five = [
        f'This section is full of information about {name} professional life.',
        f'There is a lot of information regarding {name}\'s work life in this section.',
        f'The professional life of {name} is fully covered in this section.',
        f'{name}\'s professional life is fully discussed in this section.'
        f'This section contains large amount of information about {name}\'s career path in this section.',
        f'Here is where {name}\'s work life is included.',
        f'{name}\'s professional life is included in here.',
    ]

    sentence_thirty_six = [
        f'Here we also mentioned his club career and controversies.',
        f'His club career and controversies have also been discussed here.',
        f'Also, we said something about his club career and controversy here.',
        f'His club history and controversies also are mentioned here.',
        f'His club history and controversies also are mentioned here.',
        f'In this section, we also discussed his club career and any relevant controversies.',
        f'We also analyzed his club career and controversies in this section.',
    ]

    sentence_thirty_seven = [
        f'He is known as a {known_for}.',
        f'He is well-known for playing football.',
        f'His reputation as a football player.',
        f'He is famous as a football player.',
        f'He is recognized as a football player.',
        f'His renown as a football player.',
        f'The fame of him as a football player.',
        f'The recognition of him as a football player.',
    ]

    sentence_thirty_eight = [
        f'{name} debuted for the national team on {debut}.',
        f'{name} made his national team debut on {debut}.',
        f'On {debut}, {name} made his national team debut.',
        f'Against {debut}, {name} made his national team debut.',
        f'On {debut}, {name} made his official debut for the national team.',
        f'In a game {debut}, {name} made his official debut for the national squad.',
    ]

    sentence_thirty_nine = [
        f'He plays in the {position} position.',
        f'He is a {position} on the team.',
        f'In his current position, he is a {position}.',
        f'He is now a {position}.',
        f'He is a {position} for both the national and club teams.',
        f'In both the national and club teams, he is a {position}.',
        f'Both for his country\'s and his club squad, he is a {position}.',
    ]

    sentence_fourty = [
        f'{name} jersey number is {jersey}.',
        f'{jersey} is {name}\'s jersey number.',
        f'{jersey} is the number on {name}\'s jersey.',
        f'The number on {name}\'s jersey is {jersey}.',
        f'He plays wearing the number {jersey} jersey.',
        f'He plays with the No. {jersey} jersey on.',
        f'He usually wears the number {jersey} jersey.',
        f'His uniform number is {jersey}; he always wears it.',
    ]

    sentence_fourty_one = [
        f'Previously {name} was playing for {ex_club}.',
        f'{name} previously played for {ex_club}.',
        f'{name} previously represented {ex_club} as a player.',
        f'For {ex_club} in the past, {name} was a player.',
        f'{name} had previously been a player for {ex_club}.',
        f'His previous team was {ex_club}.',
        f'He used to play for {ex_club} team before.',
    ]

    sentence_fourty_two = [
        f'But currently, he is playing for {current_club}.',
        f'However, he is currently a member of {current_club} football team.',
        f'But, he is currently a part of {current_club}.',
        f'However, he presently represents {current_club}.',
        f'Although, he currently plays {current_club}.',
        f'However, he is now seen wearing {current_club}\'s jersey.',
        f'He is now playing while wearing a {current_club} jersey, though.',
        f'However, he is now seen playing in {current_club}\'s jersey.',
    ]

    #FIFA World Cup 2022 Squad

    sentence_fourty_three = [
        f'The FIFA World Cup is the biggest football tournament that takes place every four years.',
        f'The biggest football competition, the FIFA World Cup, occurs every four years.',
        f'The largest football competition, which occurs every four years, is the FIFA World Cup.',
        f'Every four years, the FIFA World Cup, which is the largest football competition, is held.',
        f'FIFA World Cup is the biggest football tournament which is held every four years.',
        f'The FIFA World Cup is the biggest football competition and it occurs every four years.',
        f'Every four years, the FIFA World Cup, the largest football competition, is held.',
    ]

    sentence_fourty_four = [
        f'The next edition of the World Cup will be held in 2022, and it will be jointly hosted by two nations Qatar and UAE.',
        f'The UAE and Qatar will co-host the 2022 World Cup, which will be the tournament\'s next edition.',
        f'The host nations for the 2022 World Cup will be the two countries of Qatar and the United Arab Emirates.',
        f'Qatar and the United Arab Emirates will co-host the 2022 World Cup.',
        f'The 2022 World Cup will be co-hosted by Qatar and the United Arab Emirates.',
        f'The next World Cup will actually occur in 2022, and Qatar and the UAE will host it together.',
        f'The next World Cup will occur in 2022, and Qatar and the United Arab Emirates will co-host.',
    ]

    sentence_fourty_five = [
        f'However, you will be happy to know that you will see {name} in FIFA World Cup 2022.',
        f'You\'ll be pleased to hear that {name} will appear at the FIFA World Cup in 2022.',
        f'You\'ll be glad to know that {name} will play in the FIFA World Cup 2022.',
        f'The good news is that {name} will appear in the FIFA World Cup 2022, which will make you happy.',
        f'However, you can delight in the knowing that {name} will appear in the FIFA World Cup 2022.',
        f'You\'ll be relieved to hear that {name} will be wearing his nation\'s jersey and competing in the FIFA World Cup in 2022.',
        f'You\'ll be glad to know that {name} will play for his nation at the FIFA World Cup in 2022.',
    ]

    sentence_fourty_six = [
        f'{country} coach just announced a probable squad for the world cup and {name} has got a chance to represent his country on it.',
        f'{name} has a chance to represent his country on the {country} team, which was officially announced by {country} Coach.',
        f'The World Cup probable team for {country}, which was just announced, includes {name}, who could play for his country.',
        f'The {country} coach\'s World Cup probable squad was been announced, and {name} may be chosen to stand for his country.',
        f'{name} has the possibility of representing his nation on the {country} coach\'s selected  probable squad for World Cup , which was just released.',
        f'{name} might play for his country in the World Cup contingent selected by {country}\'s head coach, which was just made public.',
    ]

    #Net Worth and Salaries

    sentence_fourty_seven = [
        f'Many Football players are known for their high salaries paid by many clubs.',
        f'Many football clubs are known for paying their players huge salaries.',
        f'The enormous wages received by many clubs from many football players are well-known.',
        f'Football players are well recognized for receiving large salaries from numerous clubs.',
        f'Football players are well-known for receiving large pay from numerous clubs.',
        f'Footballers are well-known for earning huge salaries from several clubs.',
        f'Football players are renowned for earning significant salaries from numerous clubs.',
    ]

    sentence_fourty_eight = [
        f'So, everyone thinks that their net worth must be huge.',
        f'Therefore, everyone assumes that they must have a huge net worth.',
        f'people assume that they must have a very large net worth.',
        f'They consequently believes that they must have a very massive net worth.',
        f'people assume that they have much money.',
        f'Everyone believes that they must have a massive net worth.',
        f'Everyone consequently thinks that they must have a significant net worth.',
    ]

    sentence_fourty_nine = [
        f'If you want to know {name} net worth and salary information, this section is for you.',
        f'This section is for you if you\'re seeking information about {name}\'s net worth and salary data.',
        f'This section is for you if you want to know about {name}\'s earnings and net worth.',
        f'This part is designed for you if you\'re curious about {name}\'s earnings and net worth.',
        f'if you want to read about {name}\'s earnings and net worth, This section is there for you.',
        f'You can read about {name}\'s earnings and net worth in this section.',
        f'You should read this section to know more about {name}\'s earnings and net worth.',
    ]
    sentence_fifty = [
        f'The table below contains the most recent data on salary and assets.',
        f'The most recent information on income and wealth is shown in the table below.',
        f'The most recent details on wages and property is displayed in the table below.',
        f'Most latest information on earnings and assets are presented in the tables below.',
        f'One of most updated information on earnings and property is available in the table below.',
        f'The table below shows the most current information on earnings and property.',
        f'In the table below, you can find the most recent data on wages and property.',
    ]

    sentence_fifty_one = [
        f'It should be noted that both net worth and salaries change with time',
        f'It should be remembered that salaries and net worth fluctuate over time.',
        f'It should be noted that wages and net assets fluctuate over time.',
        f'Note that both net worth and salary fluctuate over time.',
        f'Both net worth and earnings fluctuate over time, it is necessary to noted.',
        f'Remember that both earnings and salary shift over time.',
        f'Keep in mind that salaries and earnings fluctuate as time passes.',
        f'Do not forget that both earnings and compensation fluctuate over time.',
    ]

    sentence_fifty_two = [
        f'{name} net worth is approximately {net_worth}.',
        f'{name} has a {net_worth} net worth.'
        f'The estimated {net_worth} net worth of {name}.',
        f'The approximated {net_worth} net worth of {name}.',
        f'{name} has a net worth of {name}.',
        f'An estimated {net_worth} is {name}\'s net worth.',
    ]

    #Social Media

    sentence_fifty_three = [
        f'In the last couple of years, social media has become a place for celebrities to connect with their fans and vice versa.',
        f'Social media has developed over the past several years into a platform for celebrities to interact with their fans and vice versa.',
        f'In recent years, social media has developed into a medium for celebrities to connect with their fans and vice versa.',
        f'Social media has evolved over the past several years into a platform for celebrities and their fans to engage.',
        f'In the recent times, social media has grown into a medium for celebrities to connect with their fans and vice versa.',
    ]

    sentence_fifty_four = [
        f'As a result, you can now follow your favorite celebrities on social media to get updates about their lives, new projects, and general goings-on',
        f'Consequently, you can now keep up with your favorite celebrities on social media to know about their lives, upcoming endeavors, and general happenings.',
        f'Therefore, you can now follow in touch with your favorite personalities on media platforms to know about their lives, upcoming endeavors, and general events.',
        f'As a result, you may now follow your favorite celebrities on social media to know about their life, upcoming endeavors, and other activities.',
    ]

    sentence_fifty_five = [
        f'Follow {name} on social media from here.',
        f'From here, you can follow {name} on social media.',
        f'Follow {name} from this page on social media.',
        f'Get social media accounts of {name} from here.',
        f'From this section, you can follow {name} on social media.',
        f'Find social media handles for {name} from below.',
    ]

    #FAQ

    sentence_fifty_six = [
        f'Quick Facts about {name}.',
        f'Frequently Asked Question.',
        f'FAQ.',
        f'Common Question.',
        f'Listed Question and Answers.',
        f'Commonly Asked Questions.',
        f'Frequent Questions.',
        f'Question and answer.',
        f'Most  Common  Questions.',
        f'Most  Commonly Asked Questions.',]

    sentence_fifty_seven = [
        f'How tall is {name}?',
        f'What is the height of {name}?',
        f'What is {name}\'s height?',
        f'{name}\'s height?',
        f'How much is {name}\'s height?',
    ]

    sentence_fifty_eight = [
        f'{name} is {height} tall.',
        f'The height of {name} {height}.',
        f'{name} height is {height}.',
        f'{name} approximately {height} tall.',
        f'{name} is around {height} tall.',
        f'{name} stands at {height}.',
    ]

    sentence_fifty_nine = [
        f'What is the age of {name}?',
        f'How old is {name}?',
        f'What is the age of {name} in [year]?',
        f'What is {name}\'s age?',
        f'What is the current age of {name}?',
    ]

    sentence_sixty = [
        f'{name} is {age} old.',
        f'The age of {name} is {age}.',
        f'The age of {name} in [year] is {age}.',
        f'The age of {name} is {age}.',
        f'{name}\'s current age is {age}.',
    ]

    sentence_sixty_one = [
        f'What is the net worth of {name}?',
        f'{name}\'s net worth?',
        f'{name} net worth in [year]?',
        f'{name}\'s current net worth?',
        f'What is {name}\s net worth?',
        f'How much money does {name} have?',
        f'What is {name}\'s estimated net worth?',
        f'What is {name}\'s approximate net worth?',
        f'What is {name}\'s current net worth?',
        f'What is {name}\'s total net worth?',
    ]

    sentence_sixty_two = [
        f'{name} net worth is {net_worth} as of [year].',
        f'{name} net worth is {net_worth}.',
        f'{name} estimated net worth is {net_worth} as of [year].',
        f'{name} current net worth is {net_worth}.',
        f'{name} approximate net worth is {net_worth}.',
        f'{name} total net worth is {net_worth}.',
        f'{name} has {net_worth}.',
        f'The property of {name} is {net_worth}.',
        f'{name} has a net worth of {net_worth}.',
        f'{name} has a net worth of {net_worth} dollars.',
    ]

    sentence_sixty_three = [
        f'Is {name} married?',
        f'Does {name} have a wife?',
        f'Does {name} have affairs?',
        f'{name} has a wife?',
        f'Is {name} currently married?',
    ]

    sentence_sixty_four = [
        f'{name} is {marital_status}.',
        f'{name} is {marital_status}.',
        f'{name} has a {marital_status}.',
        f'{name} is currently {marital_status}.',
    ]

    sentence_sixty_five = [
        f'What is the jersey number of {name}?',
        f'{name}\'s jersey number?',
        f'What is {name}\'s jersey number?',
        f'What number does {name} wear on his jersey?',
        f'What\'s {name}\'s jersey number?',
    ]

    sentence_sixty_six = [
        f'His jersey number is {jersey}.',
        f'{name}\'s jersey number is {jersey}.',
        f'{name}\'s current jersey number is {jersey}.',
        f'The jersey number of {name} is {jersey}.',
        f'The jersey number for {name} is {jersey}.',
    ]

    sentence_sixty_seven = [
        f'What is the current club’s name of {name}?',
        f'{name}\'s current club name?',
        f'What is the name of {name}\'s current club?',
        f'Which club does {name} currently belong to?',
        f'Which club does {name} currently playing for?',
        f'What\'s the name of {name}\'s current club?',
        f'What is {name}\'s current club\s name?',
    ]

    sentence_sixty_eight = [
        f'His current club’s name is {current_club}.',
        f'{name}\'s current club’s name is {current_club}.',
        f'{name} currently playing for {current_club}.',
        f'{current_club} is the name of his current club.',
        f'{current_club} is his current club.',
        f'{current_club} is his current club\'s name.',
        f'{current_club} is the name of his current team.',
        f'The name of his current team is {current_club}.',
        f'{current_club} is the name of his present team.',
    ]

    sentence_sixty_nine = [
        f'Is {name} selected for {country} FIFA [year] World Cup Squad?',
        f'Is {name} selected for FIFA World cup?',
        f'Is {name} selected for FIFA World cup [year]?',
        f'Has {name} been selected for the {country} World Cup team?',
        f'Is {name} included in the {country} World Cup lineup?',
        f'Will {country}\'s FIFA World Cup team include {name}?',
        f'Is {name} chosen for the {country} World Cup team?',
    ]

    sentence_seventy = [
        f'Yes, {name} has been selected for {country} FIFA [year] World Cup Squad.',
        f'{name} as actually been selected for the {country} World Cup team.',
        f'Yes, {name} was chosen for the {country} World Cup team.',
        f'The {country} FIFA World Cup team has already picked {name}.',
        f'{name} has been named to {country}\'s FIFA World Cup squad.',
        f'Yes, {name} has been named to {country}\'s FIFA World Cup squad.',
        f'Yes, {country}\'s FIFA World Cup squad includes {name}.',
    ]

    #Conclusion

    sentence_seventy_one = [
        f'That is everything that you need to know about {name}\'s salary, net worth, age, biography, height, and love life.',
        f'That concludes our discussion about {name}\'s earnings, age, biography, height, weight, career, and love life.',
        f'All of {name}\'s relevant information, including his salary, age, height, weight, biography, career, and love life, is listed below.',
        f'We predict that you get a clear idea about {name}\'s earnings, height, age, biography, weight, career, and affairs.',
        f'This is all about {name}\'s net worth, salary, age, biography, height, weight, career and affair.',
        f'That’s all regarding {name} Salary, Net worth, Age, Biography, Height, Weight, Career, and marital life.',
        f'All of this relates to {name}\'s earnings, age, biography, height, weight, profession, and relationships.',
    ]

    sentence_seventy_two = [
        f'Hope the above information helps you to know about him.',
        f'We hope that above information assists you to know about him.',
        f'We hope the above information helps you learn more about him.',
        f'We hope the details above will give you a better understanding about him.',
        f'You may discover more about him by reading the information above.',
        f'Through the above information, we try to give you a piece of knowledge about his bio.',
        f'Through the information above, we are trying to give you some knowledge about his biography.',
        f'We\'ve tried to provide you some information about his life through the information above.',
    ]

    sentence_seventy_three = [
        f'If you find anything wrong or want to add your favorite celebrities to our list, you can share your opinion through the comments form.',
        f'You can express your thoughts using the comments box if there is anything you think is incorrect or if you want to add any other celebrities to our list.',
        f'Please use the comments section to let us know if there is anything you think is incorrect or if you would want to add any other celebs bio to our list.',
        f'If you observe any errors or wish to add your favorite celebs to our list, please share your thoughts in the comments section.',
        f'If you notice any errors or wish to add your favorite celebs to our list, please let us know in the comments section.',
        f'If you want to add your favorite star bio into our list let us know through comment section also you can share your opinion with us.',
        f'Please let us know if you find any incorrect or want to add your favorite celebrities to our list in the comments area.',
        f'If you find any inaccuracy or want to add your favorite celebrities to our list, please let us know in the comment box.',
        f'If you find any wrong information or want to add your favorite celebrities to our list, please let us know in the comment box.',
    ]

    sentence_one = random.choice(sentence_one)
    sentence_two = random.choice(sentence_two)
    sentence_three = random.choice(sentence_three)
    sentence_four = random.choice(sentence_four)
    sentence_five = random.choice(sentence_five)
    sentence_six = random.choice(sentence_six)
    sentence_seven = random.choice(sentence_seven)
    sentence_eight = random.choice(sentence_eight)
    sentence_nine = random.choice(sentence_nine)
    sentence_ten = random.choice(sentence_ten)
    sentence_eleven = random.choice(sentence_eleven)
    sentence_twelve = random.choice(sentence_twelve)
    sentence_thirteen = random.choice(sentence_thirteen)
    sentence_fourteen = random.choice(sentence_fourteen)
    sentence_fifteen = random.choice(sentence_fifteen)
    sentence_sixteen = random.choice(sentence_sixteen)
    sentence_seventeen = random.choice(sentence_seventeen)
    sentence_eighteen = random.choice(sentence_eighteen)
    sentence_nineteen = random.choice(sentence_nineteen)
    sentence_twenty = random.choice(sentence_twenty)
    sentence_twenty_one = random.choice(sentence_twenty_one)
    sentence_twenty_two = random.choice(sentence_twenty_two)
    sentence_twenty_three = random.choice(sentence_twenty_three)
    sentence_twenty_four = random.choice(sentence_twenty_four)
    sentence_twenty_five = random.choice(sentence_twenty_five)
    sentence_twenty_six = random.choice(sentence_twenty_six)
    sentence_twenty_seven = random.choice(sentence_twenty_seven)
    sentence_twenty_eight = random.choice(sentence_twenty_eight)
    sentence_twenty_nine = random.choice(sentence_twenty_nine)
    sentence_thirty = random.choice(sentence_thirty)
    sentence_thirty_one = random.choice(sentence_thirty_one)
    sentence_thirty_two = random.choice(sentence_thirty_two)
    sentence_thirty_three = random.choice(sentence_thirty_three)
    sentence_thirty_four = random.choice(sentence_thirty_four)
    sentence_thirty_five = random.choice(sentence_thirty_five)
    sentence_thirty_six = random.choice(sentence_thirty_six)
    sentence_thirty_seven = random.choice(sentence_thirty_seven)
    sentence_thirty_eight = random.choice(sentence_thirty_eight)
    sentence_thirty_nine = random.choice(sentence_thirty_nine)
    sentence_fourty = random.choice(sentence_fourty)
    sentence_fourty_one = random.choice(sentence_fourty_one)
    sentence_fourty_two = random.choice(sentence_fourty_two)
    sentence_fourty_three = random.choice(sentence_fourty_three)
    sentence_fourty_four = random.choice(sentence_fourty_four)
    sentence_fourty_five = random.choice(sentence_fourty_five)
    sentence_fourty_six = random.choice(sentence_fourty_six)
    sentence_fourty_seven = random.choice(sentence_fourty_seven)
    sentence_fourty_eight = random.choice(sentence_fourty_eight)
    sentence_fourty_nine = random.choice(sentence_fourty_nine)
    sentence_fifty = random.choice(sentence_fifty)
    sentence_fifty_one = random.choice(sentence_fifty_one)
    sentence_fifty_two = random.choice(sentence_fifty_two)
    sentence_fifty_three = random.choice(sentence_fifty_three)
    sentence_fifty_four = random.choice(sentence_fifty_four)
    sentence_fifty_five = random.choice(sentence_fifty_five)
    sentence_fifty_six = random.choice(sentence_fifty_six)
    sentence_fifty_seven = random.choice(sentence_fifty_seven)
    sentence_fifty_eight = random.choice(sentence_fifty_eight)
    sentence_fifty_nine = random.choice(sentence_fifty_nine)
    sentence_sixty = random.choice(sentence_sixty)
    sentence_sixty_one = random.choice(sentence_sixty_one)
    sentence_sixty_two = random.choice(sentence_sixty_two)
    sentence_sixty_three = random.choice(sentence_sixty_three)
    sentence_sixty_four = random.choice(sentence_sixty_four)
    sentence_sixty_five = random.choice(sentence_sixty_five)
    sentence_sixty_six = random.choice(sentence_sixty_six)
    sentence_sixty_seven = random.choice(sentence_sixty_seven)
    sentence_sixty_eight = random.choice(sentence_sixty_eight)
    sentence_sixty_nine = random.choice(sentence_sixty_nine)
    sentence_seventy = random.choice(sentence_seventy)
    sentence_seventy_one = random.choice(sentence_seventy_one)
    sentence_seventy_two = random.choice(sentence_seventy_two)
    sentence_seventy_three = random.choice(sentence_seventy_three)

    print(sentence_one,sentence_two,sentence_three,sentence_four,sentence_five,sentence_six,sentence_seven,sentence_eight,
          sentence_nine,sentence_ten,sentence_eleven,sentence_twelve,sentence_thirteen,sentence_fourteen,sentence_fifteen,
          sentence_sixteen,sentence_seventeen,sentence_eighteen,sentence_nineteen,sentence_twenty,sentence_twenty_one,
          sentence_twenty_two,sentence_twenty_three,sentence_twenty_four,sentence_twenty_five,sentence_twenty_six,sentence_twenty_seven,
          sentence_twenty_eight,sentence_twenty_nine,sentence_thirty,sentence_thirty_one,sentence_thirty_two,sentence_thirty_three,
          sentence_thirty_four,sentence_thirty_five,sentence_thirty_six,sentence_thirty_seven,sentence_thirty_eight,sentence_thirty_nine,
          sentence_fourty,sentence_fourty_one,sentence_fourty_two,sentence_fourty_three,sentence_fourty_four,sentence_fourty_five,
          sentence_fourty_six,sentence_fourty_seven,sentence_fourty_eight,sentence_fourty_nine,sentence_fifty,sentence_fifty_one,
          sentence_fifty_two,sentence_fifty_three,sentence_fifty_four,sentence_fifty_five,sentence_fifty_six,sentence_fifty_seven,
          sentence_fifty_eight,sentence_fifty_nine,sentence_sixty,sentence_sixty_one,sentence_sixty_two,sentence_sixty_three,
          sentence_sixty_four,sentence_sixty_five,sentence_sixty_six,sentence_sixty_seven,sentence_sixty_eight,sentence_sixty_nine,
          sentence_seventy,sentence_seventy_one,sentence_seventy_two,sentence_seventy_three)
    i +=1