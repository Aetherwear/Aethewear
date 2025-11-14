from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict
import uuid
import time
from datetime import datetime

# Geometric Mind Core Engine
from geometric_core import GeometricEngine, GeometricResult

app = FastAPI(title="Geometric Mind API", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response Models
class AnalysisRequest(BaseModel):
    query: str
    domain: str = "business"
    context: Optional[Dict] = None

class AnalysisResponse(BaseModel):
    analysis_id: str
    query: str
    decision: str
    confidence: float
    risks: List[str]
    recommendations: List[str]
    geometric_balance: Dict[str, float]
    processing_time: float
    timestamp: str

class HealthResponse(BaseModel):
    status: str
    version: str
    timestamp: str
    uptime: float

# Initialize Engine
engine = GeometricEngine()

@app.post("/v1/analyze", response_model=AnalysisResponse)
async def analyze_decision(request: AnalysisRequest):
    """Complete geometric analysis endpoint"""
    start_time = time.time()
    
    try:
        # Process through all 6 geometric layers
        result = await engine.process(
            query=request.query,
            domain=request.domain,
            context=request.context or {}
        )
        
        processing_time = time.time() - start_time
        
        return AnalysisResponse(
            analysis_id=str(uuid.uuid4()),
            query=result.query,
            decision=result.final_decision,
            confidence=result.confidence,
            risks=result.risks,
            recommendations=result.recommendations,
            geometric_balance=result.geometric_balance,
            processing_time=processing_time,
            timestamp=datetime.utcnow().isoformat()
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.get("/v1/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="healthy",
        version="2.0.0",
        timestamp=datetime.utcnow().isoformat(),
        uptime=time.time() - app.startup_time
    )

@app.get("/")
async def root():
    return {"message": "Geometric Mind API", "version": "2.0.0"}

# Store startup time
app.startup_time = time.time()
