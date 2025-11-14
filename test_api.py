import requests
import json

def test_geometric_api():
    """Test the Geometric Mind API"""
    base_url = "http://localhost:8000"
    
    # Test health endpoint
    print("🧪 Testing health endpoint...")
    health_response = requests.get(f"{base_url}/v1/health")
    print(f"Health: {health_response.json()}")
    
    # Test analysis endpoint
    print("\n🧪 Testing analysis endpoint...")
    test_cases = [
        {
            "query": "Should we cut our R&D budget to increase quarterly profits?",
            "domain": "business"
        },
        {
            "query": "Should I quit my job to start a business?",
            "domain": "personal" 
        },
        {
            "query": "Should we use cheaper materials to reduce costs?",
            "domain": "business"
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📊 Test Case {i}: {test_case['query']}")
        
        response = requests.post(
            f"{base_url}/v1/analyze",
            json=test_case
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Decision: {result['decision']}")
            print(f"📈 Confidence: {result['confidence']:.2f}")
            print(f"⚠️  Risks: {', '.join(result['risks'])}")
            print(f"💡 Recommendations: {', '.join(result['recommendations'])}")
        else:
            print(f"❌ Failed: {response.status_code} - {response.text}")

if __name__ == "__main__":
    test_geometric_api()
