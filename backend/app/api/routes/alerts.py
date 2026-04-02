from fastapi import APIRouter

router = APIRouter(prefix="/alerts", tags=["alerts"])

@router.get("")
def list_alerts():
    return [{"asset_uid":"hive-001","severity":"medium","message":"High hive temperature detected"}]
