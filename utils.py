import pandas as pd

def to_mark(df, nameFile):
    table_md = df.to_markdown(index=False)
    
    with open(nameFile, 'w') as file:
        file.write(table_md)
        
    return table_md

def user2devops_user(names_users: pd.Series):
    users_devops = []
    for name in names_users:
        users_devops.append('@<' + name.split(' ')[0] + ' ' + name.split(' ')[1] + '>')
    return users_devops

def build_spreadsheet(data):
    
    table = {
        'n': data.index,
        'HU':['#'+ str(id_card) for id_card in data['ID']],
        'Nome HU': data['Title'],
        'Tester': user2devops_user(data['Tester']),
        'N CTs': ['-' ]*len(data),
        'Qualidade HU/HT': ['-' ]*len(data),
        'DEV Testou': ['-' ]*len(data),
        'Entregue': ['-' ]*len(data),
        'OBS': ['-' ]*len(data)
    }
    return pd.DataFrame(table)
    
