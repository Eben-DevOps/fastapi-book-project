from fastapi import APIRouter, Depends
from api.routes.books import router as books_router
from api.dependencies import get_db  # Example dependency

# Create the main API router
api_router = APIRouter(prefix="/api", tags=["api"])

# Include the books router
api_router.include_router(books_router, prefix="/books", tags=["books"])

# Health check endpoint
@api_router.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok"}
