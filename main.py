from fastapi import FastAPI

app = FastAPI(
    title="TestTrack API",
    description="QA test case management — free alternative to TestRail",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "TestTrack API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}