from sqlalchemy.orm import Session
from src.database import get_db
from src.controller import details_controller as controller
from src.schema.detail_schema import DetailBaseSchema, DetailInDBSchema

router_detail = APIRouter(prefix='/detail', tags=["detail"])


@router_detail.get('/')
def get_detail(db: Session = Depends(get_db)):
    return controller.get_detail(db)

@router_detail.post('/')
def create_details(detail: DetailBaseSchema, db: Session = Depends(get_db)):
    return detail
@router_detail.put("/{id}")
def update_detail(id: int, detail: DetailUpdateSchema, db: Session = Depends(get_db)):
    return controller.update_detail(id, detail, db)

@router_detail.delete('/{id}')
def delete_detail(id: int, db: Session = Depends(get_db)):
    return controller.delete_detail(id, db)
