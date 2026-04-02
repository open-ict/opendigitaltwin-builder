from fastapi import APIRouter

router = APIRouter(prefix="/telemetry", tags=["telemetry"])

@router.get("/{asset_uid}")
def get_telemetry(asset_uid: str):
    return [
        {"asset_uid": asset_uid, "temperature": 36.8, "humidity": 61.1, "weight": 18.4, "sound_index": 0.72},
        {"asset_uid": asset_uid, "temperature": 39.2, "humidity": 58.7, "weight": 9.4, "sound_index": 0.81}
    ]
