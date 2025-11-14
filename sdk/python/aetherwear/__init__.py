import requests
from typing import Optional, Dict, List
import json

class GeometricClient:
    """Official Geometric Mind Python Client"""
    
    def __init__(self, api_key: str, base_url: str = "http://localhost:8000"):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })
    
    def analyze(self, query: str, domain: str = "business", context: Optional[Dict] = None) -> Dict:
        """Analyze a decision using geometric intelligence"""
        payload = {
            "query": query,
            "domain": domain,
            "context": context or {}
        }
        
        response = self.session.post(f"{self.base_url}/v1/analyze", json=payload)
        response.raise_for_status()
        
        return response.json()
    
    def health(self) -> Dict:
        """Check API health"""
        response = self.session.get(f"{self.base_url}/v1/health")
        response.raise_for_status()
        return response.json()

# Example usage:
# client = GeometricClient(api_key="your_key")
# result = client.analyze("Should we cut R&D to boost profits?")
# print(result)
