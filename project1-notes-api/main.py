from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app=FastAPI()

@app.get("/")
def home():
    return{"message":"hello"}

class Note(BaseModel):
    id: int
    title: str
    content: str
notes_db=[]

@app.post("/notes/")
def create_note(title: str, content: str):
    note_id=len(notes_db)+1
    note = Note(
        id=note_id,
        title=title,
        content=content
    )

    notes_db.append(note)

    return {"message" :"Note Created "}

@app.get("/notes/")
def get_notes():
    return notes_db

@app.get("/notes{note_id}")
def get_note(note_id: int):
    for note in notes_db:
        if note.id==note_id:
            return note
    return{"error":"Note not found"}