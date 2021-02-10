# 3rd party modules
from fastapi import APIRouter

# application modules
from src import DTO
from src.responses import CustomResponse

# 3rd party modules
from fastapi import HTTPException

# application modules
from src.utils import get_db_cursor


router = APIRouter(
    prefix="/summary",
    tags=["Summary"]
)


@router.get("/devices", response_model=DTO.GetDeviceCountOut, status_code=200)
def get_active_device_count():
    cursor = get_db_cursor()
    sql_query = """SELECT COUNT(1) AS DeviceCount FROM Devices"""
    device_count = None
    try:
        with cursor:
            result = cursor.execute(sql_query)
            device_count = result.fetchone()
    except Exception as e:
        message = "Cannot get device count"
        raise HTTPException(detail=message, status_code=500)
    return CustomResponse(content={"deviceCount": device_count.DeviceCount}, status_code=200)

@router.get("/samples", response_model=DTO.GetSampleCountOut, status_code=200)
def get_sample_count():
    cursor = get_db_cursor()
    sql_query = """SELECT COUNT(1) AS SampleCount FROM Samples"""
    sample_count = None
    try:
        with cursor:
            result = cursor.execute(sql_query)
            sample_count = result.fetchone()
    except Exception as e:
        message = "Cannot get sample count"
        raise HTTPException(detail=message, status_code=500)
    return CustomResponse(content={"sampleCount": sample_count.SampleCount}, status_code=200)

@router.get("/labels", response_model=DTO.GetLabelCountOut, status_code=200)
def get_label_count():
    cursor = get_db_cursor()
    sql_query = """SELECT COUNT(1) AS LabelCount FROM Labels WHERE IsActive = 1"""
    label_count = None
    try:
        with cursor:
            result = cursor.execute(sql_query)
            label_count = result.fetchone()
    except Exception as e:
        message = "Cannot get label count"
        raise HTTPException(detail=message, status_code=500)
    return CustomResponse(content={"labelCount": label_count.LabelCount}, status_code=200)

@router.get("/speechAPIs", response_model=DTO.GetSpeechAPICountOut, status_code=200)
def get_label_count():
    cursor = get_db_cursor()
    sql_query = """SELECT COUNT(1) AS SpeecAPICount FROM SpeechAPI WHERE IsActive = 1"""
    speech_api_count = None
    try:
        with cursor:
            result = cursor.execute(sql_query)
            speech_api_count = result.fetchone()
    except Exception as e:
        message = "Cannot get speech api count"
        raise HTTPException(detail=message, status_code=500)
    return CustomResponse(content={"speechAPICount": speech_api_count.SpeecAPICount}, status_code=200)

@router.get("/SampleSubmissionTrend", status_code=200)
def get_sample_submission_trend():
    cursor = get_db_cursor()
    sql_query = """SELECT CAST(CreatedAt AS Date) AS Date, COUNT(1) AS SubmissionCount
                FROM Samples
                GROUP BY CAST(CreatedAt AS Date)"""
    try:
        with cursor:
            result = cursor.execute(sql_query)
            sample_submission_trend = result.fetchall()
    except Exception as e:
        message = "Cannot get sample submission trend"
        raise HTTPException(detail=message, status_code=500)
    result_list = []
    for row in sample_submission_trend:
        result_list.append({"submissionDate": row.Date, "submissionCount": row.SubmissionCount})
    return CustomResponse(content={"sampleSubmissionTrend": result_list}, status_code=200)
