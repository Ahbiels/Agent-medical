#!/bin/bash

# Configurando o uso da GCP localmente
gcloud auth login
gcloud projects list
gcloud config set project <PROJECT_ID>
gcloud config list

# Criando o cloud storage, habilitando o versionamento e copiando os arquivos para o storage
gsutil mb -l us -c standard -b on --pap enforced gs://faq-covid-19-dialogflow
gsutil versioning set on gs://faq-covid-19-dialogflow

gsutil mb -l us -c standard -b on --pap enforced gs://faq-mental-health-dialogflow
gsutil versioning set on gs://faq-mental-health-dialogflow

gsutil cp ./files/files_gold/covid_19/* gs://faq-covid-19-dialogflow
gsutil cp ./files/files_gold/mental-health/* gs://faq-mental-health-dialogflow



