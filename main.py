import pandas as pd

def csv2mark(file_csv):
    table_md = file_csv.to_markdown(index=False)
    
    with open('tabela.md', 'w') as file:
        file.write(table_md)
        
    return table_md

def user2devops_user():
    pass
# nome do arquivo
file_name = './HUs.csv'

data = pd.read_csv(file_name)
# Linhas abaixo realiaza tratamento especifico do arquivo que estou trabalhando
data = data.drop('Work Item Type', axis=1)
data = data.drop('Assigned To', axis=1)


data_mkd = csv2mark(data)

print("Tabela Markdown salva com sucesso no arquivo 'tabela.md'")
