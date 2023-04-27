"""add readers_books

Revision ID: 778549dd616a
Revises: d7564e112fa3
Create Date: 2023-01-30 18:41:52.000705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '778549dd616a'
down_revision = 'd7564e112fa3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('readers_books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('reader_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
    sa.ForeignKeyConstraint(['reader_id'], ['readers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_readers_books_book_id'), 'readers_books', ['book_id'], unique=False)
    op.create_index(op.f('ix_readers_books_reader_id'), 'readers_books', ['reader_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_readers_books_reader_id'), table_name='readers_books')
    op.drop_index(op.f('ix_readers_books_book_id'), table_name='readers_books')
    op.drop_table('readers_books')
    # ### end Alembic commands ###