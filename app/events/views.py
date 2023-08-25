from loguru import logger
from fastapi import Depends, APIRouter, HTTPException
from app.core.auth import verify_token
from sqlalchemy.orm import Session
from app.core.db.session import get_db
from app.events.models import Event as EventModel
from app.events.schema import EventSchema


router = APIRouter(dependencies=[Depends(verify_token)])


@router.get("/events", status_code=200)
async def get_events(db: Session = Depends(get_db)):

    """
    gets all the events listed in the database.

    Returns:
        list: An array of events' objects.
    """

    return db.query(EventModel).all()


@router.post("/events", status_code=201)
async def add_event(payload: EventSchema, db: Session = Depends(get_db)):

    """
    Add event in the database.

    Returns:
        Object: same payload which was sent with 201 status code on success.
    """

    db_events = EventModel(
        name=payload.name,
        description=payload.description,
    )

    db.add(db_events)
    db.commit()

    logger.success("Added a event.")
    return payload


@router.put("/events/{event_id}", status_code=201)
async def update_event(
    event_id: int, payload: EventSchema, db: Session = Depends(get_db)
):

    """
    Updates the event object in db

    Raises:
        HTTPException: 404 if event id is not found in the db

    Returns:
        object: updated event object with 201 status code
    """

    event = db.query(EventModel).filter(EventModel.id == event_id).first()
    if not event:
        desc = "Event not found"
        logger.error(desc)
        raise HTTPException(status_code=404, detail=desc)

    event.name = payload.name
    event.description = payload.description
    db.commit()

    logger.success("Updated a event.")
    return event


@router.delete("/events/{event_id}", status_code=204)
async def delete_event(event_id: int, db: Session = Depends(get_db)):
    """
    Deletes the event object from db

    Raises:
        HTTPException: 404 if event id is not found in the db

    Returns:
        Object: Deleted true with 204 status code
    """

    event = db.query(EventModel).filter(EventModel.id == event_id).first()
    if not event:
        desc = "Event not found"
        logger.error(desc)
        raise HTTPException(status_code=404, detail=desc)
    db.delete(event)
    db.commit()

    logger.success("Deleted a event.")

    return {"Deleted": True}
