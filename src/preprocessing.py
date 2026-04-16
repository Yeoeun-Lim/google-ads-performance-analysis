import pandas as pd
import numpy as np


# 텍스트 컬럼 정리
def clean_text_columns(df):
    text_cols = ['Device', 'Location', 'Campaign_Name', 'Keyword']
    
    for col in text_cols:
        df[col] = df[col].astype(str).str.lower().str.strip()
    
    return df


# 숫자 컬럼 정리 (Cost, Sale)
def clean_numeric_columns(df):
    # 숫자만 남기기
    df['Cost'] = df['Cost'].astype(str).str.replace(r'[^0-9.]', '', regex=True)
    df['Sale_Amount'] = df['Sale_Amount'].astype(str).str.replace(r'[^0-9.]', '', regex=True)
    
    # 숫자형 변환
    df['Cost'] = pd.to_numeric(df['Cost'], errors='coerce')
    df['Sale_Amount'] = pd.to_numeric(df['Sale_Amount'], errors='coerce')
    
    return df


# 날짜 정리
def clean_date(df):
    df['Ad_Date'] = pd.to_datetime(df['Ad_Date'], errors='coerce')
    return df


# 결측치 처리 (간단 버전)
def handle_missing_values(df):
    
    # 핵심 지표 결측 제거
    df = df.dropna(subset=['Clicks', 'Impressions'])
    
    # Cost, Sale은 0으로 대체 (비즈니스 가정)
    df['Cost'] = df['Cost'].fillna(0)
    df['Sale_Amount'] = df['Sale_Amount'].fillna(0)
    
    # Conversions, Leads도 0 처리
    df['Conversions'] = df['Conversions'].fillna(0)
    df['Leads'] = df['Leads'].fillna(0)
    
    return df


# 이상치 / 오류값 처리
def handle_invalid_values(df):
    
    # division 문제 방지
    df = df[df['Impressions'] > 0]
    df = df[df['Clicks'] >= 0]
    df = df[df['Conversions'] >= 0]
    
    return df


# 중복 제거
def remove_duplicates(df):
    df = df.drop_duplicates()
    return df


# 전체 파이프라인
def clean_data(df):
    
    df = df.copy()
    
    # 순서 중요
    df = clean_text_columns(df)
    df = clean_numeric_columns(df)
    df = clean_date(df)
    df = handle_missing_values(df)
    df = handle_invalid_values(df)
    df = remove_duplicates(df)
    
    return df