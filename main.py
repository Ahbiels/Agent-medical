import pandas as pd
import os

FOLDER_COVID = "./files/files_bronze/covid19"
FOLDER_MENTAL_HEALTH = "./files/files_bronze/mental-health"

files_covid = os.listdir(FOLDER_COVID)
files_mental_health = os.listdir(FOLDER_MENTAL_HEALTH)

covid_faq_dataframe = []
mental_health_faq_dataframe = []

#------------------------------------abre os datafremes e salva em uma lista-------------------------------------------

for file_csv in range(len(files_covid)):
    covid_faq_dataframe.append(pd.read_csv(f"{FOLDER_COVID}/{files_covid[file_csv]}",encoding='utf-8'))

for file_csv in range(len(files_mental_health)):
    mental_health_faq_dataframe.append(pd.read_csv(f"{FOLDER_MENTAL_HEALTH}/{files_mental_health[file_csv]}",encoding='utf-8'))

#------------------------------------Muda os nomes dos index do dataframe-------------------------------------------

covid_faq_dataframe[1] = covid_faq_dataframe[1][["context",'response']]
mental_health_faq_dataframe[1] = mental_health_faq_dataframe[1].loc[:, "Questions":"Answers"]

for dataframe in covid_faq_dataframe:
    columns = list(dataframe.columns)
    dataframe.rename(columns={columns[0]:"question",columns[1]:"answer"}, inplace = True)

for dataframe in mental_health_faq_dataframe:
    columns = list(dataframe.columns)
    dataframe.rename(columns={columns[0]:"question",columns[1]:"answer"}, inplace = True)

#------------------------------------Removendo espacos em branco descenessários-------------------------------------------
covid_faq_dataframe[0]["answer"] = covid_faq_dataframe[0]["answer"].str.replace(r'\s+', ' ', regex=True).str.strip()
print(covid_faq_dataframe[0])

#------------------------------------Salva os dataframes modificados-------------------------------------------

for file_csv in range(len(covid_faq_dataframe)):
    covid_faq_dataframe[file_csv].to_csv(f"./files/files_gold/covid_19/covid_19_{file_csv}.csv",index=False)

for file_csv in range(len(mental_health_faq_dataframe)):
    mental_health_faq_dataframe[file_csv].to_csv(f"./files/files_gold/mental-health/mentalhealth{file_csv}.csv",index=False)

# covid_faq_dataframe[0] = covid_faq_dataframe[0][['answer','question']]
# covid_faq_dataframe[1] = covid_faq_dataframe[1][['answer','question']]
# covid_faq_dataframe[2] = covid_faq_dataframe[2][['answer','question']]

