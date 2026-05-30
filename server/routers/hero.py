import crud

from typing import Annotated

from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlmodel import Session

from database import get_session
from schemas import CreateHero, ReadHero, UpdateHero

router = APIRouter(prefix="/heroes", tags=["hero"])
SessionDep = Annotated[Session, Depends(get_session)]

@router.post("/", response_model=CreateHero)
def create(hero: CreateHero, session: SessionDep):
    return crud.create_hero(session, hero)

@router.get("/", response_model=list[ReadHero])
def read_all(session: SessionDep,offset: int = 0, limit: Annotated[int, Query(gt=0, le=100)] = 100):
    return crud.get_heros(session, offset, limit)

@router.get("/{hero_id}", response_model=ReadHero)
def read(session: SessionDep, hero_id: int):
    hero = crud.get_hero(session, hero_id)
    if not hero:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no hero with this id")
    return hero

@router.put("/{hero_id}", response_model=ReadHero)
def update(session: SessionDep, hero_id: int, hero_update: UpdateHero):
    updated_hero = crud.update_hero(session, hero_id, hero_update)
    if not updated_hero:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cannot update hero")
    return updated_hero

@router.delete("/{hero_id}")
def delete(session: SessionDep, hero_id: int):
    deleted_hero = crud.delete_hero(session, hero_id)
    if not deleted_hero:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cannot delete hero")
    
    return {"ok": "Hero deleted successfully"}