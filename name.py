import requests
import streamlit as st
import pandas as pd

def make_request(url, params=None):
    response = requests.get(url, params=params)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        response = None
    else:
        response = response.json()
    return response

def get_name_by_decade(name):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{name}"
    decade_data = make_request(url = url)
    if not decade_data:
        return {}
    dict_decades = {}
    for data in decade_data[0]['res']:
        decade = data['periodo']
        ammount = data['frequencia']
        dict_decades[decade] = ammount
    return dict_decades

def main():
    st.title("Web App Nomes")
    st.write("Dados do IBGE (fonte: https://servicodados.ibge.gov.br/api/docs/nomes?versao=2)")
    name = st.text_input('Consulte um nome:')
    if not name:
        st.stop()
        
    dict_decades = get_name_by_decade(name)
    if not dict_decades:
        st.warning("Nenhum dado encontrado para o nome informado.")
        st.stop()
    
    df = pd.DataFrame.from_dict(dict_decades, orient='index')
    col1, col2 = st.columns([0.3, 0.7])
    with col1:
        st.write("Distribuição por décadas:")
        st.dataframe(df)
    with col2:
        st.write('Evolução no Tempo')
        st.line_chart(df)
        
if __name__ == "__main__":
    main()

