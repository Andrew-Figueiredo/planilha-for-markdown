import pandas as pd

def to_mark(df):
    table_md = df.to_markdown(index=False)
    
    with open('tabela.md', 'w') as file:
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
    





if __name__ == "__main__":
    # nome do arquivo
    file_csv = './HUs.csv'
    data = pd.read_csv(file_csv)
    
    # Linhas abaixo realiaza tratamento especifico do arquivo que estou trabalhando
    data = data.drop('Work Item Type', axis=1)

    # Ajuste do index
    data = data.dropna().reset_index(drop=True)
    data.index += 1
    
    df_table = build_spreadsheet(data=data)
    
    df_table.to_excel('tabela.xlsx', index=False)
    df_table = df_table.drop('Nome HU', axis=1)
    data_mkd = to_mark(df_table)

    print('Planilha e Markdown GERADOS!!')