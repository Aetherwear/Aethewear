#!/bin/bash

echo "🚀 Deploying Geometric Mind API..."

# Create data directory
mkdir -p data

# Copy environment file
if [ ! -f .env ]; then
    cp .env.example .env
    echo "⚠️  Please edit .env file with your API keys"
fi

# Build and start services
docker-compose up -d

echo "✅ Geometric Mind API deployed!"
echo "📊 API URL: http://localhost:8000"
echo "📚 Docs: http://localhost:8000/docs"
echo "❤️  Health: http://localhost:8000/health"

# Wait for service to be ready
sleep 5

# Test the API
curl -f http://localhost:8000/health && echo "🎉 Deployment successful!" || echo "❌ Deployment failed"
