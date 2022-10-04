def get_data_from_html_table(cols):
    name = cols[1].text.strip()
    protein = float(cols[2].text.strip() if cols[2].text.strip() != "" else 0)
    fat = float(cols[3].text.strip() if cols[3].text.strip() != "" else 0)
    carb = float(cols[4].text.strip() if cols[4].text.strip() != "" else 0)
    kal = float(cols[5].text.strip() if cols[5].text.strip() != "" else 0)
    return name, protein, fat, carb, kal
