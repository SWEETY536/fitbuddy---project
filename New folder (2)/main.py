import os
import google.generativeai as genai
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from dotenv import load_dotenv

import models
from database import SessionLocal, engine, Base

load_dotenv()

# Initialize Database
Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-pro')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_plan(name, age, weight, goal, intensity, feedback=""):
    prompt = f"Create a 7-day workout plan for {name}, age {age}, weight {weight}kg. Goal: {goal}. Intensity: {intensity}."
    if feedback:
        prompt += f" Ensure you incorporate this feedback: {feedback}."
    
    if not api_key:
        return "Gemini API key not configured. Mock 7-day workout plan."
    
    response = model.generate_content(prompt)
    return response.text

def generate_tip(goal):
    if not api_key:
        return "Mock nutrition tip: Eat protein."
    response = model.generate_content(f"Give a short 1-sentence nutrition and recovery tip for someone whose goal is {goal}.")
    return response.text

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
async def create_plan(
    request: Request,
    name: str = Form(...),
    age: int = Form(...),
    weight: int = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...),
    db: Session = Depends(get_db)
):
    plan = generate_plan(name, age, weight, goal, intensity)
    tip = generate_tip(goal)
    
    user = models.UserProfile(name=name, age=age, weight=weight, goal=goal, intensity=intensity, workout_plan=plan, nutrition_tip=tip)
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return templates.TemplateResponse("plan.html", {"request": request, "user": user})

@app.post("/feedback/{user_id}", response_class=HTMLResponse)
async def submit_feedback(
    request: Request,
    user_id: int,
    feedback: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(models.UserProfile).filter(models.UserProfile.id == user_id).first()
    if user:
        new_plan = generate_plan(user.name, user.age, user.weight, user.goal, user.intensity, feedback)
        user.workout_plan = new_plan
        db.commit()
        db.refresh(user)
    return templates.TemplateResponse("plan.html", {"request": request, "user": user})