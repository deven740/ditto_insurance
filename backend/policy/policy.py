from fastapi import APIRouter, Body, Depends, status
from fastapi.responses import JSONResponse, Response
from .schema import HdfcLife, IciciLife, MaxLife, PolicyOut, FilterParams, Comment
from typing import Union
from .crud import (
    db_add_policy,
    db_get_policy,
    db_delete_policy,
    db_update_policy,
    db_add_comment,
    db_get_comments,
)
from database import get_db
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate

router = APIRouter(
    prefix="/policy",
    tags=["policy"],
)


@router.post("/add-policy")
def add_policy(
    db=Depends(get_db),
    policy: Union[HdfcLife, IciciLife, MaxLife] = Body(
        ..., discriminator="policy_type"
    ),
) -> JSONResponse:
    db_add_policy(db, policy)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"detail": "Policy added"},
    )


@router.get("/get-policy")
def get_policy(
    db=Depends(get_db), filters: FilterParams = Depends()
) -> Page[PolicyOut]:
    print(filters)
    data = db_get_policy(db, filters)
    return paginate(data)


@router.patch("/update-policy/{policy_id}")
def update_policy(policy_id: int, db=Depends(get_db)):
    db_update_policy(db, policy_id)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"detail": "Policy added"},
    )


@router.delete("/delete-policy/{policy_id}")
def delete_policy(policy_id: int, db=Depends(get_db)):
    db_delete_policy(db, policy_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/add-comment")
def add_comment(comment: Comment, db=Depends(get_db)):
    db_add_comment(db, comment)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"detail": "Comment added"},
    )


@router.get("/get-comments/{policy_id}")
def get_comments(policy_id: int, db=Depends(get_db)) -> list[Comment]:
    return db_get_comments(db, policy_id)
