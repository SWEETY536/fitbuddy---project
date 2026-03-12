import uvicorn

if __name__ == "__main__":
    print("Starting FitBuddy Application...")
    print("Access the app at: http://127.0.0.1:8000")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
#To run the application, execute this script. It will start the FastAPI server and you can access the 
# app in your web browser at the provided URL.