import numpy as np

def calculate_kpis(df):
    
    df = df.copy()
    
    # CTR (Click Through Rate)
    df['CTR'] = np.where(df['Impressions'] > 0,
                         df['Clicks'] / df['Impressions'],
                         0)
    
    # CPC (Cost Per Click)
    df['CPC'] = np.where(df['Clicks'] > 0,
                         df['Cost'] / df['Clicks'],
                         0)
    
    # Conversion Rate
    df['Conversion_Rate'] = np.where(df['Clicks'] > 0,
                                    df['Conversions'] / df['Clicks'],
                                    0)
    
    # Cost per Conversion
    df['Cost_per_Conversion'] = np.where(df['Conversions'] > 0,
                                         df['Cost'] / df['Conversions'],
                                         np.nan)
    
    # Revenue per Click
    df['Revenue_per_Click'] = np.where(df['Clicks'] > 0,
                                      df['Sale_Amount'] / df['Clicks'],
                                      0)
    
    # ROI (Return on Investment)
    df['ROI'] = np.where(df['Cost'] > 0,
                         (df['Sale_Amount'] - df['Cost']) / df['Cost'],
                         np.nan)
    
    return df