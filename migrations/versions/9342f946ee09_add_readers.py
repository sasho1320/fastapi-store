"""add readers

Revision ID: 9342f946ee09
Revises: 3e1cb39c0c2a
Create Date: 2023-05-02 21:39:52.516428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9342f946ee09'
down_revision = '3e1cb39c0c2a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('pages', sa.Integer(), nullable=True))
    op.add_column('books', sa.Column('reader_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'books', 'readers', ['reader_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'books', type_='foreignkey')
    op.drop_column('books', 'reader_id')
    op.drop_column('books', 'pages')
    # ### end Alembic commands ###
