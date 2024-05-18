from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Dummy database to store user information

# CORS (Cross-Origin Resource Sharing) middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this to the origin of your React application or "*" to allow all origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Add other HTTP methods if needed
    allow_headers=["*"],
)
users_db = {}

# Model for user signup
class UserSignup(BaseModel):
    username: str
    password: str

# Model for user login
class UserLogin(BaseModel):
    username: str
    password: str

# Endpoint for user signup
@app.post("/signup/", tags=["Authentication"])
async def signup(user_data: UserSignup):
    """
    Register a new user.
    """
    if user_data.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    users_db[user_data.username] = user_data.password
    return {"message": "User signed up successfully"}

# Endpoint for user login
@app.post("/login/", tags=["Authentication"])
async def login(user_data: UserLogin):
    """
    Log in with an existing user.
    """
    if user_data.username not in users_db or users_db[user_data.username] != user_data.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"message": "Login successful"}

class IncidentData(BaseModel):
    date: str
    location: str
    casualties: str
    incident_type: str
    incident_report: str

@app.post("/submit_incident", tags=["report"])
async def submit_incident(incident_data: IncidentData):
    """
    Submit incident data.
    """
    # Here you can process the received data, like storing it in a database
    # or performing any other necessary actions
    return {"message": "Incident data received successfully"}

