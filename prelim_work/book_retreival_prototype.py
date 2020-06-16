import requests

r = requests.get('http://openlibrary.org/search.json',
                 params = {'q': 'The Bluest Eye'})

print(r.url)
print(r.json()['docs'][0]['cover_i'])

cover_id = r.json()['docs'][0]['cover_i']

print('The following URL should link to the cover art:')
print(f'https://covers.openlibrary.org/b/id/{cover_id}-L.jpg')
