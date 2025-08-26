"""
API Utilities Module
Handles checking API availability and providing demo data
"""
import streamlit as st # <-- Import Streamlit
import logging
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

def is_api_available(service_name):
    """
    Check if an API service is available from Streamlit Secrets.
    
    Args:
        service_name (str): Name of the service key in st.secrets (e.g., 'gemini', 'openai')
        
    Returns:
        bool: True if API is available, False otherwise
    """
    try:
        # Check if the secret key exists and has a valid value
        if hasattr(st.secrets, service_name):
            api_key = getattr(st.secrets, service_name)
            # Check if the key is not empty and not a placeholder
            if api_key and api_key not in ["YOUR_" + service_name.upper() + "_API_KEY", "NOT_AVAILABLE"]:
                return True
        return False
    except Exception as e:
        logger.warning(f"Could not check Streamlit Secrets for {service_name}: {e}")
        return False

def get_demo_sanctions_data():
    """
    Get demo sanctions data for testing
    
    Returns:
        DataFrame: Demo sanctions data
    """
    try:
        # Create demo data
        demo_data = pd.DataFrame({
            'entity_id': ['ENT001', 'ENT002', 'ENT003'],
            'name': ['Demo Entity 1', 'Demo Entity 2', 'Demo Entity 3'],
            'country': ['North Korea', 'Iran', 'Syria'],
            'list_type': ['Sanctions List', 'Sanctions List', 'Sanctions List'],
            'added_date': ['2023-01-01', '2023-02-01', '2023-03-01']
        })
        
        logger.info("Using demo sanctions data")
        return demo_data
    except Exception as e:
        logger.error(f"Error creating demo sanctions data: {str(e)}")
        return pd.DataFrame()

def get_demo_tax_compliance_data():
    """
    Get demo tax compliance data for testing
    
    Returns:
        DataFrame: Demo tax compliance data
    """
    try:
        # Create demo data
        demo_data = pd.DataFrame({
            'tax_id': ['TAX001', 'TAX002', 'TAX003'],
            'entity_name': ['Demo Corp 1', 'Demo Corp 2', 'Demo Corp 3'],
            'compliance_status': ['Compliant', 'Non-compliant', 'Under Review'],
            'last_checked': ['2023-01-01', '2023-02-01', '2023-03-01']
        })
        
        logger.info("Using demo tax compliance data")
        return demo_data
    except Exception as e:
        logger.error(f"Error creating demo tax compliance data: {str(e)}")
        return pd.DataFrame()

def get_demo_bank_verification_data():
    """
    Get demo bank verification data for testing
    
    Returns:
        DataFrame: Demo bank verification data
    """
    try:
        # Create demo data
        demo_data = pd.DataFrame({
            'account_number': ['ACC001', 'ACC002', 'ACC003'],
            'bank_name': ['Demo Bank 1', 'Demo Bank 2', 'Demo Bank 3'],
            'verification_status': ['Verified', 'Not Verified', 'Pending'],
            'last_verified': ['2023-01-01', '2023-02-01', '2023-03-01']
        })
        
        logger.info("Using demo bank verification data")
        return demo_data
    except Exception as e:
        logger.error(f"Error creating demo bank verification data: {str(e)}")
        return pd.DataFrame()

def get_demo_identity_verification_data():
    """
    Get demo identity verification data for testing
    
    Returns:
        DataFrame: Demo identity verification data
    """
    try:
        # Create demo data
        demo_data = pd.DataFrame({
            'id_number': ['ID001', 'ID002', 'ID003'],
            'name': ['Demo Person 1', 'Demo Person 2', 'Demo Person 3'],
            'verification_status': ['Verified', 'Not Verified', 'Pending'],
            'last_verified': ['2023-01-01', '2023-02-01', '2023-03-01']
        })
        
        logger.info("Using demo identity verification data")
        return demo_data
    except Exception as e:
        logger.error(f"Error creating demo identity verification data: {str(e)}")
        return pd.DataFrame()