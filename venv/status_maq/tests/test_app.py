import pytest
import pandas as pd
from datetime import datetime
from app import ARQUIVO

def test_data_saving():
    # Test if data is saved correctly to the CSV file
    test_data = {
        "Data e Hora": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "Turno": 1,
        "Líder": "Líder 1",
        "Pintura Máquina 1": "Rodando",
        "Pintura Máquina 2": "Parada"
    }
    
    # Create a DataFrame from the test data
    df_test = pd.DataFrame([test_data])
    
    # Save the test data to the CSV file
    df_test.to_csv(ARQUIVO, mode='a', header=not pd.io.common.file_exists(ARQUIVO), index=False)
    
    # Read the data back from the CSV file
    df_saved = pd.read_csv(ARQUIVO)
    
    # Check if the last entry matches the test data
    assert df_saved.iloc[-1].equals(df_test.iloc[0])

def test_csv_file_exists():
    # Test if the CSV file exists
    assert pd.io.common.file_exists(ARQUIVO)

def test_data_format():
    # Test if the data format in the CSV file is correct
    df = pd.read_csv(ARQUIVO)
    assert "Data e Hora" in df.columns
    assert "Turno" in df.columns
    assert "Líder" in df.columns

    # Check if the Data e Hora column is in the correct format
    try:
        pd.to_datetime(df["Data e Hora"], format="%d/%m/%Y %H:%M")
    except ValueError:
        assert False, "Data e Hora format is incorrect"