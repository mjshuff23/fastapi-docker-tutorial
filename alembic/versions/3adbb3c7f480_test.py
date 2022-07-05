"""test

Revision ID: 3adbb3c7f480
Revises:
Create Date: 2022-07-05 14:19:14.044996

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "3adbb3c7f480"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=True),
        sa.Column("last_name", sa.String(), nullable=True),
        sa.Column("age", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_users_id"), table_name="users")
    op.drop_table("users")
    # ### end Alembic commands ###