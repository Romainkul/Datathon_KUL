import polars as pl
df = pl.read_parquet("preprocessed_df.parquet")
print(df.head())


df_selected = df.filter(pl.col("french_text") != "").select(["improved_french_text","topics_french_text","extracted_location_french", "sentiment_french","french_embedding"])
#print(df_selected.head())
print(df_selected[2,"sentiment_french"])