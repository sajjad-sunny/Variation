country_name = input('write down country name: ')
university_name = input('write down university name:' )
established_in = input('when it was established?')
address = input('write down address: ')
phone = input('write down phone: ')
website = input('write down website: ')
for_graduation_informatiaon = input('write down graduation information: ')
for_online_course = input('write down online course information: ')
global_ranking = input('write down global ranking: ')
print()
print(university_name)

introduction = f"""
The {university_name}, ranks {global_ranking} in the world. It was established in {established_in}.This university was
developed based on academic standing, employer reputation, faculty to the ratio of students, staff with PhD,
international research alliance, citations per publication, papers per professor, and online impact. Find a little more
from the below section.
"""
print(introduction)
print()
print('Short Summary')
templete = f"""

1. Country Name         : {country_name} 
2. University Name      : {university_name}
3. Address              : {address}
4. Phone                : {phone}
5. Website              : {website}
6. For Graduation Info  : {for_graduation_informatiaon}
7. For Online Course    : {for_online_course}
8. Global Ranking   `   : {global_ranking}
"""
print(templete)
print("Social Media Accounts To Follow")
Social_Media_Accounts = f"""
By following their social media accounts, you can know more about this graet university. Go through the links from the
below section.
Facebook	https://www.facebook.com/admisionenlauc
Instagram	https://www.instagram.com/admisionuc/
YouTube	    https://www.youtube.com/c/Admisi%C3%B3nUC
"""
print(Social_Media_Accounts)
print()
conclution = f"""
{university_name} has been individually toped based on their total rankings in the World’s Best Universities and was 
assessed based on its researchers and ratings from academics throughout the world. That’s all about this University in
{country_name}. For any queries, you can contact us through the comment section
"""
print(conclution)