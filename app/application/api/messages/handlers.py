from application.api.messages.schemas import CreateChatRequestSchema, CreateChatResponseSchema
from application.api.schemas import ErrorSchema
from domain.entities.messages import Chat
from domain.exceptions.base import ApplicationException
from fastapi import APIRouter, Depends, HTTPException, status
from logic.commands.messages import CreateChatCommand
from logic.init import init_container
from logic.mediator import Mediator
from punq import Container

router = APIRouter(tags=["chat"])


@router.post(
    "/",
    response_model=CreateChatResponseSchema,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": CreateChatResponseSchema},
        status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
    },
)
async def create_chat_handler(schema: CreateChatRequestSchema, container: Container = Depends(init_container)):
    """
    Create new chat
    """
    mediator: Mediator = container.resolve(Mediator)
    try:
        chat: Chat
        chat, *_ = await mediator.handle_command(CreateChatCommand(title=schema.title))
    except ApplicationException as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"error": exception.message})

    return CreateChatResponseSchema.from_entity(chat)
