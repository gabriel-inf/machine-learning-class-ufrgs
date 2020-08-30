import pandas as pd

def import_data(file_name: str) -> pd.DataFrame:
    return pd.read_csv(file_name, sep=" ")
    


if __name__ == "__main__":


    new_instance = {
        "previsao": "chuva", 
        "temperatura": "moderado", 
        "umidade": "alta", 
        "vento": "não"
    }

    

    produtories = {}


    df = import_data("resources/data_feijoada_parmediana.csv")
    print(df.head())

    print("\nTest instance:")
    print(new_instance)

    p_class = {}



    # print("\nProbabilities of being feijoada/parmegiana:")
    # print(p_feijoada_priory, p_parmegiana_priory)


    attributes = df.columns
    attributes = list(attributes[0:4])

    classes = df["prato"].unique()

    for classe in classes:
        p_class[classe] = len(df[df["prato"]==classe]) / len(df)


    for classe in classes:
        total = len(df)
        total_class =  len(df[df["prato"]==classe])
        prob_class = total_class/total

        print()
        print(classe)
        print("{}: {}/{} = {}".format(classe, total_class,total, prob_class))

        produtories[classe] = 1

        
        for attribute in attributes:

            df_class = df[df["prato"] == classe]

            count_test_attribute_given_class = len(df_class[df_class[attribute] == new_instance[attribute]])
            p_attribute = count_test_attribute_given_class / total_class
            value = new_instance[attribute]
            print ("{}({})/{}, {}/{} = {}".format(attribute, value, classe, count_test_attribute_given_class, total_class, p_attribute))

            produtories[classe] *= p_attribute
        
        print("-> Produtório ({}): {}".format(classe, produtories[classe]))

    posteriori = {}
    for classe in classes:
        posteriori[classe] = produtories[classe] * p_class[classe]

    

    print("\nProdutório classe * Estimativa a priori:")
    for classe in classes:
        print("{} ({} * {}): {:.4f}".format(classe, produtories[classe], p_class[classe] , posteriori[classe]))