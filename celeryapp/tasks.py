# app/tasks.py
import pandas as pd
from celery import shared_task
from .models import Product

@shared_task
def import_excel_data(file_path):
    try:
        data = pd.read_excel(file_path)
        for _, row in data.iterrows():
            Product.objects.update_or_create(
                name=row['name'],
                defaults={
                    'description': row['description'],
                    'price': row['price'],
                }
            )
        return f"Imported {len(data)} products successfully."
    except Exception as e:
        return f"Error importing data: {str(e)}"
