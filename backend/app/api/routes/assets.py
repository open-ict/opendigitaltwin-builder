from fastapi import APIRouter

router = APIRouter(prefix="/assets", tags=["assets"])

@router.get("")
def list_assets():
    return [{"asset_uid":"hive-001","name":"Hive 001","asset_type":"beehive","metadata_json":{"location":"Santorini","template":"beehive-v1"}}]
