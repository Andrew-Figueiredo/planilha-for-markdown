import pandas as pd

file_name = './hus.csv'

data = pd.read_csv(file_name)

data = data.drop('Work Item Type', axis=1)

table_md = data.to_markdown(index=False)

with open('tabela.md', 'w') as file:
    file.write(table_md)

print("Tabela Markdown salva com sucesso no arquivo 'tabela.md'")