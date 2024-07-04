from sqlalchemy.orm import Session
from sqlalchemy import func
from .models import PolicyModel, CommentModel
from .schema import HdfcLife, IciciLife, MaxLife, FilterParams, PolicyUpdate, Comment
from typing import Union


def db_add_policy(db: Session, data: Union[HdfcLife, IciciLife, MaxLife]):
    policy = PolicyModel(**data.dict())
    db.add(policy)
    db.commit()


def db_get_policy(db: Session, filters: FilterParams):
    filter_params = filters.dict(exclude_none=True)
    query = db.query(PolicyModel)
    for key, value in filter_params.items():
        if key == "created_at":
            query = query.filter(func.date(PolicyModel.created_at) == value)
        else:
            query = query.filter(getattr(PolicyModel, key) == value)
    return query


def db_delete_policy(db: Session, policy_id: int):
    result = db.query(PolicyModel).get(policy_id)
    db.delete(result)
    db.commit()


def db_update_policy(
    db: Session, policy_id: int, policy_update: PolicyUpdate
) -> PolicyModel:
    policy = db.query(PolicyModel).get(policy_id)
    for key, value in policy_update.dict(exclude_unset=True).items():
        setattr(policy, key, value)
    db.add(policy)
    db.commit()
    db.refresh(policy)
    return policy


def db_add_comment(db: Session, comment: Comment):
    comment = CommentModel(**comment.dict())
    db.add(comment)
    db.commit()


def db_get_comments(db: Session, policy_id: int):
    return db.query(CommentModel).filter(CommentModel.policy_id == policy_id).all()
