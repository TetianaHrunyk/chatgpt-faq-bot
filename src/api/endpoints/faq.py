from fastapi import Depends, APIRouter

from src.api.models.models import FAQRequest, FAQResponse
from src.api.endpoints.utils import verify_token
from src.chat.service import ChatService

CHAT_SERVICE = ChatService()

faq_router = APIRouter(prefix="/faq")


@faq_router.post("/", dependencies=[Depends(verify_token)])
async def get_answer(request: FAQRequest) -> FAQResponse:
    response = CHAT_SERVICE.query(request.query)
    return FAQResponse(query=request.query, response=response)
