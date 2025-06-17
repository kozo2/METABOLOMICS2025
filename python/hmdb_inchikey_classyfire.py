from bs4 import BeautifulSoup

with open("hmdb_metabolites.xml", 'r', encoding='utf-8') as file:
    content = file.read()

soup = BeautifulSoup(content, 'xml')
mall = soup.find_all('metabolite')

df = pd.DataFrame(columns = ["accession", "inchikey", "kingdom", "super_class", "class"])

for m in mall:
    ac = m.find('accession').get_text().strip()
    ikey = m.find('inchikey').get_text().strip()

    kd = m.find('taxonomy').find('kingdom')
    sc = m.find('taxonomy').find('super_class')
    clss = m.find('taxonomy').find('class')

    if kd is None:
        kd = ""
    else:
        kd = kd.get_text().strip()
    if sc is None:
        sc = ""
    else:
        sc = sc.get_text().strip()
    if clss is None:
        clss = ""
    else:
        clss = clss.get_text().strip()

    df.loc[len(df)] =[ac, ikey, kd, sc, clss]

df.to_pickle('hmdb_inchi_classyfire.pkl')
